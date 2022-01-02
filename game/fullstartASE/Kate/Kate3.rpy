label kate_flowerinvite:
    show chelsea at right with dissolve
    "At the end of your shift, Kate bounces up to you."
    show K Happy with moveinleft
    show chelsea sad
    K "Look at this!"
    "She thrusts a flower in your face - a rose, by the smell."
    if corruptkate:
        if club == "track":
            show chelsea laugh
            "You can't help but laugh."
            pcname "I'd love to, but it's a little close to my eyes."
            "She giggles, pulling it back so you can actually see it."
            "You were right; it's a rose."
            show chelsea happy
            pcname "That's... cute?"
        elif club == "cheer":
            "You take a step back so you can see it."
            show chelsea happy
            pcname "That's lovely, Kate."
        elif club == "yearbook":
            "You jump back, startled."
            show K Laugh at left with move
            "She laughs."
            K "Sowwy, [pcname]..."
            show chelsea embarrassed
            pcname "I-it's fine. I was just surprised..."
            show chelsea happy
            "You were right; it's a rose."
            pcname "It's pretty, I guess?"
        show chelsea blank
        "She rolls her eyes, following you toward the front door."
        show K Happy at left with move
        show chelsea sad
        K "A customer gave it to me. Can you believe it?"
        show chelsea happy
        K "He said it \"fell out\" of a bouquet he bought {i}for his mother{/i}."
        show K Blank at left
        "As she reaches the doorway, she raises her arm out and dramatically drops it into the trash."
        K "Like I'd want garbage like that. It's just going to wilt and die."
        show chelsea laugh
        show K Laugh at left
        "You laugh with her and follow her out the door."
    elif True:
        if club == "track":
            show chelsea laugh
            "You can't help but laugh."
            pcname "I'd love to, but it's a little close to my eyes."
            show K Embarrassed at left with move
            K "Sowwy..."
            "She pulls it back so you can actually see it."
            show K Blank at left
            "You were right; it's a rose."
            pcname "That's cute!"
        elif club == "cheer":
            show chelsea happy
            "You take a step back so you can see it."
            pcname "That's lovely, Kate!"
        elif club == "yearbook":
            show chelsea sad
            "You jump back, startled."
            show K Embarrassed at left with move
            K "Sowwy, [pcname]."
            show chelsea happy
            pcname "I-it's fine. I was just surprised..."
            show chelsea blank
            "You were right; it's a rose."
            show chelsea happy
            pcname "That's very pretty..."
        show K Laugh at left with move
        K "Isn't it?"
        show K Blank at left
        show chelsea blank
        "She pulls it back, practically hugging it to her chest."
        show K Laugh at left
        K "A customer gave it to me. Isn't that sweet?"
        show chelsea confused
        pcname "Is he a regular?"
        show K Blank at left
        show chelsea blank
        K "No! I've never seen him before today."
        "She smiles softly."
        show K Happy at left
        K "He said he bought a bouquet for his mother's birthday and after he delivered it, he realized that this one had come loose."
        show chelsea happy
        K "He wasn't sure what to do with it, and then he saw the cafe and decided to have leave it on the table."
        "She blushes a little."
        show K Laugh at left
        K "But he said I was so sweet that he wanted to see my face when he gave it to me. Isn't that cute?"
        show chelsea sad
        "Your heart skips a beat, though you're not sure why."
        show chelsea blank
        "Maybe it's just the romance of the story. Or maybe it's because Kate--"
        show K Blank at left
        K "Actually, that reminds me!"
        "She looks up at you with big eyes, distracting you from your own thoughts."
        show K Embarrassed at left
        K "Um, there's a Flower Viewing Festival this weekend on Sunday. I've always wanted to go and..."
        show K Happy at left
        K "I thought, maybe... Maybe you'd like to go too?"
        menu kate_flowerinvite_choice:
            "Of course!" if True:
                show chelsea happy
                if club == "track":
                    pcname "Sure, why not?"
                elif club == "cheer":
                    pcname "Of course! That sounds fun!"
                elif club == "yearbook":
                    pcname "That could be fun..."
                show K Happy at left
                K "Really? You will?"
                "She grins and grabs your palm with her free hand."
                show K Laugh at left
                K "This is going to be so much fun!"
                show K Happy at left
                K "I'll see you Sunday!"
                $ katefestival = True
            "Not really my thing..." if True:
                show chelsea confused
                if club == "track":
                    pcname "Flowers aren't really my thing..."
                elif club == "cheer":
                    pcname "I have cheer practice, so..."
                elif club == "yearbook":
                    pcname "Thanks, but... I... I can't."
                show K Blank at left
                show chelsea blank
                "Her smile dims."
                K "Oh, of course. That's okay..."
                show K Sad at left
                "She looks down."
                K "I should get this home and into a vase."
                K "See ya, [pcname]!"
    jump events_end_period

label kate_flowerfest:
    $ clothes, hair = casualwear
    show chelsea at right with dissolve
    play sound PhoneVibration
    "You wake up to a text from Kate."
    call screen TextingScene("Kate",
    [
        TextMessage("I'm so excited! Meet at the festival at 11?"),
        TextMessage("Sounds good!", sender = False),
        TextMessage("YAY! <3")
    ])
    show chelsea happy
    "You smile at her enthusiasm and get ready for the festival."
    hide chelsea with dissolve
    show bg black with dissolve
    pause 1.0
    show bg CityD with dissolve
    show chelsea at right with moveinright
    "It's about a twenty minute walk to the park it's set up in, but you can see it several minutes before you arrive."
    show chelsea happy
    "There are tons of stands and carts set up, selling everything from pasties, to honey, to flower-scented soaps and lotions."
    "And, of course, lots of florists selling flowers and bouquets."
    show chelsea blank
    "As you approach the entrance, you see Kate standing by the gate, peering inside."
    show chelsea happy
    "Her eyes are round with wonder as she takes in the sights."
    show K Casual Blank at left with dissolve
    if club == "track":
        pcname "Hey there."
    elif club == "cheer":
        pcname "Hi, Kate."
    elif club == "yearbook":
        pcname "Hey."
    show K Casual Embarrassed at left
    "She jumps, squealing."
    K "Oh-my-god-it's-just-you!"
    "In her relief, her words run together."
    K "Everything's so pretty and I was just looking and I didn't even see you come up to me and then you were talking and I just--"
    show chelsea laugh
    pcname "Whoa, slow down."
    show K Casual Laugh at left
    "She giggles once. Then twice. Then giggles turn to laughter and you can't help but laugh too."
    show K Casual Happy at left
    show chelsea happy
    K "I'm so glad you came with me. Look at this!"
    "She sweeps her arm toward the gate, nearly hitting someone trying to enter."
    show K Casual Embarrassed at left
    K "Oops! Sorry!"
    show chelsea laugh
    "Shaking your head, you laugh again."
    show K Casual Blank at left
    show chelsea happy
    pcname "So where should we go first?"
    show K Casual Happy at left
    K "Oh, I know! Follow me!"
    show K Casual Happy at right with move
    show chelsea shocked
    hide K Casual blank
    hide chelsea
    with dissolve
    show bg black with dissolve
    "She doesn't give you a choice, taking your hand and pulling you along with her."
    "Leading you through the festival, she pulls you past a dozen stands until she reaches one selling tea."
    show bg CityD with dissolve
    show chelsea happy at right with moveinleft
    show K Casual Happy at left with moveinleft
    K "This is my favorite tea shop. I knew they'd have a stand here - that's where I heard about the festival."
    "As she approaches the stand, the cashier smiles and waves at her."
    show chelsea blank
    "Cashier" "Kate! I didn't know if I'd see you this weekend!"
    show K Casual Laugh at left
    K "Hi Tasha! You made the festival sound so nice, I just {i}had{/i} to come!"
    "They smile at each other and your heart skips another beat."
    show K Casual Happy at left
    show chelsea confused
    "Are you... jealous?"
    "Cashier" "I'm glad you did. So, what will you be having today?"
    show chelsea blank
    "It's probably just that you've gotten so used to being Kate's only real friend, the thought of her relying on someone else..."
    show K Casual Blank at left
    "She turns to you."
    show chelsea shocked
    K "What do you want, [pcname]?"
    show chelsea blank
    show K Casual Happy at left
    K "They have great tea, and the pastries are amazing too..."
    "You look at the little chalkboard menu. There are several varieties of tea, all with floral notes."
    "Glancing down at the pastry case, you see cookies and cakes decorated with flower-shaped icing and tiny candied flowers."



    pcname "I'll have..."
    menu kate_flowerfest_pastrychoice:
        "Cherry hibiscus tea. ($5)" if True:
            show chelsea happy
            pcname "...the cherry hibiscus tea."
            show K Casual Laugh at left
            K "That one is really good!"
            $ Cash -= 5
        "Peach and rose tea. ($4)" if True:
            show chelsea happy
            pcname "...the peach and rose tea."
            show K Casual Laugh at left
            K "That's one of my favorites!"
            $ Cash -= 4
        "Jasmine green tea. ($3)" if True:
            show chelsea happy
            pcname "...the jasmine green tea."
            show K Casual Laugh at left
            K "I {i}love{/i} jasmine!"
            $ Cash -= 3
        "Candied violet cookies. ($5)" if True:
            show chelsea happy
            pcname "...the candied violet cookies."
            show K Casual Laugh at left
            K "Aren't they the cutest?"
            $ Cash -= 5
        "Lavender cheesecake. ($8)" if True:
            show chelsea happy
            pcname "...the lavender cheesecake."
            show K Casual Laugh at left
            K "It's so pretty and the color comes from the flowers!"
            $ Cash -= 8
        "Chocolate and rose macarons. ($12)" if True:
            show chelsea happy
            pcname "...the macarons."
            show K Casual Laugh at left
            K "Macarons are {i}amazing{/i}!"
            $ Cash -= 12
    "Cashier" "Great choice! And for you, Kate?"
    show K Casual Blank at left
    K "Oh, um... Can I have one of each?"
    show chelsea blank
    "The cashier - Tasha, was it? - laughs."
    "Tasha" "I knew you were going to say that..."

    "Tasha gathers your treats and kindly passes them back to you, sending each of you off with a smile and a wave."
    "You're surprised to find you're relieved when you leave her stall."
    show chelsea happy
    pcname "Okay, what's next?"
    "Kate purses her lips and taps her chin in thought. Her eyes rove over the brightly colored stalls."
    show K Casual Happy at left
    K "Ah! That one looks cute!"
    "Your gaze follows hers to a lilac-painted stall. Hand-made soaps and perfumes sit on wooden display racks on either side of the register."
    pcname "That sounds great!"
    "Fresh floral scents greet you as you approach the stall."
    "Cashier" "Hey, Kate! Back again this year?"
    "A burly man with a righteous beard covered in small flowers smiles as the two of you peer at his display of hygiene products. Kate beams up at him."
    show K Casual Laugh at left
    K "Hi Bernie! I couldn't miss it!"
    "Bernie" "Well let me know if you ladies have got any questions."
    show chelsea blank
    "Bernie wanders over to help an elderly woman and her grandson as you check over the merchandise."
    show K Casual Blank at left
    K "Hmm... I can never decide what to buy here..."
    show K Casual Happy at left
    K "Everything he makes just smells so {i}good!{/i}"
    show K Casual Blank at left
    show chelsea confused
    "She picks up one of the bars of soap and tucks it under your nose. You breathe in the strong scent of citrus and cinnamon. You let out a cough."
    show K Casual Sad at left
    K "Sowwy!"
    show chelsea happy
    pcname "It's okay. I think that one's just a little too strong for me."
    show K Casual Blank at left
    K "Yeah, it doesn't suit me either. Hmmm... Okay!"
    show chelsea blank
    "Kate picks up three bars of soap, each cut into cute shapes, and sets them in a row in front of you."
    show chelsea confused
    K "What do you think I should get, [pcname]?"
    show chelsea blank
    menu kate_soap:
        "Lily." if True:
            "Shaped like its name, the lily soap is dyed with swirls of green aloe and brings a pleasantly sweet scent to your nose."
            show chelsea happy
            pcname "I think the lily suits you best, Kate."
            K "Really?"
            "Kate takes a big sniff of the soap and beams."
            show K Casual Laugh at left
            K "Wow! I love this! You're right, [pcname]!"
        "Rose." if True:
            "Dried petals rest inside of the pink-tinted soap in the shape of a heart. The aroma wafts up to your nose, scented with a hint of vanilla to give it a sensual feel."
            show chelsea happy
            pcname "The rose smells wonderful."
            "Kate leans forward and gives the soap a sniff, her lips curling happily."
            show K Casual Laugh at left
            K "That smells so good... I almost want to eat it!"
        "Lavender." if True:
            "Springs of real lavender peak out from the purple-tinted soap in the shape of a cloud. It reminds you of a peaceful dream."
            show chelsea happy
            pcname "I like the lavender best. It always helps me get to sleep."
            "Kate picks up the soap and pretends to use it as a pillow."
            show K Casual Laugh at left
            K "Mmm, you're right! I could take a nap right here with it!"
    "She giggles and sets it back down on the counter."
    "Bernie" "Have we decided, ladies?"
    show K Casual Happy at left
    K "Just this, please!"
    show chelsea blank
    "Bernie" "You got it."
    "Bernie rings her up and places the soap in a pink cloth bag."
    "Bernie" "Enjoy the festival you two!"
    show K Casual Laugh at left
    show chelsea happy
    K "We will!"
    "You each give him a small wave before leaving to explore the rest of the festival."
    "After exploring a few more stalls- a resin jewelry stand, a botanist author's book signing, and a stand full of colorful gardening hats- Kate leads you to one full of vibrant bouquets."
    show K Casual Blank at left
    K "Oooh, look at these, [pcname]!"
    show chelsea blank
    "Kate gushes over the flowers, pointing out various bouquets she likes."
    show K Casual Laugh at left
    K "Look at these roses! Ooh, and those lilies! And the carnations in that one! Wah, they're all so pretty!"
    show chelsea happy
    pcname "Why don't you get some?"
    show K Casual Sad at left
    "Kate juts her bottom lip out in a pout."
    show chelsea blank
    K "I don't have any money left..."
    "Her wide eyes stare at the flower arrangements longingly."
    menu kate_bouquet:
        "Buy her a bouquet. ($12)" if True:
            show chelsea happy
            $ Cash -= 12
            pass
        "Lecture her spending habits." if True:
            pcname "You should have saved some of your money. You were too eager to throw it around earlier."
            show K Casual Embarrassed at left
            K "I know..."
            show K Casual Sad at left
            "Kate stares at the arrangements a moment more before reluctantly pulling away from the stall."
            menu kate_bouquet2:
                "Buy her a bouquet. ($12)" if True:
                    "You glance between Kate's pitiful gaze and the vibrant arrangements on the stand."
                    pcname "Ah... wait!"
                    $ Cash -= 12
                    pass
                "Leave the festival." if True:
                    show chelsea happy
                    "You follow Kate back to the festival's entrance. Your afternoon has flown right by."
                    show K Casual Happy at left
                    "Kate clings to your arm, a vibrant smile on her face."
                    K "Thank you for coming to the festival with me, [pcname]!"
                    K "I had a really fun time."
                    pcname "Me, too. Thanks for inviting me."
                    K "Of course!"
                    show K Casual Blank at left
                    "Kate stands there for a moment, her lips parted as though she wants to say something. She shakes her head, dismissing the thought."
                    show K Casual Laugh at left
                    K "I better go. I'll see ya at work!"
                    pcname "Okay. See you then!"
                    "You each give a short wave before parting different ways down the street."
                    $ acts -=3
                    jump events_end_period
    "There are so many different kinds of bouquets it nearly makes your head spin."
    show K Casual Blank at left
    "Your gaze settles on a set of pretty bulb-like flowers in varying shades of pink."
    show chelsea blank
    hide K Casual Blank with moveoutleft
    pcname "Excuse me..."
    "An elderly woman running the stand jumps in surprise. She peers up from her book of crossword puzzles."
    "Cashier" "Oh, dear! You gave me quite a scare."
    show chelsea embarrassed
    pcname "Oh, sorry about that."
    "She waves you off, clearly unbothered by the mishap."
    show chelsea blank
    "Cashier" "It's no bother. How can I help you today?"
    pcname "I'd like to buy that set of..."
    "You squint at the name under the bouquet."
    pcname "That bouquet of peonies, please."
    "Cashier" "Yes, of course. That'll be $12, dear."
    "You fumble in your wallet for a few loose dollar bills. After you've exchanged them, the old woman wraps your bouquet up in a plastic sheet and passes it back to you."
    "Cashier" "Have a lovely day, dear!"
    show bg CityE with dissolve
    "She returns to her crossword puzzles before you've even left the stand."
    "Kate watches you curiously as you approach her with the flowers."
    show K Casual Blank at left with moveinleft
    show chelsea happy
    pcname "I heard someone wanted flowers?"
    "You smile and offer out the bouquet."
    show K Casual Laugh at left
    "Kate gives a loud, startled squeal before practically crushing them to her chest."
    K "Ah! [pcname], these are so beautiful! Oh my gosh! I love them! They're so pretty! These are gorgeous!"
    K "I can't believe you bought these for me! You didn't have to do that at all! Thank you so much!"
    "The more she talks, the more flustered she becomes, her cheeks heating up into a deep pink."
    K "I love these so much! I'm going to cherish them! Forever! I can't believe this! It's like having a boyfriend!"
    show K Casual Embarrassed at left
    "Her smile drops as she realizes what she said. Kate glances away awkwardly, still holding the bouquet close."
    pcname "Are you ready to go home?"
    "She gives a small nod."
    show K Casual Blank at left
    K "Ah, yeah..."
    K "Could you walk me...?"
    pcname "Sure."
    "You fall in step beside Kate as you escort her back to her apartment. As the sun starts to dip over the horizon you can't help but feel a little chilly."
    show chelsea blank
    "Kate is unusually quiet on the walk back, entirely focused on the arrangement of flowers in her hands."
    "Did you get her the wrong bouquet? Does she not like this one? You're tempted to go back and get her something else, but before you can make a decision, you find yourself in front of her apartment door."
    "Kate doesn't seem to notice, continuing to walk forward. You clear your throat."
    show chelsea happy
    pcname "Looks like we're here."
    K "Huh?"
    "Her head snaps up, as if pulled from a daze. She looks around, surprised to find her apartment building beside her."
    show K Casual Embarrassed at left
    K "O-Oh... We are..."
    "She makes no move to go inside. Kate clutches the flowers to her chest, her eyes downcast as she shifts her weight around."
    show K Casual Blank at left
    show chelsea confused
    "Worry creeps into your chest. Did you do something wrong?"
    show chelsea happy
    pcname "I had a really great time at the festival, Kate."
    "You wait a moment, hoping your words will encourage her to look at you. When she doesn't, you continue."
    pcname "I've never seen so many flowers in my life. It was... kind of magical, you know? Like a fairy tale."
    show chelsea embarrassed
    pcname "I, um, I hope you like the bouquet. I wasn't sure what flowers to get you, but these reminded me of you and-"
    show K Casual Embarrassed at left
    K "Will-you-be-my-girlfriend?!"
    show chelsea shocked
    "You blink, abruptly cut off by Kate's hasty question. All of her words come out in one breath, mingling together."
    "Her wide green eyes stare at you, nervous and hopeful."
    if damienrelate == "dating":
        menu kate_girlfriend1:
            "Yes, but... (Tell her about Damien)" if True:
                $ KateDamienConfession = True
                show chelsea sad
                pcname "I... Yes, but..."
                "Damien comes to mind, with his dorky smile and cargo shorts. Your date with him was so nice, and you already agreed to be his girlfriend..."
                "But..."
                pcname "I'm already sort of seeing someone right now."
                "Kate's face falls, embarrassment creeping up on her cheeks."
                show K Casual Sad at left
                K "O-Oh. Of course! You're so pretty, it makes sense..."
                show chelsea happy
                pcname "But I do really want to be your girlfriend!"
                show chelsea blank
                pcname "Maybe I can break it off with him..."
                show K Casual Blank at left
                "She stares at you, her mouth dropped in surprise."
                K "Really? You would do that for me?"
                show K Casual Embarrassed at left
                K "But what about your boyfriend? He would be heartbroken..."
                show chelsea happy
                pcname "It'll be okay. I really like you, Kate. I think... I mean, I'd really like to go out with you. If you still want that."
                show K Casual Sad at left
                "Kate bites her lip, holding back tears of excitement. She nods eagerly."
                K "Yeah. Yeah!"
                show K Casual Laugh at left
                "She stands there for a moment, wiping tears from her eyes. She gives a nervous laugh."
                K "I'm not really sure what to do now."
                show chelsea laugh
                pcname "Do whatever feels right, I guess."
                show chelsea shocked
                "Kate beams at you, her face lighting up with all the joy in the world. She hops forward and plants a quick peck on your lips."
                show K Casual Happy at left
                K "I'll see ya tomorrow!"
                show chelsea happy
                hide K Casual Happy with dissolve
                "You watch as she scurries into her apartment, blonde curls flying behind her."
                "You can't help but smile, even though the dread of seeing Damien again creeps up as soon as you leave her apartment."
                "How are you going to break it to him?"
                $ katerelate = "girlfriend"
            "Yes! (Don't tell her about Damien)" if True:
                show chelsea blank
                "You open your mouth, prepared to agree to her whims and throw caution to the wind, but Damien comes to mind, with his dorky smile and cargo shorts, and guilt replaces your excitement."
                show chelsea embarrassed
                "Your date with him was so nice, and you already agreed to be his girlfriend. Yet..."
                show chelsea blank
                "Damn the consequences. Damien is something you'll figure out later."
                if club == "track":
                    show chelsea happy
                    pcname "Yes! I'd love to go out with you, Kate!"
                elif club == "cheer":
                    show chelsea happy
                    pcname "I thought you'd never ask! Of course I'll be your girlfriend, Kate."
                elif club == "yearbook":
                    show chelsea happy
                    pcname "Y-Yes! Please! That would... that would make me very happy..."
                show K Casual Blank at left
                "Kate gasps, surprised by your answer. She practically vibrates in excitement before throwing her arms around your shoulders."
                show K Casual Laugh at right with move
                K "Yay! I'm so, so excited, [pcname]!"
                show chelsea laugh
                "You laugh, squeezing her against your chest. After a moment, she gives a nervous laugh."
                K "I'm not really sure what to do now."
                show chelsea happy
                pcname "Do whatever feels right, I guess."
                show K Casual Happy at left with move
                "Kate beams at you, her face lighting up with all the joy in the world. She plants a quick peck on your lips."
                show K Casual Laugh at left
                K "I'll see ya tomorrow!"
                hide K Casual Laugh with dissolve
                "You watch as she scurries into her apartment, blonde curls flying behind her."
                "You can't help but smile as she leaves."
                show chelsea blank
                "However, as soon as you leave her apartment, guilt gnaws at your stomach."
                "Damien is such a sweet guy, and Kate is a wonderful girl. What if they find out about each other? How are you going to choose between them?"
                "You shake your head and try to push the thought away. That's a problem for another day."
                show chelsea happy
                "For now, you try to enjoy the feeling of having a new girlfriend."
                $ katerelate = "girlfriend"
            "I'm already seeing someone..." if True:
                show chelsea sad
                if club == "track":
                    pcname "I'm sorry, Kate, but I'm already seeing someone..."
                elif club == "cheer":
                    pcname "I'm so sorry, Kate, but I have a boyfriend already."
                elif club == "yearbook":
                    pcname "I-I'm sorry! I... Um... I'm sort of... I have... I'm dating someone..."
                show K Casual Sad at left
                "Kate's face falls, all of the nervous hope draining from her expression."
                "She stares at you for a moment, unable to disguise the brief glimpse of brokenheartedness before she forces a smile and laughs."
                show K Casual Laugh at left
                K "Right! Right! Of course!"
                K "I was just kidding, anyway."
                show K Casual Blank at left
                show chelsea blank
                "She glances down at the bouquet, her expression strained."
                show K Casual Happy at left
                K "Well, I'd love to meet him sometime!"
                K "I should be going. See ya tomorrow, [pcname]!"
                show K Casual Sad at left
                hide K Casual Sad with dissolve
                "Before you can bid her a proper farewell, Kate rushes into her apartment, shutting the door tightly behind her."
                "You feel a jab of pity for her, but try to shove it aside. Kate's a sweet girl; you're sure she'll find someone worthy of her someday."
                "As you head back to your apartment, you just hope this won't make things awkward at work."
        $ acts -= 3
        $ clothes, hair = casualwear
        jump events_end_period
    elif True:
        pass
    menu kate_girlfriend:
        "Yes!" if True:
            show chelsea happy
            "There is no containing the fluttering of your heart or the grin on your face, especially when she makes such a cute, nervous expression."
            if club == "track":
                pcname "Yes! I'd love to go out with you, Kate!"
            elif club == "cheer":
                pcname "I thought you'd never ask! Of course I'll be your girlfriend, Kate."
            elif club == "yearbook":
                pcname "Y-Yes! Please! That would... that would make me very happy..."
            show K Casual Happy at left
            "Kate gasps, surprised by your answer. She practically vibrates in excitement before throwing her arms around your shoulders."
            show K Casual Laugh at left
            K "Yay! I'm so, so excited, [pcname]!"
            show chelsea laugh
            "You laugh, squeezing her against your chest. After a moment, she gives a nervous laugh."
            show K Casual Blank at left
            K "I'm not really sure what to do now."
            show chelsea happy
            pcname "Do whatever feels right, I guess."
            show K Casual Laugh at left
            "Kate beams at you, her face lighting up with all the joy in the world. She plants a quick peck on your lips."
            K "I'll see ya tomorrow!"
            hide K Casual Laugh with dissolve
            "You watch as she scurries into her apartment, blonde curls flying behind her."
            "You can't help but smile as she leaves."
            "As you walk back to your apartment, a warm sensation fills your chest. Is this what it feels like to be truly happy?"
            "Either way, you grin like an idiot the entire way home."
            $ katerelate = "girlfriend"
        "No." if True:
            show chelsea sad
            if club == "track":
                pcname "I'm sorry, Kate. I don't see you like that. But you're a great friend! I love hanging out together."
            elif club == "cheer":
                pcname "I'm so sorry, Kate, but you're more like a little {i}sister{/i} to me. I'd hate to ruin that."
            elif club == "yearbook":
                pcname "I-I'm sorry! I just... You... I see you more as a {i}friend...{/i}"
            show K Casual Sad at left
            show chelsea blank
            "Kate's face falls, all of the nervous hope draining from her expression."
            "She stares at you for a moment, unable to disguise the brief glimpse of brokenheartedness before she forces a smile and laughs."
            show K Casual Laugh at left
            K "Right! Right! Of course!"
            K "I was just kidding, anyway."
            show K Casual Blank at left
            "She glances down at the bouquet, her expression strained."
            show K Casual Happy at left
            K "I should be going. See ya, [pcname]!"
            show K Casual Sad at left
            hide K Casual Sad with dissolve
            "Before you can bid her a proper farewell, Kate rushes into her apartment, shutting the door tightly behind her."
            "You feel a jab of pity for her, but try to shove it aside. Kate's a sweet girl; you're sure she'll find someone worthy of her someday."
            "As you head back to your apartment, you just hope this won't make things awkward at work."
    $ acts -= 3
    jump events_end_period

label kate_girlfriend_aftermath:
    show chelsea happy at right with moveinright
    "As you head into work for the day, you catch a glimpse of Kate checking on one of her tables."
    show K Happy at left with dissolve
    "You wait until she's done before waving her over."
    show K Embarrassed at left
    "To your surprise, her cheeks pink and her pretty green eyes go wide with horror. She immediately looks to the ground and walks out of your line of sight."
    hide K Embarrassed with moveoutleft
    show chelsea confused
    pcname "Weird..."
    show chelsea blank
    "You try to brush off the strange interaction as you step into the back and get changed."
    "Once you're ready to go, you step back into the cafe and wait for Kate to walk back and greet you. You don't have any tables yet, and you've been looking forward to seeing your girlfriend all day."
    show chelsea happy
    show K Happy at left with dissolve
    "It takes a while, but eventually you see her blonde pigtails bounce as she makes her way toward you. You grin and wave."
    pcname "Hey, Kate!"
    show K Embarrassed at left
    "She stops in her tracks, seeming to notice you for the first time. She veers off in another direction and pretends to check on another table."
    show chelsea confused
    hide K Embarrassed with moveoutleft
    "You lower your hand awkwardly."
    pcname "Oh. Um, okay."
    "You brush it off as bad timing and leave to greet your first table."
    show chelsea blank
    "As your shift goes by, however, you notice that Kate is still avoiding you, deliberately going out of her way to prevent any interaction between you two."
    "At one point, she went as far as to walk outside and come through the back to avoid passing you with her tray of dirty dishes."
    "Before you can confront her about this, Emilia taps you on the shoulder."
    show EM Neutral with dissolve
    "Emilia" "Hey [pcname], you've got table seven."
    show chelsea happy
    show EM Blank
    pcname "Got it."
    show chelsea blank
    hide EM Blank with dissolve
    "By the time you're greeting your newest table, it begins to rain."
    "People rush in from outside, dripping wet and eager for shelter."
    "Despite the rush, you can't help yourself from glancing in Kate's direction, hoping to get her attention."
    "Every time she catches your gaze, she quickly looks away and hurries off."
    "After a couple of hours of chasing back and forth, you resign yourself to the uncomfortable silence."
    "While you're waiting for an order from the kitchen, Zoey walks up to you, her voice low and startling."
    show Zoey Neutral with dissolve
    show chelsea sad
    "Zoey" "Is everything okay?"
    show Zoey Blank
    show chelsea shocked
    pcname "Ah! Zoey, you can't sneak up on people like that..."
    show chelsea blank
    show Zoey Happy
    "Zoey" "Sorry. But, hey, everything okay? Between you and Kate?"
    show chelsea confused
    show Zoey Blank
    pcname "What do you mean?"
    show chelsea happy
    "You try to play it off with a smile, but not even you are convinced by it."
    show chelsea blank
    show Zoey Neutral
    "Zoey" "She won't come near you, man. Did you spit in her sundae or something?"
    show Zoey Blank
    "Even though Zoey says it as a joke, you can't help but feel a little panicked at her suggestion."
    hide Zoey Blank with moveoutright
    "Zoey grabs a tray of food for her table, leaving you alone with your thoughts."
    show chelsea confused
    pcname "Did I do something wrong?"
    "You search for some sign on her face that could quell your suspicions, but her nervous glances only leave you feeling more uncertain."
    show chelsea blank
    "As you near the end of your shift and the crowd disperses, you finally catch her refilling a tray of drinks."
    show K Blank at left with dissolve
    pcname "Hey, Kate."
    show K Embarrassed at left
    "Her eyes snap up to you in a panic. She hurriedly picks up the tray, her drinks only half-filled, and scans the area for an escape."
    show chelsea sad
    pcname "Is everything oka-"
    show chelsea shocked
    "Before you can get the word out, you're drenched with a splash of ice and cola. You blink, trying to adjust to the sudden freezing temperature on your torso."
    "Kate holds up one of the empty glasses with a mixed look of regret and determination."
    show chelsea angry
    pcname "Kate!"
    K "S-Sorry!"
    "She quickly moves past you, ducking her head to avoid meeting your gaze."
    hide K Embarrassed with moveoutleft
    show chelsea blank
    "You miserably clean up your uniform the best you can before returning to your customers."
    "You're grateful when your last table leaves so you can get out of your uniform."
    "As you peel the sticky clothes away in the dressing room, you mull over Kate's strange behavior."
    show chelsea sad
    pcname "Did I do something to upset her?"
    hide chelsea with dissolve
    pause 0.5
    $ clothes = 'underwear'
    show chelsea at right with dissolve
    "You roll down your stockings, leaving only your bra and panties in place. The door opens behind you."
    show K Embarrassed at left with moveinleft
    "Kate gasps. You glance over your shoulder to see her face flushed a deep crimson, her mouth gaping open like a fish."
    K "I-I'm so s-sorry!"
    show chelsea confused
    "Kate turns to leave. You quickly reach out and grab her elbow to stop her."
    if club == "track":
        pcname "Hey! Wait a minute."
        pcname "What's been going on with you today? You threw a {i}drink{/i} on me."
    elif club == "cheer":
        show chelsea angry
        pcname "Hold on!"
        pcname "What's with the cold shoulder today? And throwing a drink on me?"
    elif club == "yearbook":
        show chelsea sad
        pcname "W-Wait! Please."
        pcname "I-I just want to talk. Are you... are you mad at me? Did I do something wrong? You've been so..."
    show chelsea blank
    show K Sad at left
    K "I-I know! I'm so, so sorry!"
    show K Embarrassed at left
    "She bows her head, embarrassed and ashamed of her behavior. You finish changing as you talk to her."
    show chelsea sad
    pcname "I'm just confused. I mean... If you didn't want to date, we-"
    show K Sad at left
    K "No!"
    "Kate waves her hands wildly, as though she can dissipate the idea into nothing."
    K "It's not that! Really! I promise, I promise!"
    show chelsea blank
    pcname "Okay... Then what is it?"
    show K Embarrassed at left
    "Kate hesitates, biting her lip. She fiddles with her hands nervously."
    K "I-I just felt uncomfortable at work..."
    K "C-Can we, um, c-could you walk me to my apartment? So we... we can talk in private?"
    "You give her a small nod. You don't really want one of your coworkers to walk in the lounge during this type of conversation anyway."
    pcname "Sure."
    hide K Embarrassed
    hide chelsea with dissolve
    $ clothes, hair = casualwear
    show bg black with dissolve
    pause 1.0
    show bg Cafe with dissolve
    show chelsea at right with dissolve
    show K Embarrassed at left with dissolve
    "You sling your bag over your shoulder and stand there, waiting. Kate sheepishly looks between you and the dressing room mirrors."
    K "Could you wait outside while I... um..."
    show chelsea shocked
    "She gestures nervously to her clothes. You feel a little taken aback; changing in front of each other hadn't been a problem before."
    show chelsea blank
    pcname "Yeah, of course."
    show K Happy at left
    "Kate gives you a grateful smile as you step outside the dressing room and wait."
    hide K Happy
    hide chelsea
    show bg black with dissolve
    pause 1.0
    "Once she's dressed and ready to go, you walk alongside her out onto the sidewalk."
    show bg CityE with dissolve
    show chelsea at right with moveinright
    show K Casual Blank at left with moveinleft
    "While it's not storming, there's still enough rain to soak through your clothes. You pull a small umbrella out of your bag and pop it open, hovering it over yourself and Kate."
    "She gives you a smile, standing a little closer to avoid soaking her shoulder."
    "As you turn the corner, out of sight from the cafe, Kate carefully takes your free hand in hers. She intertwines your fingers together."
    show chelsea shocked
    show K Casual Happy at left
    K "This is so great! I've never had a girlfriend before, [pcname]. I'm so excited!"
    show chelsea happy
    "She beams up at you, the light in her eyes conveying all the eagerness of a child. You can't help but grin back."
    show K Casual Sad at left
    K "Ah, but I don't really know what to {i}do{/i} with a girlfriend. I mean, with work, and what the girls might say..."
    "Kate bites her bottom lip, worry creasing between her eyebrows."
    menu kate_work_relationship:
        "You're ashamed of me?" if True:
            show chelsea sad
            "You feel a sting to your heart as you realize what she's implying."
            show chelsea confused
            if club == "track":
                pcname "So you're saying that you're ashamed of me?"
            elif club == "cheer":
                pcname "Wait. Are you ashamed of me?"
            elif club == "yearbook":
                pcname "A-Are you... ashamed of me, Kate?"
            show K Casual Laugh at left
            show chelsea blank
            K "No! I just- I'm nervous."
            "She gives a weak, uncertain laugh."
            show K Casual Sad at left
            K "I've never done this before. But I'll get better at it! I promise!"
            show chelsea happy
            pcname "So you won't throw a drink at me next time?"
            show K Casual Happy at left
            "Kate peers up at you, a little nervous. You stick your tongue out at her, and she relaxes, understanding the joke."
            show K Casual Laugh at left
            K "Not unless you want me to!"
            "You both break out into smiles."
        "I'm sure it'll be okay." if True:
            show chelsea blank
            "You nod slowly. Now that you think about it, her behavior seemed more flustered than regretful."
            "It fills you with a sense of relief that she doesn't regret asking you to be her girlfriend."
            show chelsea happy
            if club == "track":
                "You release your held hands and yank Kate under your arm."
                pcname "Who cares what they're going to say? They'll just have to deal with it."
                pcname "Sure, maybe it'll be a little awkward at first, but they'll get used to it."
            elif club == "cheer":
                "You gently release your held hands and pull Kate under your arm, holding her close to your side."
                pcname "Yeah, maybe it'll be a little awkward, but it's not their relationship. They can get over it."
            elif club == "yearbook":
                "You hesitantly release your held hands and place an arm around her shoulders, cradling her against your side."
                pcname "It... It could be awkward for a bit, but I'm willing to go through it if you are."
            show K Casual Happy at left
            K "Yeah. I think you're right. Thanks, [pcname]."
            "Kate beams up at you, her soft curls bouncing as she walks."
    show K Casual Embarrassed at left
    "Her eyes widen suddenly."
    show chelsea confused
    K "Oh! I'm sorry about the dressing room! I just- Well, I-"
    show chelsea blank
    "She takes a deep breath, gathering her thoughts."
    show K Casual Blank at left
    K "It's different since we're dating now. I can't look at you the way I used to..."
    "She peers up at you shyly, her cheeks rosy and flustered."
    show K Casual Embarrassed at left
    K "Not that I can't look at you ever! That's not what I mean!"
    K "B-But when I look at you like {i}that{/i}, I just- we- it's, it's different!"
    K "But-but not a {i}bad{/i} different! I- D-Do you see what I mean?"
    show chelsea happy
    "She looks at you hopefully as you come to a stop outside of her apartment building."
    "She's so adorable, it's impossible to hide the genuine smile that slips onto your face."
    pcname "Yeah, I know exactly what you mean."
    show K Casual Blank at left
    "Kate lets out a gust of air, relieved."
    show K Casual Happy at left
    K "Thank you for being patient with me, [pcname]. I know it isn't easy..."
    show K Casual Laugh at left
    K "I'll try not to act so weird at work anymore, I promise!"
    pcname "Thanks, Kate. I would like that."
    show K Casual Blank at left
    "Instead of going straight into her apartment, Kate pauses, her gaze lingering expectantly."
    scene bg black with dissolve
    menu kate_walkhome:
        "Hug her." if True:
            show bg KateHug with dissolve
            "You set your umbrella to the side, ignoring the wet droplets that soak your hair as you pull Kate into your arms."
            "Kate gives a content noise, humming against the warmth of your chest as you hold her against you."
            "It feels nice to finally hold her like this, like any other couple would."
            "She pulls away too soon, leaving you shivering and wet in the rain. You pick up your umbrella, despite its uselessness now."
        "Kiss her." if True:
            show bg KateKiss with dissolve
            "You lean forward, adjusting your umbrella so it doesn't whack her in the face, and gently catch her mouth with yours."
            "Kate gives a happy moan against your lips, content as you wind your arm around her waist and pull her against you."
            "She's warm, especially against the chilly rain air."
            "Your tongue traces over her bottom lip, pulling it into your mouth. She lets out a small noise, pleased as you gently tug the skin."
            "The kiss ends too quickly, but the cold rain air leaves you both shivering and eager for shelter."
    scene bg CityE with dissolve
    show K Casual Happy at left with dissolve
    show chelsea happy at right with dissolve
    "Kate gives you a gentle smile, her cheeks flushed from the cold."
    K "Thanks for walking me home!"
    pcname "Anytime."
    "You make sure she gets inside safely before walking home."
    $ clothes, hair = casualwear
    jump events_end_period

label kate_cookies:
    $ clothes, hair = casualwear
    show chelsea at right with moveinright
    "By the time you arrive at work, there's little time in your schedule to change into your uniform. You rush to the dressing room and hurriedly pull off your clothes."
    hide chelsea with dissolve
    $ clothes = 'underwear'
    pause 1.0
    show chelsea at right with dissolve
    show K Casual Blank at left
    "The door creaks open. Kate peers in, her face flushing deeply as she takes in the sight of your half-naked body."
    show K Casual Embarrassed at left
    "She opens her mouth to apologize, but quickly snaps it shut and steps inside. She refuses to meet your gaze as she changes into her uniform."
    show bg black with dissolve
    hide K Embarrassed with dissolve
    hide chelsea with dissolve
    pause 1.0
    show bg Cafe with dissolve
    $ clothes = 'cafe'
    show chelsea at right with dissolve
    show K Blank at left
    "It's only when you're both fully dressed that Kate turns in your direction, greeting you with a shy smile."
    menu kate_pickon:
        "Pick on her." if True:
            show chelsea happy
            if club == "track":
                "You give her a devilish smirk."
                pcname "You never said I couldn't look at you, you know."
                "Kate blinks, taking a moment to process your implication. A deep pink spreads across her face to the tips of her ears."
                show K Embarrassed at left
                K "W-Wha- Y-You weren't looking, were you?!"
                "You grin, giving her a little wink before stepping out onto the work floor. You can still hear her sputtering behind you."
            elif club == "cheer":
                "You can't help yourself. You saunter over to her, your nails just barely caressing her face as you tuck a blonde lock behind her ear. She bites her lip."
                pcname "So, am I supposed to keep my eyes closed around you, too?"
                show K Embarrassed at left
                "If her face was pink before, it's certainly red now, spreading to the tips of her ears as she watches you with wide eyes."
                K "B-But- You-You weren't looking, were you?!"
                "You lean forward, her lips a breath away from hers."
                pcname "Who knows?"
                "Pulling away, you give her a wink and blow a kiss before stepping out onto the work floor."
            elif club == "yearbook":
                "Feeling a little bold, you smile playfully at her."
                pcname "S-Should I not look at you either, then?"
                "Kate eyes you warily, then laughs it off."
                show K Laugh at left
                K "Ha! You weren't looking... Were you?"
                "You give her a helpless shrug, enjoying the splotch of pink heating up her cheeks as you step out onto the work floor."
        "Don't pick on her." if True:
            show chelsea happy
            pcname "Ready to start?"
            "Kate gives a small salute."
            show K Laugh at left
            K "Aye, aye, captain!"
            "You both giggle as you leave the dressing room."
    show bg black with dissolve
    hide chelsea with dissolve
    hide K Laugh
    hide K Embarrassed
    pause 0.5
    show bg Cafe with dissolve
    show chelsea at right with moveinright
    "The cafe is moderately busy today, keeping you on your feet for the first half of your shift."
    "It's a relief when your lunch break rolls around. You hurry back to the dressing room and open up your locker."
    show chelsea confused
    "A small package starts to roll out. You rush to catch it before it falls onto the floor."
    "It's a ball of flower-patterned fabric with a small note attached with a ribbon at the top. You flip the note over to find Kate's cute, curly handwriting."
    show chelsea blank
    "It reads: 'You don't need cookies because you're so sweet already, but I made these specially for you! I hope you like them!' - Kate <3'."
    show chelsea happy
    pcname "Aww. That's so sweet!"
    "You grin, unraveling the ribbon to reveal an array of animal-shaped cookies. They're certainly homemade, with pink and yellow sprinkles making up the animals' faces."
    "You pluck a frog-shaped one from the pile and take a bite."
    show chelsea sad
    "The harsh, bitter taste of salt smacks against your tongue. You gag, your teeth grinding against the hard surface of the cookie as you try to chew and swallow it down."
    show chelsea angry
    pcname "These taste {i}terrible!{/i}"
    show chelsea sad
    "You look down at the bag of cookies in your hands. You'd hate to waste them and hurt Kate's feelings, but when you think of taking another bite, you gag again."
    show chelsea blank
    menu kate_cookies_throwaway:
        "Throw away the cookies." if True:
            "While it was a nice gesture, you can't bring yourself to try another one of these cookies. And it's not like she'd find out what happened to them if they just... disappeared."
            "Glancing around to make sure you're alone, you carry the bag of cookies over to the trash."
            show chelsea sad
            K "Oh, [pcname]! You found the cookies!"
            show K Laugh at left with dissolve
            "You freeze, dread forming in the pit of your stomach as you hold the cookies over the trash bin."
            "Kate bounces in, but the smile on her face fades when she sees what you're doing."
            show K Blank at left
            K "What are you doing, [pcname]? Are... Are they bad?"
            show K Sad at left
            "She peers up at you with those big green eyes, wide with worry and embarrassment. Guilt gnaws at your stomach."
            show chelsea happy
            pcname "No! Of course not! I was just... uh..."
            "You brush your hand over the cloth, sending crumbs into the bin."
            pcname "I was just cleaning up some crumbs. I didn't want to make a mess, see?"
            show K Blank at left
            K "Oh."
            show K Happy at left
            "Kate smiles. For a moment you think you're off the hook, but she stares at the pile of cookies in your hands expectantly."
            "You force a strained smile on your face and plop the second half of the frog cookie into your mouth. You struggle to keep the smile up as the salt dries up your tongue."
            "The second half is just as bad as the first. Maybe even worse."
            show K Laugh at left
            K "So you like them?"
            "How are you supposed to say no when she looks at you like that?"
            "You struggle to speak around the cookie, forcing it down your throat."
            pcname "Yup. Love it."
        "Eat them anyway." if True:
            show chelsea sad
            "You can't help but give a resigned sigh as you place the second half of the cookie in your mouth, cringing as the salt hits your tongue."
            show chelsea sad
            "While they may not taste good, Kate really did mean well when she made them. And you can't bear the thought of Kate finding out you hated them..."
            show chelsea blank
            show K Laugh at left with moveinleft
            K "Oh, [pcname]! You found the cookies!"
            "Speak of the devil."
            show K Happy at left
            "Kate bounces into the room, a wide grin on her face when she sees the cookies in your hand. You try to smile back, but you're not convinced it doesn't come out as a grimace."
            K "How do you like them? I made them last night before bed! I hope they're not too sweet."
            show chelsea happy
            "You force yourself to swallow the second half of the cookie, your cheeks pulled up in a strained smile."
            pcname "Oh, no. They weren't too sweet at all."
            K "That's great! Sometimes I put extra sugar in by mistake. They can come out a little sweeter than I expected."
            pcname "...I can't even tell."
    K "Oh good!"
    "Kate claps her hands together excitedly."
    show K Blank at left
    K "So I was thinking, do you want to have our very first date this Sunday?"
    show chelsea blank
    menu kate_firstdate_accept:
        "I'd love to!" if True:
            $ katedate = True
            show chelsea happy
            show K Laugh at left
            K "Really? Yay!"
            "Kate hangs onto your elbow, nearly spilling the cookies onto the floor. You kind of hope they fall, and try to hide your disappointment when they don't."
            show K Happy at left
            K "I was thinking we could have a picnic at the park! I've always wanted to go on a date like that!"
            K "Does that sound okay? Would you like that?"
            pcname "Yeah! A picnic sounds great, Kate."
            K "Yay! I'll meet you there at noon, okay?"
            pcname "That sounds great."
            show chelsea blank
            show K Blank at left
            "Before you can answer, Emilia opens the door."
            show EM Neutral with dissolve
            "Emilia" "Kate! Your table is looking for you."
            show EM Blank
            show K Embarrassed at left
            K "Oh! Right! I'm so sorry, I'll be out in a minute!"
            "Emilia gives the two of you a look before leaving."
            hide EM Blank with dissolve
            show K Blank at left
            "The salt burns in your mouth as you briefly consider letting her bring food. You're not sure you can handle another cookie scenario..."
            show chelsea happy
            pcname "Well, I'll bring the food if you bring the blanket."
            show K Happy at left
            K "That sounds great! I'll see you then, [pcname]!"
            "Kate practically trips over herself running back to the front of the cafe."
            hide K Happy with moveoutleft
            show chelsea laugh
            "You laugh, then look back at the cookies in your hands."
            show chelsea blank
            "It's a good thing {i}you're{/i} bringing the food."
        "Maybe some other time..." if True:
            $ turndownkate = True
            show K Sad at left
            K "O-Oh..."
            show chelsea sad
            "Your heart clenches a little at the disappointment on her face."
            "She looks at the cookies in your hands, as if coming to the conclusion that they're to blame."
            show K Happy at left
            K "Well, um, I'm glad you like the cookies!"
            "She gives you a small, awkward smile before hurrying back to the cafe."
            show chelsea blank
            "You stare at the cookies in your hands, unsure of what to do."
            "With a sigh, you bundle them back up and set them in your locker."
    jump events_end_period

label kate_firstdate:
    $ clothes, hair = casualwear
    $ katedate = False
    show bg HomeE with dissolve
    show chelsea at right with moveinright
    "When Sunday rolls around, you make sure to get up bright and early to prepare for your picnic date."
    "You had made sure to pick up groceries earlier this week, so you prepare an array of different sandwiches on your kitchen counter; ham, turkey, and chicken,"
    "You spread them out over fancy cloth napkins you found in one of your moving boxes, seasoning them with condiments and spices accordingly."
    "As you reach for the salt shaker, you notice it's empty."
    show chelsea confused
    pcname "Hmm..."
    "You fumble around in your cabinets, searching for the large plastic container holding all of your salt. You're surprised to find it with the baking supplies."
    pcname "Huh. That was a weird place to put it..."
    show chelsea happy
    "You refill your salt shaker and sprinkle it over the sandwiches before prepping the fruit salad."
    "Once the food is ready, you wrap each up tightly, tuck them safely into a zip-up cooler, and head to the park."
    hide chelsea with dissolve
    show bg black with dissolve
    pause 1.0
    show bg CityD with dissolve
    show chelsea happy at right with moveinright
    "It's a beautiful day; a light breeze in the air, blue skies, a perfect day for a special first date."
    "You find yourself smiling the entire walk there, your cheeks almost hurting when you spot Kate relaxing on one of the park benches. She doesn't even notice you at first, too preoccupied with a small mutt playing fetch with its owner."
    show K Casual Blank at left with dissolve
    pcname "Hi, Kate!"
    show K Casual Happy at left
    "She reluctantly tears her gaze from the pup and beams up at you. It's short-lived, and soon she's staring at the dog again."
    show K Casual Blank at left
    K "Oh! Hi, [pcname]! I'm sorry, I didn't even see you there."
    "You take a seat in the empty spot beside her and watch the puppy. It chases a drool-covered tennis ball with all the delight of a starving man at a feast."
    pcname "So you like dogs?"
    show K Casual Happy at left
    "She gives you an eager nod."
    K "I do! I love puppies. They're just so cute and cuddly and lovable!"
    K "But my apartment doesn't let me have any pets."
    show K Casual Blank at left
    "She frowns a little at that, the longing clear in her gaze as she stares at the running dog."
    show K Casual Happy at left
    "She smiles wistfully, watching for a moment longer before glancing at the basket in your lap."
    show K Casual Laugh at left
    K "The picnic! Let's find a spot to set it up!"
    show K Casual Happy at left
    "Kate takes your hand and you both glance around the park, searching for a nice spot to spread out."
    K "Oh! Oh! How about that tree?"
    "She points to a large, beautiful tree just past the lake. There's a large open spot tucked under the tree's branches in the shade."
    pcname "That looks great! Great eye, Kate."
    "She beams, pleased with herself as she bounces over to the spot, a large blanket and another cooler tucked under her arm. You follow behind, setting your cooler against the tree's trunk."
    show K Casual Blank at left
    show chelsea blank
    "You help Kate spread out the blanket, creating a perfect square in the shade, and start to unpack your bags. Kate divies out plastic cutlery, paper plates, and bottles of water while you unwrap the food."
    scene bg KCP1 with dissolve
    pcname "I wasn't sure what kind of sandwiches you liked, so I made a few different ones. I hope you like them."
    K "I'm sure I will! {i}You{/i} made it after all."
    "You grin, but your mind wanders back to those poor salty cookies she tried to surprise you with."
    "You each take a sandwich. Kate takes the first bite, her eyes widening in surprise before she swallows it down."
    pcname "How is it?"
    "She takes a moment to answer, as if deliberating how she feels about it."
    K "I love it! This is great, [pcname]!"
    "Kate smiles at you, lifting a weight off your shoulders. You grin back and take a bite of your own."
    "You immediately spit it out. Instead of a nice, salty sandwich, you're greeted with something... sweet?"
    "You lift a piece of bread and peer down at the contents of the sandwich; mayo, lettuce, tomato, cheese, ham, salt, and pepper. Nothing out of place or unusual."
    "Kate giggles beside you, watching the confusion on your face with amusement."
    K "Is something wrong, [pcname]?"
    pcname "Er... Well..."
    "You piece through the sandwich, trying to figure out what could be wrong."
    pcname "Are you sure you loved it? Did your sandwich taste okay? Mine was... definitely wrong."
    "Kate bursts into another trill of giggles. She presses her hands to her face, trying to disguise the bloom of red across her cheeks."
    "You sigh, setting your sandwich down."
    pcname "Well, there goes lunch."
    "Kate tries to talk between giggles, clearly more amused about this scenario than you are."
    K "No, no! It's great! I promise!"
    "She snorts."
    pcname "It's okay. You don't have to eat it."
    "Kate waves her arms wildly, shaking her head. She tries to catch her breath."
    K "It's not {i}bad{/i}, but I think you made the same mistake I did. Well, the opposite, maybe."
    "You cock your head to the side in confusion."
    pcname "What do you mean?"
    K "After work the other night, I went home to try some of the leftover cookies, but I must have used salt in the recipe instead of sugar! But I think you used the {i}opposite{/i} here!"
    "You briefly think back to the empty salt shaker from this morning. No wonder the 'salt' wasn't where it's supposed to be- you used {i}sugar{/i}!"
    "You can't help it. You burst into a spasm of giggles, nearly doubling over at your mistake. Kate joins you, throwing her head back with laughter."
    pcname "At least we still have the fruit salad."
    K "There's still that!"
    show bg KCP2 with dissolve
    "You both continue to giggle on and off for the next few minutes as you share the fruit salad. That, at least, is untainted by sugar {i}or{/i} salt."
    "When you've both finished eating, Kate lays back on the blanket and stares up at the sky through the branches."
    "You shove the leftover food back into the cooler and lay beside her."
    "Kate reaches out and intertwines your fingers with hers."
    "You lay together in silence, enjoying the cool shade in the midst of the sunny day."
    "After a few moments, Kate turns to you, her voice unusually quiet."
    K "Thank you."
    "You blink, taken aback."
    pcname "For the sandwiches?"
    "She grins but shakes her head."
    K "For being patient with me."
    K "I-I know I've been acting weird. I..."
    "She hesitates, gathering her courage."
    K "I really like you. I really don't want to mess this up."
    "Kate turns away, her attention drawn back to the sky. When she speaks again, it's barely above a whisper."
    K "Sometimes I wonder if this is a good idea. Maybe we should have just stayed friends. What if I really mess this up? What if we can't even look at each other again?"
    "You're not used to seeing Kate so serious. It throws you off, especially after such a sweet moment. You gently stroke her knuckles with your thumb."
    pcname "That isn't going to happen, Kate. You should just be happy instead of worrying about the future."
    if club == "track":
        "You gently touch her cheek, forcing her to meet your gaze."
        pcname "I like you. A lot. I'm not going anywhere."
    elif club == "cheer":
        pcname "I like, {i}really{/i} like you, Kate. I don't plan on going anywhere."
    elif club == "yearbook":
        pcname "I-I like you a lot, Kate. Don't push me away, please. I'm... I'm not going anywhere."
    "Kate smiles a little uncertainly, not entirely convinced, but it doesn't seem she's ready to argue. It might take some work to get her to believe you, but that's something you're willing to prove to her."
    "Her attention turns back to the sky."
    show bg CityD with dissolve
    show chelsea at right with dissolve
    show K Casual Happy at left with dissolve
    K "Thank you for the picnic. It was really fun!"
    show K Casual Laugh at left
    K "Even if the sandwiches were a little weird."
    show chelsea happy
    "You both giggle at that."
    show K Casual Happy at left
    K "I'll bake you some new cookies soon. I don't want you thinking I'm a terrible baker."
    menu kate_cookiefiasco:
        "I'm a little nervous about that." if True:
            show chelsea sad
            "You think about the bitter, salty cookies you had last time. It took forever to get that taste out of your mouth..."
            show chelsea blank
            pcname "I'm a little nervous about that."
            show K Casual Laugh at left
            show chelsea laugh
            "Kate laughs, and you can't help but join in."
        "I would like that." if True:
            "You smile and give her hand a squeeze."
            pcname "I would like that a lot."
            "Kate smiles, the light back in her eyes."
            K "They're going to be the best cookies ever! Just you wait!"
            show chelsea confused
            pcname "No salt this time?"
            show chelsea happy
            show K Casual Laugh at left
            "She laughs."
            show K Casual Happy at left
            K "Not this time."
    scene bg black with dissolve
    "You smile and rest your head on her shoulder."
    "It really is a beautiful day for a special first date."
    show bg black with dissolve
    $ acts -= 2
    jump events_end_period
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
