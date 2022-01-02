label kate_walking_family:
    show chelsea at right with moveinright
    "You take a short walk around the city, but nothing interesting happens."
    "As you start to head home, you hear someone call your name."
    show chelsea confused
    K "[pcname]!"
    "Turning, you see Kate practically running toward you."
    show K Casual Laugh at right with moveinleft
    show chelsea shocked
    "You're barely surprised when she trips over her own feet as she nears you, falling into your arms."
    show K Casual Sad at midright with move
    K "Sowwie..."
    show K Casual Sad
    if club == "track":
        show chelsea happy
        pcname "Man... you really are something else..."
    elif club == "cheer":
        show chelsea happy
        pcname "It's fine. Just be careful, okay?"
    elif club == "yearbook":
        show chelsea happy
        pcname "It's okay..."
    show K Casual Blank at left with move
    K "I know, I know..."
    show K Casual Happy at left
    "She finds her footing and grins."
    K "So, what are you doing?"
    show chelsea blank
    if club == "track":
        pcname "Just stretching my legs."
    elif club == "cheer":
        pcname "I was bored, so I went for a walk."
    elif club == "yearbook":
        pcname "Nothing, really..."
    show K Casual Laugh at left
    K "Great! We should hang out then!"
    menu kate_walking_family_hangout:
        "Sure!" if True:
            show K Casual Happy at left
            K "Yay!"
        "I'm busy, actually." if True:
            show K Casual Sad at left
            K "Oh, but I..."
            "Her face falls as she realizes what you're not saying."
            K "Right. I'll see you at work then."
            show chelsea happy
            pcname "Yep! See you then!"
            hide K Casual Sad with moveoutleft
            "You feel bad as you turn away, but you just don't feel like spending time with her right now."
            jump events_end_period
    show K Casual Blank at left
    K "So... Are you hungry?"
    if club == "track":
        show chelsea happy
        pcname "I think I've worked up a bit of an appetite..."
    elif club == "cheer":
        show chelsea happy
        pcname "As long as we keep it light..."
    elif club == "yearbook":
        show chelsea happy
        pcname "Um... sure!"
    show K Casual Happy at left
    show chelsea blank
    K "Alright! I know a great place nearby..."
    show K Casual Blank at right with move
    pause 0.1
    hide K Casual Blank with moveoutleft
    hide chelsea with moveoutleft
    "She grabs your hand, practically dragging you with her."
    "A short walk later, she pulls you into a little shop."
    show bg DatePlace with dissolve
    "At first, you're not even sure it's a restaurant. But, after a few turns, you're standing in front of a little counter."
    "It looks like a little kebab stand - there are several types of plates and sandwiches on the menu board."
    "The clerk beckons you both forward."
    show K Casual Blank at left with moveinleft
    show chelsea at right with moveinleft
    K "I'm getting the doner kebab. What about you?"
    "He nods his head, reading off her total while you look over the menu."
    menu kate_walking_family_kebab:
        "Kefta. ($6)" if True:
            show chelsea happy
            pcname "Kefta kebab, please."
            "Clerk" "That is $6."
            $ Cash -= 6
            $ order = "kefta"
        "Shish. ($7)" if True:
            pcname "Ummm... Shish kebab."
            "Clerk" "That is $7."
            $ Cash -= 7
            $ order = "shish"
        "Doner. ($8)" if True:
            show chelsea happy
            pcname "I'll have the doner too."
            "Clerk" "That is $8."
            $ Cash -= 8
            $ order = "doner"
        "Dessert. ($4)" if True:
            show chelsea confused
            pcname "Kunefe? Is that a dessert?"
            "The clerk nods his head again."
            "Clerk" "Sweet pastry."
            show chelsea happy
            pcname "Sounds good!"
            "Clerk" "That is $4."
            $ Cash -= 4
            $ order = "kunefe"
    "He plates your food while you wait."
    show chelsea blank
    show K Casual Happy at left
    K "I love coming here because the servings are {i}huge{/i}!"
    K "I always have leftovers!"
    show K Casual Blank at left
    show chelsea happy
    "He passes each of you a tray and you walk to a small table near the windows."
    if order == "kefta":
        "You look at your plate: a platter of meatballs with rice pilaf."
        "It looks really good."
    elif order == "shish":
        "You look at your plate: a platter of grilled beef, onions, and peppers, with rice pilaf."
        "Your mouth is watering already."
    elif order == "doner":
        "You look at your plate: thin slices of meat are piled on a flatbread and topped with onions, tomatoes, and tzatziki."
        "It looks amazing."
    elif order == "kunefe":
        "You look at your plate: shredded wheat is covered with syrup and sprinkled with crushed pistachios."
        "You remember from the description that there's some kind of cheese inside."
        "You've never seen anything like it!"
    if order == "doner":
        K "The tzatziki is my favorite part. I didn't like yogurt before I tried it, but there's something about the cucumber and mint..."
    elif True:
        show K Casual Happy at left
        K "Oh, that looks really good! Maybe I should've gotten [order] too..."
        show K Casual Blank at left
        pcname "You can try some, if you want."
        show K Casual Happy at left
        K "Really!?"
        show K Casual Blank at left
        K "Oh... But I have a lot of food already."
        K "Maybe I'll get it next time."
        "You can't help but laugh."
    show chelsea blank
    "As you both dig in, Kate tells you a long story about work."
    K "So Emma tells him to stop touching her and to leave a big tip or she'll tell Emilia and he won't be welcome back."
    if corruptkate:
        show K Casual Laugh at left
        K "Guess she doesn't know how to get the {i}really{/i} good tips, huh?"
        "She giggles."
    elif True:
        show K Casual Mad at left
        K "Can you believe it? I would have told Emilia right away."
    show K Casual Blank at left
    K "Enough about work, though... What do you do when you're not there?"
    menu kate_walking_family_freetime:
        "I'm still in school, so..." if True:
            if club == "track":
                pcname "Mostly school, work, and track."
            elif club == "cheer":
                pcname "Between cheerleading and work, I don't have time for much else."
            elif club == "yearbook":
                show chelsea embarrassed
                pcname "I'm in the yearbook club at school..."
            show chelsea blank
            show K Casual Happy at left
            K "Right! I forget you're still in high school sometimes..."
        "Spend time with friends." if True:
            if club == "track":
                show chelsea happy
                pcname "I like to hang out with friends."
            elif club == "cheer":
                show chelsea happy
                pcname "I {i}do{/i} have friends..."
            elif club == "yearbook":
                show chelsea happy
                pcname "Sometimes I spend time with friends..."
            K "Like me!"
    show K Casual Laugh at left
    show chelsea blank
    "She laughs, mostly at herself."
    show K Casual Happy at left
    K "What about your family?"
    menu kate_walking_family_family:
        "Tell her about the accident." if True:
            $ kateknowsaboutfamily = True
            show chelsea sad
            pcname "I..."
            if club == "track":
                pcname "I don't really have any family left."
            elif club == "cheer":
                pcname "They're... gone. It happened last year."
            elif club == "yearbook":
                pcname "I don't... They..."
            show K Casual Blank at left
            "Her face falls; she grows more serious than you've ever seen her."
            if club == "track":
                pcname "There was an accident last year. They... didn't make it."
            elif club == "cheer":
                pcname "I was with them when the accident happened. I'm the only one who survived."
            elif club == "yearbook":
                pcname "They're... dead."
            show K Casual Sad at left
            K "Oh, [pcname]..."
            if club == "track":
                pcname "That's why I live alone - and why I'm still in high school."
            elif club == "cheer":
                pcname "It took a year for me to recover - mostly."
            elif club == "yearbook":
                pcname "I missed a year of school while I... dealt with things."
            "She nods, for once at a loss for words."
            if club == "track":
                pcname "But I'm okay now. Really."
            elif club == "cheer":
                pcname "It's been hard but... I'm okay."
            elif club == "yearbook":
                pcname "It's okay. I'm okay."
            show chelsea happy
            "You smile at her, as if to prove your point."
            show K Casual Happy at left
            "She smiles back."
            show K Casual Blank at left
            show chelsea blank
            K "I can't imagine that..."
            K "No wonder you're so much stronger than me. You've had to be..."
            "She shakes her head, suddenly looking very determined."
            show K Casual Happy at left
            K "I'll be your family, [pcname]!"
            menu kate_walking_family_response:
                "Like a little sister?" if True:
                    show chelsea confused
                    K "Hey! I'm older than you!"
                    show chelsea happy
                    show K Casual Laugh at left
                    "You laugh together and the tension dissipates."
                "I'd really like that." if True:
                    show K Casual Laugh at left
                    K "Me too!"
                    show chelsea happy
                    "You smile at each other. You hate talking about the accident, but..."
                    show chelsea blank
                    "With Kate... it's almost okay."
            show K Casual Blank at left
            show chelsea blank
            K "Seriously, though, I've always wanted a sister..."
        "Change the subject." if True:
            if club == "track":
                show chelsea happy
                pcname "I was raised by wolves, actually."
                show K Casual Laugh at left
                "She laughs."
            elif club == "cheer":
                show chelsea happy
                pcname "Oh, no, I've talked too much already."
                show K Casual Laugh at left
                "She laughs."
            elif club == "yearbook":
                show chelsea sad
                pcname "That's... confidential."
    show K Casual Blank at left
    show chelsea blank
    K "My parents got divorced when I was little."
    K "I don't remember much; just that it was awful."
    K "My mom cried a lot, and she worked all the time."
    K "I don't remember my dad, actually..."
    if corruptkate:
        show K Casual Happy at left
        K "Maybe that's why I like the attention I've been getting at work."
        show K Casual Laugh at left
        K "All of those men showing interest in {i}me{/i} for once..."
    elif True:
        show K Casual Sad at left
        K "Honestly, I'm not very comfortable around men, you know?"
        show K Casual Blank at left
        K "Maybe it's because my dad wasn't around, but I just don't know how to interact with men."
    pcname "Yeah, I get that."
    show K Casual Happy at left
    show chelsea shocked
    K "Oh, shoot! I just realized I offered to pick up an extra shift tomorrow morning."
    show chelsea blank
    show K Casual Blank at left
    K "I should really go home and get to bed..."
    if club == "track":
        pcname "I should head home too."
    elif club == "cheer":
        show chelsea sad
        pcname "Awww... Already?"
        show K Casual Sad at left
        K "Yeah..."
    elif club == "yearbook":
        show chelsea embarrassed
        pcname "Oh... right."
    show K Casual Happy at left
    K "It was really nice hanging out with you again, though."
    show K Casual Laugh at left
    K "We should do it again soon!"
    show chelsea happy
    pcname "Of course!"
    "She gives you a quick hug and grabs her tray."
    show K Casual Blank at left
    "You watch her throw her trash away - she drops half of it on the floor and has to retrieve it - and bound out the door."
    hide K Casual Blank with moveoutleft
    if club == "track":
        pcname "She's so energetic..."
    elif club == "cheer":
        pcname "She's such a klutz..."
    elif club == "yearbook":
        pcname "She's so hyper..."
    "You smile to yourself; she's a really good friend."
    show chelsea blank
    "Dumping your own tray, you leave the restaurant."
    hide chelsea with moveoutright
    jump events_end_period

label kate_sick:
    show chelsea at right with moveinright
    "When you arrive at work, your boss, Emilia, approaches you."
    show EM Happy at left with moveinleft
    "Emilia" "[pcname], how are you today?"
    if club == "track":
        show chelsea happy
        pcname "I'm good, thanks."
    elif club == "cheer":
        show chelsea happy
        pcname "I'm great!"
    elif club == "yearbook":
        show chelsea embarrassed
        pcname "Oh, um... I'm fine..."
    show chelsea blank
    "Emilia" "Great. So I need you to cover some extra tables tonight."
    show EM Neutral at left
    "Emilia" "Kate and Emma both called off, so we're a little short staffed."
    show EM Blank at left
    show chelsea shocked
    if club == "track":
        pcname "Kate called off? That's not like her..."
    elif club == "cheer":
        pcname "I can't believe Kate called off. She's always here."
    elif club == "yearbook":
        pcname "Kate? Oh... I hope she's okay..."
    show EM Neutral at left
    "Emilia" "I know; this is the first time she's missed work."
    show chelsea blank
    "Emilia" "I hope she's feeling better soon."
    show EM Happy at left
    "Emilia" "Anyway, thanks for your help tonight."
    if club == "track":
        show chelsea happy
        pcname "I'll do my best!"
    elif club == "cheer":
        pcname "I'll see what I can do..."
    elif club == "yearbook":
        show chelsea happy
        pcname "S-sure!"
    hide EM Happy with moveoutleft
    "Emilia walks back into the kitchen and you quickly change into your uniform."
    show chelsea sad
    pause 1.0
    hide chelsea with moveoutright
    "It's a rough night and you're constantly moving."
    $ tips += 11
    "You keep telling yourself the extra tips will make it worthwhile, but you're not quite sure it's true."
    "Customer" "Hey!"
    show chelsea at right with moveinright
    "You turn to find a middle-aged man beckoning you over."
    if corruptkate:
        "Customer" "Where's that really young girl?"
        show chelsea confused
        pcname "Oh, Kate?"
        show chelsea blank
        "Customer" "The little blonde. She looks really young."
        show chelsea happy
        pcname "That must be Kate. She's sick today, but I'll take good care of you!"
        if club == "track":
            "You lean forward, giving him a better view of your cleavage."
        elif club == "cheer":
            "You pull the side of your neckline open a little further."
        elif club == "yearbook":
            "Blushing, you wink at him."
        "He stares at you a moment, then shakes his head."
        "Customer" "You look a little old. She'll be back soon, right?"
        "You're a little taken aback, but you keep a smile on."
        pcname "I hope so!"
        "You're a little uncomfortable, but you brush it off."
    elif True:
        "Customer" "Where's my favorite girl?"
        if club == "track":
            show chelsea happy
            pcname "Oh, Kate? She couldn't come in tonight."
        elif club == "cheer":
            show chelsea happy
            pcname "Kate had to call off, so I'm here!"
        elif club == "yearbook":
            show chelsea embarrassed
            pcname "Oh, Kate... She... Um..."
        "Customer" "I hope she's okay... Her smile always brightens my day."
        show chelsea happy
        pcname "Aww, I'll let her know you missed her!"
    "After a long night, you're happy to clock out."
    hide chelsea with moveoutright
    play sound PhoneVibration
    show bg black with fade

    call screen TextingScene("Kate",
    [
        TextMessage("Hey [pcname]... are you off work?"),
        TextMessage("Just clocking out", sender = False),
        TextMessage("Can you do me a favor?"),
    ])

    menu kate2PhoneResponse1:
        "What will you say?"
        "Of course!" if True:

            call screen TextingScene("Kate",
            [
                TextMessage("Of course!", sender = False),
                TextMessage("Could you pick up some flu medicine for me?"),
                TextMessage("I feel awful"),
                TextMessage("No problem! What's your address?", sender = False),
                TextMessage("314 S Hampton Ave, apartment 4"),
                TextMessage("Thank you soooooo much"),
                TextMessage("See you soon!", sender = False)
            ])

            $ katesickflag = True

            jump events_end_period
        "Sorry, I'm busy." if True:
            call screen TextingScene("Kate",
            [
                TextMessage("Sorry, I'm busy.", sender = False),
                TextMessage("Oh sorry!!! Have a good night!!!")
            ])

            "You're too tired to do any favors tonight."

            jump events_end_period

label kate_sick2:
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
    $ clothes, hair = casualwear
    "You walk to Kate's apartment, stopping along the way to buy some medicine."
    "The drugstore has a few options: a name brand you recognize, the generic version of that, and a really expensive brand you've seen on TV."
    "You spend a few minutes reading the boxes and looking at the price tags, but they all seem basically the same."
    menu kate_sick2_medicine:
        "Generic. ($5)" if True:
            "It's got all the same stuff, but half the cost!"
            $ Cash -= 5
            $ medicine = "generic"
        "Name brand. ($10)" if True:
            "Sometimes it's worthwhile to pay for the brand name."
            $ Cash -= 10
            $ medicine = "namebrand"
        "Expensive name brand. ($25)" if True:
            "You've seen ads for it, so it seems like the best..."
            $ Cash -= 25
            $ medicine = "expensive"
    "Medicine in hand, you walk the rest of the way to Kate's apartment."
    "It looks like a nice building, and the neighborhood doesn't seem bad either."
    show chelsea at right with moveinright
    "You quickly find her door and knock."
    "There's no answer."
    "You knock again, but you're met with silence."
    "Reflexively, you try the door handle; you're shocked to find it unlocked!"
    show chelsea sad
    pcname "Oh, Kate... You have to be more careful..."
    show chelsea blank
    "You feel a little guilty letting yourself in, but since Kate was expecting you, you figure it's okay."
    "Her apartment is clean, but cluttered - just like you expected."
    "The walls are covered in positivity slogans and cute pictures; the furniture is sprinkled with stuffed animals and cute throws."
    "It's adorably and completely Kate."
    hide chelsea
    show bg black with dissolve
    "You tip toe around her apartment, trying not to make too much noise."
    "It doesn't take long for you to find her, snoring gently on the couch, surrounded by used tissues and discarded cough drop wrappers."
    show bg KS1 with dissolve
    "She looks exhausted and pale; there's even a spot on her pillow where she must have drooled in her sleep."
    "You're not sure if you should check on her or just leave the medicine and lock the door behind you."
    menu kate_sick2_stay:
        "Wake her." if True:
            "Gently, you shake her shoulder."
            show bg KS2 with dissolve
            K "Hmmmmmnnnn..."
            "She swats at your hand, snuggling deeper into her blankets."
            menu kate_sick2_wake:
                "Try again." if True:
                    "You shake her again, more firmly this time."
                    K "NNNnnnnnn..."
                    "She tosses in her blanket, squeezing her eyes shut."
                    "Suddenly, she jolts awake."
                    K "Whaaaaa~!"
                    "She flails under her blanket, thrashing and kicking, until she recognizes you."
                "Just leave the medicine." if True:
                    show bg KS1 with dissolve
                    "She's obviously exhausted, so you let the box on the coffee table, nestled among crumpled tissues."
                    K "MMMmmmmmmnnn..."
                    "You glance back at her face; she's still asleep."
                    "You're struck again by how exhausted she looks. Poor Kate..."
                    "Suddenly, her eyelids flutter."
                    show bg KS4 with dissolve
                    K "Whaaaaa~!"
                    "She flails on the couch, stuck in her blanket."
                    pcname "Kate! It's me!"
                    show bg KS5 with dissolve
                    "She stills, recognizing you."
        "Leave the medicine." if True:
            "Placing the box softly amid the scattered tissues on the coffee table, you try not to wake her."
            K "MMMmmmmmmnnn..."
            "You glance back at her face; she's still asleep."
            "You're struck again by how exhausted she looks. Poor Kate..."
            "Suddenly, her eyelids flutter."
    K "Oh... [pcname]..."
    show bg KS3 with dissolve
    "Exhausted, she sinks back into her pillow."
    K "Sorry... I was sleeping and then..."
    pcname "It's okay, Kate. Sorry I scared you."
    "She notices the medicine on the table."
    K "Oh..."
    if medicine == "generic":
        K "This is what I always buy! Thanks!"
        pcname "You're welcome!"
    elif medicine == "namebrand":
        K "Wow, you got the name brand... Thanks!"
        pcname "Of course!"
    elif medicine == "expensive":
        K "You got {i}that{/i} one? But it's so expensive!"
        pcname "I wanted to make sure you get better fast!"
        K "Aw, [pcname]..."
    "She smiles sleepily."
    K "It's so hard... being sick... when you live alone."
    if club == "track":
        pcname "Yeah, I know what you mean."
    elif club == "cheer":
        pcname "Tell me about it!"
    elif club == "yearbook":
        pcname "Yeah... I know..."
    "She blinks up at you, thinking about that."
    if kateknowsaboutfamily:
        K "Oh... right..."
        "She frowns, clearly remembering about your family. Then, suddenly, she smiles."
        K "That's why we're family now!"
    elif True:
        K "Oh, right..."
        K "You live alone too, don't you?"
        K "Does your family live nearby?"
        "You're overwhelmed by a sudden weight on your chest."
        if club == "track":
            pcname "No, they're... gone."
        elif club == "cheer":
            pcname "No, I... I'm an orphan."
        elif club == "yearbook":
            pcname "I... don't have any family..."
        show bg KS9 with dissolve
        "She sits up, surprised."
        K "What? I'm so sorry! What happened?"
        "She covers her mouth."
        K "You don't have to tell me! I'm sorry!"
        show bg KS11 with dissolve
        if club == "track":
            pcname "It's fine, I-"
            pcname "We were in a car accident last year."
        elif club == "cheer":
            pcname "It's not your fault! There was a car accident..."
        elif club == "yearbook":
            pcname "It's okay. Don't feel bad!"
            pcname "It was a-- a car accident."
        show bg KS10 with dissolve
        K "Oh, [pcname]..."
        "She bites her lip, tears trembling in the corners of her eyes."
        if club == "track":
            "It's hard to talk about, but you feel like the pressure is lifted as you speak."
            pcname "I'm the only one who made it."
        elif club == "cheer":
            "You usually try to avoid talking about it; it's just too hard."
            "But somehow, it feels good to tell Kate."
            pcname "So now it's just me..."
        elif club == "yearbook":
            "You hate how people look at you when you tell them about your family."
            "Their pity just makes you feel worse. But Kate..."
            pcname "Th-That's why I got an apartment this year..."
        K "I'm sorry; I didn't know."
        pcname "It's okay, I--"
        show bg KS11 with dissolve
        K "You're so strong, [pcname]. You're my hero!"
    show bg KS6 with dissolve
    "She wraps her arms around your waist, hugging you tightly."
    "Putting your arms around her head, you hold her against you."
    "You can't help but smile; she's an amazing friend."
    K "I think I have a fever, but I don't have a thermometer... Can you check?"
    pcname "Um..."
    K "My mom always used to kiss my forehead when I was little."
    menu kate_sick2_fever:
        "Kiss her head." if True:
            show bg KS7 with dissolve
            "Leaning over, you press your lips gently to her forehead."
            "Despite the situation, it feels oddly intimate."
            K "Oh..."
            "You pull away, blushing slightly."
        "Use your hand." if True:
            show bg KS8 with dissolve
            "You place your hand over her forehead."
            "She feels warm, but not hot. That seems normal, right?"
            "Standing up, you smile."
    if club == "track":
        pcname "You feel fine to me. I'm sure it's just that you're tired."
    elif club == "cheer":
        pcname "You feel just right! Maybe you're just tired?"
    elif club == "yearbook":
        pcname "You don't feel too hot... I don't think. Just get some rest, okay?"
    show bg KS4 with dissolve
    K "Yeah... I should sleep..."
    K "Thanks again, [pcname]... You're the best..."
    K "I'll see you at work!"
    show bg black with dissolve
    "She smiles up at you and closes her eyes; you're sure she's asleep before you've shut the door."
    $ acts-=1
    jump events_end_period
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
