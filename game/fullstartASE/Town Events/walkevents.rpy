label walkevents:

    if acts == 4:
        scene bg CityE
    elif acts == 2 or acts == 3:
        scene bg CityD
    elif acts == 1:
        scene bg CityE
    elif acts < 1:
        scene bg CityN

    $ goingto = "town"
    $ clothes, hair = casualwear

    call eventengine from _call_eventengine_4

    jump city2

label introwalk:
    "You take a leisurely stroll through the city and become a little more familiar with it as a result."
    show chelsea happy at right with moveinright
    pcname "Knowing my way around could pay off in the end."
    jump events_end_period


label jobhunt:
    "You head outside to start your job hunt."
    show chelsea happy at right with moveinright
    pcname "Alright! I'm sure somewhere's hiring. It's a big city, after all."
    hide chelsea with dissolve
    "Your walk takes you all across town. Although you come across a few stores, they're looking for people with experience."
    "The search seems hopeless - until you find a bakery with a \"Now Hiring!\" sign out front."
    show chelsea blank at right with moveinright
    menu:
        "Let's check it out!" if True:
            scene bg black with fade
            "You decide to head in and see what they're looking for."
            show bg BakeryLisa with fade
            "The bakery smells warm and inviting; your eyes scan the room, taking in the lavender-striped wallpaper, dark wooden panels, and brick archways."
            "Eventually, you are drawn to the display case in the middle of the counter."
            "In front of the case is a young woman, with long black hair, wearing a cute little uniform."
            "She turns toward you, smiling, and adjusts her glasses."
            "Bakery Girl" "Good evening! How may I help you?"
            pcname "Um, yes, I noticed the sign out front and wanted to get an application."
            "Bakery Girl" "Oh, that's wonderful! Let me get the manager."
            "She heads into the back room."
            show bg Bakery with fade
            show chelsea blank at right with moveinright
            "You take the time to look at the different baked goods. The display case is filled with cupcakes, bread, and pastries in all shapes and colors."
            "They look amazing - and expensive."
            "A glance at the price tags proves you right."
            show chelsea confused
            pcname "I guess it must be {i}really{/i} good bread..."
            show chelsea blank
            "Eventually, the girl returns with a man following close behind her; he seems somewhat tired and {i}very{/i} agitated."
            show L Happy at left with moveinleft
            show Keith Neutral with dissolve
            "Manager" "So, Lisa says you're looking for work?"
            show Keith Blank
            show chelsea confused
            pcname "Yes, I was wondering if you had an application I could fill out or--"
            "He looks you up and down."
            show Keith Smirk
            show chelsea blank
            "Manager" "It doesn't matter; you'll do fine. Come into my office for a minute."
            show Keith Blank
            show chelsea confused
            pcname "Uh, alright...?"
            "The way he leered at you almost makes your skin crawl, but you {i}really{/i} need a job."
            hide L with dissolve
            hide Keith Blank with dissolve
            hide chelsea with dissolve
            "You follow him through a large storage area, filled with various goods."
            show bg BakeryOffice with dissolve
            "Eventually, you both enter a moderately sized office. He motions for you to sit in the chair opposite his desk."
            "He leans forward and speaks lowly - almost intimately."
            show Keith Neutral at left with moveinleft
            "Manager" "We're looking for someone to take the evening shift, from 4 to 9 PM. Can you do that?"
            show Keith Blank at left
            show chelsea happy at right with moveinright
            pcname "Yes, I can do that."
            show chelsea blank
            show Keith Neutral at left
            "Manager" "Okay, well... if you want the position, I can hire you right now."
            menu:
                "It's not quite what I'm looking for." if True:
                    show Keith Angry at left
                    "Manager" "Then why are you wasting my time!?"
                    "The manager motions to the door. Clearly, that's your cue to leave."
                    hide chelsea with dissolve
                    hide Keith Angry with dissolve
                    show bg black with fade
                    show bg CityD with fade
                "I'll take it!" if True:
                    show chelsea happy
                    $ job = "bakery"
                    show Keith Neutral at left
                    "Manager" "Good. You start tomorrow at 4 PM. Be here."
                    show Keith Blank at left
                    pcname "Yes, sir."
                    "He reaches into a box and pulls out an outfit. Then, he slides it across the table to you."
                    show Keith Neutral at left
                    "Manager" "All employees wear a uniform. Don't forget."
                    show Keith Blank at left
                    pcname "Don't worry; I won't."
                    "After going over a few basic rules, you're free to leave."
                    scene onlayer master
                    $ acts -= 1
                    $ persistent.introseen = True
                    jump city2
        "Hmm... It's not for me." if True:
            hide chelsea with dissolve
            "You give the sign one final glance before heading off in search of a different job."
    "Unfortunately, nothing really stands out. Despite your hopes, it seems to be slim pickings."
    "Right before you give up for the night, you see a little cafe sandwiched between two large buildings."
    "\"Emilia's Maid Cafe\" has the one thing you were looking for: a help wanted ad in the window."
    show bg black with fade
    show bg CafeKate with fade
    "You walk inside, taking in the bright, cheerful decor and the relaxed atmosphere."
    "A set of chalkboard menus - covered in a loopy, feminine script - line the overhang above the bar in the center of the room."
    "A short girl near the bar, wearing an almost equally short maid skirt and black stockings with garters, turns to greet you."
    "You're immediately drawn to her green eyes and adorable smile."
    pause 0.2
    "Maid" "Evening, Mistress! May I show you to a table?"
    "It's strange being called \"Mistress\", but you guess that's part of the gimmick."
    pcname "Um, I was actually hoping to apply for a job..."
    "Maid" "Really!? Please, follow me!"
    "She grabs your hand and leads you into the back of the store, stopping to knock on an open door."
    show bg black with fade
    show bg Cafe with fade
    show K Blank at left with moveinleft
    show chelsea blank at right with moveinright
    "Maid" "E-Excuse me, Ma'am?"
    show EM Neutral with dissolve
    "Woman" "Yes, Kate?"
    show EM Blank
    "Inside, a woman sits with her back to you in front of a computer."
    "Kate" "We have a potential employee here."
    "The woman turns around in her chair, looking suspicious."
    show EM Happy
    "Woman" "Ah, good, it's not another guy! Wait... You {i}are{/i} a girl, right?"
    show EM Serious
    hide K Blank with dissolve
    show chelsea shocked
    pcname "Um, yes?"
    "Woman" "Have you checked recently?"
    show chelsea embarrassed
    pcname "Uh... yes?"
    "Woman" "Is that all you can say?"
    pcname "N-No?"
    show EM Happy
    "Woman" "I'm just messing with ya. Come on over and have a seat."
    show chelsea blank
    show EM Blank
    "You step farther into her office and do as she asked."
    show chelsea happy
    show EM Neutral at left with move
    "Woman" "My name is Emilia. And you're looking to be hired on as a waitress?"
    show EM Blank at left
    pcname "Yes, I am. I'm in school, so I was hoping to work from 4pm until 9pm?"
    show EM Neutral at left
    "Emilia" "We can do that. But, I'll level with you: it's not for everyone..."
    show chelsea blank
    "Emilia" "You'll wait tables, but it's very important that you take on a specific role while you're here."
    show EM Happy at left
    "Emilia" "You embody the maid persona. You call men \"Master\" and women \"Mistress\"."
    "Emilia" "And, above all, you try to be as cute and inviting as you can be."
    show EM Neutral at left
    "Emilia" "Does it sound like something you'd want to do?"
    show chelsea happy
    show EM Blank at left
    pcname "Yes, it does!"
    show EM Happy at left
    "Emilia" "Great! You'll start tomorrow. Kate will be your trainer."
    "She stands up and shakes your hand; then, you're free to leave."
    $ job = "cafe"
    $ acts -= 1
    $ persistent.introseen = True
    jump events_end_period

label townbadarea:
    "You decide to explore a new part of town."
    "The farther you walk, the more dirty and cracked the sidewalks become."
    menu townbadarea_turnaround1:
        "Turn around." if True:
            "This looks like a bad part of town, so you turn around and head home."
            jump events_end_period
        "Keep going." if True:
            "It doesn’t look {i}too{/i} bad - and you’re not easily frightened, so you keep walking."
            "The street gets more dilapidated as you go on. Soon, even the houses are in disrepair."
            pcname "Maybe it’s time to turn around..."
            menu townbadarea_turnaround2:
                "Turn around." if True:
                    "You’ve seen enough. This isn’t a part of the city you’d like to come back to."
                    "You turn on your heels and hurry home."
                    jump events_end_period
                "Keep going." if True:
                    "It’s {i}definitely{/i} a bad part of town - but it’s a little thrilling to explore somewhere that seems so dangerous."
                    $ corruption += 2
                    "Eventually, the streets start improving again."
                    "You made it out unscathed, but you have a feeling that you might not be so lucky next time."
                    jump events_end_period


label townlottery:
    $ varlottocard = renpy.random.randint(1,100)
    if lottostand == 3:
        "As you’re walking around the city, you see a man in a stylish suit standing behind a neatly designed stall with the word \"Lottery\" on the front."
        "You decide to take a look."
        "Rich Man" "Hello there. Here to buy one of my lottery tickets?"
        show chelsea blank at right with moveinright
        pcname @ confused "How do I know you're not shady?"
        "Rich Man" "Well, it's my own money. $1000 is just pocket change to me, and I’m actually making money off the tickets too."
    elif lottostand == 2:
        "Walking around, you find the lottery stand again."
        "Rich Man" "It's good to see you."
        show chelsea blank at right with moveinright
    "Rich Man" "Wanna try getting rich?"
    menu:
        "Draw a number?"
        "Draw a number: $10" if Cash >= 10:
            $ Cash -= 10
            "You spend $10 and draw a card."
            "It's a [varlottocard]!"
            "You hand the card back to the salesman."
            if varlottocard == 69:
                $ unlock_ach(lottery)
                "His eyes widen and his jaw drops."
                "Rich Man" "Holy shit! You actually won it!"
                show chelsea shocked
                "Your own eyes widen in disbelief."
                "Rich Man" "Well, I guess this is yours."
                "He reaches under the stall and hands you a stack of ten 100 dollar bills."
                "Rich Man" "Don't spend it all in one place now."
                "You both leave the stall; he has a briefcase in one hand, and you have the stack of $100s in yours."
                "You stare down at the wad of cash in disbelief."
                pcname "Ah-- I should get going."
                hide chelsea with dissolve
                $ Cash += 1000
                $ lottostand = 0
            elif True:
                "Rich Man" "Too bad. You have to pull a 69 to win!"
                "In the end, you walk away - your wallet a little lighter than before."
                $ lottostand = 2
        "No thanks." if True:
            pcname "No thanks, I was just looking."
            "Rich Man" "Fair enough."
            "You leave the area and head back home."
            $ lottostand = 2
    hide chelsea with dissolve
    jump events_end_period

label townToxin:
    "You decide that it’s time to head a little farther downtown on your walk today."
    "Along the way, you see an ad for \"Toxin\" headphones."
    "The design looks quite elegant, and you begin to wonder what the price is."
    "Looks like the advertisement was effective."
    jump events_end_period

label towncoffee:
    "On your way deeper into the city, you stop by \"Twinkling Bliss\" - a coffee shop you’ve seen a few times."
    show chelsea blank at right with moveinright
    show bg DatePlace with dissolve
    menu towncoffeemenu:
        "What would you like?"
        "Latte: $2" if Cash >= 2:
            $ Cash -= 2
        "Mocha: $3" if Cash >= 3:
            $ Cash -= 3
        "Macchiato: $4" if Cash >= 4:
            $ Cash -= 4
        "Just water." if True:
            pass
    "You take a seat with your beverage and look around."
    "You overhear a few conversations- a man trying to do a live stream on his laptop, a couple arguing over what color to paint their bedroom..."
    show chelsea confused
    "As you glance around, you see a businessman staring at you from one of the chairs by the window."
    show chelsea blank
    menu towncoffeestare:
        "Smile at him." if True:
            show chelsea happy
            $ corruption +=1
            "Not sure how to respond, you give him a friendly smile."
            "He catches it and grins back."
            "You return to your beverage. You both make eye contact a few more times before he leaves."
        "Look away." if True:
            "You uncomfortably look away, avoiding glancing back in his direction."
            "After a few more sips of your beverage, you look up to see that he's gone."
    jump events_end_period

label towncoffee2:
    "As you wander through the city, you find yourself a little thirsty and stop at \"Twinkling Bliss\"."
    show chelsea blank at right with moveinright
    show bg DatePlace with dissolve
    menu towncoffeemenu2:
        "What would you like?"
        "Latte: $2" if Cash >= 2:
            $ Cash -= 2
        "Mocha: $3" if Cash >= 3:
            $ Cash -= 3
        "Macchiato: $4" if Cash >= 4:
            $ Cash -= 4
        "Just water." if True:
            pass
    "You return to the same seat as last time and look around."
    "The live streamer sits by the windows with his laptop. The couple argues about purchasing a new bed frame."
    "You do not see the man."
    "As you sip your beverage, a coffee plops down at your table."
    "You look up. The businessman grins down at you."
    "Business Man" "You beat me to the punch. Would you like this anyway?"
    "He offers you the coffee on the table."
    menu towncoffeeoffer:
        "Sure." if True:
            show chelsea happy
            "You set your beverage aside and gratefully take the cup."
            "You take a sip and smile up at him in thanks. He grins back."
            pcname "Thank you."
            "Business Man" "Sure thing."
            $ corruption +=1
            "He leaves a business card on the table before he leaves. A note is written by his number: 'Call me anytime.'"
            $ coffeebusinesscard = True
            $ coffeescenes += 1
        "No thanks." if True:
            show chelsea confused
            "You look at the coffee skeptically, pulling your beverage closer to your chest."
            show chelsea blank
            "The businessman frowns, but picks up the cup and walks away."
    jump events_end_period

label towncoffee3:
    "You don't even need to think twice before you enter \"Twinkling Bliss\"."
    show chelsea blank at right with moveinright
    show bg DatePlace with dissolve
    "You've visited so often that the barista has your drink ready after you enter the front doors."
    "You take your beverage and as you make your way to your usual spot, you see the businessman already sitting there."
    menu towncoffeesit:
        "Sit there anyway." if True:
            "You take a seat at the table, setting your beverage down. He grins up at you."
            if coffeebusinesscard == True:
                "Business Man" "You haven't called."
                if club == "track":
                    "You take a sip of your beverage and shrug."
                    pcname "I didn't get a chance to."
                elif club == "cheer":
                    show chelsea happy
                    "You stroke the sides of your cup, giving him a playful smile."
                    pcname "I've been busy."
                elif club == "yearbook":
                    show chelsea embarrassed
                    "You twist the cup in your hands, biting your lip."
                    pcname "I forgot to..."
                "Business Man" "That's too bad..."
            elif True:
                "Business Man" "I noticed you come here alone pretty often. Are you single?"
                if damienrelate == "dating":
                    menu coffeedamien:
                        "I have a boyfriend." if True:
                            "The man nods, understanding."
                            "Business Man" "That's not surprising. A pretty girl like you..."
                        "I'm single." if True:
                            show chelsea happy
                            "You think of Damien, but push him out of your mind. You're not ready to confess that to a stranger."
                            "The man grins, pleased with your lie."
                            "Business Man" "Really? I'm shocked. A pretty girl like you..."
                if mattchain == 2:
                    menu coffeematt:
                        "I'm seeing someone." if True:
                            show chelsea happy
                            if defymatt == True:
                                "You hate to say it, but you don't want to know what Matt's reaction would be if you'd denied him entirely."
                                "Still, it's not like you're really seeing him in that way..."
                            elif True:
                                "It's not technically true, but it's not technically a lie either. You know Matt wouldn't call you his girlfriend, but you have done some pretty intimate things..."
                            "The man doesn't seem deterred by your answer, smiling still."
                            "Business Man" "That's not surprising. A pretty girl like you..."
                        "I'm single." if True:
                            if defymatt == True:
                                "You think of Matt and all the horrible things he would say to you if he knew you were talking to another man."
                                "A sense of joy runs through you at your defiance. Yes, you're single. It's not as if Matt has forced you to be otherwise."
                            elif True:
                                "You aren't really sure how to answer his question, but this seems to be the closest to it."
                                "It isn't like you're exclusive to Matt, especially not after what happened with him and Alex..."
                            "The man grins, pleased to hear it."
                            "Business Man" "Really? I'm shocked. A pretty girl like you..."
                if violetrelate == "Sub":
                    menu coffeeviolet:
                        "I'm seeing someone." if True:
                            show chelsea happy
                            "You think of Violet and your agreement to have more control over her. Although you haven't agreed on any labels, the idea of seeing her as more than friends is appealing..."
                            "And if she doesn't like it, you'll just punish her later."
                            "The man doesn't seem deterred by your answer, smiling still."
                            "Business Man" "That's not surprising. A pretty girl like you..."
                        "I'm single." if True:
                            "You briefly think of Violet and your current relationship with her. She'll submit to anything you say..."
                            "And, well, you haven't defined what you are. She'll submit to this, too, unless she wants to be punished."
                            "The man grins, pleased to hear it."
                            "Business Man" "Really? I'm shocked. A pretty girl like you..."
                if violetrelate == "Dom":
                    menu coffeeviolet2:
                        "I'm seeing someone." if True:
                            show chelsea happy
                            "You think of Violet and hope that your answer is the right choice. You haven't gotten permission to see others, and you'd hate to disobey..."
                            "The man doesn't seem deterred by your answer, smiling still."
                            "Business Man" "That's not surprising. A pretty girl like you..."
                        "I'm single." if True:
                            "You think of Violet and, although she has control over you, she never specified that you couldn't see anyone else."
                            "You feel an enjoyable twist in your abdomen at the thought of her finding out, and what punishments she'll give you."
                            "The man grins, pleased to hear it."
                            "Business Man" "Really? I'm shocked. A pretty girl like you..."
                elif True:
                    menu coffeerelate:
                        "I'm seeing someone." if True:
                            show chelsea happy
                            "Although it isn't true, you don't want to give him the idea that you're this lonely."
                            "The man doesn't seem deterred by your answer, smiling still."
                            "Business Man" "That's not surprising. A pretty girl like you..."
                        "I'm single." if True:
                            "You tell him the truth. You don't see the point in lying when it's this obvious."
                            "The man grins, pleased to hear it."
                            "Business Man" "Really? I'm shocked. A pretty girl like you..."
            show chelsea shocked
            "His hand brushes your knee underneath the table."
            "Business Man" "I was hoping we could get to know each other better."
            if corruption >= 15:
                if club == "track":
                    show chelsea happy
                    "You feel confident under his touch, and even nudge your knee forward so his fingers can stretch to your thigh."
                    pcname "Alright."
                elif club == "cheer":
                    show chelsea happy
                    "A sly smile reaches your lips at his suggestion. It's wrong, but it's the wrongness of it all that sends a thrill through your body."
                    "You lean forward."
                    pcname "I was thinking the same thing."
                elif club == "yearbook":
                    show chelsea embarrassed
                    "You feel a sense of embarrassment and shame at his proposal..."
                    "But there's something exciting about it, too, that you can't ignore."
                    pcname "I-I might like that..."
                "His grin is sharp; shark-like. He reaches for your discarded phone on the table and copies your number into his phone."
                "In another moment, you receive a text."
                show chelsea blank
                "Before you open it, he grabs your hand."
                "Business Man" "Something for you to think about later. I expect the same in return."
                "With that, he takes his coffee and leaves, but not without eyeing you up on his way out."
                "You open up your phone and peer at the text he sent."
                call screen TextingScene("MR. D",
                [
                    TextMessage("Pick up where I leave off."),
                    TextMessage("I reach under the table at the coffee shop."),
                    TextMessage("My fingers rub against your knee, and then slide up between your thighs."),
                    TextMessage("I press them against your panties and stroke.")
                ])
                show chelsea happy
                "Despite yourself, a smile curls up your lips. You can't help but feel a little flattered."
                "You have no intention of taking it further than this, but for now, you'll enjoy yourself."
                $ chelseaContacts.contactsListed["MR. D"] = "MR. D"
                jump events_end_period
            elif True:
                show chelsea angry
                "You jerk your knee away, creating space between you both at the table."
                "His suggestion leaves you feeling disturbed and uncomfortable. This is too far."
                pcname "Please go."
                show chelsea blank
                "His calm and collected smile pulls back into a sneer."
                "Business Man" "Teasing bitch."
                $ corruption +=1
                "He yanks his coffee from the table, spilling a little on you in the process, and storms out."
                "You clutch your beverage to your chest with shaky hands. Perhaps you'll find a new coffee shop to visit."
                jump events_end_period
        "Leave." if True:
            "You clutch your drink closer to your chest, unnerved. Why does this guy keep bothering you?"
            "Before he notices your presence, you hurry out of the coffee shop."
            "It may be a while before you go back."
            jump events_end_period

label townkitten:
    transform catleft:
        xalign 0.12 ypos 530
    show chelsea blank at right with moveinright
    "You wander around the city, searching for something to do."
    "As you pass a shady alleyway, you hear a soft noise."
    "???" "Mew!"
    show chelsea confused
    "You pause, wondering if you'd actually heard it."
    "You listen closer. You barely catch it again."
    "???" "Mew!"
    show chelsea blank
    menu kitteninvestigate:
        "Investigate." if True:
            "You hesitate, trying to decipher where exactly the noise is coming from."
            show chelsea confused
            "???" "Meeew!"
            "Peering down the alley, you see an overturned tin trashcan. The noise echoes from inside."
            "You lift the trashcan up."
            show chelsea happy
            show Cat Sad at catleft with dissolve
            "Kitten" "Mew!"
            "A small, grey and white kitten yowls from underneath. It's barely larger than your hand."
            "Although you expected it to jump out as soon as it was freed, the kitten wobbles weakly toward you. Upon closer inspection, you notice how thin it is."
            show chelsea sad
            pcname "Poor thing..."
            show Cat Happy at catleft
            "You lift the small kitten into your arms. It fidgets a little, but seems to enjoy your company."
            show chelsea happy
            pcname "Don't worry. I'll take care of you."
            hide chelsea with dissolve
            hide Cat Happy at catleft
            show bg black with fade
            pause 0.5
            if acts == 4:
                scene bg CityE with fade
            if acts == 3:
                scene bg CityD with fade
            if acts == 2:
                scene bg CityD with fade
            if acts == 1:
                scene bg CityN with fade
            if acts < 1:
                scene bg CityN with fade
            show chelsea blank at right with moveinright
            show Cat Happy at catleft
            "You return from the store a short time later with fresh cat food, water, and a couple of bowls."
            "The kitten laps eagerly at the bowl of water in the alley, its back rising to your touch as you caress its soft fur."
            show chelsea sad
            pcname "I wish I could take you home..."
            "...But you really can't afford a pet right now."
            show chelsea blank
            pcname "I hope this is enough."
            "The kitten turns its attention to the food and eats eagerly."
            "You spend a little bit more time petting the kitten before it has enough energy to wander off."
            "Wherever it goes, you hope it stays safe."
            $ kittenscenes += 1
            jump events_end_period
        "Leave it alone." if True:
            "Deciding it to be a part of your imagination, you shrug it off."
            "With nothing else around, you continue on your way."
            jump events_end_period

label townkitten2:
    show chelsea blank at right with moveinright
    "As you wander around town, you struggle to find anything exciting to do."
    show chelsea angry
    pcname "Ah... This is so boring..."
    show chelsea blank
    "You pass by an alleyway and hear a strangled animal cry, followed by children's laughter."
    menu kitteninvestigate2:
        "Investigate." if True:
            show chelsea shocked
            "You peer down the alley, horrified at what you find."
            "A small group of elementary school boys surround a small animal, trapping it between garbage cans."
            "They each hold up various weapons of rocks and sticks, throwing and prodding the poor animal with them."
            show Cat Sad at catleft with dissolve
            "As you near the group, you see that their victim is none other than the grey-white kitten you had rescued."
            "One of the boys nears the kitten with his stick. It hisses up at him. He holds his stick back to strike it-"
            show chelsea angry
            if club == "track":
                pcname "HEY!"
            elif club == "cheer":
                pcname "Excuse me!"
            elif club == "yearbook":
                pcname "S-Stop!"
            "The boys stop at once. It's clear they did not think they would be caught."
            if club == "track":
                "You stomp up to them, furious."
                pcname "Leave that poor cat alone!"
            elif club == "cheer":
                "You walk up to them, your hand pressed firmly on your hip. Your nails dig into your skin, trying not to smack the smirk off of one of their faces."
                pcname "What the hell is your problem?"
            elif club == "yearbook":
                "Gathering your courage, you make your way toward them, making your anger as visible as possible."
                pcname "How would you like it if someone did that to you?"
            "As you near them, the boys drop their weapons and flee."
            if club == "track":
                pcname "Tch. Brats..."
            elif club == "cheer":
                pcname "Ugh. Little assholes."
            elif club == "yearbook":
                pcname "What horrible boys..."
            show chelsea blank
            "You kneel down to the kitten's height, examining it for injury. The kitten presses itself away from you, wary."
            "It doesn't look terribly hurt. In fact, it looks much healthier than when you had last seen it."
            "It appears you saved the kitten before the boys could do any real damage."
            "You reach out a hand for it to sniff."
            show chelsea happy
            show Cat Blank at catleft
            pcname "It's okay, buddy. Remember me?"
            "It takes a moment to gain its trust, but the kitten sniffs your hand for a moment. Then, he licks it."
            show chelsea blank
            show Cat Happy at catleft
            "You let out a small sigh of relief and gently scratch it behind its ears."
            pcname "I'm gonna need a name to call you if we keep running into each other..."
            "The kitten purrs as you run your hand across its back."
            pcname "How about..."
            $ kittenname = renpy.input("What will you call the kitten?", default="Lucky", length=12)
            $ renpy.pause
            $ kittenname = kittenname.strip()
            if kittenname == "":
                $ kittenname = "Lucky"
            pcname "[kittenname]."
            "Although you're sure the kitten doesn't care what you call it, you still feel a sense of satisfaction when it purrs in response."
            $ kittenscenes += 1
            jump events_end_period
        "Leave it alone." if True:
            "You hesitate, then turn away. It's really none of your business."
            "You continue on your way through town."
            jump events_end_period

label townkitten3:
    show chelsea happy at right with moveinright
    show Cat Happy at catleft
    "As you pass the alleyway, you're immediately greeted by your new friend, [kittenname]."
    "He can hardly be called a kitten now with how much he's grown. He's almost the size of a full cat now."
    "[kittenname] purrs lovingly as he greets you by wrapping himself around your legs, butting his head against your ankles with affection."
    show chelsea laugh
    pcname "Hello, [kittenname]."
    "You reach down to scratch behind his ears. He purrs in delight."
    show chelsea happy
    "You knew naming it would be a mistake. Now you feel attached."
    "You can't take it home. But you really want to."
    menu kittenfindhome:
        "Find a home for the kitten." if True:
            show chelsea blank
            "You suppose you have to settle for the next best thing."
            "You scoop [kittenname] into your arms and stand up. He doesn't mind, deciding to snuggle against your chest."
            "You've never known a cat to be this affectionate. It makes giving him up even harder."
            pcname "Let's find you a home."
            hide Cat Happy with dissolve
            hide chelsea with dissolve
            show bg black with fade
            pause 0.5
            show bg CityN with dissolve
            show chelsea laugh at right with dissolve
            pcname "Alright!"
            show chelsea happy
            show Cat Blank at catleft
            "You clap your hands together, relieved that your hard work is done."
            "There isn't an inch of the city that isn't covered in posters advertising [kittenname]."
            "You even made sure to include his name, so they would know what to call him."
            "Although that tidbit was more for yourself than [kittenname]."
            "You glance down at the cage you'd purchased for [kittenname]. He lays inside lazily, as he has since you started taping posters up."
            show chelsea blank
            pcname "I guess we just need to wait."
            "In the meantime, you guess it won't hurt to keep him at your place for a little bit."
            $ findkittenhome = True
            $ kittenscenes += 1
            jump events_end_period
        "Let the kitten live its life." if True:
            "While you can't take care of him yourself, you dread the idea of interfering with his lifestyle."
            "After all, he looks healthy enough."
            pcname "Come visit me whenever you're around."
            "[kittenname] doesn't acknowledge what you said, but you hope he takes it to heart."
            jump events_end_period

label townkitten4:
    show chelsea blank at right with moveinright
    "It takes no time at all for people to begin contacting you about the kitten."
    "You agree to meet one of them- Laurie, a recent college graduate- at her favorite coffee shop."
    show Cat Blank at catleft with dissolve
    "You bring [kittenname] with you just in case. He doesn't seem to want to be bothered out of his cage."
    "You wouldn't be surprised if he became a very fat, lazy, content cat wherever he ends up."
    "Laurie" "Hey! [pcname]!"
    "You find Laurie at a set of chairs by the fake fireplace, her hair pulled up in a loose bun. She waves you over."
    show chelsea happy
    pcname "Hey."
    "You shake hands and take your seats."
    show chelsea blank
    "You interview her for the better part of an hour. You want to be absolutely sure [kittenname] will be going into good hands."
    "It takes several questions, but you think she will be a good fit."
    show chelsea sad
    "Still, you feel a twinge of guilt in your chest. Is this really the right decision?"
    menu kittengiveaway:
        "Give Laurie the kitten." if True:
            show chelsea blank
            pcname "Okay, then. He's all yours."
            show chelsea sad
            "You struggle to bring yourself to it, but you gently slide the cage over to Laurie. You pull out an assortment of toys, food, and other items you collected this week for [kittenname] and pass it to her."
            pcname "I already took him to the vet, so you don't need to worry about it."
            "Laurie" "Sweet! Awesome! Thanks again, [pcname]."
            "[kittenname] perks up from the cage, noticing your lack of presence."
            show Cat Sad at catleft
            "He reaches a paw out and mewls at you."
            pcname "I'm sorry, buddy. You'll do better here."
            "Laurie" "It's okay. He'll get used to me. Thanks again!"
            "Laurie stands up, cooing [kittenname] inside his cage as they leave the coffee shop."
            show chelsea blank
            hide Cat Sad with dissolve
            "While you'll miss your furry friend, you're glad that he's gone on to someone who can properly take care of him."
            show chelsea happy
            "As you head home, you feel a little bit better about his future with his new owner."
            scene bg black with dissolve
            pause 0.5
            "You've reached the end of the Kitten Side Story in this version! Keep and eye out for more content!"
            jump events_end_period
        "Keep Him." if True:
            show Cat Sad at catleft with dissolve
            "You look down at [kittenname], taken in by his wide, sad eyes."
            "It's as if he knows you're giving him away."
            "Your heart squeezes in your chest. No, this isn't right."
            "It takes you a moment, but you pull the cage back to yourself."
            show Cat Blank at catleft
            pcname "I'm sorry. You seem like a nice girl, but I don't think it'll work out."
            "Laurie's face drops in disappointment."
            "Laurie" "Oh. Well, I get it. Thanks for your time."
            "It doesn't seem like she actually gets it at all, but Laurie grabs her purse and leaves."
            show chelsea blank
            "You're not sure how you'll make it work, but you know that [kittenname] belongs with you!"
            $ catadopt = True
            "Smiling down at him, you stare into his eyes."
            pcname "Let's go home, [kittenname]."
            $ catrent = True
            scene bg black with dissolve
            pause 0.5
            jump events_end_period

label townkaraoke:
    show chelsea blank at right with moveinright
    "You come across a busy section downtown. On either side of you are several bars and clubs."
    "You pass by several buildings until you see a sign for \"STAR LIGHT\" on the corner. A bright neon sign flashes 'KARAOKE!' in the window."
    "Would you like to go in?"
    menu karaokeenter1:
        "Go in." if True:
            show chelsea happy
            "This sounds like fun! You climb up the front steps and enter."
            "A tall man with several tattoos and bright purple hair greets you behind the counter."
            menu karaokemenu2:
                "Sing. $15" if Cash >= 15:
                    $ karaokeleave = False
                    $ Cash -= 15
                "Leave." if True:
                    show chelsea blank
                    "Maybe you're not really in the mood to sing today."
                    "Karaoke Man" "Ah, well. Maybe next time."
                    "You head back out into the city."
                    jump events_end_period
            "Karaoke Man" "Great! Take Room 7."
            "You make your way into a private room down the hall. As you pass, you hear some great singers from next door."
            show bg Karaoke1 with dissolve
            "Your own room is very comfortable, with two plush couches and a small table for ordering snacks."
            "At the other end of the room is the karaoke machine."
            show chelsea blank
            "You scroll through a few songs and pick up your microphone."
            show chelsea laugh
            "You enjoy the next few hours singing your heart out in your private room. This is pretty great!"
            "When you're finished, you leave feeling pretty satisfied. You make a note to yourself to come again soon."
            $ karaokescenes += 1
            jump events_end_period
        "Leave." if True:
            "You're not really in the mood for singing today."
            "You continue on your way."
            jump events_end_period

label townkaraoke2:
    show chelsea blank at right with moveinright
    "As you walk by the busier club district of downtown, you see \"STAR LIGHT\" on the corner. A bright neon sign flashes 'KARAOKE!' in the window."
    "Would you like to go in?"
    menu karaokeenter2:
        "Go in." if True:
            show chelsea happy
            "You had so much fun last time, maybe you'll sing again!"
            "A tall man with several tattoos and bright purple hair greets you behind the counter."
            menu karaokemenu3:
                "Sing. $15" if Cash >= 15:
                    $ Cash -= 15
                "Leave." if True:
                    show chelsea blank
                    "Maybe you're not really in the mood to sing today."
                    "Karaoke Man" "Ah, well. Maybe next time."
                    "You head back out into the city."
                    jump events_end_period
            "Karaoke Man" "Great! Take Room 7."
            "As you head to your room, you notice a man leaning outside of the bathrooms, lighting up a smoke beside a No Smoking Sign."
            "You wrinkle your nose in disgust, meeting his gaze briefly before paying him no further attention."
            "You go back to room 7, but as you pass your neighbors, you hear their wonderful singing again. Are they regulars?"
            show bg Karaoke1 with dissolve
            "After settling down, you pick your songs and take your microphone. Time to sing!"
            "After your third song, you hear a knock on the wall."
            show chelsea confused
            menu karaokeknock:
                "Knock back." if True:
                    show chelsea angry
                    "You paid for this room- you have as much right as your neighbors to sing to your heart's content!"
                    "You continue onto your fourth song, but once it ends, you hear another knock."
                    "The nerve!"
                    "You knock back."
                    show chelsea happy
                    "You continue for two more songs. They knock after each time."
                    "By the end of your last song, there's a loud barrage of knocking against your wall."
                    show chelsea angry
                    menu karaokeconfront:
                        "Confront your neighbors." if True:
                            "That's it. This has gone on for long enough."
                            show bg black with dissolve
                            "Irritated, you step out of your room and bang against their door."
                            "You're surprised by the man who greets you."
                            "He's tall and burly, with an eyepatch over one eye and scars down his arms."
                            show bg Karaoke2 with dissolve
                            "Glancing behind him, you find several other men with similar physical appearances. Despite this, they are all well-dressed."
                            show chelsea blank
                            "You have an aching feeling that you've bitten off more than you can chew."
                            "The man at the door grows tired of waiting for you to speak."
                            "Eyepatch Man" "Can we help you?"
                            if club == "track":
                                pcname "Do you mind? I'm trying to sing. I can't pay attention with all that knocking."
                            elif club == "cheer":
                                pcname "You keep knocking between my songs. I'm just trying to relax."
                            elif club == "yearbook":
                                show chelsea embarrassed
                                pcname "C-Could you please stop knocking on my wall? It's hard to sing with all the noise..."
                            "The men all share awkward glances with each other. The man with the eyepatch that's greeted you nods in understanding."
                            "Eyepatch Man" "Ah, I'm sorry about that. We meant it to be a compliment."
                            show chelsea confused
                            "You tilt your head, confused."
                            pcname "A compliment?"
                            "Another man with slicked-back hair speaks up behind him."
                            "Slick Man" "Your singing was beautiful. We meant it to be applause."
                            show chelsea shocked
                            "You're taken aback. Applause? It hadn't come across that way at all. Still, you feel a sense of flattery at their words."
                            show chelsea embarrassed
                            pcname "Oh. Well, thank you."
                            show chelsea happy
                            pcname "I love all of your singing as well. It's great to hear when I come in."
                            "The men beam at you."
                            "Eyepatch Man" "Thank you, miss. We appreciate the compliment."
                            "He thrusts out a hand toward you. You shake it. You can't help but smile at his politeness."
                            "Eyepatch Man" "I'm Jun."
                            "He gestures to a couple of the other men in the room, starting with the man with slicked-back hair."
                            "Jun" "These are Diego, Chris, Marty, and Terry."
                            pcname "It's nice to meet you. I'm [pcname]."
                            "Diego" "Hope we didn't scare you off. We look forward to hearing you sing again."
                            show chelsea laugh
                            pcname "Don't worry, I'll be back."
                            "You all bid your farewells as you head back out into the city. You look forward to your next visit!"
                            $ meetmafia = True
                            jump events_end_period
                        "Leave." if True:
                            "As annoyed as you are by their knocking, you don't feel like getting into a verbal argument."
                            show chelsea blank
                            "You gather your things and leave."
                            "Maybe next time you'll sing louder, just to piss them off."
                            jump events_end_period
                "Quiet down." if True:
                    show chelsea embarrassed
                    "You hadn't realized you were being so loud."
                    "Embarrassed, you lower your voice for the rest of your songs."
                    "Once you're finished, you gather your things and carry on your way."
                    "You hope you didn't disturb your neighbors too much!"
                    jump events_end_period
        "Leave." if True:
            "You're not really in the mood for singing today."
            "You continue on your way."
            hide chelsea with moveoutright
            jump events_end_period

label townkaraoke3:
    show chelsea blank at right with moveinright
    "As you walk by the busier club district of downtown, you see \"STAR LIGHT\" on the corner. A bright neon sign flashes 'KARAOKE!' in the window."
    "Would you like to go in?"
    menu karaokeenter3:
        "Go in." if True:
            "A tall man with several tattoos and bright purple hair greets you behind the counter."
            menu karaokemenu4:
                "Sing. $15" if Cash >= 15:
                    $ Cash -= 15
                "Leave." if True:
                    "Maybe you're not really in the mood to sing today."
                    "Karaoke Man" "Ah, well. Maybe next time."
                    "You head back out into the city."
                    jump events_end_period
            "Karaoke Man" "Great! Take Room 7."
            if meetmafia == True:
                "As you head to your room, you catch a glimpse of the smoker back outside the set of bathrooms."
                "You walk a little faster, trying to avoid his gaze."
                "You hear Jun and his friends singing again in their usual booth."
                menu karaokejoinsinging:
                    "Knock on door." if True:
                        show chelsea happy
                        "The singing cuts off and Jun answers the door with a scowl on his face."
                        "His expression immediately softens at the sight of you."
                        show bg Karaoke2 with dissolve
                        "Jun" "Ah, [pcname]! Guys, [pcname] is back!"
                        "The familiar faces of Diego, Chris, Marty, and Terry light up at the mention of this. They each hold up their mugs of beer in a cheer of hello's."
                        "Jun" "Come in, come in! We're about to start another round."
                        "Jun ushers you in as Marty takes the stage."
                        "You squeeze in between Chris and Terry, who offers you his mug of beer. Based on the redness of the men's faces and the glazed look in their eyes, they're pretty far gone."
                        menu karaokeacceptbeer:
                            "Accept beer." if True:
                                show chelsea laugh
                                "You accept the beer, grateful but also a little concerned that they hadn't asked for your age."
                                "You take a gulp from the liquid and stretch, ready for the next song to come on."
                                $ corruption +=1
                            "Decline beer." if True:
                                "You gently hold your hand out and shake your head. Terry shrugs and takes a large swig from the mug."
                                "He doesn't seem to mind your rejection at least."
                        show chelsea happy
                        "A 1980's pop hit blasts over the speakers. It was the last thing you expected to hear, but the men whoop and holler in encouragement as Marty belts out the lyrics."
                        "You cheer along with them."
                        "This continues on for a few more songs, each of the men taking turns to sing their favorite pop hits."
                        "Jun" "Do you know this one, [pcname]?"
                        "A familiar tune starts up over the speakers."
                        menu karaokejoinsinging1:
                            "Sing with him." if True:
                                pcname "Yeah, I know it."
                                "Jun beams and waves you forward."
                                "Jun" "Then get on up here!"
                                show chelsea laugh
                                "You hurry up on stage beside him, taking the extra microphone. As the song blasts, you and Jun sing your hearts out, only slightly off-key."
                            "Tell him no." if True:
                                show chelsea blank
                                "Although they had complimented your singing last time, you feel a wave of embarrassment at singing in front of an audience."
                                pcname "Sorry, I don't know it."
                                "Jun is a little disappointed, but waves Chris up on stage. The man gladly joins, and they duet over the pop song."
                                show chelsea happy
                                "You join in with the other men in cheering them on."
                        show chelsea shocked
                        "When the song ends, you hear a loud banging against the door."
                        "???" "Open up, Jun! I know your boys are in there!"
                        "The atmosphere changes around you as Jun and his men share a serious look."
                        "Jun" "I hate being bothered during my free time..."
                        "Diego" "I'll handle it, boss."
                        "Boss?"
                        show chelsea blank
                        "Diego and Marty stand up from their seats and make their way toward the door. You try to peer around as they step outside, but Terry purposefully blocks your view."
                        "He gives you an apologetic smile. Jun and Chris seem unbothered."
                        show chelsea confused
                        pcname "So, do you all work together?"
                        "Terry chuckles."
                        "Terry" "Something like that."
                        show chelsea blank
                        "Jun starts up another song on the stage, his voice carrying out throughout the room."
                        "Diego and Marty return shortly after, their jackets stained in red."
                        show chelsea confused
                        "You glance at them quizzically, but otherwise return your attention to the stage."
                        show chelsea blank
                        "The songs carry on for a few more hours before everyone lays spent across their chairs, wasted and happy."
                        "Jun" "Guess it's time to go."
                        "Jun gets up first. The others follow suit, gathering their things from around the room. You catch the glimpse of a gun resting on one of the chairs."
                        "You all file out of the karaoke bar and into the street. You offer to pay for your food and drinks, but Jun insists otherwise."
                        "Once everyone is outside and the others are returning to their car, Jun pulls you aside."
                        "He places a hand on your shoulder."
                        "Jun" "You've been a lot of fun, [pcname]. Don't be afraid to call on us if you need a favor, alright?"
                        show chelsea happy
                        pcname "Thank you! I appreciate it."
                        "Jun grins and leaves you with his business card before returning to his car."
                        "After they've left, you glance down at the card."
                        show chelsea blank
                        "Jun Miyozaki. Owner of the Diamond Casinos."
                        show chelsea confused
                        "Wait... That name sounds familiar..."
                        show chelsea shocked
                        "You suddenly realize where you've seen this name before."
                        "The Miyozaki family is a well-known criminal organization."
                        "As Jun's black car drives away, you can't help but stare after it in shock."
                        "You've made friends with the {i}mafia{/i}."
                        show chelsea blank
                        "You contemplate this on your walk home, the favor he offered making a little more sense to you."
                        "You aren't sure if you'll ever have the courage to ask such a favor, even on people that might deserve it..."
                        "You try to put it out of your mind as you head home."
                        jump events_end_period
                    "Go to Room 7." if True:
                        show chelsea blank
                        "Deciding to not interrupt, you head into your room and shut the door."
                        show bg Karaoke1 with dissolve
                        show chelsea happy
                        "After settling down in your room, you choose a song and grab your microphone. Time to sing!"
                        "You start off with a simple song to begin. When you finish, your neighbors knock on the wall."
                        "You grin and listen carefully for their song to finish. You knock in reply."
                        show chelsea laugh
                        "This occurs for the rest of the night, both of you taking turns knocking against the wall in a sort of applause when one of your songs ends."
                        "Halfway through your paid session, you hear a knock on the door."
                        "You answer to find one of the waiters with a tray of chicken wings and a beer."
                        "Waiter" "[pcname]?"
                        show chelsea confused
                        pcname "Yeah, that's me. I didn't order any of this, though..."
                        "Waiter" "It's already paid for by Room 6."
                        show chelsea blank
                        "He holds out a note to you."
                        "As you read it, the waiter sets down the wings and beer on the table before taking his leave."
                        "The note is from Jun."
                        "'Your singing is beautiful tonight! Enjoy these on me and the boys! - Jun'."
                        show chelsea happy
                        "How nice!"
                        "You enjoy the wings they sent to your room before continuing your set."
                        "Before you leave for the night, you write a thank you on the back of the note and slide it under their karaoke room door."
                        jump events_end_period
            elif True:
                show chelsea blank
                "You pass by your noisy neighbors on your way to your room."
                show chelsea happy
                "You still feel a little resentment after your last visit, but you'll try to make the best of it."
                show bg Karaoke1 with dissolve
                "Once you enter your room and settle in, you grab your microphone. The music starts up and it's time to sing!"
                "You let yourself unwind for a few hours, singing out all your troubles into your microphone."
                "Occasionally you hear a few knocks from your neighbors, but you try to ignore them."
                "At the end of your set you gather your things and walk back out into the city."
                jump events_end_period
        "Leave." if True:
            "You're not really in the mood for singing today."
            "You continue on your way."
            jump events_end_period

label townkaraoke4:
    show chelsea blank at right with moveinright
    "As you walk by the busier club district of downtown, you see \"STAR LIGHT\" on the corner. A bright neon sign flashes 'KARAOKE!' in the window."
    "Would you like to go in?"
    menu karaokeenter4:
        "Go in." if True:
            "A tall man with several tattoos and bright purple hair greets you behind the counter."
            "You're about to pay, but he holds up a hand."
            "Cashier" "Room 6 is all ready for you."
            show chelsea confused
            pcname "Ah, room 6? I think there's a mistake. I haven't even paid yet."
            "Cashier" "Are you [pcname]?"
            pcname "Yes..."
            "Cashier" "Your room fee was covered by your friends. Please enjoy!"
            "He gestures down the hall toward room 6. Confused, you make your way down."
            show chelsea blank
            "As you walk by, you see the smoker in his usual spot. You both make eye contact, and as usual, you look away before he does."
            show bg Karaoke2 with dissolve
            "Before you can knock, Jun is already opening the door. The other men hold up their beer mugs in a cheer, crying out your name."
            show chelsea happy
            "Diego" "We were hoping you'd come back!"
            "Jun" "Have a seat. We were just about to start."
            "You resume sitting beside Chris and Terry. Chris hands you a menu."
            "Chris" "Pick whatever you want, it's on us."
            "What would you like to drink?"
            menu karaokemenu:
                "Beer" if True:
                    pcname "I'll take a beer."
                    $ corruption +=1
                "Soda" if True:
                    pcname "Just a soda, please."
                "Water" if True:
                    pcname "I'm fine with water, thank you."
            "Chris nods, picking up the room's phone to place the order."
            "The men take turns singing out 1980's pop hits, occasionally duetting together on more romantic pieces."
            "The drinks keep coming, and you lose track in the revelry of it all."
            "Until you really have to use the bathroom."
            show chelsea blank
            pcname "Ah, I'll be right back."
            "Diego" "Don't take too long! You're up next!"
            show bg SchoolRestroom with dissolve
            "Jun takes the stage as you sneak out into the hallway. You make your way down to the restrooms and relieve yourself in one of the stalls."
            show chelsea shocked
            "As you exit, you're shocked to find a man standing by the sinks."
            show chelsea embarrassed
            "You were sure you'd entered the lady's room, but embarrassment hits you hard as you reconsider your decision."
            pcname "I'm so sorry. Am I in the wrong bathroom? I didn't realize."
            "Smoker Man" "You aren't in the wrong bathroom."
            show chelsea confused
            "The way he holds himself unsettles you. He looks as though he's been waiting for someone."
            pcname "O-Oh... I'll just be going then..."
            show chelsea blank
            "You try to step to the side. He steps along with you."
            "As you take another look at him, you realize he's been the man smoking outside of the bathrooms every time you've visited."
            "You make a run for the door."
            "He's faster."
            show chelsea shocked
            "The man grabs your wrist, yanking you back roughly into the bathroom. You let out a squeal. He clamps his hand over your mouth, the other yanking your arm up behind your back."
            "Smoker Man" "Shut up."
            "You feel him yank your arm up higher, threatening to break it. You let out a muffled yelp of pain behind his hand."
            "Terrified he'll break your arm, you remain as still as your trembling body will allow."
            "Smoker Man" "Scream again, and I'll cut out your tongue."
            menu karaokefightback:
                "Fight back." if True:
                    show chelsea angry
                    "He lets the words sink in before removing his hand from your mouth."
                    "You immediately clamp your teeth down on his hand as hard as you can."
                    "Smoker Man" "Shit!"
                    "The metallic taste of blood fills your mouth as you break into his skin. He releases your arm in surprise."
                    "You wiggle out of his grip, releasing your teeth's hold on his hand. He grabs you by the back of your shirt before you can run away."
                    "Smoker Man" "Get back here, bitch!"
                    show chelsea shocked
                    "He yanks you backward. You stumble in his direction as his bloodied hand forms a fist and makes contact with your face."
                    "You let out a yelp. As your head reels, he gropes your breasts violently, using them to pull you toward him."
                "Stay still." if True:
                    show chelsea sad
                    $ corruption +=1
                    "He lets the words sink in before removing his hand from your mouth. You bite your lip hard, struggling to hold in a petrified scream."
                    "His hand gropes your breast roughly, squeezing it tightly between his grubby fingers."
                    "You feel angry and frightened tears prick the edges of your eyes, but try to remain quiet."
                    "His hand trails down your stomach and under your clothes, reaching between your legs."
            "Smoker Man" "Not so tough without your friends here, are you? He-"
            show chelsea shocked
            "His words are abruptly cut off, replaced with an angry yowl of pain."
            "His grip on you relinquishes immediately. You pull yourself away, surprised to find a dagger stuck deep in his calf."
            "The man reaches down for it, his hands itching to remove it as blood stains his pants, but making no move to do so."
            "Jun stands in the doorway of the bathroom. He twirls a dagger between his hands."
            "Jun" "I was wondering what was taking so long."
            "Smoker Man" "Fuck you!"
            "Jun laughs."
            "Jun" "[pcname], would you like me to finish the job?"
            show chelsea blank
            menu karaokefinishhim:
                "Yes." if True:
                    show chelsea angry
                    "Jun grins approvingly."
                    "Jun" "As you wish. It's your turn, by the way."
                    show chelsea blank
                    "Jun steps aside, making room for you to return to the karaoke room."
                    "You don't miss the horrified gaze your attacker gives to you as you return to the karaoke room."
                    "Jun shuts the door behind you."
                    "You wait outside in the hallway until he's finished. He returns with a pleasant smile, tucking the dagger away in his jacket."
                    "Jun" "Shall we?"
                    $ corruption +=5
                "No." if True:
                    "Jun" "Very well."
                    "Disappointment is evident in his voice, but he steps aside, leaving you room to exit."
                    "Jun" "It's your turn, by the way."
                    "Jun follows behind as you make your way back to the karaoke room."
            show chelsea happy
            show bg Karaoke2 with dissolve
            "It's as if nothing has happened when you enter the room. The rest of the men lift their mugs of beer, cheering you on stage."
            "You take your place behind the microphone."
            "The rest of the night is spent in glorious debauchery and feminine pop hits."
            jump events_end_period
        "Leave." if True:
            "You're not really in the mood for singing today."
            "You continue on your way."
            jump events_end_period

label townkaraoke5:
    $ clothes, hair = casualwear
    show chelsea blank at right with moveinright
    "As you walk through the busier club district of town, the \"STAR LIGHT\" karaoke bar catches your eye."
    "Would you like to go inside?"
    menu finalgoin:
        "Go in." if True:
            show bg black with dissolve
            show chelsea happy
            "It would be nice to see your friends again, especially now that you're certain Jun and his men will protect you should anything go awry."
            "You head inside, smiling to the tattooed man behind the counter as you pull out your wallet."
            "He shakes his head and points down the hall."
            "Cashier" "You're all good to go."
            "You give him an appreciative smile and walk to Room 6."
            show bg Karaoke2 with dissolve
            show chelsea shocked
            "As you open the door, you're surprised to see Jun and his friends already packing up for the evening. You glance at your phone in confusion; the night has just begun!"
            show chelsea blank
            "You linger in the doorway and wait for someone to acknowledge you're presence among them. Luckily, after a few minutes, Diego notices you first."
            show GHCMan at left with moveinleft
            "Diego" "Oh, hey kid. You're here early, huh?"
            "You glance again at your phone. You wouldn't call this {i}early{/i}, but maybe you're mistaken and they just arrived as well?"
            show chelsea confused
            pcname "Hey..."
            show chelsea blank
            "You awkwardly step into the room and watch as they gather their things and prepare to leave. No, they're definitely finished for the day."
            show chelsea sad
            "Unease shifts in your stomach. It's one thing to be disappointed that you arrived too late to hang out with everyone, but something tells you it's more than that."
            show chelsea blank
            if club == "track":
                show chelsea confused
                pcname "Did you guys just get here?"
            elif club == "cheer":
                show chelsea happy
                pcname "Aww, why the rush? Did something come up?"
            elif club == "yearbook":
                show chelsea sad
                pcname "D-Did I show up too late?"
            "Diego and Chris share an awkward look before glancing at Jun across the room. They shake their heads."
            show chelsea blank
            "Chris" "Nah, we should have been out of here already. The room is all yours to go, though."
            "All yours? Did they intend to just leave before you even showed up?"
            show chelsea confused
            pcname "What do you mean?"
            "Neither of the men give you an answer, too busy straightening the room out before they part. Jun hesitates in the back, shrugging his jacket on."
            show chelsea sad
            pcname "Jun? What's going on?"
            "Jun" "Ah, hey kid. I wasn't expecting to see you today. I would have left a note..."
            show chelsea blank
            "Something about his attitude feels off; in fact, {i}everyone{/i} in the room has felt off today."
            if club == "track":
                show chelsea confused
                pcname "What's with everyone today? You're not trying to avoid me, right?"
                "Jun" "I wouldn't call it avoiding per say. Think of it as a safety protocol."
                pcname "And what's that supposed to mean?"
                show chelsea blank
            elif club == "cheer":
                show chelsea laugh
                pcname "Well don't run off now; I just got here! Let's at least sing a little before you go."
                "Jun" "I'd love to, but I can't, kid. The room is here for you to use, though. We'll be seeing you around."
                show chelsea happy
                pcname "'Seeing you around'? You're making it sound like I might never see you again."
                show chelsea blank
            elif club == "yearbook":
                show chelsea sad
                pcname "Is... Is everything okay?"
                "Jun" "Yeah! Of course. Things are fine. The room is here for you to use, so we'll be seeing you around."
                "His words, while trying to be comforting, leave you feeling even more uneasy."
                pcname "You- You don't want to see me anymore?"
            "Jun scratches the back of his head and lets out a long drag of his cigarette. It's obvious he had been hoping to avoid talking about the subject with you altogether."
            "Jun" "Look, I've been thinking, and it's probably for the best if you don't hang out with us like this anymore, ya dig?"
            show chelsea blank
            "Jun" "There are a lot of shady characters we deal with and the last thing we need is you getting involved in that again..."
            "You can't help but think back to the incident in the bathroom the last time you were here."
            pcname "Is this because of what happened before?"
            "Jun lets out a sigh."
            "Jun" "Partially. It's just safer this way if you aren't hanging out with us in public like this. We can't protect you all the time, so if anything were to happen while we weren't around, well, we'd feel awful about it, kid."
            "Noticing the disappointed look on your face, Jun steps forward and lightly ruffles your hair. He's so kind with you that, if you didn't know any better, you wouldn't even guess that he was involved in the mafia."
            "Jun" "Don't think so hard about it. Not like you won't ever see us again. Ah, here, give me your phone."
            "You oblige, passing him your cellphone. Jun fumbles with it for a few minutes before handing it back to you. His name and number appear on your contact list."
            "Jun" "You're a good kid. Let me make it up to you; I'll offer you a favor. Give this number a call if someone's bothering you and we'll handle it."
            "Jun" "This is a one-time thing, though, got it? Don't need that kind of power going to your head."
            "There's a serious undertone to his suggestion. You don't have to think twice to understand what kind of favor he's offering you."
            if club == "track":
                "You can't blame him for making it a one-time thing; having that kind of power over someone's life could easily go to anyone's head. It's best to give it some time and think it over... if you plan to use it at all."
                pcname "Thanks, Jun."
                show chelsea sad
                pcname "This kind of sucks, though. I was really hoping to duet with Chris today..."
            elif club == "cheer":
                "The idea of having that kind of power over someone's life is a little overwhelming. You never know what creep you'll need to use it on next, though..."
                pcname "Thanks! I appreciate it."
                show chelsea sad
                pcname "I'm sad you're leaving though! I wanted to duet with Chris today!"
            elif club == "yearbook":
                "You try not to think too hard about what his favor entails; the idea of having that kind of power over someone's life... it's terrifying."
                "But you never know when you'll need it..."
                pcname "O-Okay."
                show chelsea sad
                pcname "This is really sad, though... I wanted to duet with Chris today..."
            show chelsea blank
            "Jun lets out a loud, startled laugh."
            "Jun" "Yeah? Well, maybe we'll need to start hosting these at our place next time. Just shoot me a text so I have your number, alright kid?"
            "You nod and send him a quick text. Jun's phone blinks and he rolls his shoulders in satisfaction."
            "Jun" "See you around, kid."
            show chelsea sad
            "With one more ruffle to your hair, Jun leaves the karaoke bar."
            "You look around the empty room, disappointed to find yourself complete and utterly alone."
            show chelsea blank
            "You let out a sigh and pick up the microphone. Might as well make use of the room while you have it..."
            $ mafiafavor = True
        "Leave." if True:
            "As nice as it would be to see your friends again, you're just feeling a little too tired to sing tonight."
            pcname "Maybe I'll come back some other time..."
            hide chelsea with moveoutright
            "With a yawn, you walk past the karaoke bar without a second thought."
    scene bg black with dissolve
    "You've reached the end of the Karaoke Side Story in this version! Keep and eye out for more content!"
    jump events_end_period

label townbookstore:
    show chelsea at right with moveinright
    "It's so hard to find somewhere quiet in the city..."
    "As you turn down another street, a small little shop catches your eye: \"TWILIGHT TALES\"."
    show chelsea happy
    "Worn books and signed editions are displayed in the window of the bookshop."
    menu enterbookstore:
        "Enter." if True:
            "A little bell rings as you enter."
            show chelsea blank
            "An elderly woman stands behind the counter, squinting behind a thick pair of glasses."
            "What would you like to buy?"
            menu bookchoice:
                "Classic Myths and Fairytales $10 +1 Grades" if Cash > 10:
                    $ Cash -= 10
                    $ intelligence +=1
                "Serial Killers and Forgotten Victims $15 +2 Grades" if Cash > 15:
                    $ Cash -= 15
                    $ intelligence +=2
                "Romance during the Renaissance $20 +3 Grades" if Cash > 20:
                    $ Cash -= 20
                    $ intelligence +=3
                "BJ's, PJ's, and Sexy Slumber party Games $35 +5 Corruption" if Cash > 35 and corruption > 20:
                    $ Cash -= 35
                    $ corruption +=5
                "Nothing." if True:
                    pass
            "The bell rings again as you leave."
            show chelsea happy
            "What a cute little shop!"
            jump events_end_period
        "Leave." if True:
            show chelsea blank
            "You aren't really in the mood to shop for books."
            "You walk away from the bookstore."
            jump events_end_period

label towncatcall:
    show chelsea blank at right with moveinright
    "You stand at a crosswalk, surveying the city streets around you as you try to decide where to go."
    "There's the movie theater, the mall, the coffee shop..."
    "As you're trying to make a decision, a loud whistling catches your attention."
    "You glance behind you at a group of men in their mid-twenties, eyeing you over from outside of a bar."
    "There are four of them, all in varying stages of drunkenness."
    "A man with blonde hair and a bomber jacket stumbles toward you."
    show chelsea embarrassed
    "Blonde" "Hey, beautiful! Why don't you come over here and show me how you shake that ass?"
    "The group laughs, as though he's told a brilliant joke. You feel a blush paint your cheeks."
    "The man closest to him, a brunette sweating badly enough to stain his tank top, curls two fingers toward you, motioning you to join them."
    "Sweaty Man" "Aw, c'mon, don't be shy. Show us a pretty smile!"
    show chelsea blank
    "He grins at you as he takes a step forward. You move away, uncomfortable at his advance."
    "The walk sign pops up at your crosswalk. You hurry across the painted white lines."
    "Luckily they don't bother following you. Instead, they direct their calls to another woman passing by."
    if club == "track":
        show chelsea angry
        pcname "What pigs..."
    elif club == "cheer":
        "You roll your eyes. Boys can be so brutish."
    elif club == "yearbook":
        show chelsea embarrassed
        "You try to hide the flush on your cheeks, uncomfortable from the unwanted attention."
    show chelsea embarrassed
    "You look down at your outfit, feeling a little more self-conscious about your appearance as you walk away."
    jump events_end_period

label towncatcall2:
    show chelsea blank at right with moveinright
    "As you make your way down the street, you see a car pull up beside you."
    "You think nothing of it at first, but the driver slows down to match your speed."
    "You try to quicken your pace, but he follows you, his eyes raking over your body as you walk."
    "He rolls down the window."
    "You immediately recognize him as one of the men from outside the bar when you were first catcalled."
    "He's not so sweaty now that he's sober, but his manners have not improved."
    "Sweaty Man" "Hey, baby, what's the hurry? Where we going?"
    "You bite your tongue and keep walking. There's no point in indulging him."
    "Sweaty Man" "Those are some damn nice legs. I'd like to see them wrapped over my shoulders."
    "He laughs, expecting you to join in. You don't give him the satisfaction."
    "Sweaty Man" "Hey, slow down. Why're you looking so mad? C'mon. Gimme a pretty smile. I bet you got a real nice one. Just one. Please?"
    menu catcallresponse:
        "Get lost!" if True:
            show chelsea angry
            "Sweaty Man" "Oh, but I'm already lost in your eyes."
            "You don't miss how his eyes are clearly focused on your breasts."
            "You cross your arms over your chest and pick up the pace."
            "The car rolls to a stop at a red light. You take the opportunity to make a shortcut through an alleyway, as far from him as you can."
            if club == "track":
                "What a prick! You wish these guys would just leave you alone."
            elif club == "cheer":
                "You understand men have desires, but you have a right to walk by without being harassed!"
            elif club == "yearbook":
                "That was terrifying! You try to slow your racing heart as you make sure he didn't follow you."
            show chelsea blank
            "Still..."
            "You look down at your breasts. You can't deny that they look decent."
            "That still doesn't give him any right to behave as he did."
            "You hurry off, hoping to never see him again."
            jump events_end_period
        "Leave me alone." if True:
            "Sweaty Man" "Come on. Just one smile. Please? Look. This is how you do it."
            show chelsea angry
            "He smiles at you, as though that will encourage you to respond. When you scowl back, he glares at you."
            "Sweaty Man" "Bitch! Fuck it. You aren't even fucking hot. Ugly slut."
            "Even as he says it, you notice how he stares at your breasts."
            "You cover your chest and pick up the pace."
            show chelsea blank
            "His car rolls to a stop at a red light, and you hurry off into an alleyway, putting as much space between you both as possible."
            "You feel a little sick to your stomach at his words and lustful gaze."
            "You don't understand what's so hard about the concept of being left alone when asked."
            "Still..."
            "You look down at your breasts. You can't deny that they look decent."
            "That still gives him no right to behave as such."
            "Irritated, you walk away, hoping to never see him again."
            jump events_end_period
        "Say nothing." if True:
            "Your lack of response seems to trigger a more aggressive response."
            "Sweaty Man" "I'm just asking for a smile! Bitch. You aren't even good looking."
            "Even as he says it, you notice how his eyes rake over your breasts."
            "You cover your chest and storm off down an alleyway, as far from him as possible."
            "Once he's out of sight, you force yourself to take deep breaths and calm down."
            "The whole ordeal leaves you feeling a little shaken."
            if club == "track":
                "You clench and unclench your hands into tight fists. How dare he...!"
            elif club == "cheer":
                "You straighten yourself, trying to brush it off. Men are brutes, but you shouldn't let them get to you this much."
            elif club == "yearbook":
                "You take another deep breath, trying to come down from your rising anxiety."
            "Still..."
            "You look down at your breasts. You can't deny that they look decent."
            "That still gives him no right to behave like such an animal."
            "Making sure you're not being followed, you continue back into the city."
            jump events_end_period

label towncatcall3:
    show chelsea blank at right with moveinright
    "You step out of your local post office, a little tired, a package in your arms."
    "You had ordered a book weeks ago, but they had consistently missed you at home."
    "You suppose you feel a relief at finally having it in your arms, even if it was an effort to get it."
    "As you begin to make your trek home, you pass by a large construction site. It appears they're putting a new apartment complex."
    "You admire the steel structure for a moment before one of the construction workers catches your eye."
    "It's one of the drunken men from the bar, a member of the group that catcalled you."
    "Although he had not directly catcalled you, you recognize him by his messy black hair sticking out from his construction hat."
    "He had worn his hair similarly under a baseball cap outside the bar."
    "He sits on his work bench, an open lunchbox to his side. He must have been on his break."
    "Lunch seems to be the last thing on his mind as he ogles your legs, though."
    "You try to avert your gaze, hoping he too will look away."
    "Construction Worker" "Hey, sexy."
    if club == "track":
        show chelsea angry
        "Damn it."
    elif club == "cheer":
        "You sigh. Of course."
    elif club == "yearbook":
        show chelsea shocked
        "You're startled by his voice, but try to collect yourself."
    show chelsea blank
    "You try to ignore him, clutching the package a little tighter to your chest."
    "Construction Worker" "That's a pretty big package. You think you can handle all of that?"
    "The double meaning in his words does not impress you. You stick your chin in the air, determined to leave his presence as quickly as possible."
    "Construction Worker" "C'mon, baby. Hey. Hey! I'm talking to you."
    "Yes, you are aware of that."
    "He rises from the bench, and you're suddenly grateful for the metal fence between the two of you, no matter how flimsy it may be."
    "He keeps up with you, calling out behind the fence."
    "Construction Worker" "Hey! You better learn to answer when a man is speaking to you!"
    menu catcallresponse2:
        "Tell him to leave." if True:
            if club == "track":
                show chelsea angry
                pcname "Fuck off!"
                pcname "Is that enough of an answer for you?"
                "You hold up your middle finger in emphasis."
            elif club == "cheer":
                pcname "Go away. Clearly you're not worth my time."
                "You flick your hand, as if swatting a fly from the air."
            elif club == "yearbook":
                pcname "Leave me alone. I-I don't want to be bothered."
                "Although your voice is quiet, it's enough for him to hear you."
            "The worker grabs at the fence, rattling it loudly as he tries to get in your face."
            "Construction Worker" "Fucking cunt! You ugly whore!"
            if club == "track":
                "You don't give him the satisfaction of stepping away. You glare right back at him, daring him to make a move."
                "He spits at you. You laugh and keep walking."
                show chelsea blank
                "You can't help but think about how ridiculous he must look. Like a child throwing a tantrum."
                "Are men really so fragile that one rejection will send them into a spur of insults?"
                "Still..."
            elif club == "cheer":
                "You laugh, flipping your hair over your shoulder."
                pcname "Tell me something I don't know."
                "He continues yelling jeers at you as you walk away, forcing yourself to keep a steady pace until you're out of his sight."
                "Once he's gone, you fall back against the wall of a nearby building, letting out a long breath."
                "You can't deny that had been a frightening encounter."
            elif club == "yearbook":
                show chelsea shocked
                "You let out a little squeal, jumping back from the fence."
                show chelsea sad
                "He shakes it harder, causing you to further back away in fear."
                "You clutch your package tightly to your chest, practically running down the street away from him."
                "Tears prick at your eyes, and before you can stop them, they flood down your face, staining your cheeks."
            "You think about the hatred on his face when he rattled the fence. It was clear that he would've preferred to be rattling you."
            show chelsea blank
            "Maybe you'll try to think of another way to get them to leave you alone without a threat on your life."
            "You hope there won't be a next time."
            jump events_end_period
        "Respond with sarcasm." if True:
            if club == "track":
                show chelsea angry
                pcname "And you should learn when to shut the fuck up."
            elif club == "cheer":
                pcname "I don't see any {i}men{/i} around here. Only a noisy pig."
            elif club == "yearbook":
                "In a bout of bravery, you speak before thinking."
                pcname "Is this a man talking to me, or a child?"
            show chelsea blank
            "Yes, you're very grateful for that fence."
            "The worker grabs at the fence, rattling it loudly as he tries to get in your face. You step away."
            "Construction Worker" "You fucking bitch! I was just trying to be nice! You're a fat fucking cunt! A pig!"
            "He makes oinking noises as you walk down the street."
            if club == "track":
                show chelsea laugh
                "He looks so absurd, you can't help but laugh in his face, further angering him."
                "He makes the noises louder as you laugh hysterically down the street, clutching your stomach."
            elif club == "cheer":
                "You roll your eyes, ignoring him, despite the slight shake in your legs. If you rose to every bait, you would stoop down to his level."
                "You're better than rock bottom."
                "As you walk away, his voice fades, and you allow yourself to laugh a little."
            elif club == "yearbook":
                show chelsea sad
                "You stare at the ground, tears pricking your eyes."
                "Although it shames you, a part of you recognizes how ridiculous he looks, and you feel a little comfort in that."
            "Are men really so fragile that one comment will turn them into complete children?"
            "Still, you think of how he shook the fence, his face red with rage."
            "It could have been your neck."
            "Maybe next time you'll find another response. There must be a way to keep them from bursting into a rage."
            "Although, you hope there won't be a next time."
            jump events_end_period
        "Say nothing." if True:
            "You bite your tongue and keep walking."
            if club == "track":
                "Being silent will piss him off more."
            elif club == "cheer":
                "He isn't worth your time."
            elif club == "yearbook":
                "You don't want to risk instigating him."
            "He bangs against the flimsy gate as he follows after you, yelling to get your attention."
            "Construction Worker" "Hey! Hey! I'm {i}talking{/i} to you! What? are you deaf? Listen to me!"
            "Construction Worker" "Fucking cunt! You're an ugly bitch! I only said those things because I felt bad for you!"
            "You keep quiet until you're too far to hear his insults any longer."
            if club == "track":
                "You flex your fists at your sides, trying to resist the urge to run back there and bash his face in."
                "Did that prick think he could get away with saying those things just because you didn't respond?"
                "You'd really like to give him a piece of your mind."
                "Yet..."
            elif club == "cheer":
                "Thinking back, you can't help but realize how stupid he looked."
                "He was the one that tried hitting on you. Did he think he could take that back by calling you a bitch?"
                "You allow yourself to laugh. The entire thing is so ridiculous."
                "Still..."
            elif club == "yearbook":
                "You let out a shaky breath, reminding yourself to breathe. Your body trembles, shaken up by the encounter."
            "He looked furious when you'd left. A part of you worries about what could happen next time if someone else showed a more violent reaction."
            "You'll need to think through your options. There must be a way to stay safe without eliciting their anger."
            "Although, you hope there won't be a next time."
            jump events_end_period

label towncatcall4:
    show chelsea blank at right with moveinright
    "You push your cart around the grocery store, scrutinizing the produce and their prices. You mark off another item from your grocery list."
    "You should have known better than to go shopping while you were hungry."
    "Your cart feels heavier than you are, and while a part of you wonders if you'll really eat all of this, the hungrier part of you demands you grab more."
    "As you place a few cantaloupes into your cart, you notice a man in his twenties staring at you from down the aisle."
    "You understand him to be the man who catcalled you a couple of weeks ago."
    "His blonde hair is done up a little nicer now, his bomber jacket hanging loosely from his body."
    "You begin to push your cart away."
    "He catches up easily."
    "Grocery Man" "I think we've met before. Name's Nate. Did you miss me?"
    "You ignore him, continuing to push your cart past him."
    "Nate" "Those are some pretty big melons. Are those all for you?"
    "The hungry part of you answers before you can rationally think."
    pcname "Yes. I'm starving."
    "Nate" "I bet I can fix that. How do you like your dick? Big and juicy?"
    menu catcallresponse4:
        "Go away." if True:
            "Nate" "Don't be like that, baby girl. I'm just trying to have a conversation here."
            "Your stomach grumbles. Your patience is wearing thin."
            if club == "track":
                show chelsea angry
                pcname "Do I need to spell it out for you? Fuck off. F-U-C-K. O-F-F."
            elif club == "cheer":
                pcname "And this conversation is longer than your dick. Leave me alone."
            elif club == "yearbook":
                pcname "I just want to be left alone. Please go away."
            "You push your cart away. He grabs the edge of your cart, causing it to run into one of the stands."
            if club == "track":
                show chelsea angry
                pcname "What the fuck?"
            elif club == "cheer":
                pcname "Do you mind?"
            elif club == "yearbook":
                pcname "Excuse me?"
            "Nate" "Stupid Bitch."
            "He storms off leaving you in bewilderment as to what just happened."
            "Suddenly the stand you ran into gives way and sends produce tumbling out everywhere."
            show chelsea shocked
            "It takes you a moment to realize what's happening."
            show chelsea embarrassed
            "After he leaves, one of the employees rounds the corner and checks up on you, prodding about what happened."
            "You tell him it's an accident, too embarrassed at your lack of response to spill the truth. You're sure they'll find out on the security cameras later anyway."
            "He helps you clean up, promising to help take care of the groceries. You assure him it's fine and leave without purchasing anything."
            "You've lost your appetite anyway."
            jump events_end_period
        "Play along." if True:
            $ corruption +=2
            "You don't have the energy to start a fight with him. Besides, it has not ended very well for you in the past."
            if club == "track":
                pcname "Mmm, you know exactly what I like."
                "You have to refrain from rolling your eyes. Nate grins at you."
            elif club == "cheer":
                pcname "Are you offering?"
                "You bat your eyelashes at him, allowing your gaze to linger on his crotch. Nate grins at you."
            elif club == "yearbook":
                show chelsea embarrassed
                pcname "I-I'm not sure. Maybe..."
                "You look away shyly. When you glance in his direction, you see that Nate's smiling."
            "He leans against your cart, making no effort to hide his gaze on your body. You're suddenly very aware of how your clothes hug your body."
            show chelsea blank
            if club == "track":
                "Nate" "Then I've got a treat for you."
            elif club == "cheer":
                "Nate" "As long as you're taking it."
            elif club == "yearbook":
                "Nate" "How about we find out together?"
            "He takes your grocery list and pen, scribbling down his name and number before passing it back to you."
            show chelsea shocked
            "As he walks by, his hand cops a feel on your ass. You freeze, shocked by the touch."
            "He takes this another way. His hands roam across the surface of your ass comfortably."
            "Nate" "I look forward to hearing from you."
            "He pats your rear before disappearing down the aisle. You stare at his name and number on your grocery list."
            show chelsea confused
            "That was all it took? No insults, no threats of violence?"
            "This was easier than you thought."
            show chelsea blank
            "In the pit of your stomach, you understand that there's something wrong about this, though. Shameful, even."
            "You shouldn't need to give in to them to avoid violence."
            "Still, this is the first instance in which you feel safe after one of your encounters."
            if club == "track":
                "You shrug. It was definitely better than entering a screaming match with him."
            elif club == "cheer":
                "You toy with the paper in your hand, glancing back toward Nate. Flirting back hadn't been so bad. In fact, it was a little fun."
            elif club == "yearbook":
                "You feel a sense of relief wash over you. If this is what happens when you play along, you'll take that over their anger any day."
            "You crumple up the paper, intending to throw it out later."
            jump events_end_period

label towncatcall5:
    show chelsea blank at right with moveinright
    "You had been trying to avoid the crosswalk by the bar since your last encounter there, but today you had no choice."
    "Today also seems to be the day that Nate and his gang will terrorize you."
    "You immediately recognize the men that had harassed you at every turn the past couple of weeks. Nate stumbles out of the bar, a bottle still clutched in his hand."
    "The construction worker and the sweaty man- Nick and Steven, from what you heard Nate yelling loudly a moment ago- fall out of the doors after him."
    "A final man, quieter than the others but no less inebriated, follows after. It's only be chance you catch Nate calling him Alex."
    "You look back at the crosswalk sign, silently willing it to change colors before they notice you."
    "Nate" "Yo. Yo! Sweetie! Girl with the nice {i}ass{/i}!"
    "You turn slightly, acknowledging them. Their eyes rake across your body where their hands cannot touch."
    menu catcallstare:
        "Accept their stares." if True:
            $ corruption +=1
            show chelsea embarrassed
            if club == "track":
                "You shift a little under their gaze. You know you look good. You don't need them telling you as much."
            elif club == "cheer":
                "You allow yourself a small smirk, swishing your hips to the side. If they're going to keep calling for you, they might as well see just how good you have it."
            elif club == "yearbook":
                "You feel a flush of embarrassment at their stare, but a small part of you is thrilled at the public attention."
        "Turn away." if True:
            "You've had enough of their brazen stares. You stare back at the crosswalk, ashamed."
    "They approach you in a semi-circle, admiring every inch and curve of your body. You're suddenly very aware of what you're wearing."
    "Nate" "It's Aaron's birthday, here, ain't it, Aaron?"
    show chelsea blank
    "Nate slings an arm over their quiet companion, yanking him under his arm."
    "Nate" "You got a birthday present here for him?"
    pcname "I'm afraid I don't."
    "Nick" "That ain't true."
    "Steven" "I bet you can give him a good show."
    "Despite how quiet Aaron is, he doesn't seem to be opposed to any of this. If anything, he's only staring at you more intently, waiting for your reaction."
    "Nate" "Just show us a little bit. Give Aaron here something to remember the night by."
    "You glance between them, then at the others in the crowded crosswalk. What they're asking you to do... in public, no less..."
    menu catcallflashthem:
        "Flash them." if True:
            $ corruption +=1
            show chelsea embarrassed
            "You bite your lip, fingers curling under the edge of your tank top, and then the cups of your bra."
            "If you can be quick, and no one else sees..."
            "You quickly pull down your shirt and bra, exposing your breasts to the air."
            "Your nipples harden against the cool breeze, pointing outward toward them invitingly."
            "There isn't a pair of eyes that aren't on you. You feel their stares bore into you, the heat of their gazes practically radiating off of you."
            "You quickly yank your bra and shirt back up, the fabric feeling oddly stiff against your recently exposed breasts."
            "Grins spread across the men's faces, pleased with their show."
            show chelsea blank
            $ catcallflashing = True
            "Nate" "Now how about something a little more physical? He's gotta have a real present, you know."
            "The other men nod in agreement, waiting to see how much they can get away with."
            menu catcallpanties:
                "Give them your panties." if True:
                    $ corruption +=2
                    show chelsea embarrassed
                    "Feeling a little more encouraged, you reach underneath the holes of your shorts, gripping the hem of your panties."
                    "Despite the difficulty in their removal, the men watch eagerly as you slowly extract your legs around the panties and place them into Aaron's hands."
                    pcname "Happy birthday."
                    "The light on the crosswalk changes."
                    "You don't spare the men another glance as you rush across the crosswalk, the adrenaline of the moment wearing off."
                    "You feel a thrill of excitement as you continue through the city, the breeze under the exposed leg holes of your shorts reminding you of what you've done."
                    "There's something exciting about being seen."
                    $ corruption +=2
                    jump events_end_period
                "Say goodbye." if True:
                    "You shake your head, taking a step back."
                    pcname "Happy birthday."
                    "The light on the crosswalk changes."
                    "You don't spare the men another glance as you rush across the crosswalk, the adrenaline of the moment wearing off."
                    "There's something exciting about being seen."
                    jump events_end_period
        "Run away." if True:
            "You glance back at the crosswalk sign. It still isn't safe to cross."
            "The men step closer to you, their eyes focused on your body. No one seems to acknowledge that you have a head."
            "You look back at the crosswalk. The road is emptying, but it's not safe..."
            "As Nate steps closer, you throw yourself out into the street."
            "Car horns blare and drivers yell at you as you race across the street, putting as much space between you and the men as you can."
            "When you glance over your shoulder, you see Nick try to step out after you, but quickly retract when a car nearly smashes into his side."
            "You continue running, your feet slapping loudly against the pavement as you escape from their gazes. You don't pay attention to where you're going as long as it's away from them."
            "They don't follow, but you aren't sure which part of town you ended up in."
            "It takes you another hour before you're able to find your way back to a familiar street. By then, they're gone."
            jump events_end_period

label towncatcall6:
    show chelsea blank at right with moveinright
    "You wander past the city streets, watching the streetlights blink on as the sun dims behind the buildings."
    "Despite the oncoming night, the city is alive as city-goers dash between bars and houses, ready to start their night of debauchery."
    "You should probably start heading home..."
    "As you pause at the crosswalk, you see Nate's group approach their favorite bar, excited to end their sobriety."
    "Nate catches your eye and waves."
    "Nate" "Hey! Big tits! C'mere!"
    menu catcalljoin:
        "Join them." if True:
            $ corruption +=1
            "The comment brushes off of you, almost an endearing nickname at this point."
            show chelsea happy
            "You approach the group of men with a smile."
            "Nick" "Aaron wanted to thank you for last time. Right, Aaron?"
            "Nick slings an arm around the petite man's shoulders."
            "Aaron" "Yeah. Come grab a beer with us."
            menu catcalldrink:
                "Accept offer." if True:
                    $ corruption +=3
                    show chelsea embarrassed
                    "Your cheeks flush pink at the memory, but you give them a small accepting smile."
                    "You aren't even sure you'll be able to get into the bar being underage, but why not?"
                    pcname "Alright."
                    "They burst into whoops and hollers at their small victory. Nick and Nate throw their arms over your shoulders and escort you inside."
                    show chelsea blank
                    "It's still early, but the bar is bustling with college students ready to begin the night."
                    "The guys lead you over to a booth against the wall. Nick leaves to get drinks while the rest of you chat."
                    "Steven and Aaron sit on either side of you, squishing you between them as Aaron takes a seat across."
                    "Steven" "So what's your name, baby doll?"
                    pcname "[pcname]."
                    "Nate" "I think I prefer big tits."
                    "The men laugh."
                    "Nick returns with the drinks shortly after, dispersing them between all of you before sitting down."
                    "You all chat over drinks, and despite their initial introductions, you find yourself fascinated."
                    "The drinks keep coming, and with it, more stories spill out between them. You learn that they met during freshman year, with the exception of Nate and Aaron, who have been friends since high school."
                    "Nate" "And he's a horrible sleeper. Snores and thrashes like he's being mauled."
                    "Nate jabs a thumb at Aaron, who laughs in response."
                    hide chelsea with dissolve
                    scene bg black with dissolve
                    "You laugh as well, the alcohol flooding your system. You feel far more at ease than usual, your head slightly clouded."
                    show bg NBar1 with dissolve
                    "Steven shifts beside you some, his hand coming to rest on your thigh."
                    "You glance over at him, but don't push him away. He takes this as a sign of encouragement, his thumb rubbing circles on your inner thigh."
                    "You wonder if the others can see, but they don't seem to notice, already trailing off into another story of Aaron's sleeping habits."
                    show bg NBar2 with dissolve
                    "Steven pulls his hand further up your thigh, slipping under the top of your shorts. You try to remain neutral as his fingers press against your panties."
                    show bg NBar3 with dissolve
                    "You take another sip of beer, nearly spitting it out when his fingers slip under your panties."
                    show bg NBar4 with dissolve
                    "You expect the others to say something, to notice, but they're too far gone to pay attention. Steven's fingers part the lips of your vagina, curling up inside."
                    "You let out a small noise at the impact. This time, they notice."
                    show bg NBar5 with dissolve
                    "Nate" "Having fun, Steve?"
                    "This isn't the reaction you had expected. The conversation dies down as the men turn their attention to Steve fingering you in the booth, his fingers sliding in and out with growing ease."
                    "You glance around the bar, expecting others to notice, but everyone is wrapped in their own conversations. You think you see someone outside the window spare a questioning glance, but they walk away unaware."
                    "Steve" "Yeah. What's it to you?"
                    "You wait for one of them to object, but no one does. The table is suddenly quiet compared to the rowdy crowd around the bar."
                    "Aaron and Nick stare at you with a heavy-lidded desire in their eyes. You look away, unable to meet their gaze."
                    "Nate" "Give someone else a try."
                    show bg NBar4 with dissolve
                    "Steve continues to slide in and out of you with growing speed, his fingers curling against your g-spot. You can't help the soft whimpering that escapes your throat and hope that no one around you can hear."
                    "Although, a part of you is excited to feel such sensations in a public crowd. The idea of being caught..."
                    "His fingers pull out too soon, and you let out a soft cry of disappointment before you can help yourself."
                    show bg NBar6 with dissolve
                    "Nate's fingers are in you right after. Your body gratefully accepts him, bucking against his hand as he strokes inside of you."
                    show bg NBar7 with dissolve
                    "Steve presses his cum-coated fingers to your lips, expectant. You look to Aaron and Nick briefly before taking his fingers into your mouth."
                    show bg NBar8 with dissolve
                    "You suck on his fingers as they prod deeper into your mouth, lapping the cum with your tongue. Aaron lets out a shuddering breath, and it's only then you notice the steady movements of his arm under the table."
                    "You reach out with your leg and feel between his. Aaron's hand is wrapped around his cock, prodding out underneath his pants under the table."
                    "You feel yourself dampen with excitement at his reaction, and Nate's fingers slam into you harder than before. You bite down on your lip hard, trying to keep yourself as quiet as possible."
                    "Nick makes a similar rhythm beside Aaron, his arm shaking quickly under the table as Nate and Steve poke and prod you with their hands."
                    show bg NBar9 with dissolve
                    "Steve reaches under your shirt, pulling one of your breasts out into the open air. His mouth comes down around your taught nipple, his teeth grazing against it before sucking hard."
                    "???" "Oh my god."
                    "You glance back at the booth behind you and realize you've gathered a small audience. A group of college students watch you, too stunned to move."
                    "Your cheeks heat up, but it isn't in the initial embarrassment you expected. You feel vulnerable under their gaze, but excited at the same time. You realize with a sickening pleasure that you {i}want{/i} to be seen."
                    show bg black with dissolve
                    "The others in your group follow your gaze and quickly understand the predicament. One girl leaves her group to approach the bartender."
                    "Aaron and Nick hurriedly shove themselves back in their pants. You feel Nate yank his fingers out from you with a great disappointment, wiping the cum on your shorts."
                    "You yank your shirt back over your breast and Steve yanks his fingers from your lips as the bartender approaches."
                    "Bartender" "Break it up, break it up! That's enough fun. Get out."
                    "He jabs a finger toward the entrance door."
                    "The guys try to argue, but when the bartender threatens to call the cops, you all reluctantly grab your stuff and leave."
                    "As you all pile out of the bar, Nick and Steve yell drunken obscenities at the bartender behind them; you feel a sense of guilt."
                    show chelsea sad at right with moveinright
                    pcname "I'm sorry for getting you all kicked out..."
                    "Nate" "Sorry? Don't be. That was fun."
                    "The men nod in agreement, casting wicked glances across your body."
                    "Nick" "Wanna pick up where we left off? I want a turn."
                    show chelsea embarrassed
                    "Nick grabs your breast as you all retreat from the bar, fondling your nipple between the fabric. You look at your phone, realizing the time, and gently pull away."
                    pcname "Maybe next time."
                    "Nick tries to reach for you again, but you quicken your pace away from them and wave a quick goodbye."
                    "Nate" "We'll hold you to that!"
                    show chelsea blank
                    "Disappointed but satisfied with what they've received, the men wave their goodbyes as you depart."
                    "As you walk home, the events at the bar play in your mind."
                    if club == "track":
                        "Everything about their brazen behavior was so exciting. You can still feel their hands trailing over your body in full view of the bar patrons."
                        "You look forward to seeing what happens next time."
                    elif club == "cheer":
                        "Your clit throbs with its sudden lack of attention, and you wish that girl hadn't gotten you kicked out before you could climax."
                        "Although, you did enjoy the stares you got as the others realized just how much fun you were having in that booth..."
                        "You grin, walking a little quicker home. You definitely look forward to next time."
                    elif club == "yearbook":
                        show chelsea embarrassed
                        "You feel your face heat up in shame as you realize just how exposed you'd been in the bar."
                        "Had you really just done that?"
                        "An excitement curls in your stomach, and you try to push it down, but it does nothing for the aching desire in your belly."
                        "Being seen shouldn't cause such feelings!"
                        "Still..."
                        "A part of you hopes to see them again."
                    $ catcalltouching = True
                    jump events_end_period
                "Reject offer." if True:
                    show chelsea embarrassed
                    "A wave of embarrassment hits you as you remember your last encounter."
                    "If that's how you behaved sober, you'd hate to see how you behave around them drunk."
                    pcname "No thanks... I should really be getting home, actually."
                    "You expect the sort of violence you received from them before, but instead they all break off into disappointed groans."
                    "Steven" "C'mon, baby! Just one. It'll be a great time, we promise."
                    "You catch his eyes wander down your cleavage as he speaks."
                    "You're pretty sure you know why they want you to drink so badly."
                    pcname "No, really, I'm good. Thanks, though."
                    "You catch them spur a few insults your way as you turn back toward the crosswalk."
                    show chelsea blank
                    "Luckily, they don't follow you, but you can sense their irritation as you head home."
                    jump events_end_period
        "Ignore them." if True:
            "You have no intention of giving into them again."
            "Steve" "Yo! Tits! We're talking to you, fat ass!"
            "Yes, you stand by your decision to ignore them."
            "The crosswalk changes lights and you hurry across, wishing to be as far away from them as possible."
            jump events_end_period

label towncatcall7:
    show chelsea blank at right with moveinright
    "The next time you arrive to the bar, Nate's group is already there arguing with the bartender."
    "Nick" "What do you mean you won't let us in?!"
    "Nate" "C'mon, man, you can't do this to us!"
    "Bartender" "You're banned, buddy! Maybe next time don't take your dicks out in the bar!"
    "Steve" "My dick wasn't out!"
    "Bartender" "Get out of here, guys, before I call the cops!"
    "The bartender stands in front of the doorway, his arms crossed. Steve spits at his shoes and the others yell, but they begin to wander off."
    "Aaron gives you a small wave as you join them."
    show chelsea confused
    pcname "You're banned?"
    "Nate" "Yeah! Can you believe this shit?! We were just havin' some fun!"
    show chelsea blank
    "Steve" "Tch. Bet he never gets laid. That's why he's gotta ruin our fun."
    "You join the group as they wander through town, trying to find another source of entertainment for the night."
    pcname "Have you tried another bar?"
    "Aaron" "He's already called around and told the others about us. We got a ban around town."
    pcname "Oh."
    "Steve" "This shit sucks!"
    "Steve kicks a discarded soda can on the sidewalk. It flies into the air, smacking against the side of a building."
    "Aaron" "We could get drunk at the park."
    "The guys are disgruntled at the idea, but no one immediately argues with it."
    "Nate" "Nick, you get the beer-"
    "Nick" "Why do I have to get it?"
    "Nate" "Cause you have the money for it. I'm broke."
    "Nate turns his pockets inside out to emphasize his point."
    "Nick" "That shit don't matter to me. You get it. I'm not missing out this time."
    show chelsea embarrassed
    "As he speaks, Nick looks back down to your shorts, hinting at your last escapades in the bar. You blush slightly."
    "Nate" "Fine. Whatever. Give me your wallet."
    show chelsea blank
    "Nick turns over his wallet to Nate, and the blonde disappears a few blocks down. Nick and the others direct you to the park."
    "It's a decent size considering it's in the middle of the city. All of the children have gone home for the night, leaving the playground empty."
    "Aaron" "I used to love these as a kid."
    "Aaron jumps up and grabs one of the monkey bars, lifting himself into the air. He dangles a few inches from the ground."
    "Steve, much taller than his friend, doesn't need to jump at all. He simply grabs one of the bars as though it were a bus handle."
    "Steve" "Not as fun now."
    "Aaron" "No, not really."
    "Nick sits down on one of the swings and lights up a cigarette. He sways on the seat gently as the smoke billows out."
    "You sit down on the swing beside him, taking in your surroundings. It's been a long time since you got to enjoy a playground. Despite fond childhood memories, you feel out of place now."
    "Nate returns shortly after with a case of beer. He tosses Nick's wallet into his lap and divvies up the cans."
    "You crack yours open and take a long sip, letting the alcohol settle into your system. The men do the same, relaxing into place."
    "Nick watches you swing slightly on your seat, picking up a little bit of air as you kick your legs."
    "He stands up and makes his way behind you, dropping his cigarette into the mulch beneath him. You half expect him to push, but his hands grab your breasts from behind, immediately halting your pace."
    show chelsea shocked
    "Nick" "Damn. You were right, Nate. These are nice."
    "Nate grins from his spot on the grass, his body stretched out."
    "Nate" "I told you."
    show chelsea embarrassed
    "Nick lifts the shirt up over your head, tossing the fabric down onto the mulch. A chill runs across your body at the sudden exposure to the night air, but Nick's hands are on your breasts again, warming them up as he squishes and gropes them."
    "You tilt your head back a little, enjoying the sensation of his warm hands against your cold body. He unhooks your bra and tosses it with your shirt."
    "The night breeze plays against your breasts, and your nipples harden, eager and excited."
    "Nick reaches over your shoulder, bringing his mouth down on one of your nipples. You close your eyes and let out a soft, satisfied noise at the contact."
    hide chelsea with dissolve
    show bg NPark1 with dissolve
    "A hand strokes up your thigh and underneath unbuttons your shorts, pulling them down. You assume it to be Nick until the fingers shove your panties to the side and plunge into you. You open your eyes and find Aaron on his knees, one hand on your knee while the other toys inside of you."
    "Aaron" "Does that get you hot? All of us watching you?"
    if club == "track":
        "You glance between the men, taking in their lustful stares. Your voice comes out hot and breathy."
        pcname "You tell me."
    elif club == "cheer":
        "You jut your hips a little closer in Aaron's direction, a smile playing on your lips. The men watch eagerly as you lick your lips and let out a pleased sigh."
        pcname "I {i}love{/i} it."
    elif club == "yearbook":
        "You flush, avoiding his gaze. That's enough of an answer to satisfy him."
    "You can't deny how wet your panties were when he pushed them to the side, nor the excitement you feel as their eyes watch your every reaction, whimper, and moan."
    "Aaron's fingers slip in and out of you with ease as Nick's mouth assaults your breasts, one hand circulating between the other to give both equal attention."
    "This time, it's Steve and Nate that are unbuckling their pants, each grabbing their cocks eagerly as you thrust into Aaron's hand."
    "Aaron pulls his fingers out, but before you can fully show your disappointment, he yanks down your panties, giving the men a better view."
    "You're suddenly aware at how exposed you are in the public view of the park. There is a man walking his dog not too far off, as well as a homeless man sleeping away on a park bench. You can't help but wonder what they would do if they saw you in this compromising position."
    "Aaron dips his head forward, tracing his tongue in small circles against your thigh. Your breath shudders as he moves it closer and closer between your legs."
    "His lips find your clitoris and he sucks. You let out a strangled gasp, grasping his hair."
    "Nick" "Shit."
    "Nick lifts his head from your breasts to watch Aaron play with your clitoris, his tongue lapping against the swollen nub until he lowers his lips and plunges it into you."
    "You let out a cry, thrusting against his face. Aaron grabs your thighs with a strength you didn't expect from him, holding your legs steady over his shoulders as he licks deep inside of you."
    "Nick stands up fully and grips your face, forcing you to look at him. He unbuckles his pants, springing his cock from the tight fabric."
    "You allow him to shove himself into your mouth, gripping your hair to pull you as deeply as he can."
    if corruption >= 20:
        "Nick" "Oh, fuck."
        "He doesn't expect you to take him down your throat, your moans vibrating against his throbbing cock."
        "He thrusts into your mouth eagerly. You relish in the pleasure of his balls slapping your chin as Aaron continues to eat you out, this thumb rubbing your clit."
    elif True:
        "Nick" "Ah..."
        "Nick sighs as you struggle to take the entirety of his cock in your mouth. You get about halfway, but try to make up for it by focusing on his head, bouncing your lips against his deep thrusts."
        "He grinds against your face, moaning as you take him in. Aaron continues to pleasure you from below, his thumb reaching up to rub against your clit."
    "Nate and Steve breath heavily nearby, thrusting their cocks into their hands as they watch you with their friends."
    "Aaron eventually pulls his head back, gasping for air. You moan around Nick's cock in disappointment, your hips thrusting in Aaron's direction."
    "Aaron" "Switch."
    "Nick pulls out of your mouth with a {i}pop{/i}, and the men switch sides, Aaron standing over you while Nick kneels down in the mulch."
    show bg NPark2 with dissolve
    "You keep finding yourself surprised by Aaron, including the girth of his cock as he releases it from his pants."
    if corruption >= 20:
        "You eagerly take him entirely into your mouth, pulling him further until he's thrusting against the back of your throat."
        "Aaron" "Fuck! [pcname]..."
        "Aaron grabs your hair, fucking your mouth with a newfound eagerness."
    elif True:
        "You take Aaron into your mouth as much as you're able to, focusing your attention on his tip with long strides of your tongue."
        "He grunts and moans against you, thrusting as deeply as you will allow."
    "Nick is far rougher in eating you out than Aaron had been. Three fingers plunge into you without hesitation, his mouth nipping and sucking at your clitoris."
    "You cry out at his movements, the noise muffled around Aaron's dick. You can hear the soft grunts and moans from Steve and Nate as they rub themselves off beside you."
    "Nick releases his fingers from you shortly after, using the cum to rub himself off as he shoves his face against your vagina. His tongue laps against your folds eagerly, darting in and out of you with a ferocity you can't keep up with."
    "Your legs shake as you feel your body begin to beg for release. You tighten your legs around Nick's shoulders, squeezing his head between your thighs. He doesn't stop you, further violently rubbing your clit as his tongue pierces in and out of you."
    "Aaron's cock quivers in your mouth, his release coming."
    "Nate finishes first, letting out a soft cry nearby, shortly followed by Steve's grunts as he cums into his hand."
    "You let out a series of gasps around Aaron's cock as you rise slightly from the swing, involuntarily thrusting against Nick's face as you cum."
    "Aaron groans, pulling out only to cum against your chin, the white liquid dripping onto the swing."
    "Nick is last, using your discarded shirt on the ground to finish the job. He jerks into the fabric, splattering it with his fluids."
    "There are a few moments of silence as you all come down from your high, panting and quivering post-release."
    show bg black with dissolve
    "Surely someone must have heard you. Surely, you're about to get into trouble, just as you had at the bar. None of you had bothered to keep quiet as you came, and you wait with baited breath for the result of your antics."
    "Nothing happens. No one shows up to arrest you, or to even scold you for your behavior. You remain sitting naked on the swing, goosebumps rising on your arms as you realize just how cold it is outside."
    "Nick tosses your shirt back at you from the ground."
    "Nick" "Thanks."
    "The shirt is useless with his cum all over it. You drop it back onto the ground, quickly gathering your clothes and dressing yourself."
    "You all drink at the park for a little bit longer, musing over more childhood stories before you decide it's time to return home."
    if damienrelate == "dating":
        "As you depart from the men, your mind wanders to Damien, and a feeling of guilt presses down in you."
        "There's no way he would approve of what you've just done with these men."
        "Hell, he probably thinks you've never kissed another person."
        "You bite your lip, vowing to keep this night a secret. What he doesn't know won't hurt him."
        "And it was such a good night, too."
    if mattchain > 1:
        "As you depart from the men, your mind wanders to Matt. What would he make of this entire escapade?"
        if defymatt == True:
            "Wait, why should you care?"
            "You bite your lip, angry that you had even dared to consider how he would feel. What do his feelings matter?"
            "They don't. You raise your head, feeling a little more proud of your defiance."
        elif True:
            "You can already imagine the string of insults he would give you. 'Slut', 'Whore', 'Skank'..."
            "Somehow, it isn't as fun when you imagine him genuinely angry."
    if violetrelate == "Sub":
        "As you depart from the men, your mind wanders back to Violet, waiting dutifully to do whatever she told you to."
        "Would she involve herself in something like this if you told her to?"
        "Part of you muses over the idea of seeing her take on so many men at once as a sort of punishment for her disobeying you."
        "The other part feels guilty for doing something like this without telling her."
        "You shake your head, trying to rid yourself of the thoughts. It doesn't matter. You're in control here. You can do whatever you want."
    if violetrelate == "Dom":
        "As you depart from the men, your mind wanders back to Violet, and guilt rises up in you."
        "You had agreed to let her control you, and you had not asked permission to do something so scandalous. What would she think?"
        "Would she be angrier that you did it without her permission, or that you hadn't included her at all?"
        "You bite your lip, trying to toss the thoughts out. You just need to make sure she doesn't find out."
    "You walk back in your bra, leaving the shirt behind."
    $ catcalloral = True
    jump events_end_period

label towncatcall8:
    show black
    "With the ban at the bar in place, you have not seen Nate and his group since your eventful night on the playground."
    hide black with fade
    show chelsea with dissolve
    "You aren't sure whether to feel relieved or upset about this. The memory at the park fills you with shame and embarrassment, but..."
    show chelsea happy
    "Oh, god, it was fun."
    show chelsea blank
    "As you make your way down the street, you spot Aaron standing outside an arcade, checking his phone."
    "You expect him to ignore you in broad daylight, but he smiles as you approach, waving you over."
    "Aaron" "Hey. Long time no see."
    pcname "Hey."
    pcname "Are you hanging out with your friends today?"
    "Aaron" "Oh, no. I'm picking up my brother."
    "Aaron gestures inside the arcade. Several middle schoolers jump between the gaming systems, nearly throwing each other out of the way to switch."
    "Aaron sighs."
    "Aaron" "He was supposed to be out ten minutes ago."
    pcname "Oh. Sorry about that."
    "Aaron shrugs."
    "Aaron" "It's whatever. He always does this."
    "Aaron" "But, hey, I'm glad I ran into you. I have something to give you."
    "You watch curiously as Aaron reaches into his bag, pulling out a piece of fabric. When he hands it to you, you recognize it's your shirt."
    "Aaron" "You left it at the park last time. Thought you might want it."
    show chelsea happy
    pcname "Oh! Ah, thank you."
    "You turn the shirt over, nearly having forgotten about it."
    show chelsea blank
    "Aaron" "Don't worry, I washed it. It should be good to go."
    show chelsea happy
    pcname "Thanks."
    show chelsea blank
    "You tuck the shirt into your bag. A short, black-haired boy lolls out of the arcade, disappointed."
    "Aaron" "You ready to go?"
    "Boy" "Yeah... I guess..."
    "Aaron" "Alright. Oh, wait a second."
    "Aaron pulls out a small notepad and pen from his bag, scribbling something down in messy handwriting. He passes it to you: his cellphone number."
    "Aaron" "Call me next time you wanna hang out again. I'll see you later, [pcname]."
    show chelsea happy
    pcname "Yeah, see you. Thanks again!"
    "Aaron waves goodbye as he leads his brother away toward his car. You hear his brother ask a question about you, but you can't quite tell what it was."
    show chelsea blank
    "You glance down at the paper before tucking it into your pocket. Maybe it'll come in handy."
    scene bg black with dissolve
    pause 0.5
    "You've reached the end of the Nate & Co Side Story in this version! Keep and eye out for more content!"
    jump events_end_period

label farmersmarket:
    show chelsea blank at right with moveinright
    "As you pass by a church, a savory aroma catches your attention."
    "You glance over and find a farmer's market set up in the parking lot!"
    show bg FarmersMarket with dissolve
    "Large tables and wooden stalls take space across the asphalt, colorful poster boards listening out produce and their prices by the varying sellers."
    "Would you like to explore?"
    menu farmersmarketexplore:
        "Yes." if True:
            "You step into the farmer's market, almost overwhelmed by the sheer amount of sharpie-written signs and freshly picked produce."
            "Sellers of all ages call out to you and other passerby's, offering free samples of baked goods and special sales on in-season vegetables."
            "You stop by an elderly woman's stand, admiring the shiny array of apples spread out in thick baskets across the table."
            "Apple Granny" "Would you like a free sample, dear?"
            "She holds out a tray of homemade applesauce in little white cups."
            menu farmersmarketsample:
                "Yes." if True:
                    show chelsea happy at right with moveinright
                    "You gratefully take one of the cups and a plastic spoon before pooling it into your mouth. Delicious!"
                "No." if True:
                    pcname "Oh, no thank you."
                    "The old woman smiles and sets her free sample tray down."
            "You lean on the table to get a better look at the produce. As you place your weight on the edge, the leg snaps!"
            show chelsea shocked
            "The table collapses. Baskets upon baskets of apples tumble off of the table, rolling out into the parking lot."
            "Some patrons don't notice and nearly trip themselves over the sudden outpour of apples, fumbling to keep their balance."
            "The old woman gasps, immediately rushing out to gather her apples."
            show chelsea sad
            "You run out to help her, trying to gather as many as you can. Unfortunately, several have rolled away, and some of the baskets have broken on their tumble to the ground."
            "After you and the woman have finished salvaging as many apples as you can, it is clear that most of her produce has been lost."
            pcname "I'm so sorry..."
            "Apple Granny" "It's not your fault, dear. It was an old table..."
            "Even if it wasn't technically your fault, you feel horribly embarrassed and guilty about the entire ordeal."
            "By the dirty look she gives you, you're sure she partially blames you anyway."
            menu farmersmarketdamages:
                "Offer to pay for damages" if True:
                    pcname "I can pay for the damages..."
                    "Apple Granny" "That would be helpful."
                    "The old woman grabs a calculator from under the table and jots some numbers down."
                    "She writes it down on a slip of paper and passes it to you."
                    show chelsea shocked
                    pcname "$150?!"
                    "Apple Granny" "And that's being generous, dear."
                    show chelsea blank
                    "She eyes the bruised apples she had to throw out, in addition to the squished ones still scattered on the street."
                    if Cash > 150:
                        $ Cash -=150
                        "Miserably, you dig in your wallet and hand over the cash. She double counts it, smiling to herself."
                        "Apple Granny" "Thank you for doing business, dear."
                        pcname "Yeah..."
                        "You place your wallet back in your pocket and shuffle off. Damn those apples!"
                        $ grannypaid = True
                        $ marketscenes += 1
                        jump events_end_period
                    elif True:
                        "You dig into your wallet. A knot forms in your stomach at the realization of your situation."
                        show chelsea embarrassed
                        pcname "I don't have that kind of money..."
                        "Apple Granny" "Hmph! Well, how do you plan to make up for it then?"
                        pcname "Uh..."
                        "You rack your brain, trying to figure out how to help her out."
                        pcname "I can help you run shop next time. I can work it off."
                        "Apple Granny" "And let you near my goods again? No thank you, missy."
                        "Apple Granny" "Just go. I don't want to see you around my stand again."
                        show chelsea sad
                        pcname "I'm sorry..."
                        "You awkwardly shuffle off back through the market, trying to avoid the dirty glares nearby shop owners give you."
                        $ marketscenes += 1
                        jump events_end_period
                "Apologize Again." if True:
                    pcname "I'm sorry again..."
                    "She glares after you as you awkwardly walk away from the booth, hoping she won't cause a scene."
                    "After a little bit of exploring, you find that you're unable to enjoy the farmer's market today."
                    "Maybe you'll try again another day."
                    $ marketscenes += 1
                    jump events_end_period
        "No." if True:
            "You don't have any need for produce at the moment."
            "You carry on through the city."
            jump events_end_period

label farmersmarket2:
    show chelsea blank
    "As you pass by the church, a savory aroma catches your attention."
    show bg FarmersMarket with dissolve
    "The farmer's market is back in the parking lot!"
    "Would you like to explore?"
    menu farmersmarketexplore2:
        "Yes." if True:
            "You head into the farmer's market and peer around at the stalls."
            "As you head further into the market, you see the apple stand from last time."
            "The elderly woman shuffles between customers, greeting them with free samples of her applesauce."
            "Her business is booming."
            "You awkwardly try to avoid the booth, recalling the trouble you had caused there last time."
            "You take a turn in the parking lot and find a large booth covered in bananas. They dangle from the structure's ceiling and off of the table, overflowing from wooden crates and branching out on all sides."
            "An elderly woman in a bright yellow hat greets customers at her booth with a plate of fresh banana bread."
            "This booth is even busier than the apple lady's!"
            "You squeeze between eager customers, trying to get a better look."
            "Along with bananas, several loaves of banana-baked goods cover the table. Banana bread, banana pudding, banana {i}vodka{/i}..."
            "It smells as though you've entered a tropical paradise."
            "The woman in the yellow hat hurries to greet you, offering out her plate of bread."
            "Banana Woman" "Would you like a free sample, sugar?"
            menu farmersmarketbananabread:
                "Yes." if True:
                    show chelsea happy
                    "You accept one of the pieces, plopping it into your mouth."
                    "You're surprised to find that it's still warm. The bread melts against your mouth, filling your taste buds with a sweet banana taste."
                    "Yum!"
                "No." if True:
                    "The woman looks a little put off, but smiles politely at you before hurrying to the next customer with her tray."
            "You admire the array of banana treats on the table, eyeing over each one in delight."
            "As you pick up one of the bunches of bananas from the edge of the table, you gently bump the wooden poll holding up the roof structure."
            show chelsea shocked
            "It slides right off of the table, and the top beam falls harshly onto its side, crashing against the table."
            show chelsea confused
            "You feel a sense of Deja vu as the bananas come tumbling down from the structure, flopping and rolling across the ground."
            "Unsuspecting customers walk over them, squishing the bananas under their feet."
            "Dread fills your stomach as you slowly turn back toward the stall's owner."
            "She glares harshly down at you, her arms crossed indignantly."
            "Banana Woman" "You're going to have to pay for that!"
            menu farmersmarketdamages1:
                "Offer to pay for damages." if True:
                    show chelsea sad
                    pcname "Of course! I'm so sorry. How much will it be?"
                    "The woman grabs her calculator and a notebook, marking down her inventory. You shift awkwardly in place, trying to avoid the pitiful glances of customers as they pass by."
                    "She writes down a number on the paper and holds it out to you."
                    show chelsea shocked
                    pcname "$200?!"
                    "Banana Woman" "And that's being generous! You're lucky I don't make you pay for the booth!"
                    show chelsea blank
                    "She points her cane at the fallen roof structure."
                    if grannypaid == True:
                        "You glance at the bananas on the ground and think of the apples you'd paid for. You certainly spilled more at the last booth, but it wasn't nearly this much."
                    elif True:
                        "You glance at the bananas on the ground. They seem to smile mockingly back up at you."
                        "Well, at least the ones that aren't squished."
                        pcname "Stupid bananas..."
                    if Cash > 200:
                        $ Cash -=200
                        "You take out your wallet, trying to keep yourself remorseful as you pass the money into her hand."
                        "She snatches it from your grasp and gives you a warm smile."
                        "Banana Lady" "Come back again, you hear?"
                        "You nod, planning to never step near her booth again."
                        "As you walk out of the farmer's market, you catch a glimpse of the elderly woman at the apple booth."
                        "She glares harshly up at the banana lady, a look of pure hatred on her wrinkled face."
                        "In this moment, you can't blame her."
                        "You walk away from the farmer's market."
                        $ marketscenes += 1
                        jump events_end_period
                    elif True:
                        show chelsea sad
                        "You take out your wallet and frown at the small amount of bills inside of it. This isn't nearly enough..."
                        pcname "I'm sorry, but I don't have that kind of money."
                        "The woman looks outraged."
                        "Banana Lady" "Then how do you expect to make up for this?!"
                        "She gestures toward the top of her booth. The occasional banana still breaks off and collapses to the ground."
                        pcname "I can, um, maybe work it off?"
                        "Banana Lady" "And let you near my produce? Absolutely not! Scram, child! Don't let me catch you near my goods again, or I'll call the cops, y'hear?"
                        "You nod vigilantly, quickly making your way out of the farmer's market."
                        "As you leave, you catch a glimpse of the woman at the apple booth."
                        "She glares up at the banana lady with a look of pure hatred on her wrinkled face."
                        "Whatever is going on between them, you want no part of it."
                        "You hurry out of the market."
                        $ marketscenes += 1
                        jump events_end_period
                "Apologize again." if True:
                    show chelsea sad
                    pcname "I'm really, really sorry."
                    "Banana Lady" "Sorry isn't going to fix this!"
                    "She gestures angrily at her booth. You glance awkwardly to the side, not sure how else to really make it up to her."
                    "You help pick up a couple of good bananas that fell and place them back on the table. You also lean the pillar back up against the booth, as though that'll make up for it."
                    "She glares at you the entire time, furious. You bow in apology, making a quit exit."
                    "As you leave the farmer's market, you catch a glimpse of the woman at the apple booth."
                    "She gives the banana lady a look of pure hatred, gritting her dentures together."
                    "Whatever is happening between them, you want no part of it."
                    "You hurry out of the market."
                    $ marketscenes += 1
                    jump events_end_period
        "No." if True:
            "There's a reason grocery stores exist."
            "You continue your way down the sidewalk."
            jump events_end_period

label farmersmarket3:
    show chelsea blank at right with moveinright
    "While walking by the church, the sweet smell of fresh fruit catches your attention."
    show bg FarmersMarket with dissolve
    "The farmer's market is back!"
    "Would you like to explore?"
    menu farmersmarketexplore3:
        "Yes." if True:
            "You enter the farmer's market, a little more cautious than usual."
            "You've already ruined two booths- you want to avoid any more ire from old ladies if you can help it."
            "As you pass by, the elderly woman at the apple booth catches your attention."
            "Her booth is all but abandoned, despite the invitingly ripe fruit on her table."
            "She shuffles side to side, casting glares at the banana booth not too far away."
            "The banana lady's booth is booming, surrounded by excited customers. Her booth is practically invisible behind the crowd."
            "Despite yourself, you really do want some apples."
            "You approach the apple booth cautiously."
            if grannypaid == True:
                "She smiles, almost relieved, at your approach."
                "Apple Granny" "Welcome back, dear. What can I do for you?"
            elif True:
                "She eyes you over scornfully, as though your presence is dreaded."
                "Apple Granny" "Come to wreck my booth again, dear?"
                if club == "track":
                    pcname "No, not today."
                elif club == "cheer":
                    pcname "No, not in my plans today."
                elif club == "yearbook":
                    pcname "N-No..."
                "Apple Granny" "Well, then what can I do for you?"
            pcname "I was just looking."
            if grannypaid == True:
                "Apple Granny" "Look for as long as you like, dear. Free sample?"
                "She offers up the plate of applesauce."
                pcname "No thank you, I'm good."
            elif True:
                "Apple Granny" "Hmph. I might need to start charging for looking."
                "She grumbles under her breath, but focuses on reorganizing her stock, trying to keep busy."
            "You're too afraid to touch anything, lest the booth come crashing down again. She seems to notice your hesitance, watching you carefully."
            "Deciding against it, you give a little wave."
            pcname "I think I'm good, thank you."
            "As you turn to leave, your toe catches the edge of the table."
            "Apples tumble as the table comes crashing down."
            "This time your reflexes are a little better, and you hurry out to catch the edge of the table as it falls."
            "This does not save the crates of apples that have crashed on the ground, however. They roll across the parking lot, bruising and scratching against the asphalt."
            "You fumble with the table's leg, snapping it back in place underneath. It feels unstable, but at least it's standing again."
            "When you look up at the woman, you're shocked to catch a glimpse of giddy relief on her face."
            "It quickly falls into anger when she catches your gaze, her eyebrows pushed together."
            "Apple Granny" "Again! Really?!"
            show chelsea sad
            pcname "Sorry about that..."
            "She huffs, pulling out her calculator."
            "Apple Granny" "That'll be $300."
            show chelsea shocked
            pcname "$300?!"
            "You glance back at the apples on the ground. This isn't {i}nearly{/i} as much as the disaster you'd created the first time."
            show chelsea confused
            pcname "How is this $300?"
            "Apple Granny" "I added an emotional support tax."
            "She shows you the calculator."
            show chelsea blank
            "You think back to the events at her stall last time as well as the banana booth. Something isn't adding up here."
            "Still, you don't want to just not pay for her damages..."
            show chelsea confused
            pcname "Can I work it off? Next time the farmer's market is going on, I'll come by and work for you."
            "She considers it, although this is obviously not the result she was hoping for."
            show chelsea blank
            "Apple Granny" "How do I know you'll show up? I can't just take your word for it."
            "You consider this. It's a fair point."
            "Apple Granny" "Give me your name and address. If you don't show up, I'll call the police."
            show chelsea shocked
            "You're taken aback. This is pretty drastic, isn't it?"
            show chelsea blank
            "Still, you offered..."
            pcname "Alright."
            "You write down your name and address on the notepad she offers you. She makes a motion for you to wait as she fills out another piece of paper before passing it back."
            "It's a contract."
            "Apple Granny" "Just for my records."
            pcname "Okay..."
            "You sign your name at the bottom. She snatches up the paper, tucking it safely in her register."
            "Apple Granny" "I expect to see you first thing tomorrow."
            pcname "I'll be there."
            "She holds out her frail, wrinkled hand."
            "Apple Granny" "Dorothy."
            "You shake it."
            pcname "[pcname]."
            "Dorothy" "Nice doing business with you, dear."
            "You nod, hurrying out of the market."
            $ grannywork = True
            jump events_end_period
        "No." if True:
            "Fruit is for the weak. You are not weak."
            "You continue your way down the sidewalk."
            jump events_end_period

label farmersmarket4:
    show chelsea blank at right with moveinright
    "Although you promised to help Dorothy with her apple booth, you're feeling a sense of regret as your eyelids droop tiredly on your walk to the church parking lot."
    show bg FarmersMarket with dissolve
    "Several farmers and gardeners have begun to set up their booths for the day, plastering on poster board signs and setting up their produce on the tables."
    "You feel a bit of pity for Dorothy as you watch her struggle to put up the table by herself."
    pcname "I can help with that."
    "You reach down to grab the other end of the table's legs."
    "Dorothy" "No, no! You go grab the apples. Start putting them in their crates. Don't bruise them!"
    "You're momentarily shocked by her insistance against help, but you shrug, walking to the back of her truck."
    "The back is open, displaying several wooden crates filled with apples and jars of applesauce."
    "You grab a set of decorative crates from the side of the truck and spread them out on the ground, carefully filling them up with the ripest looking apples."
    "Once they're filled, you glance over at Dorothy. The table is up, and she is spreading a red tablecloth over it."
    "Dorothy" "Oh, you're finished. Come line them up here."
    "She points at specific spots on the table, adjusting them when you evidently don't place them precisely right."
    "As the both of you finish setting up for the day, you glance over at the banana lady as she sets up her own booth."
    "You notice her nudge the pillar holding up the roof structure to the edge, nearly enough to topple over."
    menu farmersmarketcomment:
        "Comment." if True:
            pcname "That's going to fall."
            "Dorothy" "What is?"
            "Dorothy looks over at the booth. She snorts."
            "Dorothy" "Bertha's always pulling that trick. When she's too busy, someone will nudge it over the edge and owe her payment for damages."
            "That sounds familiar."
            pcname "That's a very shady thing to do."
            "Dorothy" "It's a clever business strategy."
            pcname "Is that what you do?"
            "Dorothy" "Does it look like I have a roof here?"
            "She gestures to the lack thereof. You shrug, not entirely convinced, but continue helping her set up for the day."
        "Stay quiet." if True:
            "You're sure that it's going to fall over, but that's none of your business."
            "You finish helping Dorothy set up for the day, making sure the display as perfect."
    "The customers trickle in through the early morning, browsing with leisure, but as the afternoon settles in, the place is packed."
    "You're sanctioned to free sample duty for the day, offering small tastes of homemade applesauce. The booth does relatively well."
    "At one point during the afternoon, you glance over at Bertha's booth. True enough, the pillar has fallen, and she yells at some poor defenseless couple."
    "A few of her booth neighbors grumble and roll their eyes. This must be a common occurrence."
    "You feel irritation rise in you. You had been the victim to her stunt last time, and you feel an urge to run up and defend the couple."
    show chelsea shocked
    "Dorothy" "[pcname]! Stop daydreaming and work!"
    show chelsea blank
    "You force yourself to look away from the display and offer a nearby customer their free sample."
    "When you look back up, the couple has clearly paid the satisfied Bertha, ashamedly making their way out of the farmer's market."
    "After the farmer's market ends, you help Dorothy pack up as she counts her money."
    "Dorothy" "We did better than usual! I might need to keep you on."
    "She laughs, slamming the register box closed."
    "Dorothy" "I'll see you again soon. Bright and early, same as last time."
    "You nod and take your leave."
    $ marketscenes +=1
    $ grannywork = False
    jump events_end_period

label townfakeid:
    show chelsea blank at right with moveinright
    "As you cross through a shadier area of town, you see a giggling group of girls approach a nearby bar."
    "You know for a fact they're underage, but as they flash their ID's at the bouncer, he lets them in."
    "You watch for a moment, surprised."
    "You're about to leave, but you catch another girl running toward her companions, trying to catch up."
    menu fakeidapproach:
        "Approach her." if True:
            "You hesitantly approach the girl, waving her over. She looks at you, confused, but steps aside."
            "ID Girl" "Can I help you?"
            if club == "track":
                pcname "Yeah. Sorry, this'll be quick. I just wanted to know, how old are you?"
            elif club == "cheer":
                pcname "I just need to ask you something. How old are you, exactly?"
            elif club == "yearbook":
                pcname "Um, yeah. This is going to sound kind of awkward but..."
                pcname "How old are you?"
            "The girl gives you a wary look."
            "ID Girl" "What? Are you a cop?"
            if club == "track":
                show chelsea shocked
                pcname "What? No! Of course not."
                show chelsea blank
                pcname "I saw these other girls going in, but they can't be old enough."
            elif club == "cheer":
                pcname "Oh, no. I'm not a cop."
                pcname "But I saw those girls with fake ID's. I was thinking you had one, too."
            elif club == "yearbook":
                show chelsea shocked
                pcname "No! No. I just saw the other girls get in, and they can't be old enough, so..."
                show chelsea blank
            "The girl looks you over skeptically. Then, deciding you're safe, she pulls out her ID and holds it out to you."
            "ID Girl" "Well, yeah. It's a fake. Why? Were you interested in buying one?"
            "ID Girl" "My cousin makes 'em. He could hook you up."
            menu buyfakeid:
                "Yes." if Cash >= 20:
                    "ID Girl" "Cool. Here, let me give you his address."
                    "You both take out your phones. She places his address into your map app. He's only a block away."
                    "ID Girl" "His name is Eddie. He runs a print shop, but he also does fake ID's. Just tell him Lucy sent you."
                    "She quickly tucks her ID into her wallet and returns to the bar. The bouncer lets her in."
                    "You look down at your map."
                    "You didn't have anything else planned for the day..."
                    "You follow her directions down the block, stopping outside of \"MEME-SHOT\". Memes on t-shirts, mugs, and other items cover the store front."
                    "You step inside, looking around."
                    "A middle-aged man with curly black hair looks up from the counter. His nametag reads: EDDIE."
                    "Eddie" "Welcome! How can I help ya today?"
                    pcname "I was here to get an ID. Lucy sent me."
                    "Eddie surveys you, nodding. He waves you on over to a back room. You hesitate, but follow."
                    "There's a grey-painted wall and a steel chair pressed up against it. Across is a camera, hooked up to a computer and printer."
                    "Eddie" "Right over there."
                    show chelsea happy
                    "You take your seat, smiling as he snaps the photo."
                    show chelsea blank
                    "It takes a couple of minutes, but Eddie returns and passes the card over to you."
                    "It looks pretty genuine, at least you think so, but you've never actually seen a fake ID before."
                    "Eddie" "That'll be $20."
                    pcname "Right."
                    "You reach into your wallet, passing him the money."
                    "Eddie" "Nice doing business."
                    "You nod, stepping back out into the city."
                    $ Cash -= 20
                    $ fakeid = 2
                    $ fakerid+=1
                    jump events_end_period
                "No." if True:
                    "ID Girl" "Oh."
                    "She quickly tucks the ID into her wallet, turning away."
                    "ID Girl" "Keep your mouth shut about it then, alright?"
                    "She approaches the bar, flashing her fake ID. The bouncer lets her in."
                    "You turn away, continuing down the street."
                    jump events_end_period
        "Walk away." if True:
            "It's none of your business, and you aren't really interested in getting involved."
            "You continue down the street."
            jump events_end_period

label stripclub:
    show chelsea at right with moveinright
    if stripclubcount > 0:
        "It's a little late out. You look around the city streets on your stroll, searching to find some sort of entertainment."
        "Once again, you see the advertisement for \"CLUB 22\"."
        "The half-naked man and woman stare down at you, beckoning you to join them."
        "Maybe you could check it out?"
    elif True:
        "It's a little late out. You look around the city streets on your stroll, searching to find some sort of entertainment."
        "A large billboard sits above a pizza joint, advertising a nearby strip club: \"CLUB 22\"."
        "A picture of a half-naked man and a half-naked woman give you sultry looks from the sign, stripping out of their undergarments."
        "As you take a turn down the street, you see the club in its natural, shady glory. The windows are tinted black, but neon magenta signs advertise special deals and dancers for the night."
        "Would you like to go in?"
        $ stripclubcount +=1
    menu stripclubenter:
        "Yes." if True:
            $ stripclubvisit = True
            if club == "track":
                "You've always been curious if the strip clubs in movies resembled anything like the real thing. Why not find out?"
            elif club == "cheer":
                show chelsea happy
                "You smirk in delight at the sight, excitement twisting in your stomach."
                "It would be silly to deny your desires, after all."
            elif club == "yearbook":
                show chelsea embarrassed
                "Your face flushes in embarrassment as you gather the courage to approach the building, let alone go inside."
                "You feel an excitement twist your stomach, urging you to go inside."
                "It'll only be to sate your curiosity, or so you tell yourself."
            "As you open the front door, you find yourself in a small box of an entryway, the only way in through thick curtains hung over the doorway."
            "You hear the revelry of the party raging inside."
            "A bouncer greets you, holding out his hand before you can step further inside."
            show chelsea blank
            "Bouncer" "Hey. ID."
            "He holds out his hand. You fumble in your wallet and present your ID to him."
            "He looks it over before shaking his head and handing it back to you."
            "Bouncer" "Sorry, kid. You're too young."
            show chelsea confused
            pcname "But I'm an adult."
            "He points to another sign marked on the entryway's wall."
            show chelsea blank
            "Bouncer" "Sorry, kid. It's twenty-one and over. Policy 'n all."
            $ fakerid += 1
            if club == "track":
                "You huff in annoyance, shoving your wallet back into your bag."
                pcname "I'm not even going to drink."
                "He shrugs, making no attempt to move. You scoff, stomping out into the street."
                "It's not like you were going there to get drunk."
                "You walk home, irritated."
                jump events_end_period
            elif club == "cheer":
                "You glare up at him, pursing your lips."
                pcname "I'm not going to do anything."
                "Bouncer" "I'm sure you're not. Sorry."
                "You stand there for a moment longer, debating. You sigh, tossing your wallet in your back and exciting out into the street."
                "Whatever. You can just look up naked men and women on the internet whenever you want."
                "Still, the rule irritates you as you walk home."
                jump events_end_period
            elif club == "yearbook":
                show chelsea embarrassed
                "You frown, but shakily place your wallet back in your bag. You feel your face flush in embarrassment, unable to look him in the eye."
                pcname "I-I'm sorry for bothering you."
                "Bouncer" "No problem. See you in a couple of years."
                "You hurry out of the strip club, your heart hammering in your chest all the way home."
                jump events_end_period
        "No." if True:
            "You consider it briefly but shrug it off. You can just look up images on the internet."
            "You walk past it, continuing through the city."
            jump events_end_period

label stripclub2:
    show chelsea blank
    "It's a little late out. You look around the city streets on your stroll, searching to find some sort of entertainment."
    "You see the large billboard for \"CLUB 22\" above the pizza joint and consider it for a moment."
    "You were turned away last time because of your ID, but this time you came prepared."
    if fakeid == 2:
        "You paw at the fake ID in your wallet, something you had ordered specifically for this."
    "You feel desire curl in your stomach at the sight of the half-naked people on the sign."
    "Hopefully you get a different bouncer."
    "As you take a turn down the street, you see the club in its natural, shady glory. A new list of dancers flashes in neon magenta lights."
    "Would you like to enter?"
    menu stripclubenter1:
        "Yes." if True:
            if club == "track":
                "It can't hurt to try, at least."
            elif club == "cheer":
                "Your look over the building, desire building inside of you. Just a peek would even be enough."
            elif club == "yearbook":
                "You hope that another bouncer is working. You can't imagine facing the same embarrassment as last time...!"
            "You push the door open, entering the familiar entryway."
            "Against your luck, the same bouncer as last time stands in your way, his large hand held out to block you from entering the party inside."
            "Bouncer" "Hey. ID."
            "You reach in your bag."
            menu stripclubID:
                "Give him the fake ID." if fakeid == 2:
                    $ fakerid+=1
                    $ corruption +=1
                    "You grab the small card from the back of your wallet, hurriedly passing it over to him."
                    "The bouncer looks it over. You hope he won't look it over too closely."
                    "He narrows his eyes at it, glancing between you and the card."
                    "Bouncer" "This is a fake."
                    if club == "track":
                        pcname "Are you sure? Pretty sure it's real."
                    elif club == "cheer":
                        "You take a step closer, twirling a piece of your hair between your fingers."
                        pcname "It doesn't have to be if you let me in."
                    elif club == "yearbook":
                        pcname "I-Is it?"
                        "You twist your hands together anxiously."
                    "The bouncer shakes his head, not buying it."
                    "Bouncer" "Sorry, kid. I'm confiscating this."
                    "He tucks the fake ID into his pocket."
                    if club == "track":
                        "You glare up at him, your hand sliding down to your hip."
                        pcname "Are you serious? C'mon, man."
                    elif club == "cheer":
                        "You pout up at him, crossing your arms firmly."
                        pcname "Can't you make one exception?"
                    elif club == "yearbook":
                        show chelsea sad
                        "Your eyebrows crease in worry."
                        pcname "You aren't going to call the police, are you...?"
                        "Bouncer" "No, but you gotta go."
                    show chelsea blank
                    "He shakes his head, tapping the 21+ sign."
                    if club == "track":
                        "You scoff, casting him a dirty look before you exit out to the street."
                    elif club == "cheer":
                        pcname "Hmph!"
                        "You turn abruptly, your hair whipping behind you as you step out into the street."
                    elif club == "yearbook":
                        show chelsea sad
                        "You frown, but walk out into the street, holding your bag closely over your shoulder."
                    "Even though you should be grateful he didn't call the cops, you can't help but feel annoyed at the silly rule."
                    jump events_end_period
                "Give him your real ID." if True:
                    if fakeid == 2:
                        "You reach in your wallet, considering the fake ID in the back."
                        "But you pass it over and hand him your real ID."
                    elif True:
                        "You reach in your wallet for your ID."
                    "Bouncer" "Hey, didn't you come in here before?"
                    if club == "track":
                        pcname "I might have."
                    elif club == "cheer":
                        "You twirl a piece of hair between your fingers, batting your eyelashes up at him."
                        pcname "I don't know. Did I?"
                    elif club == "yearbook":
                        show chelsea embarrassed
                        "You flush, embarrassment creeping into your cheeks."
                        "You nod, unable to bring yourself to say it."
                    "Bouncer" "Sorry, kid. I said it last time, I meant it. It's policy."
                    "He hands you back your ID."
                    "You shove it back into your bag."
                    if club == "track":
                        "You press your hand against your hip, rolling your eyes."
                        pcname "C'mon, man. Just this once?"
                    elif club == "cheer":
                        show chelsea sad
                        "You pout up at him, crossing your arms firmly."
                        pcname "Can't you make one exception?"
                    elif club == "yearbook":
                        show chelsea sad
                        "Your eyebrows crease in worry."
                        pcname "Am I in trouble?"
                        "Bouncer" "No, but you gotta go."
                    "He shakes his head, tapping the 21+ sign."
                    if club == "track":
                        "You cast him a dirty look before briskly walking out into the street."
                    elif club == "cheer":
                        pcname "Hmph!"
                        "You turn abruptly, your hair whipping behind you as you step out into the street."
                    elif club == "yearbook":
                        show chelsea sad
                        "You frown, but walk out into the street, holding your bag closely over your shoulder."
                    show chelsea blank
                    "You suppose you understand the rule, but it doesn't mean you have to be happy about it."
                    $ fakerid += 1
                    jump events_end_period
        "No." if True:
            "Still discouraged by last time, you shake your head and head back to the streets."
            "You'll just look up something on the internet at home, anyways."
            jump events_end_period

label stripclub3:
    show chelsea at right with moveinright
    "Streetlamps and neon signs light up the city streets as you wander around, searching for something to do."
    "You find yourself back at \"CLUB 22\", their lights advertising the new dancers of the night."
    "Would you like to enter?"
    menu stripclubenter3:
        "Yes." if True:
            if club == "track":
                show chelsea happy
                "Third time's a charm, right?"
            elif club == "cheer":
                "The sound of the party inside calls out to you invitingly."
            elif club == "yearbook":
                "Despite your nerves, you can't help but want to try again."
            "You open the door, entering the familiar entryway."
            show chelsea blank
            "The bouncer holds out his hand immediately, stopping you."
            "Bouncer" "Hey now. I've stopped you twice already. If you keep coming, I'm going to need to get the authorities involved."
            menu stripclubflirt:
                "Flirt with bouncer." if True:
                    $ corruption +=2
                    if club == "track":
                        "You place a hand on your hip, jutting it out to the side."
                        show chelsea embarrassed
                        pcname "Have you thought that maybe I keep coming because I want to see {i}you?{/i}"
                    elif club == "cheer":
                        show chelsea embarrassed
                        "You lick your lips, looking him over desirably."
                        pcname "Kinky."
                    elif club == "yearbook":
                        show chelsea embarrassed
                        "Afraid of being turned away again, you grasp the edge of your shirt, avoiding his face as you speak."
                        pcname "I-I was just hoping to see you again..."
                    "He seems taken aback by your response. You brush your hair behind your ear, taking a step forward."
                    "Bouncer" "You're eighteen."
                    if club == "track":
                        "You step closer, swaying your hips as you move."
                        pcname "I'm an adult."
                    elif club == "cheer":
                        "You look up at him through your eyelashes, closing the space between you."
                        pcname "I don't think that changes anything. Do you?"
                    elif club == "yearbook":
                        "You hesitate before shuffling forward, daring yourself to look up at him. You try to will away the flush exposed on your face, but it does nothing."
                        pcname "I-I'm not a child."
                    "The bouncer takes you in, seeming to actually look at you for the first time. You notice how his eyes linger on your lips, then trail to the rest of your body."
                    "Bouncer" "I could get fired for letting you in. I'm sorry."
                    show chelsea blank
                    "This time he does seem genuinely sorry."
                    if club == "track":
                        "You shift your weight again, and you notice how his gaze focuses on the movement of your hips."
                        pcname "That's disappointing."
                    elif club == "cheer":
                        "You reach out, gently brushing your fingers along his broad chest."
                        pcname "Me too."
                    elif club == "yearbook":
                        show chelsea sad
                        "You look down, dejected."
                        pcname "I understand."
                    show chelsea shocked
                    "You turn to leave, but he reaches out, placing a large hand on your shoulder."
                    show chelsea blank
                    "He glances at one of the security cameras in the corner of the room, quickly pulling his hand back."
                    "Bouncer" "Come again some other time. Maybe we can work something out."
                    show chelsea happy
                    "You allow yourself a small smile of satisfaction."
                    "You step out onto the sidewalk, feeling a little better about your chances upon your next visit."
                    $ bouncerflirt = True
                    jump events_end_period
                "Leave." if True:
                    if club == "track":
                        "You step back, startled at his abrupt threat."
                        pcname "C'mon man, I just want to check the place out."
                        "The bouncer shakes his head, pointing to the door."
                        pcname "Fuck it. Fine."
                        "Annoyed, you stomp back out onto the sidewalk. So much for this place."
                    elif club == "cheer":
                        "You glare up at him, crossing your arms firmly over your chest."
                        pcname "Is that a threat? I'm a willing patron like anyone else."
                        "Bouncer" "You're lucky I don't call your parents to escort you out."
                        "You wince at the mention of your parents. If only he knew..."
                        pcname "Fine. I can tell when I'm not wanted."
                        "You turn, quickly exciting the establishment. You can find something better to do."
                    elif club == "yearbook":
                        show chelsea sad
                        "His words send a jolt of fear through you."
                        "It's embarrassing enough entering a strip club. You can only imagine how shameful it would be to be dragged out in handcuffs."
                        pcname "I'm sorry!"
                        "You quickly hurry back into the street."
                    jump events_end_period
        "No." if True:
            "You know this won't go well. Thinking better of it, you decide to keep walking."
            jump events_end_period

label stripclub4:
    show chelsea at right with moveinright
    "\"CLUB 22\" stands out against the dark city streets, its neon lights vibrant against the otherwise dark buildings."
    "Would you like to enter?"
    menu stripclubenter4:
        "Yes." if True:
            "You feel as though your luck might be different this time around."
            "You step over the familiar threshold, finding yourself in the entryway."
            "The bouncer grins as you enter, and although he doesn't hold out his hand to stop you, his body still blocks the entrance into the club."
            "Bouncer" "You're back."
            "Bouncer" "You must really want to see the shows."
            if club == "track":
                pcname "If I didn't, I wouldn't keep coming, would I?"
            elif club == "cheer":
                show chelsea happy
                "You eye him over, a small smirk playing at the edges of your lips."
                pcname "It's not the only thing I want to see."
            elif club == "yearbook":
                show chelsea embarrassed
                "You allow yourself an embarrassed smile."
                pcname "Y-Yes..."
            "The bouncer adjusts himself, glancing back at the heavy curtains."
            "Bouncer" "How badly do you want to get in there?"
            "His hand roams to the buckle of his belt. You understand at once what he means."
            show chelsea blank
            menu stripclubhandjob:
                "Give in." if True:
                    $ corruption +=5
                    if club == "track":
                        show chelsea happy
                        "You grin, eyeing him over eagerly."
                        pcname "Badly."
                    elif club == "cheer":
                        show chelsea happy
                        "You lick your lips, running a hand through your hair."
                        pcname "Very badly."
                    elif club == "yearbook":
                        show chelsea embarrassed
                        "You flush, a rush of excitement building up inside of you."
                        pcname "B-Badly..."
                    "The bouncer walks behind you, and for a moment you think he's going to lead you elsewhere, but instead he pulls out a set of keys from his pocket and shoves them into the door, locking them."
                    show chelsea confused
                    pcname "What about the camera?"
                    "Bouncer" "It's broken. That's what the boss thinks, anyway."
                    show chelsea blank
                    "You glance up at the security camera and notice a piece of black tape covering the lens. It's so small that unless you look closely, you might not even notice it's there."
                    "Bouncer" "Come here."
                    "The bouncer gestures you toward a set of plush seats in the entryway, set aside as a sort of waiting area."
                    "You step toward him, and he pulls you down onto his leg, spreading them apart."
                    "Bouncer" "What are you waiting for?"
                    "You reach down, undoing his belt and unzipping his pants."
                    hide chelsea with dissolve
                    "You pull out his half-erect cock, wrapping your hands gingerly around its base."
                    "He watches you with half-lidded eyes as you work your hands on him, his erection growing to its full size with each stroke."
                    "You pull your hand back, letting your spit dribble into your palm before placing it back around his member, enjoying the squelch of your spit against his skin."
                    "Bouncer" "Mmm... Fuck..."
                    "The bouncer thrusts his hips upward into your palms, bouncing you a little on his leg as he does so."
                    "You run your thumb over the slit of his tip, sliding the precum down to his cock as you pump him."
                    "He jerks off into your hands, one hand grabbing your ass and massaging your butt cheeks as the other grips the edge of the seats."
                    "You pull one hand back. He's about to protest, but once you unbutton your shorts and press them into your dampening panties, he lets out a groan."
                    "You slip your fingers in and out of yourself, bucking against your hand as the other pumps his base."
                    "You slide your fingers out, feeling a little empty without them inside of you. You wrap your cum-covered hand around his cock, pumping with both palms once again."
                    "Bouncer" "Oh, fuck."
                    "His thrusts grow more violent, and he adjusts you so you're straddling his leg."
                    "You grind against his thigh, the fabric feeling good against your growing desire."
                    "His cock quivers in your hands as he reaches his climax, white cum pouring out over your fingers."
                    "He searches for something to help you clean up, but you lift your fingers up to your mouth, licking them clean."
                    "He grins, his body sputtering a little before coming down."
                    "Bouncer" "Hell, you're better than what's in there."
                    show chelsea blank at right with dissolve
                    "He nods to the strippers inside."
                    show chelsea happy
                    pcname "Can I go in now?"
                    "The bouncer nudges you off of his lap, and you slide off easily, wiping your hands onto your wrinkled shorts."
                    "Bouncer" "Be my guest."
                    $ bouncerhandjob = True
                    show black with dissolve
                    "You step into the party room, suddenly blinded by the neon lights and blaring music overhead."
                    show bg StripclubLobby
                    show chelsea blank
                    "Women in skimpy lingerie strut around, their asses barely covered and breasts hanging out as they bend over tables and grind on men in plush seats."
                    "Men walk around similarly, their bare chests exposed and their bulges prominent in their tiny underwear."
                    if club == "track":
                        show chelsea happy
                        "You grin, taking it all in. Yeah, this was worth it."
                    elif club == "cheer":
                        show chelsea happy
                        "You eye over the strippers, a smirk forming on your lips. This is better than the movies."
                    elif club == "yearbook":
                        show chelsea embarrassed
                        "You struggle not to turn your head away in shame as you take it all in. This isn't anything like you imagined..."
                    show chelsea blank
                    "You take a seat in front of one of the stages as the lights dim. An announcer belts over the stereo."
                    "Announcer" "Welcome to amateur night! And now introducing your instructor, Cherry Bosom!"
                    "A sexy woman in high heels and pink lingerie resembling cherry blossom petals struts out onto the stage. She jumps onto the pole, jutting her body out as she swings down."
                    "Cherry Bosom" "Welcome, my sexy little nymphs. Are you ready to learn with your best friend, Cherry?"
                    "Her voice is sultry and inviting, her gaze tracing over the array of men and women joined around her crowd."
                    "There are several whoops and hollers from the men around. A couple of women in the crowd giggle and glance at each other nervously."
                    "Cherry demonstrates a few moves on the pole, things she would consider easy. You suppose they are for her, and she certainly makes them look that way, but you question your own ability to do it like her."
                    "She instructs the audience with each move, emphasizing her body as she teaches them how to dance."
                    "Once she's finished, she turns to the audience."
                    "Cherry Bosom" "Who would like to try first?"
                    menu stripclubpoledancing:
                        "Raise your hand." if corruption >= 30:
                            "Your hand shoots up before you can think. She catches your eye, waving you up on stage."
                            "Cherry Bosom" "How about this sexy little flower right here? Come on up, baby!"
                            if club == "track":
                                "You rise confidently, making your way up the steps to the stage. The crowd cheers you on, and you revel in their confidence."
                            elif club == "cheer":
                                show chelsea happy
                                "You pull yourself up from your seat and strut up the steps to the stage. The crowd cheers you on, and you blow them a kiss."
                            elif club == "yearbook":
                                show chelsea embarrassed
                                "Unable to look the crowd in the eye, you hurry up the steps, focusing on Cherry Bosom so you won't have to look at anyone else. The crowd cheers you on, further causing you to blush."
                            "Cherry Bosom" "And what's your name, baby?"
                            "You had been so focused on her body earlier that you didn't realize Cherry was holding a microphone. She holds it out to you."
                            show chelsea happy
                            pcname "[pcname]."
                            "She pulls the microphone back to herself, turning to the crowd."
                            "Cherry Bosom" "Let's hear it for our sexy little volunteer, [pcname]!"
                            "The crowd cheers again."
                            "Cherry Bosom" "Now, I won't make you take your clothes off-."
                            "There's a few laughs and playful boos from the audience."
                            "Cherry Bosom" "But how about you show us what you've learned? Don't worry, I'll be here to provide lots of help along the way."
                            "She winks, squeezing you against her side, pressing you against her bulbous breasts. There's no way they aren't fake, but you don't mind."
                            "There's a few more cheers, and you settle yourself in front of the pole."
                            "You were right: she makes it look so much easier than it is. You don't have nearly the amount of core body strength to perform the stunts with ease, but you try regardless, and Cherry is there to help adjust you to make the moves as flawless as possible."
                            "After a few moments, you feel yourself getting the hang of it, and even enjoying performing on the pole in front of the crowd."
                            "They all cheer you on, perhaps the other strippers louder and more encouraging than the rest. They obviously know how hard it is and are proud of your attempts."
                            "Once you finish, the crowd cheers again, and Cherry waves to you dramatically."
                            "Cherry Bosom" "Give it up again for [pcname]!"
                            "There's another loud cheer, and you head back to your seat."
                            "For the rest of the night, you enjoy the shows and performances, receiving plenty of compliments from other patrons and the staff on your attempts on the pole."
                            "You leave feeling a little better about yourself."
                            $ poledancing = True
                            jump events_end_period
                        "Keep your hand down." if True:
                            "You refuse to humiliate yourself in front of the crowd. You watch a few other girls' hands shoot up, and even some of the men seem eager to try."
                            "Cherry points out a girl behind you, waving her up on stage."
                            "Cherry Bosom" "How about this sexy little flower right here? Come on up, baby!"
                            "You watch as the girl hurries up on stage, drunk enough to have the bravery to act, but not enough that heading up there causes any stumbling."
                            "Cherry helps her perform on the poll, assuring her that she needn't strip, but the girl does anyway, tossing her shirt into the crowd in excitement as she performs."
                            "It's sloppy and messy, earning a few laughs in the crowd, but most of them shout out encouragement and cheers."
                            "Once she's done, you applaud with the rest of the crowd. A few more contestants try the pole, some better than others."
                            "Once it's over, the performers take center stage again, thrusting and spinning against the pole with ease."
                            "After a little while, you find yourself tired and head out."
                            "You leave feeling satisfied."
                            jump events_end_period
                "Reject him." if True:
                    if club == "track":
                        show chelsea confused
                        "What's the point of this if you aren't going to be horny when you enter?"
                        pcname "Wouldn't this be defeating the purpose of a strip club? There's plenty others around."
                        "Bouncer" "Then maybe you should've gone somewhere else."
                    elif club == "cheer":
                        "You shift, eyeing him over. Flirting is one thing, but this..."
                        pcname "I'm not that desperate."
                        "Bouncer" "Desperate?"
                        "He glares at you, offended at your choice of words."
                    elif club == "yearbook":
                        show chelsea embarrassed
                        "You feel a blush creep past your cheeks up to your ears."
                        pcname "I-I'm not that kind of girl!"
                        "He frowns, clearly irritated."
                        "Bouncer" "That's disappointing. I thought you were."
                    "He pulls his hands away from his belt, jutting his thumb toward the door."
                    show chelsea blank
                    "Bouncer" "Get out before I call the cops."
                    if club == "track":
                        show chelsea confused
                        pcname "Are you for real?"
                        "He doesn't move."
                        show chelsea angry
                        pcname "Fuck you. I should report you to your manager."
                        "Bouncer" "I should report you for trespassing."
                        "You glare back at him as you stomp out into the street. Fuck that guy. A strip club isn't worth this much trouble."
                        jump events_end_period
                    elif club == "cheer":
                        show chelsea confused
                        pcname "Really? I won't toy with your dick so you're kicking me out?"
                        "Bouncer" "The decision is up to you."
                        "You huff, turning toward the door."
                        show chelsea blank
                        pcname "Like I said- I'm not desperate."
                        "You strut out of the building, making sure to give him a good look of what he's missing out on when you leave."
                        jump events_end_period
                    elif club == "yearbook":
                        "You hesitate for a moment, thinking it over."
                        "Bouncer" "Well? Are you going to c'mhere or leave?"
                        "You turn on your heel and rush out of the strip club. Coming here was a mistake."
                        "You just hope no one else sees you as you rush out of there!"
                        jump events_end_period
        "No." if True:
            "You aren't really in the mood to check out the strip club today."
            "You continue down the street."
            jump events_end_period
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
