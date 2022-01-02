label track4:
    scene bg TrackD
    "Your body aches as you jog around the track, your muscles still tight and sore despite your early morning stretches."
    "Music plays through your wireless headphones as you finish another lap."
    "The steady rhythm of your pounding feet paired with the beat makes it easier to keep going."
    "After another couple of warm up laps, you're feeling pumped and ready to start the day!"
    show CC Blank with dissolve
    "Coach watches as the rest of your team trickles in from the end of their laps, one or two of them doubling over for air."
    "The start of the morning is always the hardest."
    "Coach's whistle rings out across the field, grabbing your team's attention."
    show CC Neutral
    "Coach" "Alright, take five! We start running bleachers after."
    hide CC with dissolve
    "Multiple groans sound out over the field, including your own. As effective as the coach's training regimen might be, it doesn't mean you have to enjoy {i}every{/i} exercise."
    $ clothes = "track"
    show chelsea sad at center, moveSprite(-0.2, 0.9, 0.85)
    "You make your way over to the bleachers and plop down, the cold aluminum still damp with early morning dew."
    show chelsea blank
    "As you lean back against the metal seats, you spy August making her way toward you with two water bottles in hand. When she's close enough, she holds one out to you."
    show August Neutral with dissolve
    "August" "Want one, [pcname]?"
    show August Blank
    show chelsea happy
    pcname "Sure."
    show chelsea embarrassed
    show August Happy
    "You accept the water bottle and chug a third of it down. The cold water feels nice and refreshing against your throat."
    show August Blank
    "August lingers by your side for a moment longer before sitting down next to you. She sips at her own water, a thoughtful look on her face."
    show chelsea blank
    "You set your bottle down on the bench and wipe the excess water from your mouth with the back of your hand."
    show chelsea happy
    show August Confused
    pcname "Whatcha thinking about?"
    show chelsea blank
    "August" "Huh?"
    show August Blank
    "August's eyes widen as if you've snapped her from a daze. She shrugs, staring back out across the field."
    show chelsea confused
    show August Neutral
    "August" "Nothing really."
    show August Blank
    "You find that hard to believe."
    show chelsea blank
    "Over on the track field, you spot Ryan goofing off with a few of his buddies on the team. He seems more relaxed than you're used to seeing him."
    "Out of the corner of your eye you see August also staring off in his direction, an unreadable expression on her face."
    show chelsea happy
    "She's good at hiding her emotions, but you're sure you see a hint of warmth in her eyes."
    show chelsea laugh
    pcname "You and Ryan have been getting along lately."
    show chelsea embarrassed
    show August Confused
    "August" "Hm."
    show chelsea confused
    show August Blank
    "She doesn't give you more than that. You look between them curiously, both confused and grateful by their change of heart. It's nice to not see them fighting all the time, at least."
    show chelsea blank
    pcname "You guys just don't seem to be taking your rivalry as seriously anymore."
    show chelsea embarrassed
    show August Confused
    pcname "It's a nice change."
    show chelsea blank
    "August" "You don't think we're serious about it?"
    show August Blank
    "August's eyebrows raise in surprise, as if she too is just noticing this for the first time. She looks back at Ryan in utter concentration, her lips pressed into a thin line; she almost looks disturbed by the idea."
    show August Confused
    pcname "Not as much as you were when we started, at least."
    show chelsea happy
    pcname "It's more of a friendly competition now."
    show chelsea blank
    show August Blank
    pcname "That's how I see it, anyway."
    "August shrugs, taking another sip from her water bottle."
    show August Neutral
    "August" "For now. There's no real stakes right now, so it's easy to let it slide."
    show chelsea confused
    "August" "We'll see how long that lasts once the track meets start."
    show August Happy
    pcname "Track meet?"
    "August nods, a small smile curling on her face."
    show chelsea shocked
    show August Laugh
    "August" "First track meet starts in a couple of weeks."
    "August" "We have a lot of preparation to do if we want to win."
    show chelsea embarrassed
    show August Happy
    "Her eyes light up at the thought of it and you can practically see the desire to run out across the field reflecting in her gaze."
    show chelsea sad
    "You had completely forgotten about the track meet, having been so preoccupied with everything else going on in your life."
    "Is it really coming up so soon? You thought you would have more time to prepare, but a few weeks is hardly enough time to get into your best shape."
    show chelsea blank
    show August Blank
    "It looks like you'll have to do a lot more practicing if you want to be ready for the first meet."
    show chelsea embarrassed
    show August Disappointed
    "August finishes off her water bottle and chucks it into a nearby recycling bin. It bounces off the rim and, with a sigh, she gets up to place it into the bin."
    show August Blank
    "She returns shortly after, resuming her seat beside you."
    show chelsea blank
    show August Neutral
    "August" "Are you excited for the track meet?"
    menu trackmeetexcitement:
        "I'm pumped!" if True:
            show chelsea laugh
            show August Happy
            "You grin back at her, a new sort of anticipation flowing through your veins."
            show chelsea happy
            pcname "Definitely! I'm pumped!"
            pcname "I can't wait to get on the track and compete with everyone."
            show chelsea embarrassed
            "You can't help but look back at the field, picturing yourself racing across the burnt red rubber."
            show chelsea angry
            show August Confused
            pcname "Maybe I'll even beat you this time."
            show chelsea blank
            show August Blank
            "There is a challenge in her eyes when August looks back at you."
            show August Angry
            "August" "I'd like to see you try."
            "August" "You have a lot more practicing to do if you're going to beat me."
        "I'm working up to it." if True:
            show chelsea embarrassed
            show August Happy
            pcname "I'm working up to it. I don't think anyone is as excited as you."
            "August grins, her dyed hair shining as the sun breaks out from the cloudy sky."
            "Your own muscles ache at the thought of putting in more effort, but you smile back in encouragement."
            "As your time on the track team has progressed, so have your muscles. You're able to do a lot more now physically than you thought possible before."
            "With more practice will come more strength and endurance. You just have to keep exercising and eventually you'll get there."
    show CC Serious at left with dissolve
    show chelsea shocked
    show August Confused
    "Coach" "Time's up! Line up!"
    scene black with fade
    "There are a few mumblings of discontent as everyone drops what they're doing and marches back into a line across the track field."
    "You follow behind, mentally preparing yourself for the next exercise."
    jump events_end_period

label track5:
    scene bg TrackD
    pause 0.8
    $ clothes = "track"
    show chelsea sad at center, enterScene(0.9, 0.5, 0.6, 0.5)
    "You arrive to the track field later than usual, just barely having enough time to change into your uniform and practice your morning stretches before you have to line up along the track."
    show Ryan Happy at left with dissolve
    "Everyone else is already there, and Ryan gives you an amused smirk from across the line as you get into position. It's almost as if he {i}knows{/i} your alarm didn't go off this morning and wants to tease you about it."
    hide Ryan with dissolve
    show CC Serious at left with dissolve
    "Coach gives you a warning look before pressing his lips to his whistle and blowing hard."
    scene black with fade
    "You take off, your legs pumping hard against the rubber ground as you try to keep up."
    "You still feel slow and sluggish as you round the first bend. You already ran to the school to make it here on time, and now the extra exercise leaves your calves and side burning."
    "Ryan and August are near the front, as usual. You see them race neck-and-neck, each one barely moving ahead of the other in their early morning race."
    "You can't imagine having the energy to race against either of them this morning, but they seem to thrive as the sun's glare beats down just after the break of dawn."
    "You pick up the pace a few times as you make your usual laps, eager to end this early so you can ease the stitch in your side."
    "Coach blows his whistle each time someone passes, marking their completion of another lap."
    "You close your eyes as you run past. Five more laps to go."
    "Four."
    "Three."
    "Two."
    "By the time you complete your final lap, you're nearly ready to collapse onto the bright green turf."
    scene bg TrackD with fade
    pause 1.0
    show chelsea embarrassed at center, enterScene(-0.2, 0.5, 0.6, 0.6)
    "Instead, you make your way to the cooler of water bottles and grab one, chugging hard. Hopefully the hydration will keep you awake."
    show chelsea shocked
    "Coach's whistle echoes over the track, drawing everyone's attention."
    hide chelsea with dissolve
    pause 1.0
    show CC Serious with dissolve
    "Coach" "Five minute break! Be quick; we start with lunges when you get back!"
    hide CC with dissolve
    "A soft murmur falls over the team as your teammates relax and fall into their usual cliques and conversations."
    show chelsea sad at center, enterScene(0.5, 0.8, 0.6, 0.5)
    "The painful cramp in your side still aches as you sit down on the turf and take deep steady breaths. God, you wish you had more time to stretch this morning..."
    show Ryan Laugh at left with dissolve
    "Ryan spots you across the track and waves, his long arm flailing in the air before he bounds toward you."
    "The stitch on your side burns. You grit your teeth to try to stop the pain."
    show Ryan Happy at moveSprite(0.0, 0.5, 0.5)
    "Ryan" "Hey, [pcname]! I wasn't sure if you were gonna make it today. Cutting it a little close, huh?"
    show chelsea embarrassed
    pcname "Ha. Yeah, a little..."
    show Ryan Worry
    "You try to smile up at him but it comes out more like a grimace. Ryan frowns, noticing your strange behavior."
    "Ryan" "You okay? You look like you're in pain."
    show chelsea sad
    pcname "I'm fine-- Ah, fuck."
    "You grab your side, another tight squeeze causing you to wince."
    pcname "I think I messed up a muscle or something. My side feels tight."
    pcname "I should have stretched more. This sucks."
    "Ryan's lips press together in a tight line as he scrutinizes your side. Holding up a finger for you to wait, he starts backing away."
    "Ryan" "Give me a sec, I'll be right back."
    hide Ryan with dissolve
    show chelsea confused
    "Confused, you watch Ryan bound off toward the bleachers. A duffle bag is there, discarded precariously to the side."
    "He opens the bag and digs in, pulling out two objects before zipping it back up."
    show chelsea blank
    show Ryan Worry with dissolve
    "Ryan returns shortly after with a bottle of muscle relaxing cream and some pain medication. He offers them out to you."
    show chelsea embarrassed
    "You give him a grateful smile before downing the pills and applying the cream to your side. Already the stitch feels better."
    pcname "Thanks, Ryan."
    show Ryan Happy
    "Ryan" "Don't mention it. I used to get those all the time, so I just started carrying this stuff on me."
    show chelsea happy
    show Ryan Worry
    "Ryan" "You feeling better?"
    show chelsea laugh
    pcname "Yeah, thanks!"
    show chelsea embarrassed
    show Ryan Happy
    "Ryan" "Good. Don't want you falling over on the track, although it would get you out of my way..."
    show chelsea blank
    hide Ryan with dissolve
    "Ryan winks at you before returning to the bleachers to place his medicine away."
    show Ryan Happy with dissolve
    "When he returns, Ryan falls back onto the turf with a loud thud, spreading his arms in a wide arc behind his head as he relaxes beside you."
    "Ryan" "So? How're you liking track so far? Still like being on the team?"
    menu trackinterest:
        "It's a lot of work." if True:
            show chelsea sad
            "You think back on all of the exercise you've been doing for the past few weeks and your coach's tough training regimen."
            "While they've certainly made you fitter and kept you on a road to a healthier lifestyle, you can't deny the amount of work is simply exhausting."
            show chelsea blank
            show Ryan Worry
            pcname "Yeah, but it's a {i}lot{/i} of work. I wasn't expecting this much exercise, I guess..."
            show chelsea sad
            pcname "Before you laugh, I already know it's silly. Signing up for a track team is basically asking for exercise."
            show Ryan Happy
            "Ryan grins but, to your benefit, doesn't laugh. At least, not with his lips. You can see his eyes are dancing with amusement, ready to tease you at the next chance he gets."
            show chelsea blank
            "Ryan" "Track {i}can{/i} be a lot of work, but it's pretty rewarding, isn't it?"
            show chelsea confused
            "Ryan" "Nothing beats the feeling of accomplishment once you get over that finish line before anyone else can."
            show chelsea embarrassed
            "You wouldn't know {i}that{/i} feeling-- it's not as if you've ever beaten him or August in a race-- but you can relate to the rush of adrenaline that comes when pushing yourself across the field."
            show chelsea laugh
            pcname "Yeah, I guess so."
        "I feel a lot more energized." if True:
            "Stretching your arms out, there's no doubt in your mind that you've gained some muscle and improved your overall health since joining the track team."
            "Even on your most exhaustive mornings, there is still some extra energy there that can only be attributed to your efforts on the track."
            show chelsea laugh
            pcname "Of course. I feel way more energized now than I did when I first joined."
            show chelsea embarrassed
            pcname "It's nice not to feel so tired all of the time."
            "Ryan smiles and nods in approval."
            "Ryan" "Track will do that to you. Sometimes after a race, I feel like I can take on anything."
            show chelsea blank
            "He reaches up toward the sky to shield his eyes, but with his palm upward like that, it looks as if he's ready to grab the sun itself and drag it down to him."
            show chelsea embarrassed
            "As if he has the world in his hands."
        "I should have gone with something else..." if True:
            show chelsea sad
            "As much as you appreciate the muscles and hard work you've put into track, the other clubs are looking really appealing right now."
            "At least, they don't have to run in circles all day."
            show chelsea blank
            show Ryan Worry
            pcname "It's... eh. I have my good days and my bad days."
            show chelsea sad
            pcname "Honestly I think I should have gone with something else. This isn't really what I imagined it would be like."
            "Ryan shrugs."
            show chelsea embarrassed
            show Ryan Happy
            "Ryan" "It's really not for everyone, but I'm glad you've stuck with it this long. Most people quit into their first or second week."
            show chelsea blank
            "You believe it; the team has diminished significantly since your first week, and you have no doubt they latched onto the little remaining spots left in the school's clubs."
            show chelsea embarrassed
            "Ryan" "You should be proud of yourself for staying so long and still keeping up with it."
            "It's not as if you've been given much of a choice, but you smile and nod anyway."
            show chelsea happy
            "At the very least, you feel way fitter now!"
    show chelsea blank
    "You roll onto your stomach and cushion your head with your arms in an attempt to block the sunlight from beaming directly into your eyes."
    show chelsea shocked
    "In your brief moment of silence, you notice Ryan's gaze trailing back to August on the bleachers, reading something on her phone as she performs some leg stretches."
    show chelsea embarrassed
    show Ryan Worry
    pcname "You've been getting along lately."
    "Ryan" "Hm?"
    "Ryan rolls his head to face you, pieces of black turf sticking through his long hair. You reach over to pick one out and fling it back across the field."
    show chelsea blank
    pcname "You and August. I mean, you haven't tried to rip each other's heads off lately, for one thing."
    show chelsea happy
    pcname "You guys have been friendly with each other. It's been nice."
    show chelsea blank
    "Ryan" "Yeah, I guess so."
    "Ryan lays back fully across the ground and gives a big stretch before sighing."
    "Ryan" "We've been talking things over, trying to smooth things out. We decided it's not helpful to anyone on the team if we're fighting all the time."
    show chelsea embarrassed
    pcname "Have you been getting to know her then?"
    show Ryan Laugh
    "Ryan" "Yeah. She's really weird."
    "He says this with a laugh and a smile, shaking his head."
    show chelsea blank
    show Ryan Happy
    "Ryan" "Like, what's up with those contacts? And the dyed hair?"
    "Ryan" "It's like she's trying to look like a cartoon character or something. It's so weird."
    show chelsea embarrassed
    "But the way he says it doesn't indicate that he {i}dis{/i}likes it, you notice. That's a start."
    menu trackaugustlook:
        "I think she looks cool." if True:
            show chelsea happy
            pcname "I don't know. I think she looks kind of cool."
            show chelsea embarrassed
            pcname "I wish people had more confidence to wear what they like, like she does."
            show chelsea blank
            show Ryan Worry
            "Ryan shrugs."
            "Ryan" "Props to her, I guess. Whatever works for her."
            show chelsea embarrassed
        "It is kind of weird." if True:
            show chelsea laugh
            pcname "Yeah... it is kind of weird."
            show chelsea embarrassed
            show Ryan Laugh
            "Ryan" "Right? Man, she's such a weirdo."
    show Ryan Happy
    "When he looks back at her, there's a spark in his eyes, a familiar one you've seen in him a hundred times now."
    show chelsea blank
    show Ryan Angry
    "Ryan" "Just because we're getting along for now doesn't mean I won't beat her at the track meet, though."
    show chelsea confused
    "Ryan" "I've been practicing real hard. It's only a matter of time before she slips up and I take the lead."
    "You feel inclined to point out that he's relying on {i}her{/i} slipping up so he can win, but decide not to. The last thing you want to start is a fight."
    show chelsea blank
    "Ryan" "I'm definitely going to beat her by the track meet. Just wait, [pcname]."
    show chelsea happy
    "The unbridled confidence he shares is enough to make you smile. Even when he constantly loses to August, there's still hope in him."
    show chelsea blank
    show Ryan Worry
    "Ryan glances you over, his gaze snagging on your arms and legs."
    show chelsea embarrassed
    show Ryan Happy
    "Ryan" "That is, if you don't beat her first. You look really toned, [pcname]."
    show Ryan Laugh
    "Ryan" "Before you know it, you'll be catching up to us in no time."
    show chelsea laugh
    show Ryan Happy
    pcname "Careful what you say; I might be outrunning you next."
    show chelsea embarrassed
    show Ryan Laugh
    "Ryan laughs."
    "Ryan" "Go ahead and try."
    show chelsea blank
    show Ryan Worry
    "As your break nears its end, you both end up looking back at August as she lines up early on the track field."
    "Ryan's expression sobers, curiosity taking hold of him as he observes her performing more stretches."
    show chelsea shocked
    "Ryan" "The girl has to have some kind of hobby, right? I mean, outside of track."
    "Ryan" "I feel like all I ever see her do is run around the field. Doesn't she ever take a break?"
    show chelsea confused
    "Now that you think about it, you have no idea what August is like outside of track. She never talks about her hobbies or interests or... anything, really. Just running."
    pause 1.0
    show chelsea sad
    pcname "I... have no idea."
    show Ryan Happy
    pause 1.0
    show Ryan Worry
    show chelsea shocked
    "Ryan opens his mouth to take a guess, but the coach's whistle echoes over the field, calling your break to an abrupt end."
    scene black with fade
    "Ryan offers you a hand and helps you up to your feet before walking back to the track."
    "You intend to ask August about her hobbies and other interests-- even her home life if that's what she wants to talk about-- but by the end of the day, you've forgotten entirely."
    jump events_end_period
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
