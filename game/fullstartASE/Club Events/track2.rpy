label track1:
    show chelsea at right with moveinright
    "It's weight room day again."
    "After stretching and some warm-up laps, the team heads to the weight room."
    "You finish your laps faster than before; it's exciting to see some improvement, even if you're not the fastest on the team."
    "As everyone files into the weight room, the coach blows his whistle."
    show CC Serious with moveintop
    "Coach" "I just got a call that I have to run home for. You guys know the drill by now."
    "Coach" "Do your reps on your own and don't slack off just 'cause I'm not here!"
    "The team exchanges some concerned glances, but quickly get in position for their squats."
    hide CC Serious with moveoutright
    "There's some confusion about how to track the time, but since one of the team is on crutches, she volunteers to keep track."
    "Teammate" "Okay... Go!"
    "You do your squats, but without the coach watching it's hard to really feel motivated."
    "Lunges, jump rope, sit-ups... The team goes through the motions, but it's obvious there's no pressure to perform well."
    "As you finish your planks, though, Ryan stands and shouts to August."
    show Ryan Angry at left with moveinleft
    "Ryan" "Hey, August! Bet I can do more crunches than you!"
    show August Confused with dissolve
    "August" "Psh. You wish!"
    "A round of amused snorts and giggles circles the room; all eyes are on the two competitors."
    show August Blank
    show Ryan Happy
    "Everyone gets into position, but few actually do their own crunches as Ryan and August shout out their own counts."
    "Ryan takes a strong lead, but quickly slows as his speed gets the best of him."
    "August starts off slower, but her steady pace allows her to overtake him at the seven minute mark."
    "As soon as she pulls ahead, though, Ryan redoubles his effort - and for another couple of minutes, he gets well ahead."
    "However, just as before, he can't maintain that pace for long and by the thirteen minute mark they're practically tied."
    "That's when August's patient, steady pace really pays off; she has the reserved energy to go all out for the last two minutes, while Ryan struggles to keep up."
    "In the end, August beats him by sixteen crunches."
    show chelsea shocked
    show Ryan Tired
    "Ryan" "I had you! I was so far ahead!"
    show chelsea blank
    show Ryan Angry
    "He jumps to his feet, face red with anger and exertion."
    "Ryan" "This is crazy! I can't keep losing to you!"
    show August Disappointed
    "Almost growling, he storms out of the weight room."
    "You want to help - Ryan was really nice to you when you met - but you're not sure if he's in any mood to talk."
    "You could try talking to August, but she doesn't seem to like you. Or anyone, for that matter."
    menu track1_convo1:
        "Talk to Ryan." if True:
            hide August Disappoint with dissolve
            $ track1_convo = "Ryan"
            "While everyone whispers about what just happened, you slip into the hallway."
            hide chelsea with moveoutright
            show bg black with fade
            pause 0.3
            show chelsea at right with moveinright
            "Ryan stands just down the hall - as you approach, he kicks a locker."
            "Ryan" "UGHHH!"
            "You pause, wondering if you should go back inside, but he notices you before you have the chance."
            show Ryan Worry
            "Ryan" "Oh, hey [pcname]..."
            "He glances at the locker and smiles apologetically."
            show Ryan Happy
            "Ryan" "Uh... Sorry."
            show Ryan Worry
            "Ryan" "I just... I hate it that she always beats me."
            "Ryan" "At everything."
            "You walk closer, more comfortable now that he seems calmer, and let him vent."
            show Ryan Happy
            "Ryan" "I guess I've always been competitive, you know?"
            "Ryan" "But until August joined halfway through freshman year, it didn't really matter; I was always the best."
            "Smiling ruefully, he sighs."
            show Ryan Angry
            "Ryan" "Now I'm always {i}second{/i} best. And she makes it look so easy!"
            show chelsea happy
            pcname "I just wish I was half as good as either of you."
            show Ryan Laugh
            "He laughs - it almost sounds genuine."
            show Ryan Happy
            "Ryan" "You joined too late, but you're not doing that bad."
            "Ryan" "Anyway... I guess I should go back in there. She's probably laughing at me right now..."
            "Ryan" "Thanks for listening, [pcname]. I really appreciate it."
            "You walk down the hallway together and he holds the door for you to enter the weight room."
            show chelsea blank
            "Inside, August looks up from her spot on the floor and meets your eyes - then Ryan's."
        "Talk to August." if True:
            $ track1_convo = "August"
            "You approach August tentatively - you haven't forgotten her gruff demeanor when you first met."
            "She's still sitting on the floor, as if in a daze."
            show August Neutral
            "August" "I don't get it... He's the one who challenged {i}me{/i}."
            show August Blank
            "She doesn't acknowledge your presence, but she keeps talking anyway."
            show August Neutral
            "August" "Every time I think we're having fun, he makes a big deal about it..."
            show August Blank
            "Finally, she looks up at you, her purple eyes catching you off guard."
            show August Neutral
            "August" "Look, I know you probably don't care, but... Track has really helped me deal with... some things."
            show August Blank
            "She pauses, looking away, and you get the impression there's more to it, but she doesn't share."
            show August Neutral
            "August" "I know I take it too seriously sometimes but... I just can't help it."
            show August Blank
            "Pushing her black and purple hair out of her eyes, she looks up at you again."
            show August Neutral
            "August" "And Ryan... He's always pushed me harder. If it wasn't for him, I don't know what I'd do."
            "August" "I don't know where I'd {i}be{/i}. He always makes me {i}work{/i} for it. I--"
            show August Blank
            "Her voice breaks off and you turn, following her line of sight."
            "Your eyes meet Ryan's, but he's staring at August."
    if track1_convo == "August":
        "As Ryan approaches, August stands."
        show Ryan Worry
        "Ryan" "Look, I--"
        show August Confused
        "August" "Hey, I'm sorry. I didn't mean to embarrass you or whatever."
        "Ryan stares at her a moment, surprised that she apologized first."
        show Ryan Happy
        "Ryan" "Thanks, I... I shouldn't have taken it so seriously."
        show August Disappointed
        "August" "No, you were kind of a jerk, but it's okay."
    elif True:
        "August stands as Ryan approaches her."
        show August Neutral with dissolve
        "August" "Hey, I--"
        show August Blank
        show Ryan Worry
        "Ryan" "Look, I'm sorry, okay?"
        "He sighs."
        show Ryan Happy
        "Ryan" "I overreacted and I'm an asshole."
        show August Confused
        "August" "I mean, yeah, but... Apology accepted."
        show August Blank
    show chelsea happy
    "He rolls his eyes, but his familiar smile returns."
    "Since they seem to have worked things out, it seems like a good time for you to excuse yourself."
    jump events_end_period

label track2:
    show chelsea at right with moveinright
    "You start stretching as soon as you get to practice. The sky is gray and overcast, but you know the breeze will feel good when you start running."
    show CC Serious with moveinleft
    "Coach" "Sprints today! Warm-up laps first, though, so get moving!"
    hide CC Serious with dissolve
    "You run your three laps, barely feeling out of breath as you finish."
    show chelsea happy
    "The more you run, the more you seem to enjoy it!"
    "As the last of the team crosses the finish line, the coach blows his whistle again."
    show CC Serious with dissolve
    "Coach" "Alright, ladies - back in position!"
    "Coach" "First of fifteen!"
    "He blows his whistle and you take off, smiling as August and Ryan shoot ahead of everyone else."
    hide CC Serious with dissolve
    "Each lap follows the same pattern, with August always pulling ahead just before the finish line."
    "By the time you get to the tenth sprint, you can see Ryan getting more and more frustrated."
    "During the thirteenth, they're neck-and-neck heading toward the finish line when August once again pulls ahead."
    show chelsea shocked
    "Suddenly, though, just short of the finish line, August stumbles, pitching forward and taking a hard fall."
    show chelsea blank
    "Ryan darts past her, crossing the finish line before August even begins to recover."
    "Ryan" "YES! FINALLY!"
    "He shouts his triumph, waving his hands in the air."
    "Behind him, August lays on the ground, cradling one knee."
    "As Ryan turns, still celebrating, he sees her there; his arms fall immediately."
    "Ryan" "August!"
    "He rushes to her side, only to be pushed away."
    "August" "You got your win, don't pretend you care now!"
    show CC Neutral at midright with moveinright
    "Coach" "Break it up, you two. August, are you okay?"
    show CC Blank at midright
    "She pulls herself to her feet, limping a few steps."
    show CC Serious at midright
    "Coach" "Someone help her to the bleachers."
    show CC Blank at midright
    menu track2_convo:
        "Help August." if True:
            show chelsea sad
            $ track2_convo = "August"
            "You rush to August's side, putting her arm around your shoulder."
            show August Neutral with dissolve
            "August" "I'm fine, I--"
            show August Blank
            "She tries to push you away, but stumbles on her injured leg."
            show chelsea blank
            show August Neutral
            "August" "Okay, okay... I just need to sit a bit."
            "This time she allows you to help her, leaning on you with every step."
            "As she sinks to the bleachers, she runs her hands through her hair."
            show August Angry
            "August" "I can't believe I screwed up like that..."
            "August" "I was a yard ahead of him; I had it in the bag!"
            show August Confused
            "August" "And Ryan... He only cared that he won; he didn't even notice I was hurt."
            show chelsea happy
            if track1_convo == "August":
                pcname "It did take him a while, but he {i}did{/i} try to help eventually..."
            elif True:
                pcname "He was just caught up in the race - as soon as he realized you were hurt, he tried to help."
            show chelsea blank
            "As you're speaking, Ryan approaches."
        "Talk to Ryan." if True:
            $ track2_convo = "Ryan"
            "You wait until August hobbles away, leaning against another runner, before you approach Ryan."
            show Ryan Worry at left with moveinleft
            "Ryan" "Shit... I didn't think she was actually hurt!"
            "Ryan" "I saw her stumble, but..."
            "He covers his face with his hand, rubbing his eyes."
            "Ryan" "And now I can't even celebrate beating her because I didn't {i}really{/i} win."
            if track1_convo == "August":
                show chelsea confused
                pcname "Ryan... Don't you think your friendship should be more important than winning anyway?"
                show chelsea blank
                pcname "August is your team mate, not your opponent."
            elif True:
                pcname "Ryan... I know you were used to winning before she came around, but..."
                pcname "Winning isn't everything, you know?"
                pcname "We're all on the same team."
            "He stares at you a moment, contemplating your words."
            show Ryan Tired
            "Ryan" "Yeah, you're right..."
            "Before you know it, he's marching off in August's direction, leaving you no choice but to follow."
    show Ryan Worry at left with moveinleft
    "Ryan" "Hey--"
    show August Angry
    "August" "Forget it; I don't want your apology."
    "Ryan" "I just wanted to see if you were okay. I--"
    "She glares at him, her purple lipstick smeared from her fall."
    show August Confused
    "August" "Whatever. I'm fine."
    "Ryan" "Look... We're teammates, August. I know I forget that sometimes, but..."
    "Ryan" "Can we just agree to focus on that instead of competing?"
    "She watches him a moment, confusion written all over her face."
    "Ryan" "Forget it. I was a jerk, and I--"
    show August Neutral
    "August" "No. You're right..."
    "August" "Let's stop competing so much."
    show August Blank
    show Ryan Happy
    "They stare at each other, and for a moment you think that even agreeing will somehow become a battle, but then Ryan smiles."
    show chelsea happy
    show August Happy
    "And, to your surprise, August smiles back."
    show CC Happy at midright
    "Coach" "Okay, if the marital dispute is over, we have two more sprints to run! August, you're on the bench until next practice!"
    "You expect her to argue, but she only nods - her familiar scowl firmly reaffixed."
    "Running the last two sprints, you feel like you've made a difference in their relationship - at least until August's knee is better."
    jump events_end_period

label track3:
    show chelsea happy at right with moveinright
    "You arrive at the track a little early and start your stretches."
    "August walks onto the track confidently, her limp seemingly healed."
    show chelsea blank
    "Ryan arrives a short time later and begins his own stretches, but the two don't seem to be talking any more than usual."
    "It looks like they're back to their old routine."
    "A little disappointed, you get ready for your laps."
    "As the last of the team gets ready, the coach blows the whistle."
    "August and Ryan quickly shoot ahead, running neck-and-neck around the first turn."
    "You can tell by their determination that they're both trying to beat the other."
    "Ryan edges ahead at the end of the first lap, but you've seen this play out enough times to know that by the end of the third, August will overtake him again."
    "And, just as you predicted, halfway through the third lap August lets loose."
    "To your surprise, though, she has a hard time passing him. As they reach the finish line, it looks like an even race."
    "As usual, though, August edges ahead of him and crosses first."
    "As you cross the line, you see Ryan approach August."
    show Ryan Happy at left with moveinleft
    "Ryan" "Shit... That was tough..."
    "He turns to August, grinning."
    "Ryan" "You win again. Congratulations."
    "All eyes are on him and a few people gasp in disbelief."
    show August Happy with dissolve
    "August smiles back, generating several more gasps."
    "August" "Yeah, you're making it harder every time. Soon you'll definitely beat me!"
    show Ryan Laugh
    "Ryan" "Count on it!"
    show August Laugh
    "They share a laugh, leaving everyone around them exchanging confused looks."
    show CC Serious at midright with moveinright
    hide August Laugh with dissolve
    hide Ryan Laugh with dissolve
    "Coach" "Alright! Endurance laps - 45 minutes on the track. I want to see you moving!"
    hide CC Serious with dissolve
    "For 45 minutes, you run the track, stopping occasionally for a drink."
    "There's no time to talk until you're done, but as you walk off the track, you hear a voice calling to you."
    if track1_convo == "August" and track2_convo == "August":
        show August Happy
        "August" "Hey, thanks for helping me last time. And for talking to me before."
        show chelsea shocked
        pcname "Oh... You're welcome."
        show chelsea happy
        "August" "And you were right; Ryan isn't so bad."
        "You smile. Maybe they {i}have{/i} learned something."
        "August" "Anyway, we're going to get some food."
        show August Laugh
        "August" "Ryan thinks he can eat more than me, so it's game on!"
        "She gives you a rare smile - with more edge than some of her glares - before joining Ryan."
        hide August Laugh with moveoutleft
        "At least they've taken their rivalry off the field?"
    elif track1_convo == "Ryan" and track2_convo == "Ryan":
        show Ryan Happy at left
        "Ryan" "Hey, sorry, I just wanted to say thanks."
        "Ryan" "It means a lot to me that you talked me down in the hallway, and when August fell."
        "His lips turn up in a sheepish half-smile."
        show chelsea happy
        pcname "Oh, of course! It's not a problem!"
        show Ryan Laugh
        "Ryan" "Well, you were right; the team is about more than just me."
        "You smile - it's good to see they've learned from their mistakes."
        show Ryan Happy
        "Ryan" "That's why we're taking it off the field now."
        show Ryan Angry
        "Ryan" "I challenged her to an eating contest and I'll definitely win!"
        "He pumps his fist to emphasize his point."
        show Ryan Happy
        "As he walks back toward August, you wonder if he really learned anything at all..."
        hide Ryan Happy with dissolve
    elif track2_convo == "August":
        show August Happy
        "August" "Hey, thanks for helping me last time... I've never taken a fall that hard!"
        show chelsea happy
        pcname "No problem!"
        "August" "And you were right; Ryan isn't so bad."
        "You smile. Maybe they {i}have{/i} learned something."
        "August" "Anyway, we're going to get some food."
        show August Laugh
        "August" "Ryan thinks he can eat more than me, so it's game on!"
        hide August Laugh with moveoutleft
        "She gives you a rare smile - with more edge than some of her glares - before joining Ryan."
        "At least they've taken their rivalry off the field?"
    elif True:
        show Ryan Happy at left with moveinleft
        "Ryan" "Hey, sorry, I just wanted to say thanks."
        show chelsea confused
        pcname "For what?"
        "Ryan" "Talking to me last time, when August fell."
        show chelsea blank
        "His lips turn up in a sheepish half-smile."
        show chelsea happy
        pcname "Oh, of course! It's not a problem!"
        show Ryan Laugh
        "Ryan" "Well, you were right; the team is about more than just me."
        "You smile - it's good to see they've learned from their mistakes."
        show Ryan Happy
        "Ryan" "That's why we're taking it off the field now."
        show Ryan Angry
        "Ryan" "I challenged her to an eating contest and I'll definitely win!"
        "He pumps his fist to emphasize his point."
        show Ryan Happy
        "As he walks back toward August, you wonder if he really learned anything at all..."
        hide Ryan Happy with dissolve
    jump events_end_period
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
