label choosedomtitle:
    $ domtitle = renpy.input("What would you like your title to be?", default = "Mistress", length = 12)

    if domtitle == "":
        $ domtitle = "Mistress"

    menu violetsub4_dinner_title:
        "You've chosen [domtitle]. Is this correct?"
        "Yes!" if True:

            pcname "Then call me [domtitle]."
        "No, I want to change it." if True:
            jump choosedomtitle

    return

label violetsub4_dinner:
    $ clothes, hair = casualwear
    scene bg CityE

    show V SubParty Blank at right with dissolve
    "After work, you find Violet waiting by her car, ready to open the door for you."
    show V SubParty Happy
    V "How was work?"
    show chelsea with dissolve
    if katerelate == "girlfriend":
        show chelsea embarrassed
        "You think of Kate in her maid uniform, smiling brightly."
        show chelsea sad
        show V SubParty Sad
        "A pang of guilt shoots through your chest."
        show chelsea blank
        show V SubParty Worried
        pcname "It was... fine."

    elif job == "cafe":
        show chelsea happy
        if club == "track":
            pcname "Not too bad."
        elif club == "cheer":
            pcname "I've had worse shifts."
        elif club == "yearbook":
            pcname "It wasn't bad, but I'm glad to be done..."
        show V SubParty Blank
    elif job == "bakery":
        show chelsea sad
        if club == "track":
            pcname "Not much fun, honestly."
        elif club == "cheer":
            pcname "Ughh..."
            "Rolling your eyes, you get into the car."
        elif club == "yearbook":
            pcname "My boss is... well..."
            pcname "A little hard to please."
        show V SubParty Sad
    elif job == "bar":
        show chelsea embarrassed
        if club == "track":
            pcname "Busy. I'm beat!"
        elif club == "cheer":
            pcname "Oh, it's always a lot of fun there..."
        elif club == "yearbook":
            pcname "Oh, i-it was fun..."
    show chelsea at exitScene(0.5, 1.0, 0.3, 0.3)
    "Shutting your door, Violet circles around to the driver's seat and gets in too."
    hide V SubParty with dissolve
    pcname "So where are you taking me for dinner?"
    scene black with dissolve
    "Violet smiles - it's a slow, almost hesitant smile. On anyone else, you'd call it shy."
    show V SubParty Blank at right with dissolve
    V "I was hoping it could be a surprise...?"
    hide V SubParty with dissolve
    show chelsea embarrassed with dissolve
    "Smiling back, you nod."
    show chelsea laugh
    pcname "If you want. Let's hope you picked well."
    hide chelsea with dissolve
    show V SubParty Worried at right with dissolve
    "Swallowing hard, Violet nods."
    show V SubParty Sad
    V "I hope you don't mind, but I brought you something to wear..."
    hide V SubParty with dissolve
    show chelsea with dissolve
    "Glancing across the seat, you see a white box."
    show chelsea confused
    pcname "You don't like what I'm wearing?"
    $ dressList.dresses[0].bought = True
    hide chelsea with dissolve
    show V SubParty Worried at right with dissolve
    V "No! It's just... I didn't want you to feel out of place."
    show V SubParty Sad
    "Inside the box, you find a classy blue dress and a pair of heels."
    $ clothes = "bluedress"
    "It's easy enough to change in the back seat."
    show V SubParty Blank
    V "Also, I was thinking..."
    show V SubParty Sad
    "She pauses, searching for words."
    hide V SubParty with dissolve
    show chelsea with dissolve
    pcname "Yes?"
    "To your surprise, her cheeks flush."
    hide chelsea with dissolve
    show V SubParty Worried at right with dissolve
    V "Well... I was thinking that I shouldn't be calling you [pcname] anymore."
    hide V SubParty with dissolve
    show chelsea confused with dissolve
    pcname "True... What did you want to call me?"
    "Her cheeks grow pinker."
    hide chelsea with dissolve
    show V SubParty Blank at right with dissolve
    V "I... I think you should pick. I'll call you whatever you want."
    call choosedomtitle from _call_choosedomtitle
    show V SubParty Happy
    V "Yes, [domtitle]. Thank you."
    hide V SubParty with dissolve
    show chelsea embarrassed with dissolve
    if club == "track":
        "She says your new title with such reverence... You can't help but grin."
    elif club == "cheer":
        "The way she says your new title with such reverence brings a smile to your lips."
    elif club == "yearbook":
        "The way she says your new title brings a rush of heat to {i}your{/i} cheeks too."
    if corruption > 40:
        "You can't help imagining how it'll sound when you fuck her."
    elif corruption > 25:
        "You can't help imagining how it'll sound in the bedroom."
    elif True:
        "You can't help feeling important. Empowered."
    hide chelsea with dissolve
    "Violet parks the car in front of a chic italian place."
    "You've never heard of it, but from the way Violet watches for your reaction, you feel like you should."
    show chelsea with dissolve
    pcname "Hm. This might not be {i}too{/i} bad."
    hide chelsea with dissolve
    show V Party Suprised at right with dissolve
    "Violet's eyes widen, and for the first time you realize that she's nervous."
    "Violet. {i}Nervous{/i}."
    hide V Party with dissolve
    "She holds the door for you to walk inside, where the hostess greets you warmly."
    scene black with dissolve
    show GWaitress with dissolve
    show chelsea at midright with dissolve
    show V SubParty Worried at right with dissolve
    "Hostess" "Good evening, ladies."
    hide V SubParty
    show V Party Blank at right
    V "Reservation for Violet Atwood."
    show chelsea shocked
    show V Party Pout
    "The woman doesn't even glance at her list."
    "Hostess" "Of course, Ms. Atwood. Right this way."
    scene black with fade
    "She leads the two of you to your table. Along the way, you take in the dim lighting and intimate atmosphere."
    "The tables are covered in fine white tablecloths, set with several glasses and lots of silverware, and most have only two chairs each."
    show GWaitress with dissolve
    "Hostess" "I hope this is acceptable, Miss?"
    show V Party Pout at left with dissolve
    "She pulls back the curtains to reveal a very private booth set into an alcove in the wall."
    hide V Party
    show V SubParty Happy at left
    V "Yes, perfect."
    show chelsea embarrassed at right with dissolve
    "Your heart jumps as you realize that this is a {i}very{/i} romantic restaurant."
    scene bg VSDDS1 with dissolve
    "The hostess waits until you both take a seat, then lays a menu in front of each of you."
    if club == "track":
        "This isn't the kind of place you {i}ever{/i} thought you'd be in."
    elif club == "cheer":
        "This is the kind of place you only {i}dreamed{/i} you'd find yourself in."
    elif club == "yearbook":
        "There are so many utensils, and two glasses - why are there two glasses? - and..."
        "You take a deep breath, trying to control your racing thoughts."
    V "Do you like veal, [domtitle]? The Tonnato is shaved veal and tuna sashimi."
    "You pick up the menu, staring at the unfamiliar words."
    "You recognize some of the words, but the descriptions don't make sense to you."
    "Each item has a name, followed by several other words in a list."
    "Carmelle di Gorgonzola con Pera. Bleu Cheese. Red Wine. Poached Pear."
    "You know the words - most of them, anyway - but you have no idea what the dish will look like. Or taste like."
    show bg VSDDS2 with dissolve
    V "Or the Fegato is good. It's chicken liver mousse on piccolina toast with some roasted pear..."
    "You've had chocolate mousse, but chicken liver? You don't know how to feel about that - let alone with pear..."
    "Your eyes catch the word spaghetti and, for a moment, you sigh with relief."
    "Spaghetti. Blue crab. Lemon. Bottarga. Chilies."
    "What does that {i}mean{/i}? What will it taste like? What is {i}Bottarga{/i}?"
    V "I usually get the Anatra. It's duck with fregola, radish, and quince, in a chicken au jus."
    "Violet looks up from her menu, watching your reaction."
    V "Oh. You probably wanted the tasting menu, didn't you?"
    "She closes her menu, fixing her eyes on the table."
    show bg VSDDS3 with dissolve
    V "Of course! Sorry, [domtitle]. This is my favorite restaurant and I got carried away."
    "As she speaks, your eyes catch the words \"Tasting Menu\" on the page."
    "\"Less a meal and more of an experience, Chef Andre's 11-course tasting menu highlights the best techniques, ingredients, and flavors from around the world.\""
    "It continues for several more lines, but there doesn't seem to be a description. And 11-courses?"
    "Still, it might be better than trying to choose for yourself."
    show bg VSDDS4 with dissolve
    pcname "Of course. You can order for both of us, since she seems so impressed with your name."
    "Violet shifts in her seat."
    pcname "Wonder what she'd think if she knew who's {i}really{/i} in charge here."
    "Violet's cheeks color again and she looks down at the table."
    "The waitress approaches and Violet orders for both of you."
    show bg VSDDS5 with dissolve
    "You tell Violet a little about your shift at work. To your surprise, she listens intently."
    "Compared to when you first met, Violet seems like a different person."
    "She still talks about herself a lot, but usually only when she's nervous."
    "It's almost as if her narcissism is a front for her insecurities."
    show bg VSDDS6 with dissolve
    "The waitress brings out two large plates and two glasses of wine, setting one in front of each of you."
    "On the plate, carefully arranged, are three appetizers."
    "One sits in a tiny cup, another is prepared inside a large, ceramic spoon, and the last is in a shallow bowl."
    "The waitress explains what each dish is, but you barely understand the words."
    "Whatever they are, though, they {i}look{/i} amazing."
    "As soon as she leaves, dropping the curtain back into place to give you privacy, Violet smiles."
    V "Most of this isn't even on the menu, [domtitle]."
    "You nod, trying to seem confident. In some ways, though, Violet's obvious attempt at impressing you makes you {i}feel{/i} more confident."
    "This new relationship seems to be having a good effect on both of you."
    "Violet watches as you taste each of the dishes, seemingly more interested in your reaction than trying them for herself."
    "The first two are delicious, even if you don't know what they are."
    show bg VSDDS7 with dissolve
    "But the third one - some kind of soup, maybe? - is cold and, though the flavor is complex, not very good."
    "Frowning, you set your spoon back in the bowl and force yourself to swallow it."
    if corruption > 25:
        "Usually you're better at swallowing."
    V "Oh, the gazpacho... It's a bit of an acquired taste."
    "You frown - you'd been trying not to let Violet see your distaste for it."
    V "I'm sorry, [domtitle]. Maybe I should have picked the food for you. I know what you like better than the chef does..."
    "Surprised, you smile. You'd been expecting her to tell you why the food is so {i}amazing{/i} and {i}expensive{/i}."
    "Instead, she seems more concerned with {i}your{/i} opinion."
    show bg VSDDS8 with dissolve
    pcname "It's fine. It's a tasting menu, right? Well, I tasted it."
    "She laughs and you find yourself joining her."
    pcname "Besides, with eleven courses, I'm sure I won't go hungry."
    pcname "Unless this is three courses..."
    V "Right? They really do give you just enough to taste it, don't they?"
    show bg VSDDS9 with dissolve
    "Laughing again, you taste the wine - realizing belatedly that they didn't even ask your ages."
    "It's light and fruity, but not overly sweet."
    V "Mmm... The wine is really good with the tartare."
    "You nod, taking another sip."
    "The waitress returns a few minutes later with another plate and another wine."
    "Over and over, you're brought new \"courses\", containing just a bite or two, and new wines."
    show bg VSDDS6 with dissolve
    "Some of the dishes are better than others, but most are {i}incredible{/i}."
    "Waitress" "I hope you ladies have enjoyed everything so far. I'll be bringing your desserts out soon."
    "As she closes the curtain again, Violet smiles and leans toward you."
    V "The desserts here are {i}amazing{/i}. Seriously, it's my favorite part!"
    "It's the most excited you've ever seen her; she doesn't seem worried about anyone's opinion but her own."
    "And yours, of course."
    "Still, it feels like you've gone too easy on her tonight. You're supposed to be pushing her - making her work for things."
    show bg VSDDS10 with dissolve
    "A smile curls your lips."
    pcname "Violet."
    "Your shift in tone catches her attention; suddenly, she looks nervous."
    V "Yes, [domtitle]...?"
    pcname "If you want dessert, get under the table."
    "Her mouth falls open and her eyes widen."
    V "W-what?"
    if club == "track":
        pcname "You heard me. On the floor."
    elif club == "cheer":
        pcname "Oh, I think you heard me..."
    elif club == "yearbook":
        "You can barely believe your own boldness. Your heart races and your words come out in a breathy whisper."
        pcname "Get under the table."
    "Violet's mouth moves, but the words don't come out."
    "You watch her expectantly and, slowly, she slips from her seat."
    show bg VSDDS11 with fade
    "Her head disappears below the table's edge, and then you feel her hands on your knees."
    "Her fingers run up your outer thighs, looping through the edges of your underwear and drawing them down."
    "Scooting forward on the seat, you lean back, releasing a breath you didn't realize you were holding."
    "Her lips start at your knee, kissing their way lightly up your inner thigh."
    "Her breath tickles your labia as she covers them in soft kisses."
    "Between the public setting and knowing the waitress will be back soon, even these small caresses are more arousing than usual."
    "Your heart pounds as Violet presses her lips to your labia, allowing her tongue to dip between them."
    "What if the waitress comes back? What if someone can see under the table? Why does this feel so much {i}better{/i} knowing you could get caught?"
    "Violet's lips move over your labia as her tongue runs up and down between them."
    "The gentle pressure leaves you squirming in your seat, eager for more."
    pcname "Better hurry. If I'm not satisfied, you won't get any dessert."
    "Her tongue presses into you, wriggling inside your cunt."
    "Absently, you spread your legs further, exhaling in a soft moan."
    if club == "track":
        pcname "Oh fuck..."
    elif club == "cheer":
        pcname "Ohhh, yes..."
    elif club == "yearbook":
        pcname "Ohhh~"
    "Her tongue thrusts in and out of your pussy, until you nearly forget where you are."
    "Waitress" "Here we are."
    "She pauses a moment to set up a serving stand before opening the curtains."
    show bg VSDDS15 with dissolve
    "Waitress" "We have {i}pots de creme{/i}..."
    "You smile up at her, nodding politely, but her words are lost against the sound of your heart thumping in your ears."
    "Waitress" "Please, enjoy."
    "She steps back, closing the curtain behind her."
    "You're almost overwhelmed by the sudden rush of sensation that follows, as a sudden surge of adrenaline makes your body more sensitive than ever."
    "Violet pulls away, gasping for breath."
    V "I thought for sure she would notice..."
    pcname "These look really good. You'd better hurry..."
    "You hear a short, frustrated sound - and then her lips fasten around your clit."
    "Sucking gently, she presses two fingers to your pussy, your arousal allowing her to easily thrust them into you."
    if club == "track":
        pcname "Oh fuck!"
    elif club == "cheer":
        pcname "Ohhh! Yes~"
    elif club == "yearbook":
        pcname "Ohhh! Ohh~"
    "Her fingers curl upward, pressing against your g-spot and rubbing hard."
    "Your pussy tightens around her as her tongue flicks across your clit."
    "Breathless, you sink your fork into a small square cake."
    "Lifting the fork to your lips, you take a bite."
    "Moaning - perhaps a little louder than you'd meant to - with pleasure, you quickly swallow the rich chocolate."
    pcname "Mmmmm... It's {i}so good{/i}..."
    "Violet's fingers press up against your g-spot, rubbing harder and faster."
    "Her tongue flicks across your clit faster and faster."
    "Your pussy tightens around her even more, clamping around her fingers and squeezing them tight."
    "Your thighs press against her face as you begin to shudder - and then your climax hits you hard and fast."
    show bg VSDDS12 with dissolve
    "Panting, you try not to cry out as your orgasm sweeps over you, leaving you shuddering in your seat."
    "Violet gasps as your thighs fall open, releasing her head."
    "She pulls your panties up as far as she can and then slides back up into her seat."
    show bg VSDDS13 with dissolve
    "Wiping her mouth with her napkin, she smiles at you."
    V "Did I do a good job, [domtitle]?"
    "Not trusting your voice, you give her a dazed smile and nod."
    V "May I have my dessert now?"
    show bg VSDDS14 with dissolve
    "Leaning over the table, you lift her fork and sink it into the cake."
    "Lifting it to her lips, you smile as she opens her mouth for you to feed her."
    pcname "Yes, you've been a very good girl..."
    "Her tongue - which only moments ago was inside you - pushes to the edge of her mouth as you push the cake between her lips."
    "Closing her lips around the fork, she sucks gently - just as she sucked your clit - as you withdraw the fork."
    V "Mmmm~ Delicious..."
    "She practically moans as she tastes it. You can't help but wonder if she can still taste {i}you{/i} as well."
    "As sexually charged as the act is, you realize how romantic it must look too."
    "You feed her each of the desserts, watching her face twist with pleasure as she enjoys each of them."
    "You'd never realized how sexy something like this could be."
    "After a bite of each, you hand her the fork and go back to your own dessert."
    "Each bite is better than the last, but what you {i}really{/i} want is to get Violet home..."
    scene black with dissolve
    "Pulling your panties back into place, you watch as Violet throws a pile of twenties onto the table."
    show chelsea confused at midright with dissolve
    pcname "How do you know the total?"
    show chelsea shocked
    show V Party Smile at right with dissolve
    V "Oh, that's not to pay the bill, [domtitle]. They'll charge that to my father's account. That's just the tip."
    "Blinking back your shock, you nod slowly."
    "The {i}tip{/i} is as much as you make in a week. More, maybe."
    show chelsea embarrassed
    hide V Party
    show V SubParty Happy at right
    V "We don't have to wait, if you don't want to."
    "Something about her smile makes your heart skip a beat."
    "Maybe it's the romantic atmosphere, or maybe it's knowing where those lips have been."
    show V SubParty Happy at exitScene(1.0, 0.5, 0.45, 0.45)
    pause 0.5
    show chelsea at exitScene(0.75, 0.25, 0.45, 0.45)
    "Standing, you let her lead you back to her car."
    scene black with fade
    "The drive to her apartment is longer than you remember. You can't stop thinking of her under the table, her lips on your pussy..."
    "When she parks in front of your apartment, she turns the car off."
    show V SubParty Blank at right with dissolve
    V "I'll get your door, [domtitle]."
    hide V SubParty with dissolve
    scene bg CityN with dissolve
    "She hurries around the car, holding your door open."
    show V SubParty Sad at midright with dissolve
    V "I... had a really good time tonight, [domtitle]."
    show chelsea at right with dissolve
    show V SubParty Happy
    pcname "It's not over yet. Close the door and come inside."
    show chelsea at exitScene(1.0, 0.5, 0.4, 0.4)
    pause 0.4
    show V SubParty at exitScene(0.75, 0.25, 0.4, 0.4)
    "Her excitement is obvious as she follows you to your apartment."
    scene black with dissolve
    "She holds the door for you, following you inside and then waiting."
    "Motioning for her to follow, you lead her to your bedroom."
    scene bg RoomN with dissolve
    show chelsea embarrassed with dissolve
    show V SubParty Blank at left with dissolve
    V "Did you want something, [domtitle]?"
    menu violetsub4_dinner_after:
        "Tease her." if True:
            $ violetcum += 1
            pcname "First, get those clothes off."
            show V SubParty Happy
            "She nods, her fingers moving to her shirt."
            scene black with fade
            "With each article of clothing she removes, she meets your eyes again, smiling softly."
            "As her panties join the rest of her clothes on the floor, she tilts her head questioningly."
            V "And now...?"
            pcname "Lay down on the bed."

            "Violet obeys and you follow, reaching out to run your hand down her chest."
            "Your fingers trail over her skin - soft, as always - circling her belly button and stopping just before her pussy."
            "She gasps at your touch, shuddering as you pull your fingers back again."
            pcname "You're so beautiful..."
            "The words escape before you have time to think, but Violet just smiles."
            "Taking her wrists in your hands, you lift her arms above her head."

            pcname "Keep your hands there and don't move them."
            "Breathing deeply, she nods."
            "Your hands move over her breasts, squeezing and massaging the soft flesh."
            "She gasps and moans - especially when your fingers skim her nipple - but keeps her hands where you put them."
            "Amused, you let your hands skim across her nipples again. And again."
            "Her nipples slowly stiffen with each contact, growing pink and puckered."

            "Her gasping and moaning grows louder each time, and eventually she begins jerking and shuddering with each touch."
            "Leaning over her, you fasten your lips around one nipple and suck gently."
            V "Ah~"

            "Enjoying her reaction, you draw your teeth over her nipple, grazing it."
            V "Ohhh~"
            "She shudders beneath you, pressing her breast up towards you."
            "Your teeth press around her nipple, biting down until she moans again."
            "Then, your teeth holding her nipple in place, you flick your tongue over it."
            "Her shoulders jerk as she tries to keep her hands in place."
            V "[pcname]... I mean... [domtitle]...."
            "Her shoulders jerk from side to side as she tries to pull her nipple from your mouth, but your teeth hold it in place."
            "She moans as her movements make your teeth tug at her nipple."
            "Your fingers find her other nipple, twisting hard."

            V "Ahh!"
            "She writhes beneath you, twisting and arching her back."
            V "I can't-- [domtitle], I can't--"
            "Releasing her nipples, you smile down at her."
            "Panting, she shivers beneath your gaze, slowly calming."
            "Your left hand falls to her breast, caressing the nipple you'd been biting."
            "Your right hand runs over her belly to cup her pussy."

            V "Ohh~"
            "She tries to shift her too-sensitive nipple away from your hand, lifting her hips to press your other hand harder against her pussy."
            "Your hands move with her, giving her neither relief nor greater contact."
            V "P-please, [domtitle]..."
            "You can feel the heat of her cunt beneath your hand, and the swollen nub of her clit."
            "Rolling her clit beneath your thumb, you smile as she gasps."
            V "Ohhh~"
            "Her nipple drags across your palm as you run your hand over her breast. Your thumb still on her clit, you run two fingers over her slit, pressing them to her opening."
            "Her pussy is hot, wet, and eager, letting your fingers slip inside without resistance."

            V "Oh fuck... [domtitle]..."
            "She spreads her legs for you, eager for your touch."
            "Your fingers tighten around her nipple, giving it a hard twist."
            V "Ah~"
            "For a few minutes you play with her, pinching and twisting her nipples, pumping your fingers in and out of her pussy, and rubbing her clit."
            "She writhes on the bed, shuddering and moaning, but manages to keep her hands above her head."
            "Eventually, though, it's too much."
            if violetcum > 1:
                V "Please, I've been good. I haven't cum since you told me not to..."
            elif True:
                V "Please... I want to cum..."
            if club == "track":
                pcname "You want to cum?"
            elif club == "cheer":
                pcname "Aww, do you want to cum?"
            elif club == "yearbook":
                pcname "So you... want to cum?"
            V "Yes, [domtitle]. Yes! {i}Please{/i}!"
            "Pulling your fingers from her pussy, you shove them into her open mouth."

            pcname "That's too bad. I don't think I want you to cum yet."
            "Violet's brows furrow and she lets out a low moan of disappointment and frustration."
            pcname "I just wanted to remind you that this..."
            "You move your fingers in and out of her mouth, before pulling them out again."
            pcname "...and this..."
            "Your hand moves to her nipple, giving it one last pinch."
            V "Ah~"
            pcname "...and this..."
            "Finally, you cup her pussy, gently teasing her opening with a single finger."
            pcname "...are all {i}mine{/i}."
            "Violet nods her understanding."
            V "Yes, [domtitle]..."
            scene bg RoomN with fade
            show chelsea embarrassed with dissolve
            "Stepping back, you smile down at her."
            pcname "Good. Then get dressed. It's getting late and you still have to drive home."
            show chelsea confused
            "Her mouth moves and, for a moment, you wait for her to protest."
            "Then she whimpers and climbs off the bed."
        "Go down on her." if True:
            $ violetcum = 0
            show V SubParty Happy
            pcname "First, get those clothes off."
            hide V SubParty with dissolve
            "She nods, her fingers moving to her shirt."
            scene black with fade
            "With each article of clothing she removes, she meets your eyes again, smiling softly."
            "As her panties join the rest of her clothes on the floor, she tilts her head questioningly."
            V "And now...?"
            pcname "Lay down on the bed."
            "She obeys, laying on her back and looking toward you."

            "Smiling down at her, you let your eyes run over her body."
            pcname "You're so beautiful..."
            "Her cheeks flush and she bites her lip."
            V "Thank you, [domtitle]."
            pcname "You were {i}very{/i} good tonight. I think that deserves a reward."
            "Violet waits obediently, her breathing just a little heavier than normal."
            "As you pause, leaving her wondering what you have planned, you watch as her nipples slowly darken, then begin wrinkling, the tips pushing forward."
            "Licking your lips reflexively, you continue:"
            if club == "track":
                pcname "So I'm going to let you cum tonight."
            elif club == "cheer":
                pcname "So I think I'll let you cum tonight..."
            elif club == "yearbook":
                "You feel your confidence waver as you try to tell her what you have planned."
                pcname "So I... I'm going to let you cum."
            "Before she can react, you climb onto the bed between her legs, spreading them wide."

            "Running your tongue up and down the soft skin where her thighs meet her labia, you feel her shuddering beneath you."
            "You draw your tongue up her slit, teasing her opening."
            "Her fingers digging into your sheets, she moans."
            V "Ohh~"
            "Flicking your tongue over her clit, you smile as she shudders again."

            V "Ah~"
            "Pressing your lips to her labia, you spread them wide and press your tongue between them."
            "Tasting her juices, you draw your tongue up and down her cunt, exploring every ridge and fold before delving inside of her."
            "Violet gasps and moans, her hips bucking and twisting beneath you."

            V "Ohhh~ [domtitle]~"
            "Burying your face against her pussy, you flick your tongue up and down, teasing her insides."
            V "Ahhh~"

            "Pressing two fingers to her clit, one on either side, you begin rubbing the little nub."
            V "Ohhh shit... Ohhh~"
            "Panting, Violet writhes beneath you, her pussy pressing tighter against your face."
            "Flicking your tongue and rubbing her clit, you continue pleasuring her until her thighs tighten around your face."
            "Then, pulling away, you look up at her."

            V "{i}Please{/i}, [domtitle]. Please, I'm {i}so{/i} close..."
            pcname "I know... And you {i}really{/i} want to cum, right?"
            V "Yes. Oh, fuck... Yes!"
            pcname "Then ask me nicely."
            "Violet bites her lip, her frustration and desperation clear on her face."
            V "Please, [domtitle], may I cum?"
            pcname "Yes, you may."

            "Lowering your head, you flick your tongue over her clit."
            "Back and forth, back and forth - you move your tongue as fast as you can."
            V "Ohh~"
            "Her legs begin trembling first, then her thighs tighten around your face."
            "As her hips begin to buck, she cries out."
            V "AHH~"

            "Her body stiffens, trembling with pleasure as she cums hard."
            "Eventually, her thighs relax, letting you move your head again."
            "The trembling stops, replaced by breathy panting and sighs of satisfaction."
            scene bg RoomN with fade
            show chelsea with dissolve
            "As you pull yourself from the bed, you lick the last of her juices from her lips."
            show chelsea embarrassed
            V "Th-thank you, [domtitle]..."
            pcname "You're welcome, Violet. You deserved it."
            "She smiles up at you, flushed and content."
            show chelsea sad
            pcname "You should get dressed, though. It's getting late and you still have to drive home."
            V "Yeah, I didn't bring a change of clothes either..."
    show chelsea embarrassed
    show V SubParty Worried at midright with dissolve
    "You watch as she dresses, noting how quickly her panties darken as they soak in her juices."
    hide V SubParty
    show V Party Suprised at midright
    "How she gasps as her bra rubs against her nipples."
    scene bg HomeN with dissolve
    show V SubParty Blank at right, enterScene(0.7, 1.0, 0.35, 0.35)
    pause 0.5
    show chelsea at midright, enterScene(0.45, 0.75, 0.35, 0.35)
    "As you walk her to the door, you pull her into a hard kiss."
    "Releasing her, you whisper in her ear:"
    show chelsea embarrassed
    hide V SubParty
    show V Party Suprised at right
    pcname "You're right, though. Dessert {i}was{/i} the best part."
    hide V Party
    show V SubParty Worried at right, exitScene(1.0, 1.5, 0.35, 0.35)
    "Blushing, she shivers and turns away. You smile as the door swings shut behind her."
    $ acts -= 1
    jump events_end_period
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
