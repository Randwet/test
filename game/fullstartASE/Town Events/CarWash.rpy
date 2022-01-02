label carwash02:
    show chelsea confused at right with moveinright
    "???" "[pcname]?"
    "You turn around when you hear a voice."
    show chelsea happy
    "It’s a familiar face. A young blond girl with a gorgeous figure and an easy smile. And, of course, she is dressed in her tiny bikini."
    show chelsea blank
    "It’s Joy. The woman who invited you to volunteer at a car wash."
    "Joy" "Long time no see."
    "She approaches you and tilts her head."
    show chelsea happy
    pcname "Joy, right?"
    pcname "What are you doing out here?"
    "She beams with excitement."
    "Joy" "We’re holding another car wash! After the last one went so well, we knew we needed to do it again!"
    if refusedbikini == True:
        show chelsea embarrassed
        "You can’t stop yourself from imagining last time. You’d seen the skimpy little outfit and had almost ran out. You hadn’t even seen all the other girls dressed for it."
        "The more you think back on it, the sexier the image in your mind looks. Why, exactly, had you turned her down in the first place?"
    if carwashlow == True:
        show chelsea embarrassed
        "You can’t stop yourself from remembering last time; standing around, exposed, while trying to clean the cars in as erotic a way as possible."
        "At the time, it had been hours of relentless embarrassment. But, the more you think back on it, the less onerous it seems."
        "Is your memory even correct? The thought of being exposed in front of a bunch of eager men and women actually doesn’t seem to bad."
        "Maybe you found it more enjoyable?"
    "These thoughts intrude, even as you try to focus on the conversation with Joy. She’s as excited as a puppy about the prospect of a second run at the car wash."
    show chelsea shocked
    "Joy" "Well, I have to get back. The girls need me. Ta-ta!"
    show chelsea confused
    "Joy turns to leave. Had she not believed you’d want to volunteer after what happened last time?"
    menu carchoiceo4:
        "Let her go." if True:
            show chelsea blank
            "You sigh. There’s no really no point in trying to follow. The idea of helping her today was attractive for a second. But, only a second."
            "Who would want to go and work there, knowing what it entails?"
            "You crossed your arms over your waist and shifted slightly in place."
            $ acts -=1
            jump events_end_period
        "Try the car wash again." if True:


            show chelsea blank
            "As Joy turns to walk away, you find yourself moving without even thinking."
            show chelsea happy
            pcname "Hey wait. Joy!?"
            "She turns around."
            pcname "You wouldn’t happen to have any spare uniforms this time, would you?"
            "Joy" "Of course…"
    "You exchange a look with her. It’s all it takes to get your message across. Soon, you’re on your way to the locker room to change."
    if carwashlow == True:
        jump carwashscenelow
    elif True:
        $ secondcarrun = True
        jump carwashscene


label carwash01:
    show chelsea blank at right with moveinright
    "You walk down a breezy riverside street that you’ve been exploring of late."
    show chelsea confused
    "But, there is something different today. There are more cars than usual, all lined up. Was some event going on?"
    show chelsea shocked
    "You’re so busy looking that you don’t even notice the next segment of the curve is misaligned. When you hit it, you tumble forward."
    if club == "track" or club == "cheer":
        show chelsea happy
        "Thankfully, you’re in good shape. Before you even hit the ground, you manage to catch yourself."
        show chelsea blank
    elif club == "yearbook":
        show chelsea sad
        "Too bad you aren’t athletic enough to do anything about it. There is a soft thud as your body hits the ground."
        pcname "Oof."
    "???" "Are you okay?"
    "A strawberry blond woman, dressed in a soggy towel and sandals, runs up. She guides you back to your feet with a gentle hand."
    if club == "track" or club == "cheer":
        show chelsea happy
        pcname "Totally."
    elif club == "yearbook":
        pcname "I think so…"
    "???" "I'm glad to hear it."
    "???" "But, it's a good thing I came. Hehe. You dropped something!"
    show chelsea confused
    "Your eyebrows furrow."
    show chelsea shocked
    "She produces your wallet in her hands. It must have fallen from your pocket when you fell over."
    show chelsea blank
    "You shudder at the realization that you likely would have continued on without even noticing you lost it. She saved your wallet."
    show chelsea confused
    "You look down at the towel that served as her only clothing. The river was nearby, but it is rarely used for swimming. Had she just come from a pool?"
    if club == "track":
        pcname "Why the towel?"
    elif club == "cheer":
        pcname "Interesting fashion choice?"
    elif club == "yearbook":
        show chelsea embarrassed
        pcname "I hope this isn’t a stupid question, but may I ask about the towel?"
    "The girl laughs."
    show chelsea blank
    "???" "Oh this? I’m starting a new fashion trend. Towel dresses."
    "???" "That’s a joke. Hehe. No no, me and some of the girls from my class are doing a car wash for charity. I’m on break right now."
    "???" "My name is Joy, by the way. Nice to meet you!"
    show chelsea happy
    "The next ten minutes are spent in rapt conversation. She tells you all about the charity she’s raising money for."
    if club == "track":
        "She is too bubbly for you to imagine making easy friends with. But, you owe her for helping you avoid losing your wallet, so you smile and nod with each of her anecdotes."
    elif club == "cheer":
        "The two of you chat easily. Joy is quite bubbly, and you find it easy to laugh with her about what happened."
    elif club == "yearbook":
        "Joy easily takes lead. You’re so shy, it’s a struggle to get a word in edgewise. Especially when speaking with someone so confident."
    if corruption >= 10 and corruption <= 20:
        "Every time she brushes her hair, you feel a touch of awe at Joy’s effortless beauty and grace. She carries herself like a model."
    elif corruption >= 21:
        "The entire time, you’re hyper-aware of Joy’s generous cleavage and model’s figure. Boys must have trouble keeping their eyes off her."
    elif corruption >= 21 and violetrelate == "Dom" or violetrelate == "Sub" or katerelate == "girlfriend":
        "Hell, you find it hard not to take peeks of her yourself. "
    pcname "I almost lost my wallet earlier. Is there any way I could pay you back?"
    "Joy" "Pay me back?"
    "Joy puts a finger to her lip."
    "Joy" "Well, actually…"
    "Joy" "Another friend helping out at the car wash would be great. For some reason, it ended up super popular. You could come back with me after my break is over!"
    "Joy" "But, oh, you're out walking, right? It would be so mean to ask you to do work..."
    menu carchoice01:
        "Join Her" if True:
            if club == "track":
                pcname "I didn't have plans. Of course, I’ll go back with you."
            elif club == "cheer":
                pcname "Oh, don't you worry about it. A car wash sounds fun. I'd love to help out!"
            elif club == "yearbook":
                pcname "It's okay... really. I wasn't doing anything."
                "You offer a soft smile."
                pcname "I'd actually, kind of, like to help out."
            show chelsea shocked
            "Joy grabs your hands so fast that you don’t have time to react."
            "Joy" "Eeeek. This is exciting! My break is right about to end. Come with me."
            show chelsea happy
            "Without another word, she starts to take off to the car wash, leaving you chuckling and following along in her wake."
        "Refuse" if True:

            show chelsea blank
            pcname "I don’t think I can today. Sorry."
            "As thankful as you are, you’re more anxious to get back home."
            "For her part, Joy seems to recognize this with a nod. You don’t catch a hint of bitterness for being turned down as she waves you off."
            jump events_end_period
    show bg black with dissolve
    hide chelsea
    pause 0.5
    show bg CityD with dissolve
    show chelsea blank
    "Joy takes you straight to the inside office of the building they’re using. You briefly spot the line of cars focused out front as you pass."
    "You also can’t help but marvel at the massive jar of cash where the co-eds are dropping their earnings."
    if corruption >= 40:
        show chelsea happy
        "Seeing so much money in one place makes you wonder if they’d notice a tiny bit missing…"
    show chelsea blank
    "Next, she leads you into an empty changing room."
    "Joy" "And here is where we are keeping the spare uniforms..."
    "She skips off to a large cabinet filled with bathing suits. You crane your neck to see them."
    if club == "track" or club == "cheer":
        show chelsea confused
        pcname "Uniforms?"
        show chelsea blank
    elif club == "yearbook":
        show chelsea embarrassed
        pcname "U-uniforms?"
    "To answer your question, she drops her towel to the ground. Underneath, she is wearing almost nothing. Only a skimpy bathing suit, little better than nudity."
    "It was an itsy bitsy teenie weenie yellow polka dot bikini."
    if corruption >=21:
        "Your eyes bathe in her perfect curves and sculpted figure. What you wouldn’t do to touch her..."
    elif corruption <= 20:
        "You instinctively cover your chest. Who wouldn’t feel inadequate when staring at that?"
    "Joy" "Hrmm. And your size is probably…"
    "She returns her focus to the cabinet."
    "With a squeal, she pulls a suit out for you. An identically designed suit that would barely even cover your nipples."
    "Joy" "So? What do you think?"
    "She giggles to herself."
    if corruption >=21:
        show chelsea shocked
        pcname "It’s so small!"
    elif corruption <= 20:
        pcname "It’s so small..."
    show chelsea embarrassed
    "Joy" "Of course, silly. How do you think we made so much today? We’ve got men coming from miles away!"
    "Joy" "So…?"
    menu carchoice02:
        "I won't wear this." if True:
            show chelsea blank
            if club == "track":
                if corruption <= 20:
                    pcname "Not happening. That thing is worse than being naked."
                elif corruption >=20:
                    pcname "I‘m not in the mood to wear something like that. Thank you for the help earlier, but my answer is no."
                "You put your hands on your hips."
            elif club == "cheer":
                if corruption <= 20:
                    pcname "No way! It’s so tiny. I can’t wear that."
                    "You continue to hide your breasts in your arms."
                elif corruption >=21:
                    "You put a finger to your lips. You imagine men turning their heads at the sight of you in it."
                    "Still, someone from school might see me! Nope nope. Can’t do it."
            elif club == "yearbook":
                if corruption <= 20:
                    show chelsea shocked
                    pcname "N-no way...People would see me."
                    show chelsea embarrassed
                    pcname "Your hands go to your face to hide your burning cheeks."
                elif corruption >=21:
                    show chelsea shocked
                    pcname "...I can’t do that. Everyone would see me…"
                    show chelsea embarrassed
                    "You struggle to stand still. Embarrassment and need duel within you, but the former wins out."
            "Joy" "Are you sure? It’s all for a good cause. And I bet you’d look cute in it too."
            "She giggles and waves the microkini again."
            menu carchoice03:
                "Refuse" if True:
                    show chelsea blank
                    if club == "track":
                        pcname "Nope. Not going to do it."
                    elif club == "cheer":
                        pcname "Sorry. Not today, honey."
                    elif club == "yearbook":
                        pcname "I can’t…"
                    "Joy pauses. For a second, you think you broke her. Then, only missing a beat, she puts the outfit back."
                    "Soon, she’s giggling and joking like you hadn’t stood her up."
                    "You and Joy talk playfully for another few minutes until her shift starts. After that, you start on the trail back home."
                    if corruption <= 25:
                        "You look back at the car wash, where the skimpy dressed girls are dancing and scrubbing cars. Your cheeks flush red."
                    elif corruption > 25:
                        "You look back at the car wash, where the skimpily dressed girls are dancing and scrubbing cars. Maybe it would have been fun…"
                    $ refusedbikini = True
                    jump events_end_period
                "Change your mind" if True:



                    jump puton
        "I'll put it on." if True:



            pass

label puton:
    if club == "track":
        if corruption <=15:
            pcname "Tsk."
            pcname "I'll do it. Give it here."
        elif corruption >= 16 and corruption <=30:
            pcname "Pretty revealing, huh? Alright, it looks fun."
        elif corruption >= 31:
            pcname "Make some money for charity and look sexy doing it? I’m in."
    elif club == "cheer":
        if corruption <=15:
            pcname "It is kind of cute…"
        elif corruption >= 16 and corruption <=30:
            pcname "Not a lot of fabric, huh? Alright. Let’s do this."
        elif corruption >= 31:
            pcname "In something like this, the boys will probably be drooling. I love it. Totally love it."
    elif club == "yearbook":
        if corruption <=30:
            show chelsea embarrassed
            "Your cheeks burn. How could you possibly wear something so humiliating? Yet, somehow the prospect of disappointing her seems even worse..."
        if corruption >= 16 and corruption <=30:
            show chelsea embarrassed
            "...Besides, being exposed in an outfit like that could be hot..."
        elif corruption >= 31:
            show chelsea embarrassed
            pcname "I’d be so exposed..."
            "Even as you say it, your hands reach out to take it. Heat rises from your cheeks...but also between your legs..."
    show chelsea blank
    "Joy places the outfit into your hands. For half a second, you think you see her smirk."
    show chelsea happy
    "Joy" "I bet you’ll look so cute in it! See you outside [pcname]!"

label carwashscenelow:
    hide chelsea at right
    show bg black with dissolve
    pause 1.5
    "It is a bright sunny day out, and nearly thirty young women are out in front of a store dressed in the skimpiest swimwear."
    "Some are engaged in scrubbing or hosing down the line of cars as provocatively as possible. With some rare exceptions, the customers are mostly male."
    "Others are just having a good time. Spraying water at each other, messing with speakers, or even passing around a beach ball."
    "A Def Leppard song screeches dramatically over the entire proceedings."
    "The men stare, ogle, and drool to their heart's content. They’re paying for the show."
    "And this entire time, you are..."
    if corruption <=20:
        $ carwashlow = True
        scene bg CarWash2 with dissolve
        "...Standing around awkwardly with bright red cheeks and your arms covering whatever shred of modesty they can manage to hold on to."
        "All the other girls happily flaunt their bodies, but you can’t shake the feeling of constantly being watched. The bikini hides nothing."
        if club == "track":
            pcname "It’s just washing cars. I can do this."
        elif club == "cheer":
            pcname "Everyone else looks like they’re having fun…"
        elif club == "yearbook":
            pcname "I made a mistake..."
        "Next to you, a well-endowed girl is washing the hood of a car while flaunting for a man in the driver’s seat."
        "None of this can be real. Most of these girls have to be play-acting. The men come here for a performance."
        "The idea of it gives you a strange shiver."
        "You barely even notice as a red car pulls into the spot assigned to you. Inside are a pair of college guys in football caps."
        "All you can do is stare at it. The car itself is already so clean; they can’t have come for much of a practical purpose. But, you’re still frozen in place."
        "Reality returns to you in the form of a sudden hand on your shoulder."
        "Joy" "You gotta clean it, silly."
        "Joy" "Give ‘em a little show. That’s how you make them happy."
        "There is no escaping it now. All you can do is lean over carefully, all of your efforts redirected to just keeping everything in your top."
        "Music" "~Pour some sugar on meeeeeeee!~"
        "Music" "~In the name of love!~"
        "Washing the car proves challenging. You make a show of getting into a posture where you’re draped over their car."
        "But, your top is so unwieldy that your nipples keep brushing against the hood of the car. Soap is getting everywhere, making your skin feel slippery."
        "The men expect it, so it’s not like you stop. In fact, you almost start to feel something exciting about it. They’re treating you like a sex object, so you should be mad. But yet…"
        if club == "track" or club == "yearbook":
            "The longer you’re watched, the more powerful you feel their glances."
        elif club == "cheer":
            "The more you start to like the feeling of drawing so much attention. It’s almost like you’re teasing them."
            "You scrub with determination, getting the few spots out of the car. You even continue after the car’s all clean just to give the voyeurs the show they want."
            "Even when that car is gone, another takes its place. Then another after that."
            "Your blush doesn’t recede. But, the odd pleasurable feeling continues too. It centers wherever your nipples brush against the car. "
            "At one point, two girls with dyed hair walk by and turn their noses up at you."
        if club == "track" or club == "yearbook":
            "You can’t help but empathize. If you’d seen girls debasing themselves this way, would you be able to stop yourself from judging?"
        elif club == "cheer":
            "It makes you glare. Do they actually think they’re better than you just because they’re wearing pants and you’re not?"
        "Music" "~A little bit of Tina is what I see~!"
        "Two of the girls make a show of throwing buckets of water at each other. You finish one car just in time to get a bucket full to the face."
        if club == "track" or club == "cheer":
            pcname "Hey!"
        elif club == "yearbook":
            pcname "Hey..."
        "On a brief towel break, your head swirls with mixed emotions."
        "Anger, embarrassment, burning humiliation...an increasing awareness of just how tight the bikini is pressing against your body. Of how stiff your nipples are getting."
        if club == "track":
            "All of it feeds your fire. When the break ends, you throw yourself at the cars with new vigor."
            "You have to perform some male fantasy for these guys? Fine. You’re going to be the best damn performer in this place. You’re going to make them all stare."
        elif club == "cheer":
            "You return to the task light-headed. It’s not the stimulation itself. Something else is having an effect on you. Your entire body is starting to feel hot now..."
            "All you can do is emulate the other girls and the way they smile and giggle for each patron. They like all the other girls so much. You want to make them like you, too."
        elif club == "yearbook":
            "You can do this...you can do this…"
            "Trying not to shake, you take your place in another (hopefully) provocative pose on the hood of a car. Your entire body feels flushed now."
            "All you can think about is the stares. Are you really the sex object that they must be seeing?"
        "No sooner, though, do you get back into action does disaster strike. The cord of your bikini falls undone."
        pcname "Eeep!"
        "You’re forced to press your chest hard against the car to prevent giving an accidental topless show. "
        "The damn thing had been getting loose all day. It was as though it was designed to have wardrobe malfunctions. Maybe that was the point?"
        "The guy in the car actually covers his eyes, seemingly as embarrassed as you are."
        "But even at this moment, the funny feeling between your legs continues to grow."
        show bg CityD with dissolve
        "Hours later, you stumble back towards your house, back in your normal clothes. You’re tired, dazed, and have enough soap in your hair to run three dishwashers."
        "Yet, there’s only one feeling you’re able to focus on. The memory of being so exposed in front of all of those hungry eyes."
        if club == "track":
            pcname "That was actually fun."
        elif club == "cheer":
            pcname "Did...Did they like me?"
        elif club == "yearbook":
            pcname "...Maybe being seen can be fun."
            pcname "Sometimes..."
        $ corruption += 5
        $ acts -= 1
        jump events_end_period


if corruption >= 21:
    label carwashscene:
        $ firstcarrun = True
        scene bg CarWash1 with dissolve
        "...Getting into it too. You’re laughing and wiggling your ass for all the watching men as naturally as the other girls."
        if secondcarrun == True:
            label secondrun:
                "You’re soon back in front of the building in the familiar bikini. It remains as comically revealing as your prior experience with it."
                "In fact, most of the scene is the same. The girls are back out in force playing and showing off more than washing cars. Naturally, the same eager line of cars has come to join the fun."
                "In fact, the only real difference is that the speakers aren’t playing the same Def Leppard song."
                "Music" "~I don't wanna know your name. 'Cause you don't look the same. The way you did before.~"
                "Well, there is one other point of difference. Before, you’d been blushing dark red and trying to hide whatever shred of modesty you had left."
                "But, walking to join the other girls today, your steps are easier. More than that. You’re positively eager."
        "While you get into position, a pair of nearby girls have a fight with water hoses using the car as a shield."
        if firstcarrun == True:
            "This is all a performance. Would any of this be done if you didn’t have an audience? If that audience didn’t have an image of a sexy car wash in their head?"
            "But, you do have an audience."
            if club == "track":
                "...And if you have to perform, then you’re going to be the best at it. You give a confident smirk."
            elif club == "cheer":
                "…And sometimes being noticed is fun."
            elif club == "yearbook":
                "...You just hope you’re good enough at it."
        "Already, you notice a man trying not to be seen gawking at your nearly nude body from the sidewalk."
        "You feel a familiar flush in your cheeks, and an eager ache starts to form between your legs."
        "But, before you can spend any more thought to your current display predicament, a red car pulls up in front of you."
        "It’s time. You bend low over the hood slowly, only inches from the surface. In the process, the driver gets an easy view of your rear."
        "You try your best to wiggle your ass side to side to the same tempo that you swirl the rag in a circle."
        if firstcarrun == True:
            "The car is not especially dirty, but odds are they’re not here out of an excess of concern for keeping a spotless vehicle."
        "From the corner of your eyes, you see the driver peak back at you. It’s an older looking woman with her trained eye on your every move."
        "As much as you try to focus on washing her car, you’re much more concerned with her state. Everywhere her eyes touch feels like it’s under a magnifying glass."
        "You even think you see the man in a neighboring car ogling you too."
        if club == "track":
            "A bright smile forms on your face. You’re just as good as all of the other car wash girls. Maybe even better."
        elif club == "cheer":
            "But then, how could they resist when you’re being so sexy? You let out a giggle and give your ass a little shake for your new fans."
        elif club == "yearbook":
            "Your head spins with emotions."
            "Every pair of eyes is overwhelming and draws your mind back to how exposed you are. Yet, you want more. More people staring. It leaves your knee quaking, ready to give in at any moment."
"When you finish her car, another comes to replace it. This time, an older man whose eyes hide behind sunglasses."
"Before you lean down to start work on his car, you look to some of the other girls. A few are boldly shaking their asses and bodies for the patrons to tease them."
"Maybe you can go further?"
"This time, when you lean over the car, you don’t leave the inches of space. Instead, you press your breasts down at the soapy water and slosh them around as though they were sponges."
pcname "This one is going to need a real deep clean."
"The man doesn’t shift his posture. Without being able to see his eyes, it’s almost like stripping in a darkened room. You feel exposed."
if firstcarrun == True:
    "Music" "~Pour some sugar on meeeeeeee!~"
    "Music" "~In the name of love!~"
if secondcarrun == True:
    "Music" "~You just want attention, you don't want my heart. Maybe you just hate the thought of me with someone new.~"
"You bring your focus to your breasts, using your hands to guide them and press them harder."
"It starts to feel good. After all, your nipples had stiffened awhile ago, and now you are just rubbing them against a surface shamelessly."
"You swirl them around and around, as though trying to hypnotize anyone who is watching."
"A cheeky giggle calls out from behind you."
"Joy" "I think that one is done."
"You blink. The hood is already clean, and the man is paying an approaching attendant. You had been so into it that you hadn’t even realized."
"All you’d been able to focus on was the way your body was growing hotter and hotter. You lick your lips and wait for the next customer."
"The next few hours slip away, as though in a trance. One car after another shows up, and you throw yourself at cleaning them. Sometimes literally."
"The wet atmosphere and the watching eyes make it easy to lose focus on anything besides that."
if club == "track":
    "Whenever you finish a car, you throw your rag over your shoulder to admire your handiwork. Though, in that pose, you’re often the one being admired."
elif club == "cheer":
    "You quickly form a habit of finishing every job by blowing the customer a little kiss."
elif club == "yearbook":
    "Without even thinking about it, you often stand in attention when you finish one car. Every time their eyes drift low to your naked skin, it makes you squirm."
"At one point, Joy even stops in to wash a car together with you with a bright smile on her face."
"Though, rather than doing much washing, she ends up spending half the time shooting you with a hose in an effort to knock your top off."
if club == "track":
    "In the end, you’re the one who manages to knock hers off with a well timed spray of water."
elif club == "cheer":
    "By the time it’s done, you’re both laughing and have had to re-adjust your bikini a few times to avoid it becoming undone."
elif club == "yearbook":
    "It makes you squeak and try to shield your bosom."
if corruption >= 25:
    if club == "track":
        "You spend the entire day openly flaunting your body. It feels good to be watched, so why not indulge?"
        "At one point, a customer asks politely if he could see underneath the suit. By this point, you’re aroused enough to agree."
        "For a brief flash, you flip your top off to give him a look. You probably enjoy it more than he did."
        "Every so often, your hand traces between your legs. You come very close to just walking off so you can fuck yourself already."
    elif club == "cheer":
        "The longer the day goes on, the more into the persona you fall. Whenever someone new approaches, you bounce in place to give the voyeurs a little jiggle."
        "It all becomes a blur of flirting and rubbing. You even continue searching for new and more provocative ways to clean the cars. At one point, you wipe down a windshield with your ass."
        "A few times, your top falls off due to wardrobe malfunctions. It’s not always as much of an accident as it seems."
        "Eventually, all of this leaves you so worked up. You’re left half-wishing you’d be allowed to give some of the customers a more personal cleaning."
    elif club == "yearbook":
        "As the day goes on, your thoughts grow sluggish under the weight of your mounting shame and need. You look like a slut. You feel like a slut."
        "You want more. At a few moments, you consider taking your top off, just so the voyeurs can see you, but always chicken out at the last moment."
        "Eventually, your pussy reaches the point of aching. You blush hard at the though of just shoving your fingers into the bikini bottoms and fucking yourself in front of everyone."
"The hours drag on. You actually end up staying longer than you’d initially told Joy."
"As the sun sets, a fancy black car rolls into your lot. Inside is a sleek young professional in a tailored suit."
"Wealthy Man" "Ya know, doll, I’ve been watching you. You’re really into this."
"Wealthy Man" "How’d you like to earn a special tip? You know, something that no one gotta tell the charity about."
pcname "Go on?"
"Wealthy Man" "Well, you seem real worked up. Bet ya got a lot of unreleased...tension."
"Wealthy Man" "I just bought this beauty. Aston Martin. She needs a warm welcome. How about you work off some of your frustrations on her? "
"Wealth Man" "With all you girls shaking your asses, I bet no one would even notice if ya put a little more hip into it."
"Comprehension dawns on you."
if club == "track":
    pcname "You want me to fuck myself using your car?"
elif club == "cheer":
    pcname "Oh. I get it. You want me to put on a private show for you using your car?"
elif club == "yearbook":
    pcname "You mean, you want me to do...well you know, using your car?"
"Wealthy Man" "And get rewarded for it nicely. I’ll pay you $200."
if club == "track" or club == "yearbook":
    menu carchoice05:
        "Accept his Offer" if corruption >=40:
            $ acceptcaroffer = True
            show bg black with dissolve
            jump acceptcaroffer
        "No Way!" if True:

            $ acceptcaroffer = False
            pass
elif club == "cheer":
    menu carchoice06:
        "Accept his Offer" if corruption >=35:
            $ acceptcaroffer = True
            show bg black with dissolve
            jump acceptcaroffer
        "No Way!" if True:

            $ acceptcaroffer = False
            pass
if club == "track":
    pcname "Fuck no. Get out of here."
elif club == "cheer":
    pcname "Ew. No. I didn’t sign up for that."
elif club == "yearbook":
    pcname "...I don’t think I could do that…"
"Wealthy Man" "Hmph."
"Wealthy Man" "Bitch."
"The car squeals as he sets the wheels in motion. You jump back slightly in surprise as it zooms out."
"You mess up your hair and sigh. Another car is already coming into the spot. One of your last for the day."
jump endwash
label acceptcaroffer:
    "You bite your lip, but don’t say a word."
    "Instead, you move to mount the sports car. The businessman offers an evil smirk."
if club == "track":
    "A dark grin forms on your face. It’s so naughty. But, you’d been considering something like this all day. Why not indulge?"
elif club == "cheer":
    "A high pitched giggle escapes your lips. You are worked up, after all. Why not find a little relief…?"
elif club == "yearbook":
    "You have to fight the urge to cover your face with your hands. Doing something like this in public…"
"The smooth angular surface of the sports car makes it easy to find an open ridge to press between your legs."
"When settled in position, you rock your hips. Your hands pretend to wash the hood so as to appear to be working."
show bg CarWash3 with dissolve
pcname "Ooooh."
"You grind slowly at first, savoring the pressure against your aching clit. It felt like masturbating after being teased for an entire day."
"Soapy water from the rag drifts down, brushing against your legs."
"It’s late enough now that the crowd has thinned out. All of the spots are still full enough to keep the other girls busy, but there are fewer observers now."
if club == "track":
    "You focus in on your own pleasure. The rhythm of your hips speeds up, shamelessly trying to eke out as much friction as you can from the car."
    "Your breath comes out hot. All you can focus on is your own pleasure. Your own need."
elif club == "cheer":
    "The pace of your hips speeds up. You also make a point of wiggling your body and letting out small theatrical moans as close to the window as you can."
    pcname "Mmm. You like this?"
    "Your fingers cascade through your hair, running all the way down before moving to your sides. "
    pcname "Am I a good girl?"
    "Wealthy Man" "Mhm. You are. You’re a good girl."
    "You let out a little gasp. Beneath it, you’re smiling."
elif club == "yearbook":
    "You lower your face to hide it from his stare. But, your hips only move faster and faster. Under his supervision, controlling your body starts to feel impossible."
"The longer it goes on, the harder it becomes to stop. Your hips move as though possessed."
if club == "cheer":
    "Soon, you’re not even performing anymore. You’re so worked up that you’re genuinely fucking yourself on his car."
elif club == "yearbook":
    "Soft whimpering escapes your lips. You’ve long since stopped performing. Now it’s your need to cum that drives you."
"At one point, you start moving so hard that you think you see the girl at the neighboring station turn her head. After that, you slow down slightly."
"But, that can’t slow you down for long. Soon, you’ve worked all the way up to the point where you’re furiously grinding into the car."
"You feel the edge drawing closer with every ounce of pressure on your clit."
"The ability to hold back leaves your body. The need to cum controls you."
"Your body jerks. You bring a hand to your mouth to silence any cries. Then, an orgasm rips through your body."
"You slump down, trying to catch your breath. Your forehead almost bumps against the car’s steel. "
"Your shaking hands try to move the rag, to make it look like you’re leaning in to scrub, but you can barely manage the effort."
"In the driver’s seat, the man just claps."
if club == "track":
    pcname "Fuck…"
elif club == "cheer":
    pcname "Holy..."
elif club == "yearbook":
    pcname "..."
label endwash:
show bg CityD with dissolve
"It’s late by the time you’re making your way back. Your mind keeps drifting back to the way all those people looked at you."
if acceptcaroffer == False:
    "The ache between your legs lingers. When you make it back home, the first thing that has to happen is some release."
"Joy said you made the charity hundreds of dollars. Her praise had made you glow. You really had gone all out."
"Your eyes turn back. In the distance, you see Joy take down the Car Wash’s sign."
if club == "track" or club == "cheer":
    "You grin."
elif club == "yearbook":
    pcname "You blush."
if acceptcaroffer == True:
    "In your pocket, you wrap your hand around a roll of bills in a rubber band."
    $ corruption += 8
    $ Cash += 200
    "You gained $200!"
$ acts -= 1
jump events_end_period
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
