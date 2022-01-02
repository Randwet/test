label violetdom3:
    show bg Cafeteria with fade
    show chelsea embarrassed at right with moveinright
    "You deliver Violet's lunch to the table, placing it in front of her as she taps away on her phone."
    show V School Pout at left with moveinleft
    "She glances up, barely acknowledging you."
    show chelsea blank
    "You take a seat, waiting for her to take a bite so that you can start eating too."
    show chelsea sad
    "Your toasted cheese sandwich looks amazing and you can practically feel the gritty, greasy bread on your tongue..."
    "School lunches are never great, but the melted processed cheese is a guilty pleasure."
    "And it does bring back memories of your mom's grilled cheese..."
    show chelsea confused
    show V School Blank at left
    V "Didn't they have fresh fruit?"
    show chelsea blank
    show V School Pout at left
    "Pulled abruptly from bittersweet memories of your mother's cooking, you shake your head to clear it."
    "Violet gestures to the fruit on her tray; it's obviously mixed fruit from a can."
    show chelsea sad
    pcname "No, sorry."
    show V School Blank at left
    "She sighs loudly."
    V "Whatever. Anyway, we're going to a party this weekend."
    if club == "track":
        show chelsea confused
        pcname "We are?"
    elif club == "cheer":
        show chelsea happy
        pcname "A party?"
    elif club == "yearbook":
        show chelsea shocked
        pcname "W-what?"
    V "I was invited by the son of one of my father's co-workers."
    show V School Pout at left
    "She rolls her eyes."
    show chelsea blank
    show V School Blank at left
    V "I doubt I'll know anyone there, so I thought you could come with me."
    show chelsea happy
    pcname "Really?"
    show V School Smile at left
    "She smiles, sending a chill of anticipation down your spine."
    V "I'll introduce you as my personal assistant and you can serve me."
    show chelsea embarrassed
    if club == "track":
        "The thought of being submissive to her in front of so many people still makes your chest tighten and your heart pound."
        "It's almost like the feeling you get right before a race."
    elif club == "cheer":
        "The thought of being submissive to her in front of so many people..."
        "It's thrilling."
    elif club == "yearbook":
        "The thought of being submissive to her in front of so many people... It still makes your chest tighten and your heart pound."
        "You swallow back your nervousness, nodding slowly."
    show V School Blank at left
    V "I've already confirmed, so I'll meet you at your apartment Saturday."
    show chelsea blank
    show V School Pout at left
    "She spares you a quizzical glance."
    show V School Blank at left
    V "Not hungry?"
    show chelsea shocked
    "You look down, only now seeing her half-eaten tray of food. You'd been so caught up in your own thoughts..."
    "Lunch is almost over and you haven't even started eating!"
    show V School Smile at left
    show chelsea embarrassed
    "She laughs as you grab your sandwich, dip it in your tomato soup, and jam it in your mouth."
    show chelsea blank
    "You barely taste it before swallowing that bite and taking another."
    show V School Pout at left
    "You're still spooning soup into your mouth when the bell rings."
    show V School Blank at left
    V "I'll leave my tray here for you. Don't forget about Saturday!"
    hide V School Blank with dissolve
    "Lifting your bowl to your lips, you guzzle down the rest of your soup and jump up from the table."
    "After dumping both trays, you race to your next class - barely making it to your chair in time!"
    $ violetdateflag = True
    jump events_end_period

label violetdom3_date:
    $ VCasualBlank = "Characters/Violet/Casual/Party/Neutral.png"
    $ VCasualPout = "Characters/Violet/Casual/Party/Pouting.png"
    $ VCasualAnnoyed = "Characters/Violet/Casual/Party/Annoyed.png"
    $ VCasualSmile = "Characters/Violet/Casual/Party/Smile.png"
    $ VCasualSuprised = "Characters/Violet/Casual/Party/Suprised.png"
    $ violetdatescore = 0
    play sound PhoneVibration
    "Your phone vibrates."
    call screen TextingScene("Violet",
    [
        TextMessage("I'm leaving soon"),
        TextMessage("Hope you're ready for the party")
    ])
    "You walk into the bedroom and look yourself over."
    $ clothes, hair = casualwear
    "Just as you finish getting ready, you get another text."
    call screen TextingScene("Violet", [TextMessage("I'm here!")])
    show chelsea at right with moveinright
    show bg black with dissolve
    "You head outside, where Violet is standing by her car, keys dangling from one finger."
    show bg CityE with dissolve
    show V Casual Smile at left with moveinleft
    "She looks amazing in a long black dress with a scooping neckline and a high slit up one side of the skirt."
    "Her breasts swell up from the neck of the dress, tempting you with their soft roundness."
    "The ruffled layers of her skirt billow in the light breeze, teasing you with glimpses of her calves and thigh."
    "She lets you stare a few seconds before clearing her throat."
    V "Well?"
    show chelsea embarrassed
    "You take the keys and open the door for her, trying not to stare at her long, smooth legs as she slides into the back seat."
    hide V Casual Smile with dissolve
    show chelsea blank
    "Shutting the door behind her, you climb into the driver's seat and turn on the car."
    "While the GPS directs you across town, Violet tells you about her morning."
    show V Casual Pout at left with dissolve
    V "It took {i}forever{/i} for them to fix, but I couldn't go to the party with a crooked nail!"
    "Arriving at a gate, you stop the car and look over your shoulder at Violet."
    show chelsea confused
    pcname "Umm..."
    "She shakes her head."
    show V Casual Annoyed at left
    show chelsea blank
    V "What are you doing? Roll down the window."
    "Rolling the window down, you hear a voice coming across a speaker - which you quickly realize is built into the gate."
    show V Casual Pout at left
    "Speaker" "Name?"
    if club == "track":
        show chelsea confused
        pcname "Violet?"
        show V Casual Blank at left
        V "Atwood."
        pcname "Violet Atwood."
    elif club == "cheer":
        pcname "It's Violet..."
        show V Casual Blank at left
        V "Atwood."
        pcname "...Atwood."
    elif club == "yearbook":
        show chelsea embarrassed
        pcname "V-Violet...?"
        show V Casual Blank at left
        V "Atwood."
        pcname "Um, At-Atwood?"
    show V Casual Pout at left
    "Speaker" "Good evening, Miss Atwood. Please proceed."
    show chelsea blank
    "The gate opens slowly, allowing you to drive up a long driveway ending in a circle at the front of a huge house."
    show chelsea shocked
    if club == "track":
        pcname "That's a mansion. An actual mansion."
    elif club == "cheer":
        pcname "That's a mansion!"
    elif club == "yearbook":
        pcname "It's... big."
    show V Casual Smile at left
    V "Oh, right, you've never seen {i}my{/i} house, have you?"
    show V Casual Pout at left
    "She waves dismissively and looks back at her phone."
    show chelsea blank
    "Two men approach the car, opening the doors for both of you."
    "As you step out, one of the men holds out his hand."
    show V Casual Blank at left
    V "Give the valet the keys, [pcname]."
    show chelsea shocked
    show V Casual Pout at left
    if club == "track":
        pcname "Valet! Right."
    elif club == "cheer":
        pcname "Oh, you're the valet? Right..."
    elif club == "yearbook":
        pcname "Oh. Sorry!"
    show chelsea blank
    "Violet leads the way into the house, pausing at the entrance to give her name to the doorman."
    show bg black with dissolve
    show bg LuxParty with dissolve
    "He leads you both inside, introducing \"Violet Atwood and her personal assistant\" to the party's host: an attractive man only a few years older than yourself."
    show V Casual Smile at left
    "Niles" "Violet! So glad you could make it. I'm Niles Bradford."
    "He takes her hand, squeezing it gently."
    "Niles" "You have to meet Jessica - our fathers were all in the same graduating class..."
    show V Casual Pout at left
    "He ignores you entirely, whisking Violet away to meet several men and women while you trail nervously behind."
    "Everyone is beautifully dressed - much better than you are - and their demeanor makes it quite clear that you're in a different world right now."
    "And yet, when they hear Violet's name they seem {i}excited{/i}."
    "Niles leaves you both with a small group of people - never even asking your name before he goes to welcome the rest of his guests."
    show V Casual Blank at left
    V "[pcname], I'd like a refreshment."
    show V Casual Pout at left
    "She barely glances in your direction, trusting you to obey her."
    if club == "track":
        "You take a look around. How hard can it be to find a drink?"
    elif club == "cheer":
        "Trying not to get distracted by all of the beautiful decor, you look for a drink table or... something."
    elif club == "yearbook":
        "Swallowing your nervousness - there are so many people! - you search for the kitchen."
    hide V Casual Pout with dissolve
    "After a few minutes, you realize you're going to need help."
    "Approaching a woman with a glass in one hand, you politely ask if she could direct you to the drinks."
    "Woman" "They're over that way."
    "She gestures toward a doorway, turning away before you have the chance to annoy her again."
    if club == "track":
        "Fighting back your own annoyance, you walk to the doorway and look around."
    elif club == "cheer":
        "Rolling your eyes, you walk to the doorway."
    elif club == "yearbook":
        "Heat suffuses your cheeks - you didn't mean to bother her - and you quickly make your way to the doorway."
    "But there doesn't appear to be any drinks in the next room either."
    "Sighing, you look for someone else to ask. There's a young man holding a glass nearby, and he seems to be alone..."
    if club == "track":
        "Swallowing your pride, you approach him."
        pcname "Excuse me, but I was sent for a drink and I can't seem to find them anywhere."
    elif club == "cheer":
        "Straightening your shoulders, you approach him."
        pcname "Excuse me, but I'm looking for a drink for my boss."
    elif club == "yearbook":
        show chelsea embarrassed
        "Biting your lip, you approach him."
        pcname "Excuse me, please, but I was sent to get a drink and I can't find them..."
    "Man" "They're around here somewhere."
    "He turns away, leaving you just as lost as before."
    pcname "Violet's going to be so mad..."
    "Abruptly, he turns back."
    "Man" "Wait... who sent you for a drink?"
    show chelsea confused
    pcname "Violet Atwood?"
    "Man" "Atwood? Here, let me show you..."
    show chelsea blank
    "He leads you to a table covered in glasses of wine, and even helps you pick one."
    "Man" "I'm sure she'll prefer the blush - the white is a little dry."
    show chelsea happy
    if club == "track":
        pcname "Thanks! You're a life saver."
    elif club == "cheer":
        pcname "Thank you {i}so{/i} much..."
    elif club == "yearbook":
        pcname "Th-Thank you. I would never have found them..."
    "Man" "No problem. If you don't mind, can you let Violet know James Pemberly helped you?"
    show chelsea confused
    pcname "Um, sure?"
    "He smiles and nods as you walk back the way you came."
    show chelsea blank
    "It takes a few minutes, but eventually you find your way back to Violet."
    "She's talking to the host - Niles - and laughing."
    show V Casual Smile at left with dissolve
    "Niles" "I can't believe he really followed through with that. An Atwood at public school!"
    show V Casual Suprised at left
    V "It's {i}awful{/i}. Oh, [pcname], that took a while!"
    show V Casual Smile at left
    show chelsea embarrassed
    pcname "Sorry, Miss Violet... I couldn't find the table at first. I'm supposed to let you know that James--"
    show V Casual Pout at left
    "She takes the glass from your hand and waves you to silence."
    show V Casual Smile at left
    show chelsea blank
    V "She's still new to the job. Anyway, public schools are the {i}worst{/i}. You should see it."
    "She takes a drink of her wine and smiles."
    V "This is {i}good{/i}, Niles."
    "Niles" "You should try the hors d'oeuvres too. We had freshly harvested caviar flown in this morning."
    V "{i}Really{/i}? [pcname], go get a plate. And don't take so long this time!"
    if club == "track":
        show chelsea happy
        pcname "Yes, Miss Violet."
        "You didn't see an appetizer table earlier - but you weren't really looking either."
    elif club == "cheer":
        pcname "Of course, Miss Violet."
        "You don't remember seeing food anywhere, but it has to be near the drinks, right?"
    elif club == "yearbook":
        show chelsea embarrassed
        pcname "R-Right, Miss Violet."
        "The thought of wandering through crowded rooms again makes you sick to your stomach, but what can you do?"
    hide V Casual Smile with dissolve
    "Traversing the rooms, you make your way back to the drink table."
    show chelsea blank
    "On the far side of the room, you see a table with loads of small plates - and a huge line."
    show chelsea confused
    pcname "She said not to take so long, but that line..."
    "Remembering how the man reacted to Violet's name earlier, you have an idea."
    show chelsea blank
    menu violetdom3_party_namedrop:
        "Name drop." if True:
            $ namedrop = True
            if club == "track":
                "You approach the table hesitantly."
                pcname "Excuse me, is this the line for hors d'oeuvres?"
                "Woman" "The line starts back there."
                pcname "Thank you. My boss, Violet Atwood, sent me for some and I wasn't sure..."
                "Woman" "Violet Atwood?"
                "She glances behind her."
                "Woman" "Niles wouldn't want to keep her waiting, I'm sure. Step in front of me."
                show chelsea shocked
                "As you do, a man further back leans out from his spot in the line."
                "Man" "Hey--"
                show chelsea blank
                "She turns to glare at him."
                "Woman" "She's getting a plate for {i}Violet Atwood{/i}. Do you want to make her wait?"
                "The man shuffles back into his spot while several others murmur behind you."
                "In only a few minutes, you step away from the table with a plate full of appetizers."
            elif club == "cheer":
                "You approach a woman who is filling a plate at the table."
                show chelsea happy
                pcname "Excuse me, but Violet Atwood sent me for some hors d'oeuvres. Is this the right table?"
                "Woman" "Violet Atwood?"
                "She glances behind her."
                "Woman" "There's quite the line, but..."
                "She passes you her plate and smiles."
                "Woman" "Tell her Sierra Klinshaw says hello."
                "Having given you her plate, she walks to the back of the line."
            elif club == "yearbook":
                "Approaching the end of the table, you get the server's attention."
                show chelsea embarrassed
                pcname "Sorry, but Niles was talking to my boss, Violet Atwood and they--"
                "Server" "Atwood? One moment, ma'am."
                show chelsea shocked
                "He grabs a plate and walks up and down the table, piling the plate with the best looking appetizers."
                "Server" "Niles was sure she wouldn't come. Please, give her that plate."
                "Taken aback, you thank him and step away from the table."
        "Wait in line." if True:
            "It seems wrong to use Violet's reputation to skip the line, so you patiently take your spot at the end."
            "A long while later, you step away from the table with a plate of food."
    show chelsea blank
    "When you get back to Violet, she's laughing at something Niles said."
    show V Casual Smile at left with dissolve
    pcname "Your hors d'oeuves, Miss Violet."
    if namedrop == True:
        V "Thank you, [pcname]."
        show chelsea happy
    elif True:
        show V Casual Annoyed at left
        V "What took so long!"
        show chelsea sad
        pcname "Sorry, there was a line and--"
        "She rolls her eyes, turning back to Niles."
        V "Why is it {i}so hard{/i} to find competent help?"
        "Flushing, you stare at the floor."
    "Niles" "Unfortunately, I should speak with some of my other guests..."
    show chelsea shocked
    "Niles" "Perhaps we could continue this another time? Saturday, maybe?"
    "He smiles charmingly, his blue eyes sparkling."
    show chelsea embarrassed
    "He's not even talking to you, but your heart flutters."
    show V Casual Smile at left
    "Still, you're surprised when Violet responds with a smile."
    V "That would be wonderful! I'll check my calendar and get back to you."
    "Niles" "It's a date then."
    show chelsea blank
    "He leaves with a smile and a wink; you can hardly blame her for being charmed by him."
    menu violetdom3_party_date:
        "Ask if she's really going out with him." if True:
            show V Casual Pout at left
            "She frowns at you, shaking her head."
            show V Casual Blank at left
            V "That's really up to me, isn't it?"
            show chelsea sad
        "Stay quiet." if True:
            "Though you're bothered by the exchange, you know it's not your place to question her."
    show V Casual Pout at left
    "She takes a bite of one of the little toasts on her plate and makes a face."
    show chelsea blank
    show V Casual Annoyed at left
    V "If it's not beluga, he shouldn't bother calling it caviar..."
    show V Casual Pout at left
    "Passing you the plate, she walks around mingling while you nibble at the various dishes."
    "Maybe your palate isn't refined enough, but none of it tastes as good as you'd expected."
    "An hour later, Violet turns to you and sighs."
    show V Casual Blank at left
    V "I've had enough. I think it's time to go home."
    show V Casual Pout at left
    "She leads you to the front door and waits for you to open it for her."
    show bg black with dissolve
    "Outside, the valets bring her car around and open the doors before passing you the keys."
    show V Casual Smile at left
    show bg CityD with dissolve
    "As you drive back to the apartment, Violet smiles."
    V "So what did you think of Niles?"
    menu violetdom3_party_impression:
        "He's very handsome." if True:
            show chelsea happy
            "She smiles."
            V "He is, isn't he?"
        "He's stuffy." if True:
            pass
    "Her eyes meet yours in the rear-view mirror and she laughs."
    V "You should see your face!"
    V "Don't worry; I'm not going out with him."
    show chelsea happy
    V "I couldn't just turn him down because of who his father is, but I'm {i}not{/i} interested."
    "Her words take the edge off your anxiety, but you can't help feeling intimidated by her importance."
    "The way everyone reacted to the mention of her name..."
    show V Casual Pout at left
    if club == "track":
        show chelsea shocked
        "You're lucky to be allowed to serve someone so powerful."
    elif club == "cheer":
        show chelsea happy
        "You're lucky to be allowed to serve someone so high class."
    elif club == "yearbook":
        show chelsea embarrassed
        "You're lucky just to be allowed to serve her. She's so far above you..."
    show chelsea blank
    "Pulling into your apartment, you shift the car into park and quickly open her door for her."
    "Stepping out of the car, she takes you by the shoulders and pulls you roughly against her."
    show chelsea embarrassed

    "Her lips meet yours, pushing them open so that her tongue can explore your mouth."
    "One hand releases your shoulder to run down your chest, cupping your breast and squeezing playfully."
    "A trail of heat follows her touch; your nipple hardens beneath her hand."
    "When she breaks the kiss off, you sway forward in a daze, barely finding your footing."
    show V Casual Smile at left
    "Giving your breast another gentle squeeze, she smiles."
    V "That was fun, but I'm getting bored with these games."
    V "Next time, I want to have some {i}fun{/i}."
    "She lets her hand fall away from your breast, skimming the tip of your nipple as it does, and steps away from you."
    V "Do you understand?"
    if club == "track":
        "Your voice is thick with desire."
        pcname "Yes..."
    elif club == "cheer":
        "You lick your lips - they're already swollen with desire."
        pcname "Yes, Violet..."
    elif club == "yearbook":
        "Taking a shuddering breath, you nod."
        pcname "Y-Yes..."
    V "Good. I'll see you soon."
    "Stepping around you, she gets into the car and waits as you close it behind her."
    hide V Casual Smile dissolve
    "You watch her drive away, wondering what she has planned for your next encounter."
    $ acts -= 2
    $ violetdateflag = False
    $ VCasualBlank = "Characters/Violet/Casual/Casual Neutral.png"
    $ VCasualPout = "Characters/Violet/Casual/Casual Pouting.png"
    $ VCasualAnnoyed = "Characters/Violet/Casual/Casual Annoyed.png"
    $ VCasualSmile = "Characters/Violet/Casual/Casual Smile.png"
    $ VCasualSuprised = "Characters/Violet/Casual/Casual Suprised.png"
    jump events_end_period
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
