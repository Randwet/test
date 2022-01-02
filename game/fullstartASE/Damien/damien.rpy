label damienintro:
    show bg School with fade
    "As you approach the school, you hear someone shouting from behind you."
    show chelsea at right with moveinright
    "Short Boy" "Hey!"
    "You turn toward the voice, only to find a boy approaching you and waving."
    show Damien Happy at left with moveinleft
    "Short Boy" "S-Sorry, but I saw you again and..."
    if club == "track":
        "He seems really nervous."
    elif club == "cheer":
        "He looks really nervous; you can't decide if it's cute or not."
    elif club == "yearbook":
        "He seems really nervous; you can't help but feel bad."
    "Short Boy" "I just wanted to thank you..."
    menu damienintro_react:
        "For what?" if True:
            show chelsea confused
            show Damien Worry at left
            "Short Boy" "Oh, I should've known you wouldn't remember..."
            show chelsea blank
            show Damien Neutral at left
            "Short Boy" "The other day, you told off a guy who was picking on me."
            if club == "track":
                pcname "Oh, right."
            elif club == "cheer":
                show chelsea happy
                pcname "Right! I remember that!"
            elif club == "yearbook":
                show chelsea embarrassed
                pcname "Oh! Sorry! That was you?"
                show Damien Worry at left
            "Short Boy" "Yeah..."
        "You're welcome." if True:
            show chelsea happy
            if club == "track":
                "It's that boy who was being bullied!"
            elif club == "cheer":
                "It's the scrawny guy you stood up for!"
            elif club == "yearbook":
                "It's the boy that bully was picking on..."
            show Damien Neutral at left
            "Short Boy" "Most people wouldn't have bothered, so it meant a lot to me."
    show Damien Happy at left
    show chelsea blank
    "Short Boy" "Anyway, I'm Damien."
    $ damienname = "Damien"
    menu damienintro_name:
        "Introduce yourself." if True:
            if club == "track":
                pcname "I'm [pcname]."
            elif club == "cheer":
                pcname "And I'm [pcname]!"
            elif club == "yearbook":
                pcname "I'm... [pcname]."
            show Damien Laugh at left
            D "I'm glad I finally got to thank you."
            show chelsea happy
            show Damien Happy at left
            if club == "track":
                pcname "Yeah, it's nice to meet you. I was wondering how you were doing."
            elif club == "cheer":
                pcname "I'm glad we could talk too."
            elif club == "yearbook":
                pcname "Yes... Me too!"
            "He smiles nervously."
            show Damien Neutral at left
            D "I don't want to make you late... Thanks again!"
            hide Damien Neutral with moveoutleft
            "He hurries ahead of you, then smiles and disappears into the crowd."
            $ damienevents += 1
        "Tell him you have to go." if True:
            if club == "track":
                pcname "No problem, but I really need to get to class!"
            elif club == "cheer":
                pcname "Yeah, that's great, but I really need to get to class."
            elif club == "yearbook":
                pcname "S-Sorry, but I have class, and..."
            show Damien Sad at left
            D "Oh, right... Sorry..."
            "He waves hesitantly as you walk away. What a strange guy..."
    jump events_end_period

label damienlunch:
    show bg Cafeteria with fade
    show chelsea at right with moveinright
    "Taking your normal seat at lunch, you remember that Violet wasn't in class today."
    pcname "Guess I'm eating alone..."
    "With a sigh, you pick at your food."
    show Damien Happy at left with moveinleft
    D "Hey... You mind if I sit here?"
    menu damienlunch_sit:
        "I'd rather eat alone." if True:
            $ corruption += 1
            if club == "track":
                pcname "I like sitting alone, actually."
            elif club == "cheer":
                pcname "That seat's taken. They're all taken."
            elif club == "yearbook":
                pcname "Actually, I... I'd rather you... didn't."
            show Damien Shocked at left
            "His eyes widen in surprise."
            D "Oh!"
            show Damien Sad at left
            D "Sorry, I... I won't bother you again."
            "He walks away and takes a seat at another table."
            jump events_end_period
        "Sure. Go ahead!" if True:
            "He smiles and takes the seat across from you."
    D "So, you're new here, right?"
    pcname "Yeah, I've only lived here for a little while."
    show Damien Neutral at left
    D "I moved a couple times when I was younger. For my dad's job."
    show Damien Happy at left
    "He smiles as he asks the question you've been dreading."
    D "Is that why you moved here?"
    show chelsea sad
    pcname "I..."
    menu damienlunch_parents:
        "Tell him the truth." if True:
            $ damienknowsaboutfamily=True
            $ corruption -= 1
            pcname "Actually, my..."
            "You bite your lip and take a deep breath."
            pcname "My parents died in an accident..."
            show Damien Shocked at left
            "His eyes go wide. He opens his mouth to speak, but clearly can't find the words."
            D "I... I'm so sorry, I--"
            if club == "track":
                pcname "It's fine. Really."
            elif club == "cheer":
                pcname "It's okay."
            elif club == "yearbook":
                pcname "It... I..."
            pcname "Can we just... talk about something else?"
            "Nodding slowly, he changes the subject."
        "Avoid the question." if True:
            show chelsea happy
            pcname "Actually, I was abducted by aliens and this is where they dropped me."
            show Damien Shocked at left
            "His eyes widen. For a second, you think he might actually believe you - but then he starts laughing."
            show Damien Laugh at left
            "You smile back, but it doesn't reach your eyes."
    show Damien Neutral at left
    show chelsea blank
    D "Have you found your way around okay?"
    if club == "track":
        pcname "I've done a little exploring, but I'm sure there are places I haven't seen."
    elif club == "cheer":
        pcname "I've wandered around, but I'm sure someone who grew up here would know a {i}lot{/i} of interesting places..."
    elif club == "yearbook":
        show chelsea embarrassed
        pcname "I guess so. I get nervous going out alone..."
    D "There are a lot of really good restaurants and cafes you should try..."
    show chelsea blank
    "He looks down at the table, his voice growing uncertain."
    show Damien Happy at left
    D "If you want... I could show you sometime?"
    menu damienlunch_hangout:
        "That would be great!" if True:
            $ corruption -= 2
            "He grins."
            D "Really?"
        "I'm not interested." if True:
            $ corruption += 1
            show Damien Worry at left
            D "Oh... Of course not."
            "He stares at his plate again; you can't help but feel a little guilty."
            if club == "track":
                pcname "I just like exploring on my own."
            elif club == "cheer":
                pcname "I'm just really busy, you know?"
            elif club == "yearbook":
                pcname "I just... have a lot of school work and stuff..."
            "His eyes meet yours and he tries to smile."
            show Damien Happy at left
            D "Yeah... No problem."
            show Damien Sad at left
            "He seems grateful, but you can tell his feelings are hurt."
            "When lunch is over, you're relieved to part ways."
            scene bg black with dissolve
            jump events_end_period
    show chelsea happy
    pcname "Sure! I'd love to try something new."
    D "How about we get coffee? Are you free on Saturday?"
    menu damienlunch_coffee:
        "Sounds good to me." if True:
            D "Really?"
            "His enthusiasm is contagious."
            pcname "It sounds like fun!"
            D "Here, I'll text you the address. What's your number?"
            "You tell him and, almost immediately, your phone vibrates."
            $ chelseaContacts.contactsListed["Damien"] = "Damien"
            call screen TextingScene("Damien", [TextMessage("518 S Highland St")])
            D "See you there around noon?"
        "Maybe another time." if True:
            $ corruption += 1
            show chelsea blank
            show Damien Worry at left
            D "Oh, okay..."
            show Damien Happy at left
            "He smiles, but you can tell he's disappointed."
            show Damien Sad at left
            "For the rest of lunch, you make light conversation - but the mood's ruined."
            scene bg black with dissolve
            jump events_end_period
    pcname "I'll be there!"
    "The bell signals the end of lunch; you both jump up from the table."
    D "Wow, that went by fast!"
    pcname "We're going to be late if we don't hurry."
    "Grabbing your things, you rush out of the cafeteria."
    D "See you Saturday?"
    "You smile back at Damien."
    pcname "See you then!"
    $ coffeeflag = True
    $ damiendate = True
    $ damienevents += 1
    scene bg black with dissolve
    jump events_end_period

label damiencoffee:
    show bg HomeD with dissolve
    $ DamienAngry = "Characters/Damien/Casual/Angry.png"
    $ DamienBlank = "Characters/Damien/Casual/Blank.png"
    $ DamienGlare = "Characters/Damien/Casual/Glaring.png"
    $ DamienLaugh = "Characters/Damien/Casual/Laughing.png"
    $ DamienNeutral = "Characters/Damien/Casual/Neutral.png"
    $ DamienSad = "Characters/Damien/Casual/Sad.png"
    $ DamienShocked = "Characters/Damien/Casual/Shocked.png"
    $ DamienSmiling = "Characters/Damien/Casual/Smiling.png"
    $ DamienWorrying = "Characters/Damien/Casual/Worrying.png"
    $ coffeeflag = False
    $ damiendate = False
    $ clothes, hair = casualwear
    show chelsea at right with moveinright
    "As you get ready to leave, you remember what day it is."
    show chelsea shocked
    pcname "I was supposed to get coffee with Damien!"
    menu damiencoffee_go:
        "Go to the cafe." if True:
            show chelsea blank
            if acts == 4:
                scene bg CityE with fade
            elif acts == 2 or acts == 3:
                scene bg CityD with fade
            elif acts <= 1:
                scene bg CityN with fade
            "Pulling the address out, you enter it into your phone's GPS and start walking."
        "Stand him up." if True:
            $ corruption += 3
            show chelsea blank
            pcname "I don't really feel like it..."
            pcname "He probably forgot anyway."
            jump eventengine
    "When you arrive, you start looking around."
    show bg DatePlace with dissolve
    "Damien is sitting by himself, reading something on his phone."
    "When he notices you, though, he looks up and grins."
    D "You made it!"
    hide chelsea with dissolve
    show bg DDScene1 with dissolve
    pcname "Sorry if I'm late..."
    D "No, it's fine! Are you ready to order?"
    menu damiencoffee_order:
        "Sure!" if True:
            D "Great, let's go."
        "What do you recommend?" if True:
            $ corruption -= 3
            D "The frozen drinks are really popular, but I like the hot ones myself."
            D "Actually, the peppermint mocha is probably my favorite."
            $ damienadvice = True
    show bg DatePlace with dissolve
    show chelsea at right with moveinright
    show Damien Blank at left
    "You walk up to the counter and get in line."
    show GWaitress with dissolve
    "Barista" "So, how can we help you today?"
    menu damiencoffee_order2:
        "Macchiato." if True:
            "Barista" "Great choice!"
        "Peppermint mocha." if True:
            "Barista" "Sounds good!"
            $ pepmocha = True
        "Frozen coffee." if True:
            "Barista" "Everyone loves those!"
    "The barista takes your money and writes down your name."
    "Damien orders next and joins you at the end of the counter."
    hide GWaitress with dissolve
    if pepmocha == True:
        show Damien Neutral at left
        D "You ordered the peppermint mocha!"
        if damienadvice == True:
            show Damien Happy at left
            D "I really hope you like it..."
        elif True:
            show Damien Happy at left
            D "That's my favorite! What a coincidence..."
    show Damien Neutral at left
    D "This is one of my favorite places to come on the weekends."
    menu damiencoffee_waiting:
        "Alone?" if True:
            show Damien Sad at left
            show chelsea confused
            "He looks down."
            show chelsea sad
            D "Yeah, usually..."
        "Seems nice." if True:
            show chelsea happy
            D "It's a quiet place. And everyone's always nice here."
    show chelsea blank
    show Damien Blank at left
    "Barista" "[pcname], your drink is ready."
    show Damien Happy at left
    D "That's you!"
    hide Damien Happy with dissolve
    show GWaitress with dissolve
    "When you reach the counter, the barista calls Damien's order as well."
    show Damien Blank at left with moveinleft
    "Barista" "There you go, Damien; just the way you like it."
    show Damien Happy at left
    "She winks as she hands him the cup."
    "Barista" "I noticed that you didn't pay for both..."
    show Damien Blank at left
    "He glances at you, clearly embarrassed."
    show Damien Neutral at left
    D "Thanks, Emily..."
    show Damien Blank at left
    hide GWaitress with dissolve
    "Together, you walk back to the table and take a seat."
    if club == "track":
        pcname "Emily seems friendly!"
    elif club == "cheer":
        pcname "So, Emily seems {i}friendly{/i}..."
    elif club == "yearbook":
        pcname "Emily seemed... nice..."
    show Damien Neutral at left
    D "She is. I come here a lot, so we talk sometimes."
    menu damiencoffee_emily:
        "Ask if he likes her." if True:
            show Damien Shocked at left
            D "What? No!"
            show Damien Worry at left
            D "I mean, we're friends, but..."
            if club == "track":
                pcname "I saw her wink at you. I think she likes you!"
            elif club == "cheer":
                show chelsea happy
                pcname "I saw the wink. Are you {i}sure{/i}...?"
            elif club == "yearbook":
                pcname "She... winked at you, though."
            D "I don't--"
            "He pauses, thinking."
        "Ask if she's always so rude." if True:
            D "What?"
            if club == "track":
                pcname "She winked at you, and then asked why we paid separately."
            elif club == "cheer":
                pcname "She winked at you right in front of me!"
            elif club == "yearbook":
                pcname "She... she winked at you!"
    show chelsea blank
    show Damien Neutral at left
    D "Actually, that comment about me paying was sort of an inside joke..."
    D "She told me once that she only considers it a date if one person pays for both of them."
    show chelsea confused
    pcname "So... she was trying to figure out if we're on a date?"
    show Damien Laugh at left
    "He laughs."
    show chelsea blank
    D "Yeah, I-- I guess so."
    pcname "Sounds jealous to me."
    show Damien Happy at left
    "He shakes his head, smiling."
    D "So what do you think of your drink?"
    menu damiencoffee_feedback:
        "It's great!" if True:
            show chelsea happy
            D "I'm glad you like it."
        "It's okay..." if True:
            show Damien Neutral at left
            D "Oh..."
        "I can see why it's your favorite." if pepmocha:
            show chelsea happy
            "He grins."
            show Damien Laugh at left
            D "Isn't it the best?"
    show chelsea blank
    show Damien Blank at left
    "You sit together in silence, each waiting for the other to speak."
    show Damien Neutral at left
    D "Honestly... I wasn't sure if you were going to show up."
    show chelsea confused
    pcname "Why wouldn't I?"
    show Damien Worry at left
    D "I don't know. I thought you might have something better to do..."
    "You shake your head."
    pcname "Like what?"
    show Damien Neutral at left
    D "I don't know... Oh!"
    show chelsea blank
    "His attention is drawn by something behind you."
    "Turning, you see a trailer for a new movie called \"Space Warlord.\""
    show Damien Happy at left
    D "I really wanted to see that; looks like it comes out tomorrow."
    menu damiencoffee_movie:
        "Let's go together." if True:
            $ corruption -= 1
            show chelsea happy
            D "Really?"
            if club == "track":
                pcname "Yeah, it looks interesting!"
            elif club == "cheer":
                pcname "Why not? I don't have anything better to do..."
            elif club == "yearbook":
                show chelsea embarrassed
                pcname "I mean, if you want to..."
            show Damien Laugh at left
            "He grins."
            D "Great. So... tomorrow night, then?"
            show chelsea happy
            show Damien Happy at left
            pcname "That works for me."
            $ movieflag = True
            $ damiendate = True
        "It's not really my thing." if True:
            $ corruption += 1
            show Damien Neutral at left
            D "Oh... What kind of movies do you like?"
            menu damiencoffee_genre:
                "Horror." if True:
                    show Damien Shocked at left
                    if club == "track":

                        D "Really? I wouldn't have expected that."
                    elif club == "cheer":
                        D "Really? You're always so cheerful!"
                    elif club == "yearbook":
                        D "What? A quiet girl like you?"
                "Comedy." if True:
                    show Damien Happy at left
                    D "I like comedies too - as long as they're not too... vulgar."
                "Action." if True:
                    D "Yeah, action movies are always good."
    show Damien Blank at left
    "You chat for a while longer, sipping on your drinks."
    show Damien Neutral at left
    D "I hate to run, but I promised I'd help a friend with his computer tonight."
    pcname "Oh, that's okay; I should probably head home too."
    if movieflag == True:
        show Damien Happy at left
        D "See you tomorrow?"
        show chelsea happy
        pcname "Wouldn't miss it!"
    "Damien pauses, smiling awkwardly."
    show Damien Neutral at left
    D "Uh... Bye then."
    hide Damien Neutral with dissolve
    "He gives you a little wave and hurries out of the cafe."
    $ DamienAngry = "Characters/Damien/School Uniform/Angry.png"
    $ DamienBlank = "Characters/Damien/School Uniform/Blank.png"
    $ DamienGlare = "Characters/Damien/School Uniform/Glaring.png"
    $ DamienLaugh = "Characters/Damien/School Uniform/Laughing.png"
    $ DamienNeutral = "Characters/Damien/School Uniform/Neutral.png"
    $ DamienSad = "Characters/Damien/School Uniform/Sad.png"
    $ DamienShocked = "Characters/Damien/School Uniform/Shocked.png"
    $ DamienSmiling = "Characters/Damien/School Uniform/Smiling.png"
    $ DamienWorrying = "Characters/Damien/School Uniform/Worrying.png"
    $ damienevents += 1
    $ acts -= 2
    jump events_end_period

label damienmovie:
    $ movieflag = False
    $ clothes, hair = casualwear
    $ damiendate = False
    $ DamienAngry = "Characters/Damien/Casual/Angry.png"
    $ DamienBlank = "Characters/Damien/Casual/Blank.png"
    $ DamienGlare = "Characters/Damien/Casual/Glaring.png"
    $ DamienLaugh = "Characters/Damien/Casual/Laughing.png"
    $ DamienNeutral = "Characters/Damien/Casual/Neutral.png"
    $ DamienSad = "Characters/Damien/Casual/Sad.png"
    $ DamienShocked = "Characters/Damien/Casual/Shocked.png"
    $ DamienSmiling = "Characters/Damien/Casual/Smiling.png"
    $ DamienWorrying = "Characters/Damien/Casual/Worrying.png"
    if goingto =='textbed':
        scene bg RoomN with dissolve
        show chelsea at right with moveinright
        "As you get ready to go to bed, you feel your phone vibrate."
    elif True:
        show bg HomeE with dissolve
        "As you get ready to leave, you feel your phone vibrate."

    call screen TextingScene("Damien",
    [
        TextMessage("Really excited to see Space Warlord!"),
        TextMessage("Heading to the theater now!")
    ])

    show chelsea shocked
    pcname "I almost forgot about the movie..."
    show chelsea blank
    menu damiencoffee_go2:
        "Go to the theater." if True:
            call screen TextingScene("Damien", [TextMessage("See you there!", sender = False)])

            "Pulling the address up, you put it into your phone's GPS and start walking."
        "Stand him up." if True:
            $ corruption += 5
            pcname "I don't really feel like it..."

            call screen TextingScene("Damien",
            [
                TextMessage("Sorry I feel really sick today", sender = False),
                TextMessage("Can we reschedule?", sender = False),
                TextMessage("Of course! Feel better soon!")
            ])

            pcname "I kinda feel bad. He's such a nice guy..."
            pcname "Too late now, though!"

            jump eventengine
    show bg CityN with dissolve
    "Nearing the theater, you see Damien standing outside, waiting for you."
    show Damien Happy at left with moveinleft
    D "Hey, [pcname]..."
    "He smiles warmly."
    D "Are you ready for \"Space Warlord\"?"
    menu damienmovie_ready:
        "I've been waiting all day!" if True:
            show chelsea happy
            show Damien Laugh at left
            D "Me too!"
        "I guess so?" if True:
            show chelsea confused
            show Damien Neutral at left
            D "You guess?"
            "He laughs uncomfortably."
    show Damien Blank at left
    show chelsea blank at right
    "You follow him inside and take a look around. The theater is pretty full, but the line moves quickly."
    "When you reach the desk, the cashier looks up at you."
    show GHCMan with dissolve
    show Damien Neutral at left
    D "\"Space Warlord\" please."
    show Damien Blank at left
    "Cashier" "Are you two together?"
    menu damienmovie_together:
        "Pay for your own." if True:
            if club == "track":
                pcname "Actually, I'm paying for my own."
            elif club == "cheer":
                pcname "Nope!"
            elif club == "yearbook":
                show chelsea embarrassed
                pcname "We're not... I--"
                show Damien Neutral at left
                D "We're paying separately."
            "Cashier" "No problem; that'll be $9."
            $ Cash -= 9
        "Let Damien answer." if True:
            show Damien Neutral at left
            D "Um, I guess... Yeah, two tickets."
            show Damien Happy at left
            "He smiles shyly, glancing your way to see if you'll disagree."
            "Cashier" "That'll be $18 then."
            $ damienpays = True
    show Damien Blank at left
    show chelsea blank
    "Cashier" "Theater 12, on the left."
    show Damien Happy at left
    hide GHCMan with dissolve
    D "Mind getting us seats while I get some snacks and drinks?"
    show chelsea happy
    pcname "No problem!"
    hide Damien Happy with dissolve
    "You make your way to Theater 12 and walk inside. Despite it being premiere night, the room is only half full."
    show bg black with dissolve
    show chelsea blank
    pcname "Hope it's a good movie..."
    menu damienmovie_sit:
        "Sit in the back." if True:
            pcname "There we go. I hate it when people talk behind me."
        "Sit in the front." if True:
            pcname "The closer to the screen, the more I feel like I'm right in the middle of the action."
        "Sit in the middle." if True:
            show chelsea happy
            pcname "Best seats in the house!"
    show chelsea blank
    "You're so immersed in the previews, you barely notice when Damien joins you."
    if damienpays == True:
        show Damien Happy at left with moveinleft
        D "So, was Emily right?"
        menu damienmovie_date:
            "Huh?" if True:
                show Damien Laugh at left
                D "N-Nothing. Bad joke."
            "Yep, this is a real date." if True:
                show chelsea happy
                "He grins and passes you the popcorn."
    elif True:
        show Damien Happy at left with moveinleft
        D "Want some popcorn?"
    "Taking a handful, you nibble on it while he gets settled in his seat."
    show chelsea confused
    pcname "Doesn't seem like this is a popular movie..."
    show Damien Neutral at left
    D "It is, but there's a superhero movie opening tonight too."
    show chelsea happy
    show Damien Blank at left
    pcname "Oh, yeah, I forgot about that!"
    show Damien Neutral at left
    D "Would you rather have gone to see that?"
    menu damienmovie_othermovie:
        "Probably." if True:
            $ corruption += 3
            show chelsea blank
            show Damien Worry at left
            D "Sorry..."
        "They're overrated." if True:
            show Damien Happy at left
            D "You think so? I couldn't agree more!"
            show Damien Laugh at left
            D "\"Space Warlord\" is just as good, and I really like the dark humor. Actually--"
    show Damien Blank at left
    "He stops speaking as the lights dim."
    show Damien Neutral at left
    D "Oh, it's starting..."
    show Damien Blank at left
    show chelsea blank
    pause 1.0
    hide Damien Blank with dissolve
    hide chelsea with dissolve
    "When the opening sequence starts, you both turn your attention toward the screen."
    show bg DMS1 with dissolve
    "A few minutes in, you feel a weight settle across your shoulders; it's Damien's arm."
    "You glance his way, but his eyes are locked onto the screen. Even still, you can feel how tense he is."
    menu damienmovie_arm:
        "Shrug him off." if True:
            $ corruption += 3
            "You shake his arm off by leaning forward and shrugging."
            "Without looking your way, he lays it back on his armrest."
        "Lean against him." if True:
            $ corruption -= 5
            "Leaning toward him, you rest your head on his shoulder."
            "He relaxes against you, breathing a sigh of relief."
    "As the movie goes on, you occasionally reach over for some popcorn."
    "At some point - without you realizing it - Damien sets the popcorn aside."
    "Engrossed in the movie, you reach over - but instead of grabbing popcorn, you lay your hand on top of his thigh."
    "He jumps a little, obviously surprised by the sudden contact."
    if corruption >= 10:
        "Though it was an accident, it {i}does{/i} give you an idea..."
        menu damienmovie_handjob:
            "Give him a handjob." if True:
                $ corruption += 1
                $ damienhandjob = True
                if club == "track":
                    "Feeling frisky, you move your hand across his thigh, drawing small circles with your fingertips."
                elif club == "cheer":
                    "Slowly, you move your hand across his thigh, drawing small circles with your fingertips."
                elif club == "yearbook":
                    "Nervous but excited, you move your hand across his thigh, drawing small circles with your fingertips."
                show bg DMS2 with dissolve
                "He inhales sharply as your fingers move along his inner thigh, but you keep your eyes on the screen."
                "After a few minutes, you draw your hand higher, casually bringing it to the top of his pants."
                "There's another sharp breath as you unbutton his shorts and slowly pull the zipper down."
                if club == "track":
                    "It's exciting, doing something so bold in a theater."
                elif club == "cheer":
                    "You lick your lips, wishing there were less people around."
                elif club == "yearbook":
                    "Your heart pounds. This is terrifying - and exciting!"
                "You can feel the heat radiating from his cock, even through the shorts."
                "Your breath catches in your throat as you slide your hand inside his zipper and run it along his engorged member."
                "Slipping your hand inside his boxers, you carefully free his cock."
                "His dick pulses in your hand, hot and ready, and you feel your own body responding."
                "Still staring straight ahead, you run your hand up and down his length, smiling at his gasps of surprise and pleasure."
                "As you stroke him, you feel your nipples stiffen against your bra, and your pussy grow hot and moist with your own arousal."
                "Maybe he's inexperienced - or maybe it's because you're in public. Either way, it doesn't take long for Damien to cum."
                "Just as he's about to reach his limit, he grabs the popcorn bag and positions it in front of him."
                "Covering his mouth, he tilts his head back and stiffens."
                "You feel his cock spasm in your hand as he blows his load into the empty snack bag."
                if club == "track":
                    "Smiling, you release him and turn your attention back to the movie."
                elif club == "cheer":
                    "Pleased - but not quite satisfied - you release him and turn your attention back to the movie."
                elif club == "yearbook":
                    "Heart still pounding at your own boldness, you release him and focus on the movie."
            "Pull your hand back." if True:
                $ corruption -= 1
                show bg DMS3 with dissolve
                pcname "S-Sorry!"
                "Snatching your hand back, you cringe with embarrassment."
                D "Ah, yeah... The popcorn's empty."
                "His whispered response makes you feel a little better; at least he knew what you meant to do."
    elif True:
        show bg DMS3 with dissolve
        pcname "S-Sorry!"
        "Snatching your hand back, you cringe with embarrassment."
        D "Ah, yeah... The popcorn's empty."
        show bg DMS1 with dissolve
        "His whispered response makes you feel a little better; at least he knew what you meant to do."
    show bg black with dissolve
    show chelsea at right with dissolve
    "As the credits roll, you stand and stretch."
    show chelsea happy
    pcname "That was pretty good!"
    show Damien Happy at left
    D "And there's definitely going to be a sequel. Did you see his hand twitch at the end?"
    pcname "Yeah! There's no way he's really dead."
    "Damien walks ahead of you, tossing the empty bags into the trash can."
    D "It's pretty late, so I'll walk you home."
    pcname "That would be nice. Thanks."
    "Chatting amiably, he escorts you to your apartment."
    show bg CityN with dissolve
    show chelsea happy at right with moveinright
    show Damien Worry at left with moveinleft
    "As you approach the door, he grows uncomfortable."
    if damienhandjob == True:
        show Damien Glare at left
        D "So... About what you did..."
        if club == "track":
            "He sounds really uncomfortable."
            show chelsea sad
            pcname "You didn't like it?"
        elif club == "cheer":
            "His awkward tone makes it obvious how inexperienced he is; you can't help but giggle."
            show chelsea happy
            pcname "Did you like that?"
        elif club == "yearbook":
            "He sounds as awkward as you feel!"
            show chelsea embarrassed
            pcname "D-Did you... like it?"
        show chelsea blank
        D "I-- Of course I did, but..."
        show Damien Angry at left
        D "I just didn't think you were that kind of girl."
        menu damienmovie_confrontation:
            "I just wanted to impress you!" if True:
                show chelsea sad
                D "You-- You didn't have to do that to impress me, [pcname]."
                show Damien Glare at left
                D "I just like spending time with you."
                show Damien Worry at left
                "He looks away, blushing."
            "Girls have needs too, you know?" if True:
                D "I-- I know that! I just... Things like that should be done in private, you know?"
                show Damien Glare at left
                "He looks at the ground."
                show Damien Worry at left
                D "I guess I'm happy that you wanted to do that with me, though..."
            "What's that supposed to mean!?" if True:
                D "I thought you were a nice girl."
                if club == "track":
                    show chelsea angry
                    pcname "I {i}am{/i} a nice girl - and I thought you were a nice guy."
                    show Damien Glare at left
                    D "Nice girls don't--"
                    pcname "Don't what? Enjoy sex!?"
                    show Damien Shocked at left
                    "He turns bright red as you raise your voice."
                    show Damien Sad at left
                    D "People can hear you!"
                    pcname "You know what, forget it. I'm not here to impress you."
                    pcname "Thanks for your time, but I don't want to see you again."
                    show Damien Shocked at left
                    D "What? I just want you to have some self-respect."
                    pcname "I have some, thanks. I have enough self-respect to tell you to fuck off."
                elif club == "cheer":
                    show chelsea angry
                    pcname "I {i}am{/i} a nice girl! Who do you think you are!?"
                    show Damien Glare at left
                    D "I just meant that nice girls don't--"
                    pcname "Don't what? Get horny!?"
                    show Damien Shocked at left
                    "He turns bright red as you raise your voice."
                    D "People can hear you!"
                    pcname "You know what, forget it! I'm not even that interested in you!"
                    pcname "Honestly? I just felt bad for you!"
                    show Damien Sad at left
                    D "What? I--"
                    pcname "Yeah! I wouldn't normally waste my time with someone like {i}you{/i}."
                elif club == "yearbook":
                    show chelsea embarrassed
                    pcname "I-I am a nice girl!"
                    D "I just meant that nice girls don't... you know."
                    show chelsea sad
                    pcname "I can't believe you're being like this!"
                    pcname "It's not like you told me to stop..."
                    show Damien Glare at left
                    "He turns red."
                    D "I know, I just... I didn't realize you were going to..."
                    "Mortified, you feel tears flood your eyes."
                    pcname "I just wanted to impress you and now you hate me!"
                    show Damien Sad at left
                    D "I don't--"
                hide Damien Sad with dissolve
                hide Damien Shocked with dissolve
                "Turning on your heel, you storm into your apartment building and slam the door behind you."
                $ damientelloff = True
                jump events_end_period
    show Damien Neutral at left
    show chelsea blank
    D "Anyway, I should let you get inside."
    if damienpays == True:
        show Damien Happy at left
        D "I guess this is the part where I'm supposed to kiss you goodnight, huh?"
        show chelsea shocked
        "Before you have a chance to respond, he leans in and presses his mouth against yours."
        "His lips are warm and soft - and as you lean into the kiss, you feel your stomach flutter."
        "He pulls away from you too soon."
    D "G-Good night, then."
    show chelsea happy
    "You smile up at him."
    pcname "Good night."
    "Walking into your apartment, you glance at him one last time before closing the door."
    hide chelsea with dissolve
    hide Damien Neutral with dissolve
    hide Damien Happy with dissolve
    $ DamienAngry = "Characters/Damien/School Uniform/Angry.png"
    $ DamienBlank = "Characters/Damien/School Uniform/Blank.png"
    $ DamienGlare = "Characters/Damien/School Uniform/Glaring.png"
    $ DamienLaugh = "Characters/Damien/School Uniform/Laughing.png"
    $ DamienNeutral = "Characters/Damien/School Uniform/Neutral.png"
    $ DamienSad = "Characters/Damien/School Uniform/Sad.png"
    $ DamienShocked = "Characters/Damien/School Uniform/Shocked.png"
    $ DamienSmiling = "Characters/Damien/School Uniform/Smiling.png"
    $ DamienWorrying = "Characters/Damien/School Uniform/Worrying.png"
    $ damienevents +=1
    $ acts = 0
    show bg black with dissolve
    jump home2
    jump events_end_period
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
