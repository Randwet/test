label bakery:
    show bg Bakery
    stop music fadeout 3.6
    $ goingto = "work"

    if bakerycorrupt == 1:
        $ clothes = 'bakerycorrupt'
    elif bakerycorrupt == 2:
        $ clothes = 'bakerynew'
    elif True:
        $ clothes = 'bakery'

    call eventengine from _call_eventengine_2

    if payday:
        if bakerycorrupt == 2:
            $ paychecktotal = 37 * daysworked
        elif True:
            $ paychecktotal = 33 * daysworked
        "Before you left work, you picked up your paycheck."
        "You made [paychecktotal] dollars!"

        $ Cash += paychecktotal
        $ daysworked = 0

    $ goingto = "textwork"
    $ TextCheck = True
    call events_run_period from _call_events_run_period_4
    $ TextCheck = False

    jump city2

label bakeryinsult:
    $ insult = renpy.random.randint(1,3)
    if insult == 1:
        $ insult = "were a clumsy moron for dropping a towel on the floor."
    elif insult == 2:
        $ insult = "will need a new uniform soon if you keep eating so much on your breaks."
    elif True:
        $ insult = "won't be working there long if you don't learn to smile more."
    return

label bakeryrandom01:
    "You head into work."
    call bakeryinsult from _call_bakeryinsult
    "The manager was tough on you, saying that you [insult]"
    "All in all, it wasn't a very good day."
    jump events_end_period

label bakeryrandom02:
    "You head to work and begin your shift."
    if club == "track":
        "The outfit is very tight, but you manage to deal with it."
        "One of the customers winks as he tells you to keep the change, so maybe it helps?"
    elif club == "cheer":
        "The outfit is very tight; you feel really sexy in it!"
        "Especially when one of the customers winks and tells you to keep the change."
    elif club == "yearbook":
        "The outfit is very tight - you blush every time a man looks at you!"
        "Especially when one of the customers winks and tells you to keep the change!"
    $ Cash += 5
    jump events_end_period

label bakeryrandom03:
    "You make it to work just in time for your shift."
    "The manager calls you stupid for messing up on a change count!"
    $ varrandomcash = renpy.random.randint(1,3)
    "But once he leaves the room, the customer tips you [varrandomcash] dollars."
    "Maybe it wasn't {i}that{/i} bad after all?"
    $ Cash += varrandomcash
    jump events_end_period

label bakerycustomer01:
    "You head into work for the day and make sure to clock in."
    "Your boss sits in the back office, doing a mountain of paperwork."
    show chelsea at right with moveinright
    pcname "For a bakery, it sure does have a lot of files..."
    "You head to the front and man the counter."
    "Over the next few hours, the amount of customers varies."
    show GCBoy with moveinleft
    "Eventually, a young man - probably in his twenties - comes in and buys two loaves of bread."
    "He looks you over from head to toe."
    "Young Man" "Hmmm… you look pretty good in that apron..."
    if club == "track":
        show chelsea embarrassed
        "You ring up his bill and tell him the price."
        "In return, he pays and leaves - but not before paying you another \"compliment\" under his breath."
        hide GCBoy with moveoutleft
        "Thankfully, you can't quite make it out."
        "You have a feeling that, thanks to your tight clothes, you’ll be getting comments like that a lot more often."
    elif club == "cheer":
        show chelsea happy
        "You ring up his bill and tell him the price."
        "In return, he pays and leaves - but not before paying you another compliment under his breath."
        hide GCBoy with moveoutleft
        "Unfortunately, you can't quite make it out."
        "You have a feeling that, thanks to your tight clothes, you’ll be getting a lot more attention!"
    elif club == "yearbook":
        show chelsea embarrassed
        "You ring up his bill and stammer out the price."
        "In return, he pays and leaves - but not before paying you another \"compliment\" under his breath."
        hide GCBoy with moveoutleft
        "Thankfully, you can't quite make it out - but your face still burns with shame."
    jump events_end_period


label bakerykittens:
    show chelsea at right with moveinright
    "You’re working the counter at the bakery. It seems to be just another boring day, until..."
    "Eventually, you notice a faint meowing sound."
    "You lift your head from your hand and head outside."
    "In the alleyway next to the store, you see a small kitten. It peers up at you with its large eyes."
    "The poor thing seems starved; maybe you should give it some bread?"
    menu:
        "Take some bread from work?"
        "Yes, it's hungry!" if True:
            "You quickly head back inside and make sure the boss is in his office."
            "As usual, he is - probably browsing the internet or something."
            "You grab one of the half-loaves and head back outside."
            "Then, you tear off several pieces for the kitten."
            if catadopt:
                pcname "I wish I could take you home, but I'm pushing the limit with one cat already."
            elif True:
                pcname "I wish my apartment allowed pets..."
            "You spend another minute or two feeding and petting the animal, but then you get back to work."
        "No." if True:
            "Even though the kitten is really cute, it’s not worth getting in trouble over."
            "You head back inside and continue your shift."
    jump events_end_period

label bakery_mistake1:
    show chelsea at right with moveinright
    "You enter the bakery and start your shift by stocking shelves."
    "After that, you cover Lisa's break by working the register."
    BM "Hey [pcname], get in here!"
    "You walk back to the stock room, where the manager is waiting."
    "He flings his hand out, motioning to the shelves."
    show Keith Angry at left with moveinleft
    BM "What do you call that!?"
    pcname "What do you mean?"
    show chelsea confused
    BM "This mess! I thought you stocked these!?"
    if club == "track" or club == "cheer":
        pcname "I did. I put all of the carts away and--"
    elif club == "yearbook":
        pcname "B-But... I did put them away..."
    "He mocks you in a high-pitched voice."
    BM "\"I put them away,\" she says."
    BM "You're useless, you know that? You're lucky you even have a job."
    show chelsea sad
    pcname "I don't understand--"
    BM "Just fix it!"
    show chelsea shocked
    hide Keith Angry with moveoutleft
    "He storms away without explaining a thing."
    show L Blank at left with moveinleft
    L "Oh dear... Put the stock away wrong?"
    show chelsea blank
    pcname "I don't get it! I did exactly what I always do."
    show L Question at left
    L "Maybe you've been doing it wrong?"
    if club == "track" or club == "cheer":
        show chelsea angry
        pcname "Well, then he could've told me before! He didn't have to scream at me."
    elif club == "yearbook":
        show chelsea sad
        pcname "Why didn't he say anything before?"
    show L Blank at left
    "Lisa shakes her head."
    L "[pcname], you're just making things harder on yourself."
    show chelsea blank
    pcname "What?"
    L "He's the boss! If he's upset, don't give him excuses."
    show L Happy at left
    L "Sometimes it's just better to apologize, you know?"
    menu bakery_mistake1_advice:
        "I guess so..." if True:
            show chelsea sad
            $ corruption += 3
            L "Just trust me!"
        "But he's wrong!" if True:
            show chelsea angry
            show L Disappoint at left
            "Lisa shakes her head in defeat."
            L "It's like talking to a brick wall..."
    "You spend the rest of the shift reorganizing the stock room."
    jump events_end_period

label bakery_correct1:
    show chelsea at right with moveinright
    "You start your shift by washing dishes."
    "After putting them away, you start prepping ingredients for tomorrow."
    show Keith Angry at left with moveinleft
    BM "What the hell do you call that!?"
    show chelsea confused
    pcname "I was just getting things ready for tomorrow so--"
    BM "Not that. The dishes!"
    "He flings his hand toward the dish cart and erratically waves."
    show chelsea shocked
    pcname "I cleaned up and put them away."
    BM "For fuck's sake... Can't you do {i}anything{/i} right!?"
    $ intelligence -= 5
    menu bakery_dishes:
        "Defend yourself." if True:
            $ bakerychain += 1
            if club == "track" or club == "cheer":
                show chelsea angry
                pcname "What are you talking about? I put them away exactly how I found them!"
                "He throws his hands up."
                BM "You're too stupid to figure anything out. I don't know why I bother!"
                "He storms into his office, slamming the door behind him."
            elif club == "yearbook":
                show chelsea sad
                pcname "I don't understand; I put them away exactly how I found them!"
                "He throws his hands up."
                BM "You're too stupid to figure anything out. I don't know why I bother!"
                "Tears sting your eyes as he storms into his office, slamming the door behind him."
            show chelsea blank
            hide Keith Angry with moveoutleft
            show L Disappoint at left with moveinleft
            "Lisa approaches you, shaking her head."
            L "I told you not to give him excuses. Just apologize and he won't act like that."
            pcname "But I didn't do anything wrong! Why should I apologize?"
            "She sighs and walks away, still shaking her head."
        "Apologize." if True:
            $ corruption += 3
            $ bakerychain += 1
            show chelsea sad
            pcname "I'm sorry, sir. I promise I'll do it better next time."
            show Keith Blank at left
            "He stares at you a moment as if judging your sincerity."
            show Keith Neutral at left
            BM "Good. I don't want to have this conversation again, understood?"
            show Keith Blank at left
            "You bow your head."
            pcname "Yes sir. Thank you, sir."
            show Keith Neutral at left
            BM "Maybe you're not hopeless after all."
            hide Keith Neutral with moveoutleft
            "With a nod of his head, he walks back to his office."
            show chelsea blank
            show L Happy at left with moveinleft
            "As he leaves, Lisa approaches you, smiling."
            L "Great job! I'm glad you took my advice."
            show chelsea happy
            pcname "He was so much nicer..."
            L "If you want 'em sweet, you just need to add a little sugar!"
            "She winks before turning back to her own work."
    jump events_end_period

label bakery_mistake2:
    show chelsea at right with moveinright
    "As you enter the bakery, your boss stops you."
    show Keith Angry at left with moveinleft
    BM "Are you kidding me?"
    show chelsea confused
    pcname "Did I do something wrong?"
    BM "How are we supposed to get customers with you looking like {i}that!?{/i}"
    "You look down at your uniform, afraid you might have gotten something on it."
    "Everything looks fine."
    pcname "Looking like what?"
    show Keith Neutral at left with dissolve
    BM "Forget it. That's probably the best you can do anyway..."
    hide Keith Neutral with moveoutleft
    "He walks away, mumbling to himself about something being \"too small.\""
    show chelsea blank
    "When you walk behind the counter, you see Lisa kneading some dough."
    show L Blank at left with moveinleft
    L "Everything okay, [pcname]?"
    pcname "He was just complaining about the way I look. Is there something wrong?"
    "She looks you over and frowns."
    show L Disappoint at left
    L "Honestly? You're not the most attractive girl we've had working here..."
    L "You really should care a little more about your appearance. Our customers have certain expectations."
    show chelsea shocked
    pcname "What!?"
    L "I mean, you barely fill out your top! At least get a new bra or something..."
    menu bakery_mistake2_advice:
        "I look fine." if True:
            L "If you say so..."
        "Do you really think so?" if True:
            $ corruption += 3
            show L Happy at left
            L "Trust me. A new bra will do wonders!"
    "She laughs and heads into the stockroom."
    show chelsea blank
    pcname "A new bra?"
    "As you finish your shift, you think about her suggestion."
    scene bg black with dissolve
    jump events_end_period


label bakery_correct2:
    show chelsea at right with moveinright
    show L Happy at left with moveinleft
    "As soon as you enter the bakery, Lisa approaches you with a bag."
    L "Here! Don't let him see you until you put it on!"
    "She thrusts the bag into your hands with a smile."
    show chelsea confused
    pcname "What is it?"
    L "A new bra! Go into the bathroom. It'll make your cleavage {i}POP!{/i}"
    menu bakery_bra:
        "I guess it can't hurt..." if True:
            $ bakerychain += 1
            $ corruption += 3
            L "That's the spirit!"
            scene bg black with fade
            show chelsea blank
            "After changing into the new bra, you look at yourself in the mirror."
            $ bakerycorrupt = 1
            $ clothes = 'bakerycorrupt'
            show chelsea with dissolve
            if club == "track":
                show chelsea happy
                pcname "My boobs {i}do{/i} look bigger..."
                "A little nervous, you head back out and start your shift."
            elif club == "cheer":
                show chelsea happy
                pcname "My boobs {i}do{/i} look bigger!"
                "Excited, you head back out and start your shift."
            elif club == "yearbook":
                show chelsea embarrassed
                pcname "My boobs {i}do{/i} look bigger, but..."
                "Nervous, you head back out and start your shift."
            show bg Bakery with dissolve
            "An hour later, the boss walks in."
            show chelsea at right with move
            show Keith Angry at left with moveinleft
            BM "Haven't I told you before that the napkins--"
            show Keith Happy at left
            BM "Oh. [pcname], you look nice today."
            show chelsea embarrassed
            pcname "Th-Thanks!"
            "He nods, staring a moment longer at your chest. Then he walks toward his office."
            pcname "What about the napkins?"
            show Keith Neutral at left
            BM "The-- Oh. Don't worry about that. Keep up the good work."
            hide Keith Neutral with moveoutleft
            "He closes his office door behind him."
            show chelsea shocked
            pcname "Wow, what a change... Maybe Lisa's right..."
        "I don't think so!" if True:
            $ bakerychain += 1
            show L Disappoint at left
            L "You're no fun at all!"
            "She grabs the bag, shaking her head at you."
            L "You won't make it in this place if you're not a team player, [pcname]."
            show chelsea confused
            pcname "What does showing off my body have to do with being a team player?"
            L "Just forget about it."
            "Sighing, she carries her bag back behind the counter."
        "And maybe I'll undo a button or two..." if corruption > 5:
            $ bakerychain += 1
            $ corruption += 2
            $ bakerycorrupt = 1
            $ clothes = 'bakerycorrupt'
            L "You're so naughty! I love it!"
            scene bg black with fade
            "After changing into the new bra, you look at yourself in the mirror."
            show bg Bakery with dissolve
            show chelsea blank
            if club == "track":
                pcname "I do look good, but maybe I'm overdoing it?"
                "With a shrug, you head back to work."
            elif club == "cheer":
                pcname "Yeah, definitely need to undo another button..."
                "After doing so, you head back to work."
            elif club == "yearbook":
                pcname "I can't believe I'm doing this..."
                "After a few anxious minutes, you decide to go for it and head back to work."
            "An hour later, the boss walks in."
            show Keith Angry at left with moveinleft
            BM "Haven't I told you before that the napkins--"
            show Keith Happy at left
            BM "Oh. [pcname]... Wow."
            show chelsea happy
            pcname "You like it?"
            if corruption > 10:
                "You squeeze your arms in a little, making your cleavage even more apparent."
            "He nods, staring a moment longer at your chest. Then he walks toward his office."
            pcname "What about the napkins?"
            show Keith Neutral at left
            BM "The-- Oh. Don't worry about that. Keep up the good work."
            hide Keith Neutral with moveoutleft
            "He closes his office door behind him."
            pcname "That was amazing. Looks like I'll be dressing like this from now on!"
    scene bg black with dissolve
    jump events_end_period

label bakery_mistake3:
    show chelsea at right with moveinright
    "While you're working the register, a customer approaches with a complaint."
    "Customer" "I know they didn't hire you for your brains, but you should at least be able to count."
    show chelsea confused
    pcname "I'm sorry, sir, but what seems to be the problem?"
    "Customer" "I gave you a ten and you only gave me $3.49 back in change. Where is my other dollar?"
    show chelsea blank
    pcname "I'm so sorry about that. Let me get my manager and he'll take care of that for you!"
    show bg black with dissolve
    "You walk to the back office, knowing that you'll be in trouble whether you made a mistake or not."
    show bg BakeryOffice with dissolve
    if club == "track":
        pcname "Sir, there's a customer who says I--"
        show chelsea sad
        show Keith Angry at left with moveinleft
        BM "What did you fuck up now? Wait right here while I take care of this!"
        hide Keith Angry with moveoutleft
        "He doesn't wait for you to answer before storming out to speak to the customer."
        "The sounds of their conversation are muffled, but you can vaguely hear him apologizing."
        pcname "Maybe I really did mess up?"
        "A few minutes later, your boss storms back into the room."
        show Keith Angry at left with moveinleft
        BM "How many times can you fuck up something as simple as counting change!?"
        pcname "I'm really sorry, it won't--"
    elif club == "cheer":
        pcname "Sir, there's a customer who says I--"
        show chelsea sad
        show Keith Angry at left with moveinleft
        BM "What did you fuck up now? Wait right here while I take care of this!"
        "He doesn't wait for you to answer before storming out to speak to the customer."
        "The sounds of their conversation are muffled, but you can vaguely hear him apologizing."
        pcname "Ugh, he seems really mad..."
        "A few minutes later, your boss storms back into the room."
        show Keith Angry at left with moveinleft
        BM "How many times can you fuck up something as simple as counting change!?"
        pcname "I'm really sorry, it won't--"
    elif club == "yearbook":
        pcname "S-Sir, there's a customer who says I--"
        show chelsea sad
        show Keith Angry at left with moveinleft
        BM "What did you fuck up now? Wait right here while I take care of this!"
        "He doesn't wait for you to answer before storming out to speak to the customer."
        "The sounds of their conversation are muffled, but you can vaguely hear him apologizing."
        pcname "Oh... I guess I really did mess up..."
        "A few minutes later, your boss storms back into the room."
        show Keith Angry at left with moveinleft
        BM "How many times can you fuck up something as simple as counting change!?"
        "Tears prick your eyes as he berates you."
        pcname "I-I'm really s-sorry, it won't--"
    BM "Lisa's running the register the rest of the day. You go clean the bathrooms."
    pcname "Yes sir..."
    hide Keith Angry with moveoutleft
    show bg black with dissolve
    "You gather up the supplies and head for the bathrooms."
    show bg Bakery with dissolve
    show L Blank at left with moveinleft
    L "Guess you're getting punished, huh?"
    pcname "He thinks I'm stupid..."
    "She shakes her head."
    L "Look, [pcname]... I wouldn't have put it so bluntly, but..."
    show L Happy at left
    L "You're not exactly the smartest person I've ever met, you know?"
    menu bakery_mistake3_advice:
        "What are you saying!?" if True:
            show chelsea angry
            show L Question at left
            L "I'm just saying that maybe you should get used to it?"
            show chelsea blank
            pcname "I-- Am I really...?"
            show L Happy at left
            L "Don't worry, honey. You're pretty enough that it won't matter."
            "She smiles kindly."
            "Tears well up in your eyes as you make your way to the restrooms."
        "You have no right to say that!" if True:
            show chelsea angry
            show L Disappoint at left
            L "Hey, don't get upset with me. {i}You're{/i} the one who can't count change."
            pcname "Everyone makes mistakes!"
            L "Yeah - but some people learn from them."
            "Glaring at her, you stomp off to the bathrooms."
    scene bg black with dissolve
    jump events_end_period

label bakery_correct3:
    show chelsea happy at right with moveinright
    "At the end of the day, as you're cleaning up the unsold bread, you have a sudden idea."
    pcname "We could make bread pudding!"
    show Keith Confused at left with moveinleft
    BM "What was that?"
    pcname "Oh, I didn't realize you were there, sir."
    show Keith Blank at left
    pcname "I was just thinking..."
    show Keith Neutral at left
    BM "Oh, here we go again."
    pcname "Maybe we could use the leftovers to make bread pudding instead of throwing them out?"
    pcname "That way we could still make some profit from--"
    show chelsea blank
    show Keith Angry at left
    BM "That's a ridiculous idea! It'd take up even more time and ingredients!"
    BM "Look, [pcname], the next time you have a stupid idea just keep it to yourself!"
    menu bakery_correct_idea:
        "Stand up for yourself." if True:
            if club == "track":
                show chelsea confused
                pcname "I think it's a great idea!"
                pcname "It might take a few extra ingredients, but we have them all right here."
                pcname "And it would give us a chance to cut our losses on the unsold bread."
            elif club == "cheer":
                show chelsea sad
                "Pouting, you protest."
                pcname "I think it's a great idea!"
                pcname "It might take a few extra ingredients, but we have them all right here."
                pcname "And it would give us a chance to cut our losses on the unsold bread."
            elif club == "yearbook":
                show chelsea sad
                pcname "B-But... We have all the ingredients, and..."
                pcname "And we wouldn't be wasting the bread..."
            BM "You really don't get it, do you?"
            BM "I don't give a damn what you think. I don't pay you to come up with \"great ideas.\""
            BM "Just do your work and stop giving me grief."
            "He slams his office door behind him."
            hide Keith Angry with moveoutleft
        "Agree." if True:
            $ corruption += 2
            show chelsea sad
            pcname "Oh, I guess I didn't think of that... I'm sorry, sir."
            pcname "I'll try not to bother you anymore."
            "You wipe up your tears and continue speaking."
            if club == "track":
                pcname "Thank you for explaining it to me."
            elif club == "cheer":
                pcname "Thank you for explaining it to an idiot like me."
            elif club == "yearbook":
                pcname "Th-Thank you for explaining..."
            "He stares at you a moment before smiling."
            show Keith Happy at left
            BM "Maybe I was too hard on you. It's not your fault you're so stupid."
            BM "Besides... you're almost pretty when you smile. So stop your crying."
            $ bakerychain += 1
            show chelsea embarrassed
            show bg black with dissolve
            pause 0.5
            show bg Bakery with dissolve
            pcname "Y-Yes sir. Thank you, sir."
            hide Keith Smile with moveoutleft
            "You finish cleaning up and get ready to leave."
            BM "[pcname], get over here."
            show chelsea blank at right with dissolve
            "You bow your head and approach the office door, waiting to be berated."
            show Keith Neutral at left with dissolve
            show bg BakeryOffice with dissolve
            BM "We have some extra cookies, so take those home with you."
            show Keith Blank at left
            "He motions to a bag on his desk."
            show chelsea happy
            if club == "track":
                pcname "Oh! Thank you, sir!"
                show Keith Neutral at left
                BM "Just make sure you exercise. I don't want you getting fat."
                show Keith Blank at left
                pcname "Don't worry - I get plenty of exercise!"
                show Keith Happy at left
            elif club == "cheer":
                pcname "Oh... {i}Thank you{/i}, sir..."
                show Keith Neutral at left
                BM "Just make sure you exercise. I don't want you getting fat."
                show Keith Blank at left
                pcname "Of course, sir!"
                show Keith Happy at left
            elif club == "yearbook":
                pcname "Oh! Th-Thank you, sir!"
                show Keith Neutral at left
                BM "Just make sure you exercise. I don't want you getting fat."
                show Keith Blank at left
                "You bite your lip."
                pcname "N-No, sir. Of course not..."
            "Taking the bag off the desk, you clock out and leave."
    scene bg black with dissolve
    jump events_end_period


label bakery_surprise:
    "You head into work."
    call bakeryinsult from _call_bakeryinsult_1
    "The manager was rough on you, saying that you [insult]"
    "All in all, it wasn't a very good day."
    show chelsea at right with moveinright
    "As you leave the bakery, you realize you forgot your phone inside."
    "You duck back in and grab your phone. On your way back out, though, you hear a strange sound coming from the manager's office."
    "Curious, you approach the door. It's open a crack."
    menu bakery_surprise_peek:
        "Take a peek." if True:
            "Putting your eye to the small opening, you look inside."
        "Just leave." if True:
            jump events_end_period
    "Inside, the manager is sitting at his desk and staring at his computer screen."
    show chelsea shocked
    "One hand holds the mouse while the other is... Oh!"
    menu bakery_surprise_watch:
        "Leave now." if True:
            "You've seen enough to know what he's doing - and you don't want to see any more."
            "As quietly as possible, you scurry out of the store."
            jump events_end_period
        "Watch." if True:
            pass
    if club == "track":
        "You know you should leave, but the idea of getting caught excites you!"
    elif club == "cheer":
        "The idea of watching him masturbate sends a thrill of arousal through your abdomen."
    elif club == "yearbook":
        "You're shocked by what you're seeing, and yet..."
        "Though you know you should go, for some reason you want to stay..."
    BM "Oh... fuck..."
    "You can't see his lap, but his shoulder jerks up and down as he strokes himself."
    BM "Yeah... fuck her face..."
    "His eyes are glued to the monitor."
    "Licking his lips, he leans a little closer to the screen."
    BM "Such a little slut..."
    "His breathing is getting more labored. He's probably almost finished. It might be a good time to sneak away."
    menu bakery_surprise_join:
        "Leave now." if True:
            "Unwilling to risk getting caught, you sneak out the front door before he's finished."
        "Keep watching." if True:
            if club == "track":
                "You know you should go while he's distracted, but..."
            elif club == "cheer":
                "You can't leave before the best part!"
            elif club == "yearbook":
                "Your face feels hot and a pool of warmth has settled between your legs."
                "You should go, but..."
            BM "Oh... fuck yes... fuck her hard..."
            "His face flushes as he strokes himself faster and faster."
            BM "You like that... you little slut...?"
            "He tilts his head back, moaning as he cums."
            "Before he recovers, you make a dash for the door."
        "Ask to help." if corruption > 15:
            $ corruption += 5
            if club == "track":
                "Feeling brazen, you push the door open."
            elif club == "cheer":
                "Too aroused to just watch, you push the door open."
            elif club == "yearbook":
                "You're too aroused to think straight."
                "Before you can reconsider what you're about to do, you push the door open."
            BM "What the fuck!?"
            "He fumbles with his pants as you step inside."
            if club == "track":
                pcname "Sir, is there anything else you need me to do before I go?"
                "He stares at you a moment, clearly unsure how much you saw."
                pcname "Is there, sir? Anything else?"
                BM "Anything?"
                "Smiling, you nod your head."
                BM "Get over here."
            elif club == "cheer":
                pcname "Please, sir... I just wanted to see if there's anything else I can help you with before I leave for the night."
                "You glance at his cock to make sure he understands."
                BM "...Is that so?"
                pcname "Yes. I want to make sure you know just how much I enjoy working for you."
                BM "Alright, show me."
            elif club == "yearbook":
                pcname "S-Sir, I just... Is there anything I can... help you with?"
                BM "What are you doing in here?"
                pcname "I just... I was..."
                "You can see the realization hit him."
                BM "You were watching me, weren't you?"
                pcname "Y-yes, sir. I--"
                BM "And you wanted to \"help\"?"
                "You can't bear to look at him - you look at the floor, instead, as you nod."
                BM "Then get over here."
            "Crossing the room, you stride around his desk and kneel beside his chair."
            "He turns toward you, letting you see his thick cock."
            if club == "track":
                pcname "Wow, you're huge!"
                "He smirks."
                BM "Think you can handle all of that?"
                pcname "I'm going to try!"
            elif club == "cheer":
                pcname "It's so big! I'm going to have a hard time getting my mouth around it."
                BM "I thought you wanted to show me how much you like your job?"
                "Looking up at him coquettishly, you lower your lips toward him."
                pcname "Oh, I do, sir. I promise I'll do a good job~"
            elif club == "yearbook":
                pcname "I-- You're so... big!"
                BM "Do you want to help me or not?"
                pcname "Y-Yes, sir, but..."
                "Taking a deep breath, you lower your face towards him."
            "You start by licking the head of his cock, which is already dripping pre-cum."
            pcname "Mmmm..."
            "Lifting his dick, you run your tongue along the bulging vein underneath."
            BM "Fuck..."
            "Licking him from base to tip a few more times, you slowly lube his cock with your saliva."
            "When it seems wet enough, you wrap your lips around his tip."
            "He's just as big as you expected, stretching your mouth wide."
            "Slowly, you lower your head and take him in an inch at a time."
            BM "You like that cock, don't you?"
            pcname "Mmmhmm!"
            "Your muffled response reverberates through his cock, making him moan."
            BM "I knew you were going to be a good girl..."
            BM "Go on. You can handle more, can't you?"
            "You bob your head up and down, trying to work your mouth a little further down his cock."
            if corruption > 17:
                "Eventually you manage to take it all in; his balls slap against your chin as you deepthroat him."
                BM "Oh fuck... I can't--"
                "He grabs your hair, holding you tight against him as he shoots his load down your throat."
                "When he releases you, you pull away with a {i}pop!{/i}"
                BM "Fuck... You were made for sucking cock."
                if club == "track":
                    "Grinning, you lick the last of his semen from your lips."
                elif club == "cheer":
                    "You smile up at him and lick your lips."
                    pcname "I know!"
                elif club == "yearbook":
                    "Gasping for breath, you offer him a shaky smile for his praise."
            elif True:
                "You manage to take a little more, but he's just too thick!"
                "Instead, you bob your head enthusiastically, noisily sucking him off."
                BM "Fuck... fuck..."
                "He grabs your hair and pulls your head back at the last second, spraying his load across your face."
                BM "That's better. I like the way you look right now..."
                "You look up at him; your lips part and you feel a string of cum move between them."
                pcname "Thank you, sir."
            "You stand up and walk to the door."
            pcname "I hope I proved myself to you today, sir."
            pcname "I'll see you next shift!"
            "Without waiting for a response, you slip out the door and close it behind you."
            if club == "track":
                "As you walk home, you feel pumped up - like you do after running!"
                "The thrill of doing something so spontaneous and {i}dirty{/i} is amazing!"
            elif club == "cheer":
                "You walk home, thinking about the taste of his cum on your tongue."
                "After that, you're sure he'll treat you better at work!"
            elif club == "yearbook":
                "Walking home, you're not sure how to feel about what you've done."
                "It was exciting, but terrifying at the same time..."
                "And yet... you can't help but think that - maybe - you'd like to do it again."
    scene bg black with dissolve
    jump events_end_period


label bakery_bossandlisa:
    "Since you skipped school, you get to work a little earlier than normal."
    "There's a sign on the counter that says they'll return soon."
    show chelsea at right with moveinright
    pcname "Huh, wonder why they put that up?"
    "You hear a soft voice coming from the manager's office."
    "The door's open just enough that you can hear him talking to someone. Maybe Lisa?"
    menu bakery_bossandlisa_peek:
        "Investigate." if True:
            pass
        "Start working." if True:
            "You don't want to get in trouble, so you get right to work."
            "A few minutes later, Lisa comes out of the office. Her eyes look wet... Was she crying?"
            "Maybe it was good that you minded your own business."
            jump events_end_period
    "Quietly, you approach the door and peek inside."
    scene bg black with fade
    BM "Tell me what your mouth is for?"
    L "Sucking cock, sir..."
    "The manager is standing in front of his desk with Lisa kneeling at his feet. He's pulling her head back by a fistful of hair."
    if club == "track":
        "Your mind is racing. Surely they're not..."
    elif club == "cheer":
        "You suck in a sharp breath."
        pcname "Oh... wow..."
    elif club == "yearbook":
        "You shouldn't be here!"
        "But now, this close, you're afraid that if you try to leave they'll hear you..."
    BM "And what else?"
    L "Nothing, sir. I'm too useless for anything else."
    BM "That's right. You're just a dumb slut, aren't you?"
    L "Yes, sir."
    "She sobs as he releases her hair."
    BM "What are you waiting for?"
    "She practically jumps forward, eagerly kissing his cock and balls."
    BM "You better have clocked out for this. Your mouth isn't worth paying for."
    L "I did, I swear!"
    "Her words are muffled by his balls. She sucks on each, her lips gently pulling at the sensitive skin."
    BM "I don't have all day; [pcname] will be here soon."
    if bakerychain < 4:
        BM "And that little bitch doesn't know her place yet."
    elif True:
        BM "Unless you think she can suck me off better than you?"
    "Lisa wraps her lips around his thick cock, easily taking him in."
    "She bobs her head up and down - staring up at him as she sucks his cock."
    BM "Fuck..."
    "Putting a hand on the back of her head, he crushes her face against him, forcing her to deepthroat him."
    "Her eyes widen in surprise - but she doesn't struggle."
    "As he holds her in place, tears run down her reddening cheeks."
    "When he releases her, she pulls back and starts gasping for air."
    "He barely gives her time to breathe before he pushes her back down again."
    BM "You can do better than that, can't you?"
    "You watch as she works the muscles of her throat, clenching and releasing to massage his cock."
    "His grip tightens on her head, pressing her tightly against him as he cums."
    "As his grip loosens, she pulls back and coughs again - a trail of cum dripping off her chin."
    BM "Clean up before you clock back in."
    "He tucks his cock back into his pants and walks around his desk to sit."
    BM "Don't you have anything to say?"
    L "Th-Thank you, sir. Your cum was delicious."
    "He smiles at her."
    BM "If you work really hard this week, maybe I'll give you a better reward this weekend."
    "You can't hear her response, as you back away from the door."
    "Hurrying back to the lobby, you wait by the door until Lisa walks out."
    L "[pcname], you're early today. There's a load of dishes back there when you clock in."
    pcname "Yeah, I didn't go to school today so I thought I'd come a little early."
    "Your voice falters a little on the word \"come.\" You {i}really{/i} hope she doesn't notice."
    "Unwilling to meet her eye, you hurry to the back and start washing dishes."
    jump events_end_period
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
