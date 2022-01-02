label cheer1:
    "You arrive for cheerleading practice in a great mood."
    "All of the girls seem similarly positive, chatting away excitedly in the locker room."
    show chelsea at right with moveinright
    "As practice starts, Ms. Vicky calls out a few names."
    show MV Blank at left with moveinleft
    "Ms. Vicky" "Emily, Olivia, Sarah, Carly! I need to chat with you girls a sec."
    show MV Smile at left
    "You glance at Olivia, who gives you a perplexed look in return."
    show Olivia Confused with moveinleft
    "Olivia" "I don't think I did anything wrong..."
    show chelsea happy
    pcname "I'm sure it's fine; maybe you did something good?"
    hide Olivia Confused with moveoutleft
    hide MV Smile with moveoutleft
    show chelsea blank
    "Tracy takes over leading the practice while the four girls walk a short distance away with Ms. Vicky."
    show bg Gym with fade
    show Tracy Blank at left with moveinleft
    "Tracy" "C'mon, ladies, we need to be in sync! Again!"
    show Tracy Smile at left
    "You actually sort of prefer Tracy's way of coaching - she's tough, but she still manages to motivate you rather than drag you down."
    "Ms. Vicky is nice, but you never feel like the team makes as much progress when she leads the practice."
    "After ten minutes or so, Tracy calls a break."
    hide Tracy Smile with moveoutleft
    "You grab your water bottle and smile at Olivia, who has just rejoined the group."
    show Olivia Sad at left with moveinleft
    show chelsea confused
    pcname "Well?"
    show chelsea blank
    "Olivia" "She... I..."
    pcname "Was it something bad?"
    "Olivia looks at the ground, nodding her head miserably."
    "Olivia" "She said that I... I need to lose some weight."
    show chelsea shocked
    pcname "What?"
    "Olivia" "She said that my thighs are too full and... And my boobs bounce too much when I'm practicing."
    show chelsea blank
    "You can't help but look at Olivia's body as she points out these supposed flaws."
    "You're sure Ms. Vicky was only trying to help, and maybe she's right - Olivia is a curvy girl with thick thighs and huge breasts - but to {i}say{/i} that..."
    menu cheer1_side:
        "Stand up for Olivia." if True:
            $ corruption -= 1
            "Frowning, you shake your head."
            show chelsea angry
            pcname "It doesn't matter why she said it, Ms. Vicky overstepped!"
            show chelsea happy
            pcname "And it's not like you're overweight... You're just curvy!"
        "Stand up for Ms. Vicky." if True:
            $ Oliviacorruption +=1
            $ corruption += 1
            "Shaking your head, you give her a tight smile."
            pcname "I don't think Ms. Vicky meant to hurt your feelings."
            show chelsea happy
            pcname "She seems really nice, so I'm sure she's just looking out for you."
    show Olivia Embarrassed at left
    "Olivia" "Thanks, [pcname]... I just..."
    "Olivia" "I'll think about it."
    show Tracy Blank with moveinleft
    "Tracy" "Alright, girls! Form up!"
    "As practice continues, you notice that Olivia isn't really putting her heart into it."
    "And you can't help but notice how much her large breasts make her stand out from the rest of the team."
    "Maybe Ms. Vicky {i}does{/i} have a point..."
    jump events_end_period

label cheer2:
    "As practice starts, Tracy tells the squad that Ms. Vicky couldn't be at practice, so she'll be leading again."
    "She goes over some of the harder routines, critiquing and complimenting each of the girl's moves."
    "It's hard work, doing each of the sets over and over again, and by the first break you're all tired."
    show Olivia Tired at left with moveinleft
    show chelsea happy at right with moveinright
    "Carly" "Ugh, I'm beat!"
    "Olivia" "Yeah, I should have brought an extra water bottle..."
    menu cheer2_tracy:
        "Complain." if True:
            show chelsea angry
            pcname "I know! Ms. Vicky never pushes us this hard!"
            show chelsea blank
            "Carly" "Right?"
        "Stay positive." if True:
            pcname "Tracy always pushes us so hard, but at least we're getting better?"
            "Carly" "I guess..."
    "Carly" "Um, can I ask you guys a question?"
    show Olivia Happy at left
    "Olivia" "Of course."
    pcname "Sure!"
    "Carly" "It's just... Last practice, Ms. Vicky said my hair was frizzy and dry, so I've been using a bunch of products, but I can't tell if they're working."
    "Carly" "Do you think my hair looks any better?"
    show chelsea blank
    show Olivia Blank at left
    "You look at Carly's hair critically, trying to remember what it looked like before today..."
    show Olivia Embarrassed at left
    "Olivia" "She told me I needed to lose weight!"
    "Carly" "What? Seriously!?"
    show Olivia Sad at left
    "Olivia" "Yeah, my thighs are too thick and my boobs are too big, she said."
    "Carly" "How can your boobs be {i}too{/i} big? I'd kill to be as thin as you with boobs like that!"
    "Just as you open your mouth, Tracy walks over."
    show Tracy Blank with moveinleft
    "Tracy" "Is there a problem, girls?"
    "Carly" "Ms. Vicky told Olivia to lose weight! And she told me that my hair is frizzy!"
    show Olivia Blank at left
    "Olivia" "I-- I just--"
    show Tracy Question
    "Tracy" "Carly, your hair {i}is{/i} frizzy. You bleach it at home instead of going to the salon."
    "Tracy" "You're lucky it grows at all with the way you treat it."
    "Carly's mouth falls open in shock. She tries to think of something to say - her mouth moves, but no words come out."
    "Carly" "Hmmph!"
    "Folding her arms over her chest, she turns and storms off."
    show Tracy Blank
    "Tracy" "And Olivia..."
    show Olivia Sad at left
    "Tracy" "...you're new, so I don't expect you to understand yet."
    "Tracy's features soften, but her determination doesn't fade."
    "Tracy" "But Ms. Vicky takes her job really seriously. As cheerleaders, it's important that we all look our best."
    "Tracy's words seem to sink in - even you have to admit she makes a good point."
    "Olivia" "I understand, it's just-- I don't know..."
    "Tracy sighs."
    "Tracy" "Look, just think about what Ms. Vicky said and give it a shot."
    "Tracy" "Nothing bad can come from eating healthier, right?"
    "Olivia" "I... I guess that's true."
    show Tracy Smile
    "Tracy smiles at Olivia, giving her an encouraging nod, and then walks back to the front of the group."
    show Tracy Laugh
    "Tracy" "Alright! We're not ending practice until we get this right!"
    "True to her word, Tracy keeps running the team through the routine until it's {i}perfect{/i}."
    "By the end of practice, you're covered in sweat and too tired to worry about Olivia anymore."
    jump events_end_period

label cheer3:
    show chelsea at right with moveinright
    "Just as you arrive at the school, a loud crash of thunder roars through the sky."
    hide chelsea with moveoutright
    "In the locker room, Ms. Vicky comes in just as everyone finishes changing into their uniforms."
    show chelsea at right with moveinright
    show MV Smile at left with moveinleft
    "Ms. Vicky" "It'll be a short practice today! I just want to go over a few things with you girls!"
    "She smiles, looking around the room, and claps her hands together."
    show MV Blank at left
    "Ms. Vicky" "We need to talk about what it means to be a cheerleader and how that should affect you outside of the club."
    "Ms. Vicky" "Can anyone tell me what cheerleaders do?"
    "Her eyes scan the room; of course it's Tracy who answers."
    show Tracy Blank with dissolve
    "Tracy" "We excite the audience and encourage the athletes."
    show MV Laugh at left
    "Ms. Vicky" "Exactly! Thanks, Tracy!"
    hide Tracy Blank with dissolve
    show MV Blank at left
    "Ms. Vicky" "Now, you've all been practicing your routines, so you know the primary way we motivate our boys."
    "Ms. Vicky" "But I want you to think of {i}other{/i} ways your behaviors might impact them."
    "She pauses for effect, meeting each girl's eyes in turn."
    "Ms. Vicky" "For example: if a guy asks you on a date, as long as he's athletic, you should give him a chance."
    "There's a quiet murmur from some of the girls, but a single voice cuts through it."
    "You're surprised to hear Olivia speaking up."
    show Olivia Confused with dissolve
    "Olivia" "What!? Who we date has nothing to do with being a cheerleader!"
    show MV Smile at left
    "Ms. Vicky smiles, clearly expecting this question, but before she can respond, Tracy chimes in."
    hide MV Smile with dissolve
    show Tracy Angry at left with dissolve
    "Tracy" "What do you mean? Of course it does!"
    "Tracy" "If you turn down one of the football players and he sees you cheering on the sidelines during a game, how do you think that'll make him feel?"
    "Tracy" "Do you think he'll play his best - or will he be distracted?"
    show Olivia Blank
    "Olivia shakes her head, opening her mouth to disagree again, but Ms. Vicky quickly cuts in."
    hide Tracy Angry with dissolve
    show MV Blank at left with dissolve
    "Ms. Vicky" "Exactly my point. Think about it..."
    "Ms. Vicky" "Having pretty girls cheering them on makes the guys play harder to impress them."
    hide Olivia Blank with dissolve
    "Ms. Vicky" "But, if they have bad encounters with those girls, they'll be discouraged instead."
    "Ms. Vicky" "That's why it's important that you give them a chance."
    show MV Smile at left
    "Ms. Vicky" "Nobody is saying you have to date them - just that you flirt a little and don't turn them down too hard."
    "Many of the girls nod their heads. You have to admit, they make some good points."
    "You've seen how hard guys can take rejection, so it's easy to see how they might be distracted or discouraged if they have to see the girl who rejected them during games."
    show MV Laugh at left
    "Ms. Vicky" "Okay! That's all for today then, girls. Go have some fun with the rest of your weekend!"
    show MV Smile at left
    "She waves, smiling at everyone, and motions for Tracy to come talk to her."
    hide MV Smile with moveoutleft
    "As the other girls begin changing, Olivia turns to you."
    show Olivia Confused at left with moveinleft
    "Olivia" "Do you really think we should flirt with guys just because they're on sports teams?"
    menu cheer3_flirt:
        "Agree with Ms. Vicky." if True:
            $ Oliviacorruption +=1
            $ corruption +=1
            pcname "I mean, it makes sense."
            pcname "And it's not like we have to do anything except be nice to the guys."
            show Olivia Sad at left
            "Olivia" "I guess so..."
            "Olivia" "I just... It doesn't seem right. I can't explain it."
            "You try to be sympathetic, but it kind of seems like she's just being uptight."
            show chelsea happy
            pcname "Maybe that's because it doesn't make any sense?"
            show Olivia Confused at left
            "Olivia" "What...?"
            show chelsea confused
            pcname "They have a good point and you don't like it but you can't explain why?"
            show Olivia Sad at left
            "You pat her shoulder, sorry to upset her."
            show chelsea blank
            pcname "They're right, Olivia. It's our job to motivate the players and we can't do that if we're rude to them."
            show Olivia Blank at left
            "Olivia" "But turning them down isn't being rude, it's just--"
            pcname "Ms. Vicky didn't say you have to sleep with them; just flirt and let them down gently."
            show Olivia Sad at left
            "Her bottom lip trembles, but she nods."
            show Olivia Embarrassed at left
            "Olivia" "Maybe you're right..."
        "Agree with Olivia." if True:
            $ corruption -= 1
            show chelsea confused
            pcname "I see what she means, but it makes me uncomfortable."
            show chelsea blank
            pcname "Just because we're cheerleaders doesn't mean we have to date athletes..."
            show Olivia Blank at left
            "Olivia" "Right!?"
            "Vindicated by your agreement, Olivia's resolve grows stronger."
            "Olivia" "Why should we have to flirt with guys we're not interested in?"
            "Olivia" "Because they're on sports teams?"
            "Olivia" "We're supposed to support them at the games, not anywhere else!"
            "Her voice grows louder as her courage grows; you glance around, motioning for her to be quieter."
            show Olivia Embarrassed at left
            "She realizes her mistake and blushes."
            show Olivia Blank at left
            "Olivia" "Sorry!"
            show Olivia Sad at left
            "Olivia" "I just... Nobody else seems to think this is weird."
            show Olivia Blank at left
            "Olivia" "Even Carly is buying it..."
            "You shrug, trying to de-escalate the situation."
            show chelsea happy
            pcname "Carly is... Carly. She can't remember what she thinks."
            show Olivia Laughing at left
            "Olivia giggles; Carly is notoriously ditzy."
    show Olivia Happy at left
    "Olivia" "I have to get going, but thanks, [pcname]."
    pcname "Me too! See you later?"
    hide Olivia Happy with moveoutleft
    "She smiles at you, but she still looks troubled."
    "As you change, you wonder why Olivia is having such a hard time."
    "Tracy and Ms. Vicky are doing their best to make the team successful, and even if you don't quite agree with everything they say, you know their hearts are in the right place."
    jump events_end_period
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
