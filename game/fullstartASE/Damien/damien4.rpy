label damien_boardgame:
    show bg HomeD with dissolve
    "You recline against your couch and flip through the TV channels, searching for something to watch."
    "It's a warm, lazy evening, and all you can think about is relaxing on your sofa with a can of soda and bowl full of snacks until you pass out."
    $ clothes = "underwear"
    show chelsea embarrassed with dissolve
    pcname "This is how weekends are meant to be. Mmm..."
    hide chelsea with dissolve
    "As you settle on a station playing a classic 90s movie, your phone lights up and buzzes from the coffee table."
    "With a groan, you stretch your arm out and pull it toward you. Hopefully it's not anyone trying to get you to cover their shift..."

    call screen TextingScene("Damien",
    [
        TextMessage("Hey, [pcname]! Are you busy right now?"),
        TextMessage("Not really, just watching TV. What's up?", sender = False),
        TextMessage("Do you mind if I come over? I got this new boardgame and I'm dying to try it out!"),
        TextMessage("Sure, I'm just hanging out for the night.", sender = False),
        TextMessage("Awesome, I'll be right over!")
    ])

    if club == "track":
        show chelsea embarrassed with dissolve
        "With a sigh, you stand up and stretch. It's been a while since you've played any board games, so maybe this could be fun."
    elif club == "cheer":
        show chelsea embarrassed with dissolve
        "You lean back against the couch and sigh. You haven't played board games since you were a kid, but if Damien is this excited about it, maybe you can give it a try."
    elif club == "yearbook":
        show chelsea confused with dissolve
        "You bite your lip and ponder what sort of board game Damien has. The kids in your club play all sorts of odd strategy games; did he get one of those?"
        show chelsea embarrassed
        "It might be kind of fun to try one out, especially after seeing how much fun the kids in your club have with it."
    show chelsea sad
    "It's not like there's anything good on TV anyways."
    scene black with fade
    $ clothes, hair = casualwear
    "You head into your room to get changed before Damien arrives."
    scene bg HomeD with fade
    "Halfway through your movie, you hear a knock at the door."
    $ damienAttire(2)
    show Damien Happy at right with dissolve
    show chelsea happy with dissolve
    "Damien grins as you swing the door open, a childlike excitement glimmering in his eyes. He holds up a square game box still covered in cellophane."
    show Damien Laugh
    show chelsea embarrassed
    D "I got the goods."
    scene black with fade
    "You step aside to let Damien in. He immediately beelines for the coffee table, pushing your snacks aside and unwrapping his game box."
    scene bg HomeD with fade
    "You peer over his shoulder and squint at the title."
    show chelsea confused at right, moveSprite(0.7, 0.7, 0.0) with dissolve
    pcname "'Negotiations'...?"
    show Damien Laugh with dissolve
    D "Yeah! It's a strategy game where everyone plays as world leaders and we have to trade and negotiate imports and exports while random world events can occur, like natural disasters, or political disagreements and stuff."
    show Damien Happy
    show chelsea blank
    D "And then you have to decide whether to go to war, nuke other players, so on and so forth. Whoever is the richest, or the last one standing, wins."
    show Damien Laugh
    D "I've had it on my wishlist forever, and I finally had some extra money this month to buy it!"
    show Damien Happy
    D "Well? What do you think?"
    menu damien_boardgameinterest:
        "This sounds like fun!" if True:
            $ corruption -= 1
            show chelsea laugh
            $ damienconfidence += 1
            show Damien Shocked
            if club == "track":
                show chelsea laugh
                pcname "War and nukes? Count me in! This sounds better than I thought it would be."
            elif club == "cheer":
                show chelsea happy
                pcname "Um, it sounds kind of complicated, but also {i}way{/i} better than I thought it would. Let's give it a try."
            elif club == "yearbook":
                show chelsea embarrassed
                pcname "T-That sounds like fun! I've never played a game like that before..."
            show Damien Laugh
            show chelsea embarrassed
            D "Really? That's great! I was worried you might be put off by it..."
            D "Let's get it set up!"
            show chelsea happy
            pcname "Sounds good; I'll get some drinks."
        "This is the lamest game I've ever heard of." if True:
            $ corruption += 1
            $ damienconfidence -=1
            if club == "track":
                show chelsea laugh
                show Damien Sad
                pcname "This is the lamest game I've ever heard of."
                show chelsea confused
                pcname "Isn't it too complicated to be a board game? Like, how are you supposed to do all of that with some paper cards? I'd rather play a video game."
            elif club == "cheer":
                show chelsea laugh
                show Damien Sad
                pcname "This is the lamest game I've ever heard of."
                show chelsea happy
                pcname "I thought we were going to play, like, {i}normal{/i} board games. Not... whatever this is."
            elif club == "yearbook":
                show chelsea embarrassed
                show Damien Sad
                pcname "I-It... It sounds kind of lame..."
            show Damien Worry
            show chelsea embarrassed
            D "O-Oh... Yeah, I guess it does sound kind of lame... I was just really looking forward to it, is all..."
            pcname "We can still play it. You brought it all the way here, after all."
            show Damien Shocked
            show chelsea blank
            D "A-Are you sure? I mean, if you really don't want to play, we can do something else..."
            show Damien Sad
            show chelsea sad
            "Although he offers an alternative, Damien's fingers brush the board game's box sadly, his gaze filled with enough disappointment that anymore teasing would feel like kicking an abandoned puppy."
            show chelsea laugh
            show Damien Neutral
            pcname "Yeah, I'm sure. Go ahead and set it up."
            show chelsea happy
            "He nods, his cheeks tinged pink with embarrassment, and quickly unwraps the game."
    scene bg HomeD with fade
    "You head into the kitchen for drinks and some more snacks. By the time you return, the game is mostly set up, with the exception of Damien punching out tiny coins from a sheet of cardboard."
    "You sit down beside him and pick up an extra sheet, helping him."
    show chelsea confused at center, moveSprite(0.8, 0.8, 0.0) with dissolve
    pcname "So how do we play this game exactly?"
    show chelsea blank
    "Damien finishes popping out his sheet and spills the coins into a makeshift treasure chest."
    show Damien Blank with dissolve
    pause 1.0
    show Damien Neutral
    D "Er, that's a great question."
    show Damien Blank
    "He picks up a thick booklet from inside of the game's lid and starts to flip through it."
    show chelsea shocked
    pcname "Are all of those the {i}rules?!{/i}"
    show Damien Neutral
    show chelsea sad
    D "Huh? Oh, ah, yeah. Games like this can get complicated, so there's a lot in here..."
    show Damien Laugh
    show chelsea blank
    D "Don't worry! I've watched a couple of videos on how the game is played, so the rules are more of a refresher than anything."
    show Damien Sad
    "Despite saying that, Damien's eyebrows crease with confusion as he flips through the booklet, occasionally backtracking and mumbling to himself."
    show chelsea sad
    "This is definitely more complicated than you thought it would be."
    if mattsubmissive == True:
        show chelsea confused
        show Damien Shocked
        "As Damien scrambles to research the rules as thoroughly as possible, you hear a knock at the door."
        show Damien Blank
        "Damien looks up in confusion."
        show Damien Neutral
        D "Did you order food?"
        show chelsea blank
        show Damien Blank
        pcname "Er, no, not yet."
        scene black with fade
        "You rise from your stiff position on the floor and head to the front door. You aren't expecting any packages and your rent isn't due yet, so who could be bothering you at this hour?"
        "Peering through the peephole, you see a familiar face... Matt."
        "You glance back at Damien, your heart pounding as you begin to panic."
        "Thoughts racing - What's Matt doing here? What if Damien sees him? What will Matt say? What will Matt expect you to {i}do{/i}? - you quickly open the door and step out."
        scene bg CityD
        show chelsea blank at left
        show Matt Casual Question
        with fade
        m "Um...?"
        show chelsea embarrassed
        pause 1.0
        hide chelsea with dissolve
        "Stifling a giddy giggle at Matt's confusion, you hiss a quick {i}shhh{/i} and take a few steps down the hallway."
        show Matt Casual Smirk
        pause 1.0
        scene bg HomeD with fade
        "Matt's expression quickly melts from confusion to understanding."
        show Matt Casual Question at center, moveSprite(0.8, 0.8, 0.0) with dissolve
        m "Do you have a visitor?"
        if defymatt:
            show Matt Casual Blank
            if club == "track":
                show chelsea angry with dissolve
                pcname "That's none of your business."
            elif club == "cheer":
                show chelsea angry with dissolve
                pcname "So what if I do?"
            elif club == "yearbook":
                show chelsea sad with dissolve
                pcname "No, no, I just... Um..."
            "He puts his hand on the wall, just above your shoulder, and leans in close."
            show chelsea sad
            show Matt Casual Angry
            m "I thought you understood how this works by now..."
        elif True:
            show chelsea embarrassed with dissolve
            show Matt Casual Pleased
            if club == "track":
                pcname "Yes, but..."
            elif club == "cheer":
                pcname "Kinda, yeah..."
            elif club == "yearbook":
                pcname "Um, I... I guess...?"
            show Matt Casual Happy
            show chelsea sad
            "With a dark chuckle, he puts his hand on the wall just above your shoulder and leans in close."
            show Matt Casual Smirk
            m "Is that so...?"
        show Matt Casual Smirk
        m "Should we go inside so I can say hi?"
        show chelsea shocked
        "You shake your head frantically as panic weighs down on your chest, making it hard to breathe."
        show chelsea sad
        pcname "Matt, no, please..."
        if defymatt:
            m "Oh, this is good."
        elif True:
            show Matt Casual Blank
            "His eyes narrow."
        show Matt Casual Question
        show chelsea embarrassed
        m "So it's a guy then? You're fucking some other guy?"
        "You shake your head - not in denial of his words, but to try to ward off the confrontation you know is coming."
        show Matt Casual Smirk
        m "I knew you were a fucking slut, but..."
        show Matt Casual Pleased
        show chelsea blank
        "Suddenly, his expression changes. The rising fury leaves his eyes, replaced by... Amusement?"
        show Matt Casual Happy
        show chelsea sad
        m "No, this is good..."
        show Matt Casual Pleased at center, moveSprite(0.8, 0.9, 0.3)
        show chelsea blank
        "He takes a step back and you can almost breathe again."
        show Matt Casual Smirk
        m "Who is he? What's his name?"
        "You answer, almost without thinking."
        show chelsea blank
        show Matt Casual Question
        pcname "Damien, he--"
        show chelsea shocked
        m "That {i}loser{/i} from school? Are you serious?"
        show Matt Casual Happy at right, moveSprite(0.9, 1.0, 0.3)
        show chelsea blank
        "He laughs, taking another step back from you."
        if defymatt:
            show chelsea angry
            show Matt Casual Question
            pcname "He's not a loser!"
        elif True:
            show chelsea embarrassed
            show Matt Casual Question
            pcname "He... he's sweet."
        show chelsea blank
        show Matt Casual Happy
        m "Whatever. This is {i}perfect{/i}."
        if defymatt:
            show chelsea angry
            show Matt Casual Smirk
            if club == "track":
                pcname "Matt, just leave him alone."
            elif club == "cheer":
                pcname "No, you can do what you want to me, but leave him alone."
            elif club == "yearbook":
                show chelsea sad
                pcname "N-no, just... Just leave him alone..."
        elif True:
            show chelsea sad
            show Matt Casual Smirk
            if club == "track":
                pcname "Matt, please, leave him alone."
            elif club == "cheer":
                pcname "No, please, Matt. Do what you want with me, but leave him out of this."
            elif club == "yearbook":
                pcname "N-no, please! Please just... just leave him alone."
        show chelsea sad
        "Smiling cruelly, he begins nodding."
        show Matt Casual Pleased
        m "Oh, don't worry. I'll leave {i}him{/i} alone."
        show chelsea shocked
        show Matt Casual Smirk at moveSprite(1.0, 0.65, 0.4)
        "You gasp as he steps in close to you again, his nose nearly touching yours."
        show Matt Casual Pleased
        show chelsea sad
        m "I'll leave now, but text me when he leaves tonight."
        $ damienNTR = True
        show Matt Casual Smirk at moveSprite(0.65, 0.8, 0.3)
        "As Matt steps back, you find yourself nodding. Anything to make him go away without a fight."
        hide Matt with dissolve
        show chelsea embarrassed
        "With a smug smirk, Matt turns and walks away. Almost instantly, the weight on your chest is lifted."
        scene black with fade
        "After a few deep breaths, you duck back inside."
        scene bg HomeD
        show Damien Worry
        with fade
        "Damien glances up from the booklet, concerned."
        show Damien Neutral
        D "Is everything okay?"
        show chelsea laugh at center, moveSprite(0.8, 0.8, 0.0) with dissolve
        show Damien Blank
        pcname "Yeah, it was just... Someone looking for their dog."
        show Damien Neutral
        show chelsea embarrassed
        D "There's a lost dog? Do you think we should help look for it?"
        show Damien Sad
        "Your heart nearly melts at his concern."
        show Damien Shocked
        pcname "No, um... They got a call while I was talking to them. They found it."
        show Damien Happy
        "He smiles, clearly relieved."
        show chelsea blank
        show Damien Neutral
        D "Well, I think I understand all the rules, but..."
        show Damien Sad
        "He sighs."
        show Damien Worry
        show chelsea sad
        D "It's too much to try to explain at once."
    elif True:
        "After a few minutes of flipping through the booklet, Damien sets it down with a sigh."
        show Damien Worry
        D "This is going to be too much to explain at once, I think..."
    show Damien Happy
    show chelsea shocked
    D "Ah, you know what, let's just try to learn as we go. I'll help guide you through it."
    show chelsea confused
    show Damien Happy
    "Based on the look on his face, you aren't sure even Damien knows exactly how the game is played."
    show chelsea embarrassed
    pcname "If you say so..."
    "Damien gives you a hopeful smile and deals out the first set of cards."
    scene bg HomeD with fade
    "It's three games in, but you're finally getting the hang of it: it feels like you are, anyway."
    show chelsea blank at center, moveSprite(0.8, 0.8, 0.0) with dissolve
    "Damien jots down numbers on a spare notepad, counting up the amount of money each of you has gained and lost over the course of your most recent game."
    show chelsea sad
    "It's perhaps the most boring aspect; having to wait for him to do math and see who the winner is."
    show Damien Neutral with dissolve
    show chelsea blank
    D "Carry the two... Then we count for your nukes... You nuked five countries, right?"
    show Damien Blank
    pcname "Six."
    show Damien Worry
    show chelsea embarrassed
    D "Oh, right, you got Croatia. Poor eastern Europe... You really took them out."
    show Damien Blank
    show chelsea blank
    "Damien finishes writing down a final score before setting the notepad down on the coffee table."
    show Damien Laugh
    show chelsea laugh
    D "Well, you beat the shit out of me. Congrats, [pcname]."
    show Damien Happy
    show chelsea blank
    D "Do you want to play again?"
    if damienNTR == True:
        show chelsea sad
        "You glance at your phone; it's getting late, and Matt wanted you to text him..."
        show chelsea embarrassed
        "But he just said to do it after Damien left, so..."
    elif True:
        show chelsea embarrassed
        "You look at your phone; it's getting late, but it is a weekend, after all. You have time for one more game at least."
    show chelsea happy
    pcname "Sure, that sounds fun."
    show Damien Happy
    show chelsea embarrassed
    "Damien grins and reshuffles the cards for the next game."
    if damienconfidence >= 50:
        show Damien Shocked
        "He pauses as he hands out your player cards, and it's like a lightbulb has gone off above his head."
        show Damien Happy
        show chelsea confused
        D "Say, uh, [pcname]... How about we make this round a little more interesting?"
        if club == "track":
            show chelsea shocked
            "You feel your eyebrows shoot up, surprised by his offer. "
            show chelsea confused
            pcname "What did you have in mind?"
        elif club == "cheer":
            show chelsea embarrassed
            "You feel a smirk play at the edge of your lips. You already have a pretty good idea for what he has in mind."
            pcname "Is that so? "
        elif club == "yearbook":
            show chelsea embarrassed
            "You feel the blood rush to your cheeks as you realize what he's suggesting."
            pcname "I-Interesting how?"
        show Damien Laugh
        D "Well, we could make this into a pretty easy stripping game. How about it?"
    elif True:
        show chelsea shocked
        show Damien Blank
        "As Damien hands out your player cards, a suggestive thought pops into your mind."
        if club == "track":
            show chelsea happy
            "You pick up the makeshift treasure chest and shake it, rattling up the cardboard coins inside."
            show chelsea laugh
            pcname "How about we make this game a little more interesting?"
        elif club == "cheer":
            show chelsea embarrassed
            "You reach forward and brush a hand down Damien's arm, freezing him in place."
            pcname "You know, I think I know something that would make this game a little more interesting."
        elif club == "yearbook":
            show chelsea sad
            "Biting down on your lip, you play nervously with your fingers, barely able to meet his gaze."
            show chelsea embarrassed
            pcname "W-Winning that last round was too easy. L-let's add something else to the game to make it more interesting."
        show Damien Shocked
        show chelsea embarrassed
        "His eyes widen in response as he registers what you're trying to say."
        show Damien Neutral
        D "M-More interesting? How, uh, would we do that?"
        "From the flush on his cheeks, it seems like he already knows what you have in mind."
    menu damien_boardgamestrip:
        "Keep it Clean." if True:
            $ corruption -=5
            $ negotiationsclean = True
            if damienconfidence >= 50:
                show chelsea sad
                show Damien Blank
                "You consider his offer for a moment, but can't bring yourself to feel the same excitement for the idea."
                show chelsea blank
                "It would be one thing if you were playing a card game or something with simplistic rules, but this game is complicated enough without adding sex to the mix."
                show chelsea confused
                "You're not even sure you could get turned on during a game like this, and isn't that the whole point of stripping games?"
                show chelsea embarrassed
                show Damien Sad
                if club == "track":
                    pcname "Uh, I think I'll pass. It sounds like it's going to be too much work."
                    show chelsea happy
                    pcname "If you want to bet, though, we can just use the snacks we have on the table."
                elif club == "cheer":
                    pcname "Mmm... a stripper war game? It sounds more fun than I think it would be when put to the test."
                    show chelsea happy
                    pcname "We have snacks we can use if you want to spice up the betting, though."
                elif club == "yearbook":
                    pcname "I-I think I'd rather just use the snacks we have on the table if we're going to gamble..."
                show Damien Worry
                show chelsea embarrassed
                "There is no denying the disappointment on Damien's face, but he quickly picks himself back up and nods in understanding."
                show Damien Neutral
                D "Yeah, don't worry, I get it. Setting up rules for this kind of game could be complicated, anyway."
            elif True:
                show chelsea happy
                "Seeing him all flustered almost makes you want to suggest what he's thinking, but the idea of changing your mind and teasing him for those thoughts is even more fun."
                show chelsea laugh
                show Damien Shocked
                if club == "track":
                    pcname "Let's do some bets! We have all this food here, anyway. Let's put it to good use."
                elif club == "cheer":
                    pcname "How about we bet some of the food we have? There's a ton of leftover snacks, so we might as well."
                elif club == "yearbook":
                    pcname "W-Well, we could throw in some betting... I have a lot of snacks to choose from."
                show chelsea embarrassed
                "You gesture toward the array of snacks on the coffee table, each one separated by little glass bowls."
                show Damien Sad
                "Damien's shoulders slump a little in disappointment as he looks over the array of chips and candy."
                show Damien Worry
                D "O-Oh... Um, yeah, we could do that..."
                show chelsea laugh
                if club == "track":
                    "He's almost making this too easy; how are you supposed to resist teasing him if he makes it so obvious?"
                    show chelsea embarrassed
                    pcname "What's wrong, Damien? Were you hoping I'd suggest something more {i}sexual{/i} instead?"
                    "You bat your eyelashes for emphasis and push your chest out a little more."
                elif club == "cheer":
                    "You can't contain the smirk on your face as Damien avoids your gaze, shifting in place on the ground."
                    show chelsea embarrassed
                    "You lean up against him, pressing your breasts against his arm. Damien sucks in a sharp breath and goes still."
                    pcname "What is it, Damien? Did you have something else in mind?"
                elif club == "yearbook":
                    "There's something both exciting and heartbreaking to see Damien's hopes dashed before him."
                    show chelsea embarrassed
                    "You know you {i}should{/i} feel bad about it, but it just makes you want to tease him more."
                    pcname "What is it, Damien? W-Were you thinking of something else?"
                show Damien Shocked
                "Damien's face flushes a deep red and he quickly shakes his head, waving his hands in denial."
                show Damien Laugh
                show chelsea laugh
                D "N-N-No! Of course not!"
                show Damien Happy
                show chelsea embarrassed
                D "F-Food bets sound great. Let's go with that."
            show Damien Blank
            show chelsea blank
            "Damien pulls away a little to divide the snacks evenly onto two separate plates, marking each one with one of the game's currency symbols."
            show Damien Happy
            show chelsea happy
            "Once the game is reset, he lifts two of his chips up and smiles at you."
            show Damien Happy
            show chelsea embarrassed
            D "Let's get started."
            scene black with fade
            "This game lasts shorter than the rest, with both you and Damien eager to beat the other and win the rest of your favorite snacks."
            "In the end, you end up with a plate full of chips while Damien wins the game with a tower of miniature candy bars."
            "You can't really be mad though; these chips are delicious."
            scene bg HomeN
            show chelsea happy at center, moveSprite(0.8, 0.8, 0.0)
            show Damien Laugh
            with fade
            D "Ha... Yeah, using food was definitely fun. That was a good decision, [pcname]."
            show chelsea laugh
            show Damien Happy
            if club == "track":
                "You grin, chomping onto one of the chips. Crumbs fly over your plate."
                pcname "I'm full of great ideas."
            elif club == "cheer":
                "You smile and dramatically brush your hair over your shoulder."
                pcname "I know."
            elif club == "yearbook":
                "You smile, nibbling on one of the chips from your plate."
                pcname "Thank you."
            show chelsea blank
            show Damien Sad
            "Looking at his phone, Damien sighs."
            show Damien Neutral
            show chelsea sad
            D "I guess I should pack up and go home, huh?"
            if damienNTR == True:
                "You look at your phone again and frown. You shouldn't keep Matt waiting..."
            elif True:
                "You look at the time on your own phone and frown. It seems all good things must come to an end."
            show chelsea embarrassed
            pcname "Yeah, I guess so."
            scene black with fade
            "You help Damien clean up the rest of the game and pack up everything before escorting him to the front door."
            scene bg HomeN
            show Damien Laugh at right
            show chelsea embarrassed at center, moveSprite(0.9, 0.9, 0.0)
            with fade
            D "Thanks for having me over, [pcname]. I had a really good time."
            show Damien Happy
            D "Maybe I'll bring over some more board games next time for us to play?"
            show chelsea laugh
            pcname "Yeah, I would like that."
        "Stripping." if True:
            $ corruption += 5
            if damienconfidence >= 50:
                show Damien Happy
                if club == "track":
                    show chelsea happy
                    "Your lips curl into a sharp grin at the challenge. The same excitement you have on the track field floods through your veins, filling your body with adrenaline."
                    pcname "Stripping, huh? You're on. I hope you're wearing clean underwear."
                    show Damien Laugh
                    show chelsea embarrassed
                    "Damien laughs, pleased with your sudden competitive behavior."
                    show Damien Happy
                    D "Heh, I hope you are, too."
                elif club == "cheer":
                    show chelsea laugh
                    pcname "Oh, now this sounds like fun. Don't be too discouraged when you lose, Damien."
                    show chelsea embarrassed
                    "You wink at him, teasing. Damien grins, his gaze slowly falling over your body."
                    show Damien Laugh
                    D "I should say the same to you."
                elif club == "yearbook":
                    show chelsea embarrassed
                    "Although you're initially embarrassed by his suggestion, the thought of adding another element to the game sounds exciting. Especially one so sexual..."
                    "Fighting back the blush on your cheeks, you bite your lip and nod."
                    pcname "T-That... That sounds fun..."
                show Damien Happy
                "Damien smiles and finishes setting up the game. He leans back on his palm, his eyes drifting down your body."
                show Damien Laugh
                show chelsea happy
                D "Let's start then, huh?"
                scene black with fade
                "Damien deals out the first set of weaponry cards, and you begin."
                "As the game goes on, you're certain that Damien has been hiding some kind of intense strategy guide out of sight that's allowing him to win."
                "It's barely five turns in, and he's already knocked you out of your socks and hoodie; there isn't much left to take off."
                "Damien picks up one of the event cards and sets it over your player card."
                scene bg HomeN
                show Damien Neutral
                with fade
                D "Global pandemic. My nation sends the disease to your country."
                show chelsea shocked at center, moveSprite(0.8, 0.8, 0.0) with dissolve
                "You gape at him and then at the card. In all of the past games, Damien hadn't been so forward with trying to destroy your country; now, it's his single goal."
                show Damien Happy
                D "You know that means-"
                show chelsea embarrassed
                if club == "track":
                    pcname "Yeah, yeah, I know."
                elif club == "cheer":
                    pcname "I'm aware."
                elif club == "yearbook":
                    pcname "I-I know!"
                hide chelsea with dissolve
                pause 1.0
                show chelsea embarrassed at center, moveSprite(0.8, 0.8, 0.0) with dissolve
                "Damien chuckles under his breath, watching as you peel your shirt off and drop it into a heap on the floor. Your breasts press against the edges of your bra, comfortable in the warm air of your apartment."
                show Damien Blank
                "You notice his gaze fall on your cleavage. Damien's eyelids droop slightly and he slowly meets your gaze."
                show Damien Laugh
                D "Your turn."
                show chelsea blank
                "Thinking you've got the better of him, you pick up a card from the deck and slam it onto his."
                show chelsea happy
                show Damien Blank
                pcname "Ha! Earthquake. Your capital is split into two."
                show Damien Sad
                show chelsea embarrassed
                "Damien squints, leaning down to read the fine print."
                show Damien Neutral
                show chelsea shocked
                D "Ah, [pcname], that's {i}your{/i} capital. See?"
                show Damien Blank
                pcname "Huh?"
                "Damien picks up the card and shows you the small print at the bottom."
                show chelsea confused
                pcname "'{i}This card is applicable to the player who draws it-{/i} Oh! Damn it."
                show Damien Laugh
                show chelsea angry
                "Damien laughs, shaking his head."
                show Damien Happy
                D "You have some poor luck this game, babe."
                hide chelsea with dissolve
                "You grumble a response as you stand up and reach down to unbutton your shorts. You slide them over your thighs and past your calves before kicking them across the room."
                $ clothes = "underwear"
                show chelsea angry at center, moveSprite(0.8, 0.8, 0.0) with dissolve
                "Left in nothing but your bra and panties, Damien lets out a contented sigh."
                show chelsea embarrassed
                show Damien Blank
                "Your initial bitterness at losing the game diminishes as you feel the heat of his stare on you."
                show Damien Happy
                if club == "track":
                    pcname "Yeah. I guess I just really suck this round, huh?"
                elif club == "cheer":
                    pcname "Just the {i}worst{/i} luck. Before you know it, I'm not going to have anything left!"
                elif club == "yearbook":
                    pcname "Y-Yeah... I'm not doing so well."
                "Damien grins but doesn't respond. He picks up another card for his turn and flips it over."
                show Damien Neutral
                show chelsea blank
                D "Oh, some good news for you. My capital flooded. We need time to recoup."
                show Damien Blank
                "Without hesitation, Damien takes his jacket off and tosses it over the armrest of the couch."
                scene black with fade
                "Another round goes by. Then another. And another."
                "Damien, left in just his underwear and socks, watches in delight as you unclasp your bra and let it fall to the floor."
                "The game is almost over, leaving you both with two turns left."
                scene bg HomeN
                show chelsea confused at center, moveSprite(0.8, 0.8, 0.0)
                with fade
                pcname "So, what's going to happen if you win? Do I still need to take everything off?"
                show Damien Laugh with dissolve
                show chelsea blank
                D "I have an idea for what we'll do."
                show Damien Happy
                "Damien lifts a card from the pile and sets it on yours."
                show Damien Laugh
                show chelsea shocked
                D "I nuke your capital."
                pcname "T-That's my last standing city!"
                show Damien Happy
                show chelsea sad
                "Damien holds his hands up in defense, but it doesn't take away from the gleeful smile on his face."
                D "Sorry! I guess that means game over."
                hide chelsea with dissolve
                if club == "track":
                    "You hook your thumbs underneath your panties and slide them down, kicking them aside. Looking up, you catch Damien's eyes roving over you."
                elif club == "cheer":
                    "You hook your thumbs underneath your panties and slide them down, tossing them at Damien playfully. He catches them with a laugh."
                elif club == "yearbook":
                    "Unable to meet his gaze, you stare at his feet as you hook your thumbs underneath your panties. Sliding them down, you step out of them."
                $ clothes = "naked"
                show chelsea embarrassed at center, moveSprite(0.8, 0.8, 0.0) with dissolve
                show Damien Laugh
                D "Wasn't that fun?"
                show Damien Happy
                if club == "track":
                    pcname "Oh, yes. Delightful."
                elif club == "cheer":
                    pcname "Oh yes, Damien~. You know how much I love stripping down for you."
                elif club == "yearbook":
                    pcname "G-Greatest game of my life."
                "You say it sarcastically, but he knows you're teasing."
                show chelsea happy
                pcname "So what was that about ending the game?"
                show Damien Blank
                show chelsea embarrassed
                "Damien's smile falters and his eyelids grow heavy with desire. He crawls over you and one hand gently cups your breast before bringing it to his mouth."
                scene black with fade
                "You run your fingers through his hair and hook your ankles around his waist, pulling him closer to you. You can feel his erection poking through his underwear against your thigh."
                "You reach for his erection, ready to pull him out, but Damien catches your hand."
                D "Not tonight. Let me just enjoy touching you."
                scene black with dissolve
                "You slowly nod and retract your hand. Damien caresses your body with gentle fingers, his lips pressing down on the bare skin of your neck and chest."
                "Each touch feels gentler than the last, sending a fluttering sensation through your body."
                "You feel your clit throb as he pinches and pulls your nipples between his thumbs, his mouth biting and sucking each one in turn."
                scene black with dissolve
                "Pulling away slightly, you reposition yourself on his lap and gently grind against his thigh."
                "Damien pulls you even closer, his hands grabbing your ass and waist as you grind against him."
                "Soft moans escape from his lips as your knee bumps against his cock."
                "His mouth becomes more aggressive on your breasts, licking and biting down on the flushed skin, and leaving hickeys in his wake."
                "You pant as he drags you back and forth across his thigh, rubbing your clit against his skin."
                pcname "D-Damien... Damien...!"
                scene black with dissolve
                "Your nails dig into his shoulders as Damien captures your mouth with his, effectively silencing you."
                "You moan into his mouth and he picks up the speed, rubbing you harder against his thigh. You rock yourself with him, small whimpers escaping your throat as you reach your climax."
                "You grip his shoulders hard as you come down from your climax, your breath heavy and uneven."
                scene black with dissolve
                "Damien kisses your hair as you come down from your high, his fingers lightly stroking your back until you're finished."
                "He smiles as you pull away and shakily pull on your shorts and t-shirt, not bothering with your underwear. Damien pulls his clothes on as well, running a hand through his messy hair."
                $ clothes, hair = casualwear
                scene bg HomeN
                show Damien Sad
                show chelsea at center, moveSprite(0.8, 0.8, 0.0)
                with fade
                "Looking at his phone, Damien sighs."
                show Damien Neutral
                D "I guess I should pack up and go home, huh?"
                show chelsea sad
                show Damien Blank
                if damienNTR == True:
                    "In the heat of the moment, you'd nearly forgotten Matt's words. Your heart sinks."
                elif True:
                    "You look at the time on your own phone and frown. It seems all good things must come to an end."
                show Damien Sad
                pcname "Yeah, I guess so."
                scene black with fade
                "You help Damien clean up the rest of the game and pack up everything before escorting him to the front door."
                scene bg HomeN
                show chelsea embarrassed at right, moveSprite(0.9, 0.9, 0.0)
                show Damien Happy at right
                with fade
                "Before he leaves, Damien presses a soft kiss to your cheek."
                show Damien Laugh
                D "I had a really good time with you tonight, [pcname]. I guess I'll bring board games over more often."
                show chelsea happy
                show Damien Happy
                pcname "I look forward to it."
                show chelsea embarrassed
                "He grins, laughing a little under his breath."
            elif True:
                show chelsea happy
                show Damien Blank
                "He looks so innocent and shy about the whole thing that you can't help but want to tease him a little."
                show chelsea laugh
                pcname "{i}He really makes this too easy...{/i}"
                show chelsea embarrassed
                if club == "track":
                    "Reaching a hand over, you grip Damien's upper thigh, relishing in the small shiver his body makes upon contact."
                    show Damien Shocked
                    pcname "How about we play some Strip 'Negotiations'?"
                elif club == "cheer":
                    "You lean forward and press yourself as close against Damien's side as you can, positioning his hand between the small gap between your legs."
                    "You notice his eyes dart down there, his cheeks burning a bright red. You smirk, drawing your lips up to his ear."
                    show Damien Shocked
                    pcname "For this game... The loser is going to strip."
                    "You run a sharp nail down his chest, enjoying the shiver his body elicits in response."
                elif club == "yearbook":
                    "Feeling bold and excited by his shy response, you lean forward, your cleavage clearly visible through the gap in your shirt."
                    show Damien Shocked
                    pcname "W-We could play while... while stripping..."
                    pcname "I-If you want to, I mean."
                show Damien Neutral
                show chelsea laugh
                D "T-That... That... Good..."
                show Damien Blank
                show chelsea embarrassed
                "Damien stammers his response, tongue-tied and flustered. He eventually takes a deep breath, working to calm himself."
                show Damien Neutral
                D "T-That sounds good, I-I mean... Yeah. Yeah."
                show Damien Blank
                show chelsea laugh
                "You grin, feeling a sexual thrill at his meekness."
                show chelsea embarrassed
                "You take the cards and shuffle them."
                pcname "Let's play, then."
                scene black with fade
                "The game drags on, with Damien making long, careful decisions as he tries to do his best to destroy your country."
                "They prove to be futile, though; halfway through the game, Damien is left down to his underwear and socks, while you're still fully dressed."
                "Damien shuffles his cards with trembling hands, concentrating hard as he views each weapon and gathered disaster card."
                "It's been ten minutes and he still hasn't made a decision."
                scene bg HomeN
                show Damien Shocked
                show chelsea angry at center, moveSprite(0.8, 0.8, 0.0)
                with fade
                pcname "Come on, Damien. Make a choice."
                show Damien Worry
                show chelsea blank
                D "S-Sorry."
                show Damien Happy
                "He picks a new one up from the deck and, with a relieved smile, sets it down on top of my card."
                show chelsea confused
                D "A flood! Your city suffers from a catastrophic flood and takes years to repair."
                show chelsea angry
                pcname "Let me see that."
                show chelsea sad
                "You pick up the card and look it over in dismay: he's right."
                if club == "track":
                    "You set the card back down with a sigh."
                    show chelsea blank
                    pcname "Well, alright. I guess I can take one loss."
                elif club == "cheer":
                    show chelsea embarrassed
                    "You smile coyly, twirling the card between your fingers."
                    pcname "Oh, alright. You've already stripped so much for me, I suppose you do deserve a little reward."
                elif club == "yearbook":
                    "You frown at the card and set it back down on the pile. At least you haven't lost any clothes yet, but it wouldn't take many turns for you to get there."
                    pcname "I-I guess I have no choice."
                show Damien Blank
                hide chelsea with dissolve
                pause 1.0
                show chelsea at center, moveSprite(0.8, 0.8, 0.0) with dissolve
                "You pull off your hoodie and toss it over the back of the couch. Your shirt is thin enough for Damien to see your bra, but nothing more exciting than that."
                show Damien Worry
                show chelsea embarrassed
                "Regardless, he stares at your chest before catching your gaze and quickly looking away. There's no disguising the rising erection in his thin underwear, either."
                show chelsea happy
                pcname "My turn."
                show chelsea blank
                show Damien Blank
                "You pick up one of the event cards and briefly glance it over before slapping it down over his player card."
                show chelsea laugh
                show Damien Shocked
                pcname "A revolt! Your people are unhappy. They think you need to take off more clothes."
                show Damien Laugh
                show chelsea laugh
                "Damien cracks a smile at your joke before removing a single sock."
                scene black with fade
                "The game carries on for a few more turns, switching over to some bad luck on your end. You end up in your bra and panties, while Damien is left in nothing but his underwear."
                "You hold up your stack of cards, looking Damien over."
                $ clothes = "underwear"
                scene bg HomeN
                show chelsea laugh at center, moveSprite(0.8, 0.8, 0.0)
                show Damien Worry
                with fade
                pcname "Final round. Any last words?"
                show Damien Happy
                show chelsea blank
                "Damien gives a hopeless, half-hearted smile."
                show Damien Worry
                show chelsea embarrassed
                D "Please spare me?"
                hide Damien with dissolve
                "You shake your head and place a nuke card on his. Damien's face bursts in shades of pink as he hooks his thumbs around the edge of his boxer briefs, hesitating."
                show Damien Blank with dissolve
                "He looks to you as if asking permission before he slides the underwear down, revealing his erect cock. He doesn't look you in the eye as he sets the fabric aside."
                show Damien Neutral
                D "Ah, good game, [pcname]. Congratulations."
                show Damien Worry
                if club == "track":
                    show chelsea laugh
                    pcname "Apparently I wasn't the only one that had fun, huh, Damien?"
                elif club == "cheer":
                    show chelsea happy
                    pcname "A very good game indeed, hm? What's that I see over there, Damien? Did you get all horny while we were playing?"
                    D "I-I-"
                elif club == "yearbook":
                    show chelsea embarrassed
                    pcname "It was fun."
                    "You smile bashfully as you take in his erection. Damien tries to hide it, but does a poor job at it."
                    pcname "O-Oh, Damien... Y-Your..."
                show chelsea blank
                "Damien looks away, too flustered to meet your gaze."
                show chelsea laugh
                "Now {i}this{/i} is something you can't pass up."
                scene black with fade
                "Reaching up on your knees, you make your way over to the shy boy and settle yourself between his legs."
                "You slowly run your hands up and down his chest, relishing in the small trembles his body makes at your touch."
                pcname "Do I get my prize now?"
                D "P-Prize? I-I don't..."
                scene black with dissolve
                "You press yourself flush against his body, situating your clit over his erection. Damien gasps, gripping the small of your back on instinct."
                pcname "My prize for winning; it's you, isn't it?"
                "Damien gapes like a fish, struggling to find the right words to respond with."
                D "I-If- I mean- If you want-"
                scene black with dissolve
                "Grinning, you silence him with the crush of your lips. Damien makes a small noise in your mouth but relents, his fingers running up and down the smooth skin of your back."
                "You grind against his cock, the fabric of your panties creating friction between you. Although he tries not to, you feel Damien thrust against you, eager to feel your body against his."
                "You intertwine your fingers tightly in his hair, kissing him hard as you grind your pussy against him. Damien's hips jerk in response, thrusting at the thin fabric of your panties."
                D "[pcname]... Ohhh, [pcname]... Please..."
                "Damien starts to slide his hand to your panties, ready to push them aside, but you grab his hand and yank it to your face."
                scene black with dissolve
                "Damien looks away, embarrassed to be caught, but you stick his fingers in your mouth and his eyelids flutter before a moan slips from his lips."
                "You can feel him getting harder beneath you with each press of your cunt on his dick. Your wetness soaks through your panties and rubs along his cock, making it easier to move against."
                "Damien moans in your ear as he feels your fluids coat him. His fingers dig into your hips, moving you against him faster."
                D "[pcname]... [pcname]...!"
                pcname "D-Damien..."
                "Your own climax builds as your clit rubs hard against him. Your legs tighten around his waist with your orgasm, and Damien gasps, his cock twitching with his own release."
                scene black with dissolve
                "You spend a few minutes calming down and catching your breath, pressing small kisses to Damien's neck. He shivers, holding you close."
                D "W-We... We should play board games more often."
                "You can't help but laugh."
                scene black with dissolve
                "Disentangling yourselves, Damien flushes with embarrassment at the sticky mess he's made on the floor."
                pcname "Don't worry, I'll clean it up."
                D "I-I don't mind! I can take care of it!"
                scene bg HomeN with fade
                "Before you can argue, Damien hops up and rushes to get some paper towels from the kitchen."
                "You put on your shorts and t-shirt, not bothering with underclothes, and start to clean up the snacks and board game while you wait."
                "Once everything is clean, Damien looks at his phone and frowns."
                show Damien Worry with dissolve
                D "I-I guess I have to go now, huh?"
                $ clothes, hair = casualwear
                show Damien Sad
                show chelsea sad at center, moveSprite(0.8, 0.8, 0.0) with dissolve
                if damienNTR == True:
                    "In the heat of the moment, you'd nearly forgotten Matt's words. Your heart sinks."
                elif True:
                    "You look at your own phone with a sigh."
                pcname "Yeah, I guess so. Let me walk you out."
                scene black with fade
                "Damien gives a small smile and follows you to the door."
                scene bg HomeN
                show Damien Happy at right
                show chelsea embarrassed at right, moveSprite(0.9, 0.9, 0.0)
                with fade
                D "Thanks for having me over, [pcname]. I had a really good time. I'll make sure to bring more board games next time, if that's okay?"
                show chelsea happy
                pcname "That sounds great."
                show Damien Blank
                show chelsea embarrassed
                "He looks relieved."
                show Damien Neutral
                D "C-Cool."
    if damienconfidence >= 50:
        show Damien Happy
        show chelsea embarrassed
        "Damien grins, pausing in the doorway."
        show Damien Neutral
        D "So, uh, I mentioned this the other day but we haven't really talked about it since then."
        show Damien Happy
        show chelsea blank
        D "I was wondering if you wanted to go to the homecoming dance with me next Friday?"
    elif True:
        show Damien Happy
        show chelsea embarrassed
        "Damien pauses in the doorway, a shy smile on his face."
        show Damien Neutral
        D "So, um, I mentioned this before, but I didn't get an answer, so I just wanted to ask again- I mean, if that's okay. I. Um."
        show Damien Blank
        "Damien takes a deep breath, steadying himself."
        show Damien Happy
        show chelsea blank
        D "Will you go to the homecoming dance with me next Friday?"
    menu damien_boardgames_homecomingoffer:
        "I'd love to." if True:
            $ corruption -= 1
            show chelsea happy
            if club == "track":
                pcname "Sure! That sounds like fun."
                show chelsea embarrassed
                pcname "I, uh, I don't have to wear heels, do I?"
                show Damien Laugh
                D "Not unless you want to."
                show chelsea laugh
                show Damien Happy
                pcname "Great! Then yeah, I'd love to go!"
            elif club == "cheer":
                pcname "Well, duh! Of course I want to!"
                show chelsea laugh
                pcname "To be honest, I kind of assumed we would, being a couple and everything. I would be insulted if you didn't take me!"
            elif club == "yearbook":
                pcname "Y-Yes! I'd love to, Damien..."
            show Damien Happy
            show chelsea embarrassed
            "Damien grins, the same boyish smile he had when he first showed up at your apartment with his board game."
            D "Great! Uh, I'll pick you up around seven, then. My mom wants some pictures, so we can get someone to take them for us on my phone while we're at the dance."
            D "Thanks for having me over, [pcname]. Sleep well."
            hide Damien with dissolve
            "Damien presses a soft kiss to your lips before stepping out of the apartment, waving to you as he leaves. You wave back before gently closing the door behind him."
            scene black with fade
            if negotiationsclean == True:
                "As you get ready to relax, slipping into nothing but shorts and a t-shirt, you think about his invitation."
            "A homecoming dance... You didn't get a chance to go to one at your old school, but you've seen what they're like in movies and TV shows."
            if club == "track":
                "From what you remember, a homecoming dance has something to do with sports, doesn't it? Maybe you can watch one of the school's games before you go to the dance."
            elif club == "cheer":
                "Cute dresses, high heels, music and laughter and partying all around... It sounds like heaven!"
            elif club == "yearbook":
                "Big groups, loud music, having to balance yourself in high heels... It sounds like a disaster waiting to happen. You already feel anxious thinking about it."
                "But Damien had looked so hopeful, and you have always been curious about what it would be like to go to one..."
                "Maybe it won't be so bad. And if it is, you're sure Damien would understand if you want to leave early."
            if damienNTR == True:
                scene bg HomeN
                show chelsea laugh
                with fade
                "You smile, imagining him dressed up... But your smile fades as your pocket vibrates."

                call screen TextingScene("Matt", [TextMessage("You didn't forget about me did you?")])

                show chelsea sad
                "Biting your lip, you summon the courage to text him back."

                call screen TextingScene("Matt",
                [
                    TextMessage("He's leaving now", sender = False),
                    TextMessage("See you soon")
                ])
            elif True:
                "Although you end up reclining back on your couch and resuming your movie on TV, your mind is already on the homecoming dance and what it might be like."
            $ homecoming = True
        "Dances aren't really for me." if True:
            show chelsea sad
            if club == "track":
                "The sports games leading up to homecoming are one thing, but the idea of having to wobble around in high heels for a night, pretending that you care if you trip into the kids from school is a whole other nightmare."
                show chelsea embarrassed
                show Damien Sad
                pcname "Uh... I think I'll pass. School dances aren't really my thing, Damien."
            elif club == "cheer":
                "As tantalizing as the idea of attending a school dance is, you can't help but feel the whole thing is a little... childish."
                "So much high school drama happens at these things, and while you love to hear the gossip about it later, you aren't interested in taking part in it."
                show chelsea sad
                show Damien Blank
                pcname "I, uh, you know I'd love to, Damien, but it just sounds like so much extra work. Not to mention how people like to cause scenes at those things."
                show Damien Sad
                pcname "I'd rather do something else."
            elif club == "yearbook":
                "You have no experience with high school dances, but from the ones you've seen in movies and TV, the idea of being surrounded by a group of sweaty, loud strangers sounds terrifying."
                show chelsea embarrassed
                show Damien Sad
                pcname "I-I'm not really interested in going... I'm so sorry, Damien..."
            show Damien Worry
            show chelsea blank
            "Damien's smile falls. He looks away, embarrassed, and scratches the back of his head."
            show Damien Neutral
            D "Oh. Um, yeah. That's fine, [pcname]. Maybe we'll figure something else out to do that night instead?"
            show Damien Blank
            show chelsea sad
            "He sounds so hopeful that you can't find it in your heart to deny him."
            show chelsea embarrassed
            show Damien Happy
            pcname "Sure. We'll plan for something else that day."
            show Damien Laugh
            D "Awesome. Well, uh, I'll see you at school."
            hide Damien with dissolve
            "Damien presses a kiss to your cheek before quickly scurrying out of your apartment. Once he's far enough away, you see him hang his head in rejection."
            scene black with fade
            if negotiationsclean == True:
                "As you get ready to relax, slipping into nothing but shorts and a t-shirt, you think about his invitation."
            "You feel bad for denying his request to go to the dance, but at the same time, it really isn't the environment for you."
            pcname "{i}I'll need to think of something else for us to do together that day, then...{/i}"
            if damienNTR == True:
                scene bg HomeN
                show chelsea shocked
                with fade
                "You ponder over alternative ideas, but your thoughts are interrupted when your pocket vibrates."

                call screen TextingScene("Matt", [TextMessage("You didn't forget about me did you?")])

                show chelsea sad
                "Biting your lip, you summon the courage to text him back."

                call screen TextingScene("Matt",
                [
                    TextMessage("He's leaving now", sender = False),
                    TextMessage("See you soon")
                ])
            elif True:
                "You ponder over alternative ideas as you relax on your couch and spend the rest of your night watching movies."
    if damienNTR:
        show chelsea embarrassed
        "You consider putting on more clothes, but it seems pointless. You know Matt will have you take them off anyway."
        show chelsea sad
        "For a moment you feel guilty; you know the things Matt will do to you, but you still haven't gone all the way with Damien yet."
        if defymatt:
            show chelsea angry
            "Not that Matt's given you much of a choice..."
        elif True:
            show chelsea embarrassed
            "But with Damien, it just feels... {i}different{/i}. Like it needs to be special, somehow."
        show chelsea sad
        "You shiver a little. With Matt, it's so {i}dirty{/i}..."
        show chelsea embarrassed
        if defymatt:
            "In a sick, twisted way, it almost makes you {i}want{/i} to hold back with Damien."
        elif True:
            "And while you know that's what you deserve, Damien makes you feel so... different. Cherished."
        show chelsea shocked
        "A knock on your door pulls you from your thoughts. You swallow back your fears and walk to the door."
        show chelsea blank at moveSprite(0.5, 0.8, 0.3)
        "As soon as you swing the door open, Matt steps inside."
        show Matt Casual Smirk at right with dissolve
        m "So, did you have {i}fun{/i} with your little boyfriend?"
        show chelsea embarrassed
        show Matt Casual Pleased
        "Your face flushes as you nod."
        show chelsea shocked
        "Without warning, Matt cups your pussy through your shorts, pressing the thin fabric against you and stroking."
        if negotiationsclean == True:
            show Matt Casual Smirk
            show chelsea sad
            m "It doesn't {i}feel{/i} like you had fun."
            show Matt Casual Question
            m "Did he even try? Maybe he doesn't know how..."
            show Matt Casual Pleased
            if club == "track":
                show chelsea angry
                pcname "Matt, does it really matter?"
            elif club == "cheer":
                show chelsea angry
                pcname "Do you really want to know about that?"
            elif club == "yearbook":
                pcname "Matt, please, I don't..."
            show Matt Casual Happy
            show chelsea blank
            "He laughs."
            m "You can't even stand up for him, can you?"
            show chelsea sad
            show Matt Casual Smirk
            pcname "He's a nice guy, I just..."
            show chelsea embarrassed
            "He pushes his fingers harder against your pussy."
            show Matt Casual Pleased
            m "He just doesn't get you {i}wet{/i}. Don't worry, I can tell."
        elif True:
            show Matt Casual Question
            m "You're wet. Did you let him fuck you?"
            show chelsea embarrassed
            "You shake your head, searching for words."
            show chelsea sad
            show Matt Casual Smirk
            pcname "No, we just... touched each other."
            show Matt Casual Pleased
            m "Did he get you off?"
            show Matt Casual Smirk
            "You lower your eyes."
            show Matt Casual Blank
            if club == "track":
                show chelsea angry
                pcname "Matt, does it really matter?"
            elif club == "cheer":
                show chelsea angry
                pcname "Do you really want to know about that?"
            elif club == "yearbook":
                show chelsea embarrassed
                pcname "Matt, please, I don't..."
            show chelsea sad
            "He strokes your pussy through your shorts again."
            show Matt Casual Angry
            show chelsea embarrassed
            m "Just answer the question, slut."
            show Matt Casual Smirk
            if club == "track":
                pcname "Yeah, I got off."
            elif club == "cheer":
                pcname "Yes, he got me off, okay?"
            elif club == "yearbook":
                pcname "Y-yes..."
            show Matt Casual Happy
            "He laughs."
            show Matt Casual Pleased
            m "I'm surprised he could figure out how."
        show Matt Casual Smirk
        "With one last stroke, he pulls his hand away from your shorts and strides into the living room."
        scene black with fade
        m "Hmmm... Let's use the couch."
        "Your heart thunders in your chest as you wait to see what he wants."
        m "Well? Get those clothes off."
        scene black with dissolve
        "He watches as you peel off your shorts and t-shirt, smirking at your lack of underclothes."
        m "So you took 'em all off for him, didn't you, slut?"
        "Nodding wordlessly, you cross your arms over your body."
        if defymatt:
            "You want to tell him to get out of your apartment, but who know what he would do?"
            "Between the pictures and Damien, he has you completely at his mercy."
        elif True:
            "You're ashamed of yourself - he's right, you {i}are{/i} a slut."
        m "Get on the couch. Face down, ass up."
        "You move to obey him, putting your phone on the coffee table, and--"
        m "Keep the phone. You're going to need it."
        scene black with dissolve
        "Your eyes widen at his words, but you do as he instructs. Crawling onto the couch, you grab hold of the arm opposite him and stick your ass up."
        "Thoughts racing, you barely notice him stripping behind you. Until you hear the familiar sound of his phone camera."
        scene black with dissolve
        "You glance back; his phone is pointed toward you, as you expected."
        "{i}Snap * Snap * Snap {/i}"
        if defymatt:
            "Knowing how much blackmail he already has, it shouldn't bother you anymore, but somehow it still does."
        elif True:
            "Your heart skips a beat. Will he use those pictures later when he...?"
        m "Good girl. Now, text Damien."
        "Your eyes widen."
        pcname "Text him... what?"
        m "I don't care what you say. Just text him."

        scene black with dissolve

        "You panic a moment, before deciding to keep it simple."

        call screen TextingScene("Damien", [TextMessage("Hey", sender = False)])

        pcname "There. I texted him."
        scene black with dissolve
        "Matt climbs onto the couch behind you, pressing his cock against your opening."
        if negotiationsclean == True:
            m "You're getting wet {i}now{/i}..."
        elif True:
            m "You're still fucking wet..."
        "{i}*Bzzt*{/i}"
        "He slides the tip of his cock up and down your slit."
        m "Well? Aren't you going to see what he wrote back?"

        call screen TextingScene("Damien", [TextMessage("Hey. Just got home")])

        m "Don't be rude. Text him back."
        "With Matt's cock running up and down your opening, you find it almost impossible to respond."
        m "Just tell him you miss him."
        "You wince; it feels so {i}wrong{/i} to do this."
        if defymatt:
            "But what choice do you have?"
        elif True:
            "But if this is what Matt wants..."

        call screen TextingScene("Damien", [TextMessage("I miss you", sender = False)])

        scene black with dissolve
        "As you lower your phone again, you feel Matt lean forward, his cock sliding between your legs."
        "{i}*Bzzt*{/i}"
        m "I bet he misses you too."
        "He reaches beneath you and grabs your breasts in his hands."
        "His fingers, already so familiar with your body, find your nipples immediately."
        m "Well? Text him back."
        "As you lift your phone, he pinches them gently, twisting them in his fingers."

        call screen TextingScene("Damien", [TextMessage("I miss you too")])

        m "See? I told you he misses you..."
        "He squeezes your breasts."
        m "I bet he misses {i}these{/i} the most..."
        m "Say something sexy now."
        pcname "What?"
        m "Go on. Do it."

        call screen TextingScene("Damien", [TextMessage("I wish you could have stayed longer", sender = False)])

        if negotiationsclean == True:
            call screen TextingScene("Damien", [TextMessage("We could have... upped the stakes", sender = False)])
        elif True:
            call screen TextingScene("Damien", [TextMessage("There's so much more I want to do...", sender = False)])

        "As you hit send, Matt pinches your nipples hard."
        "You gasp, rocking your hips back against him instinctively."
        m "Does he know what a slut you are? Texting him while you rub yourself on my dick?"
        "{i}*Bzzt*{/i}"
        "You lift the phone, knowing it's what Matt wants you to do."

        call screen TextingScene("Damien",
        [
            TextMessage("Really?"),
            TextMessage("I'd like that too")
        ])

        "Matt's fingers pinch and twist at your nipples, his erection hard between your legs."
        m "Tell him what you want him to do to you."

        call screen TextingScene("Damien", [TextMessage("I keep thinking about your fingers on my nipples", sender = False)])

        "Matt chuckles."
        m "Taking inspiration from me?"
        "He accents his words with another twist of your nipples, making you cry out."
        "Again, you rock back against him, his cock sliding back and forth between your thighs."
        "{i}*Bzzt*{/i}"

        call screen TextingScene("Damien",
        [
            TextMessage("Yeah?"),
            TextMessage("What else?")
        ])

        "Matt laughs."
        m "Oh, he's getting into this, huh?"
        "He twists your nipples hard, until you rock your hips against him again."
        m "Keep going."
        "Unsure of which one he means, you text Damien again while rocking your hips against Matt."

        call screen TextingScene("Damien", [TextMessage("Your mouth sucking on them", sender = False)])

        scene black with dissolve
        "Matt's cock slides back and forth, barely brushing your clit with every movement."
        "His fingers pinch, pull, and twist at your nipples until you can barely think."
        "{i}*Bzzt*{/i}"

        call screen TextingScene("Damien",
        [
            TextMessage("That sounds nice"),
            TextMessage("What about the rest of you?")
        ])

        m "Well? Tell him how much you want a dick inside of you."
        "Matt's fingers are relentless, and the soft caress of his cock against your clit is quickly filling your senses."

        call screen TextingScene("Damien", [TextMessage("The more I think about it, the wetter my pussy gets", sender = False)])

        m "We both know {i}that's{/i} not what's getting you wet right now..."
        "He thrusts his hips against yours, pressing his cock harder to your clit."
        "Gasping, you meet his thrusts with your own. He's right; you want a dick inside of you."
        if defymatt:
            "And to your shame, you don't really care whose right now."
        elif True:
            "But you'll never tell Damien {i}whose{/i} dick you want right now."
        "{i}*Bzzt*{/i}"

        call screen TextingScene("Damien", [TextMessage("Yeah? How wet is it?")])

        "Matt laughs."
        m "Oh, it's practically dripping. My dick is soaked."
        "You continue rocking against his thrusts, aware that he's right - you've soaked his cock in your arousal."
        "Moaning, you reply."

        call screen TextingScene("Damien", [TextMessage("Dripping", sender = False)])

        m "I think you're enjoying this. I think you like that he doesn't know what you're really doing over here."
        if defymatt:
            "You burn with shame; what if he's right? You're certainly turned on right now..."
        elif True:
            "You burn with shame. He's right; something about this really turns you on."
        "{i}*Bzzt*{/i}"

        call screen TextingScene("Damien",
        [
            TextMessage("I'm so hard right now [pcname]"),
            TextMessage("What would you do if I was there right now?")
        ])

        "Matt laughs again."
        m "Yeah, what {i}would{/i} you do if he was here {i}right{/i} now?"
        "You're already typing a response."

        call screen TextingScene("Damien", [TextMessage("That depends? Would you rather have my mouth or my pussy?", sender = False)])

        "Releasing your nipples with a final pinch, Matt sits back on the couch, leaving you moaning your disappointment as his cock slips away from you."
        scene black with dissolve
        "His cock is quickly replaced by his fingers, which he runs tantalizingly lightly over the mounds of your labia."
        "{i}*Bzzt*{/i}"

        call screen TextingScene("Damien", [TextMessage("Mouth first")])

        "You don't need any further prompting. While Matt teases you, you continue sexting Damien."

        call screen TextingScene("Damien",
        [
            TextMessage("First? Naughty", sender = False),
            TextMessage("Then I guess I'd start there. Running my tongue around the head", sender = False)
        ])

        "Matt's fingers find your clit. You moan as he rubs it in slow circles."
        "{i}*Bzzt*{/i}"

        call screen TextingScene("Damien", [TextMessage("Fuck")])

        "Your clit throbs as Matt presses just a little harder."

        call screen TextingScene("Damien", [TextMessage("Then what?")])

        "His fingers move just a little faster."

        call screen TextingScene("Damien",
        [
            TextMessage("Then I'd wrap my lips around it", sender = False),
            TextMessage("take as much as I could", sender = False),
            TextMessage("and suck you off", sender = False)
        ])

        "You press yourself back toward Matt, eager for him to continue."
        "He rubs your clit harder and faster, until it throbs almost painfully with pleasure."
        "{i}*Bzzt*{/i}"

        call screen TextingScene("Damien",
        [
            TextMessage("Fuck [pcname]"),
            TextMessage("Then what?")
        ])

        "Waves of pleasure radiate out from your swollen clit."

        call screen TextingScene("Damien", [TextMessage("After I swallow your load?", sender = False)])

        "You're so close to coming, you can feel yourself on the edge of your climax..."

        call screen TextingScene("Damien", [TextMessage("Oh fuck...")])

        call screen TextingScene("Damien", [TextMessage("Yes after that")])

        scene black with dissolve
        "Matt's fingers pull away suddenly; you cry out your frustration."
        if defymatt:
            "You barely consider your words before they leave your mouth."

        pcname "Matt, please..."

        call screen TextingScene("Damien", [TextMessage("What about you? What do you want?", sender = False)])

        "Chuckling, Matt presses his cock against your opening."
        m "Is this what you want?"

        call screen TextingScene("Damien", [TextMessage("I want you")])

        pcname "I want you."
        m "What do you want me to do?"

        call screen TextingScene("Damien", [TextMessage("Are you touching yourself?")])

        "You aren't. It's Matt's hands on your body. His cock against your pussy."

        call screen TextingScene("Damien",
        [
            TextMessage("Yes", sender = False),
            TextMessage("I want to be inside of you")
        ])

        m "What do {i}you{/i} want?"

        if defymatt:
            "You swallow your pride."

        pcname "Fuck me. Please..."

        call screen TextingScene("Damien", [TextMessage("Fuck me. Please...", sender = False)])

        scene black with dissolve
        "Matt thrusts himself inside of you, filling you in one hard motion."
        pcname "Matt!"
        "He pulls back and thrusts again."
        "{i}*Bzzt*{/i}"
        "His thrusts stop as he waits for you to look at your phone."
        pcname "Please, don't stop..."
        m "Don't blue ball him now. Answer him."

        call screen TextingScene("Damien",
        [
            TextMessage("I wish I was there right now"),
            TextMessage("I'd hold you against me as we made love")
        ])

        "Matt thrusts into you again, grabbing hold of your hips for leverage."

        call screen TextingScene("Damien", [TextMessage("Would you fuck me hard?", sender = False)])

        "Matt does. Each thrust fills you almost painfully full."

        call screen TextingScene("Damien", [TextMessage("No, I'd be gentle. You'd never feel more loved")])

        m "See? He doesn't know how to fuck a slut like you..."
        "Thrusting into you again and again, Matt quickly brings you back to the edge of orgasm."
        "{i}*Bzzt*{/i}"

        call screen TextingScene("Damien",
        [
            TextMessage("And then when we're done I'd hold you in my arms"),
            TextMessage("And tell you how precious you are to me")
        ])

        "Matt's cock hits your g-spot just right, sending an intense wave of pleasure over you."
        pcname "Ah!"
        "He thrusts again and again, hitting the spot with every thrust."
        "In moments, your pussy clamps around him and you begin to quiver with the force of your orgasm."
        pcname "Oh fuck!"
        "A few thrusts against your tightening cunt and Matt empties himself into you."
        "{i}*Bzzt*{/i}"
        scene black with dissolve
        "Matt pulls away from you, leaving his cum trailing down your thigh."
        "{i}*Bzzt*{/i}"
        "Still breathless, you lift your phone."

        call screen TextingScene("Damien", [TextMessage("Did you cum?")])

        "Matt laughs cruelly."
        m "Yeah, you came alright."
        "You fight back your shame as you reply."

        call screen TextingScene("Damien",
        [
            TextMessage("Yeah", sender = False),
            TextMessage("Me too")
        ])

        m "He came while I fucked you, huh? I wonder what he'd think if he knew..."
        "You bite your lip. Damien would be crushed if he knew what you'd been doing while you were texting him."
        "And yet, your clit still throbs at the memory..."

        call screen TextingScene("Damien",
        [
            TextMessage("Now I'm ready for bed", sender = False),
            TextMessage("Me too. Good night!")
        ])

        scene bg HomeN with fade
        "By the time you finish texting Damien, Matt's already dressed."
        show Matt Casual Blank with dissolve
        m "You know, I was going to make you break up with him..."
        $ clothes = "naked"
        show chelsea shocked at left with dissolve
        "You whirl to face him, startled."
        pcname "What!?"
        show Matt Casual Smirk
        show chelsea sad
        m "...but I think this could be a lot more fun."
        show chelsea embarrassed
        "Smirking down at you, Matt leans down to pinch your nipple again."
        show Matt Casual Pleased
        m "I kinda like it that you're fucking me behind your boyfriend's back."
        show Matt Casual Happy
        show chelsea sad
        m "And I {i}know{/i} he could never satisfy a slut like you."
        "He pinches the other nipple too, before standing again."
        show chelsea blank
        show Matt Casual Smirk
        m "I'll see you at school. I have plenty of ideas for what we can do next..."
        hide Matt with dissolve
        "Even after Matt's gone, you stare at the closed door."
        "You feel so many things - shame, guilt, and... excitement?"
        show chelsea embarrassed
        "Your clit throbs dully, still swollen with desire."
        show chelsea sad
        if defymatt:
            "How far down has Matt dragged you that you can be aroused by the idea of cheating on your boyfriend like this?"
        elif True:
            "Matt's right; you're a slut, through and through."
        scene black with fade
        "As you crawl into bed, you try to clear your mind, but you just keep thinking about it. Picturing it."
        $ corruption += 5
        "And as you fall asleep, your mind is filled with it: the image of Damien jerking himself off while Matt fucks you."
    elif True:
        jump endday
    jump endday

label damien_homecoming:
    if homecoming == True:
        $ damienAttire(2)
        $ clothes, hair = ("bluedress", "braidedponytail")
        scene bg RoomE
        show chelsea at right
        with fade
        "It's a quarter to seven when you hear Damien knocking at your door, but you're still busy in your room curling your hair."
        show chelsea happy
        pcname "Come in!"
        show chelsea blank
        "You hear Damien's footsteps wander around your living room as he lets himself in. They stop just outside of your bedroom door."
        D "Can I come in?"
        show chelsea happy
        pcname "Sure."
        show chelsea blank
        show Damien Blank at left with dissolve
        "Damien peeks into your bedroom and stares at you from behind, speechless."
        show chelsea confused
        show Damien Shocked
        pcname "...Is everything okay?"
        if damienconfidence >= 50:
            show Damien Worry
            D "You look beautiful."
        elif True:
            show Damien Laugh
            D "A-Ah, yeah! Sorry, I just... You look really pretty, [pcname]."
        show chelsea embarrassed
        show Damien Blank
        "You can't help but smile, allowing another curl to fall over your shoulder."
        show Damien Happy
        pcname "Thanks."
        show chelsea sad
        show Damien Blank
        pcname "Sorry, I wasn't expecting you for another fifteen minutes."
        show chelsea blank
        pause 1.0
        show chelsea embarrassed
        "You look him over from your bedroom mirror, relief washing through you as you take in his attire."
        show chelsea laugh
        "It's a simple black suit, nothing outlandish, and it matches your short cream and burgundy dress perfectly."
        show chelsea embarrassed
        pcname "{i}At least his style is getting a little better...{/i}"
        show Damien Laugh
        D "That's okay! I can wait in the living room while you finish getting ready."
        show Damien Happy
        show chelsea happy
        pcname "Okay. I'll be out in a minute."
        hide Damien with dissolve
        "Damien nods and disappears into the living room."
        scene black with fade
        "You spend a few more minutes curling your hair and putting on jewelry before you step back out into the living room."
        scene bg HomeD
        show chelsea embarrassed at right
        show Damien Shocked at left
        with fade
        "Damien watches you from his place on the couch, his lips parted in awe."
        if club == "track":
            show chelsea happy
            "You give him a confident spin, splaying your arms out wide."
            pcname "Like what you see?"
        elif club == "cheer":
            show chelsea laugh
            "You adjust your hair over your shoulder and pose, stretching your legs out long."
            pcname "What do you think, Damien?"
        elif club == "yearbook":
            show chelsea embarrassed
            "You shyly play with one of your curls, shifting nervously in place. Maybe the jewelry was too much?"
            pcname "D-Do you like it?"
        show Damien Happy
        show chelsea embarrassed
        D "You're the prettiest girl I've ever seen, [pcname]."
        if club == "track":
            show chelsea laugh
            "You laugh and wink at him teasingly."
            pcname "I bet you say that to all the girls."
            show chelsea embarrassed
            "But even with your joking, Damien's smile is soft and sincere."
            show Damien Neutral
            D "No, only you, [pcname]."
        elif club == "cheer":
            show chelsea laugh
            "You blow him a kiss."
            show chelsea embarrassed
            pcname "That's what I like to hear~."
        elif club == "yearbook":
            "You find yourself grinning despite the blooming blush on your cheeks."
            pcname "T-Thank you."
        show Damien Shocked
        pause 1.0
        show Damien Laugh
        show chelsea shocked
        D "Oh! This is for you; I thought it would go with your dress."
        show Damien Happy
        show chelsea confused
        "Damien picks up a small box from the coffee table and opens it up: a white and red rose corsage stares back at you."
        "It's perfect, but you never showed Damien your homecoming dress. You had hoped it would be a fun surprise."
        pause 1.0
        show chelsea laugh
        pcname "This is so pretty! How did you know it would go with my dress?"
        show Damien Worry
        pause 0.5
        show Damien Happy
        show chelsea embarrassed
        "Damien smiles back as he slides the corsage onto your left wrist."
        show Damien Laugh
        D "I just had a feeling."
        show Damien Happy
        "He offers out his elbow to you."
        show Damien Laugh
        D "Are you ready to go?"
        show chelsea laugh
        show Damien Happy
        "You loop arms with him, pressing your hand against his bicep, and smile up at him."
        pcname "Yeah, let's go."
        scene bg CityD with fade
        "Damien leads you out of the apartment and to his waiting car outside; a shiny, sleek black car that cost more than your whole apartment."
        show chelsea shocked at left with dissolve
        pcname "Oh, wow! This is really nice, Damien."
        show chelsea blank
        if damienconfidence >= 50:
            show Damien Neutral with dissolve
            D "Oh, it's my dad's, actually, but he let me borrow it for the night. My car is getting inspected."
            show Damien Blank
        elif True:
            show Damien Worry with dissolve
            "Damien sheepishly looks away, scratching the back of his head."
            show Damien Neutral
            D "O-Oh... Um, it's my dad's, actually... but he let me borrow it for the night."
            D "N-Not that I don't have a car! It's just getting inspected..."
            show Damien Worry
        "You nod in understanding. Damien opens the car door for you and helps you inside before rushing to the driver's seat."
        scene black with dissolve
        if damienconfidence >= 50:
            show Damien Neutral with dissolve
            D "Alright, it's my first time actually driving anywhere, so hold on tight."
            hide Damien with dissolve
            pause 1.0
            show chelsea sad with dissolve
            "Damien stares at the nervous look on your face for a moment before breaking out into a wide grin."
            hide chelsea with dissolve
            pause 1.0
            show Damien Laugh with dissolve
            D "I'm teasing. Relax, we'll be there soon."
        elif True:
            show Damien Worry with dissolve
            D "S-So, um, you don't mind that I don't have a license, right?"
            hide Damien with dissolve
            "Your heart drops into your stomach with a sudden panic."
            show chelsea shocked with dissolve
            pcname "What?!"
            hide chelsea with dissolve
            pause 1.0
            show Damien Laugh with dissolve
            D "K-Kidding! I'm just kidding. I've been driving for two years already, don't worry. We'll be there soon."
        hide Damien with dissolve
        "You take a deep, relieved sigh and recline into the passenger seat. Damien puts some music on the radio and drives."
        scene bg School with fade
        "By the time you reach the school, you can already hear the dance's music blasting from inside of the gymnasium and out across the school parking lot."
        "Damien parks his car and escorts you out, leading you to the dance. Once the tickets are given to the students running the event, you both head inside."
        scene bg Gym with fade
        "It seems the theme this year is Tinseltown, with various life-size props of filmmaking equipment and a long, red 'carpet' stretching through the hallway."
        "A variety of movie posters hang on the walls beside the chosen genre of each grade; apparently, your class chose Horror."
        show Damien Glare with dissolve
        "Damien makes a face at the poster as you pass."
        D "I voted for Sci-fi, but the Juniors got that."
        show Damien Neutral
        D "What would you have picked?"
        menu homecoming_moviegenre:
            "Romance." if True:
                show chelsea embarrassed at center, moveSprite(0.7, 0.7, 0.0) with dissolve
                show Damien Blank
                if club == "track":
                    pcname "It's kind of cheesy, but I like romance films. There's something about two people ending up happy together that's just kind of sweet."
                elif club == "cheer":
                    pcname "Romance, of course. It's so satisfying to see a happy ending; we don't get enough of that in real life, you know?"
                elif club == "yearbook":
                    pcname "I-I like romance, actually... It-It makes me really happy to see people fall in love."
                if damienconfidence >= 50:
                    show Damien Happy
                    "Damien smiles softly, charmed by your response."
                    D "Yeah... Romance is kind of magical, isn't it?"
                elif True:
                    show Damien Worry
                    "Damien smiles shyly, his thumb stroking down your arm."
                    show Damien Happy
                    D "I-I feel the same way..."
            "Fantasy." if True:
                show chelsea happy at center, moveSprite(0.7, 0.7, 0.0) with dissolve
                show Damien Blank
                if club == "track":
                    pcname "Oh man, ever since I saw '{i}The Ring Forger{/i} as a kid, I've been hooked on fantasy. The character designs are just so cool!"
                elif club == "cheer":
                    pcname "Okay, so it's kind of totally weird, but I've always really liked fantasy movies. Fairytales and magic and stuff like that."
                    show chelsea laugh
                    pcname "I know it's usually for kids, but it's just so creative, y'know?"
                    show Damien Laugh
                    show chelsea embarrassed
                    D "It's not just for kids, don't worry!"
                elif club == "yearbook":
                    pcname "W-Well, I really like fantasy. It's just really creative and fun..."
                show Damien Happy
                show chelsea embarrassed
                "Damien smiles wide, excitement lighting up his eyes."
                show Damien Laugh
                D "I know exactly what you mean! It's definitely in my top three favorite genres, but I can't decide between fantasy, sci-fi, and superhero movies for which is my favorite..."
            "Horror." if True:
                show chelsea happy at center, moveSprite(0.7, 0.7, 0.0) with dissolve
                show Damien Blank
                if club == "track":
                    pcname "Horror, of course! Fake blood and guts are my jam."
                elif club == "cheer":
                    pcname "I'm partial to horror, actually. There's something about the creepy vibe that gets my heart racing... It's fun."
                elif club == "yearbook":
                    pcname "I-I actually like horror movies..."
                show Damien Shocked
                show chelsea embarrassed
                "Damien's jaw drops in surprise."
                show Damien Worry
                D "Really?! I never would have taken you for a horror movie fan, [pcname]..."
                show Damien Laugh
                D "I guess I should brush up on some horror films then, huh?"
            "Action." if True:
                show chelsea happy at center, moveSprite(0.7, 0.7, 0.0) with dissolve
                show Damien Blank
                if club == "track":
                    pcname "Action, definitely! Those fighting sequences get me really pumped up!"
                elif club == "cheer":
                    pcname "I think I'd go with action, y'know? They always cast the sexiest stars, and who doesn't want to watch sweaty, shirtless men punch each other?"
                elif club == "yearbook":
                    pcname "W-well, I think action is pretty fun... The violence is a little cringey, but i-it feels really intense!"
                show Damien Shocked
                show chelsea embarrassed
                pause 1.0
                show Damien Happy
                D "Really? I didn't take you for someone that would be really into action movies. Cool!"
                show Damien Laugh
                D "My dad has a big movie collection, though, and he has a ton of old spy action movies in there. We should watch them sometime!"
        scene bg Gym with dissolve
        "You and Damien continue discussing your favorite movie genres as he escorts you into the dance."
        "The gymnasium has practically been transformed with large balloon arches, prop hollywood signs and palm trees, and a marquee board welcoming us to the dance."
        "Even Damien seems impressed by the display."
        show Damien Shocked with dissolve
        D "They really went all out this year, huh?"
        show Damien Neutral
        D "Last year the theme was 'Autumn in the City'. No one really knew what to do for it, so everyone picked different cities and tried to mash them together."
        show Damien Worry
        D "It ended up looking like a weird mix of cities with some leaves tossed in."
        show chelsea sad at center, moveSprite(0.7, 0.7, 0.0) with dissolve
        pcname "That's unfortunate."
        show Damien Sad
        pause 1.0
        show Damien Laugh
        D "Yeah. The dance was kind of lame, but I'm really glad we're here together this year, [pcname]."
        show Damien Happy
        show chelsea embarrassed
        "Damien takes your hand in his and smiles down at you. You feel your heart flutter in your chest, touched by his gentle gesture."
        show chelsea laugh
        pcname "I am, too."
        $ AliceClothes = 1
        $ AugustClothes = 1
        scene bg Gym with dissolve
        scene bg Gym
        show Alice Laughing at left, moveSprite(0.3, 0.3, 0.0)
        show August Laugh at right, moveSprite(0.7, 0.7, 0.0)
        with dissolve
        pause 1.5
        scene bg Gym
        show Sophie Shy at left, moveSprite(0.3, 0.3, 0.0)
        show V Party Smile at right, moveSprite(0.7, 0.7, 0.0)
        with dissolve
        pause 1.5
        scene bg Gym with dissolve
        $ AugustClothes = 0
        "You and Damien look out across the crowd of students as they spread out across the gymnasium; some dancing, others taking pictures, while the rest relax and enjoy some of the snacks laid out."
        if damienconfidence >= 50:
            show Damien Happy with dissolve
            D "Do you want to dance, [pcname]?"
            show chelsea at center, moveSprite(0.7, 0.7, 0.0) with dissolve
        elif True:
            show Damien Worry with dissolve
            D "U-Um, do you want to... would you like to, er...?"
            show Damien Blank
            "Damien gestures vaguely to the dance floor."
            if club == "track":
                show chelsea happy at center, moveSprite(0.7, 0.7, 0.0) with dissolve
                pcname "Are you trying to ask me to dance?"
            elif club == "cheer":
                show chelsea laugh at center, moveSprite(0.7, 0.7, 0.0) with dissolve
                "You giggle at his shy attempt."
                show chelsea embarrassed
                pcname "Are you asking me to dance, Damien?"
            elif club == "yearbook":
                show chelsea embarrassed at center, moveSprite(0.7, 0.7, 0.0) with dissolve
                pcname "D-Dance?"
            show Damien Worry
            D "Ah, yeah... If you want to, I mean."
        menu damien_homecoming_dance:
            "Sure." if True:
                $ corruption -= 2
                $ damienconfidence +=1
                if club == "track":
                    show chelsea laugh
                    "Listening to the beat of the music, you feel pumped and ready to move."
                    show chelsea happy
                    show Damien Happy
                    pcname "Hell yeah! Let's go!"
                elif club == "cheer":
                    show chelsea laugh
                    "It wouldn't be a real homecoming without dancing, right? You can't imagine a better start to the night!"
                    show chelsea happy
                    show Damien Happy
                    pcname "Definitely! I thought you'd never ask."
                elif club == "yearbook":
                    show chelsea sad
                    "Looking at the rowdy group of students on the dance floor fills your chest with panic, but at the same time, they really do look like they're having fun..."
                    show chelsea embarrassed
                    show Damien Happy
                    pcname "S-Sure."
                scene black with fade
                "Damien grins and, taking your hand in his, leads you out to the dance floor."
                scene black with dissolve
                if damienconfidence >= 50:
                    "Damien reaches out to hold you, but then pauses, looking to you for permission."
                elif True:
                    "Damien smiles at you nervously as he tries to figure out where to place his hands on your body."
                    "He hovers his hands over you instead, as though dancing with an invisible girl."
                menu damien_homecoming_dance2:
                    "Encourage him to touch you." if True:
                        $ damienconfidence +=1
                        scene black with dissolve
                        if club == "track":
                            "You quickly grab his hands and press them to your hips. Damien smiles thankfully, and you wrap your arms around his neck."
                        elif club == "cheer":
                            "You quickly grab his hands and press them to your hips. Damien smiles thankfully, and you wrap your arms around his neck."
                        elif club == "yearbook":
                            "Too shy to say anything, you gently take his hands and press them against your hips. Damien smiles thankfully, and you wrap your arms around his neck."
                        D "I'm not the best dancer."
                        pcname "Neither am I."
                        "You both smile at each other and dance."
                    "Mock him." if True:
                        $ corruption += 1
                        $ damienconfidence -= 1
                        scene black with dissolve
                        if club == "track":
                            pcname "...Seriously? You'd rather dance with the air than me?"
                        elif club == "cheer":
                            pcname "...What the hell are you doing?"
                        elif club == "yearbook":
                            pcname "T-There's a real girl to touch right here, you know..."
                        scene black with dissolve
                        if damienconfidence >= 50:
                            D "Er, sorry, I was..."
                            "Damien holds his hands out in front of you, still unsure of where to put them."
                        elif True:
                            "Damien's face erupts into bright pink as he struggles to meet your gaze. His lifted hands tremble slightly, betraying his nervousness."
                            D "S-Sorry, I was- I was just-"
                            "He continues to hold his hands out dumbly."
                        if club == "track":
                            pcname "You're hopeless, you know that?"
                            "Grabbing his wrists, you yank him closer and press his hands onto your hips."
                        elif club == "cheer":
                            pcname "Ugh, let me."
                            "You roll your eyes and press your body against him fully, forcing his hands onto your hips."
                        elif club == "yearbook":
                            "With a sigh, you step closer to him and gently place his hands onto your hips."
                        pcname "Better?"
                        "He nods quickly, his fingers digging into your hips."
                        "You wrap your arms around his neck and dance."
                scene black with dissolve
                "The beat picks up and you and Damien move against each other, helping guide each other through the various dances."
                "Despite not being a great dancer, Damien does a good job of not stepping on your feet and even keeping the two of you away from bumping into any other couples on the floor."
                if corruption >= 25:
                    "Noticing a couple of others grinding, you consider doing the same until you see a few teachers strictly enforcing rules against it and dragging anyone who disobeys more than once out into the hall."
                    "The faculty just has to ruin all the fun, don't they?"
                scene black with dissolve
                "Damien bows his head down against your shoulder as a particularly slow song comes on, burying you into his chest."
                "His breath tickles your ear as he whispers."
                D "You really are beautiful tonight, [pcname]."
                if club == "track":
                    pcname "As opposed to every other night?"
                    "You grin at your own joke, and Damien chuckles softly in your ear."
                    D "No, you're beautiful every night. I don't feel like I say that enough."
                elif club == "cheer":
                    pcname "Aw, thanks. You've really cleaned up yourself, Damien."
                    "You feel Damien's lips twitch into a smile against your skin."
                elif club == "yearbook":
                    "There's something so intimate about the way he whispers it into your ear like a prayer. You feel goosebumps spread all over your body."
                    pcname "T-Thank you."
                D "I'm so lucky to have you."
                scene black with dissolve
                if damienNTR:
                    "You feel a little guilt rise up in your chest as you think of your rendezvous with Matt behind Damien's back."
                    "There's no way Damien could know, but his unrelenting faith in your loyalty is so... pure. You can't help but feel bad for deceiving him."
                    "As you glance around the room, you notice that Matt is absent, much to your relief."
                    pcname "{i}I guess he's too 'cool' for things like this...{/i}"
                    "You can only imagine what would happen if he saw you dancing with Damien. Or if Damien saw you with Matt..."
                    if defymatt == True:
                        "You shake away the thought."
                        "After all, Matt didn't even bring {i}up{/i} homecoming; it's obvious you're just a fucktoy to him that he can blackmail into doing what he wants."
                        "You should be {i}happy{/i} he's not here."
                    elif True:
                        "You almost feel a little disappointed that Matt isn't here to stir things up; he always has a way of making things more exciting..."
                        "You quickly shake the thought from your head."
                        "You're here with {i}Damien{/i}. That's who you should be focused on."
                if katerelate == 'girlfriend':
                    "Guilt rises in your chest as you think of your relationship with Kate behind Damien's back."
                    "They're both so innocent and sweet - and they're convinced you're loyal to both of them."
                    "If either of them found out about the other, they would be devastated."
                    pcname "{i}It's a good thing Kate is out of high school...{/i}"
                if damienNTR or katerelate == "girlfriend":
                    "Realizing you haven't answered Damien yet, you smile against him and sigh."
                pcname "Me too."
                "The two of you sway for a few moments longer, lost in the music."
                scene bg Gym
                show Alex Laugh at left
                with dissolve
                "Alex" "Well, well, look who got a date."
                show Damien Shocked with dissolve
                show Alex Happy
                "Damien freezes up, pulling you to a rigid stop in your dance. You move away slightly to peer at Alex over Damien's shoulder, a smirk on his face."
                show Damien Glare
                if mattslap == 1 and bullytelloff == 1:
                    show chelsea sad at center, moveSprite(0.7, 0.7, 0.0) with dissolve
                    "You feel your heart beat unevenly, the reminder of Matt and Alex's hands on you as they pinned you down in the alley resurfacing in your mind."
                    "A sickening feeling settles in your stomach and you force yourself to look away to hide the tears brimming in your eyes."
                if mattsubmissive == True and bullytelloff == 1:
                    show chelsea embarrassed at center, moveSprite(0.7, 0.7, 0.0) with dissolve
                    "Shame heats your face as you lock eyes with Alex, all of the indecent acts you committed with him and Matt in your classroom resurfacing in your mind."
                    "Panic swells in your chest but you try to push it down."
                    show chelsea sad
                    "What if he mentions something to Damien? You aren't sure you're prepared for that kind of confrontation."
                show Alex Serious
                "Alex" "It's a miracle. Did you pay her to go with you, Damien?"
                show Damien Sad
                show Alex Happy
                "Damien sighs and turns, keeping one hand against your waist."
                if damienconfidence >= 50:
                    show Damien Angry
                    D "What do you want, Alex?"
                    show Damien Blank
                    show Alex Neutral
                    "Alex" "I wanna know how you got this babe to dance with you in the first place, to start. Did you shove enough fives in her panties that she finally said yes?"
                    show Damien Glare
                    show Alex Happy
                    "Damien grits his teeth beside you, glaring at Alex."
                    show Damien Angry
                    D "I'd prefer you didn't talk about my girlfriend that way."
                elif True:
                    show Damien Angry
                    show Alex Blank
                    D "N-No! She's my girlfriend..."
                show Damien Glare
                show Alex Serious
                "Alex" "Your {i}girlfriend?{/i}"
                show Alex Laugh
                "He barks out a laugh."
                "Alex" "No fucking way. No girl is dumb enough to go out with your creepy, loner ass."
                show Alex Serious
                show Damien Shocked
                "Alex" "Especially not after that incident with-"
                show Damien Angry
                show Alex Happy
                if damienconfidence >= 50:
                    D "{i}What do you want, Alex?{/i}"
                elif True:
                    D "J-Just tell me what you want, Alex..."
                show Damien Glare
                "Alex smirks, cocking his head to the side. You feel his gaze rove up and down your body, taking in every curve exposed by your dress."
                show Alex Laugh
                "Alex" "I just want to dance with your little girlfriend. You don't mind sharing, do ya, buddy?"
                show Alex Happy
                if damienconfidence >= 50:
                    show Damien Angry
                    D "Of course I mind! Find someone else to harass, Alex. We're busy."
                    show Damien Glare
                    "Damien squeezes you a little tighter to his side."
                elif True:
                    "Damien looks like he wants to argue, but he struggles to get the words out."
                    show Damien Neutral
                    D "I-I'm not really comfortable with that..."
                    show Damien Blank
                show Alex Neutral
                "Alex" "Why don't we ask your girlfriend instead of you making decisions for her?"
                show Alex Happy
                pause 1.0
                show Alex Laugh
                "Alex" "What do you say, [pcname]? You wanna dance with me?"
                menu damien_homecoming_alex:
                    "Fine, I'll dance with you." if True:
                        $ corruption += 2
                        show Alex Blank
                        if mattslap == 1 and bullytelloff == 1:
                            "You feel sick at the idea of touching him again, but if it means he'll leave you and Damien alone for the rest of the night, you're willing to make that sacrifice."
                        if mattsubmissive == True and bullytelloff == 1:
                            "You aren't really in any position to deny him, especially if you want Alex to keep quiet about your threesome with Matt."
                        show Damien Sad
                        show Alex Happy
                        if club == "track":
                            show chelsea blank
                            pcname "If it gets you to back off, sure, I'll dance."
                        elif club == "cheer":
                            show chelsea blank
                            pcname "Ugh, fine, whatever. Just leave us alone after this."
                        elif club == "yearbook":
                            pcname "W-Will you leave us alone if I do?"
                            "Alex's lips twist into a wicked grin. He raises up a hand, staring at Damien as he speaks."
                            "Alex" "Scout's honor."
                            show chelsea embarrassed
                            pcname "T-Then... Then I guess so..."
                        show Damien Worry
                        D "[pcname], you really don't have to do this-"
                        show chelsea shocked
                        pause 0.3
                        scene black with dissolve
                        "But Alex already has you in his arms, his hands roaming between your waist and your ass as he drags you further away on the dance floor."
                        if damienconfidence >= 50:
                            "You glimpse Damien pushing through the crowd toward you, but Alex whirls you around and out of sight."
                        elif True:
                            "You glimpse Damien standing dejectedly in the spot where you both had danced, but Alex whirls you around and out of sight."
                        "Alex grinds you against him on the dance floor, feeling your body up between his splayed fingers."
                        if mattslap == 1 and bullytelloff == 1:
                            scene black with dissolve
                            "You try to hold back your tears at his touch, biting down hard on your lip. You count down the seconds until the song is over, trying to keep from throwing up."
                            "Although, maybe it would be nice to vomit on him in front of everyone."
                        if mattsubmissive == True and bullytelloff == 1:
                            scene black with dissolve
                            "The feeling of his hands once again on your body sends a thrill through you, reminding you of every touch he gave beneath your clothes."
                            "You don't want to enjoy it, but a part of you just can't help it."
                        "Alex" "Man, you're wasting your time on that freak. He doesn't appreciate you like a real man would."
                        scene black with dissolve
                        if club == "track":
                            if mattslap == 1 and bullytelloff == 1:
                                "You glare at him, imagining all the different ways you could hurt him in the same way he hurt you."
                                pcname "Real men don't rape, asshole."
                                "Alex snorts, shaking his head."
                                "Alex" "You liked it; I saw how wet you were. Don't even try to deny it."
                                "Shame floods your cheeks and you grit your teeth, wishing more than anything that you could punch him here and now."
                                pcname "God, you're disgusting. I'm done; get the fuck away from me. I'm going back to Damien-"
                            "You elbow him hard, putting some space between you. Alex grunts but recedes a little."
                            pcname "I don't see a real man here."
                        elif club == "cheer":
                            if mattslap == 1 and bullytelloff == 1:
                                "You glare at him with pure hatred in your eyes, your throat raw from all the tears you've held in."
                                pcname "That's funny coming from a {i}rapist.{/i}"
                                "You say the last word a little louder, hoping to catch the ear of one of your fellow students."
                                "Alex forces you closer against him, his breath hot and threatening in your ear."
                                "Alex" "I'd watch it if I were you. Don't think I won't try it a second time."
                                "His words send an icy chill down your spine. You stare at him in disgust, your stomach in knots."
                                pcname "You aren't even {i}half{/i} the man Damien is-"
                            "You can't help rolling your eyes."
                            pcname "And {i}you{/i} think you're a real man? Please. My bunny slippers look manlier than you."
                        elif club == "yearbook":
                            "You try to put some space between you and Alex, but he holds you firmly against him."
                            if mattslap == 1 and bullytelloff == 1:
                                pcname "A-A real man doesn't... doesn't r-rape..."
                                "Your voice cracks on the last word, a few tears spilling down your face."
                                "Alex snorts and leans in close, his breath hot in your ear."
                                "Alex" "You liked it. Don't even pretend you didn't."
                                pcname "I-I didn't!"
                                pcname "L-Let me go. Damien's waiting for me-"
                            elif True:
                                pcname "A-A real man wouldn't pick on another man and his girlfriend..."
                        "Alex laughs."
                        "Alex" "Man, he's really got you under some freak spell, doesn't he?"
                        "Alex" "The kid is a fucking loser. There's a reason he doesn't have any friends."
                        pcname "Maybe the reason is because of people like {i}you.{/i}"
                        "Alex" "Sure. Keep telling yourself that; whatever makes you sleep at night, baby."
                        scene black with dissolve
                        "Alex drags you against him for one last spin before the song draws to a close."
                        if mattslap == 1 and bullytelloff == 1:
                            scene black with dissolve
                            "Before you can pull away, Alex leans toward you, a shit-eating grin on his face."
                            "Alex" "I'll tell Matt you said hi."
                            "You choke on a sob and push away from him."
                        if mattsubmissive == True and bullytelloff == 1:
                            scene black with dissolve
                            "Before you can pull away, Alex leans toward you, a shit-eating grin on his face."
                            "Alex" "I'll tell Matt you said hi."
                            "Your cheeks flush but you push away from him, putting some distance between you two."
                        "Alex" "Have fun with your weak ass bitch."
                        scene bg Gym with fade
                        "Alex doesn't object as you scurry back through the dance floor."
                        show Damien Glare at left with dissolve
                        "You find Damien near the punch bowl, two full cups in his hands."
                        show Damien Shocked
                        show chelsea with dissolve
                        pause 1.0
                        show Damien Worry
                        "He looks both relieved and ashamed as he lifts his gaze to meet yours."
                        show Damien Neutral
                        D "Hey."
                        show Damien Blank at moveSprite(0.0, 0.3, 0.4)
                        show chelsea embarrassed
                        "He offers you one of the cups. You gladly take it."
                        show Damien Worry
                        show chelsea blank
                        D "Are you okay?"
                        show Damien Blank
                        show chelsea sad
                        pcname "Yeah, I'm fine."
                        show chelsea blank
                        "You both sip your punch for a few moments in silence."
                        show Damien Worry
                        D "I'm sorry you ended up dancing with him. I wish I could have done more-"
                        menu damien_homecoming_alexaftermath01:
                            "You should have done more." if True:
                                $ corruption += 1
                                $ damienconfidence -= 1
                                show Damien Sad
                                show chelsea sad
                                "Damien looks down at his feet, ashamed. He nods."
                                show Damien Worry
                                D "Y-Yeah... I should have... You're right."
                            "It's fine. It's over and done with." if True:
                                $ corruption -= 1
                                $ damienconfidence += 1
                                show Damien Angry
                                show chelsea shocked
                                D "Still, I wish he hadn't grabbed you like that. You should never be forced into that kind of position."
                                show chelsea blank
                                show Damien Glare
                                pcname "It's fine; I'm just glad that was all that happened instead of a fight."
                        show chelsea blank
                        show Damien Blank
                        "You take another sip of your punch."
                        show Damien Shocked
                        pcname "I think I want a break from dancing for now. Let's just hang out for a bit."
                        show Damien Happy
                        "Damien looks at you, relieved."
                        show Damien Laugh
                        D "Yeah, that sounds nice."
                    "Ew, no thanks." if True:
                        $ corruption -= 5
                        show Alex Blank
                        if mattslap == 1 and bullytelloff == 1:
                            "The idea of him having his hands on you again is enough to make you feel nauseous. There's no way you can do that again: no way, not ever."
                        elif mattsubmissive == True and bullytelloff == 1:
                            "The shame of your affair with him and Matt hits you tenfold, but you can't risk dancing with him. It was a one time thing; you won't let it rule your life."
                        show chelsea angry
                        if club == "track":
                            show Damien Happy
                            pcname "Fuck off, Alex. I'm not dancing with your scrawny ass."
                            show Alex Angry
                            "Alex" "Big words for a {i}slut{/i}."
                        elif club == "cheer":
                            show Damien Happy
                            pcname "Ew. You smell like you bathed in a tub of body spray. No thanks."
                        elif club == "yearbook":
                            show chelsea sad
                            "Feeling his gaze land on your breasts, you cross your arms over your chest, the idea of dancing so close to him filling your body with fear."
                            show chelsea angry
                            show Damien Happy
                            pcname "N-No! I'm here with Damien!"
                        show chelsea blank
                        show Alex Angry
                        show Damien Glare
                        "Alex" "{i}Bitch.{/i} You really are deranged."
                        "Alex" "Why stand up for this freak? Don't tell me you're into his weird shit?"
                        if damienconfidence >= 50:
                            show Damien Angry
                            show Alex Blank
                            D "I think it's time you left, Alex."
                            show Alex Serious
                            show Damien Glare
                            "Alex" "Tch. Since when did {i}you{/i} become all confident? You think because you have a girlfriend now that it changes anything?"
                            show Alex Laugh
                            "Alex" "Whatever. She'll see what a piece of shit you are and leave you. Just give it time."
                        elif True:
                            show Damien Worry
                            show Alex Happy
                            D "P-Please go, Alex. We're trying to have a nice time..."
                            show chelsea shocked
                            "Alex makes a face and pitches his voice high, mocking Damien."
                            show Alex Laugh
                            show Damien Sad
                            show chelsea sad
                            "Alex" "'We're trying to have a nice time!' What a load of bullshit."
                            show Alex Serious
                            "Alex" "I have no idea why the fuck she's with your pathetic ass, but give it time. I can't wait to see her leave you crying like the little bitch you are."
                        hide Alex with dissolve
                        show chelsea sad
                        "Flipping Damien off as he turns, Alex leaves the dance floor."
                        show Damien Worry
                        "Damien sighs deeply and shakes his head."
                        show Damien Neutral
                        D "I'm so sorry about that, [pcname]. I never meant for you to get wrapped up in that."
                        show Damien Sad
                        show chelsea embarrassed
                        pcname "It's fine; I think I'm tired of dancing, though."
                        show Damien Worry
                        show chelsea blank
                        "Damien frowns, nodding in agreement."
                        D "Yeah... Yeah. Me, too."
                        show chelsea embarrassed
                        pcname "Mind if we get some punch?"
                        show Damien Laugh
                        D "Sure."
                        "You take Damien's arm and make your way to the punch bowl."
            "Maybe later." if True:
                $ damienconfidence -=1
                show chelsea sad
                if club == "track":
                    "You look back at the dance floor with disappointment. There's nothing energetic about this beat, nothing that would make {i}you{/i} want to dance, anyway."
                    "Do all dances play bad music?"
                    show chelsea blank
                    show Damien Sad
                    pcname "Uh, no thanks. Let's wait until a better song comes on."
                elif club == "cheer":
                    "Looking at the group of dancing students on the floor, you wrinkle your nose in disgust. Most of them look untidy and sweaty, no doubt."
                    show chelsea blank
                    show Damien Sad
                    pcname "I'd rather do something else; we should wait until some cooler kids show up and dance."
                elif club == "yearbook":
                    "The idea of having to jump right into dancing with that big group of people sends a jolt of fear through your body."
                    "No doubt you'll stumble over your own feet and make a fool of yourself."
                    show chelsea embarrassed
                    show Damien Sad
                    pcname "M-Maybe later..."
                show Damien Worry
                show chelsea blank
                D "O-Oh. Okay."
                show Damien Laugh
                D "How about we grab some punch instead?"
                show chelsea happy
                show Damien Happy
                pcname "Sounds great."
                scene bg Gym with dissolve
                "You follow Damien to the buffet of food where several pizza boxes, snacks, cans of soda, and large bowls of red punch are waiting for you."
                "Damien grabs some plates of food while you take care of the punch, meeting each other on the bleachers when your hands are full."
                "You both look out across the gymnasium, searching for anyone you might find familiar, but the strobe lights make it nearly impossible."
                show Damien Neutral with dissolve
                D "They're kind of hard to look at, aren't they? The lights, I mean."
                show Damien Blank
                show chelsea sad at center, moveSprite(0.7, 0.7, 0.0) with dissolve
                pcname "Yeah. It's kind of hard to see."
                show chelsea blank
                "You finish the rest of your pizza and chips while Damien sips at his punch beside you, seemingly uninterested in everything else going on around him."
                show chelsea confused
                show Damien Shocked
                pcname "Are you okay?"
                show Damien Neutral
                show chelsea blank
                D "H-huh? Oh, yeah. I'm fine. Why do you ask?"
                show Damien Blank
                show chelsea confused
                pcname "You just seem kind of zoned out, I guess."
                show chelsea blank
                show Damien Worry
                D "Oh. I'm fine. I just... I haven't been to a dance in a while is all. I don't actually know what to do other than drink and dance."
                show chelsea embarrassed
                show Damien Shocked
                pcname "I can relate. I've never been to a dance... ever."
                show Damien Neutral
                D "Wait, {i}ever{/i} ever? Like, this is your first one?"
                show Damien Blank
                "You nod in confirmation."
                show Damien Laugh
                show chelsea blank
                D "Oh, wow... I'm sorry, I thought you'd gone to one before. That makes this kind of exciting then, right?"
                show Damien Neutral
                D "Are you enjoying yourself so far?"
                menu damien_homecoming_enjoy:
                    "Yeah, I'm having a really nice time." if True:
                        $ corruption -= 1
                        show chelsea laugh
                        show Damien Happy
                        "Damien smiles in relief."
                        D "I'm glad."
                    "It could be better." if True:
                        $ corruption += 1
                        show chelsea sad
                        show Damien Worry
                        D "Ah, yeah... That's fair."
                        show Damien Laugh
                        show chelsea blank
                        D "The dance did just start, though. We have the whole night ahead of us."
                        show chelsea embarrassed
                        show Damien Happy
                        pcname "That's true."
                show chelsea shocked
                show Damien Shocked
                show Alex Laugh at left with dissolve
                "Alex" "I bet she'd be enjoying it a lot more if she had a better date."
                show Alex Happy
                "You and Damien both look up, startled to see Alex standing over you, a confident smirk on his face."
                show Damien Sad
                if mattslap == 1 and bullytelloff == 1:
                    show chelsea sad
                    "You feel your heart beat unevenly, the reminder of Matt and Alex's hands on you as they pinned you down in the alley resurfacing in your mind."
                    "A sickening feeling settles in your stomach and you force yourself to look away to hide the tears brimming in your eyes."
                if mattsubmissive == True and bullytelloff == 1:
                    show chelsea embarrassed
                    "Shame heats your face as you lock eyes with Alex, all of the indecent acts you committed with him and Matt in your classroom resurfacing in your mind."
                    show chelsea sad
                    "Panic swells in your chest but you try to push it down."
                    "What if he mentions something to Damien? You aren't sure you're prepared for that kind of confrontation."
                show Damien Worry
                "Damien sighs, already looking defeated."
                if damienconfidence >= 50:
                    show Damien Angry
                    show Alex Blank
                    D "What do you want, Alex?"
                    show Damien Glare
                    show Alex Serious
                    "Alex" "First I'd like to know how the fuck you scored [pcname] as a date. How much did you pay for her?"
                    show Alex Blank
                    "Damien glares up at Alex and I can practically hear the grinding of his teeth."
                    show Damien Angry
                    show Alex Happy
                    D "I'd appreciate if you didn't talk about my {i}girlfriend{/i} like that."
                elif True:
                    show Damien Neutral
                    show Alex Blank
                    D "H-Hey, Alex..."
                    show Damien Shocked
                    show Alex Angry
                    "Alex" "Don't 'hey Alex' me; how the fuck did you score this one?"
                    show Damien Sad
                    show Alex Blank
                    "Alex gestures vaguely toward you."
                    show Alex Serious
                    "Alex" "She's {i}lightyears{/i} out of your league!"
                    show Damien Worry
                    show Alex Blank
                    D "W-Well, [pcname] is my girlfriend, so-"
                show Alex Serious
                show Damien Shocked
                "Alex" "{i}Girlfriend?!{/i}"
                show Damien Glare
                show Alex Laugh
                "Alex" "No fucking way! No girl is crazy enough to date your creepy, loner ass."
                show Damien Shocked
                "Alex" "Especially not after that incident with-"
                show Alex Happy
                if damienconfidence >= 50:
                    show Damien Angry
                    D "{i}Are you done, Alex?{/i} Or are you going to keep bothering us all night?"
                elif True:
                    show Damien Worry
                    D "A-Alex, please leave us alone..."
                show Damien Glare
                show Alex Laugh
                "Alex" "Oh, I'll leave you alone, but first..."
                show Alex Happy
                "Alex looks you over with a sharp grin, his gaze roving over the curves of your body that are exposed by your dress."
                show Alex Neutral
                "Alex" "I think I want a dance with your little girlfriend first."
                show Alex Happy
                if damienconfidence >= 50:
                    show Damien Angry
                    D "No way! Go find someone else to harass, Alex, but leave my girlfriend out of it."
                elif True:
                    show Damien Worry
                    D "I-I don't think that's a good idea... I'm not comfortable with that..."
                show Alex Laugh
                show Damien Glare
                "Alex" "How about we ask your actual girlfriend instead of you making decisions for her, huh?"
                "Alex" "What do you say, [pcname]? Wanna dance?"
                menu damien_homeccoming_alex:
                    "Fine, I'll dance with you." if True:
                        $ corruption += 2
                        show Alex Blank
                        if mattslap == 1 and bullytelloff == 1:
                            "You feel sick at the idea of touching him again, but if it means he'll leave you and Damien alone for the rest of the night, you're willing to make that sacrifice."
                        if mattsubmissive == True and bullytelloff == 1:
                            "You aren't really in any position to deny him, especially if you want Alex to keep quiet about your threesome with Matt."
                        show chelsea blank
                        show Alex Happy
                        show Damien Sad
                        if club == "track":
                            pcname "If it gets you to back off, sure, I'll dance."
                        elif club == "cheer":
                            pcname "Ugh, fine, whatever. Just leave us alone after this."
                        elif club == "yearbook":
                            pcname "W-Will you leave us alone if I do?"
                            "Alex's lips twist into a wicked grin. He raises up a hand, staring at Damien as he speaks."
                            show Alex Laugh
                            "Alex" "Scout's honor."
                            show chelsea sad
                            pcname "T-Then... Then I guess so..."
                        show Damien Worry
                        show chelsea blank
                        D "[pcname], you really don't have to do this-"
                        show chelsea shocked
                        pause 0.3
                        scene black with dissolve
                        "But Alex already has you in his arms, his hands roaming between your waist and your ass as he drags you toward the dance floor."
                        scene black with dissolve
                        if damienconfidence >= 50:
                            "You glimpse Damien jumping up from his seat on the bleachers, prepared to chase after you, but Alex whirls you around and out of sight."
                        elif True:
                            "You glimpse Damien sitting dejectedly on the bleachers, but Alex whirls you around and out of sight."
                        if mattslap == 1 and bullytelloff == 1:
                            scene black with dissolve
                            "You try to hold back your tears at his touch, biting down hard on your lip. You count down the seconds until the song is over, trying to keep from throwing up."
                            "Although, maybe it would be nice to vomit on him in front of everyone."
                        if mattsubmissive == True and bullytelloff == 1:
                            scene black with dissolve
                            "The feeling of his hands once again on your body sends a thrill through you, reminding you of every touch he gave beneath your clothes."
                            "You don't want to enjoy it, but a part of you just can't help it."
                        "Alex grinds you against him on the dance floor, feeling your body up between his splayed fingers."
                        "Alex" "Man, you're wasting your time on that freak. He doesn't appreciate you like a real man would."
                        scene black with dissolve
                        if club == "track":
                            if mattslap == 1 and bullytelloff == 1:
                                "You glare at him, imagining all the different ways you could hurt him in the same way he hurt you."
                                pcname "Real men don't rape, asshole."
                                "Alex snorts, shaking his head."
                                "Alex" "You liked it; I saw how wet you were. Don't even try to deny it."
                                "Shame floods your cheeks and you grit your teeth, wishing more than anything that you could punch him here and now."
                                pcname "God, you're disgusting. I'm done; get the fuck away from me. I'm going back to Damien-"
                            "You elbow him hard, putting some space between you. Alex grunts but recedes a little."
                            pcname "I don't see a real man here."
                        elif club == "cheer":
                            if mattslap == 1 and bullytelloff == 1:
                                "You glare at him with pure hatred in your eyes, your throat raw from all the tears you've held in."
                                pcname "That's funny coming from a {i}rapist.{/i}"
                                "You say the last word a little louder, hoping to catch the ear of one of your fellow students."
                                "Alex forces you closer against him, his breath hot and threatening in your ear."
                                "Alex" "I'd watch it if I were you. Don't think I won't try it a second time."
                                "His words send an icy chill down your spine. You stare at him in disgust, your stomach in knots."
                                pcname "You aren't even {i}half{/i} the man Damien is-"
                            "You can't help rolling your eyes."
                            pcname "And {i}you{/i} think you're a real man? Please. My bunny slippers look manlier than you."
                        elif club == "yearbook":
                            "You try to put some space between you and Alex, but he holds you firmly against him."
                            if mattslap == 1 and bullytelloff == 1:
                                pcname "A-A real man doesn't... doesn't r-rape..."
                                "Your voice cracks on the last word, a few tears spilling down your face."
                                "Alex snorts and leans in close, his breath hot in your ear."
                                "Alex" "You liked it. Don't even pretend you didn't."
                                pcname "I-I didn't!"
                                pcname "L-Let me go. Damien's waiting for me-"
                            elif True:
                                pcname "A-A real man wouldn't pick on another man and his girlfriend..."
                        "Alex laughs."
                        "Alex" "Man, he's really got you under some freak spell, doesn't he?"
                        "Alex" "The kid is a fucking loser. There's a reason he doesn't have any friends."
                        pcname "Maybe the reason is because of people like {i}you.{/i}"
                        "Alex" "Sure. Keep telling yourself that; whatever makes you sleep at night, baby."
                        scene black with dissolve
                        "Alex drags you against him for one last spin before the song draws to a close."
                        if mattslap == 1 and bullytelloff == 1:

                            "Before you can pull away, Alex leans toward you, a shit-eating grin on his face."
                            "Alex" "I'll tell Matt you said hi."
                            "You choke on a sob and push away from him."
                        if mattsubmissive == True and bullytelloff == 1:

                            "Before you can pull away, Alex leans toward you, a shit-eating grin on his face."
                            "Alex" "I'll tell Matt you said hi."
                            "Your cheeks flush but you push away from him, putting some distance between you two."
                        "Alex" "Have fun with your weak ass bitch."
                        scene bg Gym with fade
                        "Alex doesn't object as you scurry back through the dance floor."
                        show Damien Glare at left with dissolve
                        "You find Damien near the punch bowl, two full cups in his hands."
                        show Damien Shocked
                        show chelsea with dissolve
                        pause 1.0
                        show Damien Worry
                        "He looks both relieved and ashamed as he lifts his gaze to meet yours."
                        show Damien Neutral
                        D "Hey."
                        show Damien Blank at moveSprite(0.0, 0.3, 0.4)
                        show chelsea embarrassed
                        "He offers you one of the cups. You gladly take it."
                        show Damien Worry
                        show chelsea blank
                        D "Are you okay?"
                        show Damien Blank
                        show chelsea sad
                        pcname "Yeah, I'm fine."
                        show chelsea blank
                        "You both sip your punch for a few moments in silence."
                        show Damien Worry
                        D "I'm sorry you ended up dancing with him. I wish I could have done more-"
                        menu damien_homecoming_alexaftermath:
                            "You should have done more." if True:
                                $ corruption += 1
                                $ damienconfidence -=1
                                show chelsea sad
                                show Damien Sad
                                "Damien looks down at his feet, ashamed. He nods."
                                show Damien Worry
                                D "Y-Yeah... I should have... You're right."
                            "It's fine. It's over and done with." if True:
                                $ corruption -= 1
                                $ damienconfidence += 1
                                show Damien Angry
                                show chelsea shocked
                                D "Still, I wish he hadn't grabbed you like that. You should never be forced into that kind of position."
                                show Damien Glare
                                show chelsea blank
                                pcname "It's fine; I'm just glad that was all that happened instead of a fight."
                        show Damien Blank
                        show chelsea blank
                        "You take another sip of your punch."
                        show Damien Shocked
                        pcname "I think I want a break from eating for now. Let's just hang out for a bit."
                        show Damien Happy
                        "Damien looks at you, relieved."
                        show Damien Laugh
                        D "Yeah, that sounds nice."
                    "Ew, no thanks." if True:
                        $ corruption -= 5
                        show Alex Blank
                        if mattslap == 1 and bullytelloff == 1:
                            "The idea of him having his hands on you again is enough to make you feel nauseous. There's no way you can do that again: no way, not ever."
                        if mattsubmissive == True and bullytelloff == 1:
                            "The shame of your affair with him and Matt hits you tenfold, but you can't risk dancing with him. It was a one time thing; you won't let it rule your life."
                        show chelsea angry
                        show Damien Happy
                        if club == "track":
                            pcname "Fuck off, Alex. I'm not dancing with your scrawny ass."
                            show Alex Angry
                            "Alex" "Big words for a {i}slut{/i}."
                        elif club == "cheer":
                            pcname "Ew. You smell like you bathed in a tub of body spray. No thanks."
                        elif club == "yearbook":
                            show chelsea sad
                            "Feeling his gaze land on your breasts, you cross your arms over your chest, the idea of dancing so close to him filling your body with fear."
                            show chelsea angry
                            pcname "N-No! I'm here with Damien!"
                        show Alex Serious
                        show chelsea blank
                        show Damien Glare
                        "Alex" "{i}Bitch.{/i} You really are deranged."
                        show Alex Laugh
                        "Alex" "Why stand up for this freak? Don't tell me you're into his weird shit?"
                        if damienconfidence >= 50:
                            show Alex Blank
                            show Damien Angry
                            D "I think it's time you left, Alex."
                            show Alex Angry
                            show Damien Glare
                            "Alex" "Tch. Since when did {i}you{/i} become all confident? You think because you have a girlfriend now that it changes anything?"
                            show Alex Serious
                            "Alex" "Whatever. She'll see what a piece of shit you are and leave you. Just give it time."
                        elif True:
                            show Damien Worry
                            show Alex Happy
                            D "P-Please go, Alex. We're trying to have a nice time..."
                            "Alex makes a face and pitches his voice high, mocking Damien."
                            show Alex Laugh
                            show Damien Sad
                            "Alex" "'We're trying to have a nice time!' What a load of bullshit."
                            show Alex Angry
                            "Alex" "I have no idea why the fuck she's with your pathetic ass, but give it time. I can't wait to see her leave you crying like the little bitch you are."
                        hide Alex with dissolve
                        "Flipping Damien off as he turns, Alex heads to the dance floor alone."
                        show Damien Glare
                        show chelsea sad
                        "Damien sighs deeply and shakes his head."
                        show Damien Neutral
                        D "I'm so sorry about that, [pcname]. I never meant for you to get wrapped up in that."
                        show Damien Shocked
                        show chelsea blank
                        pcname "It's fine; I think I'm tired of eating, though."
                        show Damien Sad
                        "Damien frowns, nodding in agreement."
                        show Damien Worry
                        D "Yeah... Yeah. Me, too."
                        show chelsea embarrassed
                        show Damien Happy
                        pcname "Mind if we take some pictures by the props?"
                        show Damien Laugh
                        D "Sure."
                        show Damien Happy
                        "You take Damien's arm and make your way to the large fake palm trees propped up against a wall."
        scene bg Gym with dissolve
        "For the rest of the night, you and Damien take your time moving between the dance floor, the buffet of food, and the props for pictures."
        scene bg Gym
        show Alex Laugh at center, moveSprite(0.7, 0.7, 0.0)
        show Matt Casual Pleased at center, moveSprite(0.3, 0.3, 0.0)
        with dissolve
        "Thankfully, Alex leaves you alone, busying himself with other friends of his while you and Damien enjoy the rest of the dance by yourselves."
        scene black with fade
        "Before you know it, it's 10:00pm: the dance is over, and it's time to go home."
        scene bg CityN
        show chelsea embarrassed at left, moveSprite(0.3, 0.3, 0.0)
        show Damien Blank at left, moveSprite(0.5, 0.5, 0.0)
        with fade
        "Damien pulls up to your apartment and parks on the street. He helps hold you up, your feet aching, as you wobble to the front door."
        scene bg HomeN with dissolve
        "As soon as you're in the apartment, you kick off your shoes and collapse on the couch."
        "Damien chuckles but removes his shoes as well, shutting the door closed behind him before joining you on the couch."
        scene black with dissolve
        "You cuddle up beside him and rest your head on his lap. Damien smiles and runs his fingers through your hair."
        "You take a few moments to enjoy cuddling on the couch together, the exhaustion of the night coming over you."
        pcname "I need to take off my dress still..."
        D "Are you uncomfortable in it?"
        pcname "A little bit; I've been wearing it all night."
        D "How about you go get changed and I order us some take-out? Then we can watch a movie or something, if you want."
        "You turn in his lap to smile up at him."
        pcname "That sounds great."
        scene black with fade
        "You sit up and stretch, your joints cracking as you stand up and make your way to your room."
        jump damien_homecoming_aftermath
    elif True:
        jump damien_homecoming_alt

label damien_homecoming_alt:
    $ damienAttire(2)
    scene bg HomeE
    show chelsea
    with fade
    "About a quarter to six, you hear Damien knocking at your front door, but you're currently preoccupied with filling up your purse in the living room."
    show chelsea happy
    pcname "Come in!"
    show chelsea embarrassed
    show Damien Happy at right with dissolve
    "Damien enters your apartment, a smile on his face."
    show Damien Laugh
    D "You ready to go?"
    show chelsea blank
    show Damien Happy
    pcname "I think so... You never did say where we were going, so I had to pack a little bit of everything."
    if damienconfidence >= 50:
        "Damien winks at you."
        show chelsea embarrassed
        show Damien Laugh
        D "That's because it's going to be a surprise."
    elif True:
        "Damien gives you a hopeful smile, but you can see the fear underneath it."
        show chelsea embarrassed
        show Damien Laugh
        D "W-Well, it's a surprise. I hope you like it..."
    show chelsea blank
    show Damien Blank
    "He glances at your purse."
    show Damien Neutral
    D "That's a lot of stuff; are you sure you'll need all of it?"
    show chelsea happy
    show Damien Blank
    pcname "Better safe than sorry, right?"
    scene black with fade
    "Damien shrugs before nodding in agreement and leading you outside to his car; a sleek black vehicle still with that new car smell."
    "Once you're both in and safely buckled, Damien starts up the car."
    show chelsea confused with dissolve
    pcname "Is this car yours?"
    hide chelsea with dissolve
    if damienconfidence >= 50:
        show Damien Laugh with dissolve
        D "I wish; it's my dad's. My car is getting inspected right now, but he let me borrow it for the night."
    elif True:
        show Damien Neutral with dissolve
        D "O-Oh, no... It's my dad's. I have a car, though! It's just getting inspected."
    hide Damien with dissolve
    show chelsea with dissolve
    pcname "Oh."
    hide chelsea with dissolve
    "You look around the car, surprised by how nice it is. You can't help but wonder what Damien's dad does to warrant such a nice vehicle."
    "Come to think of it, you don't know much about Damien's family at all."
    show Damien Laugh with dissolve
    D "Ready?"
    hide Damien with dissolve
    show chelsea laugh with dissolve
    pcname "Yep!"
    hide chelsea with dissolve
    if damienconfidence >= 50:
        show Damien Laugh with dissolve
        D "Good. It's my first time actually driving anywhere, so hold on tight."
        hide Damien with dissolve
        show chelsea sad with dissolve
        "Damien stares at the nervous look on your face for a moment before breaking out into a wide grin."
        hide chelsea with dissolve
        show Damien Laugh with dissolve
        D "I'm teasing. Relax, we'll be there soon."
    elif True:
        show Damien Worry with dissolve
        D "S-So, um, you don't mind that I don't have a license, right?"
        hide Damien with dissolve
        show chelsea shocked with dissolve
        "Your heart drops into your stomach with a sudden panic."
        pcname "What?!"
        hide chelsea with dissolve
        show Damien Laugh with dissolve
        D "K-Kidding! I'm just kidding. I've been driving for two years already, don't worry. We'll be there soon."
    hide Damien with dissolve
    show chelsea embarrassed with dissolve
    "You take a deep, relieved sigh and recline into the passenger seat. Damien puts some music on the radio and drives."
    hide chelsea with dissolve
    pcname "...A bowling alley?"
    scene bg CityD with dissolve
    "Sure enough, Damien parks in front of an old 1950's styled bowling alley. A large neon-lit bowling pin displays the name of the establishment- '{i}LEROY'S LANES{/i}'- in bold red letters."
    show Damien Neutral with dissolve
    D "Yeah. My parents used to take me and my little brother here all the time as kids; it's been a while, but I found out the old place was still open and thought you might like it."
    show chelsea at left with dissolve
    D "Have you ever been bowling before?"
    menu damien_bowling:
        "Yeah, plenty of times." if True:
            show chelsea laugh
            show Damien Laugh
            D "That's great! You'll already know how to play then."
            show chelsea embarrassed
            show Damien Happy
            D "Bowling with my family is really nostalgic for me, so I'm excited to share it with you, [pcname]."
        "No, never." if True:
            show chelsea embarrassed
            show Damien Shocked
            D "Really?! Oh, wow."
            show Damien Laugh
            D "Well, I hope you like it, [pcname]!"
    scene black with fade
    "Damien leads you into the building, which matches the vintage aesthetic on the outside."
    "A concession stand with old-timey diner chairs and tables sits on the left while the rental desk sits on the right. A vast array of bowling lanes spread out in front of you, filled with groups of all ages playing the game."
    show Damien Laugh with dissolve
    show chelsea at center, moveSprite(0.3, 0.3, 0.0) with dissolve
    D "Here we are! What do you think?"
    menu damien_bowling2:
        "This is super lame." if True:
            $ damienconfidence -= 1
            show chelsea sad
            show Damien Blank
            if club == "track":
                "You look around the bowling alley with distaste. You're all for physical sports, but this looks so... so... {i}boring!{/i}"
                show chelsea laugh
                show Damien Sad
                pcname "You couldn't have come up with anything better to do?"
            elif club == "cheer":
                "You wrinkle your nose in disgust at the aging atmosphere of the bowling alley. It obviously hasn't been updated in quite some time."
                show Damien Sad
                pcname "It smells like a nursing home in here."
            elif club == "yearbook":
                "There's something disturbing about the fluorescent lights as they shine down on the wooden bowling lanes and the ancient-ness surrounding the bowling alley itself."
                "You feel like you might have walked straight into a horror movie."
                show Damien Sad
                pcname "T-This place seems really creepy..."
            show chelsea blank
            "Damien's smile drops at once and he hangs his head in shame."
            show Damien Worry
            D "I-I'm sorry... I just thought... I thought it might be nice to try it out together..."
            show chelsea shocked
            D "Do you want to go somewhere else?"
            show chelsea blank
            show Damien Sad
            "You sigh and shake your head."
            show chelsea sad
            pcname "No, we're already here, so we might as well stay."
        "This looks like fun!" if True:
            $ damienconfidence += 1
            show chelsea happy
            show Damien Blank
            if club == "track":
                "You grin at the bowling alley, thrilled that Damien chose something a little more athletic for your date."
                "Bowling wouldn't have been your {i}first{/i} choice, but you're excited to get some physical activity in!"
                show chelsea laugh
                pcname "This looks great! Thanks for taking me here, Damien!"
            elif club == "cheer":
                "You look around at the vintage bowling alley, taking in all of its little quirks that haven't been changed since its original opening date."
                "Some might think it's outdated, but to you, it just adds more character."
                show chelsea laugh
                pcname "I think it's totally cute! I can almost see myself walking around in a poodle skirt. This will be fun!"
            elif club == "yearbook":
                "You smile a little at the bowling alley, pleased that he didn't choose a more physically intensive sport."
                "Although it's a little crowded, you doubt you'll mind or even notice once you and Damien are in your own lane."
                show chelsea laugh
                pcname "T-This looks fun!"
            show Damien Happy
            show chelsea embarrassed
            "Damien smiles in relief."
            show Damien Laugh
            D "Cool! Let's go get our shoes then."
    scene black with dissolve
    "You follow Damien to the rental desk and trade out your shoes before making your way to Lane 12."
    "You both change out your shoes and Damien sets up the first game on the computer screen."
    show Damien Laugh with dissolve
    D "I bought enough for us to play three games, but if you want to play any longer, just let me know!"
    show Damien Happy
    show chelsea laugh at center, moveSprite(0.3, 0.3, 0.0) with dissolve
    pcname "Okay!"
    show chelsea blank
    show Damien Blank
    "Damien takes his turn first, more familiar with the game than you are, and rolls the ball down the lane."
    show Damien Glare
    "A screen above flashes as two pins are knocked over."
    show Damien Worry
    "Damien turns back to you with a sheepish grin."
    show chelsea embarrassed
    D "I guess I'm not as well practiced as I remember."
    show Damien Angry
    D "That's okay! Just gotta get back into it, give it some time..."
    show chelsea blank
    show Damien Blank
    "Damien rolls the ball again, knocking down another pin."
    show Damien Laugh
    D "You're up, [pcname]!"
    show Damien Blank
    "You nod, picking up and weighing the various balls from the rack. You settle on a blue one with a comfortable weight before making your way to the starting line."
    show chelsea angry
    "You swing your arm back. On one... two... three...!"
    show chelsea happy
    pause 1.0
    show chelsea sad
    show Damien Worry
    "The ball soars forward and veers directly into the gutter."
    pcname "Oh..."
    show Damien Laugh
    show chelsea embarrassed
    D "That's okay, [pcname]! Try again! It just takes some practice."
    show Damien Happy
    show chelsea blank
    "You nod and wait for your ball to return before giving it another go."
    show chelsea sad
    show Damien Sad
    "Your ball once again rolls into the gutter."
    "Perhaps bowling isn't among your talents..."
    scene black
    show chelsea at center, moveSprite(0.3, 0.3, 0.0)
    show Damien Blank
    with fade
    "A few hours later and you and Damien are on your last game of the night."
    "You stare down at the end of the aisle, eyeing up the arrows marked on the lane."
    "Taking a deep breath, you roll your arm back and send the ball forward."
    show chelsea angry
    pcname "Come on, come on...!"
    show chelsea blank
    show Damien Angry
    D "You can do it, [pcname]!"
    show Damien Blank
    "The ball rolls forward..."
    show chelsea laugh
    show Damien Laugh
    "{i}STRIKE!{/i}"
    "The screen above flashes with excitement. You let out a little squeal and throw your arms around Damien's shoulders."
    "He picks you up and spins you around, laughing."
    show chelsea embarrassed
    pcname "I did it, I did it!"
    D "You did! Congrats, [pcname]!"
    show Damien Happy
    "Damien sets you back down onto your feet and presses a kiss on top of your head, squeezing you close into another hug."
    show chelsea shocked
    show Damien Shocked
    show Alex Serious at right with dissolve
    "Alex" "Ha. I was wondering where the fuck you were."
    show chelsea blank
    show Damien Glare
    show Alex Blank
    "The joyful moment of your win diminishes as Alex walks into the bowling alley with a few of his friends, his suit rumpled from the night; he must have been at homecoming."
    if mattslap == 1 and bullytelloff == 1:
        show chelsea sad
        "You feel your heart beat unevenly, the reminder of Matt and Alex's hands on you as they pinned you down in the alley resurfacing in your mind."
        "A sickening feeling settles in your stomach and you force yourself to look away to hide the tears brimming in your eyes."
    if mattsubmissive == True and bullytelloff == 1:
        show chelsea embarrassed
        "Shame heats your face as you lock eyes with Alex, all of the indecent acts you committed with him and Matt in your classroom resurfacing in your mind."
        show chelsea sad
        "Panic swells in your chest but you try to push it down."
        "What if he mentions something to Damien? You aren't sure you're prepared for that kind of confrontation."
    show Alex Neutral
    "Alex" "I figured the freak would stay home, but I didn't think he'd be out here with {i}you{/i}."
    show Alex Happy at center, moveSprite(1.0, 0.8, 0.4)
    "Alex smirks as he walks toward you both. A man from behind the desk calls out for Alex to change his shoes before stepping on the lanes, but Alex waves him off."
    if damienconfidence >= 50:
        show Damien Angry
        D "What are you doing here, Alex?"
        show Damien Glare
        show Alex Blank
        "Damien places a protective arm around your waist, pulling you tightly against his side. Alex's eyebrows raise, surprised by his new wave of confidence."
    elif True:
        show Damien Worry
        D "H-Hey, Alex... Why are you here?"
        show Damien Sad
        "Damien looks away uncomfortably, resting a loose hand on your waist. He doesn't look ready at all for this sort of confrontation."
    show Alex Laugh
    "Alex" "Me and the boys here got kicked out of the dance early, so we decided to have some fun somewhere else."
    show Damien Glare
    "Alex" "But it looks like the fun's come to me instead!"
    show Alex Serious
    "Alex" "So what the fuck are you doing here with {i}her?{/i} Was she too ashamed to be seen with you at the dance? Or did you have to pay her to even go out with you?"
    show Alex Blank
    if damienconfidence >= 50:
        show Damien Angry
        D "I'd appreciate it if you stopped talking about my girlfriend that way."
    if damienconfidence < 50:
        show Damien Worry
        D "S-She's my girlfriend..."
    show Alex Neutral
    show Damien Glare
    "Alex" "Your {i}what?!{/i}"
    show Alex Laugh
    "Alex throws his head back and cackles."
    "Alex" "No fucking way {i}she's{/i} your girlfriend. No one is stupid enough to date your crazy, loner ass!"
    show Alex Neutral
    show Damien Shocked
    "Alex" "Not since the 'incident', anyway."
    show Alex Blank
    show chelsea confused
    pause 1.0
    show chelsea blank
    "You open your mouth to ask about what he means, but the look on Damien's face tells you that he doesn't want to talk about it. Maybe another time..."
    show Damien Glare
    show Alex Laugh
    "Alex" "How much did you pay for her? You think she'd ditch you to hang out with me if I paid her more?"
    show chelsea sad
    "Alex" "What about it, [pcname]?"
    if damienconfidence >= 50:
        show Damien Angry
        show Alex Happy
        D "Shut up about [pcname]! Get out of here, Alex."
        show Alex Laugh
        show chelsea blank
        show Damien Glare
        "Alex" "Or what? You'll sick your girlfriend on me? Ha!"
    elif True:
        show Damien Worry
        show Alex Happy
        D "I-I..."
        show chelsea blank
        "Damien looks like he wants to argue, but can't find the courage to do so. You feel both pitiful and frustrated with him."
    menu damien_bowling_alex:
        "Stand up to Alex." if True:
            $ corruption -= 5
            show Alex Happy
            if mattslap == 1 and bullytelloff == 1:
                "The reminder of his hands on your body in the alleyway is enough to get your blood boiling."
                "This is about more than just Damien's pride; your own dignity was ruined by him, and you'll be damned if he tries to take anything else."
            if mattsubmissive == True and bullytelloff == 1:
                "Just because you had sex with him once doesn't mean you're about to let him bully your boyfriend; Damien deserves better than that."
            if club == "track":
                show chelsea angry
                show Damien Shocked
                pcname "You wanna fight, Alex? I'll take you out back and handle you myself!"
                show Alex Laugh
                show Damien Worry
                show chelsea blank
                "Alex" "By handle me, you mean suck my dick, [pcname]? Cause I'd be down for that."
                show chelsea happy
                show Alex Happy
                pcname "Or cut it off, but whose to say?"
            elif club == "cheer":
                show chelsea angry
                show Damien Shocked
                pcname "Why don't you go find someone else to bother, Alex? Your tough-guy act is so lame."
                show Alex Laugh
                show Damien Worry
                show chelsea blank
                "Alex" "It's not an act, [pcname]. You'd know a real man if you dumped this loser."
                show chelsea angry
                show Alex Happy
                pcname "Real men don't bathe themselves in body spray, but thanks for the offer."
            elif club == "yearbook":
                show chelsea blank
                "Summoning all of your courage, you take a timid step forward, glaring up at Alex."
                show chelsea angry
                show Damien Shocked
                pcname "L-Leave us alone. We just came here to have fun."
                show Alex Laugh
                show Damien Worry
                show chelsea blank
                "Alex" "So did I, and I'm having a {i}blast!{/i}"
                "Alex" "But I bet it would be even more fun if you took your clothes off."
                show chelsea shocked
                show Alex Happy
                "You gasp, cringing away from him."
                show chelsea angry
                pcname "Y-You-!"
            show chelsea blank
            show Damien Blank
            "You feel Damien's hand press against your shoulder, urging you away."
            show Damien Neutral
            D "Let's just go, [pcname]."
            show Damien Blank
            show chelsea confused
            pcname "What? Why?"
            show chelsea angry
            pcname "We can't just let him bully us out!"
            show Damien Happy
            show chelsea blank
            D "It's fine; the last game was almost over. We were going to be leaving soon anyway."
            show Alex Laugh
            show Damien Glare
            "Alex laughs again, shaking his head."
            show Alex Serious
            "Alex" "You're pathetic; can't even stand up to your own fights. You need to get your {i}girlfriend{/i} to do it."
            hide Damien with dissolve
            hide chelsea with dissolve
            "Damien hangs his head in shame, but pulls you toward your seats and quickly changes out of his shoes."
            hide Alex with dissolve
            "You try to ignore Alex as he continues to taunt the two of you as you gather your things and quickly leave the bowling alley."
            scene black with fade
            "Neither of you say a word as you climb into Damien's car and he drives toward your apartment."
            show Damien Worry with dissolve
            D "...I'm sorry."
            hide Damien with dissolve
            show chelsea confused with dissolve
            pcname "Huh?"
            hide chelsea with dissolve
            show Damien Neutral with dissolve
            D "I'm sorry for tonight. I... I should have stood up to him better. I just- I freeze up every time I see Alex."
            show Damien Worry
            D "We have kind of a history together. Normally I can deal with it, but when he started to pick on you, I... I just..."
            menu damien_bowling_bullying:
                "It's okay, I'm not mad." if True:
                    $ corruption -= 1
                    $ damienconfidence += 1
                    hide Damien with dissolve
                    if club == "track":
                        show chelsea sad with dissolve
                        pcname "Don't be upset, Damien, it's not your fault. I'm just pissed that Alex came and ruined our night together."
                        show chelsea happy
                        pcname "I mean, I got a freakin' strike! That was amazing!"
                        hide chelsea with dissolve
                        show Damien Happy with dissolve
                        "Damien chuckles a little, relieved."
                        show Damien Neutral
                        D "Yeah... Yeah, that was really impressive. I'm sorry he ruined it for you."
                        hide Damien with dissolve
                        show chelsea angry with dissolve
                        pcname "Don't be. Alex is just a loser that likes to pick on people smaller than him. I'm not going to let him ruin our whole night."
                        hide chelsea with dissolve
                        show Damien Laugh with dissolve
                    elif club == "cheer":
                        show chelsea embarrassed with dissolve
                        pcname "Aw, it's okay, Damien! Don't be sad, babe."
                        show chelsea angry
                        pcname "Alex is such a jerk. He's like, a toddler that still gets off on bullying other kids because he can't always get his way."
                        show chelsea laugh
                        pcname "Don't let him get you down."
                        hide chelsea with dissolve
                        show Damien Happy with dissolve
                        "Damien smiles a little, slightly encouraged by your words."
                        show Damien Neutral
                        D "Thanks, [pcname]..."
                        hide Damien with dissolve
                        show chelsea angry with dissolve
                        pcname "Besides, he has no room to talk; he smells like a walking can of body spray. It's {i}nauseating.{/i}"
                        hide chelsea with dissolve
                        show Damien Laugh with dissolve
                        "Damien chuckles and nods."
                        show Damien Happy
                        D "Yeah, he smells pretty bad..."
                        show Damien Laugh
                    elif club == "yearbook":
                        show chelsea sad with dissolve
                        pcname "I-It's okay! Please don't be sad, Damien. I... I really don't mind."
                        show chelsea embarrassed
                        pcname "I'm just glad you're okay. I was so worried he was going to try to start a real fight..."
                        hide chelsea with dissolve
                        show Damien Laugh with dissolve
                        D "[pcname], you're too sweet."
                        show Damien Happy
                        "Damien reaches a hand over to yours and squeezes it, giving you a relieved smile."
                        show Damien Laugh
                    D "Thank you so much for standing up for me. It means so much... You have no idea."
                    show Damien Worry
                    D "I'll always be here for you, too, [pcname], even if... even if I struggle sometimes. I hope you can be patient with me..."
                    hide Damien with dissolve
                    show chelsea embarrassed with dissolve
                    pcname "Of course. I'm happy with you, Damien."
                    hide chelsea with dissolve
                    show Damien Laugh with dissolve
                    "He lets out a breathless laugh, tears pricking his eyes, before quickly turning back toward the road and driving you home."
                "I can't believe you didn't stand up for me more." if True:
                    $ corruption += 1
                    $ damienconfidence -= 1
                    hide Damien with dissolve
                    show chelsea sad with dissolve
                    if club == "track":
                        pcname "I just- I can't believe you didn't stand up for me more, Damien."
                        show chelsea angry
                        pcname "You heard me in there; I was ready to throw hands for you!"
                        hide chelsea with dissolve
                        show Damien Sad with dissolve
                        "Damien winces, gripping the steering wheel even tighter."
                        show Damien Worry
                    elif club == "cheer":
                        pcname "You know, it's supposed to be the {i}boyfriend's{/i} job to stand up for the girl."
                        show chelsea angry
                        pcname "It was pretty pathetic that I had to defend us both in there while you just stared at him."
                        hide chelsea with dissolve
                        show Damien Worry with dissolve
                    elif club == "yearbook":
                        show chelsea sad
                        pcname "I-I just wish that... that you had said more to him..."
                        show chelsea embarrassed
                        pcname "I freeze up too, y-you know, but even I... Even I managed to tell him off..."
                        hide chelsea with dissolve
                        show Damien Worry with dissolve
                    D "I-I know. That's what makes this even more embarrassing..."
                    D "I want to be someone that you can rely on, [pcname], no matter what. The fact I couldn't be that tonight is mortifying."
                    show Damien Neutral
                    D "But I'm going to keep trying, [pcname], because... because you mean a lot to me."
                    show Damien Angry
                    D "I hope I can make it up to you."
                    hide Damien with dissolve
                    "Damien bites down on his lip and focuses on the road, but you can tell he's anxious about the evening's events."
                    show chelsea sad with dissolve
                    "You can't just let the date end that badly; things were going so well until Alex showed up, after all."
                    show chelsea happy
                    pcname "That was my first strike ever."
                    hide chelsea with dissolve
                    show Damien Shocked with dissolve
                    D "H-Huh?"
                    hide Damien with dissolve
                    show chelsea embarrassed with dissolve
                    pcname "The game- I never got a strike before. It was really fun. I can see why you like going to that place."
                    hide chelsea with dissolve
                    show Damien Happy with dissolve
                    "A small smile plays at the corners of Damien's mouth and he nods. Carefully, he places a trembling hand on your own."
                    show Damien Neutral
                    D "I'm glad. M-Maybe we can go again together some other time...?"
                    hide Damien with dissolve
                    show chelsea embarrassed with dissolve
                    pcname "Maybe. I might like that."
                    hide chelsea with dissolve
                    show Damien Happy with dissolve
                    "Damien smiles, and the atmosphere shifts comfortably as he drives you home."
        "Leave." if True:
            $ corruption -= 1
            show chelsea sad
            show Alex Happy
            if mattslap == 1 and bullytelloff == 1:
                "You can hardly bring yourself to look at Alex, every glance just another reminder of what he did to you in the alley."
                "Your stomach ties itself in anxious knots, begging to leave his presence. You can't be here anymore; you need to get out and as far away from him as possible."
            if mattsubmissive == True and bullytelloff == 1:
                "Looking at Alex, you can't tell if he'll mention your affair with him or not. If he's pushed enough, maybe he will."
                "Either way, if Damien ever had to find out, this isn't how you would tell him."
            show Damien Shocked
            "Gripping Damien's sleeve, you tug him toward your chairs and pick up your shoes."
            show Damien Worry
            D "[pcname]..."
            show chelsea blank
            show Damien Sad
            pcname "Come on, Damien, let's just go. I don't want to bowl anymore."
            show Damien Angry
            D "But we-"
            show Damien Shocked
            pcname "Our game is almost done anyway. Let's just go."
            show Damien Worry
            D "I..."
            "He looks back at Alex and you can see a million arguments on his face, but with a sigh, he relents and walks you back to your chairs."
            hide chelsea with dissolve
            hide Damien with dissolve
            show Alex Laugh
            "Alex" "Aw, c'mon, that was too easy. You're taking all the fun out of messing with you if you give up that quickly, Damien!"
            hide Alex with dissolve
            "Alex follows you both, continuing to throw insults and taunts as you gather your things and leave."
            scene black with dissolve
            "By the time you finally reach Damien's car, Alex has stopped following you, opting to stay inside with his friends."
            "Neither of you say a word as Damien starts the car and drives toward your apartment."
            "After a few minutes-"
            show chelsea sad with dissolve
            pcname "I'm sorry."
            hide chelsea with dissolve
            show Damien Neutral with dissolve
            D "What? What are you sorry for, [pcname]?"
            hide Damien with dissolve
            show chelsea sad with dissolve
            pcname "I didn't let you stand up to Alex, or talk to him, or anything. I just wanted to get out of there."
            hide chelsea with dissolve
            show Damien Blank with dissolve
            "Damien's expression softens. He reaches one hand over to hold yours while the other rests on the wheel of the car."
            show Damien Neutral
            D "You don't need to be sorry for anything, [pcname]. I'm sorry I didn't do a better job of standing up for you; that's on me."
            show Damien Laugh
            D "I want to be someone you can rely on, you know?"
            show Damien Worry
            D "But... But I kind of messed that up tonight. Alex and I have a history together, so it's not always easy to stand up to him."
            show Damien Angry
            D "I'm going to try, though; for your sake. You mean so much to me, I just..."
            show Damien Blank
            "He takes a deep breath."
            show Damien Laugh
            D "Thank you for sticking with me. [pcname]. Not a lot of people like me, but the fact you're willing to stay with me means so, so much to me."
            hide Damien with dissolve
            show chelsea embarrassed with dissolve
            "You squeeze his hand and press a kiss to his knuckles."
            pcname "Of course, Damien. I'm happy to be here with you."
            hide chelsea with dissolve
            show Damien Happy with dissolve
            "Damien grins and resumes the rest of the drive to your apartment."
    scene bg CityN with dissolve
    "Damien pulls up to your apartment and parks on the street. He holds your hand as you walk to the front door together."
    scene bg HomeN with dissolve
    "As soon as you're in the apartment, you kick off your shoes and collapse on the couch."
    "Damien chuckles but removes his shoes as well, shutting the door closed behind him before joining you on the couch."
    scene black with dissolve
    "You cuddle up beside him and rest your head on his lap. Damien smiles and runs his fingers through your hair."
    "You take a few moments to enjoy cuddling on the couch together, the exhaustion of the night coming over you."
    pcname "Ugh, I think I want to put on some comfy clothes; I'm tired of being dressed to go out."
    D "Are you uncomfortable in your clothes right now?"
    pcname "A little bit; I've been wearing them all day."
    D "How about you go get changed and I order us some take-out? Then we can watch a movie or something, if you want."
    "You turn in his lap to smile up at him."
    pcname "That sounds great."
    scene black with fade
    "You sit up and stretch, your joints cracking as you stand up and make your way to your room."
    jump damien_homecoming_aftermath

label damien_homecoming_aftermath:
    $ clothes = "naked"
    scene bg RoomN
    show chelsea
    with fade
    "Once your clothes are peeled off and tossed into the hamper, you look over your closet, half-tempted to put on your pajamas and call it a night."
    show chelsea embarrassed
    "Instead, a more exciting thought hits you."
    hide chelsea with dissolve
    if damienlingeriepurchase == True:
        "You dig through the bottom of your closet until you find the tiny pink bag from the lingerie store at the mall."
        show chelsea laugh with dissolve
        "Damien would {i}freak{/i} out if he saw you in this; in all the best ways, of course."
        hide chelsea with dissolve
        $ underwear2 = True
        $ clothes = "underwear"
        pause 1.0
        show chelsea embarrassed with dissolve
        "Slipping into the teal mesh bra and panties, you check yourself out a few times in the mirror before walking back out into the living room."
    elif True:
        "You dig through the bottom of your closet, searching for the perfect set of bra and panties."
        show chelsea happy with dissolve
        "You don't have anything fancy, but hopefully this pink pair will do the trick."
        hide chelsea with dissolve
        $ clothes = "underwear"
        pause 1.0
        show chelsea embarrassed with dissolve
        "You slip into the lingerie before walking back out into the living room."
    scene bg HomeN with fade
    "Damien doesn't look up from the take-out menu in his hand, busy talking into his cellphone. He's already changed into his pajamas; a t-shirt and joggers."
    show chelsea embarrassed at left with dissolve
    "You wait patiently in your doorway for Damien to finish his call."
    show Damien Happy with dissolve
    D "Cool. See you in twenty minutes."
    show Damien Shocked
    "Damien hangs up and finally notices you, his eyes practically bulging from his head."
    if club == "track":
        show chelsea laugh at moveSprite(0.0, 0.3, 0.3)
        "Spinning around, you show off every angle of the lingerie."
        show chelsea embarrassed
        pcname "What do you think?"
    elif club == "cheer":
        show chelsea at moveSprite(0.0, 0.3, 0.3)
        "Slipping onto the couch, you crawl toward him, your cleavage thoroughly exposed through your bra."
        pcname "Do you like it, Damien?"
    elif club == "yearbook":
        "You shift in place, playing with the ends of your hair as Damien looks you up and down."
        show chelsea at moveSprite(0.0, 0.3, 0.3)
        pcname "I-I thought, since it's a special occasion and all... U-Um, I hope you like it..."
    if damienconfidence >= 50:
        show Damien Happy
        "A grin splits across Damien's face as he takes you in."
        show Damien Laugh
        D "I {i}love{/i} it, [pcname]."
    elif True:
        show Damien Worry
        "His face bursts in various shades of pink as he stares at your body, no detail too small to hide through the lingerie."
        show Damien Neutral
        D "I-I... Y-You look..."
        show Damien Worry
        "He gulps, struggling to find the words. They come out as barely a squeak."
        D "H-Hot."
    show chelsea happy
    show Damien Happy
    "You smile, encouraged by his words, and settle yourself on top of his lap."
    if club == "track":
        show chelsea embarrassed
        show Damien Shocked
        pcname "I want to go all the way tonight."
    elif club == "cheer":
        show chelsea embarrassed
        pcname "I was thinking..."
        "You toy with the edge of his shirt, lifting it up over his stomach."
        show Damien Shocked
        pcname "Let's have sex tonight, Damien."
    elif club == "yearbook":
        show chelsea embarrassed
        "Butterflies fluttering in your stomach, you wrap your arms around his neck and play with the edge of his shirt."
        show Damien Shocked
        pcname "I-I was thinking... u-um... if-if you want to, we can... h-have... sex..."
        "The last two words barely escape your throat, and you're too embarrassed to meet his gaze as you whisper them to him."
    if damienconfidence >= 50:

        if damienlingeriepurchase == True:

            scene bg DAHS13 with dissolve
            D "{i}Yes.{/i}"
            "Damien breathes the word eagerly before pushing you down onto the couch, his lips crashing down hard against yours."
            "You gasp, surprised by his forcefulness, but melt easily into his arms."
            "You hadn't expected Damien to be so excited, but now that you're here, it just feels {i}right.{/i}"
            scene bg DAHS15 with dissolve
            "His hands roam over your body, squeezing your nipples through the see-through bra. His mouth comes down on one of your breasts, ignoring the mesh fabric in the way as he sucks and bites at it."
            "You let out a small gasp, your hips jerking toward him with anticipation."
            "Damien reaches one hand down to caress the outside of your panties, rubbing the fabric against your slit. You grind into his fingers, whimpering as the friction builds against your clit."
            "He lifts his head from your bra and kisses across your cleavage, dipping his tongue between the curves of your breasts."
            D "You're so beautiful, [pcname]... So beautiful..."
            "You feel his cock grow hard against your leg, grinding slightly as he continues to lick over your breasts and rub your panties."
            scene bg DAHS17 with dissolve
            "He slips his fingers underneath the fabric and pushes two in at once."
            "You gasp, grabbing for his shoulders hard. Damien stops at once and starts to pull his fingers away, surprised."
            D "Sorry! Was that too much at once? Did I-?"
            if club == "track":
                pcname "Don't stop!"
            elif club == "cheer":
                "You moan, jerking your hips up to dig his fingers in further."
                pcname "Keep going, Damien!"
            elif club == "yearbook":
                pcname "N-No! P-Please... More..."
            scene bg DAHS17 with dissolve
            "Relieved, Damien pushes his fingers deep inside of you, thrusting them in and out of your pussy."
            "You tilt your head back and moan, lifting your hips from the couch to grind into his hand."
            "His thumb presses down against your clit as he fingers you, rubbing the fabric there against the swollen nub."
            pcname "D-Damien!"
            "You gasp, feeling your climax building. It can't happen yet, not yet..."
            "Sensing your oncoming orgasm, Damien slows, smirking down at you as you whimper in displeasure."
            "You need more, more..."
            D "What do you want, [pcname]?"
            scene bg DAHS19 with dissolve
            "Damien slips his fingers from your pussy and presses them into your mouth; you lick them clean. You moan around his fingers, savoring the taste."
            if club == "track":
                pcname "You! I need {i}you{/i}. Right now."
            elif club == "cheer":
                "You smirk back up at him, impressed by his willingness to keep you on the edge."
                pcname "Damien... I need your nice, thick cock inside of me? Please, baby? Please?"
                "You bat your eyelashes up at him, spreading your legs wide."
            elif club == "yearbook":
                "You feel embarrassed begging, but you were so close, and his fingers felt so good...!"
                pcname "P-Please, Damien! P-Please... I-I need..."
            "Satisfied with your answer, Damien strips out of his clothes, leaving them in a messy heap on the floor, and crawls on top of you."
            "His erection is thick and stiff, pressed hard against your inner thigh. He peels the panties from your thighs, leaning down to lick your slit once as he flings them across the room."
        elif True:

            scene bg DAHS14 with dissolve
            D "{i}Yes.{/i}"
            "Damien breathes the word eagerly before pushing you down onto the couch, his lips crashing down hard against yours."
            "You gasp, surprised by his forcefulness, but melt easily into his arms."
            "You hadn't expected Damien to be so excited, but now that you're here, it just feels {i}right.{/i}"
            "His hands roam over your body, squeezing your breasts through the bra. His mouth moves one of the cups out of the way as he takes your nipple between his teeth, sucking and biting."
            "You let out a small gasp, your hips jerking toward him with anticipation."
            "Damien reaches one hand down to caress the outside of your panties, rubbing the fabric against your slit. You grind into his fingers, whimpering as the friction builds against your clit."
            "He lifts his head from your bra and kisses across your cleavage, dipping his tongue between the curves of your breasts."
            D "You're so beautiful, [pcname]... So beautiful..."
            "You feel his cock grow hard against your leg, grinding slightly as he continues to lick over your breasts and rub your panties."
            scene bg DAHS16 with dissolve
            "He slips his fingers underneath the fabric and pushes two in at once."
            "You gasp, grabbing for his shoulders hard. Damien stops at once and starts to pull his fingers away, surprised."
            D "Sorry! Was that too much at once? Did I-?"
            if club == "track":
                pcname "Don't stop!"
            elif club == "cheer":
                "You moan, jerking your hips up to dig his fingers in further."
                pcname "Keep going, Damien!"
            elif club == "yearbook":
                pcname "N-No! P-Please... More..."
            show bg DAHS18 with dissolve
            "Relieved, Damien pushes his fingers deep inside of you, thrusting them in and out of your pussy."
            "You tilt your head back and moan, lifting your hips from the couch to grind into his hand."
            "His thumb presses down against your clit as he fingers you, rubbing the fabric there against the swollen nub."
            pcname "D-Damien!"
            "You gasp, feeling your climax building. It can't happen yet, not yet..."
            "Sensing your oncoming orgasm, Damien slows, smirking down at you as you whimper in displeasure."
            "You need more, more..."
            D "What do you want, [pcname]?"
            scene bg DAHS20 with dissolve
            "Damien slips his fingers from your pussy and presses them into your mouth, licking them clean. You moan around his fingers, savoring the taste."
            if club == "track":
                pcname "You! I need {i}you{/i}. Right now."
            elif club == "cheer":
                "You smirk back up at him, impressed by his willingness to keep you on the edge."
                pcname "Damien... I need your nice, thick cock inside of me? Please, baby? Please?"
                "You bat your eyelashes up at him, spreading your legs wide."
            elif club == "yearbook":
                "You feel embarrassed begging, but you were so close, and his fingers felt so good...!"
                pcname "P-Please, Damien! P-Please... I-I need..."
            "Satisfied with your answer, Damien strips out of his clothes, leaving them in a messy heap on the floor, and crawls on top of you."
            "His erection is thick and stiff, pressed hard against your inner thigh. He peels the panties from your thighs, leaning down to lick your slit once as he flings them across the room."
        if damienlingeriepurchase == True:
            scene bg DAHS23 with dissolve
        elif True:
            scene bg DAHS24 with dissolve
        "He fumbles a little with the insertion, his cheeks tinging pink with embarrassment as he struggles to slide inside of you."
        "You're about to offer him some help when he finally gets it, slipping into you with one hard thrust."
        pcname "{i}AH!{/i}"
        "You let out a small shriek, your nails digging into his shoulders. A surge of pain runs through your lower abdomen as Damien forces you to accept his girth."
        "Damien pauses."
        D "Are you okay?!"
        pcname "Y-Yes... Just go a little slower next time..."
        D "Ah, sorry..."
        pcname "It's fine. Just keep going- Ohh..."
        "You moan as Damien thrusts in you slower, rocking his hips against yours as he grinds you into the couch."
        "He slowly picks up a steady rhythm, his hands fondling your breasts as he fills you up from inside."
        "You move your body to match his rhythm, whimpering as he picks up speed. You can feel your juices leaking out of your cunt and across his dick, allowing him to move in and out of you with ease."
        D "[pcname]... [pcname]... A-Ah, fuck...!"
        "Damien's breath becomes more ragged as he pounds you into the cushions, his thrusting more frantic."
        "You feel your own orgasm build up with each hard thrust of his cock inside of you."
        "One hard push after another, his cock somehow reaching deeper and deeper inside until you can't take it anymore."
        "The couch squeaks underneath you and Damien cries out with his orgasm, his cock spasming inside of your body."
        "You grind against him a little longer, waiting until you've reached your own climax before you allow this moment to end."
    elif True:

        if damienlingeriepurchase == True:

            scene bg DAHS2 with dissolve
            "Damien's face is as bright red, his eyes practically bulging from his face. He looks you over, at every exposed curve and detail through your mesh lingerie, and slowly nods."
            D "S-Sure... Y-Yes... Please..."
            "Gripping his hair, you lean down and kiss him hard, shoving your tongue deeply into his mouth."
            "Damien whimpers underneath you, his hands hovering aimlessly. Not backing away from the kiss, you pull his hands around your waist, guiding them down to your ass."
            "You can feel his cock growing stiff through his sweatpants as you grind on his lap."
            "The mesh of your panties hide nothing either; with every movement on his dick, your own juices flow through and dampen his sweatpants, making your desire known."
            "You pull Damien's shirt off and toss it to the side, rubbing the mesh of your bra and breasts against him. Damien moans, cupping your ass hard."
            if club == "track":
                "Tired of waiting, you grab one of his hands and press it hard between your thigh, your tone commanding."
                pcname "Touch me."
            elif club == "track":
                "You grow tired of waiting for Damien to make the first move and, instead, rub your breasts and ass against him, arching your back enough to his hand falls to your pussy."
                pcname "I shouldn't be the only one touching you, should I?"
            elif club == "yearbook":
                "Knowing he won't make the first move, you carefully place one of Damien's hands between your thighs and rub against it."
                pcname "P-please touch me, Damien..."
            scene bg DAHS4 with dissolve
            "He lets out a staggered breath and complies, rubbing his fingers against your wet panties. Cautiously, he raises another hand to your breast, fondling it."
            pcname "That's it... Mmph... Keep going...!"
            scene bg DAHS6 with dissolve
            "Encouraged, Damien continues to squeeze and rub against you. You reach down and slip his sweatpants and underwear down, exposing his erection."
            D "A-Ah, [pcname]...!"
            "His hands stop, eyes squeezing shut as you grind against his sensitive skin."
            pcname "Did I tell you to stop?"
            "Damien bites his lip and shakes his head, quickly lowering his head to take your breast in his mouth through the fabric."
            "The mesh doesn't seem to bother him as he toys and bites at your nipple, each movement sending a thrill of pleasure through your body."
            scene bg DAHS8 with dissolve
            "You reach down and slide your panties out of the way, the head of his cock pressing against your open slit."
            pcname "Ah, not yet..."
            "Damien moans eagerly, ready to thrust inside of you, but you grab his hand inside and shove two of his fingers inside of you."
            pcname "I want you to lick them when you're done."
            scene bg DAHS10 with dissolve
            "He nods, switching his mouth to trap your other breast inside. You grip his hair hard, yanking him down against your breasts."
            "His fingers pump in and out of you in eager thrusts, curling against your insides. You moan and rock your hips against him, grinding down into his hand."
            "Damien lets go of your other breast with a gasp, his gaze pleading."
            D "Please, [pcname]... Please... Please let me in you- Ohhh!"
            "His voice cuts off as you grab his cock in your hand, pressing the very tip against your wetness."
            "He whimpers, his hips involuntarily thrusting toward you."
            D "Please, please, please... Oh, fuck... Ohh..."
            "Satisfied with his begging, you slowly lower yourself onto his head, the folds of your vagina slowly taking him in."
            "Damien tilts his head back and inhales sharply, his hands finding their way to your ass for support."
            "He tries to push you down further, but you stop him."
            pcname "Not yet~! Be patient, Damien."
            D "[pcname]..."
            "Carefully, you lift yourself back up, almost pulling out. He opens his mouth to object, but you slam back down on him, shoving his cock as deeply inside of you as it can go."
            scene bg DAHS12 with dissolve
            "Damien gasps harshly, his body shuddering in response."
            D "[pcname]! Ohh, fuck!"
            "Unable to resist any longer, Damien grabs your ass hard and helps lift you up and down over his cock, moaning with each deep thrust inside of your cunt."
            "You moan against him, using his shoulders to help ride on top of him, matching his frantic rhythm."
            "It's like he can't get enough of you!"
            "You feel your climax build as you bounce on Damien's cock, each slight movement sending another shudder through him."
            "If you keep going like this, you'll... you'll...!"
            "Damien reaches his orgasm before you, gasping hard as his body spasms and his cock shoots hot cum into your waiting cunt."
            "You moan, rubbing against him for only a moment longer to reach your own climax, your body shuddering hard against his."
            "With a steadying breath, you unclasp your bra and remove your cum-stained panties, tossing them to the floor. They were definitely worth the price."
        elif True:

            scene bg DAHS1 with dissolve
            "Damien's face is as bright red, his eyes practically bulging from his face. He looks you over, at every exposed curve and detail through your mesh lingerie, and slowly nods."
            D "S-Sure... Y-Yes... Please..."
            "Gripping his hair, you lean down and kiss him hard, shoving your tongue deeply into his mouth."
            "Damien whimpers underneath you, his hands hovering aimlessly. Not backing away from the kiss, you pull his hands around your waist, guiding them down to your ass."
            "You can feel his cock growing stiff through his sweatpants as you grind on his lap."
            "Your panties hide nothing either; with every movement on his dick, your own juices flow through and dampen his sweatpants, making your desire known."
            scene bg DAHS3 with dissolve
            "You pull Damien's shirt off and toss it to the side, rubbing your pink bra and breasts against him. Damien moans, cupping your ass hard."
            if club == "track":
                "Tired of waiting, you grab one of his hands and press it hard between your thigh, your tone commanding."
                pcname "Touch me."
            elif club == "track":
                "You grow tired of waiting for Damien to make the first move and, instead, rub your breasts and ass against him, arching your back enough to his hand falls to your pussy."
                pcname "I shouldn't be the only one touching you, should I?"
            elif club == "yearbook":
                "Knowing he won't make the first move, you carefully place one of Damien's hands between your thighs and rub against it."
                pcname "P-please touch me, Damien..."
            "He lets out a staggered breath and complies, rubbing his fingers against your wet panties. Cautiously, he raises another hand to your breast, fondling it."
            pcname "That's it... Mmph... Keep going...!"
            "Encouraged, Damien continues to squeeze and rub against you. You reach down and slip his sweatpants and underwear down, exposing his erection."
            D "A-Ah, [pcname]...!"
            "His hands stop, eyes squeezing shut as you grind against his sensitive skin."
            pcname "Did I tell you to stop?"
            scene bg DAHS5 with dissolve
            "Damien bites his lip and shakes his head, quickly lowering his head to take your breast in his mouth through the fabric."
            "The mesh doesn't seem to bother him as he toys and bites at your nipple, each movement sending a thrill of pleasure through your body."
            scene bg DAHS7 with dissolve
            "You reach down and slide your panties out of the way, the head of his cock pressing against your open slit."
            pcname "Ah, not yet..."
            "Damien moans eagerly, ready to thrust inside of you, but you grab his hand inside and shove two of his fingers inside of you."
            pcname "I want you to lick them when you're done."
            scene bg DAHS9 with dissolve
            "He nods, switching his mouth to trap your other breast inside. You grip his hair hard, yanking him down against your breasts."
            "His fingers pump in and out of you in eager thrusts, curling against your insides. You moan and rock your hips against him, grinding down into his hand."
            "Damien lets go of your other breast with a gasp, his gaze pleading."
            D "Please, [pcname]... Please... Please let me in you- Ohhh!"
            "His voice cuts off as you grab his cock in your hand, pressing the very tip against your wetness."
            "He whimpers, his hips involuntarily thrusting toward you."
            D "Please, please, please... Oh, fuck... Ohh..."
            "Satisfied with his begging, you slowly lower yourself onto his head, the folds of your vagina slowly taking him in."
            "Damien tilts his head back and inhales sharply, his hands finding their way to your ass for support."
            "He tries to push you down further, but you stop him."
            pcname "Not yet! Be patient, Damien."
            D "[pcname]..."
            scene bg DAHS11 with dissolve
            "Carefully, you lift yourself back up, almost pulling out. He opens his mouth to object, but you slam back down on him, shoving his cock as deeply inside of you as it can go."
            "Damien gasps harshly, his body shuddering in response."
            D "[pcname]! Ohh, fuck!"
            "Unable to resist any longer, Damien grabs your ass hard and helps lift you up and down over his cock, moaning with each deep thrust inside of your cunt."
            "You moan against him, using his shoulders to help ride on top of him, matching his frantic rhythm."
            "It's like he can't get enough of you!"
            "You feel your climax build as you bounce on Damien's cock, each slight movement sending another shudder through him."
            "If you keep going like this, you'll... you'll...!"
            "Damien reaches his orgasm before you, gasping hard as his body spasms and his cock shoots hot cum into your waiting cunt."
            "You moan, rubbing against him for only a moment longer to reach your own climax, your body shuddering hard against his."
            "With a steadying breath, you unclasp your bra and remove your cum-stained panties, tossing them to the floor. At least these worked just as well."
    scene bg HomeN with fade
    "You and Damien fall back against the couch, breathless. He holds you against him, cradling you into the nook of his shoulder."
    $ clothes = "naked"
    if damienNTR:
        $ corruption += 1
        show chelsea embarrassed with dissolve
        "You feel his cum dripping out of your pussy and can't help but think of the last time you fucked someone on this couch."
        "Matt's voice echoes in your head..."
        show chelsea sad
        m "And I {i}know{/i} he could never satisfy a slut like you."
        show chelsea blank
        "You shake your head, trying to ignore it."
    elif True:
        show chelsea embarrassed with dissolve
        "You feel his cum drip out of your pussy, falling back against your ass and onto the couch, but you can't bring yourself to care right now."
    show Damien Neutral at center, moveSprite(0.7, 0.7, 0.0) with dissolve
    D "...I don't know if I ever said this before, but I was a virgin before now."
    menu damien_virginity:
        "I know." if True:
            show chelsea laugh
            show Damien Worry
            "Damien laughs weakly."
            show Damien Laugh
            show chelsea embarrassed
            D "I guess it was obvious..."
        "Looks like neither of us are virgins now." if True:
            show chelsea embarrassed
            show Damien Happy
            "Damien smiles, snuggling closer to you."
            show Damien Laugh
            D "That was amazing, [pcname]... Thank you."
    scene bg HomeN with dissolve
    "You lay there for a few moments together, calming down from the excitement of the night."
    show chelsea with dissolve
    "Now that your mind is cleared of thoughts of sex, you prop yourself up on your elbow and look at Damien."
    pcname "Alex mentioned something tonight, and I wanted to ask you about it."
    show Damien Blank at center, moveSprite(0.7, 0.7, 0.0) with dissolve
    "Damien looks down at you warily but nods."
    show Damien Neutral
    D "What's up?"
    show chelsea confused
    show Damien Blank
    pcname "He said something about an incident. What was that about?"
    show Damien Neutral
    show chelsea blank
    pause 1.0
    show Damien Glare
    "Damien opens his mouth as though to speak, but lets out a long, deep breath instead. He sighs, laying back against the couch and holding you closer."
    show Damien Worry
    D "That's kind of part of my history with him."
    D "I had a crush on a girl in middle school that Alex also liked. I tried to ask her out and, well, Alex found out."
    show Damien Neutral
    D "Before our first date happened, he got mad and spread a bunch of nasty rumors about me."
    D "She was so freaked out that she cancelled our date, and Alex has never really let me live it down. She still probably believes all that stuff he told her..."
    show Damien Sad
    show chelsea confused
    pcname "What did he tell her?"
    show chelsea blank
    "Damien shakes his head."
    show Damien Worry
    D "I really don't want to talk about it."
    show Damien Neutral
    D "Just know that Alex has had fun ruining my life since then. I wouldn't be surprised if he lied to you about everything later."
    D "You should be careful around him."
    show Damien Blank
    "Damien quiets down, and you feel that this is all you're going to hear about it tonight."
    show chelsea embarrassed
    show Damien Shocked
    "Reaching up, you place a soft kiss against his cheek."
    show Damien Blank
    pcname "Thanks for everything tonight, Damien."
    scene black with fade
    "He smiles, drawing a blanket over the back of the couch to wrap over you both."
    D "You too, [pcname]."
    $ acts-=3
    jump events_end_period
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
