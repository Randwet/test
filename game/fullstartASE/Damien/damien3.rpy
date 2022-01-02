label damien_mallinvite:
    $ clothes, hair = casualwear
    "You're in the midst of a deep slumber when a persistent buzzing wakes you up."
    "Groggy, you slide your hand out from your covers and fumble around for your phone on the nightstand."
    "Sunlight blares in from your curtains, effectively blinding you as you crawl out from the comfort of your blankets."
    pcname "Crap... I think I slept through my alarm... What time is it...?"
    "Unlocking your phone, a text from Damien lights up the screen."

    call screen TextingScene("Damien",
    [
        TextMessage("Good morning! You busy today, [pcname]?"),
        TextMessage("Not really. I just have club this morning.", sender = False),
        TextMessage("Great!"),
        TextMessage("I was wondering if you want to go out with me today. When your club is over and everything."),
        TextMessage("What did you have in mind?", sender = False),
        TextMessage("How does the mall sound?")
    ])

    menu damienPhoneChoice1:
        "What will you say?"
        "That sounds great." if True:

            jump cunt
        "I'm not really in the mood to run around today." if True:
            jump notinthemood

label notinthemood:
    call screen TextingScene("Damien",
    [
        TextMessage("I'm not really in the mood to run around today.", sender = False),
        TextMessage("Oh. Okay, no problem. Do you want to do something else instead?"),
        TextMessage("Not really.", sender = False),
        TextMessage("Oh... Okay. Maybe some other time then."),
    ])

    $ clothes = "naked"
    show chelsea at right with moveinright

    "You sigh, reluctantly climbing out of bed. You feel a little bad for rejecting him, but just because you're his girlfriend now doesn't mean you want to spend every waking moment together."
    "Besides, you have club to go to."
    "Speaking of..."
    "You flip your phone back open and take a look at the time."
    show chelsea shocked
    pcname "Crap! I'm going to be late!"
    "You toss your blankets to the side and rush to your closet to get ready."
    "At least Damien's text was good for one thing; you would've completely slept through otherwise!"
    hide chelsea with dissolve

    jump events_end_period

label cunt:
    call screen TextingScene("Damien",
    [
        TextMessage("That sounds great.", sender = False),
        TextMessage("Awesome!! Do you want me to pick you up or should we meet there?"),
        TextMessage("I'm not sure when I'll get out of club yet, so let's meet there to be safe.", sender = False),
        TextMessage("Cool! Sounds good to me. Just text me when you're done and I'll see you there!"),
        TextMessage("Okay!", sender = False)
    ])

    show chelsea happy at right with moveinright
    "You set down your phone with a grin. This was a pleasant surprise to wake up to, even if his text {i}did{/i}, in fact, wake you up..."
    pcname "I wonder how late I slept in..."
    "Rubbing the sleep from your eyes, you pick up your phone and peer down at the time."
    show chelsea shocked
    pcname "Crap! I'm going to be late!"
    "You toss your blankets to the side in a panic and rush to your closet to get ready."
    "It's a good thing Damien texted you awake!"
    hide chelsea with dissolve
    $ damienmall = True

    jump events_end_period

label damien_mall:
    $ DamienAngry = "Characters/Damien/Casual/Angry.png"
    $ DamienBlank = "Characters/Damien/Casual/Blank.png"
    $ DamienGlare = "Characters/Damien/Casual/Glaring.png"
    $ DamienLaugh = "Characters/Damien/Casual/Laughing.png"
    $ DamienNeutral = "Characters/Damien/Casual/Neutral.png"
    $ DamienSad = "Characters/Damien/Casual/Sad.png"
    $ DamienShocked = "Characters/Damien/Casual/Shocked.png"
    $ DamienSmiling = "Characters/Damien/Casual/Smiling.png"
    $ DamienWorrying = "Characters/Damien/Casual/Worrying.png"
    $ clothes, hair = casualwear
    show chelsea at right with moveinright
    show bg Shop with dissolve
    "By the time you arrive, the mall is already bustling with shopping-hungry teens, exhausted parents, and squealing children. Although you're used to the mall always having some sort of crowd, today it seems excessively packed."
    pcname "I guess it makes sense for it to be busy. It {i}is{/i} a Saturday. But still..."
    "As you look around, you can't help but notice an abundance of young adults wearing what appear to be sci-fi t-shirts and other merchandise."
    "The symbol looks sort of like a tree inside of a dome, but the leaves are sharp magenta triangles, and what look like glowing golden orbs fall to the bottom of the dome."
    "You don't recognize the symbol in the slightest, but everywhere you look you find more and more of it printed onto clothes and stitched onto backpacks."
    show chelsea confused
    pcname "What's going on...?"
    show Damien Happy at left with moveinleft
    "Before you can bring up your curiosity to a nearby group in identical shirts, you spot Damien at an empty table in the food court. He gives you a smile and a wave as you make eye contact."
    show chelsea blank
    "As you approach him, you notice the tree-like patch stitched onto his backpack. And... {i}Ugh.{/i} Does he only own cargo shorts?"
    D "Hey, [pcname]. Glad you could make it."
    show chelsea confused
    pcname "Yeah, me too... Hey, Damien, what {i}is{/i} that?"
    show Damien Worry at left
    "You point toward the patch on his backpack. His cheeks tint pink with embarrassment."
    show chelsea blank
    pcname "I've been seeing that symbol everywhere."
    show Damien Neutral at left
    D "Oh. Ha. Um, have you heard of {i}Liberation of Andromeda{/i}?"
    show Damien Worry at left
    "You shake your head. He nods, accepting, although the heat spreads further up his face."
    show Damien Neutral at left
    D "It's a comic book from the eighties. It got a resurgence in popularity a couple of years ago and now they're making a TV show out of it."
    D "I've been a huge fan for a long time... My dad got me into the comics when I was a kid."
    show Damien Blank at left
    "Damien shifts awkwardly in place, embarrassment creeping through as he struggles to meet your gaze. He looks like he wants to say something, but changes his mind."
    show Damien Happy at left
    D "So, wanna check out the mall?"
    show chelsea happy
    pcname "Sure."
    hide Damien Happy with dissolve
    hide chelsea with dissolve
    "It's a struggle to push past the large crowds of sci-fi fans as you walk alongside Damien through the mall. There's more than one occasion you think you might've lost Damien in the crowd entirely."
    "This is one of those times."
    show chelsea shocked at right with moveinright
    "You stand on your tiptoes near a soft pretzel stand and try to peer over the mass of people."
    pcname "Damien?"
    D "Here!"
    show Damien Shocked at left with moveinleft
    "Damien thrusts his hand in the air to your left, caught between two families as they commit to an awkward dance around each other. Damien ducks between them and hurries to your side."
    show Damien Worry at left
    D "Sorry."
    show chelsea happy
    pcname "It's okay."
    show Damien Happy at left
    "You take his hand in yours, entwining your fingers together. He glances at your held hands with a smile."
    pcname "Let's try to stick together."
    D "Yeah."
    "It's harder to lose him in the crowds with your hands joined, but that doesn't stop others from trying to push between you on their way to the next store. You hold onto Damien's hand tightly and keep him close."
    pcname "So where did you want to go first?"
    show Damien Neutral at left
    D "Oh. Um, well, you know..."
    "He hesitates, considering."
    show Damien Happy at left
    D "I'm up for whatever."
    "Even as he speaks, you catch his gaze straying to a nearby store. It's obvious he has something in mind, but why won't he tell you about it?"
    show chelsea confused
    pcname "It looks like you know what you want to do."
    show Damien Worry at left
    D "O-Oh. Well, now that you mention it, there's... sort of..."
    show chelsea blank
    "He trails off, looking back to the store. You gaze follows. It's a typical geek store; comic books, board games, figurines, and other merchandise of foreign series clutter the walls and shop windows. You recognize a few of the popular characters on display, but most of them are lost to you."
    "A huge line snakes out of the door. You notice a large sign displayed outside: {i}'MEET GILBERT HAVEED, AUTHOR OF{/i} LIBERATION OF ANDROMEDA{i}! SIGNINGS TODAY 12:00-6:00PM!'{/i}"
    D "He just started his tour a few weeks ago. He hardly ever does signings, but I... I don't know. It would be kind of cool to meet him, I guess. And I... I happen to have a copy of his comic with me..."
    show Damien Neutral at left
    "Damien looks at you with a mixture of hope and fear in his eyes. He shifts nervously, anticipating your response."
    menu damien_meetngreet:
        "Isn't that whole thing kind of weird?" if True:
            $ corruption += 1

            $ damienconfidence -=1
            if club == "track":
                show chelsea confused
                "You can't help but feel put off by the whole thing. Why would he invite you out if he was just going to fuck off and wait in line for some stranger?"
                pcname "You want me to stand in line for an hour to meet some middle-aged guy from a series I don't even know? What happened to our date?"
                show Damien Shocked at left
                D "Ah, s-sorry! That's not what I meant at all..."
            elif club == "cheer":
                show chelsea confused
                "As much as you can get behind wanting to meet your idol, why would he drag you along to it? It's not like you even know the series. What are you supposed to do? Stand there and look pretty?"
                pcname "I thought this was a date. Did you just bring me out here to wait around while you meet this guy?"
                show Damien Shocked at left
                D "No, no! Of course not! I promise!"
            elif club == "yearbook":
                show chelsea sad
                "The idea of waiting in line for over an hour to meet a random stranger fills your chest with anxiety. Surrounded by all those people, all talking about a series you have no knowledge about... You would be completely isolated."
                pcname "I-I thought we were on a date... Are you trying to ditch me...?"
                show Damien Shocked at left
                D "N-No! No! I would never!"
            show Damien Worry at left
            D "I just... I thought it might be nice to do... We don't have to, of course..."
            if club == "track":
                pcname "Good. No offence, but that kind of stuff weirds me out. I want to do something {i}fun.{/i}"
            elif club == "cheer":
                pcname "Cool. I was worried you were going to be lame and try to drag me around those weird nerd stores all day."
                pcname "I came to the mall to have {i}fun{/i}."
            elif club == "yearbook":
                pcname "O-Okay... Um, I'm sorry. The thought of going in there stresses me out... I-I'm just not really interested in going..."
                pcname "I think we could have fun doing something else if, um, you're alright with that."
            show Damien Sad at left
            D "Right. Right. Of course. Um, what would you like to do, [pcname]?"
            show chelsea blank
            "You tap your chin, considering the different options in the mall. There isn't much to do besides eating and shopping, but..."
            "Looking at Damien's cargo shorts, you come to an easy solution."
            show chelsea happy
            pcname "Let's go to '{i}Maytext{/i}. They released a new collection for the season."
            show Damien Blank at left
            D "Oh. Okay. Yeah, let's go there."
            "No matter how he tries to hide it, Damien's disappointment is evident as he follows you to a popular clothing store at the end of the mall. You catch him sparing a few longing glances toward other visitors you pass by in sci-fi shirts."
            "Fun pop music greets you as you enter the store. It's divided in half by male and female clothing, bright red signs indicating the sales in the back while everything new is displayed on fashionable mannequins at the front."
            "The new fall line of clothing shows off an array of darker colors, from dark wash jeans to maroon sweaters and mustard yellow jackets."
            "Starting off casual, you browse through a few racks of clothing, pointing out cute sweater dresses and jackets that catch your eye. Damien follows behind, his expression unusually blank."
            "You point out a few more things, trying to gauge a reaction out of him, but all he gives you are little shrugs and 'I don't know's."
            "Determined to get some sort of response, you scan the store until you come across a decent outfit in the male section."
            show chelsea laugh
            pcname "Hey, Damien, check these out!"
            "Tugging on Damien's hand, you lead him toward a male mannequin showing off a pair of maroon chinos and a thick cream sweater."
            show chelsea happy
            pcname "What do you think?"
            show Damien Neutral at left
            D "Of what?"
            show Damien Blank at left
            pcname "For you, silly."
            show Damien Neutral at left
            "Damien surveys the outfit, clearly unimpressed. He gives you an apologetic smile."
            D "Ah, I don't know if that's really my style..."
            "You can't help but feel a little frustrated. Is that as much as he's going to give you?"
            show chelsea blank
            pcname "What's wrong?"
            show Damien Shocked at left
            "Damien blinks, taken aback."
            D "Nothing's wrong."
            show Damien Blank at left
            pcname "That's not true. You've barely said anything since we entered the store."
            show chelsea confused
            pcname "Did I upset you? Is this about not going to the signing?"
            show Damien Shocked at left
            "His eyes grow wide, surprised by where your mind has gone. He waves his hands in front him, rejecting the idea."
            D "No, no! Of course not!"
            show Damien Worry at left
            D "I just..."
            "He looks between the racks of clothes awkwardly, struggling to gather the right words."
            D "I'm really bad at clothes shopping. I don't really know what to look for in girl's clothes, and for me... I just prefer function over fashion."
            menu damien_clothesshopping:
                "Berate him." if True:
                    $ corruption += 1
                    $ damienconfidence -= 2
                    if club == "track":
                        pcname "No shit. Those cargo shorts have {i}never{/i} been in fashion, but I don't think you {i}own{/i} anything else."
                    elif club == "cheer":
                        pcname "Obviously, if you're still wearing {i}those.{/i}"
                        "You gesture vaguely to his cargo shorts, not bothering to hide the disgust in your wrinkled nose."
                    elif club == "yearbook":
                        pcname "I've noticed..."
                        "Unable to help yourself, you give his cargo shorts a look of distaste. They're so bulky and unflattering..."
                    show chelsea happy
                    pcname "Just let me pick out some clothes for you. I bet I can find something just as functional without the ugly shorts."
                    "Damien glances down at his cargo shorts sheepishly."
                    D "Are they really that bad...?"
                    if club == "track":
                        show chelsea blank
                        pcname "Yes. Very."
                    elif club == "cheer":
                        show chelsea confused
                        pcname "They're not {i}attractive{/i} if that's what you're going for..."
                    elif club == "yearbook":
                        show chelsea sad
                        pcname "W-Well..."
                    show Damien Sad at left
                    "He frowns down at his current attire, ego deflating."
                    D "O-Oh... Um, okay, then..."
                    D "If you really want to dress me up, I guess that's okay..."
                    "Damien glances at the mannequin uncertainly. He doesn't seem entirely comfortable with the situation, but at least he isn't telling you no."
                    show chelsea happy
                    pcname "Great. Let me take a look around the store and I'll meet you at the dressing rooms."
                    show chelsea laugh
                    pcname "Just put on whatever I give you and model it for me, okay?"
                    show Damien Worry at left
                    D "I- Sure..."
                    hide Damien Worry with moveoutleft
                    show chelsea blank
                    "He shuffles away to the dressing rooms, a defeated man. You try to ignore it and browse through the clothing racks. He has no idea what a huge favor this is, but you're sure he'll be thanking you when you're done!"
                    "The amount of clothing that attracts your eye is excessive, but you eventually narrow it down to three outfits and carry the clothes and accessories to the back."
                    "You find Damien sitting on the ground outside of the dressing room, nose-deep into a comic book. You gently nudge his leg with your shoe, garnering his attention."
                    show Damien Blank at left with moveinleft
                    show chelsea happy
                    pcname "I've got the goods."
                    show Damien Shocked at left
                    D "Oh. That was fast."
                    "It wasn't, but you guess he was hoping you wouldn't find anything at all."
                    show Damien Worry at left
                    "You shove the pile of clothing into his unsteady arms, trying not to laugh at the nervous look on his face as he eyes the lack of cargo shorts."
                    show chelsea laugh
                    pcname "Well, don't just stand there. Let me see them!"
                    "Damien bites his lip, reluctantly ducking into one of the empty dressing room stalls. You take a seat on a plush cushion outside and wait."
                    hide Damien Worry with moveoutleft
                    show chelsea happy
                    "After a few moments- and what sounds like some fumbling followed by a curse here or there- you hear Damien's embarrassed voice call out through the thin door."
                    D "[pcname], you aren't serious about this outfit, are you...?"
                    pcname "I don't know. Come out and show me what it is."
                    "You hear a little sigh before Damien hesitantly opens the door."
                    "You try to bite your lip back from laughing."
                    "Too late."
                    show DamienLow with dissolve
                    show chelsea laugh
                    "Laughter comes out in high-pitched giggles as you take in the gag outfit you supplied Damien with. You certainly hadn't expected him to actually try it on, but it's better than you could have even dreamed."
                    "Shiny white go-go boots glint under the store's lights as he stumbles out of the dressing room, his chest barely covered by a purple and pink tie-dye crop top, complete with matching booty shorts."
                    "His face is even more bright pink than his shirt. He struggles to cover himself, but there's so much exposed skin that he doesn't even know where to begin putting his arms."
                    pcname "Oh... Oh Damien, you look {i}great!{/i}"
                    D "{i}Ha-Ha.{/i} Please tell me this was a joke. There's no way I could wear this out..."
                    show chelsea happy
                    pcname "You already are. The mall isn't exactly a private place, you know."
                    "Seeming to realize this, Damien's eyes grow wide as he glances to each side, afraid someone might see."
                    D "Can I change now? Please?"
                    show chelsea laugh
                    pcname "Ye- yes!"
                    "You're barely able to answer through your choking laughter. You wave him off, but find yourself bursting into louder hysterics when he turns around and you see '{i}BOOTYLICIOUS{/i}' written in shimmering silver letters on his ass."
                    hide DamienLow with moveoutleft
                    "Damien shuts the dressing room door with a little more force than necessary as he hurries back inside."
                    show chelsea happy
                    "Your laughter dies down after a few more minutes. You wipe the tears from your eyes, careful not to smear your makeup."
                    $ DamienAngry = "Characters/Damien/Casual 2/Angry.png"
                    $ DamienBlank = "Characters/Damien/Casual 2/Blank.png"
                    $ DamienGlare = "Characters/Damien/Casual 2/Glaring.png"
                    $ DamienLaugh = "Characters/Damien/Casual 2/Laughing.png"
                    $ DamienNeutral = "Characters/Damien/Casual 2/Neutral.png"
                    $ DamienSad = "Characters/Damien/Casual 2/Sad.png"
                    $ DamienShocked = "Characters/Damien/Casual 2/Shocked.png"
                    $ DamienSmiling = "Characters/Damien/Casual 2/Smiling.png"
                    $ DamienWorrying = "Characters/Damien/Casual 2/Worrying.png"
                    show Damien Neutral at left with moveinleft
                    "It's another ten minutes before Damien reappears, but when he does, the outfit isn't nearly as ridiculous. He wears a pair of white sneakers and a navy blazer and he looks utterly, dreadfully uncomfortable."
                    "He doesn't say anything at first, simply clasping his hands quietly in front of his stomach."
                    show chelsea confused
                    pcname "...Well?"
                    "He hesitates, afraid to say his answer. After a moment--"
                    D "I feel like my name is Chad, I go to private school, and I own a yacht in the south pacific."
                    "Specific. You can see it perfectly in your mind, Damien swimming in a pool of money on a private yacht in these clothes."
                    show chelsea blank
                    pcname "That doesn't sound {i}bad.{/i}"
                    D "No, it doesn't. But I'm way too poor for a yacht."
                    show chelsea happy
                    "You chuckle."
                    pcname "Same."
                    pcname "Okay, try the last one."
                    hide Damien Neutral with moveoutleft
                    "Damien nods eagerly, grateful to be getting out of the stiff clothes. He hurries back into the dressing room."
                    show Damien Happy at left with moveinleft
                    "This time when he emerges, he has a smile on his face. He hesitantly steps out in a pair of cuffed jeans and a matching denim jacket with a Sherpa collar."
                    D "I... I like this, actually."
                    "You feel a sense of pride at his words."
                    pcname "I knew you would. Just one thing..."
                    "You rise from your seat and take the front of his white t-shirt. Rolling the front up, you give him a French tuck."
                    show chelsea laugh
                    pcname "{i}Now{/i} it's perfect."
                    show Damien Blank at left
                    "Damien gives the tuck a confused look but doesn't argue. He walks toward a set of mirrors in a half-circle and checks himself out."
                    show chelsea happy
                    pcname "What do you think of the sneakers?"
                    show Damien Happy at left
                    D "I like them. I don't usually like bulky stuff like this, but these feel really nice..."
                    if club == "track":
                        show chelsea laugh
                        pcname "See? I'm a genius."
                    elif club == "cheer":
                        show chelsea laugh
                        pcname "You look really cute like that. I told you I could handle it."
                    elif club == "yearbook":
                        show chelsea embarrassed
                        pcname "I'm so glad you like it..."
                    "Damien gives a few more turns into the mirror, pleased with his outfit."
                "Offer to help him find something he likes." if True:
                    $ damienconfidence +=2
                    if club == "track":
                        show chelsea happy
                        pcname "You don't have to give up one for the other, Damien. Let me help find something for you to wear. I'm sure between the two of us we can find an outfit you'll really like."
                    elif club == "cheer":
                        show chelsea happy
                        pcname "I see... Why don't we look for some clothes you might like together? I'm sure we could find something comfortable that {i}also{/i} looks really good around here."
                    elif club == "yearbook":
                        show chelsea embarrassed
                        pcname "Um, w-why don't we look together? If you want to, I mean. I'm not trying to impose... I just think it might be fun..."
                    show Damien Neutral at left
                    "He blinks, surprised by your offer."
                    D "Oh. Um, sure. That sounds... That sounds like it could be fun."
                    show Damien Happy at left
                    "He gives you a little smile and you know you've won him over."
                    show chelsea laugh
                    pcname "Great! Why don't you tell me what kind of things you look for in clothes? That might help me find something easier..."
                    "He looks down at his cargo shorts with a sheepish grin. You can't help but laugh."
                    show chelsea happy
                    pcname "I already know you like those. But, what do you like about them? That might help me while I'm looking."
                    D "Oh, right. Ha. Let's see..."
                    show Damien Neutral at left
                    "Damien shoves his hands in his pockets and purses his lips, considering."
                    D "I like the pockets, I think. I like being able to have plenty of space to put things. They also give me plenty of room..."
                    "He shifts a little, and you don't have to guess where they give him the most {i}comfortable{/i} room."
                    pcname "Okay. So pockets and room. Anything else?"
                    D "I guess I like t-shirts. I'm not really into anything too stifling..."
                    pcname "Got it. Okay, how about you look in the sale section and I'll look up here?"
                    show Damien Happy at left
                    D "Okay. That sounds fair."
                    pcname "Cool. I'll meet you at the dressing room when I'm done."
                    D "Alright. I'll meet you there."
                    hide Damien Happy at left with moveoutleft
                    "Damien gives you a little wave before parting for the back of the store. You scan the new fall selections and tap your chin in thought. There's a lot of variety here, but Damien's specifications will help narrow that down a little."
                    "After some searching, a mannequin adorning a denim jacket with a Sherpa collar and cuffed jeans catches your eye. The jeans are stretchy, giving plenty of room, while the jacket features pockets both inside and out."
                    show chelsea laugh
                    pcname "Damien will love this!"
                    show chelsea happy
                    pcname "Well, I hope he will, anyway..."
                    "As you're walking back to the dressing rooms, you find a couple of more ridiculous, eye-catching outfits that you can't help but toss onto the pile. Even if Damien doesn't try them on, you can get a good laugh out of imagining him in them."
                    show Damien Neutral at left with moveinleft
                    "Damien gives a raised eyebrow at the unusual clothes on the top of the pile as you approach."
                    show chelsea laugh
                    pcname "I thought you might have some fun with these."
                    show Damien Happy at left
                    show chelsea happy
                    "His lips quirk into a smile as he takes the pile of clothes, readjusting his arms to put his finds on top."
                    D "Ha. Okay."
                    "You peer at the small stack of t-shirts he gathered."
                    pcname "Any luck on your end?"
                    D "A couple, yeah. I'm- excited? Is that the right word?- to see what you found."
                    hide Damien Happy with moveoutleft
                    "He gives you a half-hearted salute before ducking into one of the empty dressing room stalls. You sit back on one of the plush cushions near a half-circle of mirrors and wait."
                    "After a few moments of fumbling, you hear a burst of laughter from inside the stall."
                    D "Do I really need to come out with this on, [pcname]?"
                    "You grin, already having an idea as to what outfit he's referring to."
                    pcname "Yes! It's all part of the shopping experience."
                    "There's a pause, and then-"
                    show DamienHigh with dissolve
                    show chelsea laugh
                    "You're unable to control the high-pitched giggle that rises in your throat as Damien steps out of the dressing room- or rather, {i}struts{/i} out."
                    "White, knee-high go-go boots shine underneath the store's lights as he walks forward, his backpack thrown over his shoulder for dramatic effect. You're not sure where he got them, but Damien grins at you from behind a pair of circle sunglasses."
                    "With the addition of the purple and hot pink tie-dye crop top and booty shorts, he looks like a 1960's hot mess."
                    pcname "Oh... my... God! Haha!"
                    "You cover your mouth to try to muffle the worst of your giggling. Your ribs ache as you double over in laughter, tears brimming at your eyes as Damien makes a few rather {i}groovy{/i} poses."
                    D "Is this what you were hoping for, [pcname]?"
                    pcname "Ha! Haha! Better! It's better- haha! Better than I could've imagined!"
                    "Damien struggles to keep a straight face as he poses, prepared to double over in laughter himself."
                    D "Yeah, baby!"
                    "He speaks in a heavy British accent, reminiscent to an old 1960's parody film you vaguely remember watching."
                    "You find yourself snorting with laughter as he struts back into the dressing room stall, bright silver letters glittering '{i}BOOTYLICIOUS{/i}' on his ass. He closes the door behind him."
                    show chelsea happy
                    hide DamienHigh with dissolve
                    "It takes more than a few minutes for your laughter to die down and to wipe the tears away from your face, careful not to smear your makeup, but the image of Damien strutting around like a 1960's go-go dancer is one you'll treasure always."
                    $ DamienAngry = "Characters/Damien/Casual 2/Angry.png"
                    $ DamienBlank = "Characters/Damien/Casual 2/Blank.png"
                    $ DamienGlare = "Characters/Damien/Casual 2/Glaring.png"
                    $ DamienLaugh = "Characters/Damien/Casual 2/Laughing.png"
                    $ DamienNeutral = "Characters/Damien/Casual 2/Neutral.png"
                    $ DamienSad = "Characters/Damien/Casual 2/Sad.png"
                    $ DamienShocked = "Characters/Damien/Casual 2/Shocked.png"
                    $ DamienSmiling = "Characters/Damien/Casual 2/Smiling.png"
                    $ DamienWorrying = "Characters/Damien/Casual 2/Worrying.png"
                    show Damien Blank at left with moveinleft
                    "The door opens a little while later, followed by Damien in a pair of white sneaker and a navy blazer. He clutches his hands in front of his chest."
                    D "You know I had to do it to 'em."
                    show chelsea confused
                    "You blink, confused."
                    pcname "Do what?"
                    D "Wait, you've never-? I- Okay. I'm catching you up on your memes later."
                    show Damien Happy at left
                    show chelsea happy
                    "Damien relaxes and checks himself out in the mirror."
                    D "I feel like a guy named Chad that goes to private school and has a yacht in the south pacific. A big yacht, but not like, Jeff Bezo's yacht."
                    pcname "You know... I can actually see that."
                    D "Excuse me while I go bathe in my tub of gold and donate Gucci to the peasants. O-ho-ho-ho."
                    show chelsea laugh
                    hide Damien Happy with moveoutleft
                    "Damien flicks his hand, his voice nasally as he steps back into the dressing room. You grin, watching him go."
                    "You hadn't expected Damien to be this much fun to shop with, but now that you've seen how he acts in different outfits, you find yourself even more endeared by him."
                    show chelsea blank
                    "As you flip through your phone and glance around the otherwise empty dressing room, it takes Damien longer than usual to get changed. After ten minutes, he's still not out of the stall."
                    pcname "Damien? Did you get lost in there?"
                    D "Huh? Oh. Right."
                    show Damien Happy at left with moveinleft
                    "The door falls open and Damien steps out, catching glances of himself in the mirror inside of his stall."
                    "This was the outfit you collaborated on, the cuffed jeans and denim jacket, but it looks even better with the white t-shirt and bulky white sneakers Damien picked out from the sale selection."
                    show chelsea happy
                    pcname "I... Wow."
                    "Damien beams, a genuinely confident smile if you've ever seen one. You're not used to seeing them on him, but somehow that's all you've been blessed with on this shopping trip so far."
                    D "Right? I feel great. These pants are {i}awesome-{/i}"
                    "He shoves his hands deep into the jeans for effect."
                    D "And I love this jacket. I didn't realize denim jackets could be comfortable, you know?"
                    pcname "Yeah. You... Hold on."
                    "You rise from your seat and take the edge of Damien's white t-shirt. He gives you a curious look as you roll the bottom and give him a French tuck into his jeans."
                    pcname "There. Now you look {i}perfect.{/i}"
                    D "Yeah?"
                    "Damien walks toward the half-circle of mirrors and checks himself out."
                    D "I love these sneakers. I don't normally like stuff this bulky, but they're so comfortable..."
                    "You both spend a few minutes admiring his new attire, pleased with the end result. {i}Anything{/i} would've been better than the cargo shorts, but somehow this feels even more special."
            D "I'm going to get changed and check out."
            D "Then, do you want to wander around the mall some more?"
            show chelsea laugh
            pcname "That sounds great!"
            D "Awesome. I'll be right back."
            hide Damien Happy with moveoutleft
            show chelsea happy
            "Damien gives you a smile before ducking back into the dressing room. You can't help but find his smile even more charming in his new outfit."
            show Damien Happy at left with moveinleft
            "Once he's changed back into those dreadful cargo shorts- you'll be happy to see them gone in the future- you follow him up to the register to check out."
            "After a few minutes, all the clothes are bagged and paid for, and you find yourselves back at the entrance of the store."
            $ damienoutfitchange = True
        "Let's go meet him!" if True:
            $ corruption -= 2

            $ damienconfidence +=1
            if club == "track":
                show chelsea blank
                "You look back at the eager line of people. Damien glances their way, the longing clear on his face."
                pcname "Well if you really want to meet him, let's go."
            elif club == "cheer":
                show chelsea happy
                "You eye up the line of comic fanatics and their merchandise waiting to be signed. It's not really your thing, but you can see how badly Damien wants to join them."
                pcname "It sounds like you don't know when he'll be back. Why don't we get your comic signed?"
            elif club == "yearbook":
                show chelsea embarrassed
                "The idea of waiting in line to meet a complete stranger fills your chest with anxiety, but if that's something Damien is interested in doing, who are you to stop him?"
                pcname "L-Let's go meet him! You don't know when he'll be back, anyway..."
            show Damien Shocked at left
            "Damien blinks, surprised by your response. He seems utterly taken aback, gaping at you in silence for a moment before he finds his voice."
            D "Ah, really? You'd be okay with that?"
            show Damien Worry at left
            D "I mean, I don't want to make you wait in a long line just for me..."
            show chelsea happy
            pcname "Of course I'm sure. This is really important to you, isn't it? And you're my boyfriend, so..."
            show Damien Happy at left
            "His lips quirk into a shy smile. He takes your hand and gives it a squeeze."
            D "Yeah. Thanks, [pcname]. I've really been looking forward to this. I just felt so bad asking..."
            D "Thank you for doing this for me. Let's get in line now so we make sure to see him before they stop taking people."
            pcname "Okay."
            "Without letting go of your hand, Damien leads you toward the store. His excitement is nearly buzzing as you both take your place in line."
            D "So, uh, sorry, but do you mind if I geek out for a bit? I've been looking forward to meeting this guy for so long..."
            show chelsea laugh
            pcname "I don't mind. Go ahead."
            show Damien Laugh at left
            show chelsea happy
            D "Really? [pcname], you're so awesome! Okay, so..."
            "Damien trails off into the lore of the comic, delving into a lot of information you struggle to grasp but smile and nod at anyway."
            "You spend most of your time in line listening to Damien's long-winded explanations about the plot, characters, and mechanics of {i}Liberation of Andromeda{/i}. By the time you're both in the store, you should be an expert on the series... if you could keep up with him."
            "You find yourself doing a lot of nodding as he talks at you, breaking off from one thought to the next. You lost him in the conversation thirty minutes ago, but you're afraid to point it out lest he start all over."
            "As you reach the front of the line, Damien is nearly bouncing in his spot. He clutches what looks like a copy of his father's comic book in his hands and continues to babble on."
            "It's been over an hour now and you're sure he's repeated at least half of this conversation to you."
            show Damien Happy at left
            D "Then the Globstars-"
            show chelsea confused
            pcname "Globstars?"
            D "The Global Starlight Communicators, remember? The Globstars contact Irving-"
            "A small couple of fans wave goodbye in front of you, stepping away from a makeshift booth in the store."
            "Gilbert Haveed is an older man in his sixties with more white hair on his chin than his head. He's dressed casually, more so than you thought a professional would be. He vaguely reminds you of those ornaments of Santa Clause in sunglasses and a beach chair."
            "Two big posters sit on either side of him: one of the comic and another of the TV show. Damien's face lights up as he realizes it's your turn in line."
            "Gilbert" "Hey there."
            show Damien Shocked at left
            D "Hey! Ah, Mr. Haveed... It's an honor to meet you."
            "Damien gives the man a nervous smile, nearly twisting the comic in his hands. He seems to realize what he's doing because he abruptly stops, his face turning a deep shade of pink."
            "Gilbert" "And it's wonderful to meet you, Mr...?"
            show Damien Happy at left
            D "Damien, sir."
            "Gilbert" "Damien! A great name. And who is this you brought with you?"
            show Damien Shocked at left
            "Damien blinks, confused, then glances in your direction. It's as if he's forgotten you entirely. He smiles apologetically and waves toward you."
            show Damien Happy at left
            D "This is my girlfriend, [pcname]."
            show chelsea happy
            "You wave awkwardly, not sure how to respond."
            pcname "Hi."
            "Gilbert" "What a pretty name. A pleasure to meet the both of you."
            "Gilbert" "Now, it seems you have something for me to...?"
            "He reaches out for the comic book in Damien's hands expectantly."
            show Damien Shocked at left
            D "Yeah! Of course! I mean, if that's okay with {i}you{/i}, Mr. Haveed."
            "Gilbert" "That's what I'm here for, isn't it? And please call me Gilbert."
            show Damien Happy at left
            D "Gilbert... Yeah. Got it. Sorry."
            "Gilbert sets down the comic, then does a double take. His pen hesitates above the front cover."
            "Gilbert" "Oh boy. This is an {i}original.{/i} I haven't seen one of these copies in a {i}long{/i} time."
            D "It's my dad's."
            "Gilbert" "Ah, that makes sense. You getting it signed for him?"
            show Damien Laugh at left
            D "Oh, no, it's all mine now, sir. Mr. Ha- Gilbert. Sir. Um, it's my copy now. I've been reading it since I was a kid."
            show chelsea confused
            "As Damien and Gilbert trail off into their own conversation, you can't help but feel a little left out."
            "They branch off into some of Damien's theories that he spouted at you earlier. There's no point in trying to listen to the conversation; you can't make sense of it in the slightest."
            "Between the two of them geeking out over some old comic, you feel invisible."
            "When Gilbert addresses you, you're taken entirely by surprise."
            show Damien Happy at left
            "Gilbert" "And what about you, [pcname]? I always love hearing from a fan. What are your thoughts?"
            menu damien_meetngreet_response:
                "This stuff is lame." if True:
                    $ corruption += 1
                    "You'd hoped to take a backseat to this encounter, but since he's asking your opinion, you'd feel wrong lying to him."
                    "Not to mention it might be fun teasing Damien about it, just a little."
                    $ damienconfidence -= 2
                    if club == "track":
                        show chelsea laugh
                        pcname "Oh. I don't care about it. I'm not into this kind of stuff. It's pretty lame, actually."
                        "You poke Damien's flushed cheek."
                        show chelsea happy
                        pcname "But my boyfriend likes it, and he's so cute when he's excited."
                    elif club == "cheer":
                        pcname "I don't have any. This really isn't my thing. I find it kind of boring, actually, but Damien likes it for {i}some{/i} reason, so..."
                    elif club == "yearbook":
                        pcname "I... I-It's not really for me..."
                        pcname "But Damien likes it, so..."
                    show Damien Shocked at left
                    "Damien's face flushes a deep pink, mortified by your response. He glances between you and Gilbert nervously, jaw dropped."
                    D "I- I- Um- I'm so sorry, Gilbert, I-"
                    "Gilbert gives you a tight but polite smile; clearly he's heard your response before."
                    "Gilbert" "It's quite fine. I'm sorry to hear you feel that way, [pcname]. We all have different tastes, I suppose. It's what makes us human."
                    "Gilbert" "Of course, the bias in me hopes you'll give it a try some day."
                    show chelsea blank
                    pcname "I doubt it..."
                    show Damien Worry at left
                    "Your mumbled response is too low for Gilbert to catch, but Damien bites his lip nervously beside you, clearly afraid he might have overheard."
                "I'm not sure, but I'd like to read it someday." if True:
                    $ corruption -= 1
                    show chelsea blank
                    "As left out as you feel in their conversation, you wonder what it must be like to be into these sort of activities."
                    "Maybe it wouldn't be so bad to read it in the future, especially if it brings you closer to Damien."
                    $ damienconfidence += 2
                    if club == "track":
                        show chelsea happy
                        pcname "Honestly? I'm not sure. I've never read your comic before, but if Damien's so excited about it, it must be good."
                        pcname "I guess I could give it a try."
                    elif club == "cheer":
                        show chelsea happy
                        pcname "Well, comics aren't usually for me, but Damien's just so excited about it; I think I could read it sometime."
                    elif club == "yearbook":
                        show chelsea embarrassed
                        pcname "I-I've never read it, but I'd like to! Especially if Damien likes it as much as he says he does..."
                    "Your heart flutters as a smile breaks out on Damien's face, adoration flooding his eyes."
                    show Damien Shocked at left
                    D "Really? You'd read it?"
                    show Damien Laugh at left
                    D "That's awesome, [pcname]! I have an extra copy at home you can borrow. I'll bring it around next time."
                    D "{i}This{/i} one is going in a frame in my bedroom."
                    show Damien Happy at left
                    "Gilbert" "A good use for it. This is a rare book. You'll want to take good care of it."
                    "Gilbert" "It's always so exciting to see young people willing to give the genre a try. Things were very different when I was your age..."
                    "Gilbert" "Ah, but let's not reminisce. These were times before you were born, haha!"
            show Damien Happy at left
            show chelsea happy
            "Gilbert scrawls his name on top of Damien's comic book along with a short message and passes it back to him. Damien clutches the book protectively to his chest."
            D "Thank you so much, Gilbert. This means the world to me."
            "Gilbert" "No problem at all. It was a pleasure to meet the both of you. Have a nice day, now."
            "Gilbert gives you both a slight wave before gesturing for the next group to step forward. Damien says his goodbyes, leading you away."
            if damienconfidence >= 50:
                show Damien Laugh at left
                D "Wow... That was amazing! I can't believe I own a {i}signed{/i} original copy! My dad is going to flip!"
            elif True:
                show Damien Worry at left
                D "Hey... Uh, thanks for waiting so long to meet him with me, [pcname]. I know it's not really your thing, but it meant a lot to me..."
                "Damien clears his throat uncomfortably and carefully slides the comic book into his backpack before it can get damaged."
            $ damiencomicsigned = True
    show Damien Happy at left
    D "So, uh, where do you want to go next?"
    show chelsea blank
    "You tap your chin, considering your options."
    show chelsea happy
    pcname "I don't mind just walking around until something catches my eye."
    D "Okay. Yeah, let's do that."
    if damienconfidence >= 50:
        "Damien takes your hand in his, swinging your arms gently as you wander through the mall."
    elif True:
        "Damien's hand twitches toward yours but stops short, unsure. You take it, swinging your arms gently as you wander through the mall."
    "Now that you're past the crowded geek store, there doesn't seem to be as many people around shopping. It seems like that was the most congested area of the mall."
    "Although, glancing at the food court, you come to an understanding as to where everyone ran off to. It must be lunch time."
    "Your stomach growls a little, taken in by the smell of Chinese take-out and sandwiches. Maybe it wouldn't be so bad to eat now..."
    "As you approach the food court, a sign in a nearby store catches your eye: {i}Select bras half off!{/i} Posters of airbrushed models in lingerie cover the store windows while mannequins display silk panties and push-up bras in the entrance."
    "It's definitely been a while since you got a new bra, especially a nice one. And they're on sale, too..."
    menu damien_lingeriestore:
        "Enter the store." if True:
            "You pull Damien to a halt outside of the store, unable to resist the wafting perfume of roses and the soft undergarments."
            show chelsea laugh
            pcname "I want to stop in here."
            show Damien Shocked at left
            "Damien looks up at the store in surprise, his eyes wide and face flushed."
            D "Uh, here?"
            show chelsea sad
            pcname "Yeah. Do you have a problem with it?"
            if damienconfidence >= 50:
                show Damien Worry at left
                D "Um... No, I guess not. I've just never been in one of these stores before. It looks kind of uncomfortable for a guy to be in, you know?"
                show Damien Happy at left
                D "But if you really want to go, I don't mind. It might be neat to check it out for once."
                show chelsea happy
                "You grin, delighted by Damien's willingness to go along with you."
                "Loping your arm with his, you both step into the store."
                hide chelsea with moveoutright
                hide Damien Happy with moveoutleft
                $ damienenters = True
            if damienconfidence <= 50:
                show Damien Worry at left
                D "Um... Well no, but..."
                "He averts his eyes from the provocative posters, clearly uncomfortable with the amount of cleavage pressed into the camera's frame."
                show Damien Blank at left
                D "I think I'm going to sit this one out. I'll be on the bench over there when you're done."
                if corruption >= 25:
                    if club == "track":
                        show chelsea confused
                        "You stare at him, appalled. Is he really going to just abandon you on your date? It's not like you're trying to drag him into a brothel. It's a store, for God's sake."
                        pcname "Seriously? You're not just going to leave and make me go in by myself, are you?"
                    elif club == "cheer":
                        show chelsea happy
                        "You try to bite back the smirk that tugs at the corner of your lips. He's so clearly flustered by the sexual animosity of the store. It's almost endearing, in a way..."
                        "But really it just makes you want to tease him more."
                        pcname "You're not just going to abandon me, are you, Damien? I thought we were having a date."
                    elif club == "yearbook":
                        show chelsea sad
                        "Your smile falls as anxiety seizes your chest."
                        "The idea of entering a lingerie store by yourself is intimidating enough, but to have to do it alone..."
                        "You had hoped he would be more willing to share the embarrassment at least."
                        pcname "A-Are you sure? I... I thought we could go together... I don't really want to go in by myself..."
                    $ damienenters = True
                    show Damien Worry at left
                    D "Well, I mean..."
                    "Damien shifts uncomfortably in place, trying to find a place to settle his gaze on that isn't underwear or photo manipulated tits."
                    D "I-I... I guess I could go in... If you insist..."
                    show chelsea happy
                    "You seize his arm in yours, unwilling to let him change his mind, and drag him into the store."
                    hide chelsea with moveoutright
                    hide Damien Worry with moveoutleft
                    $ damienenters = True
                elif True:
                    show chelsea sad
                    pcname "Oh... Okay. I'll meet you out here then."
                    hide Damien Blank with moveoutleft
                    "You give Damien a slight parting wave before stepping into the store."
            show bg black with fade
            pause 0.5
            show bg Shop with dissolve
            show chelsea blank at right with moveinright
            "The sweet scent of roses and vanilla greets you both as you enter, beckoning you inside. Various bras and panties are littered throughout the store, separated by size, style, and collection."
            if damienenters == True:
                if damienconfidence >= 50:
                    show Damien Happy at left with moveinleft
                    "Damien looks around the store curiously, casually falling in step beside you as he takes it all in for the first time."
                    pcname "So? Is it as bad as you thought?"
                    D "Oh, yeah. Absolutely. But it's really fascinating at the same time."
                elif True:
                    show Damien Worry at left with moveinleft
                    "Damien tries to find something to look at, but each new direction offers a more sexual and scandalous undergarment. He ends up staring at the ground as he follows you around, his face burning pink."
                    "You feel a little thrill at watching him squirm uncomfortably in the store, too embarrassed to take his eyes off of the ground."
            elif True:
                "There are so many varieties of bras and panties that you're almost unsure of where to start."
            show chelsea blank
            "You wander toward a newer collection of bras, taken in by the lace sewn into the top. Beside it are a series of strings that somehow make up a bra, although you doubt it's used for the support."
            if damienenters == True:
                if damienconfidence >= 50:
                    show Damien Neutral at left
                    "Damien stares at the strings, afraid to touch it, but morbidly curious."
                    D "How would you even wear this? I feel like it would get tangled in the wash really easily."
                    "He turns his attention to the lacy bras you're admiring. They're a little out of your price range right now, but they're cute nonetheless."
                    show Damien Happy at left
                    D "Hey, uh, can I say something?"
                    pcname "Sure. Go ahead."
                    D "I think you would look good in that one."
                    "Damien points to a soft teal bra displayed on one of the mannequins. It has white lace on the trim and a little bow at the front, along with a set of patching panties."
                    show Damien Shocked at left
                    D "Ah, not trying to be creepy or anything! I'm not trying to picture you in it. I mean- I {i}am{/i}, but not like that! I just... I feel like teal would be a good color on you..."
                    if club == "track":
                        show chelsea laugh
                        pcname "I know what you're trying to say. Thanks! I hadn't really considered that color before."
                    elif club == "cheer":
                        show chelsea happy
                        pcname "Really? Hm. Maybe I should start wearing teal around you more often then..."
                    elif club == "yearbook":
                        show chelsea embarrassed
                        "You feel your face heat up at his fumbling implications."
                        pcname "T-Thank you. M-Maybe I'll try something like that..."
                    show Damien Happy at left
                elif True:
                    "You glance back at Damien with a mischievous smirk. He's not even paying attention when you pick up the set of strings and hold them in front of your breasts."
                    show chelsea happy
                    pcname "Damien, can I get your opinion on something?"
                    D "A-Ah, yeah. Hm?"
                    show Damien Shocked at left
                    "He looks up. You can visibly see scarlet flood his face to the tips of his ears as he takes in the strings draped in front of your torso."
                    if club == "track":
                        pcname "Doesn't this look hot?"
                    elif club == "cheer":
                        show chelsea laugh
                        pcname "Don't you think this looks cute?"
                    elif club == "yearbook":
                        show chelsea embarrassed
                        pcname "W-what do you think?"
                    "Damien stands there gaping at you, utterly speechless. You revel in the mortification and ashamed arousal mixed on his face."
                    D "W-W-What do {i}I{/i} think?"
                    if club == "track":
                        show chelsea confused
                        pcname "Is there another Damien I should be talking to?"
                    elif club == "cheer":
                        show chelsea happy
                        pcname "Of course you, silly."
                    elif club == "yearbook":
                        pcname "Y-Yes..."
                    D "I-I- Um- I- Er-"
                    show Damien Worry at left
                    "He ducks his head down, unable to look any longer at the strings."
                    D "I-I think it's too much..."
                    if club == "track":
                        show chelsea shocked
                        pcname "Really? Huh. I thought you might be into this sort of thing."
                    elif club == "cheer":
                        show chelsea happy
                        pcname "Oh, boo. And here I thought you might like to see me in it."
                        "You wink at the poor, flustered boy."
                    elif club == "yearbook":
                        show chelsea sad
                        pcname "I-I see..."
                    show chelsea happy
                    pcname "Maybe something a little more average then. What about this?"
                    "You pick up a teal bra with white lace and a little bow in the front. Damien barely glances at it before taking a sudden interest in the floor."
                    D "That... That could... b-be nice..."
            elif True:
                "For fun, you try to imagine yourself in the set of strings. Would Damien like something like that? You're not sure."
                "Opting for something a little less daring, you browse through a set of lace-trimmed bras. A teal one in particular catches your eye."
            "As you search through the bras in your size, a peppy woman with dark hair and freshly manicured nails approaches you. The nametag over her breast reads 'Wendy'."
            "Wendy" "Hi! How are we doing over here today? Can I help you find anything?"
            if club == "track":
                pcname "Hey. No, I'm good. Just looking around."
            elif club == "cheer":
                pcname "Hi! No, yeah, I'm okay, just browsing."
            elif club == "yearbook":
                show chelsea embarrassed
                pcname "Ah, n-no... I'm just looking..."
            "Wendy" "Awesome! Is this your first time shopping here?"
            show chelsea embarrassed
            pcname "Yeah. I mean, I've looked online once in a while, but I never got around to purchasing."
            show chelsea blank
            "Wendy" "That's totally okay! Welcome! My name's Wendy, I'll be wandering around the store if you need anything."
            "Wendy" "Just so you know, all of the Pretty Kitty, Angel Bust, and Godsend bras are half off. Just look for the ones with a little red sticker on the tag."
            show chelsea laugh
            pcname "Okay. Thank you!"
            "Wendy" "No problem!"
            show chelsea happy
            if damienenters == True:
                if damienconfidence >= 50:
                    show Damien Neutral at left
                    "Damien looks back at the teal bra, trying to find the product's name on the tag."
                    D "Uh, does that include these ones here?"
                elif True:
                    pcname "Does that include these ones?"
                    "You gesture between the lace bras and the string ones, relishing in Damien's embarrassment as you make a point to run your fingers over the strings."
            elif True:
                "You pick up the teal bra you were eyeing and try to find the product's name on the tag."
                pcname "Are these one of the bras on sale?"
            show chelsea sad
            "Wendy" "Unfortunately these bras here aren't on sale since they're brand new, but they look fantastic and have easily become some of my favorites."
            "Wendy" "Since it's your first time here, we should take you in the back for a bra fitting. Does that sound good?"
            show chelsea happy
            pcname "Ah, yeah. I can do that."
            "Wendy" "Awesome! You can come right this way with me. We have some bases in the back we'll try to fit you in, and then once you know your size you can browse the store and choose what you like!"
            "Wendy" "Are we shopping for any special occasion? Or something to please a boyfriend, perhaps?"
            if damienenters == True:
                show Damien Worry at left
                "You don't miss how her gaze falls on Damien, clearly amused by his discomfort."
                pcname "Sort of. It's nice to get a second opinion."
                "Wendy" "Especially if they're going to be the ones taking it off later. Right, honey?"
                "Wendy throws Damien a wink and laughs."
                if damienconfidence >= 50:
                    show Damien Laugh at left
                    "A blush paints Damien's cheeks. He laughs awkwardly, scratching the back of his head."
                elif True:
                    "Damien stares back down at his feet, absolutely mortified by her suggestion."
                menu damien_lingeriejoke:
                    "Tease him with her." if True:
                        $ corruption += 3
                        $ damienconfidence -= 1
                        show Damien Worry at left
                        if club == "track":
                            show chelsea laugh
                            pcname "If he gets that far, haha!"
                        elif club == "cheer":
                            show chelsea happy
                            pcname "Hmm, I don't know. I might be the one taking it off for him."
                        elif club == "yearbook":
                            show chelsea embarrassed
                            "You {i}should{/i} feel guilty about enjoying Damien's discomfort, but something about the way he squirms sends a thrill through your body that you can't explain."
                            pcname "I'd like to see him try, at least."
                        "Wendy laughs along with you as Damien shuffles awkwardly behind, unable to look either of you in the face."
                    "Defend him." if True:
                        $ corruption -= 1
                        $ damienconfidence += 1
                        show Damien Worry at left
                        show chelsea shocked
                        "You're surprised by her inappropriate joke, and it's clear to you just how uncomfortable he is by her statement. The whole situation leaves you with an uneasy feeling in your stomach."
                        if club == "track":
                            show chelsea angry
                            pcname "What did you just say to us? That's really inappropriate. Not cool."
                        elif club == "cheer":
                            show chelsea confused
                            pcname "Hey, that's not okay. Our sex life is a private thing."
                        elif club == "yearbook":
                            "You feel your own blush creep onto your face, embarrassed by her suggestion."
                            pcname "I-It isn't like that! W-we just started dating... T-That isn't appropriate..."
                        show Damien Shocked at left
                        show chelsea blank
                        "Wendy's smile drops, surprised to find you disagree with her. She straightens herself uncomfortably."
                        "Wendy" "...Of course. I apologize. Right this way, please."
                        show Damien Happy at left
                        "You glance sideways at Damien to make sure he's alright. He smiles at you sheepishly, taking your hand in his. He gives it a gentle squeeze."
                        D "Thanks."
                        show chelsea happy
                        "You smile and squeeze his hand back."
            elif True:
                pcname "Sort of. My boyfriend's right outside."
                "Wendy laughs."
                "Wendy" "They all do that, don't they? Too afraid to come in themselves. Which one is he?"
                "You point at Damien reclined on a bench outside, absorbed in his phone."
                "Wendy" "Oh, dear. It doesn't look like you'll need to do much to impress {i}him{/i}."
                show chelsea confused
                pcname "What do you mean?"
                "Wendy" "Well... You see the cargo shorts, right?"
                "She shakes her head with a sigh."
                "Wendy" "Boys like that are so easy. You show up in something from here and they'll be eating out of the palm of your hand."
                "Wendy" "Let's give him something that'll really make him step up his game for you, okay, honey?"
                "She nudges you with a wink."
                menu damien_malljibe:
                    "Tease him with her." if True:
                        $ corruption += 3
                        $ damienconfidence -= 1
                        "It's almost a relief to hear her bring up Damien's dreaded cargo shorts. Someone who {i}understands!{/i}"
                        if club == "track":
                            show chelsea laugh
                            pcname "I'll wear just about anything to see him torch those cargo pants to the ground."
                        elif club == "cheer":
                            show chelsea happy
                            pcname "That's a pretty big promise. I hope you can hold up your end of the bargain."
                        elif club == "yearbook":
                            show chelsea embarrassed
                            pcname "P-Please... Those shorts just need to {i}go{/i}..."
                        "Wendy laughs along with you as she escorts you to the dressing room."
                    "Defend him." if True:
                        $ corruption -= 1
                        $ damienconfidence += 1
                        show chelsea blank
                        "You don't see what's supposed to be so funny about her teasing. You may hate Damien's cargo shorts, yes, but you're his {i}girlfriend{/i}. That doesn't give other women the right to pick on him."
                        if club == "track":
                            show chelsea confused
                            pcname "I don't think he needs to step anything up. I like him the way he is."
                        elif club == "cheer":
                            show chelsea confused
                            pcname "Maybe you can say that because {i}your{/i} boyfriend needs to step it up, but I'm happy with mine."
                        elif club == "yearbook":
                            show chelsea sad
                            pcname "P-Please don't talk about my boyfriend like that... I'm really happy with how he is..."
                        "Wendy" "I-Oh."
                        show chelsea blank
                        "She stays still for an awkward moment, not having anticipated your negative response. You wonder how many girls are unhappy in their relationships that this woman feels comfortable shaming your boyfriend."
                        "Wendy" "I apologize. Let's get that fitting done, shall we?"
            if damienenters == True:
                "You're about to follow her into the dressing room, but Wendy stops abruptly in front of you, holding out a hand to halt Damien."
                "Wendy" "Sorry, but you can't come back here. I know young couples like to come here together and shop for those 'special occasions', but we can't have any of that happening in our dressing rooms."
                if damienconfidence >= 50:
                    show Damien Shocked at left
                    D "Ah! No! Of course not! Ah, sorry, I really wasn't trying to follow you in there!"
                    show Damien Happy at left
                    D "I'll just, ah, stand outside here then. Come meet me when you're done."
                    hide Damien Happy with moveoutleft
                    "He gives you an awkward wave before trying to somewhere to comfortably wait."
                elif True:
                    show Damien Shocked at left
                    "You aren't sure if you're looking at Damien's face or a fire truck with how red it is. All you know is something or someone needs hosed down."
                    "He covers his face, positively mortified."
                    D "O-O-Of course! I-I'll just be out here!"
                    D "Alone... with... all of the... underwear..."
                    hide Damien Shocked with moveoutleft
                    "He glances around the store, clearly trying to find a safe place to stand. You giggle, following Wendy into the dressing rooms."
            elif True:
                pass
            "The dressing rooms match the rest of the store in varying shades of bright pink and black. Wendy picks up a measuring tape and escorts you in front of a mirror."
            "Wendy" "Are you okay taking your shirt off?"
            $ clothes = 'underwear'
            "You nod, pulling the fabric over your head. Wendy measures your breasts in the bra, writing down the results on a small card. She passes you a few black bras to try on."
            "You spend a little time trying on the different styles of bra, settling on a couple that you like. Wendy writes them down on the card and passes it back to you."
            "Wendy" "This will have your bra size and all of the styles you really liked today. They'll all be marked in the store, and some are even on sale, so if you need help finding any, feel free to come get me."
            show chelsea happy
            pcname "Okay. Thank you!"
            hide chelsea with moveoutright
            if damienenters == True:
                show Damien Happy at left
                $ clothes, hair = casualwear
                show chelsea at right with moveinright
                "Damien looks relieved when you step out of the dressing room, clothed and ready to shop."
                if damienconfidence >= 50:
                    D "How'd it go?"
                    pcname "It went fine. Do you want to help me pick out some bras to try on?"
                    "He gives you a bashful smile."
                    D "Ah, sure. I can definitely try..."
                    show chelsea laugh
                    pcname "Awesome!"
                    show chelsea happy
                    pcname "I'm looking to get some matching panties, too, so let's keep an eye out together, okay?"
                    D "Yeah. I can do that."
                elif True:
                    $ clothes, hair = casualwear
                    show chelsea at right with moveinright
                    D "Um, are you done? Are you ready to go?"
                    pcname "Not yet. I still need to pick a couple of bras out here and try them on in the back."
                    show Damien Worry at left
                    D "O-Oh... Okay..."
                    pcname "And I want you to help me pick some out."
                    "Damien bites his lip. The fear of your suggestion is written all over his face. He gives a small nod."
                    show chelsea laugh
                    pcname "Awesome! I'm looking to get some matching panties, too, so keep an eye out, okay?"
                    show chelsea happy
                    D "S-Sure."
            elif True:
                pass
            "Even though the store's space is limited by the mall, you can't get over how huge it is and what a wide selection of lingerie it carries."
            if damienenters == True:
                "You lead Damien through the different collections of lingerie, pointing out a few of your favorites and cringing at the worst."
                "A particularly sheer teal set catches your eye, fitted with black lace around the cups and edges of the panties."
                pcname "Ah, Damien, what do you think of this?"
                if damienconfidence >= 50:
                    show Damien Neutral at left
                    "Damien pauses, glancing between you and the mannequin showing the lingerie off. Even though he looks a little embarrassed, he smiles."
                    show Damien Happy at left
                    D "I think it's cute, actually. That color really suits you..."
                    hide Damien Happy with moveoutleft
                elif True:
                    show Damien Shocked at left
                    "He reluctantly looks to the set on the mannequin, his face burning with shame. He just as soon returns his gaze to the ground."
                    show Damien Worry at left
                    D "I-I'm not sure. It... It's cute..."
                    "His last words come out a mumble, but you're barely able to make them out."
                    hide Damien Worry with moveoutleft
                "Satisfied, you find the set in your size and head to the dressing room."
            elif True:
                "After some thorough searching- especially in the sale section- you return to the dressing rooms with a pretty teal set to try on."
                "It's a particularly sheer teal bra and panty set, fitted with black lace around the cups and edges of the panties."
            "Wendy waits for you in the dressing room and quickly gets you set up with a stall of your own."
            show chelsea blank
            "They're much nicer stalls than any other store you've been in, with a plush chaise, a giant mirror, several hooks on the walls, and even a scanner to check the price of your lingerie."
            "You carefully hang up your lingerie and start to peel your clothes off."
            hide chelsea with dissolve
            pause 1.0
            $ clothes = 'underwear'
            show chelsea with dissolve
            "Looking at your current bra, you can see where it's failed you; there are gaps in the cups, the straps often slide off of your shoulders, and the elasticity has almost worn out."
            "You unclasp your bra and drop it onto the chaise. The new bra feels so much softer in your hands."
            "You pull it on and clasp it in the back, taking a moment to admire how it fits to your body."
            show chelsea happy
            "It's a tighter fit than your old bra and, after adjusting the straps a little, you're surprised by just how well your breasts fit in the cups."
            "You slide the matching panties over your own and look in the mirror."
            hide chelsea with dissolve
            pause 1.0
            $ underwear2 = True
            show chelsea with dissolve
            if club == "track":
                "You turn around a couple of times, unable to stop staring at the attractive curve of your breasts inside of the sheer fabric."
                show chelsea laugh
                pcname "Ooh, this is so comfortable! I definitely wasn't expecting that!"
            elif club == "cheer":
                "You pose a few times in the mirror, making sure to get a good look of all your best angles."
                show chelsea laugh
                pcname "Oh my god, this looks {i}hot!{/i} Damien would {i}lose{/i} it if he saw this!"
                "You bend over in front of the mirror, admiring the cleavage that peers out from the sheer teal fabric."
            elif club == "yearbook":
                show chelsea embarrassed
                "You can't help but feel a little embarrassed as you realize just how attractive your breasts look in the sheer fabric."
            show chelsea happy
            "The black lace just barely covers your nipples, not leaving much to the imagination."
            "The panties match as well; a sheer teal fabric with black lace barely disguising your crotch and hugging your hips."
            show chelsea shocked
            pcname "Wow... This looks even better than I thought it would..."
            show chelsea laugh
            pcname "I wonder what Damien would say if he saw it!"
            "Suddenly, an idea pops in your mind."
            show chelsea happy
            pcname "I {i}could{/i} show it to him on my phone..."
            menu damien_lingerietext:
                "Send Damien pictures." if True:
                    $ corruption += 1
                    if club == "track":
                        "Grinning, you strike a confident pose in the mirror, showing off how well the bra and panties fit onto your body, and snap a picture."
                    elif club == "cheer":
                        "Using one hand to cup your breast, you tilt your head to the side and angle the camera to best show off your assets."
                    elif club == "yearbook":
                        show chelsea embarrassed
                        "Both embarrassed and excited by your brave idea, you shyly position the camera to capture the bra and panties, using your arm to cover anything you're too embarrassed to show."
                    show DMSS1 at truecenter with flash
                    "{i}CLICK!{/i}"
                    "{i}CLICK! CLICK! CLICK!{/i}"
                    "You look back at your camera's gallery, deleting the less flattering takes before picking one out and sending it to Damien."
                    "It hardly takes any time at all for him to respond."
                    hide DMSS1 with dissolve
                    if damienconfidence >= 50:
                        call screen TextingScene("Damien",
                        [
                            TextMessage("DMSS2", image = True, sender = False),
                            TextMessage("Oh WOW!"),
                            TextMessage("That's"),
                            TextMessage("I like that."),
                            TextMessage("I like that very much.")
                        ])
                    elif True:
                        call screen TextingScene("Damien",
                        [
                            TextMessage("DMSS2", image = True, sender = False),
                            TextMessage("Did you mean to send this to me??"),
                            TextMessage("oh god I think the lady working here just saw it over my shoulder"),
                            TextMessage("Um"),
                            TextMessage("Ahhhhhhh"),
                            TextMessage("Well? Do you like it?", sender = False),
                            TextMessage("adsakdjaksfjadsja"),
                            TextMessage("..."),
                            TextMessage("yes")
                        ])

                    show chelsea laugh
                    "A small giggle escapes your throat. You cover your mouth, trying to muffle the noise."
                    "You can already imagine his shocked expression when he opened your picture up in public."
                    show chelsea happy
                    "You almost wish you'd been able to see his reaction in person..."
                    $ damienlingeriepictures = True
                    if mattchain >= 2:
                        "Before you can put your phone away, Matt's face sneaks up in the back of your mind. This would definitely be the sort of thing he likes..."
                        menu matt_lingerietext:
                            "Send Matt the pictures." if True:
                                $ corruption += 5
                                "You scroll through your phone until you find your last text exchange. Opening your gallery, you choose one of the more attractive pictures and send it."
                                "You're not sure when to expect his response. Usually he's pretty fast, but that's always at school. You have no idea what he gets up to on the weekends."
                                if defymatt == True:
                                    show chelsea blank
                                    "You're not even sure why you sent it in the first place. The last thing he needs is more blackmail against you."
                                    "Although, you're sure he would find these pictures one way or another, even if it means stealing your phone to do it."
                                "You're about to get changed when his response lights up the screen."
                                call screen TextingScene("Matt",
                                [
                                    TextMessage("DMSS2", image = True, sender = False),
                                    TextMessage("You better buy that."),
                                    TextMessage("I don't even know if I can afford it.", sender = False),
                                    TextMessage("Don't care. Bring it to school. I'll tell you when I want you in it.")
                                ])
                                show chelsea happy
                                "A thrill runs through your body at his suggestion. Perhaps sending him these pictures was a good idea after all..."
                                show chelsea sad
                                "A small part of your conscious scolds you for the desire unfolding in your belly, a desire created by an entirely different man than your boyfriend."
                                "Damien would be heartbroken if he knew about this, you're sure of it."
                                show chelsea blank
                                pcname "{i}But he doesn't have to know... At least not right now.{/i}"
                                "You put your phone away and try to push Matt, and all the problems that come with him, far from your mind."
                                $ mattlingeriepictures = True
                            "Keep them to yourself." if True:
                                $ corruption -= 1
                                show chelsea blank
                                "You shake your head and exit your photo gallery. The last thing you need is for Matt to show these pictures to Damien and prove you sent them..."
                                show chelsea sad
                                "Guilt gnaws at your heart at the idea of Matt and Damien even talking, let alone about you."
                                "You hadn't exactly thought of either one together, but you're sure Damien thinks of you as exclusive."
                                "He would be heartbroken if he knew what you were doing with Matt... And Matt..."
                                if defymatt == True:
                                    "He's made it clear you're just a fucktoy to him. And even if you tried to break it off, he has that picture of you..."
                                elif True:
                                    "He's made it clear you're just a fucktoy to him. So why can't you bring yourself to break this weird thing you have with him off?"
                                show chelsea blank
                                "You shake your head again, as if the physical act will remove him from your mind. Today is your date with Damien; the last person you should be thinking about is Matt."
                "Keep it to yourself." if True:
                    $ corruption -= 1
                    "You consider the idea for a moment, then shake your head."
                    "If you're going to show off new lingerie to him, you would rather do it in person."
                    if mattchain >= 2:
                        "Before you can put your phone away, Matt's face sneaks up in the back of your mind. This would definitely be the sort of thing he likes..."
                        menu matt_lingerietext2:
                            "Send Matt the pictures." if True:
                                $ corruption += 5
                                "You scroll through your phone until you find your last text exchange. Opening your gallery, you choose one of the more attractive pictures and send it."
                                "You're not sure when to expect his response. Usually he's pretty fast, but that's always at school. You have no idea what he gets up to on the weekends."
                                if defymatt == True:
                                    show chelsea blank
                                    "You're not even sure why you sent it in the first place. The last thing he needs is more blackmail against you."
                                    "Although, you're sure he would find these pictures one way or another, even if it means stealing your phone to do it."
                                "You're about to get changed when his response lights up the screen."
                                call screen TextingScene("Matt",
                                [
                                    TextMessage("DMSS2", image = True, sender = False),
                                    TextMessage("You better buy that."),
                                    TextMessage("I don't even know if I can afford it.", sender = False),
                                    TextMessage("Don't care. Bring it to school. I'll tell you when I want you in it.")
                                ])
                                show chelsea happy
                                "A thrill runs through your body at his suggestion. Perhaps sending him these pictures was a good idea after all..."
                                show chelsea sad
                                "A small part of your conscious scolds you for the desire unfolding in your belly, a desire created by an entirely different man than your boyfriend."
                                "Damien would be heartbroken if he knew about this, you're sure of it."
                                show chelsea blank
                                pcname "{i}But he doesn't have to know... At least not right now.{/i}"
                                "You put your phone away and try to push Matt, and all the problems that come with him, far from your mind."
                                $ mattlingeriepictures = True
                            "Keep them to yourself." if True:
                                $ corruption -= 1
                                show chelsea blank
                                "You shake your head and exit your photo gallery. The last thing you need is for Matt to show these pictures to Damien and prove you sent them..."
                                show chelsea sad
                                "Guilt gnaws at your heart at the idea of Matt and Damien even talking, let alone about you."
                                "You hadn't exactly thought of either one together, but you're sure Damien thinks of you as exclusive."
                                "He would be heartbroken if he knew what you were doing with Matt... And Matt..."
                                if defymatt == True:
                                    "He's made it clear you're just a fucktoy to him. And even if you tried to break it off, he has that picture of you..."
                                elif True:
                                    "He's made it clear you're just a fucktoy to him. So why can't you bring yourself to break this weird thing you have with him off?"
                                show chelsea blank
                                "You shake your head again, as if the physical act will remove him from your mind. Today is your date with Damien; the last person you should be thinking about is Matt."
            show chelsea sad
            pcname "This outfit is so cute... I want to buy it..."
            "Tilting yourself in front of the small computer built into the wall, you run the barcode across the scanner and look at the price."
            show chelsea shocked
            pcname "$80?!"
            pcname "And that's just for the bra! I guess this isn't one of the ones on sale..."
            show chelsea sad
            pcname "And then it's another $20 for the panties, so $100 total..."
            pcname "But they're both so cute..."
            "You bite your lip and stare at the price on screen."
            menu damienlingeriepurchase:
                "Purchase lingerie. ($100)" if Cash >= 100:
                    show chelsea happy
                    "Despite it not being on sale, you love the set too much to leave without it."
                    hide chelsea with dissolve
                    pause 1.0
                    $ clothes, hair = casualwear
                    show chelsea happy at right with dissolve
                    "You change back into your regular clothes and carry the lingerie with you out of the dressing room."
                    if damienenters == True:
                        show Damien Happy at left with moveinleft
                        "You find Damien standing awkwardly by a selection of perfumes; the only things in the store that couldn't possibly embarrass him."
                        if damienconfidence >= 50:
                            "He smiles as you approach, his gaze wandering to the lingerie in your arms."
                            D "All set?"
                            pcname "Just about. I just need to check out."
                        elif True:
                            "Damien looks up, relieved to see you."
                            D "H-Hey. Um, can we go now?"
                            pcname "Yeah. Let me just pay for this."
                            show Damien Shocked at left
                            "You hold up the lingerie, biting back a smirk as he shuffles uncomfortably in place."
                            D "Okay."
                        show chelsea shocked
                        "You turn, ready to to proceed to the cashiers, when you notice a bulge poking out of the side of Damien's shorts."
                        "You stop, glancing down at what's clearly a boner. "
                        menu damien_mallboner:
                            "Point it out." if True:
                                if club == "track":
                                    show chelsea laugh
                                    pcname "Whoa. Someone's happy to see me."
                                elif club == "cheer":
                                    show chelsea happy
                                    pcname "Damien, honey, were all these bras a little too much for you?"
                                elif club == "yearbook":
                                    show chelsea shocked
                                    pcname "Ah, Damien... Your pants..."
                                    D "My-? {i}Oh.{/i}"
                                if damienconfidence >= 50:
                                    show chelsea embarrassed
                                    "Damien glances down at the lingerie in your arms and pulls you under his arm. He presses his lips to your ear."
                                    if damienlingeriepictures == True:
                                        D "I can't help it. When you send me pictures like that..."
                                    elif True:
                                        "I can't help it. Picturing you in that sheer bra and those little panties..."
                                    D "All I want to do is make out with you against this wall."
                                    if club == "track":
                                        show chelsea laugh
                                        pcname "I think you want to do a little more than make out."
                                    elif club == "cheer":
                                        show chelsea happy
                                        pcname "{i}Only{/i} make out?"
                                    elif club == "yearbook":
                                        show chelsea embarrassed
                                        pcname "M-Make out?"
                                    "A sheepish grin spreads over his face."
                                    D "Well... maybe a little more than that."
                                elif True:
                                    "Damien glances down at the lingerie in your arms, his ears tinged red."
                                    show chelsea blank
                                    D "I'm sorry! I just..."
                                    show Damien Worry at left
                                    if damienlingeriepictures == True:
                                        D "I wasn't expecting those pictures..."
                                    elif True:
                                        D "I was just thinking of you... and..."
                                    D "It just sort of happened. I didn't mean- Sorry."
                                    "Damien shoves his hands into his pockets, flustered and unable to meet your gaze."
                                    if club == "track":
                                        show chelsea happy
                                        "Something about teasing him like this fills you with a sense of raw power. It's like sprinting towards the finish line; you want to see how far you can push."
                                    elif club == "cheer":
                                        show chelsea happy
                                        "You run your hand down his arm, enjoying the way he tenses under your touch. He's so sweet and naive... You can't help but want to tease him mercilessly."
                                    elif club == "yearbook":
                                        show chelsea embarrassed
                                        "You {i}should{/i} feel guilty seeing him so embarrassed, but it's almost endearing and fills you with a sense of... confidence?"
                                        "Maybe you like to tease him more than you're willing to admit."
                                pcname "I think I'm ready to check out now."
                                if damienenters == True:
                                    if damienconfidence >= 50:
                                        "Damien's gaze roves over your body quickly, his lips quirking into a smile."
                                        D "Yeah. I'm ready to check something out, too."
                                    elif True:
                                        D "Y-Yeah. That sounds good."
                                        "He glances at your choice of lingerie before shifting his legs, trying to adjust to the discomfort of his boner."
                                show chelsea happy
                                "You bite back a grin and lope your arm with his, taking your place in line behind the cash register."
                                "The line moves quickly, and your new underwear is wrapped and packed nicely away in a pretty pink bag."
                                show bg black with fade
                                pause 0.5
                                show bg Shop with dissolve
                            "Let it slide." if True:
                                show chelsea happy
                                "You try to ignore the obvious erection poking through his shorts, offering him a sympathetic smile instead."
                                "Opting to hold his hand, you head to the check-out line."
                                show bg black with fade
                                pause 0.5
                                show bg Shop with dissolve
                    elif True:
                        "Satisfied, you head to the check out counter and purchase your new lingerie."
                        "By the time you meet Damien at the store's entrance, your underwear is packed away safely in a nice pink bag where it can't fluster him any longer."
                        show bg black with fade
                        pause 0.5
                        show bg Shop with dissolve
                    $ damienlingeriepurchase = True
                    $ Cash -=100
                "Don't purchase." if True:
                    $ underwear2 = False
                    show chelsea blank
                    "As much as you love the lingerie, you can't fathom spending $100 on it right now. Maybe next time..."
                    hide chelsea with dissolve
                    pause 1.0
                    $ clothes, hair = casualwear
                    show chelsea at right with dissolve
                    "With a heavy heart, you change back into your regular clothes, leaving the lingerie on a rack outside."
                    if damienenters == True:
                        show Damien Happy at left with moveinleft
                        "You find Damien standing awkwardly by a selection of perfumes; the only things in the store that couldn't possibly embarrass him."
                        if damienconfidence >= 50:
                            "He smiles as you approach, his gaze wandering to your empty arms."
                            D "How'd it go?"
                            show chelsea sad
                            pcname "It was nice, but too expensive."
                            show Damien Blank at left
                            "Damien frowns, disappointed with the turn of events."
                            if damienlingeriepictures == True:
                                D "Oh. That sucks. You looked {i}really{/i} good in that."
                            elif True:
                                D "Oh. That sucks. I think you would've looked really good in that..."
                            show chelsea blank
                            D "Maybe next time, I guess."
                            D "You ready to head out?"
                            pcname "Yeah, I'm ready."
                        elif True:
                            "Damien looks up, relieved to see you."
                            D "H-Hey. Um, what happened to the...?"
                            show Damien Neutral at left
                            "He looks to your empty arms, searching for the lingerie. He looks almost disappointed that you don't have it."
                            pcname "Yeah. I'm all set."
                            D "Cool."
                            D "Um, how did it go?"
                            show chelsea sad
                            pcname "It went fine. It was too expensive, though."
                            D "O-Oh..."
                            if damienlingeriepictures == True:
                                D "It looked nice..."
                            elif True:
                                D "I'm sure it looked great..."
                            "He looks like he wants to say something else, but quickly shakes his head, banishing the thought."
                            show Damien Happy at left
                            show chelsea blank
                            D "Ah, let's head out then."
                            pcname "Sure."
                            show bg black with fade
                            pause 0.5
                            show bg Mall1 with dissolve
            "As you exit the store, you hear your stomach growl."
            D "Are you hungry? I bet the food court's calmed down a little by now."
            pcname "Yeah. Let's go grab something to eat."
        "Keep walking." if True:
            "As tempted as you are, the empty pit of your stomach is too much to ignore. You need to eat. Now."
    "You steer Damien in the direction of the food court. Your stomach growls louder, begging for sustenance."
    "The half-circle of food court stands are crowded, even for a Saturday, but the warm smell of burgers and Chinese food nearly have you drooling."
    show Damien Neutral at left
    D "Where do you want to eat?"
    show chelsea happy
    show Damien Blank at left
    pcname "Um..."
    menu damien_foodcourt:
        "Chinese Food" if True:
            "You catch sight of a middle-aged man offering free samples of orange chicken in front of the '{i}China Wok{/i}' counter."
            pcname "I think I want Chinese food."
            show Damien Happy at left
            D "Cool! Me, too. Let's eat there then."
            "You step in line beside Damien and look over the wide variety of affordable Chinese food. Orange chicken, General Tso's, Shrimp Lo Mein... It all sounds delicious."
            "As you approach the front of the line, a young woman with slick black hair greets you."
            "Cashier" "Hello! What can I get you?"
            menu damien_chinesefood:
                "Orange chicken." if True:
                    pcname "Mmm... Orange chicken and fried rice, please."
                    show Damien Happy at left
                    D "Ooh, my favorite. Make that two, please."
                "General Tso's." if True:
                    pcname "General Tso's sounds great. With some steamed rice, please."
                    show Damien Happy at left
                    D "And I'll have the orange chicken with fried rice, please."
                "Shrimp Lo Mein." if True:
                    pcname "It's been a while since I've had seafood... Shrimp Lo Mein, please."
                    show Damien Happy at left
                    D "And I'll have the orange chicken with fried rice, please."
            "Cashier" "Coming right up!"
            "You reach for your wallet, but Damien places his hand over yours."
            show Damien Laugh at left
            D "I got it."
            show Damien Happy at left
            show chelsea shocked
            pcname "Oh. Thank you."
            show chelsea happy
            "You both share a smile before Damien pays for your food. The cashier places your meals on a tray and nudges it toward you."
            "Cashier" "Have a nice day!"
        "Burgers" if True:
            "The wafting scent of burgers from '{i}Patty Prince{/i}' practically leaves your mouth watering."
            pcname "Definitely burgers."
            show Damien Happy at left
            D "Awesome. Let's eat there."
            show chelsea blank
            "You step in line beside Damien and look over the variety of burger and fry combinations."
            "When you reach the front of the line, a tired teenager with dark hair and a face full of acne greets you, his voice monotone."
            "You're pretty sure you've seen him in one of your classes before, but the dead look in his eyes tells you he's running on autopilot."
            "Cashier" "Hi, welcome to Patty Prince, home of Prince Patty, what can I get for you today?"
            menu damien_burger:
                "Cheeseburger and steak fries." if True:
                    show chelsea happy
                    "It's hard to go wrong with a classic."
                    pcname "I'll just have a cheeseburger and fries, please."
                    D "Make that two."
                "Turkey burger and salad." if True:
                    show chelsea happy
                    "It's always good to try to be a little healthy."
                    pcname "I'll have the turkey burger and a side salad, please."
                    D "Oh man, now I feel bad about my order. I'll just get a cheeseburger and steak fries, please."
                "Hamburger and curly fries." if True:
                    show chelsea happy
                    "There's nothing better than a box of curly fries!"
                    pcname "I'll have a hamburger and curly fries, please."
                    D "And I'll get the cheeseburger and steak fries."
            "The cashier punches in your order and gives you a slip."
            "Cashier" "That'll be $10.84. We'll call your number when it's ready."
            "You reach for your wallet, but Damien places his hand over yours."
            D "I got it."
            show chelsea shocked
            pcname "Oh. Thank you."
            show chelsea happy
            "You both share a smile before Damien pays for your food. You both step aside and wait a few minutes before your number is called. The cashier gives it to you in a brown paper bag."
            "Cashier" "Have a nice day."
        "Sandwiches" if True:
            "Nothing in the food court particularly catches your eye, but the idea of a nice sub from '{i}Greener Eats{/i}' sounds appetizing."
            pcname "I could go for a sub right now."
            show Damien Happy at left
            D "Sounds good. Let's get some sandwiches then."
            "You step in line beside Damien and look over the menu, your attention caught between the wide variety of signature sandwiches."
            "A peppy blonde teen greets you when you reach the front of the counter. You might recognize her from one of your classes."
            "Cashier" "Hi! What can I get you folks today?"
            menu damien_sandwiches:
                "Meatball sub." if True:
                    "It's hard to mess up a simple meat and cheese sandwich."
                    pcname "I'll have the meatball sub, please, and a bag of chips."
                    D "Hmm... I'll take the turkey sub."
                "Turkey sub." if True:
                    "It's hard to go wrong with a classic."
                    pcname "I'll have a turkey sub, please, and a bag of chips."
                    D "Yum... Make that two, please. Thank you."
                "Tuna sub." if True:
                    "Something about a tuna sandwich just sounds great right now!"
                    pcname "I'll have a tuna sub please, and a bag of chips."
                    "Damien makes a face at your choice, but quickly adds in his order."
                    D "I'll just get a turkey sub, please."
            "Cashier" "Coming right up!"
            "You reach for your wallet, but Damien places his hand over yours."
            D "I got it."
            show chelsea shocked
            pcname "Oh. Thank you."
            show chelsea happy
            "You both share a smile before Damien pays for your food. The cashier places your sandwiches in a slim bag and passes it to you."
            "Cashier" "Have a nice day!"
    "You both set your food down at a small, comfortable around table near the back of the food court and proceed to dig in."
    "After a few moments of joyous, blissful eating, Damien clears his throat."
    show Damien Neutral at left
    D "You mentioned you had club earlier today. What club are you in?"
    if club == "track":
        pcname "I'm on the track team."
        D "Track? Oh, wow. You must be really into exercise and stuff. I'm such a couch potato..."
    elif club == "cheer":
        pcname "I'm on the cheerleading squad."
        D "Cheerleading? Oh, wow. I had no idea I was dating a cheerleader... That's kind of cool."
    elif club == "yearbook":
        show chelsea embarrassed
        pcname "I-I'm in yearbook."
        D "Yearbook? Oh, wow. You must be really creative. I'm the worst at art. I mean, I can draw stick figures, but..."
    show Damien Happy at left
    D "What do you usually do in club?"
    if club == "track":
        show chelsea laugh
        pcname "We have a lot of track meets. Usually it just involves a lot of running, pacing ourselves, stuff like that. It's a lot of hard work."
        D "Hard {i}physical{/i} work. Yikes. Ah, no offence. I'm really bad at exercising. I'd much rather work out my brain."
    elif club == "cheer":
        show chelsea happy
        pcname "We practice a lot of cheers and dance routines. Once we have everything memorized, we'll start going out to perform."
        D "In front of the whole school... That's insane. I mean, you must be used to it, but I'd get nervous with all those people watching me. I feel like they would just be waiting for me to fail."
    elif club == "yearbook":
        show chelsea embarrassed
        pcname "W-Well, sort of... everything. Some people play games, but lately I've been trying to learn photography..."
        D "That's really cool! What kinds of pictures do you take?"
        pcname "Ah, anything that catches my eye."
        D "That's neat. I hope I get to see some of your pictures someday."
    D "Do you like your club?"
    menu damien_clubenjoyment:
        "Yeah!" if True:
            if club == "track":
                show chelsea laugh
                pcname "Yeah! It's a lot of hard work, but I like to push myself and see what I can accomplish."
            elif club == "cheer":
                show chelsea laugh
                pcname "Totally! It's so much fun getting to learn new dances and cheers. The outfit is really cute, too."
            elif club == "yearbook":
                show chelsea embarrassed
                pcname "Y-yeah. I get to spend a lot of time by myself learning how to photograph. It's relaxing..."
            D "That's great. It's always important to have some kind of interest in the club you're in."
        "Not really..." if True:
            if club == "track":
                show chelsea confused
                pcname "No. It's okay, I guess, but I'd rather have picked something else..."
            elif club == "cheer":
                show chelsea confused
                pcname "Not really. It's all very catty. I wish I could've had more options when I started here."
            elif club == "yearbook":
                show chelsea sad
                pcname "N-Not really... I wish I could have tried something else..."
            show Damien Blank at left
            D "Oh... I'm sorry to hear that."
    show chelsea blank
    pcname "What about you? You're in the biology club, right? Do you like it?"
    "A genuine smile spreads across his face. Damien dabs his lips with a napkin, nodding."
    show Damien Happy at left
    D "Yeah. I love my club. It'll look really good on my college resume, especially to get into veterinary school."
    show chelsea shocked
    pcname "What made you want to work with animals?"
    show chelsea blank
    "Damien considers for a moment, then shrugs."
    show Damien Neutral at left
    D "I don't know. I guess I've felt pretty guilty since that dog got put down. I want to help animals, not hurt them."
    show chelsea sad
    pcname "That wasn't your fault, though."
    D "It wasn't the dog's either."
    show chelsea blank
    D "It's fine. I really enjoy working with different kinds of animals. Sometimes I volunteer at the animal shelter and help find homes for the pets there."
    show chelsea shocked
    pcname "Really? Wow. That's so... nice."
    show Damien Happy at left
    show chelsea blank
    D "You think so? I don't know. It just makes me feel good, to help other people, I mean."
    "He looks down at his food shyly, taking small bites. You watch him, your heart swelled with admiration."
    pcname "{i}He really is such a selfless person...{/i}"
    show chelsea happy
    pcname "Maybe I could help you volunteer sometime. I've never been to a pet shelter."
    show Damien Shocked at left
    D "Really? You'd do that?"
    show Damien Laugh at left
    D "That would be awesome, [pcname]! I'll let you know the next time I'm going and we can both volunteer together."
    show chelsea laugh
    pcname "I'd like that a lot."
    show Damien Happy at left
    show chelsea happy
    "You both share another grin before finishing up your meals."
    "You spend a little more time in the mall together afterward, trying on funny hats and exploring unique shops that are tucked into the back corners of the building."
    "Damien escorts you back to your apartment afterwards, determined to hold your hand for as long as he can get away with."
    "Once you reach your apartment, he plants a kiss on your cheek before making his way home."
    $ acts -= 1
    hide Damien Happy with dissolve
    hide chelsea with dissolve
    $ damienmall=False
    jump events_end_period

label damien_clubvisit_track:
    show bg CityD with dissolve
    $ clothes, hair = casualwear
    show chelsea at right with moveinright
    "The air is crisp and a little windy as you make your way to school, an indication that the autumn season is finally rolling in."
    "The cold air really helps wake you up. By the time you reach the track field, you feel pumped and ready to go!"
    hide chelsea with dissolve
    show bg black with dissolve
    pause 0.5
    $ clothes = 'track'
    show bg TrackD with dissolve
    show chelsea at right with moveinright
    "Coach starts you off with your usual stretches. You join your other teammates in spreading out across the field to warm up."
    "Coach" "Alright, ladies, line up! Warm-up laps, then sprints!"
    "A few people groan, but everyone gets up from the field and start to line up along the track."
    "You keep a steady pace as you complete your warm-up laps, the cool air feeling good against your skin."
    "You find it's easier to run than before. You're barely tired when you finish the laps."
    "All of this practice really pays off!"
    "Coach blows his whistle once everyone's finished with their laps."
    "Coach" "Alright, let's get that blood pumping!"
    "Coach" "Back in position, first of fifteen!"
    show chelsea shocked
    "As you approach the starting line, you notice Damien sitting on the bleachers. He gives you an encouraging smile and waves."
    show chelsea happy
    "You grin and wave back."
    show chelsea blank
    show August Confused at left with dissolve
    "August" "Aren't these supposed to be private practices?"
    "You're surprised to see August and a few other teammates staring up at him as well."
    "Ryan nudges her playfully."
    "Ryan" "You're just nervous you'll lose in front of an audience."
    show August Laugh at left
    "August gives him a sharp smile, all teeth and challenge."
    "August" "You wish."
    "The whistle blows and you take off."
    hide August Laugh with dissolve
    "August and Ryan soar ahead, neck-and-neck as they compete for first place."
    "You push yourself after them, struggling to keep up. While you may be further ahead than most of your other teammates, you're still a ways off from beating August or Ryan."
    "But with Damien watching, you can't help but feel an extra pressure to beat your teammates."
    "You try to push yourself harder than usual, hoping to catch up and surpass them."
    "In the end, though, you still come behind August and Ryan."
    "You bend over and grasp your knees for support, entirely out of breath. Perhaps you pushed yourself a little {i}too{/i} hard..."
    show chelsea confused
    "Coach" "Back in position! Two of fifteen!"
    show chelsea blank
    "You have to bite back a groan as you line up again. Even wanting to impress Damien, there's no way you can push yourself that hard again."
    "You finish the remaining sprints at a decent pace, settling on average among your teammates."
    "Even so, you're sweaty and out of breath."
    "Coach" "Good work today, team! Head home and get some rest!"
    "Your teammates bid their farewells, some leaving to clean up in the locker rooms while others head straight home."
    "You jog over to the bleachers and meet Damien by the stairs."
    show chelsea happy
    pcname "Hey! I wasn't expecting to see you here."
    $ DamienAngry = "Characters/Damien/Casual 2/Angry.png"
    $ DamienBlank = "Characters/Damien/Casual 2/Blank.png"
    $ DamienGlare = "Characters/Damien/Casual 2/Glaring.png"
    $ DamienLaugh = "Characters/Damien/Casual 2/Laughing.png"
    $ DamienNeutral = "Characters/Damien/Casual 2/Neutral.png"
    $ DamienSad = "Characters/Damien/Casual 2/Sad.png"
    $ DamienShocked = "Characters/Damien/Casual 2/Shocked.png"
    $ DamienSmiling = "Characters/Damien/Casual 2/Smiling.png"
    $ DamienWorrying = "Characters/Damien/Casual 2/Worrying.png"
    show Damien Happy at left with moveinleft
    D "Yeah. I thought I'd surprise you. I hope that's okay."
    pcname "Yeah! I'm really glad you came."
    if damienoutfitchange == False:
        show chelsea shocked
        "As you finally take a minute to look your boyfriend over, you're surprised- and utterly grateful- to see him in jeans and a denim jacket."
        "With his t-shirt and sneakers he actually looks... cool."
        show chelsea confused
        pcname "What happened to the cargo shorts?"
        show Damien Neutral at left
        D "Huh? Oh..."
        show Damien Happy at left
        D "I, uh, I thought I'd switch it up. Do you like it?"
        menu damien_newclothes:
            "I love it!" if True:
                show chelsea happy
                $ damienconfidence += 1
                show Damien Laugh at left
                pcname "You seriously look great, Damien. This was a great choice."
                "His face lights up, thrilled by your approval."
                show Damien Happy at left
                D "You think so? Awesome! I mean, cool. Yeah. Cool."
                show chelsea confused
                pcname "Does this mean I can torch your cargo shorts?"
                show Damien Laugh at left
                "Damien laughs nervously, his cheeks tinting pink with embarrassment."
                show Damien Neutral at left
                D "Ah, maybe not yet..."
            "You still look like a dork." if True:
                show chelsea happy
                $ damienconfidence -= 1
                "Even though you know his new outfit is pretty stylish, you can't outright {i}tell{/i} him that."
                "Not when you can tease him instead."
                "Grinning, you poke his cheek."
                show chelsea confused
                pcname "Are you kidding? You still look like a dork."
                show Damien Worry at left
                show chelsea happy
                pcname "But you're my dork, so I guess it's okay."
                "His cheeks pink with embarrassment. He looks down at his clothes, suddenly unsure."
                D "You think so? It's not that bad, is it?"
                show chelsea laugh
                pcname "Let's just say it {i}definitely{/i} fits you."
                show Damien Neutral
                show chelsea happy
                D "Ah, okay..."
                D "Well, um..."
    elif True:
        pass
    show Damien Happy at left
    D "You did really great out there, [pcname]. I suck at sports myself, so it was really impressive."
    show chelsea happy
    pcname "Thanks! I pushed myself a little too early today, but one day I'd like to beat out my teammates during the sprints!"
    show Damien Blank at left
    "Damien stares at you, thoroughly impressed by your ambition."
    show Damien Neutral at left
    D "That sounds like a lot of hard work... How do you do it?"
    show chelsea blank
    pcname "Mostly I just practice. I have to keep my body in shape, so I need to watch what I eat, do stretches, practice running..."
    show chelsea happy
    pcname "It's a lot of work to keep your body in shape for this kind of thing, so I have to keep up with it every day."
    show Damien Shocked at left
    D "Wow... That's crazy."
    show Damien Happy at left
    D "I don't even know where I'd begin with this sort of thing."
    pcname "Well, you know, you could always try running with me. I'd be happy to train you."
    pcname "It might be a lot of {i}long, hard{/i} hours at work, but I'm sure we could get you there."
    "You squeeze his bicep and wink."
    if damienconfidence >= 50:
        "He considers it for a moment, a nervous smile breaking out on his face."
        D "Ah, yeah. Maybe. I'm not that great at exercising, but if you try out some of these series I'm into, maybe I can try to exercise with you."
        D "You'll need to be patient with me, though. I'll probably slow you down for a while."
        show chelsea laugh
        pcname "I wouldn't mind. That's what the practice is for!"
    elif True:
        show Damien Worry at left
        "Damien's face flushes, biting down on his lip."
        D "Oh, um, I don't... I don't know about that..."
        D "I'm not good at running at all. I would just hold you back, honestly..."
        show chelsea laugh
        pcname "Sounds like you just need a little push!"
        show Damien Happy at left
        "You shove his arm lightly for emphasis. Damien gives you a nervous smile, clutching onto the railing for support."
    show bg black with dissolve
    hide chelsea with dissolve
    hide Damien Happy with dissolve
    "You spend a few more minutes chatting together, discussing upcoming tests you need to prepare for and other weekend plans."
    "By the time you finish catching up, your teammates have already begun leaving for the day."
    show bg TrackD with dissolve
    show chelsea happy at right with dissolve
    pcname "Thanks for coming out to watch me practice, Damien. It was a nice surprise."
    if damienconfidence >= 50:
        show Damien Laugh at left with dissolve
        "He smiles, casually leaning himself against the railing. He reaches out to tuck a piece of hair behind your ear."
        D "It was nothing. Maybe I'll stop by again sometime."
    elif True:
        show Damien Happy at left with dissolve
        "He smiles nervously, both pleased and embarrassed by your comment."
        D "Ah, it- it was nothing. I just really wanted to see you..."
    show Damien Happy at left
    D "Do you want me to walk you home? I'm heading over that way anyways."
    if corruption >= 20:
        menu choice387:
            "Take him to the locker rooms." if True:
                show chelsea blank
                "You consider saying yes, but standing here beside your boyfriend, you're suddenly aware of the sticky sheen of sweat over your body. You probably smell terrible..."
                pcname "Sure. I just need to shower first. I feel pretty gross."
                pcname "Do you mind coming to the locker rooms with me?"
                if damienconfidence >= 50:
                    show Damien Shocked at left
                    "Damien raises his eyebrows in surprise."
                    show Damien Neutral at left
                    D "Oh. Yeah, I guess I can come with you. But what about the other girls...?"
                elif True:
                    show Damien Shocked at left
                    "A blush spreads across Damien's face. He stares at you, surprised by your suggestion."
                    show Damien Worry at left
                    D "Come with you to... to the {i}girl's{/i} locker rooms? Ah, I don't know if that's such a good idea..."
                menu damien_lockerroom2:
                    "Tease him." if True:
                        $ corruption += 1
                        $ damienconfidence -= 1
                        show chelsea happy
                        pcname "Oh come on. You don't want an orgy?"
                        show Damien Shocked at left
                        D "An- A {i}what?{/i}"
                        show chelsea blank
                        pcname "Don't act dumb. All guys are perverts, you included."
                        show chelsea happy
                        pcname "I bet you'd love to see us all naked. What a nasty pervert you are, Damien..."
                        show Damien Sad at left
                        "His face floods red, stretching to the tips of his ears. He quickly shakes his head."
                        show Damien Worry at left
                        D "N-No! It isn't like that at all!"
                        show chelsea laugh
                        pcname "It's {i}not?{/i} I doubt that."
                        show chelsea happy
                        pcname "Too bad for you, the locker rooms are empty now, so it would just be us."
                        pcname "I know that's not exciting as the {i}entire track team{/i}, but you better not keep me waiting, Damien."
                    "Reassure him." if True:
                        $ corruption -= 1
                        $ damienconfidence += 1
                        show chelsea blank
                        pcname "It's fine. They'll all be gone by now. I just want to hang out a little longer."
                        show Damien Happy at left
                        D "I... Yeah, I guess that's okay then."
                        show chelsea happy
                        pcname "Great!"
                show bg black with dissolve
                hide chelsea with dissolve
                hide Damien Happy with dissolve
                hide Damien Worry with dissolve
                "You turn on your heel and walk back to the school, Damien in tow."
                "As you predicted, the locker rooms are abandoned by the time you get there. Damien peers around cautiously, although you can sense his curiosity as he takes in the room."
                show bg Lockeroom with dissolve
                "You open your locker and remove a set of clean clothes and showering essentials."
                show chelsea happy at right with moveinright
                pcname "What do you think?"
                "Damien peeks around the locker room a little longer, his curiosity getting the better of him."
                "When he's finished observing, he sounds almost disappointed."
                show Damien Neutral at left with dissolve
                D "It's just like the boys'. I thought there would be more differences."
                D "I guess the showers have curtains on them, but that's pretty much it..."
                show Damien Blank at left
                show chelsea confused
                pcname "Really? I thought you boys would've trashed yours by now."
                show Damien Happy at left
                show chelsea blank
                D "Ah, well, some do, but it's relatively clean..."
                show Damien Blank at left
                "You lift your shirt over your head and toss the fabric onto a nearby bench. Damien stops in his tracks, his gaze locked onto your body."
                show Damien Shocked at left
                if damienconfidence <= 50:
                    "Realizing what he's doing, Damien shoves his hands over his face, averting his gaze to the ceiling tiles."
                    D "W-What are you doing?"
                elif True:
                    D "Ah, [pcname]...?"
                show chelsea confused
                pcname "What? This is the {i}girl's{/i} locker room. I can't shower in my clothes."
                "Kicking your shoes off, you reach down, sliding out of your track shorts. You drop them onto the dirty pile of clothes on the bench."
                $ clothes = 'underwear'
                show chelsea blank
                show Damien Worry at left
                if damienconfidence >= 50:
                    "Despite the blush on his cheeks, Damien continues to stare at your body, unable to look away. His gaze roves over your hips and the soft curves of your breasts in your bra."
                    D "Ah, sorry, do you want me to go...?"
                elif True:
                    "Despite himself, you notice Damien taking glances in your direction, his face heating up with each look."
                    D "I-I should go-"
                menu damien_showerbj:
                    "Ask him to join you." if True:
                        $ corruption += 3
                        show chelsea happy
                        pcname "No. I don't want you to leave."
                        "Feeling confident, you unclasp your bra and let it fall to the floor."
                        "You peel off your panties, tempted to fling them at him. Instead you drop them onto the pile and walk forward."
                        hide chelsea with dissolve
                        pause 1.0
                        $ clothes = 'naked'
                        show chelsea happy at right with dissolve
                        "Damien tenses as you run your hands up his chest and start to remove his jacket."
                        pcname "Come take a shower with me."
                        if damienconfidence >= 50:
                            show Damien Shocked at left
                            D "You want me to..."
                            show Damien Happy at left
                            "It takes a moment for your suggestion to click in his mind, but once it's there, you can see the desire flood his eyes."
                            "Picking up on your suggestion, Damien hesitantly lifts his shirt over his head and tosses it to the floor. You run your nails across his bare skin, savoring the shudder he makes."
                            "Encircling you in his arms, Damien presses a hard kiss to your lips. You eagerly return it, your fingers already fumbling with his belt."
                            hide chelsea with dissolve
                            hide Damien Happy with dissolve
                            show bg DTS2 with dissolve
                            "He reaches one hand down, easily unclasping the buckle and unzipping his pants. His lips never leave yours, desperate for the feel of you against him."
                            "You press your hand into his boxer briefs and pull him out, one hand pumping his erection while the other tangles into his hair."
                            D "Ohh... [pcname]..."
                            "He grinds into your palm, grunting as you play with his hard cock."
                            "Your lips part for just a moment, enough for you to get some air into your lungs."
                            pcname "The... The shower..."
                            "Damien lets out a breathy laugh, tickling the skin of your neck."
                            D "Right. The shower..."
                            "You begin to pull away, but Damien keeps a tight grip on your hand. He whirls you back against him, pressing a hard kiss against your lips."
                            "It's a fun game as you try to make your way to one of the empty shower stalls. Damien continues to pull you back against him on the way there, his lips meeting your neck, your shoulders, anywhere they can touch."
                            "He strips out of his clothes along the way, tripping over jeans and sneakers until he's pressed flush against your body, pinning you against the tile wall of the shower."
                            "Between harsh kisses on your neck, you somehow manage to turn the water on."
                            "Damien yelps and jumps as the freezing water hits his back. You laugh, quickly trying to adjust the temperature."
                            "He's back on you in an instant, cupping your face, your breasts, your ass, anywhere that you'll let his hands roam across your body. His touch is gentle but desperate, eager to feel every inch of your skin."
                            "You run your hands down his chest, your lips following. Damien sucks in a sharp breath as you kiss down to his groin, your tongue sending a firm stroke against his tip."
                            D "[pcname]..."
                            "His fingers carefully entwine with your hair, thumbs stroking the back of your skull as you lick along his tip."
                            "You squint a little as the water of the shower begins to smack into your face. Noticing this, Damien turns, taking most of it against his back."
                            D "Ah, is that better...?"
                            "You nod, licking the underside of his cock as thanks. He shudders against you, his erection bobbing in your direction."
                            "You lean forward and take his tip between your lips, tongue stroking its underside. Damien bites down hard on his lip, trying to avoid the moan bubbling in his throat."
                            "You lick and stroke his tip, teasing him until you feel his fingers press against your skull, urging you forward."
                            "You happily oblige, taking more of him into your mouth. He gasps as his tip smacks against the side of your cheek."
                            D "Hah... [pcname]... You're so freaking hot..."
                            "You hum happily at his words, the noise reverberating around his cock. He jerks his hips forward on instinct, desperate to feel more."
                            D "Ah! Sorry, I didn't mean- {i}Mmmm....{/i}"
                            "His words quiet down as you begin to slide him down your throat. His fingers massage into your scalp as he bucks his hips against your mouth."
                            D "Hah... Hah... Is this... okay?"
                            "He thrusts into your throat once, testing your endurance. You bob your head happily around his cock, encouraging him."
                            "Relieved, Damien's grip on your hair tightens. He shoves himself as far down your throat as his cock will go."
                            "You moan around his erection, the vibrations pleasuring him almost as much as your throat."
                            "Gripping your head, he gently fucks your skull, making sure to check your reactions in case he pushes too far."
                            "When he sees that it isn't hurting you, he lets out a moan, his hips bucking more harshly against your face."
                            "As Damien becomes more confident in his movements, you feel desire swell in your belly, begging for release."
                            "You reach down and press your fingers against your clit, toying the stiff nub as Damien drives himself into your throat."
                            D "Oh... Oh, yes, [pcname], keep playing with yourself..."
                            D "You look so fucking hot like this... Just keep touching yourself...!"
                            "You're not sure you've ever heard Damien swear, but the desperation in his voice nearly sends you over the edge. You grind eagerly against your fingers, allowing Damien to take control of fucking your skull."
                            "His breath hitches as he comes close to his climax. You feel his balls smack against your chin, eager for release."
                            D "[pcname], I'm... I'm gonna..."
                            D "Hah... Ah!"
                            "His cock twitches in your throat, emptying his load inside of your throat."
                            "You swallow his cum and let out a moan as you reach your own climax, bucking against your fingers eagerly as your fluids drip onto the tile floor."
                            "Damien grips your hair, keeping it in place until he's finished and out of breath."
                            "He gasps for air, gently sliding his cock out of your mouth. You can taste the saltiness of his cum on his tip as he drags it out of you."
                            D "A-Ah... [pcname]... Hah, sorry about that."
                            "He gives you an apologetic smile, although you don't think he's particularly sorry."
                            D "You came, too?"
                            "You pull your sticky fingers away from your clit and wash them under the showerhead."
                            pcname "Mhm."
                            D "That's good."
                            D "Maybe leave it for me next time. I'll take care of you."
                            "His fingers gently brush back the tangles in your hair. You grin, a new excitement forming in your belly."
                            pcname "I look forward to it."
                            "You rise to your feet, already eager for next time."
                        elif True:
                            show Damien Shocked at left
                            D "I- What-"
                            "You don't wait for him to catch up to your intentions. You push his jacket off of his shoulders and capture his mouth in a kiss."
                            "He freezes, his eyes wide as you slip your hands under his shirt and peel it from his chest. His breath catches as your nails stroke along the bare skin."
                            D "[pcname]... I-I..."
                            pcname "Shh."
                            "You press a finger to his lips, effectively silencing him."
                            pcname "Kiss me."
                            hide Damien Shocked with dissolve
                            hide chelsea with dissolve
                            show bg DTS1 with dissolve
                            "Damien blinks, understanding crossing his features. Face beet red, he shakily presses his lips to yours. It's clear he doesn't really know what to do."
                            "Taking charge of the situation, you press him against the lockers and fumble with his belt buckle. He lets out a little noise of surprise but doesn't object."
                            "His hands hover over you, unsure where to touch. You can't help but feel excited by his trepidation."
                            "You pull his erection from his boxer briefs and stroke the sensitive skin, desire swelling in your belly as he squirms eagerly against your touch."
                            pcname "Does that feel good, Damien?"
                            "Too embarrassed to speak, he bites down on his lip and nods."
                            "You press your lips against his, forcing your tongue into his mouth as you toy with the tip of his cock. Damien opens his mouth to accept you, his hips bucking lightly in your direction."
                            pcname "That's better. You aren't completely hopeless."
                            pcname "Now get in the shower."
                            "You let go of him suddenly. He trembles in your wake, bare-chested and cock out. He stares at you, entirely unsure."
                            pcname "What? Do you need me to strip you, too? You aren't incompetent, Damien. Don't make me do all the work."
                            "He jolts at your words. He bends over and shakily removes the rest of his clothes, leaving them in a heap on the floor."
                            "Once he's naked and exposed, you take a moment to appraise his body, scrutinizing every detail. He shifts uncomfortably under your gaze, barely resisting the urge to cover himself."
                            pcname "You really don't work out that much, do you?"
                            "You squeeze his scrawny bicep, then run a long nail down his chest. Damien shudders under your touch, desire and anxiety mixed in his eyes."
                            pcname "You'll have to really impress me, boyfriend. Now get in the shower."
                            "You slap his ass, startling him. Damien scrambles into one of the empty stalls."
                            "You follow behind him and, standing away from the showerhead, turn on the water. He yelps as the freezing water hits his back, quickly pressing himself against a tile wall. You laugh, readjusting the water to a more comfortable temperature."
                            pcname "Come over here."
                            "Damien presses a hand in the water, checking the temperature before hesitantly stepping into the center of the shower. He watches you warily, waiting for your next move."
                            "You step forward and tangle your fingers in his hair, yanking his head down to kiss you. He struggles to keep up, his hands still afraid to touch you."
                            "Not breaking the kiss, you grab his hands and force them on your ass. He elicits a small gasp but doesn't pull away, his hands planted firmly on the curve of your ass."
                            "Carefully, so carefully you barely notice it, he gives a small squeeze. He relaxes slightly as you kiss him, his hands roaming shakily up your back and against the back of your thighs."
                            "You grind against his erection as his fingers brush the underside of your breast."
                            D "Is this... is this okay...?"
                            pcname "{i}Yes.{/i}"
                            "He nods to himself and gently caresses your breasts. His touch is soft, almost feather-light, against your skin. You press into him more, forcing him to touch you."
                            pcname "Are you scared, Damien?"
                            D "I..."
                            "He looks away. It's all the answer you need."
                            "You cup his face and force him to look at you."
                            pcname "Don't be."
                            "You gently bite his lower lip, enjoying the sharp intake of breath he takes, and continue to nip down his neck and chest. He trembles underneath you, excited and uncertain as you kiss and bite down his chest to his thighs."
                            "You settle on your knees between his legs, adjusting yourself to avoid the showerhead splashing you in the face. Damien gnaws on his lower lip, his hands pressed against your shoulders lightly."
                            "You lean forward and trace a long lick on the underside of his dick. Damien gasps. His erection bobs happily in response."
                            pcname "Mmm. What a little pervert..."
                            "Damien opens his mouth to protest but his words are lost as you take his tip into his mouth."
                            D "Ohh... [pcname]..."
                            "His grip on your shoulders tighten ever so slightly, encouraging you forward."
                            "You smirk, your tongue pressing and lapping against the slit and curve of his tip, sucking on the sensitive skin."
                            "Damien whimpers above you, unable to control the little jerk of his hips every time you do something a little too pleasurable."
                            "He lets out a gasp as you dig your nails into his hips and urge him forward, taking more of his cock into your mouth."
                            D "[pcname]...!"
                            "Grinning, you push and pull at his hips, forcing him to thrust gently into your mouth. Once he's picked up the rhythm, you let go, using a free hand to pump his base while your mouth works around the rest of his cock."
                            D "[pcname]... [pcname]... P-Please... Please..."
                            pcname "Please what, Damien?"
                            D "Please... keep going..."
                            "He's too embarrassed to look you in the eye as he makes his request, focusing instead on a shower tile as the water beats against his back. He grips your shoulders, begging silently, as he struggles to catch his breath."
                            pcname "Well, since you asked so nicely..."
                            "Without warning, you yank him hard against you, taking the entirety of his cock down your throat."
                            "Damien cries out in surprise, throwing his head back."
                            "Although he doesn't say it, you can tell by the pressure of his fingers on your shoulders and the way he struggles to hide his embarrassed smile that this is exactly what he wanted."
                            "You bob your head eagerly against his cock, taking him as deeply as your throat will allow. Damien bites into his lip, struggling to contain his moans."
                            "You feel the desire in your belly swell and ache, begging for release. Pressing two fingers against your clit, you circle the stiff nub, moving in rhythm with Damien's thrusts."
                            D "Hah... Hah... [pcname], are you...?"
                            "He stares down at you, his erection throbbing eagerly at the sight of you masturbating."
                            "You grind against your fingers, struggling to keep up with both pleasuring Damien and yourself. You moan around his cock, tears pricking your eyes as you feel your climax coming."
                            D "Oh... Oh {i}fuck...!{/i}"
                            "The vibrations of your moans send him over the edge. Damien lets out a small cry, his cock twitching as he empties his load down your throat."
                            "You swallow his cum, your hips bucking hard against your hand as your own release takes you."
                            "Damien quickly pulls out of your mouth, leaving only the salty taste of his cum on your tongue."
                            D "I-I'm so sorry! I didn't mean- I wasn't going to-"
                            "You press a hard kiss to his cock, silencing him."
                            pcname "It's fine. I like the taste of you."
                            "You give him a smirk, enjoying the embarrassed face he makes as you rise to your feet."
                        "You and Damien shower together peacefully, your conversations trailing off to school, upcoming events, and other things going on around town."
                        "When you're finished, you head back to the locker rooms to get changed."
                        "After you're all clean and set to go, Damien walks you home."
                        "Before you reach your apartment, Damien gives your hand a squeeze, capturing your attention."
                        D "You know, the homecoming dance is coming up. If you plan on going, well, maybe we could go together?"
                        "You open your mouth to reply, but Damien quickly shakes his head."
                        D "Ah, I don't need an answer now. Just think on it, if you can..."
                        "He bids you farewell with a kiss on the cheek when you reach your apartment."
                        "Between your practice at track and the blowjob in the shower, you can't help but feel energized for the rest of the day!"
                        $ damienclubbj = True
                        jump events_end_period
                    "Ask him to stand outside." if True:
                        $ corruption -= 3
                        show chelsea confused
                        pcname "Why would you leave? I asked you to hang out with me."
                        if damienlingeriepictures == True:
                            show chelsea happy
                            pcname "I {i}know{/i} you've seen me in my underwear before."
                        elif True:
                            pcname "Don't tell me you've never seen a girl in her underwear before."
                        if damienconfidence >= 50:
                            show Damien Worry at left
                            D "Ah... Well, I've never seen it in person..."
                        elif True:
                            show Damien Worry at left
                            "Damien looks away, struggling to meet your gaze. The embarrassed look on his face is all the answer you need."
                        show chelsea blank
                        pcname "I'm just going to shower really quick. Wait for me outside. We can talk in the meantime."
                        D "I... Okay. If that's what you want."
                        pcname "It is."
                        show bg black with dissolve
                        hide chelsea with dissolve
                        hide Damien Worry with dissolve
                        "You head to the showers, leaving no room for argument as you step inside and strip the rest of your underwear off, reaching a hand out to set it in a pile outside."
                        "You turn the faucet on and adjust the temperature to something comfortable before stepping into the water. It feels nice and cleansing against your sweaty body."
                        "You hear Damien shift uncomfortably just outside of the curtain."
                        if damienconfidence >= 50:
                            D "You know, if someone comes in here, I'm not sure what I'd do."
                            D "I guess I'd have to jump in there with you."
                            show chelsea happy at right with dissolve
                            pcname "Yeah? Huh. I guess you would."
                            show chelsea embarrassed
                            pcname "I'm not complaining."
                        elif True:
                            D "W-What if someone comes in here?"
                            show chelsea happy at right with dissolve
                            pcname "Then I guess you'd have to jump in here with me."
                            D "I-I... But..."
                            "He trails off, but you can imagine the blush on his face as he takes in your suggestion."
                            show chelsea blank
                        "There's a moment of silence as you carefully wash and rinse your hair, scrubbing away all of the grime from working out this morning."
                        menu damien_showertalk:
                            "Pretend someone's entering the locker room." if True:
                                $ corruption += 1
                                $ damienconfidence -= 1
                                show chelsea happy
                                "Bored of the silence, a mischievous thought enters your mind. Biting back a smirk, you feign curiosity as much as you can muster."
                                show chelsea confused
                                pcname "Did you hear that?"
                                "There's a slight pause as Damien tries to pick up on what you allegedly heard."
                                D "Hear what?"
                                show chelsea blank
                                pcname "I thought I heard the locker room door open."
                                "There's another moment of silence as Damien tenses outside, trying to listen. His voice drops to a whisper."
                                D "I don't hear anything."
                                show chelsea confused
                                pcname "Are you sure? I really thought I heard it."
                                show chelsea happy
                                pcname "Do you want to go check for me?"
                                D "Ah, I really shouldn't... I'm not supposed to be in here..."
                                pcname "Oh, {i}right.{/i} Huh. Well, let's hope no one came in here. They might see you and tell the whole school you're a pervert..."
                                D "But- But that isn't true!"
                                pcname "Well {i}I{/i} know that and {i}you{/i} know that, but would {i}she{/i} know that? I don't think so..."
                                D "..."
                                D "What... should I do? I can hide in one of the other showers..."
                                pcname "And risk her getting naked and opening that curtain to find you there? That would look even worse!"
                                show chelsea laugh
                                "You try to resist giggling as Damien shifts his weight uncomfortably outside, trying to listen for anymore noise."
                                D "I really don't think anyone is in here, [pcname]..."
                                show chelsea confused
                                pcname "Are you going to risk that?"
                                D "I..."
                                D "No..."
                                "Carefully, Damien moves the curtain aside and slips in beside you. The shower splashes water onto his clothes, dampening them."
                                "You let out a squeal and cover yourself, feigning modesty."
                                show chelsea shocked
                                pcname "Ah! Help, this {i}pervert{/i} just jumped in my shower!"
                                "Damien's face tinges bright pink, mortified by your response. He shakes his head, nearly tripping out of the shower."
                                show Damien Shocked at left with dissolve
                                D "I'm not! I'm not!"
                                show chelsea laugh
                                "You burst into laughter, watching him stumble to get through the curtain."
                                pcname "I can't believe you actually jumped in here! There's no one else in here. Obviously."
                                pcname "You're such a {i}pervert{/i}, Damien. Haha!"
                                show Damien Sad at left
                                D "I... You tricked me...!"
                                show chelsea confused
                                pcname "Yeah, what are you going to do about it?"
                                show chelsea blank
                                "There's no response from the other side. You peek your head out, amused to find Damien pouting on the bench."
                                pcname "You can't be {i}that{/i} upset. You got to see me naked."
                                D "I don't know if that's how I wanted to go about seeing that..."
                                show chelsea confused
                                "You raise a challenging eyebrow, a sharp smile curling on your lips."
                                pcname "How would {i}you{/i} have done it?"
                                D "I-I don't know."
                                show chelsea laugh
                                pcname "Haha! You're so funny, Damien."
                                hide Damien Sad with dissolve
                                hide chelsea with dissolve
                                "You pop your head back behind the curtain and continue your shower."
                            "Ask About {i}Liberation of Andromeda{/i}" if True:
                                $ corruption -= 5
                                $ damienconfidence += 1
                                show chelsea confused
                                pcname "Hey, so tell me more about that series you're into. Legion... Liberty... The robot one?"
                                D "'{i}Liberation of Andromeda?{/i}'"
                                show chelsea blank
                                pcname "Yeah, that one."
                                D "What do you want to know?"
                                "You shrug, although he can't see it, and begin lathering your body with soap."
                                show chelsea confused
                                pcname "I don't know. Just tell me about it. You really love it, so I'd like to hear about it."
                                show chelsea happy
                                D "Do you want to hear some theories about it?"
                                pcname "Ah... maybe not. You should just go over the plot."
                                show chelsea blank
                                "You can hear his voice perk up as he speaks, the excitement coming through clearly."
                                D "Well, it starts with humanity being nearly wiped out by climate change disasters. Floods, fires, stuff like that."
                                D "A bunch of rich people end up fleeing to space and building their own society on the moon. Eventually they branch out to other planets and explore space and stuff."
                                D "Way in the future, when the story {i}actually{/i} starts, humanity is still chugging along, but they're still suffering from the disasters, so they build robot companions. The main character is one named Andromeda, because that's her model make."
                                D "They've made it so robots can incubate humans and birth them to help double the birthrate. Andromeda is one of those, and she's basically impregnated with a human baby."
                                D "But it turns out the baby is the result of an affair between the governor and the queen of another space court, and the governor's wife finds out and wants the baby dead."
                                D "At this point robots don't really have sentience, but Andromeda manages to gain it- it's complicated, but the comic explains it really well- and she becomes super protective of this baby that isn't even hers."
                                D "So the story basically follows this robot as she tries to birth and raise this child and protect it from this woman that's desperately trying to kill it."
                                D "...Sorry, I just realized I might've spoiled the comic for you."
                                show chelsea happy
                                pcname "That's fine, I don't mind."
                                pcname "It sounds like it's a really good read. And it must be popular, too, if it's getting turned into a TV show."
                                pcname "Maybe we can watch it together when it airs."
                                D "Really? You'd be up for it?"
                                pcname "Yeah, I think that would be fun."
                                D "Awesome! It should air in a few months. I'll remind you so we can make a date out of it!"
                                pcname "Cool!"
                                hide chelsea with dissolve
                        show bg Lockeroom with dissolve
                        show chelsea at right with dissolve
                        "When you're done showering, you pull your underwear back on behind the curtain and step out to get changed."
                        show Damien Worry at left with dissolve
                        "Damien struggles not to stare at your freshly cleaned body as you pull on the rest of your clothes and get ready to leave."
                        show bg black with dissolve
                        "Once you're finished, Damien walks you home, seemingly lost in thought."
                        "Before you reach your apartment, Damien gives your hand a squeeze, capturing your attention."
                        show bg CityD with dissolve
                        show Damien Happy at left with dissolve
                        show chelsea at right with dissolve
                        D "You know, the homecoming dance is coming up. If you plan on going, well, maybe we could go together?"
                        "You open your mouth to reply, but Damien quickly shakes his head."
                        show Damien Worry at left
                        D "Ah, I don't need an answer now. Just think on it, if you can..."
                        "He stops outside of your apartment, planting a small kiss on your cheek before he heads out to run some errands."
                        "Between practice and hanging out with Damien in the locker room, you can't help but feel energized for the rest of the day!"
                        jump events_end_period
            "Go home now." if True:
                pass
    elif True:
        show chelsea happy
        pcname "Yeah, that sounds great. Let me just grab my stuff and we can go."
        show Damien Happy at left
        D "Okay."
        show bg black with dissolve
        pause 1.0
        show bg CityD with dissolve
        "After you change into your normal attire and grab your stuff from the locker room, you meet Damien back outside at the track field."
        "Before you reach your apartment, Damien gives your hand a squeeze, capturing your attention."
        show Damien Happy at left with dissolve
        show chelsea blank at right with dissolve
        D "You know, the homecoming dance is coming up. If you plan on going, well, maybe we could go together?"
        "You open your mouth to reply, but Damien quickly shakes his head."
        show Damien Worry at left
        D "Ah, I don't need an answer now. Just think on it, if you can..."
        "He finishes walking you home, planting a small kiss on your cheek when you reach your apartment before heading out to run some errands."
        "Between practice and seeing Damien at club, you can't help but feel energized for the rest of the day!"
        jump events_end_period
jump events_end_period

label damien_clubvisit_cheer:
    show bg CityE with dissolve
    $ clothes, hair = casualwear
    show chelsea at right with moveinright
    "The air is crisp and a little windy as you make your way to school, an indication that the autumn season is finally rolling in."
    "You feel a little more awake as you head to practice, the idea of your skirt flowing in the wind putting you in a good mood."
    "Fall is always the best season for cheerleading!"
    $ clothes = 'cheer'
    show bg Cheerlocker with dissolve
    "You join in the excited chatting of the other girls as you get changed in the locker room. Everyone seems a little eager for the change of the seasons!"
    show chelsea happy at right with moveinright
    "Once everyone's dressed, you join the other girls into the gymnasium. Ms. Vicky claps her hands, gesturing you all forward."
    show bg Gym with dissolve
    show MV Smile at left with moveinleft
    "Ms. Vicky" "Alright girls! Today we're going to start on a new routine for half-time."
    "Ms. Vicky" "Pay close attention what Tracy shows you and try to keep up!"
    "Ms. Vicky picks up her phone and takes a moment to synch up to the speakers."
    show Tracy Blank with dissolve
    "Once she's set up, Tracy moves to the front, her back facing you. She taps her foot to the music as a pop song blares over the speakers."
    "Tracy" "One, two, three, four!"
    "Tracy runs through the movements a few times on her own, slowing down at more complicated steps so you get a clear idea of what you're doing."
    "You try to pay attention to the moves, but she runs through them so fast that you miss half the steps."
    show Tracy Smile
    "Tracy turns toward you all too soon, prepared to have you run through it."
    "Tracy" "Okay, girls! Let's see it! One, two, three-"
    "On 'four', the gym doors open, catching you all off guard."
    show chelsea blank
    "Damien creeps into the room, halting abruptly when he realizes all eyes are on him. Ms. Vicky pauses the music."
    show MV Worried at left
    "Ms. Vicky" "Can we help you?"
    "Although she says it politely, you can tell Ms. Vicky is unhappy with the interruption. Tracy doesn't bother to hide her irritation."
    show Tracy Angry
    "Tracy" "This is a private practice!"
    show MV Blank at left
    $ DamienAngry = "Characters/Damien/Casual 2/Angry.png"
    $ DamienBlank = "Characters/Damien/Casual 2/Blank.png"
    $ DamienGlare = "Characters/Damien/Casual 2/Glaring.png"
    $ DamienLaugh = "Characters/Damien/Casual 2/Laughing.png"
    $ DamienNeutral = "Characters/Damien/Casual 2/Neutral.png"
    $ DamienSad = "Characters/Damien/Casual 2/Sad.png"
    $ DamienShocked = "Characters/Damien/Casual 2/Shocked.png"
    $ DamienSmiling = "Characters/Damien/Casual 2/Smiling.png"
    $ DamienWorrying = "Characters/Damien/Casual 2/Worrying.png"
    show Damien Worry at midright with dissolve
    D "Ah, sorry, I just- Um- I meant to get here earlier."
    D "My girlfriend's on the team. I just came to support her..."
    show Damien Happy at midright
    show Tracy Blank
    "He gives you an awkward wave, just as embarrassed as you are by his interruption."
    menu damien_cheerinterruption:
        "Pretend not to know him." if True:
            $ corruption += 1
            $ damienconfidence -=1
            "As nice as it is to have your boyfriend visit you during practice, you feel mortified by your other teammate's reactions."
            "None of them seem impressed, or even believing, that this dork belongs to you."
            "You snort, brushing your ponytail over your shoulder."
            pcname "I don't know what he's talking about. I'm just trying to practice."
            show Damien Sad at midright
            "Damien's face falls, confused and hurt by your response."
            D "[pcname]?"
            pcname "Nope. Never heard of her."
            show chelsea confused
            pcname "I think you've got the wrong girl."
            "Damien stands there awkwardly, clearly at a loss for what to do. The other girls on the squad snicker around him."
            show chelsea blank
            show Damien Worry at midright
            D "I... I guess I'll leave then..."
            "Like a kicked puppy, Damien turns to leave."
            show chelsea happy
            show Damien Blank at midright
            pcname "Oh, don't look so sad. I'm just teasing."
            pcname "Do you really think I'm so heartless?"
            D "O-Oh. No, of course not..."
            show Tracy Question
            "Tracy" "{i}That's{/i} your boyfriend?"
            pcname "I guess you can call him that. He's more like a cute puppy that follows me around."
            "You blow a kiss to Damien. He gives you an awkward wave, struggling to smile amidst his discomfort."
            show Damien Worry at midright
            D "I-I was just going to sit in and watch... Is that okay...? I can go..."
            "Ms. Vicky gives you a look, seemingly torn on what to do with him."
            show MV Smile at left
            "Ms. Vicky" "As long as you aren't a distraction, I don't see why not."
            show Damien Happy at midright
            D "T-Thank you."
            show Damien Blank at midright
            "Ms. Vicky" "You girls better practice extra hard with an audience now!"
        "Flirt with him." if True:
            $ corruption -= 1
            $ damienconfidence += 1
            show chelsea happy
            pcname "Hey, babe."
            "You blow a kiss in his direction, much to the chagrin of some of your teammates."
            "You know they certainly didn't expect you to be dating... {i}him{/i}."
            "Trying to ignore the uncomfortable stares of your teammates, Damien grins and pretends to catch it."
            D "I was just going to sit in and watch. Is that okay...?"
            "Ms. Vicky gives you a look, clearly displeased with this turn of events."
            "Ms. Vicky" "As long as you aren't a distraction, it's fine. The minute my girls can't concentrate though, you have to leave."
            D "Okay. Got it."
    hide Damien Happy with dissolve
    hide Damien Blank with dissolve
    "Damien moves to a set of bleachers set up in the gym and takes a seat, trying to be as quiet and inconspicuous as possible."
    show Tracy Angry
    show chelsea blank
    "Tracy clicks her tongue, annoyed, and starts again."
    show Tracy Smile
    "Tracy" "{i}As I was saying.{/i} One, two, three, four-"
    "You all struggle to keep up with the pace of the music, fumbling over each other and missing timestamps. Tracy stops the music early."
    show Tracy Angry
    "Tracy" "Again! We're not leaving until this is {i}perfect!{/i}"
    "True to her word, practice runs longer than usual, forcing you to memorize the steps again and again until your legs feel more like jelly than bone."
    show Tracy Blank
    "By the end, every girl is panting, struggling to grasp a particular step that requires a lot of focus."
    show Olivia Tired at midright with moveinright
    "Olivia" "Tracy... Couldn't we just take a water break...?"
    show Tracy Angry
    "Tracy snaps her eyes to Olivia, infuriated by the suggestion."
    "Tracy" "You already had one. Or is it that you can't {i}concentrate?{/i}"
    "No one misses the dirty look she tosses Damien, clearly wishing he wasn't here to witness their failure."
    show Olivia Sad at midright
    "Olivia" "No, I can concentrate, I just-"
    "Tracy" "Then we keep going. Come on, ladies! From the top!"
    hide Olivia Sad with dissolve
    "Again and again, you dance as a unit through the new routine until it's all your body can do."
    "At first you try to give it all your effort if only to impress Damien, but by the end he's the last thing on your mind. All you can think is {i}move, move move.{/i}"
    "Once she's satisfied, Tracy turns off the music."
    show Tracy Smile
    "Tracy" "That's enough for today. I'll see you for practice tomorrow! Don't be late!"
    "Your teammates nod, mumbling a few things amongst themselves as they head to the locker rooms to get changed."
    show Tracy Question
    show chelsea confused
    "Tracy" "[pcname], can I have a word?"
    show chelsea blank
    hide MV Blank with dissolve
    "Dread coils in your stomach, but you follow Tracy to the other side of the gym, out of earshot."
    show Tracy Tired
    "Tracy" "I get wanting your boyfriend around, but if he's a distraction to the team, we can't have him sitting in on practice."
    show Tracy Angry
    "Tracy" "I mean, it's not like he even plays sports. He has no idea how these things operate."
    menu damien_cheerdefend:
        "Defend him." if True:
            $ corruption -= 1
            $ damienconfidence += 1
            show chelsea angry
            pcname "But he didn't distract anyone, Tracy. He just sat there peacefully while we practiced."
            "Tracy" "Then explain to me why we took two extra hours to practice today."
            pcname "Because you chose a really hard routine to learn? It was going to take hours to learn anyway."
            "Tracy" "We would've had an easier time learning it if your boyfriend hadn't interrupted us in the first place."
            show Tracy Blank
            "Tracy" "Just make sure he doesn't come to another practice, alright? I don't care what you do outside of club, but this is practice time, okay?"
            show chelsea blank
            pcname "Fine. I get it."
            "Tracy" "Good."
            "She pauses, then sighs."
            "Tracy" "I'm not trying to be hard on you. But cheerleading is a {i}lot{/i} of hard work. You need to be willing to put that in for the team's sake."
            "Tracy" "Any sort of distraction could seriously hurt the squad."
        "Agree with Tracy." if True:
            $ corruption += 1
            $ damienconfidence -= 1
            show Tracy Blank
            pcname "Yeah, I know. I had like, no idea he was even coming today."
            show chelsea happy
            pcname "I'll make sure to tell him not to come to practice again."
            show chelsea blank
            "Tracy" "Good. We really can't afford any distractions like that, especially when we're learning a new routine."
            "Tracy" "Something like that could seriously hurt the squad."
    hide Tracy Blank with moveoutright
    "Tracy gives another disgruntled glance toward Damien before making her way to the locker rooms to change."
    "With the rest of your team and Ms. Vicky gone, you approach Damien on the bleachers."
    pcname "Hey."
    show Damien Worry at left with dissolve
    D "Ah, hey..."
    if damienoutfitchange == False:
        "As you finally get a good look at your boyfriend, you're entirely taken aback by his new wardrobe."
        "The dreaded cargo shorts are gone- {i}thank God{/i}- and replaced with a pair of jeans and a matching denim jacket. He compliments the outfit with a white-shirt and matching sneakers."
        "Altogether he looks really, {i}really{/i} cool. You're not sure how you missed it until now."
        show chelsea happy
        pcname "Oh thank God, you finally ditched those cargo shorts."
        show Damien Laugh at left
        "Damien laughs nervously, glancing down at his new attire."
        D "Ah, yeah. I thought I needed a change..."
        show Damien Happy at left
        D "Do you like it?"
        menu damien_newclothescheer:
            "I love it!" if True:
                $ damienconfidence +=1
                "You take a moment to appraise his outfit, searching for anything wrong. But... you find nothing."
                "It looks {i}great.{/i}"
                show chelsea laugh
                show Damien Laugh at left
                pcname "I love it! God, Damien, you look so {i}cool.{/i}"
                show chelsea happy
                pcname "Even if you aren't an athlete, I know the girls on the squad were jealous. None of their boyfriends dress {i}this{/i} stylish."
                D "Ah, really? You think so?"
                "He grins, scratching the back of his head."
                show Damien Happy at left
                D "I'm really glad you like it..."
            "You still look like a dork." if True:
                $ damienconfidence -=1
                show chelsea blank
                pcname "I mean, {i}obviously{/i} anything is better than the cargo shorts. But..."
                pcname "You look like you walked straight out of the 80's. All you're missing is a mullet."
                "You ruffle his hair teasingly, messing it up. Damien frowns, quickly putting his hair back in place."
                pcname "By the way, don't get a mullet. Ever."
                show Damien Neutral at left
                D "Ah, don't worry, that's not on the table..."
        $ damienoutfitchange = True
    "Damien looks at you sheepishly, running a hand through his hair."
    show Damien Worry at left
    show chelsea blank
    D "Look, I'm really sorry if I got you in trouble. I didn't mean to."
    D "I just thought it would be nice to watch you practice... I wanted to support you."
    show Damien Shocked at left
    show chelsea happy
    pcname "Aww! That's so sweet."
    show Damien Happy at left
    pcname "It's fine. Tracy says you can't come to any more practices, though."
    show chelsea blank
    pcname "Which kind of sucks, because this practice wasn't even my best one. If you were going to come to one, I wish you'd made it to a better one."
    show Damien Laugh at left
    D "I don't think you did that bad!"
    show chelsea confused
    pcname "{i}That{/i} bad?"
    show Damien Shocked at left
    show chelsea blank
    "Damien's jaw drops a little, catching his mistake."
    show Damien Worry at left
    D "Ah, that's not what I meant..."
    show Damien Happy at left
    D "It looked like a really hard routine to learn. I don't even know where I'd begin to try it myself..."
    show Damien Neutral at left
    show chelsea happy
    D "Oh! But if there's anything I can do to help, let me know. I watched it a lot today, so maybe together we could figure it out."
    show Damien Happy at left
    menu damien_cheerpractice:
        "Take Damien up on his offer." if True:
            "A part of your brain finds the idea of Damien- poor, unathletic Damien- trying to perform the routine hysterical. Another part knows how desperately you need the practice, and who better than your boyfriend?"
            pcname "If you're not in a hurry, I could use some help going over the routine a couple more times."
            pcname "I just need someone to do it with me and help point out what I'm missing or messing up on."
            show Damien Shocked at left
            "Damien's face lights up, both surprised and happy that you decided to take him up on his offer to help."
            show Damien Happy at left
            D "Sure! Just tell me what to do."
            show chelsea blank
            "You lead Damien down to the center of the gymnasium and search for the song on your phone. It's not hooked up to the gym's sound system, so you have to put the volume all the way up to hear it."
            pcname "Okay. Do you know how to count beats?"
            show Damien Worry at left
            D "...No."
            pcname "Every beat goes one, two, three, four and repeats. It's important to keep up with the beats so you know when to time your movements."
            show Damien Blank at left
            "Damien looks at you skeptically, but nods, accepting your words as truth."
            show Damien Neutral at left
            D "Okay. I can... try."
            show Damien Blank at left
            "You press play on your phone and quickly get into position. Your body is already aching and begging to stop, but you don't want to feel left behind in the routine."
            "Damien stumbles beside you, not at all sure what he's supposed to be doing. When you move to leap into his arms, he panics and drops you onto the floor."
            show chelsea sad
            show Damien Shocked at left
            pcname "{i}Ow!{/i}"
            D "Oh no! I'm so, so sorry, [pcname]!"
            show Damien Worry at left
            "He crouches down beside you, worry lining his face."
            show Damien Neutral at left
            D "Are you okay?"
            show Damien Blank at left
            pcname "Ngh... Yeah..."
            show chelsea blank
            pcname "You were supposed to catch me, you know..."
            show Damien Worry at left
            D "I know. I'm so sorry. I panicked."
            show Damien Sad at left
            D "Maybe I shouldn't be helping with this..."
            "You sigh, resting your head back against the hard floor. It feels better than standing on your legs again right now."
            show chelsea happy
            pcname "It's okay. I should have warned you. When you said you watched the routine, I just assumed you knew what was coming. That's my bad."
            show Damien Blank at left
            show chelsea blank
            "Ignoring the ache of your body, you rise to your feet."
            show chelsea happy
            pcname "Let's try again."
            "You run through the routine a couple more times, instructing Damien on what he needs to do to help."
            "After a few more tries, you feel like you have a much better grasp on what you're doing!"
            "Damien, on the other hand, is out of breath and panting. It's obvious he's not used to this much physical activity, and he isn't even performing the whole dance..."
            pcname "Let's just run through it one more time, okay? And then we can stop."
            show Damien Happy at left
            "Damien gives you a thumbs up, too breathless for words. You turn the music on again and take your place."
            show chelsea blank
            "As the beat starts, an idea forms in your mind. It could be fun to tease Damien, especially after he dropped you on the floor..."
            menu damien_danceflirt:
                "Change the routine." if True:
                    $ corruption += 1
                    "As the dance starts, you vaguely keep up with the moves, swaying and moving your body in a way that shows off your body."
                    show Damien Blank at left
                    "Damien stops, confused. You dance around him, making sure to brush your breasts and ass against him."
                    if damienconfidence >= 50:
                        show Damien Happy at left
                        "He raises an eyebrow, biting back an amused smile."
                        D "What are you doing?"
                    elif True:
                        show Damien Worry at left
                        "His cheeks bloom a bright pink, eyes wide as he watches you rub against him."
                        D "W-What are you doing?"
                    show chelsea happy
                    pcname "I'm trying something new for the routine. Do you like it?"
                    D "I..."
                    "His gaze follows you as you move away, making sure to bend and strut your body into appealing poses."
                    if corruption >= 20:
                        pcname "I was just thinking... This would be a really good song to strip to. Don't you think?"
                        show Damien Shocked at left
                        "Keeping your eyes locked on his, you reach underneath your skirt and slowly pull your spanks down, kicking them across the gym."
                        if damienconfidence >= 50:
                            show Damien Happy at left
                            "Damien's eyebrows raise, but he doesn't object. He shoves his hands in his pockets and focuses on you, biting down on his lip."
                            D "Ah, you're going to do it right here...?"
                            pcname "Why not? We're alone."
                            "He thinks for a moment, glancing around the empty gym."
                            D "Yeah... I guess we are."
                        elif True:
                            "Damien's eyes go wide, his face coloring pink. He glances around the empty gym nervously, searching for wandering eyes."
                            D "What- What if someone comes in and sees?"
                            pcname "I guess you'll have to cover me up with your hands, then."
                            "You run your hands over the curve of your breasts for emphasis. Much to your pleasure, Damien squirms, not sure whether to stare at you or avert his gaze."
                        "You dance a little to the music, lifting your legs high enough to give him a good view of your panties."
                        "Taking the edge of your shirt, you lift it over your head and drop it to the ground. Damien's eyes trail to your breasts, desire flooding his eyes."
                        "You strut toward him, your hips swaying delightfully until your bra is inches from his chest."
                        show bg DCS1 with dissolve
                        hide Damien Happy with dissolve
                        hide Damien Worry with dissolve
                        hide chelsea with dissolve
                        if damienconfidence >= 50:
                            "Damien eyes your breasts hesitantly, his face caught in an internal struggle."
                            pcname "You can touch them if you want, you know. You {i}are{/i} my boyfriend."
                            "That seems to do the trick. Encouraged by your words, Damien hesitantly reaches up and gropes your breasts, squeezing them gently between his hands."
                            "You bite your lip, enjoying the sensation of his hands on you. Losing his shyness, Damien continues to massage your breasts, slipping his hands under your bra to stroke the skin there."
                            "You reach back and unclasp your bra, allowing it to drop to the floor."
                            "Damien's movements are less hesitant now but still just as gentle as he runs his thumbs over your nipples and cups the weight of your breasts into his palms."
                            "You press yourself into him, encouraging him to keep touching you as you slip out of your skirt and panties, kicking your shoes off."
                            "He stares down at you with half-lidded eyes, taking in the full exposure of your naked body pressed against his."
                            "Damien leans forward and captures your mouth with his. His kissing is inexperienced but urgent, his tongue desperately tracing the caverns of your mouth."
                            "Gripping his jacket, you pull him back behind the bleachers, small moans and gasps eliciting from your throat as Damien clutches you against his body, kissing you hard."
                            show bg DCS2 with dissolve
                            "His hands roam your body freely as you shove his jacket off and toss his shirt onto the floor. You kiss down his neck and chest eagerly, your tongue lapping against the sensitive skin of his nipples."
                            show bg DCS3 with dissolve
                            "You continue down until you're on your knees, fumbling with his belt buckle. Desire swells in your belly as you take in the thick erection poking against his jeans."
                            "Sensing your frustration, Damien hastily undoes his belt, letting it fall against his hips as you unzip his jeans."
                            "His erection stands proud against his boxer briefs, poking against the thin blue fabric. He shudders as your fingers stroke him, rubbing the fabric against his skin."
                            "You take him out, his cock bobbing in pleasure as your tongue traces along its underside. Damien grips one of the poles of the bleachers for support."
                            D "Ohh... [pcname]..."
                            "Excited by his response, you trace your tongue against the slit of his tip, lapping up his salty precum."
                            "Damien's fingers find their way into your hair, caressing the back of your scalp as you lean forward and take his tip into your mouth."
                            "A low, guttural moan escapes his throat; pouring out as you suck and flick the tip of his cock. He shudders against you, trying to resist the urge to push too much into your mouth at once."
                            "You bob your head and slowly slip more of his cock into your mouth, your tongue toying with him as his head presses against your cheek."
                            "You bat your eyelashes up at him in false innocence, your nails digging into his hips as you pull him further into your mouth."
                            "Damien's fingers tighten in your hair, slightly urging you forward as he rocks his hips against your face."
                            "You can't help but enjoy the sensation of Damien fucking your face, his shy exterior cracking into something more lustful; more dominant. It's just a glimpse, but you wonder what he'd be like if you ever had sex."
                            "Breathing carefully through your nose, you urge him further into your mouth, letting out a small moan as his cock hits the back of your throat."
                            D "Oh, {i}fuck{/i}, [pcname]...! Where did you learn to do that...?"
                            "He lets out a breathy laugh, but his face quickly contorts into pleasure as he thrusts into your throat."
                            "His fingers dig into the back of your scalp as he fucks your skull, sweat brimming on his forehead. You eagerly comply with his desires, moaning against his erection."
                            "The vibrations send another shudder through his body, followed by a loud gasp."
                            D "[pcname], if you keep doing that, I'll..."
                            "You feel your own body react at his suggestion, begging for a source of release. You hum against his cock again, enjoying the soft, pleasured cries that pour out of him as you slip your fingers between your legs."
                            "You rock your hips against your fingers, toying with the stiff nub of your clit as Damien shudders and spasms around you. He thrusts hard down your throat, forcing your head in place as he fucks your mouth."
                            D "[pcname]... Fuck, [pcname]...!"
                            "You feel your own release coming as his cock twitches, releasing his load down your throat. You swallow eagerly, a moan eliciting from your lips as you cum against your hand."
                            "Damien struggles to catch his breath, slumping against you slightly before he hesitantly pulls himself out of your mouth. You taste the saltiness of his cum as his tip runs against your tongue."
                            D "Ah... Hah... Sorry about that, [pcname]. I didn't mean to... Well, I meant to pull out first."
                            "He gives you an apologetic smile, although you're sure he's not particularly sorry."
                            pcname "Mmm, don't worry about it. I like the taste of you."
                            "You lick your lips seductively, peering up at him between your lashes. Damien shuffles nervously, a smile on his face."
                            D "Really? That's... Ah, that's good."
                            D "Maybe next time I can see how you taste."
                            "You blink, both surprised and aroused by his suggestion. You smirk back up at him."
                            pcname "Mmm~ How exciting. I'll hold you to that, Damien. You better not disappoint me."
                        elif True:
                            "Damien struggles to find a safe place to look at. You push against him, your cleavage exposed against his chest. Damien jolts, his body still as stone against you."
                            pcname "What's wrong, Damien? Are you nervous?"
                            "You grab one of his hands and force it against your breast, squeezing it against you. He lets out a small noise, his hand held firmly in place against you."
                            pcname "Haven't you ever touched a girl like this before?"
                            "He opens and closes his mouth a few times, struggling to find the right words."
                            D "I-I- I mean- I never-"
                            pcname "You've {i}never{/i} touched a girl like this before? What about like this?"
                            "You reach back and unclasp your bra, nudging it out from under his hand before it drops to the floor. You grab both of his wrists, forcing him to grope your breasts."
                            pcname "How does that feel, Damien? Do you like it?"
                            D "I- Er, yes, I mean- But-"
                            pcname "So you {i}do{/i} like it. Mmm, touching your girlfriend in school... What a {i}perverted{/i} thing to do, Damien."
                            "You see the blood rush to the tips of his ears, painting his face red. He tries to pull his hands away but you grip them firmly, forcing them to squeeze and massage your breasts."
                            D "But- But I didn't- I'm not-"
                            pcname "Shh. It's okay, Damien. I won't tell anyone about all the sick, perverted things you're doing to me in this gym. All of the things you're {i}going{/i} to do."
                            "You carefully remove your hands from his, everything in your gaze telling him to keep his hands in place as you kick off your shoes and slip out of your skirt and panties."
                            "Damien struggles not to look down, but in the end he can't help it. His breath hitches and he bites down on his lip nervously, taking in the full extent of your nakedness."
                            pcname "You're such a bad boy, Damien. You can barely keep your eyes off of me."
                            pcname "I guess I have no choice..."
                            show bg DCS2 with dissolve
                            "Gripping his jacket, you drag him back behind the bleachers, your mouth meeting his in frenzied kisses. Damien struggles to keep up, stumbling after you with clumsy kisses."
                            "Once you're blocked from view, you shove his jacket from his shoulders, letting it drop to the floor."
                            D "Ah, w-what are you doing?"
                            pcname "You didn't think I'd let you see my naked for free, did you, Damien? You can be so cruel..."
                            D "That's not..."
                            pcname "Not what? You {i}weren't{/i} looking at my naked body, Damien?"
                            "You press your bare body against him. He glances down again, his expression a mixture of embarrassment and desire."
                            pcname "And there you go again! Really, Damien, it's only fair~"
                            D "Ah, r-right. If... If it's fair..."
                            "Damien shyly peels his shirt off, carefully dropping it onto the floor. He stands there, unsure, awkwardly covering himself. You take his arms and pull them down to his sides."
                            pcname "There's no point if you're going to hide yourself."
                            D "Oh... Um, is that everything, [pcname]?"
                            "A smirk pulls at your lips."
                            pcname "Not even close."
                            "Wrapping your arms around his neck, you pull Damien close and press a kiss to his lips. He's rigid at first, but hesitantly starts to kiss you back. His hands hover over your body, too afraid to touch."
                            "You trace your nails over the soft skin of his bare chest, enjoying the way his body shudders against your touch. Your lips trail down his neck and chest, nipping at the pale skin."
                            "You slide down onto your knees and grip his hips tightly. Damien looks down at you uncertainly."
                            show bg DCS4 with dissolve
                            D "Ah, [pcname], w-what..."
                            "You fumble with his belt buckle until it's free, exposing the zipper of his jeans. Leaving little time for him to question, you unzip his jeans and pull him out of his boxer briefs, his erection bobbing eagerly in your direction."
                            "Damien lets out a small gasp. His hands hover over your shoulders, not sure whether to push you away or pull you further."
                            "Peering up at him through your lashes, you trace your tongue underneath his cock in one long stroke. You feel his erection harden. Damien grips your shoulders, trembling under your touch."
                            "Despite his embarrassment, you can feel Damien's excitement as his fingers press into your shoulders, begging for more."
                            "You take his tip between your lips, sucking and sliding your tongue along the slit. He shudders against you, his cock twitching in pleasure."
                            D "Hah... [pcname]..."
                            "Damien whimpers, struggling not to buck his hips forward into your mouth. Desire swells in your body at the realization of how just badly he wants you."
                            "Digging your nails into his hips, you force his hips forward, taking him further into your mouth."
                            "His whimpers increase in frequency and pitch as you bob your head along his cock, sliding him in and out of your mouth, his tip slapping the inside of your cheek."
                            "Damien's hips pick up a steady rhythm, unable to resist the little jerk of his hips every time you pull him back inside of your mouth."
                            "You can feel your own desire rising, begging for release as he moans and whimpers above you. Releasing one hand from his hips, you press two fingers against the stiff nub of your clit and rub."
                            "Pressure builds up between your legs as you masturbate. Damien notices this, unable to look away. You feel his cock twitching in your mouth, close to its release."
                            pcname "{i}He can't cum yet...I'm not finished with him.{/i}"
                            "Adjusting your breathing, you open your throat to him, yanking Damien as deeply down your throat as his cock will allow."
                            "He throws his head back in a loud cry, his nails leaving marks into the soft skin of your shoulders as he jerks his hips forward."
                            "You moan around his cock as your own release comes, jerking your hips against your fingers."
                            D "[pcname]... [pcname], I-I-"
                            "Before he can pull out, the vibrations of your moan push Damien over the edge. His cock twitches in your throat, emptying his load. He gasps, his face flushed with embarrassment."
                            D "I-I'm so sorry!"
                            "He pulls out quickly, leaving a trail of salty cum against your tongue. You swallow it all."
                            pcname "Mmm, don't be sorry, Damien."
                            "Your nails trace slightly against his hips, soothing him. Damien bites his lip."
                            pcname "You tasted {i}wonderful.{/i} Next time, I'll make you see how I taste."
                            D "O-Oh... Oh."
                            "He gives a quick nod, his body trembling and recovering from the blowjob."
                        show bg Gym with dissolve
                        show Damien Worry at left with dissolve
                        show chelsea happy at right with dissolve
                        "You both dress quickly, suddenly aware of the possibility that Ms. Vicky may still be in the school and searching for you before she locks up."
                        show Damien Happy at left
                        D "Ah, can I walk you home, [pcname]?"
                        pcname "Sure, let me just get changed first."
                        "Damien smiles shyly, pulling his jacket back on."
                        D "Okay. I'll be here."
                        show bg black with dissolve
                        hide Damien Happy at left
                        $ clothes, hair = casualwear
                        hide chelsea with dissolve
                        "You hurry back to the locker rooms and change back into your regular clothes, leaving your uniform behind."
                        "You find Damien waiting for you in the gym, reading a comic book on the bleachers."
                        show bg CityD with dissolve
                        show Damien Happy at left with dissolve
                        show chelsea happy at right with dissolve
                        "He escorts you home with a smile, lost in thought."
                        "Before you reach your apartment, Damien gives your hand a squeeze, capturing your attention."
                        show Damien Neutral at left
                        show chelsea blank
                        D "You know, the homecoming dance is coming up. If you plan on going, well, maybe we could go together?"
                        show Damien Blank at left
                        "You open your mouth to reply, but Damien quickly shakes his head."
                        show Damien Worry at left
                        D "Ah, I don't need an answer now. Just think on it, if you can..."
                        "When you reach your apartment, he leaves a kiss on your cheek before he departs."
                        hide Damien Worry with dissolve
                        "Although practice may not have gone how you wanted, you can't deny that {i}afterwards{/i} was well worth the wait!"
                        $ damienclubbj = True
                        jump events_end_period
                    elif True:
                        show chelsea happy
                        pcname "Oh no! My skirt just keeps riding up...."
                        "You bend over, showing off the blue spanks over your panties."
                        if damienconfidence >= 50:
                            show Damien Happy at left
                            "Damien shifts in place, his gaze entirely focused on the curve of your ass. There is no hiding the desire in his eyes, and especially not the desire poking through his pants."
                        elif True:
                            show Damien Worry at left
                            "Damien struggles to avert his gaze from your ass, embarrassment creeping on his face. There is no hiding the desire poking through his pants, however."
                        "You smirk, pleased to have caught his attention."
                        pcname "This uniform is just so tiny. I don't know what to do half the time. It's so easy to just see right up my skirt. Don't you think?"
                        D "Ah... I... Well..."
                        if damienconfidence >= 50:
                            "Damien approaches you as you pose on the bleachers, legs spread and your skirt lifted."
                            pcname "Is there something you want, Damien?"
                            "You bat your eyelashes up at him, fully aware of the thick erection pressed against the entrance of his jeans."
                            "He searches your face, cautious, before settling his gaze on your lips. He leans forward and presses his lips against yours."
                            show bg black with dissolve
                            hide Damien Happy with dissolve
                            hide chelsea with dissolve
                            pcname "Mmmm..."
                            "You wrap your arms around his neck, enjoying the taste of him. One of his hands slides down your arm to your breast. He gives it a slight squeeze."
                            "You try to resist a little moan as you pull back and bop him on the nose."
                            pcname "Mmmm, cute, but not today, Damien!"
                            pcname "Your little kiss was cute, though."
                            "You pull away from him, already bouncing back to your phone on the floor as Damien blinks dumbly behind you."
                            show bg Gym with dissolve
                            show Damien Shocked at left with dissolve
                            show chelsea happy at right with dissolve
                            D "Aww. You were just teasing?"
                            pcname "Maybe~"
                            pcname "Next time don't drop me and you'll get more. Kay?"
                            "Damien grins despite himself."
                            show Damien Happy at left
                            D "That's just cruel."
                            show chelsea blank
                            pcname "Tell that to the bruise on my ass. That's going to take forever to heal."
                            show Damien Neutral at left
                            "Damien opens his mouth to say something, but quickly shakes his head. His grin widens, eyes twinkling with mischievousness."
                            show Damien Happy at left
                            show chelsea confused
                            pcname "...What? What were you going to say, Damien?"
                            "He holds his hands up innocently."
                            D "Nothing. Don't worry about it."
                            show chelsea happy
                            pcname "You were thinking something {i}dirty{/i} weren't you? Naughty boy."
                            "To your surprise, Damien winks, shoving his hands in his pockets."
                            D "You want me to walk you home?"
                            pcname "Of course! Just let me get changed first."
                            show bg black with dissolve
                            $ clothes, hair = casualwear
                            hide chelsea with dissolve
                            hide Damien Happy with dissolve
                            "You hurry to the locker rooms and change into your normal clothes before meeting Damien back in the gym."
                            "You lock arms with him and allow him to escort you back to your apartment."
                            show bg CityD with dissolve
                            show chelsea happy
                            show Damien Happy at left
                            "Before you reach your apartment, Damien gives your hand a squeeze, capturing your attention."
                            show Damien Neutral at left
                            show chelsea blank
                            D "You know, the homecoming dance is coming up. If you plan on going, well, maybe we could go together?"
                            "You open your mouth to reply, but Damien quickly shakes his head."
                            show Damien Worry at left
                            D "Ah, I don't need an answer now. Just think on it, if you can..."
                            "He gives you a kiss on the cheek when you arrive to your apartment and leaves to go run errands."
                            hide Damien Worry with dissolve
                            "Practice may not have gone how you hoped, but all of the fun {i}after{/i} was worth it!"
                            "Even if you do have a massive bruise..."
                            jump events_end_period
                        elif True:
                            show Damien Worry at left
                            "You slink toward Damien, lifting your skirt a little more with each step until you're in front of him, a mischievous smirk on your lips. He remains still, afraid to move."
                            pcname "What's that look for, Damien? Is something wrong?"
                            "You press forward, pressing your breasts against his chest. He tenses up, searching for anywhere {i}but{/i} your cleavage to look at."
                            "You bat your eyelashes up at him and press a leg forward, brushing it against the firm erection in his jeans."
                            pcname "Oh? What's this?"
                            pcname "Am I turning you on, Damien?"
                            "He opens his mouth but nothing comes out, words running dry. He quickly snaps his lips closed and meets your gaze, face burning."
                            pcname "What's going on in that head of yours?"
                            "You trail your fingers through his hair, twisting one of the pieces around your finger."
                            pcname "Are you thinking dirty things about me?"
                            D "I-I-"
                            pcname "What a {i}pervert{/i} you are. I bet you're just undressing me with your eyes..."
                            "You press tighter against him for emphasis, your groin rubbing against his. A small noise escapes the back of his throat."
                            pcname "And you're so eager, too! I bet I could just..."
                            "You run your hand down his neck and chest."
                            pcname "Touch you..."
                            "You gently grasp his erection through his pants."
                            pcname "Right here, and you would cum. Is that true...?"
                            D "I-I-I-"
                            "The poor boy's head is spinning. You chuckle and pull away."
                            show chelsea laugh
                            pcname "But I won't! Seeing you like this is enough to make up for you {i}dropping me{/i}. For now, at least!"
                            show chelsea happy
                            "Damien gapes at you, mortified and disappointed. He covers his face with a groan."
                            show Damien Glare at left
                            D "You were teasing me!"
                            pcname "I was! Aren't I so good at it?"
                            pcname "I just can't help it. You're so easy to get {i}hot and bothered.{/i}"
                            show Damien Worry at left
                            "You smirk as he tries to adjust himself in his pants, clearly having a reaction at your words."
                            show chelsea blank
                            pcname "I'm going to go get changed. Walk me home?"
                            D "S-Sure."
                            show chelsea happy
                            pcname "Thanks~"
                            show bg black with dissolve
                            hide chelsea with dissolve
                            hide Damien Worry with dissolve
                            "You blow him a kiss before heading back to the locker rooms. Once you're dressed and tidied, you lope your arm through Damien's and allow him to escort you home."
                            show bg CityD with dissolve
                            show chelsea happy at right with dissolve
                            show Damien Blank at left with dissolve
                            "Before you reach your apartment, Damien gives your hand a squeeze, capturing your attention."
                            show Damien Neutral at left
                            show chelsea blank
                            D "You know, the homecoming dance is coming up. If you plan on going, well, maybe we could go together?"
                            show Damien Blank at left
                            "You open your mouth to reply, but Damien quickly shakes his head."
                            show Damien Worry at left
                            D "Ah, I don't need an answer now. Just think on it, if you can..."
                            "He kisses your cheek when you reach your apartment before heading off to run errands."
                            hide Damien Worry with dissolve
                            "Although practice wasn't at all what you were hoping for today, at least you had a lot of fun teasing Damien!"
                            "Even if you did leave with a massive bruise..."
                            jump events_end_period
                "Practice as normal." if True:
                    $ corruption -=1
                    "You shake your head, pushing the thought away. You really need to memorize this routine as is- if you start making changes now, you'll definitely forget it!"
                    show chelsea happy
                    "You run through the dance again, feeling pretty confident with the results by the end of it."
                    "Damien is, at least, relieved that you're done."
                    show Damien Neutral at left
                    show chelsea blank
                    D "You want me to walk you home?"
                    show chelsea happy
                    show Damien Blank at left
                    pcname "Sure! Let me just get changed."
                    show chelsea blank
                    "You walk off to the locker rooms quickly, changing into your normal attire."
                    hide chelsea with moveoutright
                    $ clothes, hair = casualwear
                    show bg black with dissolve
                    hide Damien Blank with dissolve
                    pause 1.0
                    show bg CityD with dissolve
                    show chelsea happy at right with moveinright
                    show Damien Happy at left with dissolve
                    "You find Damien waiting for you outside when you're done, ready to go. You walk home hand-in-hand, lost in conversation about upcoming tests and other school events happening."
                    "You both step back out into the cold autumn day, prepared to go home."
                    "Before you reach your apartment, Damien gives your hand a squeeze, capturing your attention."
                    show Damien Neutral at left
                    show chelsea blank
                    D "You know, the homecoming dance is coming up. If you plan on going, well, maybe we could go together?"
                    show Damien Blank at left
                    "You open your mouth to reply, but Damien quickly shakes his head."
                    show Damien Worry at left
                    D "Ah, I don't need an answer now. Just think on it, if you can..."
                    "When you reach your apartment, Damien gives you a kiss on the cheek before heading out to run errands."
                    hide Damien Worry with dissolve
                    "While practice itself wasn't the best, at least you have the routine memorized and ready for next time!"
                    jump events_end_period
        "Just go home." if True:
            show chelsea confused
            "You consider it for a moment, but knowing the lack of athletic bones in Damien's body, you can't imagine having him run the routine with you will end well."
            show chelsea happy
            pcname "No... Thanks, but I think I'd rather just go home."
            show chelsea blank
            pcname "This day has been exhausting."
            "Damien nods, understanding."
            D "That's fair. Can I walk you home?"
            show chelsea happy
            pcname "Sure. Let me go get changed first."
            show Damien Laugh at left
            D "Okay."
            show bg black with dissolve
            hide Damien Laugh with dissolve
            $ clothes, hair = casualwear
            hide chelsea with dissolve
            "You head to the locker room and quickly swap out of your uniform for your normal clothes. Most of the girls have already gone home for the day at this point, essentially leaving you alone."
            "Damien is waiting for you outside of the locker rooms when you're done. He takes your bag without prompting and escorts you home."
            show bg CityD with dissolve
            show Damien Happy at left with dissolve
            show chelsea happy at right with dissolve
            "He's a pretty good listener, remaining silent as you vent about the routine and how exhausted your body feels."
            "Before you reach your apartment, Damien gives your hand a squeeze, capturing your attention."
            show Damien Worry at left
            show chelsea blank
            D "You know, the homecoming dance is coming up. If you plan on going, well, maybe we could go together?"
            "You open your mouth to reply, but Damien quickly shakes his head."
            show Damien Neutral at left
            D "Ah, I don't need an answer now. Just think on it, if you can..."
            "When you reach your apartment, he plants a small kiss on your cheek before leaving to run errands."
            hide Damien Neutral at left
            show bg black with dissolve
            "Although practice may not have gone how you hoped, you're at least left with the comforting reminder that Damien cares about you."
            jump events_end_period

label damien_clubvisit_yearbook:
    show bg CityD with dissolve
    show chelsea at right with moveinright
    "The air is crisp and a little windy as you make your way to school, an indication that the autumn season is finally rolling in."
    pcname "{i}I hope some of the leaves start changing color soon... They would make really nice pictures...{/i}"
    show bg black with dissolve
    hide chelsea with dissolve
    pause 0.5
    show bg Art with dissolve
    show chelsea at right with moveinright
    "As you enter the art room, you find Mr. Davis hovering over a set of desks pushed together. As you approach him, you realize he's staring at various photographs."
    "You look around for Sophie, but she's nowhere to be found."
    "Mr. Davis lifts his head as you approach, a smile spread over his face."
    show MD Open Smile at left with moveinleft
    "Mr. Davis" "Ah, there you are, [pcname]. I was hoping you would show up soon."
    show MD Neutral at left
    "Mr. Davis" "We've got a bit of a project ahead of ourselves. Even though we open the club up to everyone, we're still responsible for the yearbook by the end of the year, which means we need to pick our photos from every event to include."
    show MD Closed Smile at left
    "Mr. Davis" "We still have plenty of time until the yearbook needs to be completed, but it's never too early to start looking through them!"
    show MD Blank at left
    "Peering down at the photographs, you see they're all from a recent cafe event held by the anime club."
    show MD Neutral at left
    "Mr. Davis" "I need to step out for a minute, but I trust you to pick out the pictures you think will work best."
    show MD Blank at left
    "Mr. Davis gives your shoulder an encouraging squeeze before stepping out of the room."
    hide MD Blank with dissolve
    show chelsea shocked
    "You stare down at the pictures, surprised by the elaborate maid costumes and brightly colored wigs."
    show chelsea happy
    pcname "They did such a good job on these outfits..."
    "As you're thumbing through them, a voice speaks over your shoulder, startling you."
    D "What are you looking at?"
    show chelsea shocked
    pcname "Ah!"
    "You drop the stack of photos onto the floor, scattering them around you. Damien stumbles back in surprise."
    $ DamienAngry = "Characters/Damien/Casual 2/Angry.png"
    $ DamienBlank = "Characters/Damien/Casual 2/Blank.png"
    $ DamienGlare = "Characters/Damien/Casual 2/Glaring.png"
    $ DamienLaugh = "Characters/Damien/Casual 2/Laughing.png"
    $ DamienNeutral = "Characters/Damien/Casual 2/Neutral.png"
    $ DamienSad = "Characters/Damien/Casual 2/Sad.png"
    $ DamienShocked = "Characters/Damien/Casual 2/Shocked.png"
    $ DamienSmiling = "Characters/Damien/Casual 2/Smiling.png"
    $ DamienWorrying = "Characters/Damien/Casual 2/Worrying.png"
    show Damien Shocked at left with dissolve
    D "Oh, I'm sorry, [pcname]! I didn't mean to scare you!"
    show chelsea embarrassed
    pcname "D-Damien? What are you doing here?"
    show Damien Blank at left
    "Trying to hide the embarrassment creeping on your cheeks, you bend down on the floor to pick up the photos. Damien crouches down as well, scooping up ones too far for you to reach."
    show Damien Happy at left
    D "I thought I'd surprise you. My club was cancelled for the day, so..."
    show Damien Neutral at left
    D "Ah, here. I'm really sorry for scaring you..."
    show Damien Blank at left
    "He shyly offers the stack of photographs in his hand. You take them and slide them back into the pile."
    show chelsea happy
    pcname "I-It's okay. Thank you for coming..."
    if damienoutfitchange == False:
        show chelsea shocked
        "As you look back in his direction, you can't help but feel surprised by his new outfit."
        "Gone are the days of ugly cargo shorts, although it feels too good to be true. Damien wears a pair of jeans- actually {i}cool{/i} jeans- and a denim jacket. His white-shirt is half-tucked into his pants, matching his white sneakers."
        "You feel your face heat up as he catches you staring."
        show Damien Neutral at left
        D "Are you okay, [pcname]?"
        show chelsea embarrassed
        pcname "Y-Yes! I-I... I just..."
        pcname "You... You changed your outfit, Damien?"
        if damienconfidence >= 50:
            show Damien Happy at left
            "Damien sheepishly looks down at his clothes, a small smile forming on his face."
            D "Yeah. You seemed like you really hated my cargo shorts, and they were getting old anyway..."
            D "So I thought I'd try for a new look. What do you think?"
        elif True:
            show Damien Worry at left
            "Damien looks down at his clothes nervously, embarrassment creeping on his face. Perhaps he was hoping you wouldn't notice..."
            D "Ah, y-yeah. Um, you... you didn't seem like you enjoyed my cargo shorts and, um, they were getting old... so..."
            show Damien Neutral at left
            D "D-Do you like it?"
        menu damienoutfitchange_year:
            "I love it!" if True:
                show chelsea happy
                $ damienconfidence +=1
                "You take a moment to look over his outfit, biting down on your lip nervously."
                "He actually looks... really, {i}really{/i} cute."
                pcname "I-I... I really like it, Damien..."
                show Damien Happy at left
                "You avert your gaze, trying to will away the heat on your face."
                "Damien grins, scratching the back of his head."
                D "You think so? I'm really glad you like it."
            "You still look like a dork." if True:
                $ damienconfidence -=1
                "You can't deny he looks really cute, but something is... missing. You're not sure if it really feels like {i}Damien.{/i}"
                show chelsea blank
                pcname "I-I don't really know how to feel about it..."
                pcname "It... It doesn't feel like you..."
                show Damien Worry at left
                "Damien frowns, awkwardly running a hand through his hair."
                D "Oh. You don't like it? ...Should I change back?"
                show chelsea sad
                pcname "N-No. I just... I don't know..."
                show Damien Neutral at left
                D "Ah... Okay. Um."
                show Damien Sad at left
                "Damien bites his lip, not sure what else to say."
    "As you both stand back up, Damien peers down at the photos in your hand, trying to get a good look at them."
    show Damien Neutral at left
    D "So, um, what are you doing?"
    show chelsea happy
    show Damien Blank at left
    pcname "Um, Mr. Davis left me in charge of picking out some photos for the yearbook."
    pcname "It's a still long ways off from being published, but we want to try to stay on top of it..."
    show Damien Neutral at left
    D "Oh, right. I guess that makes sense."
    show Damien Happy at left
    D "Do you want some help? I'm not sure if I'll be really useful, but..."
    pcname "S-Sure! Um, come have a seat."
    show chelsea blank
    show Damien Blank at left
    "You both pull up chairs around the desks and lay out the photos, separating them into small groups of 'good' versus 'bad'."
    show Damien Shocked at left
    D "There are so many photos here. I had no idea you took this many..."
    show chelsea embarrassed
    pcname "Well, um, I didn't take these. Sophie probably did..."
    show Damien Neutral at left
    D "Sophie?"
    show Damien Blank at left
    show chelsea blank
    pcname "She's a photographer. B-But I don't think she's here today..."
    show Damien Happy at left
    D "Oh. That's too bad. She did a really good job. I'm sure she wishes she were the one picking these out."
    show chelsea sad
    pcname "Yeah..."
    show chelsea blank
    "As you thumb through the photos, you come across a familiar face seated at one of the tables."
    show Damien Blank at left
    "What is clearly Damien chats animatedly with a 'maid' in long pink pigtails, a half-eaten scone in front of him. He doesn't even notice the camera."
    show chelsea confused
    pcname "I-I didn't know you were into these kind of things, Damien..."
    "He gives you a confused look, cocking his head to the side. You lift up the photograph. Embarrassed understanding crosses his face."
    show Damien Worry at left
    show chelsea blank
    D "Ah, that..."
    menu damien_animecafe:
        "Express Jealousy." if True:
            $ damienconfidence -=1
            "Looking at the photograph, you can't help but feel a rising irritation in your chest. She's so pretty, even if she's dressed ridiculously, and Damien looks so happy talking to her..."
            show chelsea confused
            pcname "Do you know her?"
            show Damien Neutral at left
            D "W-well, a little bit. She's in my biology class."
            show Damien Blank at left
            "So she's smart, too. Anxiety builds in your stomach."
            pcname "D-Do you usually flirt with other girls?"
            show Damien Shocked at left
            "He blinks, entirely taken aback."
            D "Flirt? N-No! Of course not!"
            show chelsea blank
            pcname "Because you {i}look{/i} like you're flirting..."
            D "I wasn't, I swear, [pcname]. We were just talking."
            show Damien Worry at left
            "Even though he denies it, there is no doubting the light blush spread across his face. You struggle to keep your nerve."
            show chelsea sad
            pcname "I... I'm not really comfortable with you talking to girls alone like this. You're my boyfriend, after all..."
            show Damien Sad at left
            "Damien frowns."
            show chelsea blank
            D "I... Okay. B-But it really wasn't like that... She has a boyfriend."
            "Although the mention of a boyfriend eases your jealousy some, you can't help but feel a little stubborn in your decision."
            "Maybe it's your own insecurities being reflected through her, but you still feel uncomfortable with the idea of Damien flirting with other girls."
            show Damien Blank at left
            pcname "I-Okay. B-But I still want to be there... It would make me feel comfortable... Please..."
            "Damien bites his lip but gives a sheepish nod."
            show Damien Neutral at left
            D "O-Of course. I'm sorry for making you worry, [pcname]..."
        "Express Curiosity." if True:
            $ damienconfidence +=1
            "Looking at the photograph, you can't help but feel a rising curiosity in your chest. The event looks like a lot of fun, and if it's something Damien enjoyed..."
            show chelsea happy
            pcname "Y-You look like you had a lot of fun..."
            show Damien Happy at left
            D "Oh, yeah. It was a good time. One of my biology classmates invited me- that's her in the pink wig."
            D "She and her boyfriend hosted the event."
            "The mention of a boyfriend eases any sliver of jealousy in you, although there wasn't much to begin with."
            "Instead, you find yourself captivated with the well-made costumes and styled wigs. It's like a cute Halloween party with breakfast food."
            show chelsea sad
            pcname "I-I wish I could go..."
            show Damien Shocked at left
            "Damien's eyebrows raise, surprised."
            D "Really?"
            show Damien Worry at left
            D "I'm sorry, [pcname]. I wasn't really sure if this would be your thing, so I didn't mention it..."
            show Damien Happy at left
            D "But if you're really interested, the next time they hold an event, I promise to take you with me."
            show chelsea happy
            pcname "Y-You will?"
            "He smiles, placing his hand overtop yours. Its soft and warm, a gentle comfort."
            D "I promise."
            pcname "O-Okay..."
            show chelsea embarrassed
            "Looking down, you can't help but admire Damien's smile in the photograph. It's really such a good picture of him, and you don't have any so far..."
    "You set the photo down aside from the rest. It's too blurry to use in the yearbook, but maybe Mr. Davis won't notice if it goes missing..."
    show chelsea blank
    show Damien Blank at left
    "As you continue to thumb through the photos, an idea comes to your mind."
    show chelsea embarrassed
    pcname "Y-You know, um, Damien, we're dating now... But we still don't have a picture together."
    "Damien pauses his own search through the photos. He opens his mouth to object but stops, tapping his chin in thought."
    show Damien Neutral at left
    D "You're right. We don't have any together."
    show Damien Blank at left
    show chelsea happy
    "Carefully lifting the camera strapped around your neck, you glance at Damien shyly."
    pcname "U-Um, do... do you want to...?"
    if damienconfidence >= 50:
        show Damien Happy at left
        "Damien eyes the camera around your neck and gives you a soft smile."
        D "Yeah. I'd love to."
    elif True:
        show Damien Happy at left
        "Damien eyes the camera around your neck nervously, biting down on his lip. He gives an equally shy nod."
        D "S-Sure..."
    show chelsea blank
    "Setting the pictures aside, leaving the two you really like on top of the pile, you glance around the classroom. The lighting isn't great and it's a little crowded."
    pcname "L-Let's go outside. The lighting will be better."
    show Damien Neutral at left
    D "Okay."
    show Damien Blank at left
    "Discreetly tucking the photograph of Damien in your pocket, you grab a tripod from the stock room and lead Damien outside of the school."
    show bg School with dissolve
    "It's not a perfect day, with overcast skies and a chill wind in the air. Still, the lighting will be perfect for some soft photos together."
    "Where would you like to take a photograph together?"
    menu damien_photograph:
        "By the fountain." if True:
            "You lead Damien to a beautiful fountain near a set of benches on the school grounds, a large fish spitting water up into the air. A few freshly fallen leaves litter the edges of the fountain's cement edges."
            "Damien shuffles before the camera awkwardly as you set up the tripod, unsure of what to do with himself."
            "After you set the timer, you quickly gesture for him to take a seat on the fountain's edge."
            show Damien Neutral at left
            D "What do I do?"
            show Damien Worry at left
            "He sounds nervous, his gaze constantly glancing at the camera's lens. He must not be used to being photographed. Truthfully, you aren't either."
            show chelsea happy
            "You settle beside him on the ledge as the camera begins to blink down its timer. It feels awkward trying to pose for a picture. You aren't sure what to do with your hands or feet."
        "By a tree." if True:
            "You lead Damien to a large oak tree, its leaves tinged with yellow and orange as autumn settles in."
            "Damien shuffles before the camera awkwardly as you set up the tripod, unsure of what to do with himself."
            "After you set the timer, you quickly gesture for him to lean against the tree's bark. He does so, stiff as a board and entirely unphotogenic."
            show Damien Neutral at left
            D "What do I do?"
            show Damien Worry at left
            "He sounds nervous, his gaze constantly glancing at the camera's lens. He must not be used to being photographed. Truthfully, you aren't either."
            show chelsea happy
            "You lean against him and the tree as the camera begins to blink down its timer. It feels awkward trying to pose for a picture. You aren't sure what to do with your hands or legs."
        "By the pond." if True:
            "You lead Damien to the small koi pond near the back of the school grounds; a project completed by Seniors long before your time."
            "Damien shuffles before the camera awkwardly as you set up the tripod, unsure of what to do with himself."
            "After you set the timer, you quickly gesture for him to take a seat in the grass beside the pond."
            show Damien Neutral at left
            D "What do I do?"
            show Damien Worry at left
            "He sounds nervous, his gaze constantly glancing at the camera's lens. He must not be used to being photographed. Truthfully, you aren't either."
            show chelsea happy
            "You settle beside him on the grass as the camera begins to blink down its timer. It feels awkward trying to pose for a picture. You aren't sure what to do with your hands or feet."
    "Looking up at Damien, you see he feels the same."
    "At least there's one thing you know you {i}want{/i} to do."
    show Damien Shocked at left
    "Gathering your courage, you lean forward and softly kiss his lips. Damien blinks, surprised, as the first picture is taken."
    D "Was that it?"
    show chelsea embarrassed
    pcname "T-There are a few more set for the timer..."
    show Damien Happy at left
    D "Oh... okay."
    if damienconfidence >= 50:
        "Damien closes his eyes, leaning into a second kiss. This one feels more natural as he pulls you against him, one hand in your hair while the other settles on your waist."
        "You press your hands against his shoulders, melting into his touch."
        show chelsea shocked
        "Another photo is taken. Damien's hand shifts down your waist. You let out a little yelp as he firmly cups your ass."
        "The camera clicks with another photo."
        show chelsea embarrassed at right
        "He pulls away slightly, chuckling a little."
        D "Was that too much, [pcname]?"
        pcname "I-I..."
        "Your cheeks flare up, but you can't deny that you liked it. Feeling him touch your body is a new sensation, something you would like to feel more of..."
        "Embarrassment floods your face as you realize what it is you {i}want{/i} from him."
        pcname "I-It's fine!"
        show chelsea happy
        "You quickly hurry back to the tripod, trying to use your hair as a shield as you review the pictures. They're actually quite cute, except for the last one..."
        "You feel desire swell in your belly as you stare at the most recent picture. If he could just keep touching you like that..."
    elif True:
        "Damien hesitantly closes his eyes, carefully leaning into a second kiss. It feels a little more natural, but you can still tell he's nervous around you."
        "You press your hands against his shoulders and pull him forward, trying to encourage him to kiss you. He does, but barely, too afraid to mess up."
        "You grip his hands and pull them to your waist, trying to shove the embarrassment you feel down as far as you can."
        "The camera clicks with another photo."
        "Damien pulls away slowly. He bites on his lip, uncertain."
        show Damien Worry at left
        D "W-Was that okay, [pcname]?"
        show chelsea embarrassed
        pcname "I-I..."
        "You want to tell him that it's okay to touch you, but the thought of its implication only further embarrasses you."
        "But maybe you could {i}show{/i} him..."
        "You quickly shake your head, erasing the thought. It's too embarrassing to think about!"
        show Damien Blank at left
        show chelsea happy
        pcname "I-It's fine!"
        "You quickly hurry back to the tripod, trying to use your hair as a shield as you review the pictures. They're actually quite cute, although you can clearly see Damien's nervousness in his stiff posture."
        "Something about seeing him so nervous around you, though, sends a thrill of desire through you. If you can make him feel that flustered just from a kiss, you wonder what he would do if you did something more..."
    show chelsea embarrassed at right with move
    pcname "W-we should get back to the club room."
    show Damien Happy at left
    D "Yeah. That sounds like a good idea..."
    show chelsea blank
    "You pack up the camera and give the tripod to Damien, allowing him to carry it back inside."
    show bg Art with dissolve
    "By the time you reach the club room, you're surprised to find it empty."
    show chelsea confused
    pcname "Did club end already?"
    "Damien glances at a large clock above the chalkboard."
    show Damien Neutral at left
    show chelsea blank
    D "Yeah, it's about that time. I didn't realize we were taking pictures for so long..."
    show Damien Blank at left
    "You look back to the set of desks, but the pictures of the anime cafe event have already been cleaned up and put away. You hope Mr. Davis wasn't too disappointed that you didn't pick a photo..."
    show Damien Neutral at left
    D "We should put this away and head home."
    show Damien Blank at left
    pcname "Y-Yes."
    "You lead Damien to the stock room, pointing out where the tripod goes."
    if corruption >= 20:
        menu choice188:
            "Blow Damien in the stock room." if True:
                $ corruption += 2
                show chelsea embarrassed
                "As you watch him put away the equipment, there's no denying the warmth spreading between your legs."
                "Hands shaking, you close the door behind you."
                show bg black with dissolve
                "Darkness surrounds you, although you can just barely make out Damien's figure as he jumps, startled."
                show Damien Shocked at right
                D "[pcname]?"
                pcname "I-It's just me."
                show Damien Neutral at left
                D "Why did you close the door?"
                show Damien Blank at left
                "Anxiety twists knots in your stomach. Maybe this was a bad idea. Maybe you should just open the door and leave..."
                "But here in the darkness where you can't see any judgment on his face, you feel a little more confident in your decision."
                "At least if he rejects you, you don't have to see it..."
                "You reach out in the small space, your hand finding his arm. You carefully step forward and close the distance between you with a kiss."
                hide Damien Blank with dissolve
                hide chelsea with dissolve
                show bg DYS1 with dissolve
                show powerout with dissolve
                if damienconfidence >= 50:
                    "He doesn't react at first, surprised by your unusual boldness. Slowly, his hands find your waist, pulling you flush against him."
                    "Everything about his touch feels sweet, from the gentle movement of his lips to the way his thumbs rub circles into your waist."
                    "Hesitantly, his fingers reach under your shirt, roaming over the exposed skin there."
                    "You pull back from the kiss slightly and his hands stop, prepared to pull away as well. With shaking hands, you lift your shirt over your head and drop it onto the floor."
                    "A soft sigh escapes his lips before Damien kisses you hard, his hands pressed even firmer against your body."
                    D "Ah... [pcname]..."
                    "His hands roam up to cup your breasts."
                    D "Is this okay...?"
                    "You bite your lip, almost too embarrassed to answer. Somehow it feels easier in the dark, though..."
                    pcname "Y-Yes..."
                    "You gasp as Damien gropes your breasts, squeezing the soft fabric of your bra between his fingers. It would feel even nicer if there wasn't anything there at all..."
                    show bg DYS2 with dissolve
                    "As if reading your mind, Damien is already reaching back and fumbling with the clasp of your bra. You reach back and help him, your nipples hardening as they're hit by the cold air."
                    D "[pcname]..."
                    "He gently squeezes your bare breasts, testing for your reaction. You lean into him further, biting back a moan."
                    "Encouraged, Damien fondles your breasts, his gentleness slowly ebbing away with his growing desire."
                    "Your fingers tremble as you slip out of your bottoms and nudge your shoes off. All that's left are the panties..."
                    "Reminding yourself that he can't see, you shakily drop your panties onto the floor, the moist spot of your arousal suddenly greeted by the cold air."
                    "Damien's hands slide down your breasts to your waist, pausing slightly in his surprise to find your clothes aren't there."
                    D "[pcname], are you...?"
                    "You open your mouth to confirm, but you can't bring yourself to do it. Even in the dark, your heart is hammering in your ears, flooding all rational thought from your brain."
                    "Instead, you kiss him again, your trembling hands running down his chest. You push back his denim jacket, allowing it to fall into a heap on the floor."
                    "Picking up on what you desire, Damien lifts his shirt up over his head, dropping it on top of his jacket. You carefully feel the planes of his chest, each touch of your skin against his like electric."
                    show bg DYS3 with dissolve
                    "Hesitantly, your lips move down his jawline and his neck, soft and careful against his skin as you kiss down his chest and slide onto your knees."
                    "You look up to him in askance, only to realize he can't see you. The soft caress of his fingers against your scalp encourage you to keep going, though."
                    "In the dark, it's difficult for you to unclasp his belt. Sensing your trouble, Damien reaches down and undoes it for you, one hand returning to brush your hair. The touch is comforting, easing the building anxiety in your chest."
                    "You unzip his jeans and pull him out of his boxer briefs, his erection flexing eagerly in your direction."
                    "Damien lets out a soft moan as you place your tongue against his tip."
                    "Relaxing, you continue to lick his tip, relishing in the bob of his cock with every touch."
                    D "Ah... Hah... [pcname]..."
                    "His fingers tangle in your hair, nudging his cock against your lips."
                    pcname "{i}H-He likes it!{/i}"
                    show bg DYS4 with dissolve
                    "You take his tip in, sucking and flicking the sensitive skin with your tongue."
                    "Damien's hold of your hair grows tighter, becoming less of a caress and more of a grip as he bucks his hips toward your face."
                    "You let out a little gasp around him as his cock presses into the side of your cheek."
                    D "S-Sorry... Is this okay...?"
                    "You bob your head in confirmation, the movement forcing his cock in and out of your mouth. Damien moves, thrusting with the movement."
                    pcname "{i}I-It's so embarrassing, b-but... But I really want to see his reaction if I...{/i}"
                    "Careful, you work to control your breathing before opening your throat to him. With Damien's next thrust, he's surprised to find you take his cock entirely down your throat."
                    D "Ohh, fuck, [pcname]!"
                    "Fingers digging into your scalp, Damien holds you in place as he fucks your face eagerly. You feel his balls slap against your chin, and pressure builds between your legs, begging for release."
                    "Only in the safety of the dark do you feel bold enough to touch yourself, slipping two fingers against your clit and rubbing hard."
                    "It's in the dark, so it's not like he can see, but the knowledge of what you're doing... It's enough to turn your ears pink."
                    "You continue to touch yourself as Damien grinds down your throat, close to his own climax."
                    D "[pcname], I'm- I'm gonna-"
                    "Before he can finish his words, you let out a loud moan, your own orgasm sending you over. The noise reverberates against his cock, sending him over the edge as well."
                    "You feel Damien's cock twitch in your throat, emptying his load. You swallow, desperate to keep from making a mess as he finishes in your mouth."
                    "He pulls out of your mouth, out of breath and sweating. His fingers ease on your scalp, returning to the soft strokes from before."
                    D "Ah... Hah... Sorry about that, [pcname]. I didn't mean to... Well..."
                    "You shakily catch your breath, the salty taste of his cum still coating your tongue."
                    pcname "I-It's okay! I..."
                    "You avert your gaze, unable to look in his direction even in the safety of the dark."
                    pcname "I liked it, actually..."
                    D "Really?"
                    D "I'm glad. Maybe next time I'll get to taste you."
                    "You blush and bite down on your lip, unable to find the words to respond without stuttering. That does sound nice..."
                elif True:
                    "He doesn't react at first, rigid as a stone in the face of your unusual boldness. Slowly his lips move with yours, but it's uncertain, as if he's afraid he's mistaking the situation."
                    "You try to kiss him a little harder, to show him how much you want him in this small space. His lips move with yours, trying to keep up with your growing desire."
                    "Carefully so he won't pull away, you lift your shirt over your head and drop it to the floor. He pauses at the noise, confused."
                    pcname "I-I want you to... to..."
                    "Too embarrassed to say it, you grab his wrists and press his hands against your chest. The shaking in his hands are almost as bad as yours."
                    D "Y-You... You're sure you want this? F-from me?"
                    "You nod quickly and hope he can see it."
                    "Damien gives your breasts a very light squeeze. It feels like nothing at all with your bra in the way."
                    pcname "H-Hold on."
                    show bg DYS2 with dissolve
                    "He pauses at once, ready for you to push him away. Instead, you unclasp your bra and let it fall to the floor before pressing your bare breasts against his palms. His breath hitches with the contact."
                    pcname "T-Touch... Touch me, Damien..."
                    "You can feel the trembling of his hands as he slowly plays with the weight of your breasts, squishing them softly between his fingers."
                    "You can see the vague outline of him glancing in your direction, likely checking your reaction for reassurance, and then not knowing what to do when he can't see it."
                    "You may be too embarrassed to say it outright, but perhaps you can reassure him in another way..."
                    "Your fingers tremble as you slip out of your bottoms and nudge your shoes off. All that's left are the panties..."
                    "Reminding yourself that he can't see, you shakily drop your panties to the floor, the moist spot of your arousal suddenly greeted by the cold air."
                    "Slowly, you tug one of Damien's hands down your waist and to your ass. You can feel his body stiffen as he realizes you're naked."
                    D "A-Ah, [pcname]..."
                    "Even in the dark, you're too embarrassed to say much of anything. You only feel confident in the boldness of your actions, despite your heart hammering in your ears."
                    "You kiss him again, struggling to control the trembling in your hands as you push back his jacket."
                    "Picking up on what you desire, Damien doesn't object or struggle as you tug his shirt over his head as well, tossing it into a heap on the floor. You feel the planes of his bare chest, each touch of your skin against his like electric."
                    pcname "T-Tell me if... if you want me to stop..."
                    show bg DYS3 with dissolve
                    "Even as you say it, you desperately hope he won't. You press feather-light kisses down his neck and chest, shakily dropping onto your knees."
                    "You reach to unzip his pants, but his belt stands in your way. After a few moments of struggling, you realize you can't get it without some light."
                    pcname "Your belt..."
                    "Damien's shaky hands unclasp it, his fingers settling lightly onto your shoulders. You unzip his jeans and pull his erection out of his boxer briefs."
                    "You can feel your heart pick up the pace as you lean forward and brush your tongue against the tip of his cock. Damien bites down in his lip, a small whimper eliciting from his throat."
                    "Encouraged by his response, you relax a little, your tongue lapping lightly against the soft curve. Damien digs his fingers into your shoulders, trying to resist the little jerk of his hips as his body begs for more."
                    pcname "{i}H-He's really enjoying it...!{/i}"
                    "You pull his tip into your mouth, sucking and flicking the sensitive skin with your tongue. Damien shudders, his hips bucking in your direction."
                    show bg DYS4 with dissolve
                    D "O-Ohhh..."
                    "A moan escapes his mouth as his hips jerk forward. You let out a little gasp around his cock as he presses it further into your mouth, smacking it against the side of your cheek."
                    D "S-sorry! I didn't mean-"
                    "He starts to pull out, but you quickly shove your head forward, pushing him even further into your mouth. Damien's legs quake, weak with your touch."
                    "You bob your head up and down, moving his cock in and out of your mouth with growing eagerness. He continues to thrust his hips, slowly, afraid to push too much too hard at once."
                    pcname "{i}I-It's so embarrassing, b-but... But I really want to see his reaction if I...{/i}"
                    "Careful, you work to control your breathing before opening your throat to him. With Damien's next thrust, he's surprised to find you take his cock entirely down your throat."
                    D "Ah! Ah, [pcname]!"
                    "His fingers dig into your shoulders, leaving small marks as he gently fucks your face. You can feel the moist spot between your legs grow wetter, begging for some sort of release."
                    "Only in the safety of the dark do you feel bold enough to touch yourself, slipping two fingers against your clit and rubbing hard."
                    "It's in the dark, so it's not like he can see, but the knowledge of what you're doing... It's enough to turn your ears pink."
                    "You continue to rub yourself off as Damien grinds lightly into your throat, his balls gently brushing your chin with each movement."
                    "You're close to your own climax when you feel his fingers dig hard against your shoulder, his cock twitching in your throat."
                    D "[pcname]... [pcname]...!"
                    "You let out a moan around his cock, the noise reverberating against him as you cum. He lets out a cry, his erection spasming as he empties his load into your throat."
                    "You swallow his salty cum, afraid if you open your mouth now, it'll all spill out and Mr. Davis will definitely know where you disappeared to..."
                    "Realizing what he's done, Damien quickly pulls himself from your mouth, stumbling back."
                    D "I-I'm so sorry, [pcname]! I- I didn't mean- That wasn't-"
                    "He fumbles over his apology, struggling to find the right words. You bite back a smile. At least you aren't the only one embarrassed..."
                    pcname "I-it's okay! Please... I..."
                    "Even in the dark, you're too embarrassed to look in his direction."
                    pcname "I enjoyed it..."
                    D "I... You... You did?"
                    "Relief washes over the both of you as you come to realization that you actually {i}enjoyed{/i} what just occurred."
                    D "T-That's... I-Thank you."
                    "You briefly consider asking him to return the favor, but even {i}that{/i} is too embarrassing to ask out loud..."
                "You both quickly get dressed in the dark, the thought of Mr. Davis coming back to find you naked in the stock room putting the sense of fear in your mind."
                "Once you're set, Damien carefully entwines his fingers with yours and leads you out."
                show bg Art with dissolve
                show Damien Happy at left with dissolve
                show chelsea embarrassed at right with dissolve
                D "So, um, can I walk you home?"
                "You nod, struggling to look him in the eye. After {i}that...{/i} You're not sure if you ever will again!"
                "Damien offers to hold your backpack and leads you out of the school."
                show bg CityD with dissolve
                show chelsea blank
                show Damien Worry at left
                D "Hey, um, you'll send me those pictures, right?"
                show Damien Neutral at left
                D "I think I'd really like to have one as my phone background..."
                show chelsea happy
                "You bite back a smile, nodding."
                show Damien Happy at left
                pcname "S-Sure. Me too..."
                "Before you reach your apartment, Damien gives your hand a squeeze, capturing your attention."
                D "You know, the homecoming dance is coming up. If you plan on going, well, maybe we could go together?"
                "You open your mouth to reply, but Damien quickly shakes his head."
                show Damien Worry at left
                D "Ah, I don't need an answer now. Just think on it, if you can..."
                show Damien Happy at left
                "When you reach your apartment, he plants a small kiss on your cheek before leaving to run errands."
                hide Damien Happy with dissolve
                "Although you didn't get to finish that project for Mr. Davis, you can't deny that this was certainly the most {i}exciting{/i} club you've had yet!"
                "If only you could stop blushing..."
                $ damienclubbj = True
                jump events_end_period
            "Go home." if True:
                $ corruption -=2
                pass
    elif True:
        pass
    show bg black with dissolve
    hide Damien Blank with dissolve
    hide chelsea with dissolve
    "Once the equipment is safely put away, you both wander back outside of the school."
    show bg CityD with dissolve
    show Damien Happy at left with dissolve
    show chelsea at right with dissolve
    D "Hey, um, you'll send me those pictures, right?"
    D "I think I'd really like to have one as my phone background..."
    show chelsea happy
    "You bite back a smile, nodding."
    show chelsea embarrassed
    pcname "S-Sure. Me too..."
    show chelsea happy
    "You both share a shy grin, entwining your fingers together as Damien escorts you back home."
    "Before you reach your apartment, Damien gives your hand a squeeze, capturing your attention."
    show chelsea confused
    D "You know, the homecoming dance is coming up. If you plan on going, well, maybe we could go together?"
    show chelsea blank
    "You open your mouth to reply, but Damien quickly shakes his head."
    show Damien Worry at left
    D "Ah, I don't need an answer now. Just think on it, if you can..."
    "When you reach your apartment, he plants a small kiss on your cheek before leaving to run errands."
    hide Damien Worry with dissolve
    "Although you didn't get to finish that project for Mr. Davis, you can't help but feel warm and fuzzy after the day spent with your boyfriend."
    jump events_end_period
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
