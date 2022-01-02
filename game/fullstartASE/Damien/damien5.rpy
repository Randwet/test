label damien_missingpanties:
    $ clothes = "school"
    show chelsea at right with moveinright
    show bg Cafeteria with dissolve
    "As usual, the cafeteria is crowded by the time you arrive, and the lunch line is already well past the open doors."
    "You sigh in disdain and reluctantly walk toward the end of the line."
    D "Ah, [pcname]!"
    show Damien Happy at left with moveinleft
    show chelsea shocked
    "Glancing over your shoulder, you catch a glimpse of Damien waving at you from your usual cafeteria table. There are two trays of food in front of him."
    show Damien Neutral
    show chelsea happy
    "Abandoning your line, you join him at the table."
    show Damien Happy
    "Damien perks up with your arrival, sliding one of the trays toward you."
    show chelsea shocked
    pcname "Is this for me?"
    show Damien Laugh
    show chelsea blank
    D "Yeah. I figured the lines would get pretty long by the time you got here, so I grabbed you a tray, too."
    show Damien Happy
    D "Even scored you the last cupcake!"
    "Sure enough, a pretty red velvet cupcake sits on your tray."
    if club == "track":
        show chelsea laugh
        pcname "Shit, thanks! I was sure they'd be out!"
    elif club == "cheer":
        show chelsea happy
        pcname "Aww, thank you, Damien!"
    elif club == "yearbook":
        show chelsea embarrassed
        pcname "T-Thank you!"
    if damienconfidence >= 50:
        "Damien smiles at you, pressing a kiss to your cheek."
        D "No problem."
    elif True:
        "Damien smiles bashfully, eager to be praised."
    show Damien Blank
    show chelsea happy
    "You grin back and dig into your food without hesitation, pleased to find it's still warm."
    "Damien takes that as his cue to dig in as well, munching on a pack of carrot sticks."
    show Damien Neutral
    D "So, what are you up to after school today?"
    show Damien Blank
    show chelsea blank
    pcname "Not much. I have some laundry to do when I get home, but that's about it."
    show chelsea shocked
    show Damien Shocked
    pcname "Ah! That reminds me!"
    show Damien Blank
    "You lower your voice so the neighboring tables won't overhear."
    show chelsea confused
    show Damien Shocked
    pcname "I haven't been able to find my lingerie from the other night. I've been looking everywhere for it, but I have no idea what I did with it."
    show chelsea sad
    show Damien Blank
    pcname "Do you remember seeing it anywhere?"
    show Damien Worry
    show chelsea blank
    "Damien presses his hand to his lips, thinking it over. After a moment he frowns, shaking his head."
    show Damien Sad
    show chelsea sad
    D "Sorry, [pcname], I don't. The last I saw it was when we... well..."
    "A light blush paints Damien's cheeks as he thinks back to the night of the dance."
    "You sigh, disappointed."
    show chelsea blank
    show Damien Blank
    pcname "That's okay. I knew it was a long shot, but I thought I'd ask."
    if damienlingeriepurchase == True:
        if club == "track":
            show chelsea confused
            pcname "What a waste. That shit was expensive."
        elif club == "cheer":
            show chelsea sad
            pcname "But this really sucks... It was so cute, too."
        elif club == "yearbook":
            show chelsea sad
            pcname "I-I wish I could find it... It was very comfortable..."
    elif True:
        if club == "track":
            show chelsea confused
            pcname "This sucks. That was my favorite pair."
        elif club == "cheer":
            show chelsea confused
            pcname "This is so annoying... It was my favorite pair, too..."
        elif club == "yearbook":
            show chelsea sad
            pcname "I-I just wish I could find it... It was so comfortable..."
    show chelsea blank
    show Damien Happy
    "Damien smiles sympathetically and places his hand over yours, his skin rubbing softly over the top of your palm."
    show Damien Neutral
    D "I'm sorry, [pcname]. I'm sure it'll turn up eventually."
    show chelsea sad
    pcname "Yeah... I hope so. I just have no idea what I did with it..."
    show chelsea shocked
    show Damien Shocked
    show Alex Laugh at center with moveinleft
    "Alex" "Aw, look at the lovebirds."
    show Damien Sad
    show Alex Happy
    "You jump, startled by Alex's voice. He stands near the edge of your table, a harsh smirk on his face as he looks between you and Damien."
    show Alex Blank
    if mattslap == 1 and bullytelloff == 1:
        show chelsea sad
        "A sickening feeling settles in your stomach and you find yourself unable to look him in the eye, the reminder of his brutal assault on you in the alley still fresh in your mind."
    if mattsubmissive == True and bullytelloff == 1:
        show chelsea embarrassed
        "Your cheeks flush with shame and panic settles deep in your chest as you recall the threesome you had with him and Matt in the classroom."
        show chelsea sad
        "You can't bring yourself to look him in the eye, afraid that Damien will see something there and instantly know what happened."
    elif True:
        show chelsea confused
        pass
    show Alex Neutral
    "Alex" "I'm surprised you're still together. Did you pay [pcname] to stick around at school, too?"
    show Alex Happy
    if damienconfidence >= 50:
        show Damien Glare
        "Damien rolls his eyes and turns away, trying to ignore Alex's taunts."
        show Damien Angry
        show Alex Blank
        D "Go away, Alex."
    elif True:
        show Damien Sad
        "Damien shrinks a little under Alex's gaze, his hands trembling a little as he takes another bite of his food."
        show Damien Worry
        "He says nothing in response, clearly wishing to avoid the confrontation altogether."
    show Damien Glare
    show chelsea shocked
    show Alex Laugh
    "Alex laughs cruelly, walking past Damien to stand behind you. You tense up as you feel his arm wrap around your shoulders, tugging you into his side as he leans close to your ear."
    show chelsea confused
    show Alex Neutral
    "Alex" "You're too hot to be into freaks like this, [pcname]."
    show Alex Laugh
    "Alex" "That is, unless {i}you're{/i} deranged, too. I hear redheads {i}are{/i} pretty freaky in bed."
    if mattslap == 1 and bullytelloff == 1:
        show chelsea shocked
        show Damien Shocked
        show Alex Happy
        "Alex smirks at you knowingly, his eyes trailing down to a gap in your blouse."
        show Damien Glare
        show chelsea angry
        show Alex Laugh
        "You quickly push him away, crossing your arms over your chest. Alex laughs, his breath tickling your ear."
        show chelsea sad
        "You feel tears prick at the corners of your eyes but squeeze them shut in an attempt to hold them back. The last thing you want is for Alex to see you cry again."
    if mattsubmissive == True and bullytelloff == 1:
        show Damien Shocked
        show chelsea shocked
        show Alex Happy
        "Alex smirks at you knowingly, his eyes trailing down to a gap in your blouse."
        show Damien Glare
        show chelsea embarrassed
        "You feel your cheeks heat up, the familiar desire growing in your belly alongside shame."
        show chelsea sad
        show Alex Laugh
        "You quickly look away, unable to look him in the eyes. Alex laughs, his breath tickling your ear."
    elif True:
        show Damien Shocked
        show chelsea embarrassed
        show Alex Happy
        "Alex smirks at you, his eyes trailing up and down your body with a growing hunger."
        show chelsea confused
        show Damien Glare
        show Alex Laugh
        "You cross your arms over your chest, uncomfortable under his gaze."
    if damienconfidence >= 50:
        show Damien Glare
        show chelsea sad
        "An angry look crosses Damien's face as Alex eyes you up and down."
        show Damien Angry
        show chelsea shocked
        show Alex Neutral
        D "Do you {i}mind?{/i} That's my {i}girlfriend.{/i}"
    elif True:
        show Damien Sad
        show chelsea sad
        "Damien's face contorts uncomfortably, clearly torn between his fear of confrontation and his own anger at Alex."
        show Damien Neutral
        show Alex Laugh
        D "A-Alex, leave her alone, please... That's my girlfriend..."
    show chelsea blank
    show Damien Glare
    show Alex Blank
    "Alex waves him off, uncaring."
    show chelsea confused
    show Alex Serious
    "Alex" "I know who the bitch is."
    show Damien Worry
    show Alex Neutral
    "Alex" "Why are you still sitting here, [pcname]?"
    show Damien Shocked
    show chelsea shocked
    show Alex Laugh
    "Alex" "C'mon, drop this loser. Let's have lunch at my table."
    show chelsea blank
    show Damien Worry
    show Alex Happy
    "He nods his head back toward another table in the cafeteria where a few of his other friends sit and goof around."
    if damienconfidence >= 50:
        show Damien Glare
        show chelsea shocked
        show Alex Angry
        "Damien slams a fist on the table, startling both of you. He glares up at Alex, angrier than you've ever seen him."
        show Damien Angry
        show Alex Blank
        D "I told you to {i}leave{/i}. Don't bring [pcname] into whatever beef you have with me."
        show Alex Laugh
        "Alex gapes at him, laughing in disbelief."
        show chelsea sad
        show Damien Glare
        "Alex" "Are you fucking serious? When the hell did you grow a spine?"
        show Damien Blank
        show chelsea blank
        show Alex Angry
        "Alex opens his mouth, ready to give Damien a piece of his mind, but one of the homeroom teachers walks by, eyeing up the boys with suspicion."
        show chelsea sad
        show Alex Happy
        "Alex forces a smile instead, leaning close so Damien can hear him through clenched teeth."
        show chelsea shocked
        show Damien Worry
        show Alex Serious
        "Alex" "You're going to regret that, Damien."
        show chelsea sad
        show Alex Blank
        "He gives your body another long, full stare before turning back to his table, leaving the two of you alone."
        hide Alex Blank with moveoutleft
        show Damien Glare
        "Damien sighs in frustration, taking an angry bite of his food."
    elif True:
        show Damien Worry
        show chelsea sad
        "Damien looks as though he wants to say something but keeps his mouth shut, glancing nervously between the two of us."
        show Damien Shocked
        show Alex Laugh
        "Alex" "What is it, Damien? You have something to say?"
        show Damien Worry
        show Alex Blank
        show chelsea blank
        D "I-I... Well..."
        show Damien Shocked
        show chelsea shocked
        show Alex Angry
        "Alex" "Speak up! The fuck do you have to say to me?"
        show Damien Sad
        show chelsea sad
        "You hate to see your boyfriend getting bullied, especially from someone as self-centered and rude as Alex."
        show chelsea blank
        show Alex Blank
        "Fed up with his antics, you decide to stand up to him."
        show Alex Serious
        show Damien Shocked
        if club == "track":
            show chelsea angry
            pcname "Alex, fuck off. No one wants to sit with your stank ass."
        elif club == "cheer":
            show chelsea confused
            pcname "Alex, be a dear and kindly go fuck yourself. Your voice is giving me a migraine."
        elif club == "yearbook":
            show chelsea sad
            pcname "G-Go away, Alex. We just want to eat our lunch in p-peace..."
        show chelsea confused
        show Alex Neutral
        "Alex" "Oh, so now the slut has something to say?"
        if mattslap == 1 and bullytelloff == 1:
            show chelsea sad
            show Damien Sad
            show Alex Blank
            "You wince at his words but try not to show how badly they affect you."
            "It's not like it was your choice to have sex with him and Matt in that alley. Just the implication of it fills your heart with grief."
            show Damien Shocked
            show Alex Serious
            if club == "track":
                show chelsea angry
                pcname "Go fuck yourself, Alex."
            elif club == "cheer":
                show chelsea angry
                pcname "You're disgusting. Go back to the other pigs waiting for you."
            elif club == "yearbook":
                show chelsea angry
                pcname "I-I'm not a slut...! You... You..."
                show chelsea sad
                "You can't bring yourself to say any more, your throat constricting with the threat of tears."
            show Damien Sad
            show chelsea sad
            show Alex Laugh
            "He laughs, unbothered by your response. It only makes you feel worse inside."
        if mattsubmissive == True and bullytelloff == 1:
            show chelsea shocked
            show Damien Worry
            show Alex Blank
            "The words hit you like a slap to the face. You feel your cheeks burn with shame and you glare up at him, trying to push down the terror rising in your chest."
            "Is he going to say something to Damien? You don't know, but you desperately hope not."
            show Damien Shocked
            if club == "track":
                show chelsea confused
                pcname "Real mature, Alex. Fuck off."
            elif club == "cheer":
                show chelsea confused
                pcname "Don't you have any better insults to use? Slut is so outdated."
            elif club == "yearbook":
                show chelsea sad
                pcname "A-At least be original..."
            show chelsea sad
            show Damien Sad
            show Alex Happy
            "Alex smirks down at you, fully aware that he's won this argument."
        elif True:
            show Damien Sad
            show Alex Laugh
            if club == "track":
                show chelsea confused
                pcname "Is that the best you can come up with?"
            elif club == "cheer":
                show chelsea confused
                pcname "Can't be that much of a slut if I refuse to suck your dick."
            elif club == "yearbook":
                show chelsea sad
                pcname "T-That's not even true..."
        show chelsea confused
        show Damien Worry
        show Alex Happy
        "Alex leans close to you again, his lips too close to your face for comfort."
        show chelsea shocked
        show Damien Shocked
        show Alex Neutral
        "Alex" "How about we settle this after class? I can think of a few better uses for your mouth."
        show Damien Glare
        show Alex Laugh
        "He pulls away suddenly, his laughter cruel and arrogant. Your face burns as you glare up at him, embarrassed by his suggestion."
        show Damien Blank
        show chelsea blank
        "Alex opens his mouth to say something else, but one of the homeroom teachers walks by, eyeing Alex with suspicion. You can only assume you aren't the first girl he's harassed."
        show chelsea shocked
        show Damien Shocked
        show Alex Neutral
        "Alex" "Guess we'll need to settle this another time. I vote we do it on your back."
        show chelsea confused
        show Damien Glare
        show Alex Happy
        "Alex winks at you and gives Damien an arrogant, shit-eating grin before he walks back to his table."
        hide Alex Happy with moveoutleft
        show chelsea blank
        "Glancing back at your boyfriend, you see that Damien's body is trembling, anger and shame evident on his face."
        show chelsea sad
        pcname "Damien..."
    show Damien Angry
    show chelsea shocked
    D "I {i}hate{/i} them: Alex, his friends, that whole group. They think they can get away with whatever they want."
    show Damien Glare
    "You're surprised by the anger on Damien's face, something you rarely see with his shy, down-to-earth attitude."
    show chelsea sad
    D "He should have never talked to you that way. I'm used to him picking fights with me, but things are different now."
    show Damien Neutral
    show chelsea embarrassed
    D "I really like you, [pcname]. I feel... I feel close to you in a way I've never felt with any other girl."
    show Damien Worry
    D "I want to protect you at all costs."
    show chelsea sad
    show Damien Blank
    "You can't help but feel touched by Damien's declaration, and a little saddened by it as well."
    "Has Damien always suffered from such intense bullying? What else have people like Alex done to him over the years?"
    menu damien_alexcomments:
        "People will say those things anyway." if True:
            show chelsea blank
            "Even so, although what Alex said to you isn't right, there is no point in trying to hold a grudge over it."
            "People are going to say what they want about you regardless, so it's best not to get too hung up on it."
            show chelsea sad
            show Damien Worry
            pcname "It's okay, Damien. Let's just let it go."
            show Damien Shocked
            D "You're okay with it?"
            show chelsea confused
            show Damien Blank
            pcname "I wouldn't say I'm {i}okay{/i} with it..."
            show Damien Worry
            show chelsea blank
            pcname "But I'll drive myself crazy if I hold onto all of the mean things people say to me."
            show Damien Glare
            D "Do people say mean things to you often?"
            show Damien Blank
            show chelsea sad
            pcname "Well, not all the time... But it does happen."
            show chelsea blank
            pcname "I just need to learn to let it go and not put so much stock into what people say."
            show Damien Sad
            show chelsea sad
            D "...I guess... But he shouldn't speak to you like that, anyway..."
        "I don't like how I'm treated." if True:
            show chelsea sad
            "Hearing all of the sexist, objectifying things Alex had to say to you, there's no doubt it has taken a hit to your self-esteem."
            "It's not fair that he can get away with calling you a slut and suggesting he has the right to fuck you."
            show chelsea confused
            show Damien Sad
            pcname "I don't want him to treat me like that, either."
            show chelsea sad
            pcname "I wish people didn't harass me because of what I look like. It makes me feel embarrassed to be in this body..."
            show Damien Shocked
            show chelsea embarrassed
            D "You shouldn't feel embarrassed, [pcname]. You look wonderful."
            show Damien Angry
            show chelsea sad
            D "I just hate people that objectify that and think they can get away with it."
            show Damien Sad
            D "I'm sorry you had to go through that."
    show Damien Blank
    show chelsea blank
    "With a sigh, you and Damien finish off the rest of our meals, moving on in conversation."
    scene black with dissolve
    pause 0.5
    show bg Cafeteria with dissolve
    show chelsea blank at right with dissolve
    "As lunch comes to an end, Damien picks up both of your trays in an offer to clean up."
    show Damien Neutral at left with moveinleft
    D "Hey, uh, I was thinking we could go to the aquarium this weekend, by the way. Go out around the city a little."
    show chelsea laugh
    pcname "Oh yeah? That sounds great!"
    show Damien Happy
    D "Cool! I'll uh, pick you up at noon then. We can text about it to finalize everything."
    show chelsea happy
    show Damien Blank
    "You smile at him and follow Damien out into the hall."
    show chelsea laugh
    pcname "It's a date."
    show chelsea happy
    show Damien Happy
    "Damien grins, thrilled, and the two of you walk back to class."
    hide chelsea with dissolve
    hide Damien Happy with dissolve
    jump events_end_period

label damien_aquarium:
    show bg black with dissolve
    $ DamienAngry = "Characters/Damien/Casual 2/Angry.png"
    $ DamienBlank = "Characters/Damien/Casual 2/Blank.png"
    $ DamienGlare = "Characters/Damien/Casual 2/Glaring.png"
    $ DamienLaugh = "Characters/Damien/Casual 2/Laughing.png"
    $ DamienNeutral = "Characters/Damien/Casual 2/Neutral.png"
    $ DamienSad = "Characters/Damien/Casual 2/Sad.png"
    $ DamienShocked = "Characters/Damien/Casual 2/Shocked.png"
    $ DamienSmiling = "Characters/Damien/Casual 2/Smiling.png"
    $ DamienWorrying = "Characters/Damien/Casual 2/Worrying.png"
    show bg CityD with dissolve
    "Damien picks you up for your date at twelve o'clock sharp, driving you further into town until you come across a large dome-like building made of thick, sturdy glass."
    $ clothes, hair = casualwear
    "When he promised to take you to the aquarium, you had expected a little side exhibit at the zoo: not {i}this.{/i}"
    show chelsea shocked at right with moveinright
    show Damien Happy at left with moveinleft
    pcname "This place is huge!"
    show chelsea blank
    D "You like it? My mom used to take me here all the time when I was a kid. The exhibits are pretty much the same, but they get new animals every year."
    show Damien Neutral
    D "Have you ever been to an aquarium before?"
    show chelsea shocked
    pcname "No, not really. I've been to small aquarium exhibits at the zoo, but nothing like this."
    show Damien Happy
    show chelsea happy
    D "Really? Awesome! We can really take our time here then so you get the full experience."
    show bg black with dissolve
    pause 0.5
    show bg CityD with dissolve
    show Damien Blank
    "Once Damien parks, you follow him inside to pick up your tickets."
    hide Damien Blank with moveoutleft
    show chelsea shocked
    pcname "Whoa..."
    "Somehow, the aquarium is even bigger on the inside than it was outside. Various blue signs with different sea creatures painted on show off a variety of exhibits and dining options, each one pointing in a different direction."
    "There are escalators going up another two floors with overlooks into the main lobby. The first exhibit sits in the middle: a giant tubular tank filled with jellyfish."
    show Damien Happy at left with moveinleft
    "You don't realize that you're staring in awe until Damien comes up beside you, pulling you back to the present."
    show chelsea happy
    D "It's really beautiful, isn't it? I bet it's a lot to take in for your first time here. I always forget how pretty it looks until I come back."
    show Damien Neutral
    show chelsea shocked
    D "They have some internship programs here that I might apply to once we graduate."
    show Damien Laugh
    show chelsea blank
    D "Well, first I need to get into veterinary school, but it's always good to look ahead!"
    show chelsea happy
    show Damien Blank
    pcname "I think that's a great idea. Working close to animals like this would really suit you."
    show Damien Happy
    show chelsea blank
    "Damien smiles, a wistful look in his eyes as he admires the aquarium lobby."
    D "Yeah..."
    show Damien Laugh
    show chelsea happy
    D "So, what exhibit do you want to look at first?"
    $ damienexhibit1 = True
    menu damien_aqexhibit1:
        "The sea turtles!" if True:
            jump damien_aqseaturtles
        "The sea otters!" if True:
            jump damien_aqseaotters
        "The sharks!" if True:
            jump damien_aqsharks
        "The penguins!" if True:
            jump damien_aqpenguins
        "The octopus!" if True:
            jump damien_aqoctopus

label damien_aqseaturtles:
    show chelsea happy
    show Damien Happy
    if club == "track":
        "Turtle shells are hard and tough, a natural barrier to any predator that tries to take a bite out of them."
        "You like to think of yourself the same way."
        show chelsea laugh
        pcname "The sea turtles, man! Their shells can take on anything."
        show chelsea happy
        show Damien Laugh
        D "Aren't they so cool? Let's go see them!"
    elif club == "cheer":
        "There's something admirable about an animal that's whole home is a part of its body. It's a free spirit, ready to roam the world at a moment's notice."
        "Not to mention, sea turtles are just adorable."
        pcname "Definitely the sea turtles. Have you seen the videos of those little baby turtles walking out to sea once they hatch? It's so cute!"
        show Damien Laugh
        D "I love those videos! Let's check them out."
    elif club == "yearbook":
        "Growing up, you always wished you could shrink back into your shell like the turtles in the cartoons."
        "You know that it's not an accurate depiction now, but you still feel like you can relate to them the most out of all the sea life out there."
        show chelsea embarrassed
        pcname "I-I'd like to see the sea turtles, if that's okay..."
        show Damien Laugh
        D "Definitely! Let's go check them out."
    "You both follow the signs for the sea turtle exhibit, the path painted with little white turtle shells to lead the way."
    hide chelsea with moveoutleft
    hide Damien Laugh with moveoutleft
    show bg black with dissolve
    pause 0.5
    show bg CityD with dissolve
    show chelsea shocked at right with moveinright
    show Damien Happy at left with moveinright
    "You find yourselves surrounded by an array of glass tanks stretching up at least two stories high and filled to the brim with sea life."
    show chelsea happy
    "Coral sways at the bottom while you both approach the first tank, searching for the turtles in question."
    show chelsea confused
    show Damien Blank
    "Damien makes his way over to a description plaque as you continue to search the first tank, disappointed and confused at the severe lack of turtles."
    show Damien Happy
    show chelsea sad
    D "It says here that her name is Pearl, she's a Green sea turtle, and she's a rescue from the ocean."
    show chelsea confused
    pcname "But where {i}is{/i} she? I don't see her anywhere."
    show Damien Sad
    "Damien peers into the tank with a frown."
    D "I don't either..."
    show Damien Shocked
    D "Ah, wait a sec! Take a look back there."
    show chelsea blank
    show Damien Worry
    "You lean against the glass and squint into the water, trying to see past the various oceanic structures that obscure your view."
    show chelsea shocked
    show Damien Shocked
    "There it is!"
    show Damien Happy
    show chelsea happy
    "Floating peacefully along the back wall is a large sea turtle, her back to you as she glides across her tank. She paces back and forth on her side, one fin flapping wildly to push her around."
    show chelsea shocked
    "As Pearl finally floats closer, you realize why she's swimming so funny."
    show chelsea sad
    show Damien Shocked
    pcname "She only has three fins..."
    show Damien Sad
    D "Oh, yeah. I guess she does. Poor thing..."
    show Damien Neutral
    show chelsea blank
    D "It says here that they're working on building her a prosthetic, though. I guess she's still new to the aquarium."
    show chelsea shocked
    show Damien Shocked
    "Aquarium Employee" "Yes, Pearl is quite new."
    show chelsea blank
    show Damien Blank
    "An elderly employee with a blue ID badge shuffles up to you, relying heavily on her cane as she approaches the tank. She smiles at the turtle through the glass, like a mother watching her child play."
    "Aquarium Employee" "She's still getting used to her exhibit here. I think she's a little shy."
    "Aquarium Employee" "Is this your first time visiting?"
    show Damien Happy
    show chelsea embarrassed
    D "Ah, it's [pcname]'s, but I've been here plenty of times."
    show chelsea blank
    "Aquarium Employee" "Welcome back."
    show Damien Blank
    "Aquarium Employee" "You know, you made it just in time for one of our seminars. We're about to feed one of our long-time residents, Bubble. Would you like to come see?"
    if damienconfidence >= 50:
        show Damien Happy
        "Damien's eyes light up at the suggestion and he nods eagerly."
        D "That sounds great! What do you say, [pcname]? Are you up for it?"
    elif True:
        show Damien Happy
        "Damien looks excited by the suggestion, but quickly looks to you for a response, clearly waiting for you to make the decision."
        D "Well, um, what would you like to do, [pcname]?"
    menu damien_aqturtlefeed:
        "Yes!" if True:
            if club == "track":
                show chelsea laugh
                pcname "Hell yeah! Do we get to feed them ourselves?"
                show chelsea happy
                "The woman chuckles."
                show chelsea sad
                "Aquarium Employee" "No, unfortunately not, but it's a fun little event."
            elif club == "cheer":
                show chelsea laugh
                pcname "That sounds so cute! I'd love to see it!"
            elif club == "yearbook":
                show chelsea laugh
                pcname "Y-Yes please!"
                show Damien Shocked
                show chelsea shocked
                "Damien glances at you, surprised by your excitement. You feel your cheeks heat up and glance away, embarrassed by your eager response."
                show chelsea embarrassed
                show Damien Happy
                pcname "I-I mean, that... that sounds like fun..."
                "The old woman chuckles."
            show Damien Blank
            show chelsea blank
            "Aquarium Employee" "It'll start in a minute or two, so you better hurry. Just walk around the corner here; you'll see the sign out front."
            show Damien Happy
            show chelsea happy
            D "Sounds easy enough. Thank you!"
            "Taking your hand in his, Damien leads you around the corner to another section of the exhibit."

            scene bg DADS1 with dissolve
            "The next tank is much lower-- low enough for you to reach in if you aren't careful-- with a wooden platform in the back for the employees."
            "A younger employee stands on top of the platform as a large Loggerhead turtle, Bubble, splashes around in the water beneath her, racing back and forth to greet the small audience surrounding its tank."
            "You and Damien find a spot along the side of the tank and watch as the performance begins."
            "Aquarium Employee 2" "Hey everyone! How are we doing today?"
            "Various positive responses ring out and blend together. The employee smiles, nodding along."
            "Aquarium Employee 2" "That's great to hear! My name is Tamir and today we have one of my best friends in the world, Bubbles! Everyone say 'hi, Bubbles!'"
            "Everyone responds in unison, some of the younger audience jumping up and down excitedly as the turtle swims their way."
            "Tamir" "Bubble has been with us for twenty years, which seems like a really long time to some of you, but Loggerheads typically live seventy to eighty years or more in captivity, which is thirty more years than their lifespans in the wild."
            show bg DADS2 with dissolve
            "He tosses a small crab into the water, which Bubble immediately dives for, her jaws cracking into the shell."
            "Tamir" "Now, Bubble here is a carnivore, so her primary diet is stuff like crab, fish, anything that these big jaws can crunch into."
            "The show continues on with Tamir describing facts about Bubble and her diet as he feeds her from a tin bucket."
            "By the end of the feeding, you remember more information about this one Loggerhead turtle than half the things you were taught in your science class."

            show black with dissolve
            show Damien Happy
            show chelsea happy at midright with dissolve
            "Damien smiles down at you, his thumb stroking over your knuckles as you leave the tank."
            hide chelsea with moveoutleft
            hide Damien Happy with moveoutleft
            show bg black with dissolve
        "No thanks." if True:
            if club == "track":
                show chelsea confused
                "As cute as the turtles are, you aren't sure if you're interested in watching them eat."
                show chelsea sad
                pcname "{i}Besides, it will probably be crowded.{/i}"
                show chelsea confused
                show Damien Shocked
                pcname "Nah, I'm ready to move on."
            elif club == "cheer":
                show chelsea confused
                "Turtles are fun to watch for a little bit, but you've had your fill now."
                show Damien Shocked
                pcname "Mmm... No thanks. I'm over turtles now."
                show chelsea laugh
                show Damien Sad
                pcname "Let's find something even cuter to look at!"
            elif club == "yearbook":
                show chelsea sad
                "You're not really sure what's in a sea turtle's diet, but knowing how sharp some of their jaws can be, you'd rather not see one tear into a poor sea creature."
                show Damien Sad
                pcname "I-I think I'd rather to go the next exhibit..."
            "Damien frowns, his disappointment evident, but he nods."
            show Damien Neutral
            D "O-Oh... Okay. Whatever you want, [pcname]."
            "With a wave goodbye to the employee, Damien takes your hand in his and moves onto the next exhibit."
            hide chelsea with moveoutleft
            hide Damien Blank with moveoutleft
            show bg black with dissolve
if damienexhibit2 == False:
    $ damienexhibit1T=True
    jump damien_exhibitchoice2
if damienexhibit2 == True:
    $ damienexhibit2T=True
    jump damien_exhibitchoice3
if damienexhibit3 == True:
    jump damien_enddate

label damien_aqseaotters:
    if club == "track":
        show chelsea happy
        "There's something to be said about a sea creature that's clever enough to use tools to eat its food, and if you're lucky, you'll get to see it in action today!"
        show chelsea laugh
        pcname "Let's check out the sea otters! They're some clever little shits."
    elif club == "cheer":
        show chelsea happy
        "You don't know much about sea otters, but you've watched enough videos of them holding hands while they sleep to know how adorable they are, and that's enough for you."
        pcname "Is that even a question? The sea otters, of course! They're so freakin' cute!"
    elif club == "yearbook":
        show chelsea blank
        "Sea otters are pretty social creatures-- the exact opposite of yourself-- but there's something to admire about their close-knit community."
        show chelsea embarrassed
        pcname "I-I think I'd really like to see the sea otters..."
    show Damien Happy
    "Damien's face lights up with excitement, a bright smile stretching across his face."
    show Damien Laugh
    show chelsea happy
    D "Awesome! The sea otters are my favorite."
    show Damien Happy
    "You follow him down a path covered in painted otter footprints to a large tank near the back."
    scene bg DADS3 with dissolve

    "Half of the exhibit is underwater while the other half stretches up on dry land, a small water slide extending down for the otters to play in."
    "You watch as the little furry critters run up in a line and take turns down the slide, splashing with ease into the tank and chasing each other back up to the top to do it again."
    "This is even cuter than you imagined."
    "You and Damien take a moment to admire the creatures, smiling as they hop in and out of the water, splashing each other as they run up and down their slide."
    D "You know, I used to have a stuffed sea otter as a little kid; it was a souvenir from my first trip here."
    D "I named it Happy, because the sea otters looked so happy running around. I used to wish I could jump in their tank and run around with them."
    D "Did you have a toy like that as a kid?"

    menu damien_aqtoy:
        "A stuffed dinosaur." if True:
            show bg black with dissolve
            if club == "track":
                pcname "Oh yeah, I used to have a stuffed t-rex that I'd carry around everywhere."
                show chelsea confused at midright with dissolve
                pcname "I'm pretty sure my old dog bit its head off, though."
                show Damien Laugh
                show chelsea happy
                D "Ouch! Haha. That's really cool."
            elif club == "cheer":
                show chelsea embarrassed at midright with dissolve
                show Damien Shocked
                pcname "Yeah, it's kind of lame, but I had a t-rex that I was like, obsessed with."
                show chelsea laugh
                show Damien Happy
                pcname "It had sparkles and everything, so I was kind of a sucker for it."
                show Damien Laugh
                D "That's not lame. It sounds really cute!"
            elif club == "yearbook":
                show chelsea embarrassed at midright with dissolve
                pcname "W-Well, there was a dinosaur I liked... I named him Stuffy..."
                show Damien Happy
                D "Aw, that's really cute, [pcname]."
        "A doll." if True:
            show bg black with dissolve
            if club == "track":
                show chelsea embarrassed at midright with dissolve
                show Damien Shocked
                pcname "Ugh, it's so lame, but I had one of those Uni Girls growing up. You know, the historical ones with all the books?"
                show chelsea confused
                pcname "I think mine was from one of the wars or whatever. She had like, a red cross packet or something."
                show Damien Neutral
                show chelsea happy
                D "Oh, that's really cool! My cousin used to have one of those. I think hers was from the turn of the century, though."
            elif club == "cheer":
                show chelsea happy at midright with dissolve
                show Damien Happy
                pcname "Oh, you know, I had one of those Uni Girls that like, every girl had. She was from the turn of the century."
                show chelsea laugh
                pcname "I remember getting her for my birthday. She came with her own petticoat and everything!"
                show Damien Neutral
                show chelsea happy
                D "Oh yeah. My cousin had that one. She used to make me play tea parties with her and her doll."
            elif club == "yearbook":
                show chelsea embarrassed at midright with dissolve
                show Damien Happy
                pcname "W-Well, I had a Uni Girls doll... They were really popular when I was little."
                show chelsea sad
                show Damien Sad
                pcname "I-I think mine was from the Great Depression..."
                show chelsea embarrassed
                show Damien Neutral
                D "Oh yeah... I remember those. My cousin's was from the turn of the century, I think."
        "A toy truck." if True:
            show bg black with dissolve
            if club == "track":
                show Damien Blank
                show chelsea laugh at midright with dissolve
                pcname "Yeah, I actually had a toy truck that I used to go to sleep with every night."
                show Damien Shocked
                show chelsea happy
                D "A toy truck?"
                show Damien Laugh
                show chelsea shocked
                D "I don't even know why I'm surprised. That's totally in line for you."
                show Damien Happy
                show chelsea happy
                pcname "Really? I guess I was always sort of a tomboy."
            elif club == "cheer":
                show chelsea sad at midright with dissolve
                show Damien Blank
                pcname "Yeah, but it's kind of embarrassing..."
                show Damien Shocked
                show chelsea laugh
                pcname "I used to have a toy truck as a kid. I was totally obsessed with it, but looking back, I have no idea why!"
                show chelsea embarrassed
                show Damien Happy
                pcname "I guess it was just one of those weird kid things you latch onto for a while before you move onto something else."
                show Damien Laugh
                show chelsea happy
                D "I don't think that's embarrassing. Kids are always getting into some weird trends."
                show chelsea shocked
                show Damien Neutral
                D "When I was little, apparently I was obsessed with lawn mower commercials. All I wanted to do was mow the lawn."
                show Damien Laugh
                show chelsea laugh
                D "I bet my dad wishes that were the case now, heh."
            elif club == "yearbook":
                show chelsea embarrassed at midright with dissolve
                show Damien Blank
                pcname "W-Well, sort off..."
                show Damien Shocked
                pcname "It wasn't an animal, but I had a toy truck I really liked..."
                show chelsea shocked
                D "A toy truck?"
                show chelsea sad
                show Damien Blank
                pcname "W-Well-- um-- yes... I know that's not really normal..."
                show Damien Happy
                show chelsea sad
                D "It doesn't have to be normal, you know. Kids are always into pretty weird stuff."
                show Damien Laugh
                show chelsea shocked
                D "I think it's really cool."
                pcname "Ah, really?"
                show chelsea embarrassed
                show Damien Happy
                D "Yeah."
    show Damien Happy
    show chelsea happy
    "Damien smiles at you before looking back at the tank, watching the little sea otters tumble down the slide."
    show Damien Neutral
    show chelsea blank
    D "So there are five of them in here-- Judy, Tuppins, Lionel, Fudge, and Coconut-- but I can't tell which is which."
    show Damien Blank
    "Damien reads off their names from a plaque attached to the tank, grinning to himself as he reads over various sea otter facts listed underneath."
    show chelsea happy
    "The otters speed up and down the water slide, occasionally pushing past each other to slide down first."
    show Damien Shocked
    D "Oh! And it looks like they have two new pups, too."
    if club == "track":
        show chelsea happy
        pcname "Oh, sweet! Baby otters!"
        show chelsea sad
        "You search through the exhibit, but all you see are the five adult sea otters playing around."
        show chelsea confused
        pcname "Where are they?"
    elif club == "cheer":
        show chelsea shocked
        show Damien Shocked
        "You gasp, the noise followed by an excited squeal as you grin and search through the exhibit."
        show chelsea laugh
        pcname "Oh em GEE! Where?!"
        show Damien Happy
        "Damien chuckles, continuing to read the plaque."
    elif club == "yearbook":
        show chelsea embarrassed
        pcname "Aww... T-That sounds really cute..."
        show chelsea sad
        pcname "But I don't see them anywhere..."
    show Damien Happy
    show chelsea sad
    D "They were just born so they aren't out yet, but they have a contest running to name one of them."
    show Damien Laugh
    show chelsea blank
    D "What do you say? Should we try it out?"
    menu damien_aqottername:
        "Name the Otter" if True:
            show chelsea happy
            show Damien Blank
            "Of course you can't pass up the opportunity to name one of these cute creatures!"
            show chelsea laugh
            pcname "Yeah, let's do it!"
            show Damien Happy
            show chelsea happy
            "Damien grins and walks over to a nearby table, passing you a pencil and one of the forms."
            D "Hmm... I think I'd name one Salacia, after Neptune's consort."
            show Damien Neutral
            show chelsea shocked
            D "What about you, [pcname]?"
            show chelsea confused
            "You tap the pencil to your chin and think it over."
            $ seaottername = renpy.input("What would you like to name the sea otter?", default="Neptune", length=12)
            $ renpy.pause
            $ seaottername = seaottername.strip()
            if seaottername == "":
                $ seaottername = "Neptune"
            show chelsea laugh
            show Damien Shocked
            pcname "[seaotter]."
            show Damien Laugh
            show chelsea happy
            D "That's perfect, [pcname]! Salacia and [seaottername]... They kind of go together, don't you think?"
            show Damien Happy
            "Once you're both finished writing down your names and information, Damien takes the sheets of paper and puts them into the submission box before moving onto the next exhibit."
            $ seotname = True
            hide chelsea with moveoutleft
            hide Damien Happy with moveoutleft
            show bg black with dissolve
        "Don't name the otter." if True:
            if club == "track":
                show chelsea blank
                "As tempting as it is to win a sweepstakes like that, you can't think of a good enough name for the sea otter, and you'd rather it not live with something lame for the rest of its life."
                show chelsea confused
                show Damien Shocked
                pcname "Nah, I think I'm good. Let's go check out the next exhibit."
                show Damien Sad
                show chelsea blank
                D "O-Oh. Er, okay..."
            elif club == "cheer":
                show chelsea confused
                show Damien Shocked
                pcname "Isn't that whole thing kind of... you know... childish?"
                show Damien Neutral
                pcname "I'd rather do something else."
                show chelsea blank
                show Damien Sad
                D "O-Oh... Yeah, I guess it is..."
            elif club == "yearbook":
                show chelsea sad
                "You don't feel really confident about winning the contest, and you would rather not get your hopes up by trying."
                pcname "I-I think I'm good..."
                show Damien Shocked
                D "Really? Are you sure?"
                pcname "Yeah... Thank you, though..."
                show Damien Sad
                D "Well, okay. If you're sure, [pcname]."
            show Damien Worry
            "Damien looks at the sweepstakes advertisement one more time before shrugging it off and moving onto the next exhibit."
            hide chelsea with moveoutleft
            hide Damien Worry with moveoutleft
            show bg black with dissolve
    if damienexhibit2 == False:
        $ damienexhibit1SO=True
        jump damien_exhibitchoice2
    if damienexhibit2 == True:
        $ damienexhibit2SO=True
        jump damien_exhibitchoice3
    if damienexhibit3 == True:
        jump damien_enddate

label damien_aqsharks:
    if club == "track":
        show chelsea happy
        "The most metal animal in any aquarium has to be the sharks. Their raw, savage energy gets you excited!"
        show chelsea laugh
        show Damien Shocked
        pcname "Let's check out the sharks! They're so cool!"
    elif club == "cheer":
        show chelsea blank
        show Damien Worry
        "You notice how Damien glances nervously toward the shark sign, as though begging you not to choose it."
        show chelsea happy
        "Smirking, you lean into him and pretend to take a bite of his neck."
        show Damien Shocked
        D "W-What was that for?!"
        show chelsea happy
        pcname "I want to see the sharks."
    elif club == "yearbook":
        show chelsea embarrassed
        "Despite their bad reputation, you know that sharks are actually pretty tame and cool and that most accidents with them are... well, accidents."
        pcname "I-I'd like to see the sharks, if that's alright..."
        show Damien Shocked
        show chelsea sad
        D "Ah, really? I didn't think you would be into that sort of thing..."
    show Damien Sad
    "Damien pales a little, but forces a smile and nods."
    show Damien Happy
    show chelsea happy
    D "If that's what you want to do... sure."
    show Damien Blank
    "You take Damien's hand in yours and lead him down the wave-themed tunnel near the back of the building, pretending not to notice how his grip tightens on yours as the lights dim."
    hide chelsea with moveoutleft
    hide Damien Blank with moveoutleft
    show bg black with dissolve
    pause 0.5
    show bg CityD with dissolve
    show chelsea shocked at right with moveinright
    show Damien Shocked at left with moveinright
    pcname "Whoa..."
    show chelsea happy
    "You find yourselves in what feels like a glass-protected bubble, the rippling water of the tank around you reflecting down on the blue carpet floor."
    "Sharks of all shapes and sizes swim above and beside you, some of them gliding close to the glass while others are spread out further in the tank."
    show chelsea confused
    "As you take a step further, you notice that Damien has all but frozen beside you."
    show chelsea sad
    pcname "Are you okay, Damien?"
    show chelsea blank
    if damienconfidence >= 50:
        show Damien Happy
        D "Yeah, totally..."
    elif True:
        show Damien Neutral
        D "Y-Yeah, never better."
    show Damien Shocked
    "But the look he gives the sharks is one of pure terror."
    if club == "track":
        show chelsea happy
        pcname "Oh, come on. You aren't {i}scared{/i} of these things, are you? They're behind a glass wall!"
    elif club == "cheer":
        show chelsea happy
        "You smirk at him, unable to resist teasing."
        pcname "Aww, are you scared of some little fishies, Damien?"
    elif club == "yearbook":
        show chelsea embarrassed
        pcname "A-Are you scared, Damien? It's okay if you are..."
    if damienconfidence >= 50:
        show Damien Neutral
        show chelsea sad
        D "Er, well... Sharks kind of creep me out, if I'm being honest with you."
        show Damien Happy
        show chelsea blank
        D "But it's okay. I'll be fine. Enjoy the exhibit."
    elif True:
        show Damien Shocked
        show chelsea blank
        "He shakes his head abruptly, completely in denial."
        D "N-No, of course not! I-I... I just..."
        show Damien Sad
        show chelsea sad
        "His face tells you everything."
    show chelsea sad
    "Before you can suggest leaving the exhibit early, a fit employee in his thirties with a blue badge approaches you."
    show Damien Blank
    show chelsea blank
    "Diving Instructor" "Hey, guys! Date night?"
    show chelsea happy
    show Damien Happy
    pcname "Yeah."
    "Diving Instructor" "Excellent! Well, hey, are you both over eighteen?"
    show chelsea blank
    show Damien Blank
    "You both nod."
    show chelsea shocked
    show Damien Shocked
    "Diving Instructor" "Perfect! We're offering our last session of diving with sharks for the day. It would be $200 for the two of you, so I get it's a little pricy, but it's a once-in-a-lifetime opportunity to swim around with our little baddies here."
    show Damien Sad
    show chelsea blank
    "The man pats the glass tank with a smile, his grin as sharp as the sharks' inside."
    show Damien Shocked
    "Damien's eyes go wide and, even in the pale blue light, you can see that his skin is ashen."
    if damienconfidence >= 50:
        D "But-- er-- aren't those wild animals?"
        show chelsea happy
        pcname "What's scarier, Damien? Me or the sharks?"
        "You wink at him, hoping that it'll put him at ease, but he doesn't dare look away from the tank."
    elif True:
        "Damien stares in horror at the tank, unable to look away from the various pointed teeth that pass by."
        D "T-They aren't going to eat me...?"
    show chelsea happy
    "Diving Instructor" "Oh, these boys here wouldn't hurt a fly. Well, haha, maybe I shouldn't say that..."
    show Damien Worry
    show chelsea shocked
    "Diving Instructor" "They won't hurt you a bit, though. We have our more deadly sharks in another tank, but these ones are non-aggressive."
    show chelsea blank
    show Damien Sad
    "Diving Instructor" "So, what do you say? Are you interested?"
    menu damien_aqsharkswim:
        "Let's do it! ($200)" if True:
            $ corruption -= 5
            $ Cash -=200
            if club == "track":
                show chelsea happy
                "You stare up at the shark tank with the excitement of a child in a candy store. How many people get to say they've swum with sharks?!"
                show chelsea laugh
                show Damien Shocked
                pcname "Hell yeah we are! Let's do this!"
            elif club == "cheer":
                show chelsea happy
                "Glancing at Damien, you feel even more inclined to drag him along into this. The boy needs to learn to live a little!"
                "Besides, what other girl on the cheer squad will get to say she's swum with sharks?"
                show chelsea laugh
                show Damien Shocked
                pcname "We'll do it!"
            elif club == "yearbook":
                show chelsea embarrassed
                "Knowing how non-aggressive the sharks in the tank are make you feel a little more comfortable about the decision."
                show chelsea sad
                "You do feel bad for dragging Damien into this, but how often do you get the chance to swim with sharks?"
                show Damien Shocked
                show chelsea embarrassed
                pcname "I-I'd like to do it."
            show Damien Worry
            "Damien looks at you skeptically, obviously wishing to say otherwise, but he gives a slow nod."
            show Damien Sad
            show chelsea happy
            D "If that's what she wants..."
            "Diving Instructor" "Excellent! Come with me, I have a few forms for you to fill out, and then we can get you into your scuba gear!"
            show chelsea laugh
            pcname "Fun!"
            show chelsea happy
            show Damien Worry
            D "...Yay..."
            hide chelsea with moveoutleft
            hide Damien Worry with moveoutleft
            show bg black with dissolve
            pause 0.5
            show bg CityD with dissolve
            show chelsea happy at right with moveinright
            show Damien Sad at left with moveinright
            "You, Damien, and two other couples stand at the edge of the enormous shark tank, fully dressed in your scuba diving gear."
            show Damien Shocked
            show chelsea blank
            "Although you expected Damien to give you nervous glances, it seems that he can't take his eyes off of the sharks inside, without a doubt terrified of the swirling sea creatures within."
            show chelsea happy
            show Damien Sad
            "The forms were signed, the money paid, and the instructions given: all you have to do now is get in."
            show chelsea blank
            "Diving Instructor" "Alright, folks, follow my lead! Again, you have one hour, and then we're coming back up here!"
            "Diving Instructor" "Ready? Go!"
            "The instructor lowers himself into the tank, and the rest of you follow behind."
            show Damien Shocked
            show chelsea confused
            "Damien freezes up in front of you, continuing to stare at the tank, before he realizes it's his turn."
            show chelsea happy
            show Damien Worry
            "Taking a deep breath, Damien lowers himself into the tank, and you climb in after him."
            show chelsea shocked
            pcname "{i}Wow...{/i}"
            scene bg DADS4 with dissolve

            "Everything looks so much different in the tank compared to the aquarium floor."
            "You have a better perspective of what the tank looks like from the inside as you gently float through the water, brushing past the walls of live coral and school of fish."
            "Slowly, you swim through the water, tensing up a little with shock as the occasional sea creature brushes against your legs or side."
            "The sharks don't seem to mind you at all-- they must be used to this, considering how many diving sessions are held each day-- but as you peek over at Damien, he is keeping a safe distance from the rest of the creatures."
            "A part of you feels a little bad for dragging him in here, but as a couple of sharks swim right by you without so much as a glance in your direction, excitement flutters in your chest."
            "This may be the coolest thing you've ever done, and you would hate for Damien to miss out."
            "You make your way over to him and slip his hand in yours, tugging him out to the center of the tank."
            "Damien's eyes widen behind his goggles, clearly horrified at the idea, but he makes no move to reject you. Carefully, he pushes away from the wall, his fingers tightly gripping yours."
            "You swim together through the tank, slowly floating through the water and past the vibrant aquatic life inside."
            "As you make your rounds, Damien seems to relax at your side, and although he tenses up when a shark passes by, he doesn't swim away. You count that as a win."
            "Before you know it, your hour is up, and it's time to head back to land and get changed."
            show bg black with dissolve
            show chelsea blank at right with moveinright
            show Damien Sad at left with moveinright
            "You and Damien walk back into the bubble-like room, dry and safe from the sharks inside."
            show chelsea happy
            pcname "Well? What did you think?"
            show Damien Sad
            "Damien hesitates for a moment, peering back up through the tank."
            if damienconfidence >= 50:
                show Damien Neutral
                show chelsea blank
                D "It was... different. I don't think I'd never do it again, but thanks for making me give it a shot."
                show Damien Happy
                show chelsea happy
                D "I had a good time, [pcname]."
            elif True:
                show Damien Worry
                D "...Do I ever have to do it again?"
                show chelsea happy
                pcname "No."
                show Damien Shocked
                show chelsea laugh
                D "Good. I almost peed myself."
                show chelsea happy
                show Damien Happy
                D "B-But it was nice to have you with me, at least..."
            show Damien Worry
            "Taking your hand, Damien is eager to leave the shark tank, and this time you don't stop him."
            hide chelsea with moveoutleft
            hide Damien Worry with moveoutleft
            show bg black with dissolve
        "Pass." if True:
            if club == "track":
                show chelsea sad
                "Looking at how terrified Damien is, you can't bring yourself to drag him into the shark tank, even if it would be the adventure of a lifetime."
                show Damien Shocked
                pcname "...No, I think we'll pass."
            elif club == "cheer":
                show chelsea sad
                "As cool as you would be swimming with sharks, you notice just how scared Damien looks and feel bad about the idea of dragging him in there."
                "You definitely wouldn't want {i}him{/i} dragging you to something you hated."
                show Damien Shocked
                show chelsea laugh
                pcname "Sorry! We're actually going to check out another exhibit now!"
            elif club == "yearbook":
                show chelsea sad
                "Looking between Damien's terrified gaze and the shark tank itself, you're glad that you aren't the only one feeling nervous about the whole thing."
                show Damien Blank
                pcname "N-No thank you. We were just about to leave..."
            show Damien Blank
            show chelsea sad
            "Diving Instructor" "Alright, no problem! Thanks for stopping by!"
            "The instructor waves to you before walking off to the next entering group of people, giving them his spiel as well."
            show Damien Worry
            show chelsea blank
            "Damien sighs audibly in relief and takes a shaky step away from the tank wall."
            show Damien Happy
            D "...Thanks."
            show chelsea happy
            pcname "Don't mention it. That thing is really overpriced, anyway."
            "Taking Damien's hand in yours, you move onto the next exhibit."
            hide chelsea with moveoutleft
            hide Damien Happy with moveoutleft
            show bg black with dissolve
    if damienexhibit2 == False:
        $ damienexhibit1S=True
        jump damien_exhibitchoice2
    if damienexhibit2 == True:
        $ damienexhibit2S=True
        jump damien_exhibitchoice3
    if damienexhibit3 == True:
        jump damien_enddate

label damien_aqpenguins:
    if club == "track":
        show chelsea happy
        "Although not technically a sea creature, there's no way you can pass up seeing those cool feathered birds!"
        show chelsea laugh
        pcname "Let's check out the penguins!"
    elif club == "cheer":
        show chelsea happy
        "After watching a ton of videos of little penguin parades at the zoo, the option to see them close up is too exciting to pass up!"
        show chelsea laugh
        pcname "Aww, they have penguins here, Damien! Let's go see them!"
    elif club == "yearbook":
        show chelsea shocked
        "Usually they're only an option at the zoo, but seeing a sign for the penguin exhibit, you can't resist giving them a visit!"
        show chelsea happy
        pcname "I'd like to see the penguins!"
        show chelsea embarrassed
        pcname "Um, I mean, if that's okay..."
    show Damien Happy
    "Damien smiles at you, amused by your excited response."
    show Damien Laugh
    D "Yeah, that sounds great. Let's go check them out."
    show Damien Happy
    show chelsea happy
    "Looping your arm through his, you follow Damien along a path of painted penguin footprints upstairs to a cold, winter-inspired exhibit."
    hide chelsea with moveoutleft
    hide Damien Happy with moveoutleft
    show bg black with dissolve
    pause 0.5
    show bg CityD with dissolve
    show chelsea shocked at right with moveinright
    show Damien Happy at left with moveinright
    "It's huge, with plenty of room to move around, and although the water in the tank and the exhibit itself is protected behind a thick glass wall, you can still feel the cold of the ice on the other side."
    "The whole exhibit is like an arctic wonderland..."
    "Except there are no penguins."
    show chelsea confused
    show Damien Shocked
    pcname "Huh?"
    show chelsea blank
    show Damien Blank
    "Confused, you follow Damien closer to the exhibit and peer through the glass, searching for even just one feathered friend swimming in the water."
    "Instead, you find a sign stating that the penguins have gone inside the back of their enclosure for a bath."
    show Damien Sad
    show chelsea sad
    D "Oh man... That's some really bad timing."
    "Frowning, you're about to leave the exhibit when Damien grabs your hand, pulling you back."
    show Damien Shocked
    show chelsea confused
    D "Ah, wait a sec!"
    show chelsea blank
    show Damien Neutral
    D "Did you see this?"
    show Damien Blank
    show chelsea blank
    "Damien points at a poster on the wall showing off a list of timestamps for a penguin meet-and-greet."
    show Damien Neutral
    D "There's supposed to be one in fifteen minutes. Do you want to wait here until it starts?"
    menu damien_aqpenguinmg:
        "Wait for the penguins." if True:
            $ corruption -= 5
            show chelsea happy
            "Fifteen minutes isn't a long wait at all, and if it means you get to meet a penguin, that's definitely worth it!"
            if club == "track":
                pcname "Let's wait here. We're not in any rush."
            elif club == "cheer":
                pcname "Let's stay! I beg the penguin will be super cute. I don't want to miss out on it!"
            elif club == "yearbook":
                show chelsea embarrassed
                pcname "I-I want to wait, if that's okay..."
            show Damien Happy
            D "That sounds good. Let's sit down and relax until they come out."
            show Damien Blank
            show chelsea blank
            "You and Damien find a comfortable place to sit on the floor and pull out your phones to pass the time until the meet-and-greet begins."
            hide chelsea with dissolve
            hide Damien Blank with dissolve
            show bg black with dissolve
            pause 0.5
            show bg CityD with dissolve
            show chelsea at right with dissolve
            show Damien Blank at left with dissolve
            "The penguin exhibit is much more crowded now as the meet-and-greet is about to begin, and an employee directs you and the rest of the guests into a wrapping line while you wait."
            "Loud cheers erupt as a troupe of penguins come bumbling back into their enclosure from a door inside, many dispersing to take up spots around the ground or dive into the water."
            "Little kids cry out with delight as the penguins flop in and out of the water, flopping and twirling before hopping back onto their feet and racing out to do it again."
            "The employee that directed you all stands in the center of the room, an exhausted smile on her face."
            show Damien Happy
            show chelsea happy
            "Aquarium Employee" "Alright! Is everyone ready to meet Mr. Flippers?!"
            show Damien Shocked
            show chelsea shocked
            "Screams and shrieks and cheers erupt around the room. You wince a little at the shrill noise, sharing a small smile with Damien as the children proceed to lose their shit."
            "Aquarium Employee" "Here he comes!"
            show chelsea happy
            show Damien Happy
            "Another employee with a microphone attached to her face walks out, pushing out a large wooden crate with 'LIVE ANIMAL' painted on the side."
            "Aquarium Employee 2" "Hi, everyone! I'm Kim, and this here is Mr. Flippers! I'm going to ask everyone to follow a few rules to make sure we stay safe, healthy, and friendly to our guest!"
            show chelsea blank
            show Damien Blank
            "Kim lists off a series of rules-- many of them obvious, a few that are not-- that essentially tell you not to touch the penguin, but that he will walk around and may stop in front of you."
            "Kim" "With all that, here is Mr. Flippers!"
            show Damien Laugh
            show chelsea laugh
            "Kim opens the crate and an emperor penguin waddles out like a celebrity, completely unbothered by the crowd."
            show chelsea blank
            show Damien Blank
            "The first employee allows each guest to walk up and stand with the penguin for a picture, occasionally lecturing the nearby children and reminding them not to grab for him."
            "In no time at all, it's your turn."

            scene bg DADS5 with dissolve
            "You and Damien walk up behind the penguin, watching the little creature waddle and stare up at you with curiosity."
            "It's the closest you've ever been to a penguin before-- or any bird this big-- and although it's just a small little offering at the aquarium, you can't help but feel excited."
            "Kim" "And who is this fine couple up here?"
            D "I'm Damien, and this is [pcname]."
            "Kim" "Well welcome, Damien and [pcname]! Are you ready for a picture with Mr. Flippers?"
            D "Definitely."
            pcname "Yep!"
            "Kim smiles and nods toward the camera. You feel something a little cold brush against your leg as you and Damien smile for the camera. The crowd aww's, and the camera flashes."
            "Kim" "Ha, looks like you made a friend, huh, Mr. Flippers?"
            "Looking down, you see that the penguin is snuggling against your leg. Aww indeed."
            "Kim" "Okay, Flippers! Time to say hi to our next guests! Damien, [pcname], you can step right over there and collect your photo down that hall."
            pcname "Thank you."

            show bg black with dissolve
            show Damien Happy
            show chelsea happy at midright with dissolve
            "Unable to stop yourself from grinning, you walk with Damien down the hall to another table. A man with a computer system and printer sits behind it."
            show chelsea blank
            show Damien Blank
            "Glancing at your faces, he pulls up the photo of you two and Mr. Flippers."
            show chelsea laugh
            show Damien Laugh
            "Computer Employee" "Aw, now that's cute. He doesn't always cuddle like that, you know."
            show chelsea happy
            show Damien Happy
            "Computer Employee" "Would you like to purchase the photograph?"
            menu damien_aqpenguinphoto:
                "Purchase penguin photo. ($30)" if True:
                    show Damien Blank
                    "You're not sure when you'll get to go to the aquarium again, or if you'll ever have a penguin snuggle up against your leg."
                    "This is too cute to leave without."
                    show Damien Happy
                    show chelsea laugh
                    pcname "I'll take it, please!"
                    show chelsea happy
                    "Computer Employee" "No problem!"
                    "You run your card through the machine and the employee gives you a printed copy of the photo. This is definitely a keeper!"
                "Leave without it." if True:
                    show chelsea sad
                    show Damien Blank
                    "As cute as the photo is, you can't imagine spending $30 on a single photograph."
                    if club == "track":
                        show chelsea confused
                        pcname "Uh, I'll pass, thanks."
                    elif club == "cheer":
                        show chelsea confused
                        pcname "Sorry, but I think I'm good."
                    elif club == "yearbook":
                        pcname "N-No thank you..."
                    show chelsea sad
                    show Damien Sad
                    "The guy shrugs and pulls up a photo for the next family, waving you on."
            show Damien Happy
            show chelsea blank
            D "That was fun. I've never been that close to a penguin before!"
            show chelsea happy
            pcname "Neither have I."
            "Grinning down at you, Damien takes your hand and you move onto the next exhibit."
            hide chelsea with moveoutleft
            hide Damien Happy with moveoutleft
            show bg black with dissolve
        "Move on to another exhibit." if True:
            show chelsea blank
            "Although fifteen minutes isn't a particularly long time, there's still a lot of the aquarium you haven't seen yet, and you would rather spend your time elsewhere."
            show chelsea confused
            pcname "I think I'm good... I'll just see them some other time."
            show chelsea blank
            show Damien Sad
            "Damien looks a little disappointed, but he doesn't argue."
            show Damien Blank
            "Fitting his hand with yours, you make your way to the next exhibit."
            hide chelsea with moveoutleft
            hide Damien Blank with moveoutleft
            show bg black with dissolve
    if damienexhibit2 == False:
        $ damienexhibit1P=True
        jump damien_exhibitchoice2
    if damienexhibit2 == True:
        $ damienexhibit2P=True
        jump damien_exhibitchoice3
    if damienexhibit3 == True:
        jump damien_enddate

label damien_aqoctopus:
    if club == "track":
        show chelsea happy
        "Octopuses are clever creatures that are constantly breaking out of their enclosures, and you can't help but feel admiration for their stealthy behavior."
        show chelsea laugh
        pcname "Let's go see the octopus! They're always pretty cool to look at."
    elif club == "cheer":
        show chelsea blank
        "Knowing how much of a nerd Damien is, you wouldn't be surprised if he was into some of that weird tentacle stuff you've stumbled across once in a while."
        show chelsea happy
        "This would be the perfect opportunity to tease him about it."
        pcname "How about we go look at the octopus?"
    elif club == "yearbook":
        show chelsea blank
        "Octopuses are one of the smartest creatures in the ocean, and you've always admired them for their ability to solve puzzles without the aid of others."
        show chelsea embarrassed
        pcname "C-Can we see the octopus?"
    show Damien Happy
    D "Yeah, that sounds great! Let's go check it out."
    show chelsea happy
    "Looping your arm through his, Damien leads you upstairs."
    hide chelsea with moveoutleft
    hide Damien Happy with moveoutleft
    show bg black with dissolve
    pause 0.5
    show bg CityD with dissolve
    show chelsea happy at right with moveinright
    show Damien Happy at left with moveinright
    "The cephalopod exhibit has a variety of tentacle sea creatures roaming around their various tanks, many of them lit by blue light to give you a better view."
    hide Damien Happy with moveoutleft
    show chelsea blank
    "You and Damien split up throughout the exhibit and explore, drawn to separate tanks and admiring various critters just living their daily lives."
    show chelsea shocked
    "You had no idea there were this many variation of cephalopod, but the thought that this could only be a small number of what's really in the ocean is as fascinating as it is terrifying."
    show Damien Happy at left with moveinleft
    D "Hey, [pcname], come check this out!"
    show chelsea blank
    "Damien waves you over to what must be the octopus tank based on the plaque outside, but you don't see anything inside of it."
    show chelsea confused
    show Damien Blank
    "You squint inside, searching, but you see nothing."
    pcname "What is it?"
    show Damien Neutral
    show chelsea blank
    D "Look through here."
    "Damien gently maneuvers you to the side of the tank, and you finally see what he's excited about."
    show chelsea shocked
    show Damien Happy
    "There is an octopus in there, but it's squished up inside of a little carved cave, its tentacles barely visible in the dim light of the tank."
    show chelsea confused
    "Wait... is that...?"
    pcname "Is it holding a rubix cube?"
    show Damien Laugh
    "Damien nods excitedly."
    show Damien Happy
    D "Yeah! It's trying to figure out the puzzle."
    D "Look at its tentacles go! Isn't that wild? It's figuring it out so fast. Even I'm not that good at it..."
    show chelsea embarrassed
    "At the mention of the tentacles, a million dirty jokes pop up in your mind."
    pcname "{i}I shouldn't say anything, we're in public...{/i}"
    show chelsea shocked
    show Damien Neutral
    D "That looks really hard. Wow..."
    show chelsea laugh
    pcname "...{i}But he's making this too easy!{/i}"
    menu damien_aqoctopustease:
        "Tease Damien Inappropriately." if True:
            $ corruption += 1
            if club == "track":
                show chelsea happy
                show Damien Shocked
                "Deciding not to hold back, you nudge Damien and waggle your eyebrows at him."
                pcname "I didn't think you were that into tentacles, Damien. Why don't you just get in there and let it play with you instead?"
            elif club == "cheer":
                show chelsea happy
                "Unable to resist, you lean against Damien and press your lips to his ear, whispering seductively against his skin."
                show Damien Shocked
                pcname "I never knew you had a thing for tentacles, Damien. Is that the kind of dirty stuff you're into?"
            elif club == "yearbook":
                show chelsea embarrassed
                pcname "W-Would you like something like that?"
                show Damien Neutral
                D "Like what, [pcname]?"
                pcname "A-Are you into... tentacles like that, Damien?"
                show Damien Shocked
                "Although you're just teasing, the words come out like a genuine question and you feel your face heat up as you say it aloud, the tips of your ears burning red with embarrassment."
            if damienconfidence >= 50:
                show Damien Happy
                "Damien grins down at you, a faint blush painting his cheeks. He laughs awkwardly, shrugging."
                D "Where did that come from? I didn't mean it that way..."
                show Damien Laugh
                show chelsea shocked
                D "But I wouldn't mind slipping something inside of you, if that's what you're looking for."
                if club == "track":
                    show chelsea laugh
                    "You grin up at him and laugh."
                    show chelsea happy
                    pcname "Maybe if you play your cards right, I'll think about it."
                elif club == "cheer":
                    show chelsea happy
                    "You smile coyly back up at him, twirling a piece of his hair around your finger."
                    pcname "And what do you have in mind, Damien~?"
                    show Damien Neutral
                    D "I think you know."
                    show Damien Happy
                    show chelsea laugh
                    pcname "Mmm, I'm sure I don't know what you mean~ I'll have to think {i}really{/i} hard to see if I can come up with anything."
                elif club == "yearbook":
                    show chelsea embarrassed
                    show Damien Happy
                    "Now you're definitely blushing, the blood running through your body from head to toe."
                    "You glance down nervously, unable to meet his lustful gaze."
                    show Damien Shocked
                    pcname "I-I... I might like that sometime..."
                show Damien Happy
                "Damien's grin widens and he places an arm around your waist, pulling you snug against his side."
            elif True:
                show Damien Shocked
                "Damien's face heats up and his eyes practically bulge out of his head as he glances around, making sure no one overheard you."
                show chelsea laugh
                D "T-That's not it at all! I... I didn't mean it like that..."
                if club == "track":
                    show chelsea happy
                    pcname "Aww, are you sure? And here I was, ready to get a tentacle dildo and shove it up your ass."
                    D "What?!"
                    show chelsea laugh
                    show Damien Worry
                    pcname "I'm kidding! I'm kidding!"
                    show chelsea confused
                    pcname "...Unless you're into that--"
                    show chelsea laugh
                    show Damien Shocked
                    "He pales, horrified by the idea."
                    D "No! I'm definitely not!!"
                    show chelsea laugh
                    show Damien Worry
                    pcname "Haha, okay, okay! I believe you!"
                elif club == "cheer":
                    show chelsea happy
                    pcname "Are you sure? It's okay if you meant it. Maybe I can make all your weird little fantasies come true~"
                    show Damien Worry
                    "You run your fingers up his chest, enjoying the shudder that runs through his body at your touch."
                    show chelsea laugh
                    "It's almost too easy to tease him, but you love it."
                    show Damien Shocked
                    show chelsea happy
                    pcname "But if you aren't, I guess I'll just have to take your word for it~."
                    "You breathe the words into his ear, enjoying the little noise that escapes his mouth as he closes his eyes and trembles against you."
                elif club == "yearbook":
                    show chelsea shocked
                    show Damien Worry
                    pcname "W-Well, only if you're sure..."
                    show chelsea embarrassed
                    pcname "I've never done anything like that, but I could give it a try, if you really wanted..."
                    show Damien Shocked
                    "There's some sick satisfaction in seeing the shock and embarrassment on Damien's face as he takes in your suggestion. You know it's cruel to enjoy it, but something about teasing Damien just gets you so... so excited!"
                show chelsea happy
                show Damien Worry
                "Satisfied, you wrap your arm around his waist and pull him against your side, resting your head against his shoulder."
            "You enjoy watching the octopus for a few minutes longer before moving onto the next exhibit."
            hide chelsea with moveoutleft
            hide Damien Worry with moveoutleft
            show bg black with dissolve
        "Let him enjoy this." if True:
            $ corruption -= 1
            show chelsea happy
            show Damien Happy
            "Resisting the urge to tease him, you bite back your smile and nod, doing your best to push back the dirty thoughts to the back of your mind."
            pcname "Yeah... This is really cool."
            "You both watch in fascination as the octopus continues to fumble with the rubix cube, twisting the squares with its tentacles until each side matches evenly."
            show Damien Shocked
            show chelsea shocked
            D "Wow! That's so cool!"
            show chelsea blank
            show Damien Worry
            D "Ugh, I'm jealous of an octopus now..."
            show chelsea laugh
            show Damien Blank
            "You can't help but giggle, shaking your head."
            show chelsea happy
            pcname "You're so silly..."
            show Damien Happy
            show chelsea shocked
            "Damien grins and gives you a little peck on the cheek."
            show chelsea embarrassed
            D "Ready to check out something else?"
            show chelsea happy
            pcname "Sure."
            "Hooking your arms around each other's waists, you move onto the next exhibit."
            hide chelsea with moveoutleft
            hide Damien Happy with moveoutleft
            show bg black with dissolve
    if damienexhibit2 == False:
        $ damienexhibit1O=True
        jump damien_exhibitchoice2
    if damienexhibit2 == True:
        $ damienexhibit2O=True
        jump damien_exhibitchoice3
    if damienexhibit3 == True:
        jump damien_enddate

label damien_exhibitchoice2:
    show chelsea blank at right with moveinright
    show Damien Happy at left with moveinright
    "What would you like to do?"
    $ damienexhibit2=True
    menu damien_aqexhibit2:
        "The Sea Turtles!" if damienexhibit1T == False:
            jump damien_aqseaturtles
        "The sea otters!" if damienexhibit1SO == False:
            jump damien_aqseaotters
        "The sharks!" if damienexhibit1S == False:
            jump damien_aqsharks
        "The penguins!" if damienexhibit1P == False:
            jump damien_aqpenguins
        "The octopus!" if damienexhibit1O == False:
            jump damien_aqoctopus

label damien_exhibitchoice3:
    show chelsea blank at right with moveinright
    show Damien Happy at left with moveinright
    "What would you like to do?"
    $ damienexhibit3=True
    menu damien_aqexhibit3:
        "The Sea Turtles!" if damienexhibit2T == False:
            jump damien_aqseaturtles
        "The sea otters!" if damienexhibit2SO == False:
            jump damien_aqseaotters
        "The sharks!" if damienexhibit2S == False:
            jump damien_aqsharks
        "The penguins!" if damienexhibit2P == False:
            jump damien_aqpenguins
        "The octopus!" if damienexhibit2O == False:
            jump damien_aqoctopus

label damien_enddate:
    hide bg black with dissolve
    show chelsea blank at right with moveinright
    show Damien Blank at left with moveinright
    "You and Damien continue through the aquarium together hand-in-hand, admiring the various forms of sea life as they swim and scuttle by."
    "Eventually, you reach their final exhibit: an aquarium tunnel brimming with tropical fish and a wide variety of aquatic sea life."
    show chelsea happy
    show Damien Happy
    "It feels as though a little bit of everything is in the tunnel, from gliding sea turtles to schools of fish to hermit crabs shuffling across the tank floor."
    "Damien wraps his arm around your waist and holds you close, the two of you taking time to admire the aquatic life."
    show chelsea sad
    "But seeing all of this water has made you feel something a little less exciting than awe."
    show chelsea blank
    show Damien Shocked
    pcname "I'll be right back, I just need to run to the bathroom."
    show Damien Neutral
    show chelsea sad
    D "No problem. This place closes soon anyway, so we should probably be on our way."
    show Damien Happy
    show chelsea happy
    D "I'll meet you back in the lobby."
    pcname "Okay."
    hide Damien Happy with moveoutleft
    "You follow the directions to a set of restrooms at the end of the hall and go about your business."
    hide chelsea with moveoutright
    show bg black with dissolve
    pause 0.5
    show bg CityD with dissolve
    show chelsea at right with moveinright
    "{i}Fluuuuuush....{/i}"
    show chelsea confused
    "You pull your shorts back up, ready to leave the stall and clean up, when you hear a soft moan in the stall next to you."
    show chelsea shocked
    "Stall Neighbor" "O-O-Ohhh..."
    show chelsea confused
    "You pause, hand hovering over the handle. You didn't notice it when you first came in, but peering down, there are {i}definitely{/i} two sets of feet in the stall next to you."
    show chelsea shocked
    pcname "{i}Are there people having sex next to me?!{/i}"
    "Another moan echoes throughout the public restroom, followed by a wet sucking sound."
    show chelsea confused
    "You should leave, or at least pretend not to notice as you sneak out of the restroom, but you feel frozen to the spot as a warmth spreads in your lower belly."
    show chelsea blank
    "Not sure what to do, you remain still and wait for them to finish up."
    "After a few minutes-- and a lot of panting and moaning-- they finally clean themselves up and rush out of the bathroom, oblivious to your presence beside them."
    show chelsea shocked
    "You feel your own panties dampen with excitement, but you remain rooted in place, unsure of what to do."
    menu damien_aquariumsex:
        "Text Matt." if mattsubmissive:
            $ corruption += 3
            if defymatt == True:
                show chelsea confused
                "You hate the idea of texting Matt for any sort of favor, but if he's going to blackmail you for sex, the least he can do is get you off when you need it."
            elif True:
                show chelsea sad
                "You feel bad texting Matt behind Damien's back, but the idea of fucking another guy right after your date excites you even more."

            call screen TextingScene("Matt",
            [
                TextMessage("I'm really, really horny right now.", sender = False),
                TextMessage("Ha. The fuck you want me to do about it?"),
                TextMessage("Please? I'm out with Damien right now, but when I get home...", sender = False),
                TextMessage("You're out with that fucking loser? No wonder you need me."),
                TextMessage("The door better be unlocked when I get there.")
            ])

            show chelsea happy
            "You grin and tuck your phone back into your pocket."
            show Damien Shocked at left with moveinleft
            "You open up the stall door to find Damien standing right outside."
            show chelsea shocked
            pcname "Huh?! Damien?!"
            show chelsea angry
            show Damien Worry
            pcname "What are you doing in the girl's room?!"
            show chelsea blank
            if damienconfidence >= 50:
                show Damien Shocked
                D "H-Huh?!"
                show Damien Neutral
                D "Oh, shit... I must have gotten the signs mixed up. My bad, [pcname]!"
            elif True:
                show Damien Shocked
                D "I-I-I--!"
                D "S-Sorry! I must have gotten the signs mixed up!"
            show Damien Neutral
            D "I'll see you in the lobby!"
            show chelsea shocked
            "Damien rushes out of the bathroom before you get a chance to respond, leaving you confused and alone."
            hide Damien Neutral with moveoutright
            show chelsea confused
            if club == "track":
                pcname "{i}What the hell was that about?{/i}"
            elif club == "cheer":
                pcname "{i}...That was super weird.{/i}"
            elif club == "yearbook":
                pcname "{i}O-okay then...{/i}"
            show chelsea blank
            "Shrugging it off, you wash your hands and leave to meet Damien back in the aquarium's lobby."
            hide chelsea with moveoutright
            show bg black with dissolve
            pause 0.5
            show bg CityD with dissolve
            show chelsea at right with moveinright
            show Damien Happy at left with moveinleft
            "Damien waits for you on one of the plush chairs around the center tube of jellyfish, an embarrassed smile on his face. He waves you over."
            show Damien Neutral
            D "Do you want to get some dinner and then head home?"
            show chelsea happy
            "Your clit throbs, and it takes everything in you to smile and nod. Your mind is barely on Damien's suggestion, already jumping ahead to how it'll feel when Matt fucks you back at your apartment later."
            pcname "Yeah, that sounds good."
            show chelsea blank
            show Damien Happy
            "Damien smiles, seemingly relieved that you've said nothing more about the weird bathroom experience, and walks you back out to his car."
            hide chelsea with moveoutleft
            hide Damien Happy with moveoutleft
            show bg black with dissolve
            pause 0.5
            show bg CityD with dissolve
            show chelsea at right with moveinright
            "Damien drives off shortly after dropping you off at your apartment and, while you were afraid he might try to come up inside with you, he gives you a kiss goodnight on the cheek before driving off."
            show Matt Blank with moveinleft
            show chelsea shocked
            "Which is great, considering you find Matt standing outside of your apartment door, barely obscured by a nearby tree."
            show chelsea blank
            "You hurry up to the front door and unlock it."
            show Matt Angry
            show chelsea shocked
            m "I thought I said to leave the door unlocked."
            show chelsea sad
            show Matt Blank
            pcname "Sorry, I was out..."
            show Matt Angry
            m "Next time, either leave it unlocked or get me a key. I'm not freezing my balls off for you again."
            hide chelsea with moveoutleft
            hide Matt Angry with moveoutleft
            show bg black with dissolve
            pause 0.5
            hide bg HomeE with dissolve
            show chelsea at right with moveinright
            show Matt Blank at left with moveinright
            "Matt follows you inside, peering around the empty apartment as you shut and lock the door behind you."
            show Matt Smirk
            "He takes a seat on the couch and spreads his legs wide, a smirk on his face."
            show chelsea shocked
            m "You made me come all the way here and wait outside for you; the least you can do is make it up to me."
            show chelsea embarrassed
            "Glancing at the erection poking through his pants, you have a good idea as to what he wants."
            if defymatt == True:
                show chelsea confused
                show Matt Blank
                "This was supposed to be a quick thing to get you off, but now that he's asking for more, you feel a little regret for inviting him over."
                "You make a face of displeasure that he catches."
                show chelsea shocked
                show Matt Angry
                m "Do you want me to fuck you or not?"
                show chelsea embarrassed
                "As he asks, you can feel the desire growing in your belly. You need him, whether you like it or not."
                if club == "track":
                    pcname "Yes..."
                elif club == "cheer":
                    pcname "Yes, Matt..."
                elif club == "yearbook":
                    pcname "Y-Yes, please..."
            elif True:
                show chelsea embarrassed
                "You lick your lips in anticipation, your excitement evident in the wetness of your panties."
            show Matt Blank
            "Getting down on your knees, you unzip his pants and take his cock out, your lips brushing against the tip."

            "Matt inhales sharply, his fingers finding their way through your hair as you take his tip into your mouth, tracing your tongue against the sensitive skin."
            m "That's right, you slut. Show me how much you need it."
            "You feel a new moisture form in your panties, and it takes all of your willpower not to jump on his cock and ride him now."
            "You pull him further into your mouth and bob your head up and down the length of his cock."
            "Matt's fingers tighten in your hair and he bucks against you, his erection driving right down your throat."
            "You moan as he fucks your face, his groin grinding hard against your chin."
            "With a hard yank of your hair, Matt pulls himself out of your mouth. You gasp for air, startled by the change."
            m "Get up here."
            "You don't need to be told twice. Stripping down bare, you straddle him, his wet cock pressing hard against your slit."
            "Matt grabs your hips and drives himself inside of you fully with one swift thrust."
            pcname "Ohh!"
            "You gasp, your fingers gripping onto his arms tightly. He drives himself into your dripping cunt, one harsh thrust after another."
            "You feel your breasts bounce as you move up and down on his lap, each thrust eliciting a new wave of pleasure through your body."
            m "You like that, you little whore?"
            if club == "track":
                pcname "Yes... Fuck-- fuck, yes!"
            elif club == "cheer":
                pcname "O-Ohhh... Ohh, Matt, yes! Fuck, yes!"
            elif club == "yearbook":
                pcname "Y-Yes, Matt! P-Please... More-- Ohhh..."
            "You feel your body spasm with your oncoming orgasm, your hips jerking involuntarily against his. Matt admires the sight, making no effort to slow down."
            "Your pussy clenches around him, urging him in deeper with each rough movement."
            "Shortly after, you feel his hot cum fill you up one spurt after another."

            show chelsea embarrassed
            "Satisfied, you shakily climb off of him and grab for a box of tissues nearby to clean up."
            show Matt Smirk
            "Matt smirks at you from on the couch, tucking himself away."
            show chelsea shocked
            m "I wonder what your 'date' would think of that."
            show chelsea sad
            show Matt Blank
            "Shame floods you as you quickly remember Damien. Matt laughs at your reaction as he makes his way to the door, leaving you alone with your guilt."
            hide Matt Blank with moveoutright
            hide chelsea with dissolve
            show bg black with dissolve
            $ acts -= 3
            jump events_end_period
        "Text Damien." if True:
            $ corruption += 1
            show chelsea embarrassed
            "Despite your better judgement, you can't stand the thought of waiting until you get home. You need Damien, and you need him {i}now.{/i}"
            "Pulling your phone out of your pocket, you send him a text."
            if damienconfidence >= 50:
                call screen TextingScene("Damien",
                [
                    TextMessage("Damien, can you come in here?", sender = False),
                    TextMessage("Uh, maybe. Is everything okay?"),
                    TextMessage("I'm really horny and I need you.", sender = False),
                    TextMessage("Oh. OH."),
                    TextMessage("Yeah, just give me a second!")
                ])
            elif True:

                call screen TextingScene("Damien",
                [
                    TextMessage("Damien, can you come in here?", sender = False),
                    TextMessage("In the girls' room? Um, I'm not sure..."),
                    TextMessage("I'm really horny and I need you.", sender = False),
                    TextMessage("dsakfjakfhjds"),
                    TextMessage("Um... Uh... I'm not really sure if I should..."),
                    TextMessage("Please? You have no idea how bad it is right now.", sender = False),
                    TextMessage("Um okay... I'll be right there.")
                ])

            show chelsea shocked
            "You blink, shocked to hear a soft knock on your stall door. Glancing at the shoes on the other side, you recognize it as Damien."
            show chelsea confused
            pcname "{i}...Well, that was fast.{/i}"
            show chelsea blank
            pcname "Come in."
            show Damien Happy at left with moveinright
            if damienconfidence >= 50:
                "Damien rushes into the stall, shutting the door behind him. He grins down at you, the tips of his ears tinging pink."
                D "You rang, my lady?"
                if club == "track":
                    show chelsea happy
                    pcname "Damn right I did. Want to help me out?"
                elif club == "cheer":
                    show chelsea happy
                    "You smirk up at him, deciding to play along with his little fantasy."
                    show Damien Shocked
                    pcname "I did, my noble steed. Will you take care of your fair lady?"
                elif club == "yearbook":
                    show chelsea embarrassed
                    pcname "Y-Yes, if you could help me... please..."
                show Damien Happy
                "Damien lets out a breathy laugh, his hands coming down to your waist. You feel his fingers slide up under your shirt and trace the skin underneath."
                D "Abso{i}lutely.{/i}"

                "He leans down and kisses you, inexperienced but excited. You kiss him back, hands sliding up his shirt and over the flat planes of his chest."
                "In between kisses, you feel Damien unbutton your shorts and shove them down, followed by your panties as he slips a finger into your pussy."
                "A small noise escapes the back of your throat and you arch toward him, enjoying the sensation as he curls his finger inside of you."
                D "Heh... You like that?"
                "You nod, biting down on your lip as he slips another inside, curling them both in your wet folds."
                "Your rock your hips against him as he repeats the motion, sliding his fingers in and out of your pussy only to curl them deep inside of you again."
                "You feel Damien's erection stiffen against his pants as you inevitably rub against him, your thigh brushing hard against his pants."
                "Damien removes his fingers from your pussy with a wet {i}shluck{/i} and brings them to his lips, his long tongue licking off your fluids."
                if club == "track":
                    "You lick your own lips, turned on by watching him suck off your juices."
                    pcname "Fuck, that's hot..."
                elif club == "cheer":
                    "You let out a soft, satisfied moan, your pussy growing even more moist at the sight of him licking off your juices."
                elif club == "yearbook":
                    "The action brings a flush to your cheeks, heat running throughout your whole body."
                D "You taste amazing, [pcname]..."
                if club == "track":
                    pcname "Why don't you get a feel for what's inside?"
                elif club == "cheer":
                    pcname "I bet I feel even better inside~"
                elif club == "yearbook":
                    pcname "Th-Thank you..."
                "Pulling his fingers away, Damien unzips his jeans and pulls himself out."
                "Without a word, he grabs you by the hips and turns you around, bending you over so you can grab the top of the toilet's flush maneuver for leverage."
                "You feel his cock press against the folds of your pussy, a pleasant moan spilling out of his mouth as he feels just how wet you are."
                D "Damn, [pcname], you aren't kidding..."
                "He slips into you easily and you gasp at the sudden movement, his cock fully pressing into your body without hesitation."
                "Damien pauses, worry in his voice."
                D "Are you okay? Did I hurt you?"
                pcname "N-No, I'm fine! Keep going, please..."
                "Who knows when someone will walk in? You need to get this done quickly before you're caught."
                "Satisfied with your response, Damien thrusts in and out of you, slowly picking up pace as his confidence grows."
                "You grip the silver bar tightly, your breathing coming out in pants as Damien's cock rams into your body and against your G-spot."
                pcname "D-Damien...! I... I..."
                "Your legs quiver as your release builds up inside of you. You let out a small cry, your body trembling as you hit your orgasm."
                "Damien's breath is hot in your ear as he continues fucking you after you're finished, his fingers digging hard into your hips."
                "You shiver as he moans against your skin, shooting his load deep inside of you."
                "When he pulls out, white cum drips down onto your panties around your ankles and around the rim of his zipper."
                "Damien laughs bashfully, grabbing some toilet paper to clean up. You do the same, wiping up as much of the mess as you can before flushing it down the toilet."
            elif True:

                show Damien Shocked
                "Damien nervously shuffles inside, shutting the door behind him. When he turns to you, his face is bright red."
                show Damien Neutral
                D "Y-You needed me, [pcname]?"
                "Damien fidgets with his fingers nervously, his voice kept low despite the emptiness of the restroom."
                if club == "track":
                    show chelsea happy
                    "You grin, a thrill running through your body as to watch him squirm. You feel so... so {i}powerful.{/i}"
                    pcname "Yeah. I need you to help get me off."
                    show Damien Shocked
                    "Damien's eyes widen but he doesn't object, glancing uneasily between you and the stall door."
                elif club == "cheer":
                    show chelsea happy
                    "You easily close the distance between the two of you, wrapping your arms tightly around his neck, and press your breasts against him."
                    show Damien Shocked
                    pcname "I need you {i}so{/i} badly, Damien."
                elif club == "yearbook":
                    show chelsea embarrassed
                    "You feel just as nervous, struggling to look him in the eye now that he's here, but seeing how quick he is to follow your instructions gives you a little feeling of excitement: of power."
                    pcname "Y-yes, if you could help me..."
                    show Damien Shocked
                    "You shyly gesture toward your crotch, unsure of what else to say."
                show Damien Neutral
                D "U-Um, what would you like me to do?"
                show chelsea happy
                show Damien Shocked
                "There isn't much room in the stall for movement, but you motion for Damien to strip down and, with some hesitation, he does."
                show chelsea happy
                show Damien Blank
                "With his clothes on a pile on the floor, you take a moment to enjoy the sight of his naked body exposed before you."
                show chelsea embarrassed
                "Despite his nervousness of the situation, there is no denying the hard erection jutting out from his groin."
                if club == "track":
                    show chelsea laugh
                    pcname "I see someone's excited, haha!"
                elif club == "cheer":
                    show chelsea happy
                    pcname "Ooh, Damien, you should have told me how hard you were earlier. Maybe I would have taken care of this by one of the exhibits~"
                elif club == "yearbook":
                    pcname "I-I'm glad you're enjoying this..."
                show Damien Shocked
                "His face flushes harder, but he doesn't deny it."

                "Taking his hand, you reposition him onto the toilet. Damien sits down, glancing up at you with uncertainty as you strip out of your shorts and panties."
                "Your pussy moistens as the cold air of the bathroom rushes against your slit, encouraging your fluids to spill out and down your thigh."
                "Damien watches with wide eyes as you straddle him, gasping loudly as you start to slide his cock inside of you."
                if club == "track":
                    pcname "You like that, Damien?"
                elif club == "cheer":
                    pcname "Mmm... You feel so good~! Does it feel nice for you, too?"
                elif club == "yearbook":
                    pcname "D-Does that feel good?"
                D "Y-Yes."
                "His eyes roll back and he squeezes them shut as you push down further, wiggling your hips on his lap until his girth is fully in you."
                D "Ooohh... [pcname]..."
                "Damien's fingers grip your hips tightly but he makes no further motion, content with just being inside of you."
                "You rise up and down on him slowly, tension building in your groin as you enjoy the sensation of riding his dick."
                "Damien's hips jerk toward you suddenly and releases a small gasp, his breath coming out in little pants as you pick up speed."
                "Fuck, this feels good. You bounce on top of him, slamming his erection as hard as you can against your g-spot."
                "After a few moments, you stop pulling out and grind on his cock instead, rolling your hips back and forth over his lap."
                D "[pcname]!!"
                "Damien's body jerks in motion with yours, unable to resist thrusting as you grind into him, your clit throbbing with pleasure at each movement."
                D "[pcname]... [pcname]...!"
                "Damien continued murmuring your name like a prayer as his body spasms and you feel the hot spurt of cum burst inside of you, dripping down your walls and against your thighs."
                "You keep grinding against him as Damien comes down, your own orgasm building until you can't take it anymore."
                "You dig your nails into his shoulders, biting down hard against his neck as you cum, your fluids mixing with his inside of your body."
                "Damien winces as you pull away and, with a shocked laugh, you realize that you've left a harsh bite mark on his neck."
                pcname "Oops..."
                "Damien touches his neck, smiling shyly."
                D "I guess I'll need to hide that..."
                pcname "Yeah, I guess you do."
                "Carefully, you climb off of him and clean up, leaving Damien to fend for himself. He quickly cleans up and gets dressed behind you, suddenly reminded that you're in a public restroom."

            show Damien Blank
            show chelsea blank
            "You peek your head out into the restroom, making sure the coast is clear before Damien rushes out, leaving you to wash your hands and finish cleaning up alone."
            hide Damien Blank with moveoutright
            hide chelsea with dissolve
            show bg black with dissolve
            pause 0.5
            show bg CityD with dissolve
            show chelsea at right with moveinright
            show Damien Happy at left with moveinleft
            "You meet him back in the lobby when you're done, an embarrassed smile on his face."
            D "So, um, that was really fun."
            if mattchain >= 2:
                pcname "I'm glad you enjoyed it."
                show Damien Blank
                if club == "track":
                    show chelsea happy
                    pcname "It's a good thing you showed up. I might have found someone else if you didn't."
                elif club == "cheer":
                    show chelsea happy
                    pcname "I'm glad you were so eager to help me. I would've been really lonely if you turned me down..."
                    show chelsea laugh
                    pcname "I might have even had to find someone else to help me."
                elif club == "yearbook":
                    show chelsea embarrassed
                    pcname "I-I'm happy you were there... I don't know what I would have done otherwise... or who..."
                show Damien Glare
                "Damien's eyebrows pinch together in confusion, the mood shifting a little."
                D "What do you mean by that?"
                show Damien Blank
                if club == "track":
                    show chelsea laugh
                    pcname "Haha, I'm just teasing! Chill out, Damien."
                elif club == "cheer":
                    show chelsea laugh
                    pcname "Oh, I'm just teasing, babe~! Don't get so worried."
                elif club == "yearbook":
                    show chelsea sad
                    pcname "I-I'm just joking! I'm sorry, I was trying to be funny..."
                show Damien Glare
                D "It didn't feel very funny... I'm not sure how to feel about it."
                show Damien Sad
                D "You shouldn't say things like that, [pcname], even if you're teasing. I might believe you one day."
                show chelsea sad
                pcname "Ah... Sorry."
                show Damien Worry
                "Damien sighs, shaking his head, and tries to move on from your awkward conversation."
            show Damien Neutral
            show chelsea blank
            D "Do you want to go grab some dinner and then I'll drop you off at home?"
            "Now that you've come down from your lustful expenditure, you realize just how empty your stomach is. You've been so busy exploring the aquarium all day that it had completely slipped your mind!"
            show chelsea happy
            show Damien Happy
            pcname "That sounds great! I think I know a good sushi place nearby..."
            show Damien Shocked
            D "Aw, right after seeing all these fish? Now that's just cruel."
            show chelsea laugh
            show Damien Laugh
            "You both laugh as you leave the aquarium and head back to Damien's car."
            $ acts -= 3
            jump events_end_period
        "Wait until you get home." if True:
            $ corruption -= 2
            show chelsea blank
            "The aquarium isn't a place for sex, so despite the urge you feel to take care of business now, you decide it's best to wait until you get home."
            show Damien Blank at left with moveinright
            "With a sigh, you open up the stall door to find Damien standing right outside."
            show chelsea shocked
            show Damien Shocked
            pcname "Huh?! Damien?!"
            show chelsea angry
            show Damien Worry
            pcname "What are you doing in the girl's room?!"
            show chelsea blank
            if damienconfidence >= 50:
                show Damien Shocked
                D "H-Huh?!"
                show Damien Neutral
                D "Oh, shit... I must have gotten the signs mixed up. My bad, [pcname]!"
            elif True:
                show Damien Shocked
                D "I-I-I--!"
                D "S-Sorry! I must have gotten the signs mixed up!"
            show Damien Neutral
            D "I'll see you in the lobby!"
            hide Damien Neutral with moveoutright
            show chelsea shocked
            "Damien rushes out of the bathroom before you get a chance to respond, leaving you confused and alone."
            show chelsea confused
            if club == "track":
                pcname "{i}What the hell was that about?{/i}"
            elif club == "cheer":
                pcname "{i}...That was super weird.{/i}"
            elif club == "yearbook":
                pcname "{i}O-okay then...{/i}"
            show chelsea blank
            "Shrugging it off, you wash your hands and leave to meet Damien back in the aquarium's lobby."
            hide chelsea with moveoutright
            show bg black with dissolve
            pause 0.5
            show bg CityD with dissolve
            show chelsea at right with moveinright
            show Damien Happy at left with moveinright
            "Damien waits for you on one of the plush chairs around the center tube of jellyfish, an embarrassed smile on his face. He waves you over."
            show Damien Neutral
            D "Do you want to get some dinner and then head home?"
            show chelsea happy
            "Your clit throbs, begging you to go home and get off now, but you force a smile in place and nod."
            pcname "Yeah, that sounds good."
            show Damien Happy
            show chelsea blank
            "Damien smiles, seemingly relieved that you've said nothing more about the weird bathroom experience, and walks you back out to his car."
            hide chelsea with moveoutleft
            hide Damien Happy with moveoutleft
            show bg black with dissolve
            pause 0.5
            show bg HomeE with dissolve
            show chelsea happy at right with moveinright
            "As soon as you've said your goodbyes to Damien and stepped into your apartment, you strip down, tossing your clothes off without a care in the world."
            $ clothes = "naked"
            "All throughout dinner, your mind was solely focused on the need to pleasure yourself."
            "You suppose you could have taken care of yourself in the bathroom, but some things are better left in private."
            hide chelsea with moveoutleft
            show bg black with dissolve
            pause 0.5
            show bg RoomE with dissolve
            show chelsea at right with moveinleft
            "Free from the constraints of your clothes, you make your way into the bedroom and plop down on your comforter, grabbing the nearest throw pillow and squeezing it between your legs."
            show chelsea embarrassed
            "A small moan escapes your lips as you rub against the fabric, your clit throbbing with delight as you hump the square cushion."
            show chelsea happy
            "Yes, this is what you needed!"
            show chelsea embarrassed
            "You feel your face heat up as you grind against the soft pillow, your bodily fluids soaking into the fabric and making it easier to rub against it."
            show chelsea happy
            "You hear the phantom moans of the couple in the stall beside you and imagine what they could have been doing."
            show chelsea embarrassed
            "Was she blowing her husband? Was his cock shoved down her throat and fucking her face in the publicity of a bathroom stall?"
            "Or maybe he was eating her out, her legs crossed tightly around his neck, squeezing his tongue into her vagina--"
            show chelsea shocked
            "Your body shudders against the pillow as you feel the tension build in your lower abdomen and release, your cum dripping out and soaking through your throw pillow, small droplets landing on your sheets."
            show chelsea happy
            "You take a moment for your breathing to settle before to pull the pillow away and examine the damage with a sigh."
            show chelsea blank
            "Guess it's time to do laundry."
            $ acts -= 3
            jump events_end_period

label damien_conveniencestore:
    $ damienAttire(0)
    $ clothes = "school"
    show chelsea at right with moveinright
    "The school day ends without much excitement, and as you make your way to the front doors, Damien catches up to you from down the hall."
    show Damien Neutral at left with moveinleft
    D "Hey, [pcname]. Are you heading home now?"
    show chelsea sad
    show Damien Blank
    pcname "Yeah, but I need to get changed for work."
    show Damien Neutral
    if damienconfidence >= 50:
        D "I'm heading in that direction, so let's head back together."
    elif True:
        D "Well, I have to go that way today... Um, do you mind if we walk back together?"
    show chelsea happy
    pcname "Sure!"
    show Damien Happy
    "Damien grins and slings his bag over his shoulder, following you outside of the school."
    hide chelsea with moveoutleft
    hide Damien Happy with moveoutleft
    $ clothes, hair = casualwear
    $ damienAttire(2)
    show bg black with dissolve
    pause 0.5
    show bg CityD with dissolve
    show chelsea at right with moveinright
    show Damien Blank at left with moveinright
    "The air is crisp and chill despite the late afternoon, and you huddle further into your jacket for warmth."
    show Damien Neutral
    D "How were your classes today, [pcname]?"
    menu damien_classes:
        "They were great!" if True:
            show chelsea happy
            if club == "track":
                pcname "They were awesome! I got picked as captain for dodgeball in our gym class."
            elif club == "cheer":
                pcname "They were really fun! I got interviewed for the school's TV station. I'll get to see my face on the TV tomorrow!"
            elif club == "yearbook":
                pcname "I-I really liked them! My history teacher brought in some original photographs from the 1900's for us to look at... They were so cool!"
            show Damien Happy
            D "That's great, [pcname]! I'm glad you had a good time."
        "It was okay." if True:
            show chelsea blank
            "You shrug. You can't say you hate the classes, but it's not like school is your favorite place to be."
            if club == "track":
                pcname "It was okay, I guess... I get antsy when I'm in one place for too long, so sitting down through class can be pretty hard."
            elif club == "cheer":
                pcname "It was alright. The classes can go on forever, but it's not like I'm completely wasting my time..."
                show chelsea confused
                pcname "I just wish I could use my phone during class without worrying about getting caught."
            elif club == "yearbook":
                show chelsea sad
                pcname "I-It was fine. I like learning, but some of the stuff we go over can get really repetitive..."
            show Damien Blank
            D "Yeah, I can relate to that."
        "I hate school." if True:
            if club == "track":
                show chelsea confused
                pcname "Terrible. I can't stand sitting through all of these classes; I have too much energy and get really fidgety."
                pcname "I'd rather be doing anything else except sitting through school."
            elif club == "cheer":
                show chelsea confused
                pcname "Ugh, boring, as usual. There's nothing exciting going on, and this dress code is so restricting."
                pcname "Like, who wants to wear grey every day? We look like blobs."
            elif club == "yearbook":
                show chelsea sad
                pcname "I-I don't really like school... It's too crowded, and a lot of the people there are mean..."
                pcname "I'd rather do it all online, if I could..."
            if damienconfidence >= 50:
                show Damien Shocked
                D "I didn't realize you hated school so much. I'm sorry to hear that, [pcname]."
            elif True:
                show Damien Sad
                D "O-Oh... I'm sorry. I didn't realize school was a bad experience for you..."
    show chelsea blank
    show Damien Blank
    pcname "How about you? How were your classes?"
    if damienconfidence >= 50:
        show Damien Neutral
        show chelsea sad
        D "They were alright; I had to deal with Alex in my astronomy class, so you know how that went."
        "Damien sighs in frustration, shaking his head."
        show Damien Glare
        show chelsea blank
        D "I don't even get why he took the class in the first place. He can barely pass math, let alone calculate the things we do in astronomy..."
        D "I'm sure he took it just because I did. He's always looking for a reason to harass me."
        show Damien Neutral
        show chelsea sad
        D "He hasn't been bothering you lately, has he?"
    elif True:
        show Damien Sad
        show chelsea sad
        D "They were okay, but I had astronomy with Alex, so I had to hear his mouth run for the whole class..."
        "Damien sighs in defeat, his shoulders slumping as he stares down at the sidewalk."
        show Damien Worry
        show chelsea blank
        D "I think he took it because I did; there's no way Alex could pass this class without his dad bribing the school."
        show Damien Sad
        D "I just wish he would leave me alone."
        "He suddenly looks up at you, worry creasing across his face."
        show Damien Neutral
        show chelsea sad
        D "Ah, he hasn't been bothering you lately, has he [pcname]?"
    pcname "No, he hasn't really said anything since lunch the other day."
    show Damien Blank
    show chelsea blank
    "Damien nods, relief relaxing his features."
    if damienconfidence >= 50:
        show Damien Glare
        show chelsea shocked
        D "That's good. I won't take him harassing you anymore, [pcname]."
        show Damien Neutral
        show chelsea embarrassed
        D "Bothering me is one thing, but you... that's different."
    elif True:
        show Damien Neutral
        show chelsea embarrassed
        D "G-Good. I hate when he bothers you, [pcname]. You don't deserve it."
        show Damien Glare
        show chelsea shocked
        D "I-I won't let him do it anymore. I know I haven't been the best at standing up to him, but I won't let him hurt you like that..."
    if mattslap == 1 and bullytelloff == 1:
        show chelsea shocked
        "You feel the color drain from your face as you recall all of the horrific things Alex and Matt have done to you."
        show chelsea sad
        "You're tempted to tell Damien about all of it now, but you can't bring yourself to do it. You're not sure you ever want to tell anyone about what happened."
    if mattsubmissive == True and bullytelloff == 1:
        show chelsea embarrassed
        "You feel your face heat up as you recall all of the lewd acts you performed with Alex and Matt."
        show chelsea shocked
        "If Damien tries to stand up against Alex, would Alex tell him about everything?"
        "The thought sends a spike of panic through you. The last thing you need is Damien to find out about that threesome."
    elif True:
        show chelsea embarrassed
        "You feel a warmth of appreciation swell in your chest."
        "Alex can be a real pain to deal with, but hearing Damien speak so strongly about wanting to stand up to him for your sake makes you smile."
    show Damien Shocked
    show chelsea confused
    "Before you get a chance to respond, something catches Damien's attention and he catches your elbow gently."
    show Damien Neutral
    show chelsea blank
    D "Hey, do you mind if we stop in here? I'm really thirsty."
    show Damien Blank
    "Damien gestures toward a convenience store across the street, a blue mascot of a penguin lit up at the front."
    show chelsea happy
    show Damien Happy
    pcname "Sure."
    hide chelsea with moveoutleft
    hide Damien Happy with moveoutleft
    show bg black with dissolve
    pause 0.5
    show bg CityD with dissolve
    show chelsea at right with moveinright
    show Damien Blank at left with moveinright
    "You follow Damien across the street and into the store where you're immediately greeted by an array of short snack aisles, magazine racks, and a wall full of cooler drinks."
    "Damien wanders toward the cooler and scrutinizes the options before pulling out a green iced tea."
    show Damien Neutral
    D "What would you like, [pcname]?"
    menu damien_conveniencedrink:
        "Soda." if True:
            show Damien Blank
            "Although not the healthiest option, you're craving something fizzy and sweet."
            show chelsea happy
            pcname "I'll just get a soda."
        "Milk tea." if True:
            show Damien Blank
            "Tea sounds good, but you want something a little creamier."
            show chelsea happy
            pcname "I'll get a milk tea, I think."
        "Slushy." if True:
            show Damien Blank
            "You eye up the spinning slushy machine nearby, tempted by the vibrantly colored syrups."
            show chelsea happy
            pcname "I could really go for a slushy right now."
    show Damien Happy
    D "That sounds good. Why don't you pick one out while I pick up a few snacks?"
    show chelsea laugh
    pcname "Okay."
    hide Damien Happy with moveoutleft
    show chelsea happy
    "Damien wanders down another aisle, disappearing behind the rows of chips and pretzels."
    show chelsea blank
    "As you pick out your drink, you hear the little bell from the front door ring, followed by approaching footsteps."
    "You pay no attention to it until you actually look up and notice the new arrival."
    show chelsea shocked
    "A girl around your age with short red hair and bright green eyes passes by, eyeing up the selection of drinks in the cooler."
    "Her uniform is different-- she must be from another school-- but you feel something familiar about her, something you can't quite put your finger on."
    show chelsea embarrassed
    "She notices you staring at her and gives you an odd look."
    "Girl" "Can I help you?"
    if club == "track":
        show chelsea shocked
        pcname "Oh, my bad! I didn't mean to stare."
        show chelsea blank
        pcname "You just look familiar, that's all."
        "Girl" "Oh..."
    elif club == "cheer":
        show chelsea shocked
        pcname "Oh, I'm so sorry! You're just really pretty. I didn't mean to stare."
        show chelsea blank
        "Girl" "Oh... Thank you."
    elif club == "yearbook":
        show chelsea shocked
        pcname "S-Sorry! Y-You just look like someone and I thought..."
        show chelsea blank
        "Girl" "It's okay."
    show chelsea confused
    pcname "Have we met before?"
    "She shakes her head, plucking a water bottle from the cooler."
    "Girl" "I don't think so. I'm Lydia."
    if club == "track":
        show chelsea happy
        "You give her a bright smile, thrusting your hand out. She shakes it."
        pcname "[pcname]."
    elif club == "cheer":
        show chelsea happy
        "You smile, tossing your hair over your shoulder."
        pcname "What a cute name! I'm [pcname]."
    elif club == "yearbook":
        show chelsea embarrassed
        "You smile shyly at her, nervously twisting a piece of hair between your fingers."
        pcname "I'm [pcname]..."
    show chelsea happy
    "She smiles politely, fingering the cap of her water bottle."
    "Lydia" "It's nice to meet you."
    show chelsea shocked
    D "[pcname], are you read--"
    show Damien Happy at left with moveinleft
    "Damien's question cuts off as he turns the corner, coming to an abrupt halt behind Lydia."
    show chelsea blank
    show Damien Blank
    "Although she doesn't look at him, you notice her eyes go wide and her face pale, her hands trembling around the water bottle."
    "Damien looks between the two of you, his jovial mood gone in an instant."
    show Damien Worry
    D "...Lydia?"
    "With zombie-like slowness, Lydia turns to meet Damien head-on."
    show Damien Neutral
    D "...Hey."
    show Damien Blank
    show chelsea shocked
    "She bolts, dropping the water bottle on the floor. It bounces against the linoleum, rolling down one of the aisles."
    "In seconds, she's gone."
    "You stare after her, baffled by her sudden reaction. Damien stares after her as well, his expression blank."
    show chelsea confused
    "You look back at Damien, confused."
    pcname "Do you know her?"
    show chelsea blank
    "You already know the answer, but you aren't sure what else to ask. The whole scenario was just so... weird."
    show Damien Sad
    "Damien sighs and nods, leaving to pick up the water bottle and place it back into the cooler."
    show chelsea shocked
    D "Yeah... She's my ex..."
    show Damien Blank
    show chelsea blank
    "He looks at you a little nervously, his thumb running up and down the cooler's handle."
    show Damien Neutral
    D "Did she tell you anything...?"
    show Damien Blank
    show chelsea confused
    "You shake your head."
    if club == "track":
        pcname "We just met."
    elif club == "cheer":
        pcname "I just said she looked pretty."
    elif club == "yearbook":
        show chelsea sad
        pcname "N-No, we just said hi..."
    show chelsea blank
    show Damien Worry
    "Damien nods, more to himself than to you, his attention still drawn to where Lydia ran off."
    show chelsea confused
    "This doesn't seem to be something he wants to talk about, but you can't get over that strange departure. She looked {i}terrified.{/i}"
    if club == "track":
        pcname "What was that about?"
    elif club == "cheer":
        pcname "So... bad blood between you two?"
    elif club == "yearbook":
        show chelsea sad
        pcname "D-Damien...?"
    show Damien Sad
    show chelsea blank
    "He frowns, glancing back toward the front door before finally turning his attention to you."
    show Damien Neutral
    D "I don't really like talking about it, but I want to be honest with you, too, [pcname]."
    show Damien Sad
    show chelsea sad
    D "Our breakup was kind of messy. That whole relationship was actually kind of a mess..."
    show Damien Happy
    D "I was really invested in our relationship. We only dated for six months, but I really thought we would be one of those high school sweetheart couples one day."
    show Damien Blank
    show chelsea blank
    "Damien looks to the side, reminiscing over his past relationship. He doesn't look eager to continue, but he does so anyway."
    show Damien Glare
    show chelsea sad
    D "She didn't take it as seriously as I did, though, and would talk about me behind my back to all of her friends."
    show Damien Angry
    show chelsea shocked
    D "Before I knew it, she was spreading rumors about me around the whole school."
    show Damien Glare
    show chelsea sad
    "Maybe that's why you see Damien alone all of the time; those rumors must have stuck with him, at least some of them."
    show Damien Sad
    D "People didn't want to hear my side of the story, and the bullying was really bad..."
    "He lets out a deep breath, as though trying to release some of his hold on the past."
    show chelsea blank
    "You understand how difficult it can be to relay difficult moments in life, starting with your own parents."
    show Damien Neutral
    D "This was a few years ago, and Lydia ended up transferring schools for her dad's job, so most people moved on."
    show Damien Glare
    show chelsea sad
    D "But people like Alex like to bring up the rumors once in a while just to fuck with me. I'm honestly surprised no one's tried to break us up yet..."
    show Damien Worry
    show chelsea shocked
    "He looks at you anxiously, as though expecting you to confirm otherwise."
    show chelsea blank
    "But you haven't heard anything. You've heard Alex's taunts, sure, but there hasn't been any rumors that would make Damien look bad."
    if club == "track":
        show chelsea confused
        pcname "That really sucks, Damien. Why the hell would she spread rumors about you?"
        show Damien Sad
        show chelsea sad
        "He shrugs, disheartened."
        D "I don't know. I wish that I did."
    elif club == "cheer":
        show chelsea shocked
        pcname "That's horrible! Girls can be so catty. I can't believe your own girlfriend did that to you."
        show chelsea sad
        show Damien Sad
        D "Yeah... It was a rough time. She was the first girlfriend I had, and the only other one for that matter."
        D "No one really wanted to date me after hearing what she said."
    elif club == "yearbook":
        show chelsea sad
        show Damien Sad
        pcname "T-That's terrible! I'm so sorry, Damien..."
        D "It's okay. I wish things had ended better, but there's nothing I can do about that."
    show Damien Happy
    show chelsea shocked
    "He smiles at you and takes your hand in his, giving it a little squeeze."
    show chelsea blank
    D "But it's okay now. We have each other, and that's all that matters, right?"
    show chelsea happy
    pcname "Yeah."
    "You give him an encouraging smile which seems to cheer him up. Damien glances at the drink in your hand, suddenly remembering why he's here."
    show Damien Shocked
    show chelsea blank
    D "Oh! Right! Let me get that for you. Were you all ready to check out?"
    show chelsea happy
    show Damien Happy
    pcname "Mhm!"
    "You pass Damien your drink and follow him to the cash register. He pays for your beverages and snacks before walking you back to your apartment."
    hide Damien Happy with dissolve
    hide chelsea with dissolve
    show bg black with dissolve
    jump events_end_period

label damien_flowers:
    show chelsea at right with moveinright
    $ clothes, hair = casualwear
    "The weekend is finally here and you're ready to relax after a long week of school and work."
    show chelsea happy
    "As you settle down on your couch, fully prepared to binge whatever special is suggested to you on your streaming services, you hear a soft knock at the door."
    show chelsea confused
    show bg HomeE with dissolve
    "You aren't expecting any food deliveries and your landlord defintely isn't due for rent yet, so with an ounce of confusion and curiosity, you answer the door."
    show Damien Neutral at left with moveinleft
    D "Hi, [pcname]."
    show Damien Blank
    "You hear Damien's voice, but your boyfriend is hidden behind a thick bouquet of flowers: not just any flowers, but your {i}favorite!{/i}"
    show chelsea shocked
    "You gasp, accepting the bundle in your arms. The colorful bouquet smells amazing and fresh, and it's larger than most wedding bouquets you've seen."
    show Damien Happy
    if club == "track":
        show chelsea happy
        pcname "Damien, these are beautiful! I love them!"
    elif club == "cheer":
        show chelsea laugh
        pcname "Oh my god! Damien, these. Are. So. {i}Gorgeous!{/i} Thank you!"
    elif club == "yearbook":
        pcname "T-These are for me?"
        "You stare at the bouquet in shock. You've never been given flowers like this before."
        show chelsea happy
        pcname "T-Thank you so much! I love them!"
    show chelsea happy
    "Staring at the bouquet, you're sure that you've never told him what flowers are your favorite, and yet this bouquet couldn't be any more perfect."
    show chelsea confused
    show Damien Laugh
    pcname "How did you know these were my favorite?"
    show chelsea happy
    show Damien Happy
    "Damien shrugs, a proud but mischievous glint in his eyes."
    show Damien Laugh
    D "Lucky guess!"
    show Damien Happy
    D "I was just thinking of you and wanted to bring these by. I'm glad you like them."
    show chelsea laugh
    pcname "I {i}love{/i} them. Let me just put these in some water."
    show Damien Blank
    show chelsea happy
    "You gesture for Damien to follow you inside while you grab a vase from the kitchen, filling it up with water before you stuff the bouquet inside."
    "The flowers barely fit through the narrow opening, but you manage to squeeze them inside. You prop the vase up in the living room where you can smell them all the time."
    show Damien Neutral
    D "I was actually wondering if you wanted to go out and grab dinner with me? There's a place nearby I wanted to try."
    menu damien_dinner:
        "Let's go!" if True:
            $ corruption -= 2
            show Damien Blank
            "Although you had planned to stay home and binge some TV, the sudden appearance of Damien and his romantic gestures have swayed you enough that the idea of going outside is exciting."
            show chelsea happy
            pcname "Sure! Let's go."
            show Damien Happy
            "Damien grins and you turn off the TV and pull your shoes on, making sure to lock up the apartment before following Damien outside to his car."
            hide chelsea with moveoutleft
            hide Damien Happy with moveoutleft
            show bg black with dissolve
            pause 0.5
            show bg CityD with dissolve
            show chelsea at right with moveinright
            show Damien Blank at left with moveinright
            "Damien drives you through town passing by an array of shops and restaurants but stopping at none of them."
            show chelsea confused
            if club == "track":
                pcname "Uh, aren't we supposed to stop at one of these?"
            elif club == "cheer":
                pcname "Sooo where are we going?"
            elif club == "yearbook":
                show chelsea shocked
                pcname "D-Damien...? Did we pass it...?"
            show Damien Neutral
            show chelsea blank
            D "It's just another block down. We're almost there."
            show Damien Happy
            if damienconfidence >= 50:
                "Damien gives you an encouraging smile before pulling into the parking lot of a strip mall."
            elif True:
                "Damien gives you a nervous smile before pulling into the parking lot of a strip mall."
            show chelsea confused
            "You're skeptical at first, but as Damien escorts you out of the car, you see a large sign displaying the name of a new restaurant: 'THE TIME LODGE'."
            hide chelsea with moveoutleft
            hide Damien Happy with moveoutleft
            show bg black with dissolve
            pause 0.5
            show bg DatePlace with dissolve
            show chelsea shocked at right with moveinright
            show Damien Blank at left with moveinright
            "As you follow Damien inside, the walls are covered in various clocks both new and old, and as the restaurant stretches on, you see a variety of posters, magazines, newspaper clippings, and photographs dated from the 1900s until now."
            "The whole restaurant feels a little chaotic, but seems to have a whole time travelling theme going on."
            if damienconfidence >= 50:
                show Damien Happy
                "Damien gestures toward the restaurant proudly, obviously excited by this hidden gem in the city."
                D "Well? What do you think?"
            elif True:
                show Damien Neutral
                "Damien stares at you nervously as you take it all in, anxious about your reaction."
                D "S-So, um, do you like it?"
            menu damien_timmelodge:
                "This looks so cool!" if True:
                    $ corruption -= 1
                    if club == "track":
                        show chelsea happy
                        "You've always wondered what it would be like to travel back in time, and this restaurant might be the closest you ever get to it."
                        show chelsea laugh
                        pcname "This place looks awesome!! Where did you find it, Damien?"
                        show chelsea happy
                        show Damien Neutral
                        D "Ah, it was recommended to me by a friend online..."
                        show Damien Blank
                        show chelsea laugh
                        pcname "Sweet! I can't wait to try it out!"
                    elif club == "cheer":
                        show chelsea happy
                        "Although a little nerdier than your typical taste in restaurants, you can't deny that this place looks amazingly authentic, and the various degrees of pop culture shown off through the decades is fun to look at."
                        show chelsea laugh
                        pcname "This place is so cute! Did you find this by yourself, Damien?"
                        show Damien Neutral
                        show chelsea happy
                        D "Oh, um, no. One of my friends online showed it to me."
                        pcname "Laugh"
                        show Damien Blank
                        pcname "It's sooo adorable! You'll have to thank them for me!"
                    elif club == "yearbook":
                        "This is exactly the kind of nerdy thing you're used to seeing the other members fawn over at your club, and you can't deny that the display of various dates and photographs is fascinating to you."
                        show chelsea embarrassed
                        pcname "T-This is so neat! How did you find it...?"
                        show Damien Shocked
                        D "A friend of mine recommended it to me online. You really like it?"
                        show Damien Blank
                        pcname "Mhm! It looks so cool..."
                    show Damien Happy
                    show chelsea happy
                    "Damien smiles and lets out an exhalation of relief."
                    show Damien Laugh
                    D "I'm glad! I wasn't sure you would like this place when I heard about it, but I must have guessed right!"
                    show Damien Blank
                    show chelsea blank
                    "The hostess approaches you then, a cherry-lipped smile on her face."
                    $ damienconfidence += 1
                "This place is so lame." if True:
                    $ corruption += 2
                    if club == "track":
                        show chelsea confused
                        "You audibly groan as you look around the restaurant. It feels just like the sort of dorky sci-fi thing that Damien would be into, and it's not your style at {i}all{/i}."
                        pcname "You couldn't have just taken me to an Applehornets or something? This place is a mess..."
                    elif club == "cheer":
                        show chelsea confused
                        "You sneer at the restaurant, embarrassed to be setting foot in here. What was Damien thinking?"
                        pcname "It looks like you brought me to a geek convention."
                    elif club == "yearbook":
                        show chelsea sad
                        pcname "W-Well... Do you want me to be honest...?"
                        "You grimace as you look around the restaurant, clearly thrown off by the chaos of it all."
                    show Damien Sad
                    show chelsea blank
                    "Damien's face falls instantly, a flush of shame overcoming him as he nervously glances around the restaurant."
                    show Damien Worry
                    D "O-Oh... Um, I'm sorry. We can go somewhere else..."
                    show Damien Sad
                    if club == "track":
                        show chelsea confused
                        "You let out an audible sigh."
                        pcname "And have to drive somewhere else? No thanks. I'm hungry now."
                    elif club == "cheer":
                        show chelsea confused
                        "You sigh, shaking your head."
                        pcname "We're already here and I'm hungry, so we might as well just deal with it..."
                    elif club == "yearbook":
                        show chelsea sad
                        "You frown and shake your head."
                        pcname "N-No, it's okay... We're already here..."
                    show Damien Sad
                    "Damien looks like he's ready to take your hand and leave, but the hostess arrives back at her stand, drawing your attention."
                    $ damienconfidence -=1
            show Damien Blank
            show chelsea blank
            "The hostess is dressed like a vintage 1950's housewife, with a petticoat under her dress and a pair of shiny red heels. Glancing around the restaurant, you realize everyone is costumed in a different time period."
            "Time Lodge Hostess" "Good evening, friends! Will there just be two of you travelling with us today?"
            show chelsea happy
            pcname "Two, please."
            "Time Lodge Hostess" "Wonderful! We'll be travelling back to 1953 this evening."
            "With a smile, the hostess grabs two menus and walks you through the restaurant to a 50's styled 'kitchen' with various pop culture icons on the walls and retro tables and chairs set up."
            "You and Damien take your seats as the hostess hands you your menus and disappears back to the front of the restaurant."
            show chelsea confused
            show Damien Happy
            "You look over the vast menu briefly-- each section separated by popular items of various decades-- before putting your order in with the waitress."
            show chelsea blank
            show Damien Blank
            "Once your order is in, both you and Damien take a few moments to simply admire the atmosphere and listen to an old doo-wop play over the speakers."
            show Damien Neutral
            D "So, [pcname], do you have any plans for the Day of Harvest?"
            show chelsea shocked
            "Damien's question catches you off guard and it takes you a moment to pull yourself back to the present."
            show chelsea blank
            "The Day of Harvest... It's still a long ways away, but you've avoided thinking about it as much as you can."
            show chelsea sad
            "You haven't properly celebrated that holiday since your parents died. It's a holiday centered around family and being together, but with no family left, how are you supposed to celebrate?"
            "You shake your head, your mood dampening a little with the reminder."
            pcname "No, I don't have any plans..."
            if damienconfidence >= 50:
                show Damien Neutral
                D "Really? Well, that works out for my next question then, haha."
                show Damien Happy
                show chelsea shocked
                D "Do you want to spend the holiday weekend with me at my house?"
                show Damien Neutral
                show chelsea blank
                D "My family goes out of town every holiday and rents a cabin in the woods to celebrate, but I'm staying home this year to take care of my brother's dogs."
                show Damien Happy
                D "So I'll be alone at my house all weekend, but I'd love for you to stay over. My parents won't be back until Sunday, so I figured we could have a nice romantic weekend to ourselves."
                "Damien reaches across the table to hold your hand, his fingers soft as they stroke the top of your palm."
            elif True:
                show Damien Shocked
                show chelsea confused
                D "Really?"
                "Damien's eyes light up, not quite picking up on your somber mood as whatever he has planned comes to fruition."
                show Damien Happy
                show chelsea blank
                D "W-Well, um, you see my family is going to be out of town that weekend... They always rent a place in the woods for the holidays, but I'm staying home this year to take care of my brother's dogs."
                show Damien Neutral
                D "I-I was... Well I was thinking... I mean, if you wanted to..."
                "He takes a deep breath, struggling to get the words out."
                show Damien Happy
                show chelsea shocked
                D "I was thinking it would be fun if you stayed over for the weekend, since you aren't doing anything... My parents won't be back until Sunday, s-so we'll have the whole place to ourselves..."
                show Damien Blank
                show chelsea blank
                "Damien looks down at his hands nervously, his suggestion hanging in the air."
            show chelsea embarrassed
            "You feel a little surprised but touched by his offer. You had been avoiding thinking about the holiday as a whole, but now that you might be able to spend it with Damien..."
            "A familiar warmth fills your chest and you smile. It would be nice to spend the holiday with someone, especially your boyfriend."
            show chelsea happy
            pcname "That sounds great, Damien. I would love to."
            if damienconfidence >= 50:
                show Damien Shocked
                D "Really? Cool! We'll set things up when it's a little closer, but this is awesome!"
                show Damien Happy
                D "I'm really looking forward to spending the weekend with you, [pcname]."
            elif True:
                show Damien Shocked
                D "R-Really?"
                show Damien Happy
                "Relief washes over Damien's face and he grins."
                D "C-Cool! I mean, awesome, yeah... We can, um, set things up when the weekend is closer, but I'm really excited for it."
            show chelsea confused
            pcname "I'm surprised you aren't going to the cabin with your family. Do you usually watch the dogs?"
            show chelsea blank
            show Damien Neutral
            D "Ah, no, not normally. My brother usually gets his friend to watch them, but all of them were busy this year."
            show Damien Happy
            D "Besides, I was really hoping to spend some extra time with you."
            if club == "track":
                "Getting to spend some alone time with Damien without the usual interruptions at school sounds great."
                show chelsea laugh
                pcname "I love it! Let's do it."
            elif club == "cheer":
                show chelsea happy
                "You can't help but let your mind wander to all the things you and Damien could do while you're alone in his house."
                "It's not as if it'll be your first time hooking up, but there's something exciting about the idea of staying at a guy's house all weekend with zero supervision."
                pcname "I can't wait~. We're going to have a {i}lot{/i} of fun together."
            elif club == "yearbook":
                show chelsea embarrassed
                "You're a little nervous about the idea of staying at a guy's house alone for a whole weekend, but it's not as if you haven't gone all the way with Damien before."
                "You blush at the memory but try to push it back, focusing on the importance of spending the Day of Harvest with someone else instead of all by yourself."
                pcname "I-I can't wait... Thank you for inviting me."
            show chelsea sad
            pcname "Now I just wish the holiday wasn't so far away..."
            show Damien Laugh
            show chelsea blank
            "Damien laughs a little, his body visibly relaxing as you begin to hype yourself up for the holiday sleepover."
            show Damien Happy
            D "Me too. It's going to be a lot of fun, [pcname]. The holiday can't come soon enough."
            show chelsea happy
            "The waitress drops off your food then, and the conversation ends as you enjoy your meals."
            hide chelsea with moveoutleft
            hide Damien Laugh with moveoutleft
            show bg black with dissolve
            pause 0.5
            show bg DatePlace with dissolve
            show chelsea at right with moveinright
            show Damien Blank at left with moveinright
            "Once you're finished eating and have paid, Damien walks you back out to his car, holding the door open for you to get in before driving you back to your apartment."
            "As Damien walks you up to your apartment door, he pauses, watching you fumble with your keys to open the lock."
            show chelsea confused
            show Damien Neutral
            D "Ah, before I go, [pcname], there's something I've been meaning to tell you..."
            show chelsea blank
            show Damien Happy
            D "My mom really wants to meet you sometime soon. I've told her a lot about you and she's really excited."
            show chelsea shocked
            "Meet his mom? Your heart thumps hard in your chest as a new sort of anxiety settles in."
            show chelsea blank
            show Damien Blank
            "Meeting someone's parents-- especially if you're dating them-- is pretty serious business, and for you to meet Damien's mom... It feels like a solidification of the relationship in your mind."
            show chelsea sad
            "What if she doesn't like you? Or what if she likes you too much and wants to adopt you, making you and Damien siblings? Will you have to dump your adopted brother?"
            show chelsea blank
            "You shake your head, pushing the thoughts away. Now you're definitely getting ahead of yourself."
            "Meeting Damien's mom... If she's anything like Damien, you're sure that you'll do a good job."
            show chelsea sad
            "That doesn't make you any less nervous."
            show chelsea shocked
            show Damien Happy
            pcname "Ah... Okay. That sounds good."
            show chelsea confused
            pcname "When did she want to meet me...?"
            show Damien Neutral
            show chelsea sad
            D "She's pretty busy with work right now, but I'll talk to her and we'll figure something out."
            "Noticing the change in atmosphere, Damien carefully wraps an arm around your shoulder and kisses the top of your head."
            show Damien Happy
            show chelsea embarrassed
            D "It's nothing for you to be worried about. I'm sure it'll go great."
            show chelsea sad
            "He gently pulls away and turns to walk back to his car."
            show Damien Laugh
            D "I'll see you at school, [pcname]!"
            show chelsea laugh
            pcname "See you then!"
            hide Damien Laugh with moveoutleft
            show chelsea sad
            "With a little wave, Damien walks back to his car and drives off. You enter the apartment alone, your thoughts consumed with how to make a good impression on Damien's mother."
            jump events_end_period
        "I'd rather stay home." if True:
            show chelsea blank
            "You glance back at your comfortable spot on the couch and then at your TV, the urge to be lazy and stream TV while you gouge on Chinese food overriding any of your desire for a date."
            show chelsea sad
            pcname "I was actually about to start watching some shows here..."
            menu damien_homeinvite:
                "Invite Damien to join you." if True:
                    show chelsea embarrassed
                    pcname "Do you want to watch them with me?"
                    show Damien Happy
                    "Damien smiles, seemingly relieved by the invitation."
                    if damienconfidence >= 50:
                        D "Sure."
                        show chelsea happy
                        "Damien settles on the couch comfortably, pulling you down against his side to cuddle more effectively."
                    elif True:
                        show Damien Neutral
                        D "If-- If that's okay..."
                        show Damien Happy
                        show chelsea happy
                        "Damien settles on the couch, careful not to take up too much room, and you lean against him, cuddling up against his side."
                        "His body tenses up upon the impact but slowly relaxes, his arm hesitantly finding its way around your waist."
                    pcname "Are you hungry? I was thinking of ordering some Chinese food."
                    if damienconfidence >= 50:
                        show Damien Neutral
                        D "Yeah, but let me take care of it. I'm the one that crashed your evening."
                        show chelsea confused
                        show Damien Blank
                        pcname "Are you sure? You don't have to--"
                        show Damien Happy
                        D "It's fine. Just tell me what you want and I'll take care of it."
                        show chelsea happy
                        pcname "Thanks, Damien."
                    elif True:
                        show Damien Neutral
                        D "L-Let me take care of it! I'm the one that barged in like this..."
                        show chelsea confused
                        show Damien Blank
                        pcname "It's fine, I really don't mind."
                        show chelsea shocked
                        show Damien Neutral
                        D "Please? It would make me feel better about showing up unexpected..."
                        show chelsea happy
                        show Damien Happy
                        pcname "Well, if you really want to, sure."
                    show chelsea blank
                    "Damien smiles gratefully and picks up the discarded Chinese food menu you left on the coffee table, briefly viewing his choices before calling the restaurant."
                    "One lengthy order and twenty minutes into your show later, the food arrives, and you both take a break to divvy up the bag's contents."
                    "Once your food is settled, you reach for the remote, ready to start up the show again, but Damien speaks up, catching your attention."
                    show Damien Neutral
                    show chelsea confused
                    D "Ah, [pcname], there's something I wanted to talk to you about, actually..."
                    D "Do you have any plans for the Day of Harvest in a few weeks?"
                    show chelsea shocked
                    show Damien Blank
                    "You're caught off guard by his question but shake your head."
                    show chelsea sad
                    "Day of Harvest is typically a holiday celebrating family, and with both of your parents dead, there's not really much to celebrate."
                    show Damien Happy
                    show chelsea blank
                    D "Well, my family is going to be away that weekend. They usually go up to a cabin we rent in the woods, but I'm staying behind to watch my brother's dogs."
                    show chelsea shocked
                    "Your eyebrows rise up in surprise."
                    pcname "You're not going up with them? Can't someone else watch the dogs?"
                    show Damien Neutral
                    show chelsea blank
                    D "They usually get one of his friends to do it, but everyone's pretty busy this year."
                    show Damien Happy
                    D "Besides, I thought it would be nice to spend the holiday weekend together. If you want, I mean."
                    if damienconfidence >= 50:
                        "Damien smiles at you with a glimmer of hope in his eyes, and you can tell he's already planning the romantic weekend in his head, intending to make as much use of the time as he can."
                    elif True:
                        "Damien glances at you sheepishly, a small glimmer of hope in his eyes as he nervously twists his hands together, waiting for the inevitable rejection."
                    show chelsea happy
                    show Damien Blank
                    pcname "That sounds great. I don't have any plans for the Day of Harvest, so..."
                    show Damien Shocked
                    show chelsea laugh
                    D "Really? Awesome. I mean-- cool. Yeah, cool."
                    show Damien Happy
                    show chelsea blank
                    D "I'll set something up for us, then. It'll be really romantic..."
                    show chelsea embarrassed
                    "The idea of Damien planning your whole date excitedly makes your heart flutter. It's such an innocent, sweet gesture that you can't help but feel excited about it yourself."
                    show chelsea happy
                    pcname "I'm looking forward to it. Now I just wish the holiday wasn't so far away..."
                    show Damien Laugh
                    D "Yeah... You and me both."
                    show Damien Blank
                    "Damien sighs in contentment, his gaze slowly trailing back to the pile of Chinese food on the table. He blinks, as if just recognizing it for the first time."
                    show Damien Neutral
                    D "Ah, we should eat our food before it gets cold."
                    show chelsea shocked
                    pcname "Oh, right!"
                    show Damien Happy
                    show chelsea happy
                    "With that, you both dig into your meals and resume binging the TV show, your thoughts wandering back to the possibilities of what Damien might plan for the Day of Harvest."
                    hide chelsea with dissolve
                    hide Damien Happy with dissolve
                    show bg black with dissolve
                    jump events_end_period
                "You want to be alone." if True:
                    show chelsea confused
                    show Damien Sad
                    "An awkward silence stretches between you, and Damien slowly realizes that the invitation was not extended to him."
                    show Damien Neutral
                    show chelsea sad
                    D "Ah, right... I have some, uh... stuff to take care of at home, actually."
                    show Damien Happy
                    show chelsea blank
                    D "I'm glad you like the flowers, [pcname]."
                    show chelsea shocked
                    show Damien Shocked
                    "Damien walks toward the door but pauses in the threshold, his face lighting up with realization."
                    show chelsea confused
                    D "Oh! Before I forget, there was another reason I wanted to see you today."
                    show Damien Neutral
                    show chelsea blank
                    D "My family is going away in a few weeks for the Day of Harvest. I'll be staying home, so maybe we can have a weekend-long date."
                    show Damien Blank
                    show chelsea shocked
                    "He lets the words sink in and all of the implications that come with it."
                    show chelsea happy
                    "A whole weekend alone at Damien's house... There's a lot you could get up to while his parents are away. You've never been to a sleepover quite like that before; the thought excites you a little."
                    show Damien Happy
                    D "Anyway, enjoy your shows, [pcname]. Text me about them!"
                    hide Damien Happy with moveoutleft
                    "Damien smiles and steps back out into the cold, gently shutting the door behind him."
                    show chelsea blank
                    "As you sit down to enjoy your TV shows, your mind continues to wander back to Damien's suggestion, and you can't help but wonder what his house and family are like."
                    show chelsea confused
                    "You know next to nothing about Damien's family, or what his house looks like, or even where he {i}lives{/i}."
                    show chelsea happy
                    "Staying there for the weekend will be a whole new experience and you find yourself really looking forward to it."
                    show chelsea laugh
                    "This will be a fun Day of Harvest!"
                    hide chelsea with dissolve
                    show bg black with dissolve
                    jump events_end_period
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
