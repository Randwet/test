label matt_damienconflict1:
    "The sky is grey and overcast outside with a few trickles of rain splashing against your classroom window."
    "As your teacher drones on with his lecture, it's even harder to fight the exhaustion pulling you under."
    show chelsea sad with dissolve
    "Maybe staying up late last night to watch all those true crime documentaries wasn't the best idea..."
    show chelsea shocked
    "Thankfully, second period is almost over when you feel your phone buzz in your pocket."
    call screen TextingScene("Matt",
    [
        TextMessage("Meet me in the storage room by the gym after class."),
        TextMessage("Okay.", sender = False),
    ])
    show chelsea blank
    "You're sure whatever Matt has planned will wake you up; there never seems to be a dull moment when he's involved."
    show chelsea at center, exitScene(0.5, 0.0, 0.3, 0.2)
    pause 0.5
    show Matt Pleased with dissolve
    pause 1.0
    show Matt at center, exitScene(0.5, 0.0, 0.4, 0.2)
    "The bell rings, and instead of heading to your next class, you immediately turn and follow the path to the storage room. You can hear Matt behind you, keeping his distance."
    scene black with fade
    show chelsea with dissolve
    "The storage room is cramped but organized, with all of the sports equipment in the right spot. Matt closes the door behind you and flicks the light on."
    show Matt Smirk at left with dissolve
    pcname @ confused "What's up?"
    show Matt Pleased
    m "I had an idea. You know how Alecia's boyfriend caught her getting fucked by half the soccer team last week?"
    if club == "track":
        "You're pretty sure you heard about it somewhere on the grapevine; it was hard to keep that kind of gossip away from the other sports teams."
        show chelsea confused
        pcname "What about it?"
    elif club == "cheer":
        "Of course you knew; everyone on the cheer squad had been talking about it. It was the biggest news since one of the goth girls got a nose job last month."
        show chelsea confused
        pcname "Um, yeah, why?"
    elif club == "yearbook":
        show chelsea sad
        "You certainly {i}didn't{/i} know about that, but you've done a pretty good job at avoiding most of the school's gossip to begin with."
        pcname "I-I didn't know about that, actually..."
        show Matt Question
        show chelsea shocked
        m "What? Do you live under a rock? Everyone's been talking about it."
        show chelsea sad
        show Matt Angry
        m "Tch, whatever."
    show Matt Smirk
    show chelsea shocked
    m "What if we did the same thing to Damien?"
    show Matt Question
    show chelsea confused
    pcname "You want to catch me fucking Damien?"
    show Matt Angry
    show chelsea shocked
    m "No, you dumb bitch. I want Damien to watch {i}me{/i} fuck {i}you.{/i}."
    show chelsea blank
    m "Go ahead and text him to meet you outside the gym. Let's give your toy a fucking show."
    menu matt_damienschoolfuck:
        "Let's do it, but..." if True:
            show Matt Smirk
            show chelsea embarrassed
            "Matt's idea is tempting; there's something cruelly sexual about the idea of your boyfriend watching you get fucked by another man."
            show Matt Blank
            show chelsea sad
            "But you care about Damien, too. There's no way he would go along with something like this... at least not how Matt's presenting it."
            show chelsea laugh
            "A better idea hatches in your mind."
            if club == "track":
                show chelsea blank
                show Matt Question
                pcname "Okay, but maybe not today. I have some other stuff in mind."
            elif club == "cheer":
                show Matt Question
                show chelsea embarrassed
                pcname "Sure, let's do it, but maybe give me a little more time to prepare. I want it to be special, you know."
            elif club == "yearbook":
                show chelsea sad
                show Matt Angry
                pcname "D-Do you think we could wait... for just a little bit...?"
            show Matt Angry
            show chelsea blank
            "Anger flickers across Matt's face. He opens his mouth to object, but you quickly cut in."
            show Matt Question
            pcname "I'm not saying no, but I want to do this a certain way. I have an idea for how to do it..."
            show chelsea shocked
            show Matt Pleased
            "You expect Matt to yell at you or berate you for your disobedience. Instead, after a few silent moments of processing, he almost looks... impressed."
            show chelsea embarrassed
            show Matt Happy
            m "Have you been thinking about this, [pcname]? Fuck, you're a dirtier slut than I give you credit for."
            show Matt Pleased
            m "Fine, I'll give you some time, but you better make it worth the wait."
            show Matt Angry
            show chelsea sad
            m "And don't put it off forever, either."
            show Matt Blank
            "You swallow hard and nod. The implication of his words are clear; you can already picture the photos he would use to spread around the school if you act out of line."
            show Matt Pleased
            show chelsea blank
            "Matt nods, satisfied, and looks around the room."
            show chelsea shocked
            show Matt Smirk
            m "Since I'm feeling generous today, the least you can do is make it up to me."
            show chelsea embarrassed
            "Matt's legs spread out and you can see his erection poking out against his pants. Excitement twists inside of you, dampening your own panties."
            show Matt Pleased
            pcname "Yes, Matt."
            show Matt Blank
            show chelsea blank
            "You start to lower to your knees, but Matt clicks his tongue, halting you at once."
            show Matt Angry
            m "Clothes off. Now."
            $ clothes = "naked"
            show chelsea blank
            show Matt Pleased
            "You do as told, a slight chill raising goosebumps along your arms and legs as your attire forms a soft pool on the floor."
            show chelsea confused
            m "Now grab that hockey stick."
            hide chelsea with dissolve
            pause 1.0
            show chelsea confused with dissolve
            "You raise an eyebrow but don't object as you fumble with one of the large hockey sticks in the corner of the room. You pass it to Matt, curiosity burning in your gaze. What the hell does he want the stick for?"
            show Matt Smirk
            show chelsea blank
            m "Get down and face the door."
            show Matt Blank
            show chelsea confused
            pcname "Um, Matt--"
            show chelsea shocked
            "Something hard and curved slams against your ass. You cry out, already aware of the bruise forming on your backside as you look back to see Matt clutching the hockey stick above you."
            show chelsea sad
            show Matt Angry
            m "No talking."
            scene black with dissolve
            "He doesn't wait for you to turn away as he holds the stick back and slams it against your ass again. You bite down on your lip, unable to hold back the whimper that crawls up your throat."
            "Another smack. This time you feel your hips jerk toward the hockey stick, eager to feel its pleasantly painful slap against your ass."
            "A small part of you feels deserving of it; not only have you obeyed him to speak your mind, but you've shown you're willing to go through with exposing your affair in the most humiliating way possible."
            "It only feels right that you'd be punished, but why does Matt's punishments always feel so {i}good{/i}?"
            scene black with dissolve
            m "Wow, I can't believe you're getting off on this. You really are a slut; you're fucking dripping."
            "Sure enough, you feel the moisture from your pussy slide down your thighs and dampen the floor underneath."
            scene black with dissolve
            "Unable to help yourself, you reach down and stroke your clit, the sensation eliciting another pleasured cry."
            "Although Matt doesn't tell you to stop, you can feel the force of the hockey stick hit harder against your ass, leaving bright red marks in its wake."
            m "Move your hand."
            scene black with dissolve
            "Suddenly the hockey stick is underneath you, rubbing between your folds. You grind against it, eager to get off."
            "Somewhere in your haze of excitement, a sudden thought occurs to you: isn't there a gym class being held around this time? Aren't they going to need equipment?"
            "You stare at the lock, the small metal turned to allow anyone wandering outside to burst right in. What if someone saw you like {i}this?{/i} There's no way you could survive the humiliation."
            "And yet, a part of you wants exactly that to happen."
            scene black with dissolve
            "The idea of someone walking in to see this only fuels you further, and this time you don't try to disguise your cry as you orgasm, your body thrusting hard against the hockey equipment."
            "You hear Matt's cruel laugh above you as he watches you come down from your high, but you're too overwhelmed to feel the shame you're sure will come later."
            scene black with dissolve
            "Matt drags a spare chair out from its spot and plops down, his pants unbuckled and legs spread wide."
            m "Finish me off."
            scene black with dissolve
            "Your limbs are trembling as you crawl to him on your knees and pull his cock from his pants. It seems you won't even need to work him up to it today; Matt's hard erection points out at you, ready for pleasure."
            scene black with dissolve
            "You take him into your mouth and down your throat, the sensation easier now with practice. You feel his cock flex inside of you, attempting to catch you off guard and force you to gag."
            "When it doesn't work, he just shoves himself into your mouth deeper."
            m "That's a good slut."
            scene black with dissolve
            "You know you shouldn't, but you can't help feeling a surge of pride from his praise and attempt to pull him down deeper."
            "Matt grabs a fistful of your hair and takes control, yanking your head back and forth as he fucks your skull."
            "You follow his motions, your own excitement building up as you sense Matt's coming orgasm."
            scene black with dissolve
            "His fingers tighten in your hair, his thrusts become harder. In, out, in, out, until you feel a thick load of cum shoot down your throat."
            "Matt's grip slackens and he slumps back in his chair lazily, pushing you off with a smirk while he tucks his cock back in place."
            scene black with fade
            m "Have fun cleaning that up."
            "He gestures toward the hockey stick with a laugh before leaving you alone and naked in the storage room."
            $ mattdamienntr = True
            jump events_end_period
        "I'm not doing that to him!" if True:
            show Matt Smirk
            "You feel your body freeze up. Heat rushes up your neck to your ears, and although you gape at Matt, you can't find the words to express just how far against this you are."
            "What is he {i}thinking?{/i} There's no way you would do this to your boyfriend!"
            if club == "track":
                pcname "Are you out of your fucking mind? I'm not doing that to him!"
            elif club == "cheer":
                show Matt Blank
                show chelsea angry
                pcname "You're kidding, right? Damien is a total sweetheart; I'm not going to humiliate him like that."
            elif club == "yearbook":
                pcname "N-No! I can't do that... Not to Damien..."
            show Matt Question
            show chelsea shocked
            m "Why not? You seem pretty fine with fucking me behind his back."
            show chelsea sad
            "Guilt seizes your chest. Matt had a point, but there is no way you can bring yourself to announce your affair to Damien this way."
            show Matt Blank
            "What Matt is suggesting is just... cruel."
            show chelsea blank
            "Matt scrutinizes you, a realization settling in."
            show chelsea shocked
            show Matt Question
            m "Wait. Don't tell me you actually {i}care{/i} about that nerd?"
            show Matt Angry
            m "Are you fucking kidding me? I thought he was just some idiot you were messing around with."
            show chelsea angry
            pcname "He's not. He's my boyfriend."
            show Matt Blank
            show chelsea shocked
            m "Yeah? How do you think he'll feel when he finds out you've been fucking other guys behind his back?"
            "Matt reaches into his pocket and pulls out his phone. He turns the screen towards you and flips through your naked photos."
            show chelsea sad
            show Matt Pleased
            m "I'd love to see his reaction when I show him these."
            if club == "track":
                pcname "Seriously? Matt, come on. He doesn't need to see those."
            elif club == "cheer":
                pcname "You're not seriously going to show him those, right?"
            elif club == "yearbook":
                pcname "M-Matt, please... Please don't..."
            show Matt Smirk
            m "Why not? Don't you want to be {i}honest{/i} with your boyfriend?"
            show Matt Question
            show chelsea shocked
            m "Or are you just a dirty whore that loves getting off behind his back?"
            show chelsea sad
            "You want to object but can't find the words to defend yourself. That's exactly what you've done."
            show Matt Pleased
            m "That's what I thought."
            show chelsea angry
            "Your body trembles. You tighten your fists at your side and try to hold back angry tears; the last thing you want to do right now is give Matt the satisfaction of seeing you cry."
            show Matt Smirk
            "Matt notices anyway, a cruel smirk spreading across his face."
            show Matt Happy
            m "What? Are you going to cry and beg me not to send these?"
            show chelsea shocked
            show Matt Pleased
            m "It's your own fault, whore."
            show Matt Smirk
            show chelsea sad
            m "So what do you say? Have you changed your mind yet?"
            "Matt waves the phone in front of you, scrolling through the damning photos. All the evidence of your infidelity is there for the world to see."
            menu changedmind:
                "Fine, let's fuck in front of him." if True:
                    show chelsea confused
                    "If Matt is going to tell Damien everything anyway, what was the point of trying to hide any longer?"
                    show chelsea blank
                    show Matt Blank
                    "Maybe this was a sign. This ruse was bound to come apart eventually; it was only a matter of time before you had to make a choice."
                    if club == "track":
                        show Matt Pleased
                        pcname "Fine. We'll fuck in front of him."
                    elif club == "cheer":
                        show Matt Question
                        pcname "You're not really giving me a choice."
                        show Matt Pleased
                        pcname "Fine. He has to find out somehow."
                    elif club == "yearbook":
                        show chelsea sad
                        pcname "I-I... Yes..."
                        show Matt Smirk
                        m "Yes, what?"
                        "You take a deep, shaky breath."
                        show Matt Pleased
                        show chelsea blank
                        pcname "Yes, we can fuck in front of him..."
                    show chelsea sad
                    m "That's better."
                    show Matt Blank
                    m "Text him now. I want to see him cry before school ends."
                    "You nod, trying to ignore the sickening guilt in your stomach. You know this is going to crush Damien, but what other choice do you have?"
                    "You can't stand the thought of breaking off things with Matt, and there's no way Damien will want to stay with you when everything comes to light."
                    call screen TextingScene("Damien",
                    [
                        TextMessage("Hey Damien, can you meet me outside the gym?", sender = False),
                        TextMessage("Uh sure. Everything okay?"),
                        TextMessage("Yeah, I just really want to see you. :)", sender = False),
                        TextMessage("Okay, I'll be there soon. :)"),
                    ])
                    show chelsea blank
                    show Matt Smirk
                    pcname "He's on his way."
                    m "Good. Let's not keep him waiting."
                    scene bg School with fade
                    "You follow Matt outside of the school and behind the gym, tucking yourselves in the shadow along the side of the building."
                    "The rain is letting up at least. Maybe that's a good sign?"
                    "You glance nervously at the windows nearby; the classroom is empty, but there's no guarantee it'll stay that way. What if someone else sees? You're all fucked if a teacher finds you."
                    "That's the least of your concerns, though."
                    show chelsea sad with dissolve
                    "Your heart hammers against your chest as you hear a nearby door unlatch."
                    show Matt Smirk at left, moveSprite(0.3, 0.3, 0.0) with dissolve
                    "Matt steps up behind you and snakes an arm around your waist, his hand creeping down to your upper thigh. A part of you wants to push him away-- another part wants to pull him even closer."
                    "Damien appears around the bend."
                    $ damienAttire()
                    show Damien Shocked at right with dissolve
                    D "[pcname]--?"
                    show Damien Glare
                    "He stops short, his gaze snapping to Matt."
                    if damienconfidence >= 50:
                        scene black with dissolve
                        D "What's happening here? What is Matt doing here?"
                        "His eyes flicker to Matt's hand slipping under your skirt. Damien's jaw tightens."
                        scene black with dissolve
                        D "Get your hands off of her."
                        m "Why? This little slut likes it."
                        scene black with dissolve
                        "Matt reaches up under your skirt and cups your pussy, two fingers stroking against the fabric. He pulls you closer, his hot breath caressing the shell of your ear."
                        m "Don't you, whore?"
                        "You can't help it; a small whimper of delight escapes your throat. Colored heat bursts across your face afterward, and you can barely stand to look up at Damien's furious expression."
                        D "What the fuck? [pcname], you're just going to let him touch you like that?"
                        scene black with dissolve
                        "You open your mouth to answer-- with what, you aren't sure-- but the words die on your tongue as Matt lifts your skirt and uses one hand to finger you while the other gropes your breasts."
                        "Damien's fists ball at his sides, and you can tell he wants you to fight Matt. You can see it in his eyes, how badly Damien wants you to scream and punch and kick and run into his arms."
                        "You do nothing."
                        m "She's been letting me touch her like this for a {i}long{/i} time. What, you seriously thought a slut like this wanted {i}you?{/i}"
                        m "You're fucking pathetic."
                        scene black with dissolve
                        D "I thought I knew you, [pcname]."
                        "Damien shakes his head, fists clenching and unclenching beside him. Is he going to hit Matt? Is he going to hit {i}you?{/i}"
                        "He does neither."
                        D "Well, Matt's right about one thing; you're a fucking {i}whore{/i}."
                        scene black with dissolve
                        D "Go to Hell."
                        "Damien flips you both off before storming back inside. You flinch as the school's door slams shut behind him."
                        scene bg School with fade
                        show Matt Pleased at left with dissolve
                        show chelsea sad with dissolve
                        "Matt's cruel laugh is hot against your ear. He pulls away suddenly, leaving you needy and wanting."
                        show Matt Happy
                        m "He couldn't even stand to see you get fingered; I should've just started with fucking you from the start. Imagine what he would've said to {i}that.{/i}"
                        hide Matt with dissolve
                        "Matt wipes his wet fingers on your skirt before striding back inside. He doesn't spare you another glance."
                        show chelsea embarrassed
                        "Shame heats your face as you tug your clothes back in place."
                        "Did you make the right decision?"
                        scene black with fade
                        "You shake your head. It's too late for those kind of thoughts. What's done is done."
                        "At least Matt is exciting-- you doubt you'll have a dull moment with him."
                        "Once you're cleaned up, you sneak back into the school and head to your next class."
                        $ damienbreakup = True
                        $ mattroutelock = True
                        jump events_end_period
                    elif True:
                        scene black with dissolve
                        D "Um, [pcname], what is he doing here...?"
                        "Damien's eyes flicker to Matt's hand slipping under your skirt. Hurt flashes across his face."
                        scene black with dissolve
                        D "[pcname]...?"
                        "Matt reaches up under your skirt and cups your pussy, two fingers stroking against the fabric. He pulls you closer, his hot breath caressing the shell of your ear."
                        m "Well, slut? Do you wanna tell him or should I?"
                        scene black with dissolve
                        "You can't help it; a small whimper of delight escapes your throat. Colored heat bursts across your face afterward, and you can barely stand to look up at Damien's pained expression."
                        m "Look at her-- she can't get enough of it. What a fucking {i}slut{/i}."
                        scene black with dissolve
                        "His fingers dig deeply into you, shoving the fabric of your panties out of the way. You gasp, your hips involuntarily jerking toward him."
                        "Damien is frozen. He watches Matt pull and remove your clothes, his lips stuck in a shocked 'o'."
                        D "[pcname]... I-I don't understand--"
                        m "For fuck's sake, you're stupid."
                        m "Your girlfriend is a goddamn {i}whore{/i}; we've been fucking for months."
                        m "Did you seriously think she would be interested in a pathetic loser like {i}you?{/i} You're a fucking idiot!"
                        scene black with dissolve
                        "Matt laughs cruelly as he strips you down to nothing, practically ripping the buttons off of your shirt in an effort to expose you to your boyfriend."
                        "The act is both humiliating and exciting. You feel pleasure ripple through you as you stand naked before Damien while another man touches you."
                        "Damien's face is flushed red, but he doesn't move. You're not sure he remembers how to; it's like he's stuck, scrambling to process what's happening in front of him."
                        "Matt settles behind you. You hear the sound of his zipper go down."
                        scene black with dissolve
                        m "Bend over."
                        "You hesitate but do as told, using the brick wall as leverage. Matt's erection presses behind you, the tip slipping against your wet entrance."
                        m "See how easily she listens to me? I barely have to touch her before she's ready to take my cock."
                        "Damien's eyes widen in horror. He takes a shaky step back."
                        D "Please don't--"
                        "But Matt slides into you, the folds of your pussy easily accepting his length. It's as if your own body is in on the joke, eager to perform."
                        scene black with dissolve
                        "Your gasp turns into a moan as Matt thrusts in and out of you roughly. One of his hands clutches your hair, yanking your head back so you're forced to look Damien in the eye as Matt fucks you."
                        "Damien stands there, stunned silent. You notice tears wet his red eyes and spill over as Matt pounds you against the wall, careless to how forceful he is while your skin rubs against the rough brick."
                        "He's enjoying Damien's heartbreak, you realize. And with a little bit of guilt, you realize you're enjoying it, too."
                        scene black with dissolve
                        "Matt keeps going until he's finished. You whimper as he pulls out, loads of his cum dripping out of your cunt and onto your thighs and the ground."
                        scene bg School with fade
                        $ clothes = "naked"
                        show Matt Smirk with dissolve
                        show Damien Sad at right, moveSprite(0.75, 0.75, 0.0) with dissolve
                        show chelsea embarrassed at left with dissolve
                        "Matt zips himself back up and approaches Damien. Your boyfriend just stares at you, for once ignoring one of his bullies."
                        show Matt Pleased
                        m "She's an adequate fuck; shitty at everything else, though."
                        hide Matt with dissolve
                        "Matt punches his shoulder and leaves him there, striding back into the school as if he hadn't just destroyed a relationship."
                        show chelsea sad
                        pause 1.0
                        hide chelsea with dissolve
                        "With the high of Matt's confidence gone, guilt and shame properly settles in you. You can't meet Damien's gaze as you pull your clothes back on."
                        $ clothes = "school"
                        show chelsea sad at left with dissolve
                        show Damien Worry
                        D "You've been sleeping with Matt this whole time, haven't you?"
                        show chelsea embarrassed
                        show Damien Sad
                        "You try to find the right words to explain, maybe to even excuse yourself, but nothing feels right. You nod instead."
                        show Damien Worry
                        show chelsea sad
                        D "I'm such an {i}idiot.{/i}"
                        show Damien Sad
                        "His voice cracks on the last word and, finally, Damien looks away. He stares up at the sky in a poor attempt to blink back his tears, but they're already cascading down his face."
                        pcname "I'm sorry."
                        show Damien Laugh
                        "Damien laughs, the sound cruel and bitter and hurt. You wince."
                        show Damien Worry
                        D "Yeah, me too."
                        hide Damien with dissolve
                        "Damien scrambles to his feet, but he doesn't head back into the school; he walks back to the parking lot, toward his car."
                        scene black with fade
                        "You don't need to ask him for clarification to know that it's over between you two."
                        "Straightening your skirt, you duck back inside the school and pray the day ends soon."
                    $ damienbreakup = True
                    $ mattroutelock = True
                    jump events_end_period
                "No way." if True:
                    show chelsea blank
                    "He's right; there's no one to blame but yourself, but it doesn't mean Damien deserves to find out this way."
                    if club == "track":
                        show chelsea angry
                        show Matt Blank
                        pcname "You're out of your fucking mind. I'm not doing that to Damien, he deserves better."
                    elif club == "cheer":
                        show chelsea angry
                        show Matt Blank
                        pcname "I'm not going to humiliate the poor kid like that so you can get off on blackmailing me, Matt. Not happening."
                    elif club == "yearbook":
                        show chelsea sad
                        show Matt Blank
                        pcname "No! I-I'm not doing that to Damien. It would be so humiliating..."
                    show chelsea blank
                    "Matt's expression falls, his eyes narrowing at you with distaste. He grips his phone a little tighter."
                    m "Fine. Have it your way, slut."
                    show Matt Angry
                    show chelsea shocked
                    m "As soon as I see him, these photos are out. Have fun explaining them."
                    show Matt Smirk
                    pause 1.0
                    hide Matt with dissolve
                    "Matt gives you another harsh smile before storming out of the storage room."
                    show chelsea sad
                    "There's no time to waste; you need to get to Damien and explain yourself. Now."
                    "With shaking hands, you pull out your phone."
                    call screen TextingScene("Damien",
                    [
                        TextMessage("Hey, meet me in the storage room by the gym asap.", sender = False),
                        TextMessage("Uh sure. What's up, [pcname]?"),
                        TextMessage("I'll explain everything when you get here.", sender = False),
                        TextMessage("If you see Matt just ignore him.", sender = False),
                        TextMessage("Easier said than done, but k."),
                    ])
                    pause 1.0
                    show chelsea blank
                    pause 0.5
                    scene black with fade
                    "You pace around the storage room while you wait. The minutes ticking by feel like hours."
                    show chelsea sad with dissolve
                    "Did Matt stop him in the hall on his way here? Does he already know what you've done? What if he found out and doesn't show up?"
                    show chelsea blank
                    "You check your phone again, waiting for a call-out text, but nothing."
                    show chelsea embarrassed
                    show Damien Blank at left, moveSprite(0.25, 0.25, 0.0) with dissolve
                    "You nearly breath out in relief when Damien creeps into the storage room, glancing around in the hall to make sure he doesn't get caught before closing the door."
                    show chelsea blank
                    show Damien Worry
                    D "[pcname]? Is everything okay? Why are you hiding in the storage room?"
                    show chelsea sad
                    show Damien Blank
                    "Damien puts a comforting arm around your shoulders and strokes your hair. The guilt nearly eats you up inside."
                    show chelsea blank
                    "At least Matt hasn't reached him yet. That's good."
                    pcname "We need to talk."
                    show Damien Neutral
                    D "...Okay."
                    show Damien Blank
                    "You can see the spike of fear and concern in Damien's eyes as he pulls a couple of chairs out from nearby to sit down on. You take a seat if only so you don't wear the soles of your shoes out pacing."
                    show chelsea sad
                    show Damien Sad
                    pcname "There's something you need to know, and it's going to be best for everyone if you hear it from me first."
                    show Damien Blank
                    pcname "I..."
                    show chelsea shocked
                    "Oh God, this was harder than you thought it would be. It feels like there's a giant lump in your throat as you struggle to get your confession out."
                    show chelsea sad
                    show Damien Shocked
                    pcname "I've been sleeping with Matt."
                    show chelsea embarrassed
                    "Damien stares at you and you can see the world crumple on his face."
                    show Damien Sad
                    "It takes a long time for him to process what you've said. His shoulders slump over and he presses his face into his hands, occasionally glancing back up in your direction in disbelief."
                    show chelsea sad
                    show Damien Neutral
                    D "You're joking. Tell me this is a joke."
                    show Damien Sad
                    pcname "I'm not-- it's not."
                    show chelsea blank
                    "Another long pause. Damien runs his hands over his face and when he pulls them away, you see tears in his eyes."
                    show chelsea sad
                    show Damien Glare
                    "It's a whole new stab in the heart as you realize just how badly you've hurt him."
                    show Damien Angry
                    show chelsea shocked
                    D "What the {i}fuck{/i}, [pcname]? How long has this been going on?"
                    show Damien Glare
                    show chelsea blank
                    pause 1.0
                    show chelsea sad
                    pcname "...A while. Longer than it should have."
                    show Damien Angry
                    show chelsea shocked
                    D "It shouldn't have happened {i}ever!{/i}"
                    show Damien Glare
                    "You flinch at his tone, your gaze dropping to your lap."
                    show chelsea sad
                    pcname "You're right, it shouldn't."
                    if damienconfidence >= 50:
                        show Damien Laugh
                        show chelsea blank
                        "Damien laughs but it's a bitter sound, full of hatred and malice. It feels wrong coming from Damien."
                        show Damien Glare
                        show chelsea sad
                        "A little voice in the back of your head reminds you that you're the reason for this change."
                        show Damien Angry
                        D "I can't believe this. {i}Matt{/i} of all people. Seriously?"
                    elif True:
                        show Damien Sad
                        "Damien sniffs and wipes the tears on his sleeve. He keeps his arm pressed there, as if he can hide his emotions from you as long as you can't look in his eyes."
                        show chelsea shocked
                        show Damien Worry
                        D "I thought you cared about me, [pcname]. I thought you were different."
                        show chelsea embarrassed
                        show Damien Glare
                        pcname "I do care about you, Damien."
                        show Damien Angry
                        show chelsea sad
                        D "If you cared, you wouldn't have cheated on me."
                    D "How did this happen?"
                    show chelsea blank
                    show Damien Glare
                    "You aren't sure where to start; it all happened so fast. You try to explain the length of your affair with Matt, sparing Damien of the hot and heavy details. He's suffering enough as it is."
                    show Damien Sad
                    show chelsea sad
                    with fade
                    "When you finish, Damien has trouble meeting your gaze. Will he ever be able to look at you again without disdain? You aren't sure, but the thought of it nearly breaks your heart."
                    show Damien Worry
                    D "Do you want to be with him?"
                    menu mattfinalchoice:
                        "I want to stay with Matt." if True:
                            show chelsea shocked
                            show Damien Sad
                            "You stare at him, surprised to find the first name that pops up in your mind isn't your boyfriend, but {i}Matt.{/i}"
                            show chelsea sad
                            "Maybe the reason you couldn't stay faithful to Damien was because you wanted Matt all along. Even though he treats you like shit, a part of you likes it, and likes him even more for doing it."
                            show chelsea embarrassed
                            "There's no way a girl like that deserves another chance at Damien."
                            show chelsea blank
                            "Besides, even if you try to stay with Damien, there's no guarantee it'll work out. That trust has already been broken, and you're not sure it can be repaired."
                            show Damien Shocked
                            pcname "...I want to stay with Matt."
                            show Damien Glare
                            show chelsea sad
                            "A flicker of surprise makes its way on Damien's face, then he glares, the hurt and disappointment you were expecting taking full force."
                            show Damien Angry
                            show chelsea blank
                            D "You want to stay with {i}him?{/i} Why? Is he that good in bed?"
                            show Damien Glare
                            "You know he doesn't really want that answer. You don't even want to give it to him; Damien's self esteem is low enough as it is."
                            show chelsea sad
                            "Damien's fists clench in his lap, his limbs shaking in anger."
                            pcname "...I'm sorry, Damien."
                            show Damien Angry
                            show chelsea shocked
                            D "Yeah. I'm sure you are."
                            show Damien Glare
                            "He stands up suddenly, a furious, hateful gleam in his eyes. His reaction freezes you in place; it's only fair for him to be angry, but you've never seen him {i}this{/i} angry."
                            show chelsea sad
                            "He's like a different person."
                            show Damien Angry
                            D "I'm so {i}sick{/i} of him ruining everything I have!"
                            show chelsea embarrassed
                            show Damien Glare
                            pcname "Damien?"
                            hide Damien with dissolve
                            pause 1.0
                            show chelsea sad
                            "But he's already gone, the storage room door slamming behind him."
                            show chelsea blank
                            "You hesitate, not sure what to do. Should you follow him? Leave him alone? You doubt anything you have to say will matter to Damien right now."
                            hide chelsea with dissolve
                            "Class is almost over, so after a few minutes, you slip out of the storage room."
                            scene black with fade
                            "You don't see Damien for the rest of the school day-- it seems he's even skipped lunch, leaving you to eat alone."
                            "That is, until school ends."
                            scene bg School
                            show Matt Smirk at left
                            with fade
                            "As you make your way out of the building, you find Matt standing in the parking lot, phone in hand, clearly waiting for Damien."
                            show Damien Glare with dissolve
                            show chelsea sad at right with dissolve
                            "Damien is a few paces ahead of you, but instead of heading to his car, he steers toward Matt. This can't be good."
                            show Matt Pleased
                            m "I guess you told him, huh?"
                            show Matt Happy
                            m "Look at how mad he is. How's it feel knowing your girlfriend is a total whore?"
                            show Matt Smirk
                            m "I bet you'll love this picture. She ever do something this kinky for--"
                            scene black with dissolve
                            "Damien's fist collides with Matt's jaw, shutting him up. The phone sprawls across the ground, but doesn't crack. You aren't sure if you're disappointed or not."
                            "You gasp and several heads turn your way, their attention immediately drawn to the fight. They abandon their cars, circling up around Damien and Matt as Damien throws another punch."
                            D "You {i}fucked{/i} my girlfriend?!"
                            scene black with dissolve
                            "Matt rubs his jaw, the playful mocking gone. Fists are raised and Matt strikes back."
                            "The crowd jeers as Damien and Matt tackle each other onto the ground, their bodies a tangle of fists and kicks and blood. You can't even tell who's winning."
                            "Damien reels his fist back and it looks like he's prepping to break Matt's nose."
                            pcname "Stop-- Stop!"
                            scene black with dissolve
                            "You dive into the fight without thinking, landing a hard punch against Damien's face. You hear a sickening {i}crunch.{/i}"
                            pcname "C-Crap, Damien, I'm so sorry..."
                            "But he doesn't hear you, too concerned with his now broken nose as he slumps back in pain."
                            m "Holy {i}fuck!{/i} That was a good fucking punch, slut."
                            scene black with dissolve
                            "Matt pushes away from Damien and leaps to his feet, laughing in disbelief. Damien clutches his bloody nose and rolls back and forth on the ground like a turtle stuck on their shell."
                            "It's bad enough you left him for Matt, but this is just humiliating. You grimace, looking away."
                            "Matt's arm snakes around your waist; he makes sure Damien gets a good look as he gropes your body before pulling away, leaving you and Damien alone."
                            pcname "Um, let me call an ambulance."
                            scene black with fade
                            "You scurry out of the crowd, trying to ignore the whispers and gossip that follow after you."
                            $ damienbreakup = True
                            $ mattroutelock = True
                            jump events_end_period
                        "I want to stay with Damien." if True:
                            show chelsea embarrassed
                            show Damien Neutral
                            "You shake your head, tears falling down your cheeks. You don't bother to wipe them away."
                            pcname "No. {i}No.{/i} Definitely not. I want to stay with you, Damien."
                            show Damien Shocked
                            pause 1.5
                            show Damien Sad
                            show chelsea sad
                            "You reach for his hand before you can think better of it. Damien flinches, yanking his hand away. You place your hands back in your lap, embarrassed and ashamed."
                            show Damien Worry
                            D "Then why? Just... why? If you wanted me, why would you do that?"
                            show chelsea blank
                            show Damien Blank
                            pcname "Matt-- He--"
                            show chelsea sad
                            "You can't blame the whole thing on Matt, but you want to. You would do anything to earn Damien's trust again."
                            pcname "He didn't give me a choice."
                            show Damien Neutral
                            D "What does that mean? Did he threaten you?"
                            show Damien Shocked
                            pcname "He has pictures of me. Bad ones. I... If I don't do what he says, he'll leak them."
                            show Damien Angry
                            D "So he's been blackmailing you."
                            show Damien Neutral
                            D "[pcname], why didn't you just tell me? Is that why you've gone along with everything?"
                            show chelsea blank
                            show Damien Blank
                            "You're not sure if you can keep from confessing your own interest in the affair if you speak, so you nod instead, nails digging into your palms. He doesn't need to know the extent of your interest with Matt."
                            show chelsea sad
                            pcname "I never wanted to hurt you, Damien."
                            show chelsea blank
                            "Damien's expression softens. You aren't sure why your chest hurts more-- are you overwhelmed with relief or guilt? Maybe both?"
                            show chelsea sad
                            show Damien Sad
                            pcname "I promise, I won't do it again. I-I'm done. I just want to be with you."
                            "Damien looks down at your hand, almost as if he wants to take it, but he remains where he is."
                            show Damien Angry
                            show chelsea blank
                            D "You should have told me sooner about the blackmail, [pcname]. I never would have let it get this far."
                            show Damien Blank
                            show chelsea sad
                            pcname "I wasn't sure how to tell you."
                            show chelsea blank
                            "It isn't entirely a lie; the less Damien knows about your involvement right now, the better."
                            if damienconfidence >= 50:
                                show chelsea shocked
                                show Damien Glare
                                "Damien stands up from his chair suddenly, fists clenched at his sides. Did he decide not to forgive you after all?"
                                show Damien Angry
                                show chelsea blank
                                D "I'm so fucking {i}sick{/i} of Matt and his friends ruining my life."
                                show chelsea sad
                                D "It's one thing to come at me, but it's another to {i}blackmail{/i} my {i}girlfriend{/i}."
                                show chelsea shocked
                                D "I'm going to do something about it."
                            elif True:
                                show chelsea shocked
                                show Damien Angry
                                D "I... I can't take this anymore, [pcname]. I can't."
                                show chelsea sad
                                show Damien Glare
                                "Panic grips your heart. Is he deciding not to forgive you after all? You can't blame him, but you can't stand the thought of breaking up either."
                                show chelsea blank
                                "Damien stands up and paces, his hands twisting in front of him."
                                show Damien Angry
                                D "Matt is always on my case, and now that he's dragged you into it... I can't let that go."
                                show chelsea shocked
                                D "I need to stand up to him."
                            show Damien Glare
                            "Damien cracks his knuckles, a strange gleam in his eyes. It's a side of Damien you've never seen before; you had no idea he could get this angry."
                            show chelsea confused
                            pcname "What are you going to do?"
                            show Damien Happy
                            show chelsea embarrassed
                            "He smiles down at you, and as undeserving of his kindness as you feel, it helps ease the panicked ache in your chest."
                            show Damien Laugh
                            show chelsea blank
                            D "Don't worry about anything, [pcname]. I have it all taken care of."
                            show chelsea confused
                            D "Just meet me outside after school and support me, okay?"
                            show Damien Happy
                            pcname "Um, okay."
                            show chelsea sad
                            "Damien presses a soft kiss to your forehead before helping you out of the chair. You can tell it pains him a little, but he's trying."
                            show chelsea embarrassed
                            "It's a better ending than you could have asked for."
                            scene black with fade
                            "Damien escorts you back to class and lingers around for the rest of the day, even sitting in on a few classes he's definitely not supposed to be in."
                            "You can't tell if it's comfort or paranoia that's driving him, but either way, you feel a little more relaxed at his side."
                            "Then school ends."
                            scene bg School
                            show Matt Smirk at left
                            with dissolve
                            "You follow Damien outside to the parking lot. Matt is already there, phone in hand, clearly waiting for Damien to arrive to show off the pictures. There's a wicked grin on his face as you and Damien approach."
                            show Matt Pleased
                            show Damien Glare
                            show chelsea blank at right, moveSprite(0.7, 0.7, 0.0)
                            with dissolve
                            m "I guess you told him, huh?"
                            show Matt Happy
                            m "Look at how mad he is. How's it feel knowing your girlfriend is a total whore?"
                            m "I bet you'll love this picture. She ever do something this kinky for--"
                            scene black with dissolve
                            "Damien's fist collides with Matt's jaw, shutting him up. The phone sprawls across the ground, cracking against the asphalt."
                            "You gasp and several heads turn your way, their attention immediately drawn to the fight. They abandon their cars, circling up around Damien and Matt as your boyfriend throws another punch."
                            D "Leave my girlfriend {i}alone!{/i} She's {i}mine!{/i}"
                            scene black with dissolve
                            "Matt rubs his jaw, the playful mocking gone. Fists are raised and Matt strikes back."
                            "The crowd jeers as Damien and Matt tackle each other onto the ground, their bodies a tangle of fists and kicks and blood. You can't even tell who's winning."
                            "Matt reels his fist back and it looks like he's prepping to break Damien's nose."
                            pcname "Stop-- Stop!"
                            scene black with dissolve
                            "You dive into the fight without thinking, landing a hard punch against Matt's face. You hear a sickening {i}crunch.{/i}"
                            m "Holy {i}fuck!{/i} You crazy bitch, you broke my fucking {i}nose!!{/i}"
                            scene black with dissolve
                            "Damien pulls off of Matt and holds you back against him before Matt can retaliate. You almost feel pity for Matt as he clutches his bloody nose and rolls back and forth on the ground like a turtle stuck on their shell."
                            "Almost."
                            D "Nice punch."
                            scene black with dissolve
                            "Damien laughs, and when you look at him, you see his own face is cut up and swollen from the fight."
                            "Not nearly as bad as Matt is, though."
                            pcname "Let's get some ice for this."
                            "You hesitantly touch Damien's jaw. He winces, but doesn't push you away. Well, it's a start; you're lucky he's forgiven you at all."
                            scene black with fade
                            "Tossing an arm around your shoulders, Damien leads you back to his car. You both leave Matt writhing in the parking lot, the sound of someone calling an ambulance fading out behind you."
                            $ mattbreakup = True
                            jump events_end_period

label matt_damienconflict2:
    "It takes some time for Damien to start building up trust with you again, but you never expected it to be a fast process."
    "The fact he's willing to forgive you at all is more than enough."
    scene bg Cafeteria with fade
    show chelsea happy
    show Damien Happy at left, moveSprite(0.3, 0.3, 0.0)
    with dissolve
    "You sit beside him during lunch, happy to listen to him ramble on about a new fantasy TV show he's been binge-watching."
    show Damien Laugh
    show chelsea embarrassed
    D "--Then the Queen of Salvation murders her husband--"
    show chelsea blank
    show Damien Blank
    "Damien stops, his words cutting off abruptly as something across the cafeteria captures his attention."
    "You turn in your seat to get a better look."
    show chelsea laugh
    pcname "Oh my god."
    show chelsea embarrassed
    "Matt is back, his nose taped up and left arm in a cast. He hobbles into the cafeteria, a harsh glare on his face as he makes his way to the lunch line. Several glances are tossed his way, gossip and laughs barely concealed by passing tables."
    show chelsea blank
    show Damien Glare
    "When he looks up, he meets your gaze. You can feel the hatred and fury burning in his eyes."
    show chelsea sad
    "You glance away, unnerved."
    show chelsea blank
    show Damien Blank
    pcname "He hasn't pressed charges against you, has he?"
    "Damien shakes his head."
    show Damien Neutral
    D "No. I don't think he wants to make it a bigger deal than it is. It's already embarrassing enough he got his ass kicked by a 'nerd'."
    show Damien Happy
    show chelsea embarrassed
    "A wry smile makes its way to Damien's face. At least he's found some humor in the situation."
    show Damien Neutral
    show chelsea blank
    D "Do you know if he got his phone fixed?"
    show Damien Blank
    pcname "No. I don't talk to him."
    show Damien Neutral
    D "You think the pictures are gone?"
    show chelsea sad
    show Damien Blank
    pcname "I don't know. I hope so."
    show Damien Happy
    show chelsea embarrassed
    "You feel Damien's arm wrap around your waist and he pulls you close."
    show Damien Laugh
    D "We'll figure something out."
    show chelsea laugh
    show Damien Happy
    pcname "Yeah, I hope so."
    show chelsea embarrassed
    pause 1.0
    scene black with fade
    "You continue eating your lunch and try to ignore the look Matt is giving you across the cafeteria."
    jump events_end_period

label matt_violetconflict:
    scene black with dissolve
    "You climb out of Violet's car and follow her down the street, the lights of busy restaurants and shops illuminating the dark city streets."
    "Shortly after work, Violet had been quick to text you about grabbing dinner together at a nearby restaurant. And who were you to turn down free food?"
    "Violet leads you to a fancy ivy-covered building with a large outdoor patio practically covered in plants and fairy lights."
    $ violetAttire(1)
    $ clothes = "bluedress"
    scene bg CityN
    show chelsea happy
    show V Casual Smile at right, moveSprite(0.7, 0.7, 0.0)
    with fade
    pcname "This place is like a greenhouse."
    show V SubCasual Happy
    show chelsea embarrassed
    V "Right? They have the best Thai food for miles."
    if violetrelate == 'Dom':
        show V Casual Smile
        V "You're going to try the spicy duck and pad Thai; they're to die for."
        show chelsea happy
        pcname "Okay."
    elif True:
        show V SubCasual Blank
        show chelsea blank
        V "I hope you like it."
        show V SubCasual Sad
        "Violet glances at you hopefully, perhaps realizing for the first time tonight that she didn't even ask you if you {i}liked{/i} Thai food."
        show V SubCasual Worried
        pcname "We'll see."
    scene black with fade
    "You follow Violet into the restaurant and back out onto the patio, a small table in the back already waiting for you."
    scene bg CityN with fade
    "You barely have a chance to open your menu before you feel your phone buzzing in your pocket."
    call screen TextingScene("Matt",
    [
        TextMessage("What are you wearing right now, slut?"),
        TextMessage("Some cute pink panties and bra.", sender = False),
    ])
    if violetrelate == 'Dom':
        show V Casual Annoyed at left with dissolve
        "You tuck the phone back into your pocket and look at the menu, but you don't miss Violet's annoyed glare."
        show V Casual Blank
        V "Who was that?"
        show V Casual Pout
        show chelsea with dissolve
        if club == "track":
            pcname "Just someone from track. They wanted to know what time we're meeting this weekend."
        elif club == "cheer":
            pcname "One of the girls on the squad; she couldn't find her spanx."
        elif club == "yearbook":
            pcname "S-Someone from club. They wanted to know where last year's yearbook files are."
        show chelsea sad
        V "Hmph."
        "Violet narrows her eyes and you can tell she doesn't entirely believe you, but she doesn't put up a fight as the waitress arrives to take your drink orders."
    elif True:
        show chelsea blank with dissolve
        show V Casual Pout at left with dissolve
        "You tuck the phone back into your pocket and look at the menu, but you don't miss Violet's suspicious glance."
        "A part of you nearly comes up with an excuse, but you keep your mouth shut and glance through the menu. It's none of her business who you're texting, and even if she asked, there's no way you're going to tell her."
        "A waitress stops by shortly after to take your drink orders."
    show chelsea blank
    with fade
    "Once she leaves, Violet eases into a new conversation."
    show chelsea blank
    show V Casual Blank
    V "There's a children's art gala my parents are attending this weekend. They've been trying to get me to go with them, but why the hell would I want to stare at a bunch of kids' drawings for five hours?"
    V "Have you ever been to one?"
    show V Casual Pout
    show chelsea confused
    pcname "Er, no, nothing like that."
    show V Casual Blank
    show chelsea blank
    V "Ugh. Lucky. I went last year and--"
    show V Casual Suprised
    show chelsea shocked
    "Mid-sentence, your phone buzzes once more."
    call screen TextingScene("Matt",
    [
        TextMessage("I'll be the judge of that. Show me."),
    ])
    show chelsea sad
    show V Casual Pout
    "You bite down on your lip; Violet will definitely be suspicious if you leave to take a new photo in the bathroom now. And Matt will definitely know if you send him an old one."
    scene black with dissolve
    "Trying to look as casual as possible, you lean your cheek against your palm on the table and pretend to focus on whatever Violet's talking about while you snap a picture under your skirt with your other hand."
    "You don't look at the screen as you send it over to Matt."
    scene bg CityN with dissolve
    show V Casual Annoyed at left with dissolve
    V "What are you doing?"
    show chelsea with dissolve
    pcname "I'm listening to you."
    call screen TextingScene("Matt",
    [
        TextMessage("What the hell is that? I can't see shit."),
        TextMessage("Are you out right now?"),
        TextMessage("Yeah, I won't be home for a while...", sender = False),
        TextMessage("Are you with anyone?"),
        TextMessage("Yeah, I'm out with Violet right now.", sender = False),
        TextMessage("That rich bitch from our school? What the hell would she want with you?"),
        TextMessage("Is she a lesbian? Are you fucking her right now?"),
        TextMessage("I knew you were a slut but I didn't know you'd fuck girls, too. You have to tell me this shit."),
        TextMessage("Send pics."),
    ])
    show V Casual Blank
    V "[pcname]."
    show V Casual Pout
    "You look up to see Violet glaring at you."
    if violetrelate == 'Dom':
        show V Casual Blank
        show chelsea shocked
        V "Give me the phone."
        show V Casual Pout
        show chelsea blank
        "She thrusts her hand out toward you expectantly."
        if club == "track":
            pcname "Fine, I'll put it away..."
            show V Casual Annoyed
            show chelsea shocked
            V "That's not what I said."
            show chelsea embarrassed
            pcname "Come on, Vi, you're not seriously going to go through my phone, are you?"
        elif club == "cheer":
            show chelsea angry
            pcname "Vi, seriously, I already told you who I was texting. You don't need to go through my phone. It's kind of weird..."
        elif club == "yearbook":
            show chelsea sad
            pcname "I-I'm not comfortable with you going through my phone, Vi..."
        show V Casual Annoyed
        show chelsea shocked
        V "Did you just talk back to me?"
        show chelsea sad
        show V Casual Pout
        V "I'm not saying it a second time."
        show chelsea shocked
        show V Casual Annoyed
        "You hesitate, but before you can even make the decision, Violet swipes the phone from your hand."
        show chelsea sad
        show V Casual Annoyed
        "Her face turns a deep red of fury as she scrolls through your messages with Matt, going far beyond just today's conversation."
        scene black with dissolve
        V "What the fuck, [pcname]? You've been sexting this guy for {i}months?{/i}"
        "You flinch at her raised voice. You can't bring yourself to look in her eyes; the betrayal is clear enough in her voice."
        V "And fucking him too. Great. You're a fucking {i}slut{/i}."
        "She tosses the phone back at you in disgust, her arms crossed firmly in front of her chest. You barely catch the device before it falls onto the ground."
    elif True:
        show chelsea confused
        show V SubCasual Worried
        pcname "What?"
        show chelsea blank
        pause 1.0
        show V Casual Pout
        "Violet's lips press together in a tight line. You can tell she wants to argue, but being your sub, that's out of the question."
        show V SubCasual Sad
        show chelsea shocked
        V "I'm trying to have a conversation with you..."
        show chelsea blank
        show V Casual Pout
        pcname "Then keep talking. I'm not stopping you."
        show V SubCasual Sad
        "Violet squirms in her chair; she's clearly upset with your behavior, but doesn't put up further argument."
        show V SubCasual Worried
        pause 1.0
        show V Casual Blank
        V "Okay... Anyway, there's a big auction at the gala and..."
        show chelsea shocked
        "You barely pay attention to Violet's rant about the art gala as Matt blows up your phone, sending one steamy text after another."
        show chelsea blank
        show V Casual Pout
        "You're vaguely aware of the waitress coming and going from the table, bringing drinks and food at Violet's request. Your mind is on other things, like Matt's texts and the places he's telling you he wants to put his cock..."
        show V Casual Blank
        V "--[pcname], are you listening?"
        show V Casual Annoyed
        show chelsea shocked
        pcname "Huh?"
        "You look up from your phone, surprised to find Violet staring at you. Your mind had been pretty far from your date; you nearly forgot where you were."
        show V Casual Blank
        V "You've barely said a word to me since we got here."
        show V Casual Pout
        show chelsea blank
        "Her eyes narrow on the phone in your hands."
        show V Casual Blank
        V "Does your club seriously need that much help?"
        show chelsea sad
        show V Casual Pout
        "It's not an order to put your phone away, but it may as well be. Usually you would find a way to punish her for it, but your guilt at texting Matt during a date with Violet overrides your kink."
        show chelsea embarrassed
        pcname "Ah, you're right..."
        show chelsea blank
        "You set the phone down on the table. Matt will just have to wait until dinner is over."
        "There's a slight awkwardness at the table as you both enjoy your meals-- especially with your phone buzzing-- but it eases as you refrain from looking at the device."
        show V Casual Smile
        "Violet waves the waitress over to order dessert, a relaxed smile on her face."
        show chelsea happy
        pcname "I'm going to the bathroom, I'll be right back. Order me something good."
        scene black with fade
        "Violet nods, already scanning the dessert menu. You walk off to the bathroom and take care of business."
        scene bg CityN
        show V Casual Annoyed at left
        with fade
        "As you make your way back to the table, you notice Violet bent over her phone, her face quickly deepening in various shades of furious red."
        show chelsea confused with dissolve
        pcname "What's up? Is everything okay?"
        show chelsea blank
        "You plop back into your chair, but Violet doesn't answer you right away; in fact, she doesn't even look at you."
        show chelsea shocked
        V "We need to talk. Now."
        scene black with dissolve
        "Violet turns the phone toward you and, with a sinking dread, you realize it's {i}your{/i} phone she's holding: and all of your conversations with Matt are front and center for the world to see."
    scene black with dissolve
    V "You have ten seconds to explain what I just looked at before I leave."
    pcname "Vi--"
    V "Nine seconds."
    "It's more than just anger in Violet's face-- although there's a lot of that, too. She's hurt."
    "And it's your fault."
    if mattsubmissive == True:
        "There's no good way to explain it-- you cheated on Violet, and you had enjoyed it. Any excuse you give is going to be just that: an excuse."
        scene black with dissolve
        "The best thing to do is tell the truth."
        if club == "track":
            pcname "I fucked up. It wasn't supposed to go this far, but I didn't know how to stop it. Every time I tried, he just pulled me back in."
        elif club == "cheer":
            pcname "It wasn't supposed to happen like this. I should've broken it off with him forever ago--"
            V "Of fucking course you should have."
            pcname "--but then he kept texting me and it just got out of control."
        elif club == "yearbook":
            pcname "I-I'm sorry... I-I wasn't-- I never meant-- I'm {i}sorry.{/i}"
            V "Did you even {i}try{/i} to stop it? Did you even tell him to fuck off or did you just jump on his cock like a little bitch?"
            "You drop your gaze to your lap, ashamed."
        scene black with dissolve
        V "So you {i}willingly{/i} cheated on me."
        pcname "I'm sorry. I... Vi, look, I care about you. I mean it. You mean the world to me..."
        V "Then why the hell are you sleeping with {i}Matt?{/i} Is that your way of showing you care?"
        pcname "I..."
        scene black with dissolve
        "You close your mouth and look away. There's nothing you can say that will justify your behavior."
        "Violet is silent for a long time. A part of you wonders if she got up and left and you just didn't hear her, but when you glance back up, Violet is there, glaring at you."
        scene black with dissolve
        V "You're a complete idiot."
        pcname "I... I mean, we never said if we were exclusive, and--"
        V "So instead of checking with me, you fucked Matt?"
    elif defymatt == True:
        scene black with dissolve
        if club == "track":
            pcname "Look, you're not going to believe me and that's fine, but Matt is blackmailing me."
            pcname "He took some photos of me in the shower and if I don't do what he says, he'll spread them all over the school."
        elif club == "cheer":
            pcname "Vi, honey, he's blackmailing me. You seriously think I would cheat on you because I {i}want{/i} to?"
            V "How is he blackmailing you?"
            pcname "He has some naked pictures of me in the shower."
        elif club == "yearbook":
            "You feel tears prick at your eyes but try to hold them back. You take in a deep, shuddering breath."
            pcname "P-please believe me, Vi. He's blackmailing me..."
            pcname "I never wanted to hurt you. H-He has photos of me showering and if I don't do what he says, he'll... he'll..."
            "You bite down on your lip to keep it from quivering. Just the thought of the school seeing those photos brings you to tears."
        "Violet's grip on her arms tighten, her knuckles turning white."
        V "You seriously expect me to believe that? How did he take pictures of you in the shower without you knowing?"
        pcname "He set up a camera somewhere. I know it's hard to trust me right now, but it's the truth."
        scene black with dissolve
        "Violet stares at you long and hard, her long nails digging hard into her blouse. Then--"
        V "Why the hell would you keep that a secret?"
        pcname "Who was I supposed to tell, Vi?"
        V "Me, duh!"
        pcname "I didn't want to. If Matt even finds out you know he's blackmailing me, he'll send them everywhere."
        V "As if! I could have squashed that asshole like a bug."
    scene black with dissolve
    V "Seriously, [pcname], don't you trust me?"
    menu violet_trust:
        "I do trust you." if True:
            pcname "Of course I trust you, Vi! I just..."
            "You bite down on your lip, the words harder to find than you imagined."
            pcname "I was scared to tell you. I'm sorry."
            scene bg CityN
            show V Casual Blank at left
            show chelsea shocked
            with dissolve
            V "If you trust me, then text him something for me."
            show chelsea confused
            pcname "Uh, okay. What do you want me to say?"
            show V SubCasual Happy
            show chelsea shocked
            V "Tell him you have a friend that wants to come over together and play with him, too."
            show chelsea blank
            show V Casual Pout
            "You blink, startled. Did you hear her correctly?"
            show chelsea sad
            if club == "track":
                pcname "What? Are you serious?"
            elif club == "cheer":
                pcname "Do you mean that?"
            elif club == "yearbook":
                pcname "Y-You want to... to..."
                show chelsea embarrassed
                "You feel a rush of heat color your face as you imagine yourself and Violet both entangled in one of Matt's sexual games."
            "Violet rolls her eyes and speaks to you as if she's talking to a child."
            show V Casual Annoyed
            show chelsea shocked
            V "Of course not. Are you stupid? I wouldn't touch that creep with a ten-foot-pole."
            show V Casual Blank
            show chelsea blank
            V "But we're putting an end to your relationship. Now."
            show V Casual Smile
            V "Now text him."
            show chelsea confused
            "With a slight nod, you do as told, confused and horribly curious about the mischievous look on Violet's face. What could she be planning?"
            call screen TextingScene("Matt",
            [
                TextMessage("Hey, are you home right now?", sender = False),
                TextMessage("Why? You that desperate to get a dick in you?"),
                TextMessage("I have a friend that wants to come over and meet you... among other things, if you're interested.", sender = False),
                TextMessage("Are you serious? Hell yeah."),
                TextMessage("I didn't know you had slutty friends that wanted to fuck around, too. Maybe you're not a complete idiot."),
                TextMessage("Now pick up her ass and go home. I'll be there in twenty."),
                TextMessage("Don't make me wait."),
            ])
            show chelsea shocked
            show V Casual Pout
            pause 1.0
            show V Casual Smile
            "Violet snatches the phone from your hand and views the messages with a smirk before reaching into her wallet and slapping some cash on the table."
            show chelsea blank
            show V Casual Pout
            "Swinging her purse over her shoulder, she stands up and gestures for you to follow her out of the restaurant."
            show V SubCasual Happy
            V "Come on. You are {i}not{/i} going to want to miss this."
            scene bg black with fade
            "Within ten minutes you're back at your apartment and seated on the couch."
            scene bg HomeN
            show chelsea
            show V Casual Pout at left
            with fade
            "You and Violet make yourselves comfortable-- or as comfortable as you can get, considering why you're here-- while you wait."
            show chelsea sad
            "Occasionally you glance over at Violet, but she seems completely immersed in her phone, tapping and scrolling relentlessly."
            "She's been that way since the restaurant, but you're a little scared to ask what she's doing. She's in a bad enough mood as it is."
            show chelsea shocked
            show V Casual Suprised
            pause 1.0
            show chelsea blank
            show V Casual Pout
            "A single knock at the door causes you to jump. You and Violet exchange a look: it's time."
            show Matt Casual Blank at right with dissolve
            "Matt barely acknowledges you as you open the door; his eyes are already scanning the apartment, searching for his new toy."
            show V Casual Smile at moveSprite(0.0, 0.75, 0.75)
            show Matt Casual Smirk
            "He smirks as his attention catches on Violet striding up behind you, phone clutched in her manicured palm. She smiles coldly at him, but Matt mistakes it for allure."
            show Matt Casual Pleased
            m "I knew a rich bitch like you would turn out to be another slut. All that money and it still can't buy you class."
            show V Casual Pout
            "Violet's eyes narrow but she doesn't move."
            show Matt Casual Smirk at moveSprite(1.0, 0.0, 1.0)
            show chelsea shocked
            pause 1.0
            show chelsea blank
            "Matt pushes past both of you and settles on the couch, his arms and legs spread wide as if he owns the place. Violet shuts and locks the door behind you, blocking the exit."
            show Matt Casual Question
            show chelsea sad
            m "What are you waiting for, slut? On your knees."
            show Matt Casual Smirk
            "Matt snaps his fingers at you and points to the empty spot in front of him."
            show Matt Casual Blank
            show V Casual Annoyed
            V "Is {i}that{/i} how you talk to girls? You're an even bigger loser than I thought."
            show Matt Casual Angry
            show V Casual Smile
            m "Don't act high and mighty now you whore. "
            show Matt Casual Blank
            V "About that..."
            show chelsea blank
            show V Casual Pout
            pause 1.0
            show V at moveSprite(0.75, 0.3, 0.5)
            "Violet presses a hand down on your shoulder-- a subtle signal to stay where you are-- and walks toward him."
            show V Casual Blank
            V "This is your mom, right?"
            show V Casual Pout
            "She holds out her phone, and although you can't see what's on the screen, you notice Matt's face pale slightly."
            show Matt Casual Question
            m "What about it?"
            show V Casual Blank
            show Matt Casual Blank
            V "Your mom is pretty-- sort of. She'd look better without that tacky 2015 haircut. But she knows how to decorate a house, huh?"
            V "That {i}is{/i} your house, isn't it?"
            show V Casual Pout
            "Violet continues to scroll through her phone, showing off what you assume are pictures of Matt's home. Even {i}you{/i} haven't seen what it looks like."
            show V SubCasual Happy
            V "And-- Oh, how weird. Her phone number just ended up on my screen. Do you think we should check in and let her know how much fun we're having?"
            show chelsea sad
            "Violet grins but it's all teeth; an animal whose caught their prey. You'd hate to be on the receiving end of that look."
            show chelsea blank
            "Matt barks a laugh."
            show Matt Casual Happy
            show V Casual Pout
            m "What? You're going to call my {i}mom?{/i} Are we in Kindergarten?"
            show Matt Casual Question
            m "What the hell are you going to tell her? That I'm having sex?"
            show V Casual Smile
            V "Maybe."
            show Matt Casual Blank
            V "Or maybe I'll tell her about you blackmailing girls at school, or that prostitution ring you have going on, or how you've been harassing [pcname] and probably half the other girls in our grade, too."
            show chelsea embarrassed
            "Matt stares at her, his face taking on a whole new shade of white. You've never seen Matt afraid before, especially not like {i}this{/i}."
            show V Casual Pout
            m "What the fuck are you talking about."
            "He tries to instill some confidence in his voice, but you can see the beads of sweat forming at the brim of his hairline."
            show V Casual Blank
            show Matt Casual Question
            V "Don't try to act cute. I know everything, and I have plenty of evidence to back me up."
            show V Casual Pout
            show Matt Casual Angry
            m "You don't have {i}shit.{/i} The only evidence you have is a load of crap."
            show Matt Casual Blank
            show V Casual Smile
            V "You think you're the only one with connections? Please. School boys are such amateurs."
            show V Casual Pout
            show chelsea blank
            "Violet scrolls on her phone once again. This time you catch a glimpse of one of the photos Matt took of you."
            show Matt Casual Angry
            m "How the hell did you get those?"
            "Violet practically rolls her eyes into the back of her head, tossing her hair over her shoulder."
            show V Casual Annoyed
            show Matt Casual Blank
            V "Again, {i}connections{/i}. Aren't you listening? Ugh, it's like talking to a brick wall."
            show V Casual Pout
            show chelsea sad
            show Matt Casual Angry at moveSprite(0.0, 0.05, 0.2)
            "Matt stands up from the couch and eases toward the front door. Whatever fear he showed before is gone now, replaced by a sort of panicked anger that sets all three of you on edge."
            "You can feel him glaring in your direction, each glance full of accusation. Well, it {i}is{/i} your fault, but you can't help making Vi a higher priority than his dick."
            show Matt Casual Smirk
            m "There's nothing on the prostitution ring. It's your word against mine."
            show V Casual Smile
            show Matt Casual Blank
            V "Or, you know, half a dozen guys' word against yours. Money really {i}will{/i} buy anything, you know?"
            show V SubCasual Happy
            V "And even without them it's {i}my{/i} word."
            show V Casual Pout
            show Matt Casual Question
            m "So?"
            show V Casual Blank
            show Matt Casual Blank
            V "Do you even realize how much my parents donate to the school? And you think they'll want a delinquent like {i}you{/i} running around?"
            show V Casual Smile
            V "Let me paint a picture for you, Matt. I want this to be crystal clear."
            show chelsea blank
            show V at moveSprite(0.3, 0.20, 0.20)
            "Violet stalks toward him, her chin raised high and arrogant. You stay firmly planted in front of the door; if Matt wants to leave, he'll have to take both of you down."
            show V Casual Blank
            V "You already have a pretty bad reputation with the school-- and by pretty bad, I mean you'll be lucky to work as a gas station attendant after graduation."
            show V Casual Smile
            V "But if any of these things got out? You don't just have me calling your mom to worry about. Oh no, you have your whole career-- your whole {i}future{/i} on the line."
            show V Casual Blank
            show chelsea embarrassed
            V "You think {i}any{/i} college is going to take you after this? Hell no. You'll be expelled, no college, and then what?"
            V "Your mom certainly won't want you, not after hearing about all of {i}this.{/i} Not to mention all the jail time you'll go through... Yikes. I'd hate to be in your shoes."
            show V Casual Smile
            "Violet is standing right in front of him now, her face just inches away from Matt's."
            "You feel bad for thinking so, but there's something hot about watching Violet go feral on him."
            show V SubCasual Happy
            V "Really Matt, you should thank me. I'm doing you a real favor."
            show Matt at moveSprite(0.05, 0.0, 0.2)
            "Matt stumbles a step back, putting some distance between them. The space seems to calm him down and help renew his confidence."
            show V Casual Pout
            m "You're forgetting one thing, bitch; I'm not going to jail."
            show Matt Casual Smirk
            m "My best friend's dad is on the force. You think he hasn't gotten me out of shit before?"
            show V Casual Smile
            show Matt Casual Blank
            "Violet's lips twitch into a smirk."
            V "Sweetie, who do you think signs your friend's daddy's checks?"
            show Matt Casual Smirk
            pause 1.0
            show Matt Casual Blank
            "Matt opens his mouth to make a smartass remark, but nothing comes out. You can almost see the realization click on his face like a lightbulb: he's fucked."
            show V SubCasual Happy
            "Violet's smile only grows smugger with his lasting silence, but the moment Matt clamps his mouth shut in defeat, her fake pleasantries drop."
            show V Casual Annoyed
            V "Now get out. And if you come near [pcname] again, my foot up your ass is going to be the {i}least{/i} of your problems."
            show chelsea blank
            show V Casual Pout
            show Matt Casual Angry
            pause 1.0
            show Matt at exitScene(0.0, 1.0, 0.4, 0.4)
            "Matt turns and Violet barely has time to nod for you to step away from the door before Matt pushes past, his face bright red with anger. Even when the door slams shut, you can hear his footsteps stomping as he retreats down the stairs."
            if violetrelate == 'Dom':
                "Violet dusts off her hands, as if even being in the same room as Matt has left grime on her palms."
                show V Casual Blank
                V "I've been wanting to call him out on his creepy behavior forever, but who knew he had so much dirt on him? So gross."
                show V Casual Annoyed
                show chelsea shocked
                V "Now. You."
                show chelsea sad
                "You feel your body tense as Violet turns on you. She beckons you forward with the curve of her finger."
                show V Casual Blank
                V "I'm still mad that you went through with his crap at all. If you do it again, I seriously won't forgive you."
                show V Casual Smile
                show chelsea shocked
                V "But you {i}were{/i} good during our little meeting. I guess that has to count for something."
                scene black with dissolve
                "Without warning, Violet leans forward and captures your lips with hers. You practically melt into her arms, eager to taste her."
                scene black with dissolve
                "She barely pushes her tongue into your mouth before pulling away, eliciting a small whine from the back of your throat. Violet smirks but leaves you hanging there, desperate for more."
                V "A {i}small{/i} something. I'll see how I'm feeling again tomorrow."
            elif True:
                show V SubCasual Blank
                "Violet slowly turns to you, her demeanor changing entirely. She glances at you nervously, a small, hopeful smile on her face."
                show chelsea shocked
                V "Did you like that, [pcname]?"
                "You stare blankly at her for a second. You're so thrown off by the change in behavior that it takes you a moment to register what she's doing."
                scene black with dissolve
                "With a grin, you pull her into your arms and cradle her close."
                if club == "track":
                    pcname "That was so cool, Vi. Way better than I imagined it'd go down."
                elif club == "cheer":
                    pcname "Vi, that was amazing! You're seriously the best!"
                elif club == "yearbook":
                    pcname "I... I really liked that. You did well."
                "Violet beams up at you, thrilled to hear your praise."
                V "Do you think I did well enough to get something in return?"
                "Her fingers play with the edge of your shirt. You pretend to think it over, but the grin tugging at your lips betrays you."
                pcname "Hmmm... Maybe."
                scene black with dissolve
                "You pull Violet forward and kiss her hard, forcing your tongue in her mouth. She moans against you, gripping the fabric of your shirt to pull herself even closer."
                "But after a few seconds, Violet pulls away."
                scene black with dissolve
                pcname "What's wrong?"
                V "Nothing! Really, nothing's wrong, I promise."
                pcname "But I thought you wanted something in return?"
                V "I do, but I need to let my dad know how everything went. If we're going to make sure he doesn't bother you again, some things need to be put into motion."
                V "But I'll text you as soon as I can! I mean, if that's okay?"
                pcname "Definitely. I'll look forward to it."
            scene black with fade
            "With the slight wave of her hand, Violet breezes through the front door and leaves you behind feeling a little more secure in your relationship."
            $ mattbreakup = True
            jump events_end_period
        "I don't think I can." if True:
            "Your lips part, ready to defend yourself and her, but nothing comes out."
            "A realization hits you: maybe you don't trust Violet."
            if mattsubmissive == True:
                "Why would you sleep with Matt unless you were sure Violet wasn't sleeping with other people? You aren't sure, and a part of that scares you. A part of it always has."
                "You didn't even realize how much it bothered you until now."
            elif defymatt == True:
                "Why didn't you tell Violet about the blackmail unless you trusted her? Are you afraid she will leave you? Or she would know and Matt would find out, and nothing could be done about him anyway?"
                "It breaks your heart a little to realize just how little you believed in Violet; how little you {i}still{/i} believe in her now."
            scene black with dissolve
            pcname "...I don't think I can trust you, Vi..."
            "Violet's jaw drops but she catches it quickly, her lips clamping together."
            V "That's {i}real{/i} funny coming from {i}you{/i}, [pcname]."
            V "I was willing to forgive you for this and work things out, but it's clear there's nothing here worth saving."
            V "Good luck with your fuckboy; you're seriously going to need it."
            scene black with dissolve
            "Violet stands up at once and strides out of the restaurant without looking behind. You watch her go, trying to ignore the squeezing pain of your heart."
            scene black with fade
            "It's for the best, you tell yourself."
            "Your phone buzzes again on the table. You don't hesitate to pick it up and continue sexting Matt."
            "He's all you have left, anyway."
            $ violetbreakup = True
            $ mattroutelock = True
            $ Cash =- 50
            jump events_end_period
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
