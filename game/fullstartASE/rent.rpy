






default rentdue = False
default rent = 600
default firstrent = True
default missedrent = False
default dayofmonth = 1
default month = "January"
default catrent = False

label calendarcompute:
    $ dayofmonth += 1
    if month == "December":
        if dayofmonth > 31:
            $ month = "January"
            $ dayofmonth = 1
    elif month == "November":
        if dayofmonth > 30:
            $ month = "December"
            $ dayofmonth = 1
    elif month == "October":
        if dayofmonth > 31:
            $ month = "November"
            $ dayofmonth = 1
    elif month == "September":
        if dayofmonth > 30:
            $ month = "October"
            $ dayofmonth = 1
    elif month == "August":
        if dayofmonth > 31:
            $ month = "September"
            $ dayofmonth = 1
    elif month == "July":
        if dayofmonth > 31:
            $ month = "August"
            $ dayofmonth = 1
    elif month == "June":
        if dayofmonth > 30:
            $ month = "July"
            $ dayofmonth = 1
    elif month == "May":
        if dayofmonth > 31:
            $ month = "June"
            $ dayofmonth = 1
    elif month == "April":
        if dayofmonth > 30:
            $ month = "May"
            $ dayofmonth = 1
    elif month == "March":
        if dayofmonth > 31:
            $ month = "April"
            $ dayofmonth = 1
    elif month == "February":
        if dayofmonth > 28:
            $ month = "March"
            $ dayofmonth = 1
    elif month == "January":
        if dayofmonth > 31:
            $ month = "February"
            $ dayofmonth = 1
    if dayofmonth == 1:
        $ rentdue = True
    return

label payrent:
    $ rentdue = False
    if Cash > rent and catrent == True:
        jump landlordcat
    if firstrent:
        $ firstrent = False
        "A sudden knock on your door startles you from your bed."
        "You throw some clothes on in a hurry, wondering who it could be."
        $ clothes, hair = casualwear
        show chelsea blank at right with moveinright
        pcname "Did someone text me?"
        show chelsea confused
        "Grabbing your phone, you check your notifications."
        show chelsea blank
        pcname "No messages..."
        "Your eyes settle on the date."
        show chelsea shocked
        pcname "It's the 1st! Rent's due!"
        "Hurrying through the living room, you open the front door."
        show bg HomeE with dissolve
        show LL Happy at left with moveinleft
        "Landlord" "Hello again, [pcname]. I hope I didn't wake you?"
        show chelsea happy
        pcname "Not at all!"
        "Landlord" "Great. I just stopped by to pick up rent."
        pcname "Right!"
        if Cash < rent:
            show chelsea sad
            pcname "Right..."
            show LL Serious
            "Landlord" "Is there a problem?"
            if club == "track":
                show chelsea embarrassed
                pcname "It's just that... I don't actually have it."
            elif club == "cheer":
                show chelsea embarrassed
                pcname "I... Sorta don't have it?"
            elif club == "yearbook":
                show chelsea sad
                pcname "I... I don't..."
                pcname "I don't have enough money..."
            show LL Blank
            "His smile melts away immediately."
            show LL Serious
            "Landlord" "This doesn't make a good impression, [pcname]. It's only been one month and you already can't afford rent?"
            jump notpayrent
        elif True:
            "You hand him an envelope."
            show chelsea happy
            pcname "There you go!"
            show LL Blank
            "He thumbs through the bills, counting silently."
            show chelsea blank
            show LL Happy
            "Landlord" "All set then. Everything okay here? Is there anything you need?"
            if club == "track":
                pcname "I mean, a personal gym would be nice."
                "He laughs."
                "Landlord" "Keep dreaming big!"
            elif club == "cheer":
                show chelsea happy
                pcname "Any plans to install a walk-in closet?"
                "He laughs."
                "Landlord" "I don't think so, sweetheart."
            elif club == "yearbook":
                show chelsea embarrassed
                pcname "N-no, everything is fine..."
                "He smiles."
                "Landlord" "Glad to hear it."
            "Landlord" "Well, I have more apartments to visit. I'll see you again next month, okay?"
            show chelsea happy
            pcname "See you then!"
            hide LL Happy with moveoutleft
    elif True:
        $ rentscene = renpy.random.randint(1,3)
        if rentscene == 1:
            "Getting out of bed, you start dressing for the day."
            "As you finish brushing your hair, you hear a knock on the door."
            $ clothes, hair = casualwear
            show chelsea blank at right with moveinright
            pcname "Coming!"
            "You open the door a crack, peaking outside."
            show LL Happy at left with moveinleft
            "Landlord" "Hi, [pcname]. Just stopping by for your rent."
            show chelsea happy
            pcname "Right! Come in!"
            "You open the door and step back. He takes a step just inside the door and smiles."
            show LL Neutral
            "Landlord" "Anything not working?"
            show LL Blank
            if club == "track":
                pcname "Nope; everything's fine!"
            elif club == "cheer":
                pcname "Not so far!"
            elif club == "yearbook":
                show chelsea blank
                "You glance around the room."
                pcname "No, I don't think so..."
            "He smiles."
            show LL Happy
            "Landlord" "Great. I'll just collect rent and be on my way then."
            if Cash < rent:
                show chelsea blank
                pcname "Right..."
                show LL Serious
                "Landlord" "Is there a problem?"
                if club == "track":
                    show chelsea embarrassed
                    pcname "It's just that... I don't actually have it."
                elif club == "cheer":
                    show chelsea embarrassed
                    pcname "I... Sorta don't have it?"
                elif club == "yearbook":
                    show chelsea sad
                    pcname "I... I don't..."
                    pcname "I don't have enough money..."
                "His smile melts away immediately."
                "Landlord" "Well that {i}is{/i} a problem..."
                jump notpayrent
            elif True:
                "Producing the normal envelope, you hand it to him with a smile."
                show chelsea happy
                "Landlord" "Let me just check it... Yep, all there."
                "He tucks the envelope away, giving you a nod."
                "Landlord" "Until next month then."
                hide LL Happy with moveoutleft
        elif rentscene == 2:
            $ clothes, hair = casualwear
            show chelsea blank
            show chelsea at right with moveinright
            "You consider staying in bed a little longer, until you realize what day it is."
            pcname "The landlord will be by for rent soon."
            if Cash < rent:
                "You check your cash."
                show chelsea shocked
                if club == "track":
                    pcname "Shit... I don't have enough!"
                elif club == "cheer":
                    pcname "Oh no... No, no, no... What am I going to do?"
                elif club == "yearbook":
                    "You count it three times before it really sinks in; you can't pay your rent."
                "The dread settling in your stomach jumps into your throat when you hear a familiar knock on the door."
                "You open the door slowly."
                show LL Happy at left with moveinleft
                show chelsea sad
                "Landlord" "Hey, [pcname], just stopping by for your rent."
                "Seeing the look on your face, he looks concerned."
                show LL Neutral
                "Landlord" "Is everything okay?"
                if club == "track":
                    pcname "I... don't have rent."
                elif club == "cheer":
                    pcname "I... don't really have enough for rent this month."
                elif club == "yearbook":
                    pcname "I... I can't..."
                    pcname "I can't pay it..."
                show LL Blank
                "He sighs."
                show LL Serious
                jump notpayrent
            elif True:
                "By the time he arrives, you're dressed and waiting by the door, envelope in hand."
                "As soon as he knocks, you open the door and hold out the envelope."
                show LL Happy at left with moveinleft
                "He takes it, grinning."
                "Landlord" "Wow, you're really ready for me, huh?"
                "He counts it quickly and pockets the envelope."
                "Landlord" "No problems?"
                show chelsea happy
                if club == "track":
                    pcname "Still waiting on that gym."
                    "He laughs, shaking his head."
                elif club == "cheer":
                    pcname "Other than the closet?"
                    "He laughs, shaking his head."
                elif club == "yearbook":
                    pcname "No, everything is good."
                "Landlord" "Just give me a call if you need something then."
                hide LL Happy with moveoutleft
        elif True:
            $ clothes, hair = casualwear
            show chelsea blank at right with moveinright
            "You get dressed and walk into the living room, ready to start your day."
            show chelsea confused
            "Grabbing a muffin, you sit down for breakfast when you hear a knock on the door."
            "Muffin in hand, you unlock the door and open it a crack."
            show chelsea blank
            show LL Happy at left with moveinleft
            "Landlord" "Good morning, [pcname]. I'm here for rent."
            if Cash < rent:
                show chelsea shocked
                "A cold dread washes over you. Is rent due already?"
                "Swinging the door open, you let him inside."
                "Landlord" "Any problems?"
                show chelsea sad
                if club == "track":
                    pcname "Well, just one..."
                elif club == "cheer":
                    pcname "I guess you could say that..."
                elif club == "yearbook":
                    pcname "K-kind of..."
                show LL Serious
                "Landlord" "You should've called me! What's not working?"
                pcname "Nothing! I just... don't have rent."
                "His face darkens, concern turning quickly to disappointment."
                jump notpayrent
            elif True:
                show chelsea happy
                "Smiling, you swing the door open and motion for him to come in."
                pcname "I forgot it was rent day! Let me grab it for you."
                hide LL Happy with dissolve
                "Setting the muffin on the table, you duck into your bedroom and grab the envelope."
                show LL Happy at left with dissolve
                if club == "track":
                    "You wave it in the air."
                    pcname "Here you go!"
                elif club == "cheer":
                    "You present it with a flourish."
                    pcname "Here it is!"
                elif club == "yearbook":
                    "You hold it out, smiling up at him."
                    pcname "Here..."
                "Taking the envelope, he counts the cash and quickly tucks it away."
                "Landlord" "Sorry to interrupt your breakfast. No problems around the apartment?"
                pcname "Everything is good here!"
                "Landlord" "All right then, I guess I'll see you next month."
                hide LL Happy with moveoutleft
    "The door clicks shut behind him."
    $ Cash = Cash - rent
    return

label landlordcat:
    $ catrent = False
    show bg HomeE with dissolve
    show chelsea happy at right with moveinright
    "You start your day by dressing and getting [kittenname] his breakfast."
    show chelsea blank
    "While he's eating, you look around the kitchen trying to decide what you want."
    "As you close the cupboard, you hear a knock at your door."
    show chelsea confused
    pcname "Who could that be?"
    "Cracking the door open, you see your landlord outside."
    show LL Happy at left with moveinleft
    "Landlord" "Good morning, [pcname]. I'm here for rent."
    show chelsea shocked
    "Glancing nervously behind you, you see [kittenname] still eating his breakfast."
    show chelsea embarrassed
    pcname "Oh, right..."
    show LL Neutral
    "Landlord" "Can I come in?"
    if club == "track":
        pcname "Yeah, yeah, of course..."
    elif club == "cheer":
        pcname "Oh, um, sure..."
    elif club == "yearbook":
        pcname "Uh, y-yes..."
    "You step back, allowing him in."
    show LL Happy
    "He looks around the room, but doesn't seem to notice the cat."
    "Landlord" "Do you have your rent ready?"
    show chelsea shocked
    pcname "It's in the bedroom. Be right back!"
    hide LL Happy with dissolve
    show bg RoomE with dissolve
    "You hurry into the bedroom and grab the envelope. You can feel yourself starting to sweat with nervousness."
    show bg HomeE with dissolve
    "When you step back into the living room, your heart drops. [kittenname] is weaving between the landlord's legs, rubbing against them."
    show LL Happy at left with dissolve
    "Landlord" "And who is this?"
    if club == "track":
        show chelsea happy
        pcname "That's [kittenname]. He was a stray kitten and I was going to find him a new home, but..."
    elif club == "cheer":
        show chelsea happy
        pcname "Isn't he the cutest? His name is [kittenname]. I found him living outside and just couldn't bear the thought of what might happen to him..."
    elif club == "yearbook":
        show chelsea sad
        pcname "T-that's [kittenname]. I... I found him and..."
    show LL Serious
    "Landlord" "He's adorable, but you know we don't allow pets."
    show chelsea sad
    show LL Blank
    "You bite your lip, your heart breaking. Maybe he'll give you time to rehome him?"
    pcname "I understand. He's a really good cat, though. He hasn't messed up any of the furniture or anything."
    pcname "If I could have a little time, I'm sure I could--"
    "He holds up a hand."
    show LL Serious
    "Landlord" "Let me take a look around and see if he's caused any damage."
    hide LL Serious with moveoutleft
    "You nod, heart pounding. What if he makes you pay to replace the furniture? Or clean the carpets?"
    "What if he won't let you find [kittenname] a home? Would Laurie still take him?"
    "You watch the landlord inspect your apartment, nodding to himself the whole time."
    show LL Neutral at left with moveinleft
    "Landlord" "Well, it doesn't look like anything's damaged. Honestly, I can barely tell you've had a cat living here."
    show chelsea blank
    "[kittenname] jumps up on the back of the couch, meowing for attention."
    show LL Happy
    "The landlord smiles down at him, scratching him behind the ears."
    "Landlord" "You really found him on the streets?"
    show chelsea sad
    pcname "Some kids were being mean to him in an alley. He was just a tiny kitten."
    pcname "I fed him there for a while, since I knew I couldn't keep him here."
    pcname "Honestly, I meant to find him a new home when I brought him here, but..."
    "He nods understandingly."
    "Landlord" "I'm an animal lover myself, but I have to protect my investment, you know?"
    show LL Neutral
    "Landlord" "Still... I can't see putting him back on the streets and he seems like a good cat..."
    show LL Blank
    "He sighs."
    show chelsea blank
    show LL Serious
    "Landlord" "As long as nobody reports you, I might be able to overlook it this time."
    show chelsea shocked
    "You can barely believe your ears."
    pcname "What?"
    show LL Neutral
    "Landlord" "Just make sure he doesn't damage anything and I'll pretend not to notice him."
    show LL Blank
    "[kittenname] butts his head against the landlord's arm, demanding more attention."
    show LL Happy
    show chelsea happy
    "Thankfully, the landlord laughs."
    "Landlord" "As much as he'll let me, anyway."
    "You nod, not trusting yourself to speak."
    "Landlord" "Let's have the rent, then."
    "Passing him the envelope, you smile as he counts the money out. He's really going to let you keep [kittenname]!"
    $ Cash-=600
    "Landlord" "Looks like it's all there. I guess I'll see you both next month."
    "Giving [kittenname] one more round of ear scratches, he lets himself out."
    hide LL Happy with moveoutleft
    return

label notpayrent:
    if missedrent:
        "Landlord" "I told you last time that this couldn't happen again."
        show chelsea sad
        pcname "I know, but..."
        "He holds up a hand."
        "Landlord" "I should never have let you slide before. I'm not doing it again."
        pcname "But I--"
        "Landlord" "You have one week until I change the locks, so you better get your stuff out before then."
        scene bg black with fade
        "With no other choice, [pcname] packs her stuff and moves out."
        "For a few weeks, she couch surfs with various friends and acquaintances, but soon the invitations dwindle."
        "Without a place to stay, she soon loses her job and drops out of school."
        "You've reached the Eviction Ending."
        pause 1.0
        $ renpy.full_restart()
    "Landlord" "I told you that we have a no-tolerance policy on the rent."
    if club == "track":
        show chelsea sad
        pcname "I know, I know... I just..."
    elif club == "cheer":
        pcname "I remember, it's just been such a bad month and..."
    elif club == "yearbook":
        show chelsea sad
        pcname "I-I'm sorry, I..."
    "He sighs."
    "Landlord" "I hate doing this, but this is how we make our income."
    "Landlord" "I'll be back to change the locks in a week."
    "Landlord" "If your stuff isn't out by then, you'll have to make arrangements to come pick it up."
    "Shaking your head, you try to think of a way to get the money."
    if club == "track":
        show chelsea shocked
        pcname "I have nowhere else to go. Just let me call some people and I'll see if I can get the money somehow..."
    elif club == "cheer":
        show chelsea shocked
        pcname "What? I don't have anywhere else to go."
        pcname "Maybe my boss will give me an advance..."
    elif club == "yearbook":
        pcname "But I... I don't have anywhere else..."
        "Maybe you could stay with someone? How could you even ask someone to do that?"
    "Landlord" "Look... I wish I could be more lenient, but I've been through this before."
    "He shakes his head; he really does look sorry."
    "And the whole situation reminds you of all those movies, where the girl..."
    if corruption < 20:
        show chelsea shocked
        "No, you couldn't!"
        show chelsea sad
        "But if you don't {i}try{/i}..."
    elif True:
        show chelsea happy
        "It doesn't hurt to try, right?"
    menu missingrent_offer:
        "Offer to pay him another way." if True:
            if club == "track":
                show chelsea blank
                pcname "Maybe we could... Help each other out...?"
            elif club == "cheer":
                show chelsea happy
                pcname "If you could let me off this {i}one{/i} time, I could do something for you..."
            elif club == "yearbook":
                show chelsea embarrassed
                pcname "I... I'll do a-{i}anything{/i}..."
            "His brows furrow."
            show LL Neutral
            "Landlord" "Are you... suggesting what I think you are?"
            show chelsea embarrassed
            if club == "track":
                "You give him a sheepish smile and shrug suggestively."
            elif club == "cheer":
                "You bite your lip and smile up at him."
                pcname "Maybe...?"
            elif club == "yearbook":
                "Cheeks burning, you nod."
                pcname "I... think so?"
            show LL Blank
            "He stares at you a long moment, his cheeks slowly reddening."
            "You're sure that he's angry at the suggestion - you should never have tried this!"
            "He turns suddenly, shutting the door to your apartment before turning back toward you."
            show LL Neutral
            "Landlord" "What {i}exactly{/i} are you offering?"
            show chelsea shocked
            show LL Blank
            "You hesitate; you hadn't expected to get this far."
            if club == "track":
                show chelsea confused
                pcname "Uh... A blowjob?"
            elif club == "cheer":
                show chelsea confused
                pcname "I could... blow you?"
            elif club == "yearbook":
                show chelsea confused
                pcname "Um... I... I could... Blow you...?"
            "He stares again, his face unreadable."
            show LL Neutral
            "Landlord" "No, I can't... Look, thanks for the offer but..."
            show chelsea sad
            if club == "track":
                pcname "Please, just this once. I really need this apartment!"
            elif club == "cheer":
                pcname "Please, I really have nowhere else to go!"
            elif club == "yearbook":
                pcname "Please, I... I can't... I'll do anything!"
            show LL Blank
            "He sighs, running his hand through his hair."
            show LL Neutral
            "Landlord" "I can't believe we're even discussing this. If my wife found out..."
            show LL Blank
            pcname "I won't tell anyone! Please, {i}please{/i}!"
            show LL Disappoint
            "Landlord" "I'm sorry, it's just not right. You don't actually {i}want{/i} to blow me and-"
            "You can tell his resolve is weakening. He's tempted, or he would already have left."
            if club == "track":
                show chelsea happy
                pcname "No, I- I do! I've wanted to since I heard your voice on the phone..."
                "You nod reassuringly, glancing meaningfully at his crotch. You're surprised to see that he's been growing slowly harder."
            elif club == "cheer":
                show chelsea happy
                pcname "Why would you think {i}that{/i}? I wouldn't have offered if I didn't {i}want{/i} to."
                "You lick your lips, glancing down at the growing bulge in his pants."
            elif club == "yearbook":
                show chelsea embarrassed
                pcname "I do! I {i}want{/i} to suck your... your cock."
                "You blush furiously, shocked at your own words."
            show LL Neutral
            "Landlord" "Is that so...?"
            show LL Blank
            "His eyes slide down your body, lingering at your breasts and legs."
            if club == "track":
                pcname "I bet you have a real big one..."
            elif club == "cheer":
                show chelsea happy
                pcname "Of course! I've always fantasized about this..."
            elif club == "yearbook":
                show chelsea embarrassed
                pcname "Y-yes. Please..."
            "When he speaks again, his voice is thick and husky with his arousal."
            show LL Neutral
            "Landlord" "Tell me how much you want to suck it."
            show LL Blank
            if club == "track":
                "Eyes fastened to his pants, you try your best to sound seductive."
                pcname "After I signed the lease, I couldn't get your voice out of my head..."
                pcname "I just knew you would be tall and sexy, and I kept thinking about how it would feel to wrap my lips around you and..."
            elif club == "cheer":
                show chelsea happy
                "Sighing dramatically, you speak with a breathy voice."
                pcname "I can't stop thinking about it. I touch myself sometimes, thinking about this exact scenario..."
            elif club == "yearbook":
                show chelsea embarrassed
                "Fighting back your embarrassment, you force the words out."
                pcname "Please let me suck it. I... I really want to..."
            scene bg black with dissolve
            "His hands fall to his pants as you speak. Unzipping his fly, he pulls his cock free."
            "It waves in your direction, as if searching for you."
            "Landlord" "Fine, I'll forget about rent just this once..."
            "Relieved, you practically throw yourself to your knees in front of him, covering his cock in little kisses."
            if club == "track":
                "You waste no time, wrapping your hand around his shaft while you work the tip in and out of your mouth to moisten it."
            elif club == "cheer":
                pcname "Oh, thank you!"
                "You take his cock in your hand, raising it so that you can lick the underside from base to tip."
            elif club == "yearbook":
                "Nervously, you lower your lips to the head of his dick, sucking gently."
            "His breath catches in his throat as you touch him; you find yourself enjoying his reaction."
            "Stroking his shaft, you run your tongue in circles around the head, teasing him gently."
            "Then you slowly work him in and out of your mouth, taking more each time."
            if corruption >  20:
                "He moans when he hits the back of your throat, but you aren't done yet."
                "Raising your eyes to his face, you press even further, sliding his cock down your throat as far as it can go."
                "You hold him there for a few seconds, letting the muscles of your throat contract around him for as long as you can."
                "Pulling back, you take in a few ragged breaths through your nose before swallowing him again."
                "Landlord" "Fuck..."
                "You deepthroat him a few more times - each time, pressing your tongue along the bottom of his shaft - until his breath is coming hard and fast."
                "You can tell he's getting close."
            elif True:
                "He moans when he hits the back of your throat, and you fight back the urge to gag."
                "You pull back, until only his tip is still in your mouth, and flick your tongue across the head."
                "His breath hisses in response and you slide your lips back down his shaft again."
                "Over and over, you bob your head up and down on his cock, until salty precum coats your tongue."
                "You can tell he's getting close."
            "Sucking hard from base to tip, you bring him to a climax."
            "His hips buck rhythmically as he empties his load, filling your mouth with spurts of hot, salty cum."
            "When he finishes, you sit back on your heels, swallowing the last of it with a smile."
            if club == "track":
                pcname "Even better than I expected."
            elif club == "cheer":
                pcname "Mmmmmm..."
            elif club == "yearbook":
                pcname "I hope that was okay..."
            "Landlord" "Shit..."
            "He tucks his cock back in his pants and lets out a deep sigh."
            "Landlord" "I can't believe that just happened..."
            pcname "So we're good now...?"
            "He looks down at you, still on your knees in front of him, your lips puffy and red."
            "Landlord" "Yeah, we're good. But this can't happen again."
            "Landlord" "Fuck... I don't know what I was thinking. It shouldn't have happened at all."
            "Landlord" "Jesus..."
            "He makes his way to the door, almost in a stupor."
            "Landlord" "I mean it. Have your rent ready next month."
            pcname "I will!"
            "As he lets himself out, you wipe your lips with the back of your hand."
            "You can barely believe what just happened. Did you really just suck off your landlord?"
            if club == "track":
                "You can't help but laugh."
                pcname "I didn't think that would actually {i}work{/i}..."
            elif club == "cheer":
                "You smile, a little proud."
                pcname "I just gave a $600 blowjob!"
            elif club == "yearbook":
                "You touch your lips, amazed at how puffy and full they feel."
                pcname "I can't believe I did that..."
            $ missedrent = True
        "Accept your fate." if True:
            pcname "I understand. I'll be out by the end of the week."
            scene bg black with fade
            "With no other choice, [pcname] packs her stuff and moves out."
            "For a few weeks, she couch surfs with various friends and acquaintances, but soon the invitations dwindle."
            "Without a place to stay, she soon loses her job and drops out of school."
            "You've reached the Eviction Ending."
            pause 1.0
            $ renpy.full_restart()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
