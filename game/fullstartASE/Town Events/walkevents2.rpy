label stripclub5:
    scene bg CityN
    pause 0.5
    $ clothes, hair = casualwear
    show chelsea at center, enterScene(1.0, 0.5, 0.7, 0.5)
    "As you make your way downtown, the neon lights of \"CLUB 22\" illuminate the dark city streets in vibrant shades of magenta and purple."
    "Would you like to enter?"
    menu stripclubenter5:
        "Yes." if True:
            scene bg StripclubLobby with fade
            show chelsea at right with dissolve
            "Recalling your last visit, you step into the lobby and hope for the same bouncer as before. You doubt you'll be allowed in if anyone else is in charge for the evening."
            show GHCMan with dissolve
            show chelsea happy
            "You grin as the familiar bouncer eyes you up from beside the heavy velvet rope blockading the entrance."
            "Bouncer" "Back for amateur night, huh?"
            if club == "track":
                show chelsea laugh
                pcname "You know it!"
                show chelsea embarrassed
            elif club == "cheer":
                show chelsea laugh
                pcname "Of course~ I need to practice somewhere, don't I?"
                show chelsea embarrassed
            elif club == "yearbook":
                show chelsea sad
                pcname "Y-Yes..."
            "The bouncer licks his lips, his eyes roving over the familiar curves of your body."
            "Bouncer" "I was wondering if you'd show back up again. You seemed really desperate to get inside last time."
            if club == "track":
                "You raise your chin and grin back confidently, the memory of your successful handjob clear in your mind."
                show chelsea happy at moveSprite(1.0, 0.75, 0.3)
                pcname "I got in, didn't I?"
                show chelsea embarrassed
                "A low laugh rumbles from his chest. You don't miss the way his gaze flits to your palms as if he can will the memory back into existence."
                "Bouncer" "That you did."
            elif club == "cheer":
                "You smirk back at him, recalling the feel of his hefty cock in your hands. When you speak, your words come out in a sultry purr."
                show chelsea happy at moveSprite(1.0, 0.75, 0.3)
                pcname "Or maybe I was desperate for something else."
                show chelsea embarrassed
                "The bouncer shifts, but you can easily see the outline of his arousal through his pants."
                show chelsea confused
                "You wonder for a moment if he's going to make you work your way in again. You're not entirely sure you would mind."
                show chelsea embarrassed
            elif club == "yearbook":
                show chelsea embarrassed
                "You feel your face heat up in a strange mixture of shame and delight as you recall the feel of his cock between your palms."
                pcname "I-I was curious..."
                show chelsea shocked
                "Bouncer" "Yeah. Seems like you were curious about a couple of things."
                show chelsea embarrassed
                "Blood rushes up your neck and to the tips of your ears, your face burning hot as the bouncer chuckles to himself."
            "The bouncer unhooks the velvet rope and steps aside."
            "Bouncer" "Come right in."
            if club == "track" or club == "cheer":
                show chelsea at moveSprite(0.75, 0.0, 1.0)
            elif True:
                show chelsea at moveSprite(1.0, 0.0, 1.2)
            scene bg StripclubLobby with fade
            "The loud music entices you inside and, without another moment's hesitation, you make your way into the strip club."
            show chelsea blank at center, enterScene(1.0, 0.5, 0.7, 0.5)
            "Dancers both professional and amateur are already in varying states of undress across the stage, their breasts and legs on full display as the pole dancers teach the amateurs some new moves."
            show chelsea shocked
            "Many of the men remain seated at their tables or chairs, ogling the variety of dancers with lustful eyes, but a few attempt to dance on stage as well."
            show chelsea laugh
            "Based on their reactions, you suspect a few of them are more eager to be within close proximity to the dancers than actually learn how to dance."
            scene black with fade
            "You make your way to an empty table to enjoy the show."
            show chelsea blank at left with dissolve
            "A familiar stripper steps up to the stage, her long hair as pink as the lingerie barely covering her body."
            show chelsea laugh
            show GStripper with dissolve
            "Cherry Bosom" "Let's give our dancers a round of applause! Be free with your sexy little selves!"
            show chelsea happy
            hide GStripper with dissolve
            "The professionals step back to clap as the amateur dancers make their way off stage. A few of the more confident ones pose or give a little strip tease on their way down, but many smile nervously and rush off stage."
            show chelsea blank
            show GStripper with dissolve
            "Cherry Bosom" "We're going to give these cuties up here a little break before we start our next lesson."
            show chelsea embarrassed
            "Cherry Bosom" "Next up is one badass babe-- you guessed it-- Spike Taylor!"
            show chelsea happy
            hide GStripper with dissolve
            "The crowd goes wild as the lights and music abruptly change, signifying the new performance. A skimpy leather-clad woman struts on stage, a whip in one hand and a baton in the other."
            show chelsea laugh
            "You sit back and watch the performances go by, one colorfully-dressed dancer after another somehow making the act of removing clothes into an art form."
            show chelsea shocked
            "By the third performance, you feel a light tap on your shoulder."
            show GStripper with dissolve
            "Cherry Bosom stands behind you with a warm smile and a clipboard. A few names are scribbled on the sheet."
            show chelsea blank
            if poledancing == True:
                "Cherry Bosom" "Hey, baby! I was hoping you'd come back. You were real fun up on stage."
                "Cherry Bosom" "You interested in joining us for some amateur strip lessons this week?"
            elif True:
                "Cherry Bosom" "Hey, baby. You wanna sign up for the amateur strip lessons?"
                "Cherry Bosom" "You only gotta do what you're comfortable with."
            show chelsea confused
            "You take the clipboard from her hands and read the fine print over. There's no fees and there doesn't seem to be a catch, either."
            show chelsea blank
            "There is a disclaimer to allow the strippers to touch and fondle you, but nothing involving penetration."
            menu stripclubstriptease:
                "Sign me up!" if True:
                    $ corruption +=5
                    if club == "track":
                        show chelsea embarrassed
                        if poledancing == True:
                            "You grin down at the paper, thinking back to when you showed up for pole dancing here before."
                            show chelsea happy
                            "It was such an exhilarating experience; there's no way you could pass this up!"
                        elif True:
                            "You grin down at the paper, remembering with a twinge of regret how you had avoided pole dancing last time."
                            show chelsea happy
                            "Well, now's your chance to shine!"
                        pcname "Definitely! Sign me up!"
                    elif club == "cheer":
                        if poledancing == True:
                            show chelsea embarrassed
                            "Your lips curl into a smirk as you recall the sexual thrill you felt the last time you learned how to pole dance here."
                            "Being up on stage and cheered on by a crowd was a sensation you hadn't felt until then, but now it's like an addiction."
                            show chelsea happy
                            "You have to get up there again!"
                        elif True:
                            show chelsea sad
                            "As you stare at the sheet, you can't help but feel some regret for not pole dancing on your last visit here."
                            show chelsea embarrassed
                            "You don't want to make the same mistake twice."
                            show chelsea happy
                        pcname "I'd love to~!"
                    elif club == "yearbook":
                        if poledancing == True:
                            show chelsea sad
                            "The memory of your pole dancing comes back in a burst of shame. All of those people watching you dance, cheering you on..."
                            show chelsea embarrassed
                            "And yet you had never felt more confident."
                        elif True:
                            show chelsea embarrassed
                            "You had been too timid to attempt pole dancing the last time you were here, but after seeing how much fun everyone was having, you couldn't help feeling left out."
                            show chelsea sad
                            "You never thought you would be the type of girl to try stripping..."
                            show chelsea embarrassed
                            "But then again, you never thought you would be the type of girl to go to a strip club in the first place."
                        pcname "S-Sure... I can try..."
                    show chelsea laugh
                    "You scribble your name down on the clipboard and hand it back to Cherry Bosom."
                    show chelsea embarrassed
                    "Cherry Bosom" "Yasss! It'll be so much fun girl, just you wait!"
                    "Cherry Bosom" "Meet me down by the stage there in five minutes. We'll get you all set up."
                    show chelsea blank
                    hide GStripper with dissolve
                    "Cherry Bosom points to a door leading backstage at the end of the actual stage before wandering off to her next table."
                    scene black with fade
                    "In five minutes, you join the small group that has formed a line at the door."
                    "A security guard and another dancer with vibrant blue hair leads you through the door and backstage to a long rack of costumes and sparkly lingerie."
                    scene black with fade
                    show chelsea shocked with dissolve
                    "You stare at the racks, slack-jawed. You had no idea there were this many types of underwear!"
                    show chelsea blank
                    "The stripper in front of your group rattles off a few of the broader details of the lesson before gesturing toward the costumes."
                    show GStripper at left with dissolve
                    "Stripper" "These are our costumes for guests. Don't worry, everything is thoroughly cleaned before we hand them off to any of our amateurs."
                    "Stripper" "Feel free to look around and pick out something you like! You can get dressed either in here or the restroom over there."
                    "The blue-haired stripper points to a tiny bathroom across the hall."
                    hide GStripper with dissolve
                    "You, along with a gaggle of other girls that signed up to strip, browse the array of sparkly costumes."
                    show chelsea confused
                    "It isn't hard to find something in your size, but some of the options have so many random strings and zippers that you find yourself questioning how you would even put it on in the first place."
                    show chelsea shocked
                    show GStripper at left with dissolve
                    "Stripper" "Five more minutes, ladies!"
                    show chelsea sad
                    hide GStripper with dissolve
                    "Panicked, you grab the first thing you see-- a cobalt blue fishnet bikini-- and quickly get changed."
                    scene black with fade
                    "Once you're all dressed and lined up, you hear Cherry's voice boom over the speakers."
                    "Cherry Bosom" "Let's give it up for our amateur angels who are {i}brave{/i} enough to shake it for you tonight!"
                    scene black with dissolve
                    "The blue-haired stripper ushers your group on, and suddenly you're thrust on stage, blinded and warmed by the stage lights as you follow the other girls across the platform."
                    "Hoots, hollers, and whistles drown out the bass-heavy music as you all take your spots on stage. A few girls alongside you chuckle nervously, almost hiding their bodies, while others pose and strut for the audience."
                    scene black with dissolve
                    "Professional strippers line up behind each of you. You feel Cherry Bosom's long nails caress your skin as she settles her hands on your hips."
                    "Cherry Bosom" "We'll guide you the whole way, ladies. Don't be shy!"
                    "She winks at the audience before she and the rest of the strippers help guide you."
                    scene black with dissolve
                    "Cherry Bosom helps guide you, doing more of the actual stripping on your body while you follow along with her hand's movements."
                    "Cherry whispers in your ear the whole time, making sure that you're okay with each step as she helps you entice the audience."
                    "Her hands run from your inner thighs and up your body, squishing and groping your breasts through the fishnet fabric while you reach back to untie it."
                    scene black with dissolve
                    "The straps fall loose but your breasts are still covered by her hands as she plays it out for the audience."
                    scene black with dissolve
                    "With a flirtatious gasp, she releases your breasts, allowing the weight of them to fall naturally in the open. With a single tug of the string, your bra is gone, fluttering to the ground with the other pile of lingerie on stage."
                    "Your nipples perk in the air, but a new rush of excitement runs through you as the crowd applauds your performance."
                    "Cherry's hands slide down to your waist and you realize she's just as much of the act as you are; the audience loves watching her toy and play with you."
                    scene black with dissolve
                    "She spins you around, groping your ass through the fishnet fabric once before wrapping her finger around the strings at your sides. You give her a subtle nod before she pulls them loose."
                    scene black with dissolve
                    "The panties fall to the ground. A sudden chill wafts between your legs but you don't mind. You allow Cherry to feel you up, for her hands to move over yours and place them in just the right spots to cover your genitalia."
                    "She poses with you a few more times, eliciting the excited catcalls from the crowd."
                    scene black with fade
                    $ clothes = "naked"
                    show chelsea embarrassed with dissolve
                    "By the end of the performance, you realize that a few of the girls had left-- probably too flustered after being fondled on stage-- and you're one of the few posing naked before the captive audience."
                    show GStripper at right with dissolve
                    "Cherry Bosom" "These girls were on {i}fire{/i} tonight, wouldn't you say so?"
                    show chelsea happy
                    "Several yells of agreement pierce the air. You can't help but feel a sense of pride for having participated in it."
                    show chelsea embarrassed
                    "Cherry Bosom" "Give it up for our amateur angels!"
                    scene black with fade
                    "There is more clapping and yelling as you're ushered backstage to change back into your clothes. A few of the strippers compliment you on your performance."
                    show GStripper with dissolve
                    "Cherry Bosom" "That's all we have for amateur night. We hope to see you again next week!"
                    scene bg StripclubLobby with fade
                    $ clothes, hair = casualwear
                    show chelsea blank with dissolve
                    "You head back into the show room and try to process what just happened on stage."
                    show chelsea embarrassed
                    "The phantom touch of Cherry's hands feeling you up are still on you, and fuck, you want more."
                    "You gather your things and return home as quickly as possible."
                    $ stripdance=True
                    jump events_end_period
                "This isn't really my thing..." if True:
                    if club == "track":
                        show chelsea sad
                        if poledancing == True:
                            "While pole dancing was fun, you aren't sure you're ready to strip in front of a bunch of strangers."
                        elif True:
                            "You weren't even willing to pole dance the last time you were here."
                            "While you're sure you'd look great stripping on stage, it's not exactly something you want to mark off your bucket list."
                        show chelsea blank
                        pcname "I'll pass, thanks."
                    elif club == "cheer":
                        show chelsea sad
                        if poledancing == True:
                            "As sexy as you felt pole dancing, stripping in front of a crowd is really taking that to a whole new level."
                            "If you're going to give the audience a show like that, you at least expect to be paid for it."
                        elif True:
                            "As tempting as the idea of showing off your body to an adoring crowd is, you know there's no way you could compare to the actual professionals."
                            "And you'd definitely rather leave that to the professionals."
                        show chelsea blank
                        pcname "Sounds fun, but I'm good for now. Thanks."
                    elif club == "yearbook":
                        if poledancing == True:
                            show chelsea embarrassed
                            "Your face heats up as you recall your last time performing here on amateur night."
                            show chelsea sad
                            "You feel as though your time pole dancing here was a fluke, a minor lapse of confidence that you aren't sure you'll ever see again."
                            "Dancing was already embarrassing enough, but you can't imagine how it would feel to strip in front of other people."
                        elif True:
                            show chelsea sad
                            "You hadn't even been able to work up the courage to try out pole dancing the last time you were here. What makes her think you're capable of stripping?"
                        pcname "N-No thank you..."
                    "You pass the clipboard back to her."
                    show chelsea embarrassed
                    "Cherry Bosom" "No problem, baby! Our next session starts after this act, so be sure to stick around and watch it!"
                    hide GStripper with dissolve
                    "Cherry Bosom takes her clipboard and walks away to the next table."
                    show chelsea happy
                    "You sit back and enjoy the rest of the performances before heading home for the night."
                    jump events_end_period
        "No." if True:
            show chelsea sad
            "The strip club didn't really impress you last time. You would rather find something else to do."
            "You continue down the street."
            show chelsea at exitScene(0.5, 0.0, 0.7, 0.5)
            pause 1.4
            jump events_end_period

label stripclub6:
    scene bg CityN
    pause 0.5
    $ clothes, hair = casualwear
    show chelsea happy at center, enterScene(1.0, 0.5, 0.7, 0.75)
    "The city is filled with life tonight. As you make your way downtown, you remember that it's amateur night at \"CLUB 22\"."
    "Would you like to go?"
    menu stripclub6enter6:
        "Yes." if True:
            scene black with fade
            "Without hesitation, you turn down the street and follow the signs to the familiar strip club."
            scene bg StripclubLobby with fade
            show chelsea blank with dissolve
            "As you enter, the usual bouncer smirks at you, his eyes locked on your tits."
            show GHCMan at left with dissolve
            if stripdance == True:
                "Bouncer" "You did a good job last week. It was nice to get a full view of what's under those clothes."
                if club == "track":
                    show chelsea shocked
                    "You struggle to contain your surprise. You didn't realize the bouncer would have any ability to see you up on stage from here."
                    show chelsea confused
                    pcname "I didn't think you would be watching."
                    "Bouncer" "You didn't want me to?"
                    show chelsea blank
                    "Bouncer" "I guess it doesn't matter, haha. I get breaks sometimes, so I like to check in and see what's going on."
                    "Bouncer" "Guess I got lucky last week."
                elif club == "cheer":
                    show chelsea embarrassed
                    "You aren't sure whether to feel disgusted or secretly pleased by the fact he was watching you strip down for the whole club last week."
                    show chelsea happy
                    "That handjob must have left a better impression on him than you thought."
                    show chelsea embarrassed
                    pcname "I'm glad you enjoyed it. I tried to put on quite a show."
                    show chelsea laugh
                    "Bouncer" "You nailed it."
                    show chelsea embarrassed
                elif club == "yearbook":
                    show chelsea embarrassed
                    "A sudden heat rises to your cheeks. You didn't think about {i}who{/i} would see that performance, only what it felt like to be up on that stage..."
                    pcname "Y-You saw?"
                    "Bouncer" "Hell yeah. Gotta take a break from work sometimes."
                    show chelsea happy
                    "Bouncer" "Too bad I'm on the clock tonight. I'd love to see you shake those tits some more."
                    show chelsea embarrassed
            elif True:
                "Bouncer" "I was hoping you'd be up on stage with the others last week. I was disappointed when I went on my break and you weren't up there."
                if club == "track":
                    show chelsea confused
                    pcname "Shouldn't you be doing your job instead of watching the girls strip?"
                    "Bouncer" "Hey, man's gotta take a break sometimes."
                    show chelsea blank
                elif club == "cheer":
                    pcname "Sorry to disappoint, but it wasn't really my style."
                    show chelsea shocked
                    "Bouncer" "Ha. But giving out hand jobs to strangers {i}is{/i} your style, I guess."
                    show chelsea embarrassed
                elif club == "yearbook":
                    show chelsea sad
                    pcname "Y-You shouldn't be watching that..."
                    "Bouncer" "Haha! Why not? I work at a strip club. We get breaks too, you know."
                    show chelsea shocked
                    "Bouncer" "Besides, I'm used to all the girls working out there. It's the new ones that get me excited."
                    show chelsea embarrassed
                    "You feel a flush of shame heat up your cheeks as his eyes rove over you."
            "The bouncer steps to the side and unhooks the red velvet rope."
            "Bouncer" "Have fun tonight, [pcname]. Don't be afraid to try things out in there."
            hide GHCMan with dissolve
            show chelsea at moveSprite(0.5, -0.5, 1.2)
            scene black with fade
            "He winks at you before you pass through the doorway's threshold. You can feel his eyes still watching you from behind as you make your way into the strip club."
            scene bg StripclubLobby with fade
            show chelsea happy with dissolve
            "As soon as you enter, you see a large poster hanging up beside the bar: '{i}AMATEUR NIGHT! LEARN TO LAP DANCE!{/i}'"
            show chelsea embarrassed
            "Sure enough, you can already see the professionals mixed in with the amateurs as they grind against each other on stage, each taking turns and demonstrating the movements."
            show chelsea confused
            show GWaiter at left with dissolve
            "The bartender looks you over as you walk in, his eyebrow raised."
            show chelsea sad
            "Anxiety wrenches in your gut as you wonder if he's aware you're too young to be in here, but a look of recognition crosses his face and he leans over the bar so you can hear him."
            show chelsea shocked
            "Bartender" "Hey! You were up stripping last week, weren't you?"
            if club == "track":
                show chelsea confused
                pcname "Yeah. What's up?"
            elif club == "cheer":
                show chelsea confused
                pcname "I was... Why?"
            elif club == "yearbook":
                show chelsea sad
                pcname "Y-Yes... I-I mean... Well..."
                "You feel embarrassed to even admit it aloud."
            show chelsea blank
            "The bartender glances around the room before muttering a curse under his breath."
            show chelsea confused
            "Bartender" "She's always running off..."
            show chelsea shocked
            "Bartender" "Anyway, Cherry told all of us to grab her if we saw you."
            show chelsea confused
            pcname "Really? Why?"
            "The bartender shrugs, clearly just as lost as you are."
            show chelsea blank
            "Bartender" "Beats me, but just wait here a second. I'll go find her."
            hide GWaiter with dissolve
            "Bartender" "Hey, Cami!"
            "The bartender steps out from behind the counter, switching out with another female bartender while he searches around the room."
            show GWaiter at right with dissolve
            show GStripper at midright with dissolve
            "After a few minutes, he returns with the pink-haired stripper in tow. Her face lights up as she approaches and takes you in."
            show chelsea shocked
            "Cherry Bosom" "You came back! Baby, I was hoping to see you again."
            show chelsea sad
            hide GWaiter with dissolve
            pcname "Is everything okay? I'm not in trouble, am I?"
            show chelsea blank
            "Cherry tosses her hair back with a dramatic laugh, shaking her head. Her locks are so luxurious, you start to wonder if it's her real hair or a wig."
            show chelsea shocked
            "Cherry Bosom" "Of course not, baby! The opposite, in fact!"
            if stripdance == True:
                "Cherry Bosom" "You did such a great job with me last week, I wanted to know if you would sign up to learn some of the lap dances tonight."
                "Cherry Bosom" "I'd love to put on another little show with you!"
                show chelsea embarrassed
                "She winks at you, suddenly reminding you of the feel of her hands groping along your body last week."
            elif poledancing == True:
                "Cherry Bosom" "You did such a great job with the pole dancing, I wanted to know if you would sign up to learn some of the lap dances tonight."
                "Cherry Bosom" "I'd love to put on another little show with you!"
                show chelsea embarrassed
                "She winks at you, and there's no containing the slight blush that rises to your cheeks."
            elif True:
                "Cherry Bosom" "I'm really in need of some more girls to sign up for the lesson today, and I see you come by every week."
                "Cherry Bosom" "I know lap dancing can be intimidating, but I'll do it with you and help you every step of the way! I promise it'll be fun."
                "You stare back at her, shocked. You hadn't realized you were that memorable. You were just another face in the crowd..."
                show chelsea embarrassed
                "But clearly something you did left an impression with this woman."
            "Cherry Bosom" "What do you say?"
            menu stripclublapdance:
                "I'll sign up." if True:
                    show chelsea blank
                    "You're still surprised that she sought you out for this, but you can't help feeling flattered at the same time."
                    show chelsea embarrassed
                    "How can you turn her down when she went out of her way to ask you?"
                    if club == "track":
                        show chelsea happy
                        pcname "Yeah, I'll sign up. That sounds great."
                    elif club == "cheer":
                        show chelsea happy
                        pcname "Ooh, this sounds fun! You can count on me, Miss Bosom~"
                    elif club == "yearbook":
                        pcname "I-I... Um... S-sure, that sounds fun..."
                    show chelsea shocked
                    "Cherry suddenly clasps your hands in hers, and you're more than impressed when she jumps up and down in excitement-- especially in those nine-inch heels."
                    show chelsea embarrassed
                    "Cherry Bosom" "Great, darling! Oh, this will be so much fun."
                    show chelsea blank
                    "She releases you and takes a step back, giving you room to breathe, but all you can smell is the sweet scent of her cherry blossom perfume."
                    show chelsea confused
                    "It's like the woman's life goal is to exist as a singular color."
                    show chelsea embarrassed
                    "Cherry Bosom" "We'll be getting ready for the next group in about ten minutes, so you arrived at the perfect time."
                    "Cherry Bosom" "Just head to the backstage door there when you're ready."
                    "Cherry points to the door by the stage where a bodyguard stands watch."
                    show chelsea happy
                    "Cherry Bosom" "I'll see you on stage!"
                    show chelsea blank
                    hide GStripper with dissolve
                    "And with a slight wave of her hand, Cherry Bosom disappears into the crowd."
                    scene black with fade
                    "You spend the next few minutes sipping at a bottle of water provided by the bartender and watching the other girls grind on customers before making your way backstage."
                    if stripdance == True:
                        "The blue-haired stripper is back again, and she leads you and a few other excited amateurs down the familiar corridor to the rack of sparkling lingerie from before."
                        scene black with fade
                        show chelsea embarrassed with dissolve
                        "After the success of the blue fishnet lingerie last week, you almost feel a connection to it now."
                        show chelsea laugh
                        "You pluck the lingerie from the rack and change."
                    elif True:
                        "A blue-haired stripper greets you all and welcomes you backstage, her cheery voice rattling off random dos and don'ts for the stage. A few girls chuckle nervously and glance amongst each other."
                        scene black with fade
                        "The stripper stops near the end of the hall to a large alcove just before the dressing rooms. There are some benches and a rack of sparkly lingerie in all sorts of cuts and lengths sits front and center."
                        show chelsea shocked with dissolve
                        "You had no idea so many varieties of underwear even existed!"
                        show chelsea blank
                        show GStripper at left with dissolve
                        "Stripper" "These are our costumes for guests. Don't worry, everything is thoroughly cleaned before we hand them off to any of our amateurs."
                        "Stripper" "Feel free to look around and pick out something you like! You can get dressed either in here or the restroom over there."
                        "The blue-haired stripper points to a tiny bathroom across the hall."
                        show chelsea confused
                        "It isn't hard to find something in your size, but some of the options have so many random strings and zippers that you find yourself questioning how you would even put it on in the first place."
                        show chelsea shocked
                        "Stripper" "Five more minutes, ladies!"
                        hide chelsea with dissolve
                        "Panicked, you grab the first thing you see-- a cobalt blue fishnet bikini-- and quickly get changed."
                    scene black with fade
                    "Once you're all dressed, the stripper leads you to the backstage curtain and signals for you to wait while Cherry Bosom makes her announcement."
                    show GStripper with dissolve
                    "Cherry Bosom" "Have you had enough of our amateur angels tonight, babes?"
                    "Cherry Bosom" "No? Good! Cause we have some very special, very brave young ladies here to pleasure you tonight!"
                    "Cherry Bosom" "Fly in, my little angels!"
                    scene black with dissolve
                    "On her cue, the blue-haired stripper signals for you all to move. You hurry across the stage after the other amateurs, careful not to trip over yourself as you all sit down in one of the metal chairs provided."
                    scene black with dissolve
                    "A professional moves in front of each girl, and with the start of the music, the show begins."
                    scene black with dissolve
                    "You were briefed on this inside, but it's still strange to hear Cherry Bosom instructing you on how to provide a lap dance while she bumps and grinds against you on the chair."
                    "Her perfume makes your head feel dizzy, and you almost want to reach out and take one of her large tits into your mouth."
                    "You squirm on your seat and force yourself to resist the urge."
                    "It appears you aren't alone, though. You notice how dazed the other amateurs are, their addled brains struggling to keep up with their stripper's instructions."
                    "Cherry Bosom" "Now, let's have our angels try it out!"
                    show black with dissolve
                    "You and Cherry swap places, and suddenly the pressure is on as you struggle to remember everything she told you."
                    "Thankfully, Cherry must be used to enchanting young amateurs, because she continues to give you lots of praise and applause as she reminds you where to place your hands and hips."
                    scene black with dissolve
                    "You find yourself straddling the stripper, grinding hard on her lap as the music blares over the speakers."
                    "Cherry Bosom" "Mmmm, yes honey. Now bend back-- Just like that~!"
                    scene black with dissolve
                    "Cherry helps you bend backwards, her hands on your ass to keep you steady while the audience gets a clear view of your covered breasts."
                    "Several men-- and some women, too--call out in approval. You toss your hair a few times, mimicking the way you'd seen Cherry do it."
                    "Cherry Bosom" "Look at this angel! Isn't she a natural?"
                    "The audience seems to agree. You climb off of Cherry's lap only to spread her legs and come up through them again, your breasts hovering just above her face."
                    scene black with dissolve
                    "Cherry catches your chin between her long nails. You look down, surprised to find a mischievous glint in her eye."
                    scene black with dissolve
                    "Slowly, Cherry pulls your face down until your lips are touching. The audience cries out in anticipation, but you can barely hear them; your focus is entirely on Cherry."
                    scene black with dissolve
                    "Cherry Bosom" "You've got such a cute little face."
                    scene black with dissolve
                    "Her sultry voice sends a thrill through your body. She presses her lips harder against yours, using her tongue to poke and prod your mouth."
                    "You let out an involuntary moan that excites the crowd even more. You're suddenly aware of Cherry's hands roaming across your body, pulling you in as she kisses you slowly, tenderly, in the kind of open-mouthed pleasure you've only seen in porn films."
                    "The woman is an expert."
                    scene black with dissolve
                    "Cherry pulls away slightly, tongue still out as if she'll suck you right back in. You almost want her to."
                    "Your heart thunders in your chest and the moisture between your legs begs for more."
                    "But Cherry turns her head to the audience and addresses them in her usual sexy tone."
                    "Cherry Bosom" "And that's our angels tonight, babes! Give it up for our girls!"
                    scene black with fade
                    "The crowd cheers and you slip off of Cherry's lap, following the rest of the girls backstage."
                    scene black with fade
                    show chelsea blank with dissolve
                    show GStripper at right with dissolve
                    "You've barely begun to change when Cherry slips back behind the curtain, a broad smile on her face."
                    show chelsea shocked
                    "Cherry Bosom" "What's your name, baby?"
                    show chelsea blank
                    pcname "[pcname]."
                    show chelsea confused
                    "Cherry Bosom" "Ooh~ [pcname]! I love it. Come with me for a sec?"
                    "You glance back at the other girls, confused, but obediently follow Cherry into her dressing room."
                    scene black with fade
                    show chelsea embarrassed at midright with dissolve
                    show GStripper with dissolve
                    "Cherry Bosom" "You see that, baby girl? They loved you!"
                    "Cherry pulls on a pretty silk pink robe from one of the vanity chairs and wraps it around her slender figure."
                    show chelsea laugh
                    "Cherry Bosom" "How about you come by next week, too?"
                    show chelsea happy
                    pcname "What are you teaching then?"
                    show chelsea confused
                    "Cherry shakes her head, pink waves bouncing."
                    "Cherry Bosom" "Oh honey no, I don't want to teach you nothing."
                    show chelsea shocked
                    "Cherry Bosom" "There's actually some very important clients coming in next week. They booked out a special room, but one of them saw you perform and requested you be there, too."
                    show chelsea blank
                    "Cherry Bosom" "I'd pay you, of course! This wouldn't be a freebie."
                    "Cherry Bosom" "What do you say? Want to put on a little show with me?"
                    menu stripclubclient:
                        "I'll do it." if True:
                            show chelsea embarrassed
                            "The last thing you expected was an offer to come strip with Club 22's headliner, but after hearing the audience's reaction over just a kiss tonight, you're not sure how you could turn it down."
                            show chelsea laugh
                            "Besides, you could always use the extra money."
                            show chelsea happy
                            "And if you're actually as good as she says you are, this should be a piece of cake."
                            if club == "track":
                                pcname "For sure. I can do that."
                            elif club == "cheer":
                                pcname "Oh, absolutely~ As long as I get to work with you again, I'm all on board."
                            elif club == "yearbook":
                                show chelsea embarrassed
                                pcname "D-Depending on um, what we do, I... I think I can do that..."
                            show chelsea embarrassed
                            "Cherry beams, a childlike excitement gleaming in her eyes."
                            "Cherry Bosom" "Perfect! Meet me here at 7:00pm then; come through the side door. I'll have Viktor show you the way."
                            "Cherry Bosom" "You can call me if there are any problems."
                            scene black with fade
                            "After a quick exchange of phone numbers, you finish getting changed and head home for the night."
                            $ privateclient=True
                            jump events_end_period
                        "No thanks." if True:
                            show chelsea sad
                            "Something weighs down in your gut like a stone. Something about this doesn't feel right; in fact, it feels very, very wrong."
                            "Everything up to this point has been public amateur lessons, but stripping for a private event when you don't even work for the company... It feels shady."
                            show chelsea at moveSprite(0.75, 0.9, 0.5)
                            "You take a cautious step back toward the door and shake your head."
                            show chelsea embarrassed
                            if club == "track":
                                pcname "Sorry, I have shit to do that night. Maybe some other time..."
                            elif club == "cheer":
                                pcname "Sorry, no can do. I have other plans."
                            elif club == "yearbook":
                                pcname "I-I'm not interested. Um, thank you, but no..."
                            "Cherry's face falls. She takes a moment to collect herself, but the disappointment is evident in her slumped shoulders and dejected attitude."
                            "Cherry Bosom" "Oh. I see."
                            "Cherry Bosom" "Alright then, honey. I'll see you around."
                            hide GStripper with dissolve
                            "She dismisses you with a wave of her hand, already turning back to the mirror to fix her makeup."
                            show chelsea sad
                            pause 0.5
                            show chelsea at exitScene(0.9, 1.5, 0.9, 0.3)
                            "You leave, a heavy, uncomfortable cloud hanging over your back as you hurry to get changed and head home."
                            scene black with fade
                            "You're not sure you'll be back."
                            jump events_end_period
                "I prefer watching." if True:
                    show chelsea sad
                    if poledancing == True:
                        "As much fun as you had pole dancing, a lap dance feels way more involved. You're not sure it's something you want to go through with in public."
                    elif stripdance == True:
                        "As much fun as you had stripping on stage last week, you can't bring yourself to push your luck any further."
                    elif True:
                        "You couldn't bring yourself to participate in any of the other lessons, and you certainly can't face the shame and embarrassment of trying-- and likely failing-- at a lapdance in front of a crowd of people."
                    if club == "track":
                        pcname "Uh, thanks but no thanks. I'm just here to watch."
                    elif club == "cheer":
                        pcname "Sorry, but I'm more interested in watching tonight."
                    elif club == "yearbook":
                        pcname "N-no thank you... I would rather... rather watch..."
                    "Cherry's face falls but she nods, clearly disappointed."
                    show chelsea embarrassed
                    "Cherry Bosom" "I see. Well, thank you anyway!"
                    "Cherry Bosom" "Have fun with our show tonight!"
                    show chelsea blank
                    hide GStripper with dissolve
                    "Without another glance in your direction, Cherry disappears into the crowd."
                    scene black with dissolve
                    "You take up a seat at the bar and watch the next couple of performances go by before calling it a night."
                    jump events_end_period
        "No." if True:
            show chelsea blank
            "Despite the fun you had before, you're not really interested in seeing the strip club today."
            show chelsea at exitScene(0.5, 0.0, 0.7, 0.75)
            "You continue down the street in search of something else to do."
            jump events_end_period

label stripclub7:
    scene bg CityN
    "You make your way downtown and follow the familiar signs to \"CLUB 22\"."
    $ clothes, hair = casualwear
    show chelsea blank at center, enterScene(1.0, 0.5, 0.65, 0.5)
    "Cherry had texted you all of the instructions for how to get to the backdoor, but as you approach the building, there is some uncertainty settling in your stomach."
    "Are you sure you want to go through with this?"
    menu stripclubprivateevent:
        "Yes!" if True:
            $ corruption += 5
            show chelsea sad
            "As you stare up at the tinted windows and neon lights, you chalk up the uneasy turns of your stomach to stagefright and look for the side entrance."
            scene black with fade
            "Sure enough, a tall bodyguard-- Viktor, you guess-- stands in the back. Once you show him your text from Cherry and fake ID, he lets you inside."
            "The back of the building is a whirlwind of costumes and relaxed strippers."
            scene black with fade
            "They cross between the break room and the dressing room in a flurry of colors, some rushing to get on stage while others leisurely ate take-out food and scrolled through their phones."
            show chelsea with dissolve
            "You feel a little overwhelmed as you search through the dressing room for Cherry."
            show chelsea embarrassed
            show GStripper at left with dissolve
            "As you're making your way around, the blue-haired stripper from last time approaches you, a curious look on her face."
            "Stripper" "You lost, honey?"
            show chelsea sad
            pcname "A little bit. I'm trying to find Cherry...?"
            "She scrutinizes you for a moment before recognition crosses her face."
            "Stripper" "Oh! You're here to help her tonight, right?"
            "Stripper" "She's getting ready now. Right this way, hon."
            scene black with fade
            "You follow the blue-haired woman through the dressing room to what is no doubt Cherry's vanity; it's covered in anything and everything conceivably pink. Perfumes, scarves, boas, makeup, jewelry, trinkets-- all pink."
            show chelsea blank with dissolve
            "Cherry sits at the stylist chair in front of her mirror, busy applying her makeup while another woman helps curl her hair from behind."
            "She catches a glimpse of you in the reflection."
            show GStripper at midright with dissolve
            "Stripper" "Found your lost kitty, Cher~!"
            show chelsea embarrassed
            show GStripper as GStripper2 at left with dissolve
            "Cherry Bosom" "There you are, baby! I was starting to worry you wouldn't make it."
            "Cherry Bosom" "Steel, you mind helping her get ready? We need to be on in thirty minutes."
            "Stripper" "Sure."
            scene black with fade
            "The blue-haired woman-- Steel, apparently-- ushers you to a rack of costumes and helps you get changed."
            "After twenty minutes, they've dressed you up, styled your hair, and covered your face in more makeup than you've used in your life."
            scene black with dissolve
            "Cherry stands up from her chair and struts over to you. You realize that your costumes are perfect compliments of each other, but while hers is pink, yours is entirely blue."
            "Cherry Bosom" "Ready to put on a show, baby?"
            "She leans forward to shake her barely-contained tits. They look ready to pop out of her tiny pink bra."
            "Your own breasts are in a similar state, the blue bra only covering half of the soft skin. Even your thong is tighter than you imagined, your ass and pussy almost out in full display."
            if club == "track":
                scene black with dissolve
                "The lingerie they picked is uncomfortable at best and painful at worst. You constantly have to tug the string of your thong out from your crotch lest it get stuck up there."
                "How do these ladies wear this kind of stuff every day? You can't imagine putting yourself through that."
                "Still, there's no denying you look great, and you're sure whatever client sees you is going to think the same thing."
                pcname "Sure, why not."
            elif club == "cheer":
                scene black with dissolve
                "Glancing at yourself in the reflection, you can't help but check yourself out. The lingerie fits you perfectly, practically molding against the curves of your body."
                "You've never felt so sexy in your life. Whatever client Cherry has, there's no way they're going to be able to take their eyes off of you."
                pcname "Absolutely~!"
            elif club == "yearbook":
                scene black with dissolve
                "You feel heat rush from your neck to the tips of your ears, the embarrassment of your situation coming to the forefront of your mind. You've never been so exposed to an audience before..."
                "But it is a private event, so it should be fine, right?"
                pcname "Y-Yes, I guess so..."
            "Cherry Bosom" "Great! Come on baby, it's show time!"
            scene black with fade
            "Cherry hooks arms with you and parades you through the main strip club to a hallway of private side rooms rented out by clients."
            "You can't help but notice the way men's heads turn when you strut by, their gazes locked hungrily on your exposed ass and supported breasts."
            "Cherry notices as well, blowing a kiss to a few of them before guiding you into one of the private rooms."
            "The room is smaller than you imagined, with a short platform, a single pole, and an array of plush couches against the wall."
            "Two gentlemen in suits sit on the couch, their hair slicked to the side and briefcases discarded under the small coffee table in front of them. It looks like they just got off of work."
            "Cherry Bosom" "Welcome, boys~ Are you ready to have a little fun?"
            "You can already see the outline of their erections through their tight slacks, but the men nod eagerly, focusing between the two of you."
            "Once the door is closed, the music starts, and Cherry takes the stage."
            scene black with dissolve
            "She's in complete control, moving you around and feeling you up to the pleasure of her guests. You feel your body tense in anticipation as she slinks up behind you and squeezes your breasts."
            "The men lean forward, wringing their hands together in excitement."
            scene black with dissolve
            "Cherry grinds and rubs against you, one hand moving down to stroke you through your thin thong while the other releases one of your breasts. She pinches and pulls at your taught nipple before leaning down to take it in her mouth."
            "You gasp, the warmth of her mouth sending a thrill through your body. You can feel her tongue flick your nipple, her teeth grazing against the skin. She stares up at you through her long lashes, lips pulled into a sultry smirk."
            "You had no idea this is what you were signing up for, but as you feel a familiar heat run through your lower abdomen, you can't be upset."
            "Cherry pops your other tit from your bra and fondles it. She takes turns between sucking and biting each breast, making sure to keep the actions long and playful for her clients' enjoyment."
            "Then you hear the unzipping of pants."
            scene black with dissolve
            "You glance over, surprised to find the men's cocks out, their hands moving slowly up and down their shafts as they watch Cherry suck on your breasts."
            scene black with dissolve
            "You open your mouth to object-- this isn't supposed to happen, right?-- but Cherry catches the gesture and immediately plants her mouth in yours."
            scene black with dissolve
            "You melt in her arms, the feel of her hand slipping under your thong and touching you intimately sending a tremor through your body."
            "Her fingers slip inside of you, her thumb rubbing against your clit as she fingers your dripping hole. You gasp, your body involuntarily jerking against her in response."
            "Blonde Client" "Fuck yeah... Touch her just like that..."
            "With a glance toward the men, you can see they've begun to masturbate with more fervor. They can't be older than their early 30s. Yet heavy desire clouds their eyes, and you can see just how eager they want to participate by the stiffness of their cocks."
            scene black with dissolve
            "Cherry guides your hand to her own pussy, and you're surprised to find she's just as wet and excited as you are as you slip your fingers into her."
            "You remain like this for some time, fingering and grinding against each other while Cherry's tongue invades your mouth. You can barely catch your breath with her so intent on stealing it away."
            "Blonde Client" "Come here, Cherry."
            "His voice is husky and strained. He can't simply watch anymore."
            "Your pink-haired companion slowly pulls away, nodding for you to follow her lead as she struts over to the blonde man."
            scene black with dissolve
            "He doesn't waste any time as he grabs her hips and slams her down on his waiting cock. Cherry throws her head back in a loud moan, her fingers digging against the man's scalp."
            "You can't help but watch as he bounces her up and down, shoving her bra down to get a better look at her bouncing tits."
            "This is {i}definitely{/i} not what you thought you were coming here for."
            "And yet..."
            "You feel your inner thighs grow wet as your own excitement drips from your cunt."
            if club == "track":
                "Adrenaline kicks through you as you realize you want this as much as they do."
            elif club == "cheer":
                "Desire coils in your belly as you realize you want this just as much as they do."
            elif club == "yearbook":
                "With some shame, you want this just as much as they do."
            "The businessman's friend, a brunette with sharp blue eyes, stares at you with a wolfish grin."
            "Brunette Client" "Well? Are you gonna keep me waiting?"
            "Slowly, you take Cherry's lead."
            scene black with dissolve
            "You straddle the brunette, your fingers still wet with Cherry's fluids. The man takes your fingers in his mouth, licking them clean before shoving you down on his cock."
            "You cry out, surprised by the sudden pain that jolts through your body, but the brunette only grins wider."
            "His fingers dig into your hips as he bounces you up and down on his cock, his mouth and tongue leaving excited bites and licks across your exposed breasts."
            "You can barely breathe-- barely even think-- as yours and Cherry's moans fill the room. The pain ebbs away into a delightful pressure between your legs, each thrust fuelling your own needs further."
            scene black with dissolve
            "The men seem to both share the same idea at once and they readjust on the couch to face each other, one laying you down on your back while the other pushes Cherry onto all fours."
            scene black with dissolve
            "Cherry seems to already understand their need, dipping her head low to press her tongue against your cunt."
            pcname "A-Ah, mmmph...!"
            "You squirm, your hips jerking in her direction as Cherry eats you out. You feel her tongue rub against you, inside of you, while her thumb strokes your clit."
            show black with dissolve
            "The brunette settles behind her, quick to shove his dick in her pussy while the blonde man's cock brushes your teeth."
            "Blonde Client" "Don't keep me waiting, sweetheart."
            scene black with dissolve
            "He doesn't give you a moment to catch your breath. As soon as your lips part his cock is inside of your mouth, his large hand grabbing the back of your head for leverage."
            "The client doesn't leave you much room to disagree, shoving your face down against his cock, but you find yourself wanting to take in as much as possible as Cherry continues pleasuring you from down below."
            "Blonde Client" "Mmm... Fuck. Yeah, take it all in."
            scene black with dissolve
            "His cock slips further into your mouth and smacks against the back of your throat. You reach up to stroke his balls while he fucks your face, your other hand clutched in Cherry's hair to hold her down against your pussy."
            "Blonde Client" "Fuck. Fuck, yeah, take it all you little whore. You like that? Huh?"
            "The client's words come out grunted and breathy, and his fingers tighten in your hair as he reaches his climax. You swallow his load with ease."
            "Pleasure rocks through your own body. Cherry doesn't hesitate to continue lapping at your cunt as you cum, even moaning in delight as your body trembles beneath her."
            "You feel Cherry's body move against you a little more as her other client finishes inside of her, the wet {i}slap{/i} of his cock pounding into her cunt mixed with your pants as you come down from your own orgasm."
            scene black with fade
            "Once finished, you all take a moment to catch your breath. The men collapse back against the couch, their hands idly roaming and groping at your breasts and ass."
            "You almost wonder if they're going to ask you for a second round when Cherry helps you stand up and adjust your clothes."
            "You expect to leave then, but Cherry wipes a piece of stray cum from your breast with her finger. She sucks it off sensually, eyeing up her clients from the side."
            "Cherry Bosom" "I'll see you boys next week."
            "With a wink, Cherry escorts you from the room."
            "The loud chaos of the regular strip club feels like a hazy dream as Cherry pulls you through it and leads you back to the dressing room."
            scene black with fade
            "Several pairs of eyes snag on the two of you, and you can't help but wonder how many other men in here Cherry has let fuck her."
            "Silence builds between you and Cherry as the both of you get dressed, the events of the night passing through your mind in a daze. It almost doesn't feel like it actually happened."
            show chelsea sad with dissolve
            if mattsubmissive == True:
                "Fresh anxiety coils in your belly as you think of what Matt might say to all of this. Would he be angry that you've just fucked two men and a stripper?"
                "Knowing Matt, his reaction could be unpredictable. He would either delight in your whoreish activities or demean you even more for them."
            elif damienrelate=='dating':
                "You feel sick with guilt as you think of poor Damien and how he might react if he found out."
                "You have no doubt he would be heartbroken if you even suggested the idea of fucking two other men and a stripper."
                "He's so sweet... He doesn't deserve this. And yet you can't stop yourself from doing it."
            elif violetrelate=='Sub':
                "Guilty thoughts nag at you from the back of your head as you think of Violet and what she might have to say about all of this."
                "Should you tell her? Does she need to know?"
                "You shake your head, pushing the thoughts aside."
                show chelsea angry
                "You {i}are{/i} in charge here, so it's not like she has any say in what you do inside or out of your relationship."
                show chelsea blank
                "Violet will just have to deal with it; she doesn't have a choice."
            elif violetrelate=='Dom':
                "Guilty thoughts nag at you from the back of your head as you think of Violet and what she might have to say about all of this."
                "Should you tell her? Does she need to know?"
                "Knowing Violet, she would insist on you telling her. She is in charge, after all. Keeping it to yourself, disobeying her..."
                "It almost feels worse than an actual punishment. But if you did tell her, would she actually punish you, or would she dump you entirely?"
                show chelsea blank
                "You take a deep, staggered breath. You'll keep this to yourself, even if it means upsetting her later."
            elif katerelate=='girlfriend':
                "Kate pops up in the back of your mind and you stop cold. Kate: poor, innocent Kate..."
                "How can you lie to her about something like this? You're clearly left with no other choice, but you hate the idea of deceiving her."
                "She trusts you so wholeheartedly... You feel your own guilt consume you. Maybe this was a mistake."
            elif True:
                "You vaguely think of your classmates and coworkers. What would they say to you doing something like this?"
                show chelsea shocked
                "You hadn't considered it before, but almost any adult can get into a strip club."
                show chelsea sad
                "What if one of your teachers is here tonight? What about your classmates' parents, or your coworkers? Your boss?"
                show chelsea blank
                "You glance back at the hall leading to the show room, but you can't bring yourself to check. Hopefully no one you know is here."
                show chelsea sad
                "And if they are, you pray that they won't say anything."
            show chelsea shocked
            show GStripper at left with dissolve
            "Once her robe is secured, Cherry smiles and runs her hand over your hair, bringing you back to the present."
            "Cherry Bosom" "Thanks for the help, baby. You did great."
            scene black with fade
            "Cherry leans in to give you a long hard kiss before pulling away and stuffing a wad of cash in your hand. You feel her eyes watching you in lidded desire as you stumble out of the side door and back into the night."
            $ Cash += 300
            $ fuckclients=True
        "I've changed my mind." if True:
            show chelsea sad
            "Staring up at the tinted windows and neon lights, you feel that there's something more to tonight than just a strip show."
            "You decide to follow your gut's instincts. You quickly turn around and walk the other way."
            show chelsea at exitScene(0.5, 1.0, 0.65, 0.5)
            "Cherry can figure something else out with her client-- this isn't your responsibility."
            scene black with fade
            "A wave of relief washes over you as you make your way back home."
    jump events_end_period

label stripclub8:
    scene bg CityN
    pause 0.5
    $ clothes, hair = casualwear
    show chelsea blank at center, enterScene(1.0, 0.5, 0.75, 0.65)
    "It's been a little while since you passed the billboard for \"CLUB 22\", but as you see it now, you feel inclined to visit."
    "At least, it wouldn't hurt to pass by."
    if fuckclients == True:
        show chelsea embarrassed
        "The memory of your last visit floods your mind. Those men's cocks inside of you, Cherry's tongue in your cunt..."
        "You feel a wave of pleasure run through you. Will they be there again tonight? Will Cherry want you to do that again?"
    elif privateclient == True:
        show chelsea sad
        "The memory of Cherry's request leaves you feeling uneasy. You had decided to not go through with it, and Cherry hasn't messaged you since."
        "What would she say if she saw you now? Will you even be allowed inside?"
    elif True:
        show chelsea confused
        "It's certainly been a while since you last visited. What kind of events are they holding tonight?"
    scene bg CityN with fade
    show chelsea shocked at right with dissolve
    "You make your way back to the familiar street of \"CLUB 22\", but when you arrive, you're shocked to find the neon lights are off and the street is cast in darkness."
    show chelsea confused
    pcname "Did the power go out?"
    show chelsea at moveSprite(1.0, 0.1, 1.4)
    pause 1.5
    show chelsea shocked
    "As you approach the darkened building, you're surprised to find a bright orange paper stuck to the door, along with spray-painted signs of 'FOR RENT' across the windows."
    show chelsea blank
    "You lean in close and squint at the paper to get a better look."
    show chelsea confused
    pcname "It's been shut down?"
    show chelsea blank
    "You guess business wasn't doing as well as you thought."
    show chelsea at exitScene(0.1, -0.5, 0.7, 0.3)
    "With a shrug, you make your way to a better lit street. It's time to find something else to occupy your time."
    scene bg HomeN with fade
    "Later on the news, once you're curled up in a throw blanket and relaxing on the couch, you watch a reporter discuss cases of illegal prostitution occurring at \"CLUB 22\" and its inevitable shutdown."
    if fuckclients == True:
        $ clothes = "naked"
        show chelsea sad with dissolve
        "You feel a wave of nausea take over as you recall the feel of the businessmens' hands on your body, their cocks fucking you without remorse."
        "It shouldn't surprise you that the club was shut down after an event like that. Cherry had treated it so normally, as if she'd done this a thousand times."
        "She must have fucked the wrong person or got caught somehow. You just hope that they won't suspect your own involvement."
        scene black with fade
        "You end up turning off the news and lay down in your bed, anxiously staring up at the ceiling as you contemplate whether either of those men will turn you in. Or even Cherry herself."
        "It's not as if you expected that going into the strip club. And surely they would get in more trouble for letting you inside in the first place."
        "You do not sleep well tonight, but at least you're comforted with the reminder that the club is shut down and you can put that chapter in your life behind you."
    elif privateclient == True:
        $ clothes = "naked"
        show chelsea sad with dissolve
        "You feel a wave of nausea take over as you recall Cherry's request. Had it all really been a ploy to fuck her client? Was it ever really a show, or just a way to whore you out?"
        scene black with fade
        "You turn off the news and head to bed, but the mixed feelings of anger and relief keep you awake."
        "At least the club is closed now and you don't have to worry about facing any of them again."
        pcname "Thank God I decided to not show up..."
        "You eventually drift off to sleep, happy to be rid of the club."
    elif True:
        $ clothes = "naked"
        show chelsea shocked with dissolve
        "You gape at the news report in shock, struggling to grasp exactly what you're reading."
        show chelsea confused
        "Prostitution? Did they really get shut down for that? Just how bad was this prostitution problem for the whole club to be shut down?"
        show chelsea sad
        "You can't help but think back on the lessons Cherry Bosom led and how close they were to going over the edge. Sometimes it really felt like everyone was being prepped for an orgy..."
        "Well, now you know why."
        scene black with fade
        "Shaking your head, you turn off the news and head to bed."
        "Looks like you're going to need to find somewhere else to hang out Sunday nights."
    jump events_end_period

label farmersmarket5:
    scene bg FarmersMarket
    "The sun is beating down hard as you approach the farmer's market, its reflection nearly blinding against the white tents and tapestries hung to garner attention."
    "Dorothy's apple stall is a welcome escape with its wooden structure and friendly red signs. At the very least, it doesn't hurt your eyes to look at it."
    $ clothes, hair = casualwear
    show chelsea blank at center, enterScene(1.0, 0.5, 0.85, 0.65)
    "The stall is already set and ready to go when you arrive, and Dorothy still has a steady stream of customers that she welcomes to her stand."
    show chelsea sad
    show GOLady1 at left with dissolve
    "Her gaze latches on you as you approach, her friendly demeanor gone."
    "Dorothy" "About time you showed up, girl! I've been running this stall for hours. My poor legs are killing me."
    show chelsea confused
    "Dorothy reaches down to rub her calf for effect. You aren't sure if she's trying to garner sympathy or is simply being dramatic."
    show chelsea blank
    "Dorothy" "Take over the booth for a moment. I need to sit down and rub some ointment on this for a moment."
    pcname "Okay."
    scene bg FarmersMarket with fade
    show chelsea happy at left with dissolve
    "You replace Dorothy at the stand while she slumps back against her yellow folded chair and grabs a bottle of lotion from her purse."
    show chelsea laugh
    "As you pass out free samples and help ring up customers, your mind wanders back to the last time you helped Dorothy out here."
    show chelsea happy
    "You can't help glancing back at Bertha's booth, your gaze snagging on the rigged pillar."
    show chelsea laugh
    "It's so unfair of her to trick customers like that. There has to be some kind of rule against it, right? You can't imagine these two old women getting away with this for very long."
    show chelsea shocked
    show GOLady1 with dissolve
    "Dorothy" "Eyeing up the competition?"
    "You jump, startled. You didn't even hear the old woman approach, but there she is, glaring at Bertha's stall from behind your shoulder."
    show chelsea confused
    pcname "You don't like her?"
    "Dorothy snorts."
    show chelsea blank
    "Dorothy" "Like her? I {i}hate{/i} her."
    "From the harsh look in her eyes, you believe it to be true."
    show chelsea confused
    pcname "Why? What did she ever do to you?"
    show chelsea happy
    "Dorothy harumphs and crosses her arms. Another customer approaches and you busy yourself taking care of them before Dorothy answers."
    show chelsea shocked
    "Dorothy" "Bertha and I go way back. We lived down the street from each other. Grew up together, went on double dates-- we were best friends."
    "Her confession surprises you. That doesn't sound like the kind of woman that she would create a rivalry with."
    show chelsea confused
    pcname "So what happened?"
    show chelsea blank
    "Dorothy" "Don't jump ahead of yourself, girly! I'm just getting started!"
    "She spits at the ground in Bertha's direction, and although the woman looks elderly and frail, there is nothing but fire behind her eyes."
    show chelsea confused
    "Dorothy" "Oh, Bertha was always a copycat. She wanted everything I had, and it {i}had{/i} to be better than mine."
    "Dorothy" "Halloween costumes, toys, haircuts, {i}boyfriends{/i}-- it didn't matter. If I had it, she had to have it, too."
    show chelsea blank
    "You glance back at Bertha's stall. It's hard not to see the similarities between hers and Dorothy's, from the free sample setup to the specific arrangement of fruit."
    "Except where Dorothy's stand is clearly designed and handled with care, Bertha's a neater, more professional copy, with extra touches like napkins and yellow decor to catch the customer's eye."
    "Dorothy doesn't notice your distraction and carries on with her story, her own anger building by the minute."
    show chelsea shocked
    "Dorothy" "Which is why that backstabbing {i}whore{/i} stole my dear Frank!"
    "Her voice chokes on the sound of his name. You can see the devastation and betrayal on her face, and Dorothy brushes a tear away from her face."
    show chelsea confused
    pcname "Who is Frank?"
    show chelsea blank
    "Dorothy composes herself, pulling her shoulders back and standing up as straight and tall as she can. Even doing so, she's still significantly shorter than you."
    "Dorothy" "Frank was my boyfriend fifty years ago."
    pause 1.0
    show chelsea shocked
    "...Did she say {i}fifty years ago?{/i}"
    "You stare at her, mouth agape. She can't be serious, can she?"
    pause 1.0
    show chelsea angry
    pcname "...That's what this whole thing is about? Some guy you haven't even dated in the past fifty years?"
    show chelsea sad
    "You can't imagine holding a grudge that long, no matter how wronged you'd been. Especially over something as petty as a boy..."
    "Dorothy scoffs, waving you off with a wrinkled hand."
    show chelsea blank
    "Dorothy" "Bah! A child like you would never understand. This is about a woman's pride!"
    "Dorothy" "Frank and I were practically engaged. We had been sweethearts since childhood! But Bertha {i}had{/i} to have him, no matter what."
    "Dorothy" "I can remember it like it was yesterday; Mary Lou and I were discussing graduation plans while Frank left to get me a drink."
    "Dorothy" "He didn't come back for quite some time, so I got worried and went searching."
    show chelsea confused
    "Dorothy" "Wouldn't you know, I find the bastard with his drawers down, riding that whore of a woman in the coat closet!"
    "The old woman's face is red with anger, and you can see clear as day that the wound of that night is still fresh on her heart."
    show chelsea sad
    "You frown, feeling sympathetic for the old woman. She obviously still has feelings for this man, even after all this time."
    show chelsea confused
    pcname "Is she still with him?"
    show chelsea shocked
    "Dorothy" "Oh heavens no. Frank would never be caught dead gallivanting around with some-- some {i}harlot{/i}."
    show chelsea blank
    "She practically hisses the word, her gaze cutting right back to Bertha. Bertha seems oblivious, strutting around her booth as she greets her own customers and offers samples. Whether she'll trick anyone today has yet to be seen."
    "Dorothy" "It was a one time thing, and although Frank begged for me to take him back, I just couldn't. Not knowing where he'd been-- {i}who{/i} he'd been in."
    show chelsea angry
    pcname "It sounds like Frank wasn't that loyal in the first place. He may have been thinking about it and Bertha just happened to be the first girl he came across."
    show chelsea sad
    pcname "He didn't deserve you."
    "Dorothy snorts and nods in agreement."
    show chelsea blank
    "Dorothy" "Now that may be true. But no, Bertha had sunk her claws in him early on. It was only a matter of time before she convinced him to stray."
    "Dorothy" "Things were never the same that night, and Bertha has only made her attempts to live my life for me more obvious."
    show chelsea shocked
    "The elderly woman clenches a fist at her side and slams it down hard on her booth's tabletop. The apples rattle a little, but the false leg doesn't give out."
    show chelsea confused
    "You're confused until you see that a carefully placed crate is holding the leg in place."
    show chelsea shocked
    "Ah. So that's how she does it."
    show chelsea blank
    "You look between their booths once more, and their similarities strike you as more than just the surface; even their deviant tricks to pull more money from customers is the same."
    show chelsea angry
    pcname "You're pulling the same tricks she is."
    show chelsea shocked
    "Dorothy" "No, she's pulling {i}mine.{/i} There's a difference!"
    "She doesn't even deny it, which makes you angrier. You shouldn't have to be working for her here in the first place!"
    show chelsea angry
    pcname "But you're tricking innocent people!"
    show chelsea confused
    "Dorothy" "So? Money is money. We all have bills to pay somehow."
    pcname "Isn't scamming people in a church parking lot a sin?"
    show chelsea shocked
    "Dorothy" "I never said I was religious."
    show chelsea blank
    "Dorothy" "Now enough of your yappin'! We still have work to do."
    hide GOLady1 with dissolve
    "Dorothy tries to leave then, busying herself with arranging a few apple-themed displays on the side of the booth."
    "Knowing that these two booths are a scam, and that you yourself have been tricked, you have no desire to work off any debt for this woman."
    show chelsea angry
    pcname "I'm leaving."
    show chelsea blank
    show GOLady1 with dissolve
    "Dorothy halts in her tracks, her gaze snapping back to you with a serious expression."
    "Dorothy" "You can't. You haven't paid off your debt yet."
    show chelsea angry
    pcname "My debt shouldn't matter if you tricked me to work for you. I don't have to do free labor anymore."
    show chelsea blank
    "Dorothy's eyes narrow into slits. You can sense her anger rising underneath her calm surface, like a violent wave about to crash. You know the look well from your own mother's face when she would catch you talking back to her."
    show chelsea shocked
    "Dorothy" "You signed a contract. Whether you like it or not, that is a binding agreement."
    "You blanch, vividly remembering your signature on that piece of paper."
    show chelsea sad
    "Right. The contract."
    show chelsea angry
    pcname "But it's not a real contract--"
    show chelsea shocked
    "Dorothy" "It's a written agreement. If I were to call the police right now, they're going to enforce it."
    show chelsea sad
    pcname "T-Then I'll..."
    show chelsea shocked
    "You'll what? There has to be some way to get out of this agreement."
    "You look around the farmer's market, desperate for some kind of solution to your problem."
    show chelsea happy
    "Once more, you stare at Bertha's loose beam."
    show chelsea angry
    pcname "I'll expose you, then."
    show chelsea blank
    "Dorothy" "Expose me? And how will you do that?"
    show chelsea angry
    pcname "You and Bertha use the same kind of methods for your booth. I'll just show them how you rigged it up to scam poor customers like me."
    show chelsea embarrassed
    "Dorothy purses her lips in thought and, for a brief, joyous moment, you're sure you have her. There's no way she can get out of this one-- not with the proof you have."
    show chelsea sad
    "...Or maybe she can."
    "Dorothy" "I'll just say you set me up. Who are they going to believe? A troublemaker trying to get out of her contract, or an old lady they've known for years?"
    show chelsea shocked
    "You feel your lips part in shock and a triumphant expression crosses the old woman's face. She has the advantage on you and she knows it."
    show chelsea angry
    pcname "B-But that's not fair!"
    show chelsea sad
    "It's all you can manage to sputter out, too shocked to think of a more intelligent argument. Dorothy nods, fully knowing she has won."
    "Dorothy" "Life isn't fair, sweet cheeks."
    "Her lips curl up in a sadistic sort of pleasure as you realize you're stuck. You watch in despair as she wanders around the booth, tidying up anything that looks out of place."
    "After a few moments she looks back at you, eyebrow raised and gaze scrutinizing."
    show chelsea shocked
    "Dorothy" "But, you know what [pcname], I'm feeling generous today. You're young. Smart--well, no, but you're young."
    show chelsea sad
    "Dorothy" "It won't do to have you so miserable at my booth. That will only drive my customers away."
    "Dorothy" "So I'll offer you a choice. Either you can help me make that extra money {i}my way{/i}, or you can keep your mouth shut and do as I say until you pay off your debt."
    "Dorothy" "And before you answer, know that I'll split some of the payments with you if you help. I'm not cruel, after all."
    menu farmersmarketscam:
        "Participate in the scam." if True:
            show chelsea blank
            "You shift back and forth on the balls of your feet, heavily weighing your options."
            show chelsea confused
            "You have to continue working for Dorothy anyway until your debt is paid, but at least if you helped her out, you would be making extra money on top of it."
            pause 1.0
            show chelsea blank
            pcname "...Alright. I guess I can do that."
            "Dorothy" "Hmph. Maybe you are a little smarter than you look."
            "Dorothy" "Good. We want to get one down before closing time, so..."
            "Dorothy checks her watch, tapping the glass cover with one thin finger."
            show chelsea sad
            "Dorothy" "Next customer or two, whichever ends up closer to the baskets."
            "Dorothy gestures toward a basket of apples on the stand."
            "Dorothy" "Ah, here comes one now."
            show chelsea shocked
            "You look up to see a pregnant woman and her small child walk up toward the booth, their eyes wide and excited as they take in the bounty of apples and apple-like treats for sale."
            show chelsea sad
            "A pregnant woman. Of course, it {i}had{/i} to be a pregnant woman."
            show chelsea happy
            "You try to push down your guilt as you smile at her and her child, greeting them with a friendly customer service voice."
            show chelsea embarrassed
            "You can feel Dorothy maneuvering behind you as you take the woman's order, but you try not to look at her, focusing on bagging the woman's order instead."
            show chelsea sad
            "With any luck, Dorothy will find someone else to scam. This poor woman already looks like she has her hands full..."
            "But as soon as you see the small child run forward, toward the basket of apples, you already know it's too late."
            show chelsea shocked
            "He stumbles into the booth, barely enough to jostle it, and you hear Dorothy subtly knock something down beside you. The apples go tumbling, their red skins bruising as they hit the hot asphalt of the parking lot."
            "You gasp and stand back, feigning shock. It comes to you more naturally than you thought it would."
            "The mother grabs her son and you watch as they scurry across the parking lot, desperately trying to clean up the mess."
            show chelsea blank
            "Pregnant Lady" "I-I'm so sorry! I had no idea he was-- He shouldn't have been-- I'm {i}so{/i} sorry!"
            "The woman stumbles over her words and attempts to offer up the ruined apples back. Dorothy scowls down at them, causing the boy and even his mother to shrink back under her harsh stare."
            "Dorothy" "Look at the mess you've made! My poor booth!"
            show chelsea shocked
            "Dorothy" "How is my granddaughter here supposed to afford her lung surgery if we can't make money?"
            "Dorothy dabs her eyes with a handkerchief, although where on earth she got it from, you couldn't say. It's as if the woman was born for the stage."
            "Pregnant Lady" "Lung surgery?"
            show chelsea confused
            pcname "Lung surgery?"
            "You realize a beat too late that you and the pregnant woman both said it at the same time. The poor mother looks at you with a mix of confusion and guilt. She wrings her hands in front of her in worry."
            show chelsea blank
            "It seems Dorothy lives for dramatics."
            show chelsea sad
            "Catching onto Dorothy's intention, you hunch over and give a weak cough into your elbow. It sounds as pathetic as you feel."
            "There's no missing the displeased look Dorothy gives you out of the corner of her eye, but she's quick to recapture the attention of the mother and resume her usual scheme."
            "Once the woman has paid her $200, Dorothy shoos her off and returns to the stand."
            pause 1.0
            show chelsea confused
            pcname "...You gave me lung surgery?"
            "Dorothy doesn't look up from her stack of cash as she counts."
            show chelsea blank
            "Dorothy" "I didn't give it to you, you need it. That's why we're running this stand. Or, so that's what we tell people. Our healthcare system is as poor as the States, so they'll sympathize."
            "She squints at one of the bills, deciphering its validity before tucking it back in with the rest."
            show chelsea blank
            "Dorothy" "We'll need a sob story-- every good con has a sob story. I'll be your grandmother; you're my sick granddaughter that I've gotten saddled with when your no good lousy mother ran off."
            pause 1.0
            show chelsea angry
            "Hearing her talk about your mother like that-- even as a hypothetical-- makes you feel sick to your stomach."
            show chelsea sad
            pcname "...My parents are dead."
            "The words barely come out as a whisper, but Dorothy catches it, nodding enthusiastically."
            "Dorothy" "Even better! Dead parents are sure to draw up more money."
            "Dorothy" "We'll say you have some sort of lung disease and need surgery. You've got a little time before the hospital, but not much."
            "Dorothy" "I would've preferred to be the elderly, vulnerable grandmother in the situation, but..."
            "Her gaze flickers up to you in displeasure. From the pucker of her lips, you'd assume she had just eaten a lemon whole."
            show chelsea shocked
            "Dorothy" "I see you aren't the best actress, so best to keep your involvement to a minimum."
            show chelsea blank
            "You brush off her stinging insult with a deep sigh, looking back at the direction the woman had left."
            show chelsea confused
            pcname "Did we really have to scam {i}her{/i} of all people, though? She looks like she's struggling enough."
            "Dorothy" "Hmph. If she can afford two children, she can afford to fix my booth."
            show chelsea sad
            "Not that the booth was ever in danger in the first place."
            pcname "We don't know her situation enough to make that kind of judgement..."
            show chelsea shocked
            "Dorothy" "Doesn't matter. What's done is done, can't take it back now."
            show chelsea blank
            "Dorothy splits the stack in two and holds out half of the money to you. You stare at it, sensing a trick."
            show chelsea confused
            pcname "I thought I still had to pay you back."
            "Dorothy" "You do, but that'll just come from sales. This will be our little secret."
            show chelsea blank
            "Dorothy presses the bundle of cash into your palm and walks away to start cleaning up the booth."
            pause 1.0
            show chelsea sad
            "Maybe you do feel a little bad-- okay, {i}really{/i} bad-- for tricking that poor woman out of her money, but feeling the stack of bills in your hand helps make up for it a little."
            scene black with fade
            "You pocket the cash and carry on with the rest of your day."
            $ Cash += 100
            $ applescam = True
        "Play it safe." if True:
            show chelsea blank
            "You shake your head at once. There's no way you can help with something like this!"
            show chelsea sad
            "What if we're found out? You have no doubt that Dorothy would throw you under the bus in her stead, leaving you to handle whatever lawsuits and jail time the police decided was suitable."
            "You barely have enough to get by each month, let alone paying lawyers and damages..."
            show chelsea angry
            pcname "I'm going to pass. I would rather just work my debt off."
            show chelsea sad
            "Even though it pains you to say it, it's still a better option than scamming people."
            "Dorothy clicks her tongue, obviously annoyed by your choice, but shrugs and tries to brush it off as no big deal."
            "Dorothy" "If that's what you want, fine. But get back to work."
            show chelsea blank
            pause 0.8
            show chelsea happy
            "You nod, forcing a smile on your face as you greet the next customer and help bag her order."
            "As you turn to the side to handle her cash, you notice her small child run up to the stand. He bumps into the booth slightly, but it's enough to set off Dorothy's trap."
            show chelsea shocked
            "Apples go flying and you notice Dorothy struggle to hide her smirk as the woman and child gasp, rushing to pick up the now bruised fruit."
            show chelsea sad
            "Dorothy" "Look at the mess you've made! My poor booth!"
            "You sigh, turning away. You can't stand to watch her berate this poor mother for something she herself set up from the start."
            scene black with fade
            "The con goes by similarly to when you yourself were scammed, and by the end of the day, Dorothy leaves an extra $200 richer."
    jump events_end_period

label farmersmarket6:
    scene bg FarmersMarket
    "The farmer's market is bustling by the time you arrive, the parking lot filled with many people who have either finished work, church, or school activities for the day."
    "The church bells echo across town as you make your way to Dorothy's familiar wooden booth tucked in the midst of the chaos."
    $ clothes, hair = casualwear
    show chelsea blank at center, enterScene(0.8, 0.5, 0.65, 0.55)
    "You approach the booth with some expectation that she'll scold you for being late-- it's only three minutes, but to Dorothy, that could be a lifetime-- but the old woman doesn't even look up at you, her glare cast across the parking lot."
    show chelsea confused
    pcname "Uh, Dorothy...?"
    "You point at a few customers that are near the apple basket. If Dorothy were to kick the crate now, the whole thing would come tumbling down."
    show chelsea blank
    show GOLady1 at left with dissolve
    "Instead, Dorothy huffs and greets the customers as usual, bagging up their order quickly before sending them on their way."
    if applescam == True:
        show chelsea shocked
        "You struggle to hide your surprise, having been utterly convinced that she would be jumping at the opportunity to scam these youths out of their money."
        "Instead she just glares to the side, her focus drawn away."
    elif True:
        show chelsea embarrassed
        "You can't help but feel a little relieved that she didn't go through with her scam right then and there. You're not sure you're ready to deal with her theatrics today."
        show chelsea sad
        "Dorothy glares to the side, completely and utterly distracted."
    show chelsea blank
    "You walk forward and stand beside her, searching for the source of your boss's distress."
    show chelsea confused at moveSprite(0.5, 0.2, 0.55)
    pcname "What are we looking at, Dorothy?"
    show chelsea blank
    "But you don't even need to ask to see Bertha's successful banana booth, its bright yellow design nearly blocked out by the crowd of people surrounding it."
    "From here you can make out two steady workers behind the register-- one of them Bertha, and another younger girl with long, wavy black hair and a sundress as bright as her smile."
    "Dorothy glances up at you from the side, finally taking in your entrance."
    show chelsea shocked
    "Dorothy" "When did you get here? Bah, forget about it. You're late."
    "She shakes her head, but even her voice isn't into it as she scolds you. This is certainly a new distressing side of Dorothy you're seeing."
    show chelsea blank
    "Dorothy" "Look at that. Just look! I told you, the woman loves to copy me. She's obsessed with it."
    show chelsea confused
    pcname "What did she do this time?"
    show chelsea happy at moveSprite(0.2, 0.5, 0.55)
    show GHCMan at right with dissolve
    "You keep your voice light and friendly as you move on to greet the new approaching customers. If Dorothy won't take care of them, you will."
    show chelsea laugh
    hide GHCMan with dissolve
    "The old woman rants behind you, completely ignoring the transaction as she focuses solely on her arch enemy."
    if applescam == True:
        show chelsea happy
        show V Casual Pout at right with dissolve
        "Dorothy" "She brought her granddaughter in to help-- her {i}real{/i} granddaughter, not some poor actress she picked up off the street."
        show chelsea laugh
        show V Casual Smile
        pause 1.0
        hide V Casual Smile with dissolve
        "You notice how she cuts a glare in your direction, her implication clear."
        show chelsea sad
        pcname "I didn't think I was {i}that{/i} bad. You threw me in the spotlight..."
        "But the look on Dorothy's face says yes, you were just that bad. Maybe worse. She shakes her head and sighs, looking back at Bertha."
    elif True:
        show chelsea happy
        show K Casual Blank at right with dissolve
        "Dorothy" "She brought her granddaughter in to help. See, I told you-- I {i}told{/i} you! The woman has to copy everything I've ever done!"
        show chelsea laugh
        show K Casual Laugh
        pause 1.0
        hide K Casual with dissolve
        "Dorothy" "She sees me working with a young girl and now she has to bring one around your age in, too!"
    show chelsea confused
    "Dorothy" "This is a real shame. We need to be careful."
    pcname "Careful? How come?"
    show chelsea blank
    "Dorothy" "Well, just look at my booth, girl! There's hardly anyone here."
    "Dorothy" "Dealing with Bertha is bad enough, but her granddaughter is a whole other level of charming. And you're... you."
    "You glare back at her but Dorothy hardly notices, already back to watching the crowd around Bertha's stall."
    if applescam == True:
        show chelsea angry
        pcname "I didn't think I was that bad. Your expectations are too high."
        show chelsea blank
        "Dorothy" "Or I got saddled with an insufferable fool of a girl."
        show chelsea angry
        pcname "You don't {i}have{/i} to keep me here, you know. You could let me get out of the contract if you hate it so much."
        show chelsea sad
        "But even as you say it, you don't want that to happen. Having that extra $100 last week was more than nice after a long day's work."
        show chelsea embarrassed
        "If it meant more money like that, you could get used to the occasional scam with this old lady."
        show chelsea blank
        "Dorothy is quick to call you out on your bluff, waving you off like a pesky fly."
        "Dorothy" "Oh hush, child. We both know you're not going anywhere."
    elif True:
        show chelsea angry
        pcname "I've been perfectly nice to the customers, but if you wanted a real worker with real work ethic, maybe you shouldn't have tricked me into working it off."
        show chelsea confused
        "Dorothy" "You signed the contract yourself. I'd hardly call that a trick."
        show chelsea blank
        "You would disagree, but knowing this conversation will lead you nowhere, you drop it. After all, it's only another week or two before your debt is fully paid and you never have to work for her again."
        show chelsea sad
        "That is, as long as you can get more customers over here."
    show chelsea confused
    "Dorothy" "Damn it! She's doing something over here, I can see it. What is she trying to steal now?"
    show chelsea angry
    pause 1.0
    show chelsea confused
    "A flash of irritation runs through you as Dorothy continues ranting to herself while you take care of the new hoard of customers coming your way."
    $ damienAttire(1)
    show chelsea happy
    show Damien Blank at right with dissolve
    "Maybe if Dorothy wasn't so obsessed with competing with Bertha and worrying about every little thing her competitor did, she would notice that her booth was actually getting busy."
    show chelsea laugh
    show Damien Happy
    pause 1.0
    hide Damien Happy with dissolve
    pcname "Dorothy, I could use your help here."
    show chelsea happy
    show GCBoy at right with dissolve
    "Dorothy" "And her hair is all over the place. Who wants to eat banana bread with hair--"
    show chelsea angry
    pcname "{i}Dorothy.{/i}"
    show chelsea blank
    "The old woman scowls as she snaps her head in your direction."
    pause 1.0
    show chelsea confused
    pcname "A little help? Please?"
    show chelsea blank
    "Her gaze softens as soon as she sees the crowd forming around you."
    "Dorothy" "Oh. Dear, why didn't you say something?"
    show chelsea laugh
    hide GCBoy with dissolve
    "Dorothy pulls on her apple-themed apron and rushes to the front, the mask of a kindhearted grandmother on her face as she greets the next group."
    scene black with fade
    "You both work like this for a while, greeting customers and rushing to bag up their orders. Dorothy doesn't even go near her false leg setup, too busy helping one customer after the next."
    "After a while, the crowds finally start to dissipate, and you're left sweating and chugging down a nearby bottle of water to ease the ache of your dry mouth."
    scene bg FarmersMarket with fade
    show chelsea embarrassed with dissolve
    show GOLady1 at left with dissolve
    "Dorothy scrutinizes you from the sidelines, a deep look of concentration detailed on her wrinkled face."
    show chelsea confused
    "You set the now empty water bottle down, unnerved by her stare."
    pause 1.0
    show chelsea sad
    pcname "...What?"
    "Dorothy" "I want you to go over there and see what they're doing."
    if applescam == True:
        show chelsea confused
        pcname "What? But what about the customers?"
        show chelsea blank
        "Even with the smaller crowd, there were still people roaming the farmer's market. If Dorothy wanted to pull off her scam, she needed you to be there."
        "Dorothy" "Go, go, I'll handle them. Just go observe."
        show chelsea sad
        pcname "But--"
        "Dorothy" "Now! You stubborn, impatient thing..."
        hide chelsea with dissolve
    elif True:
        show chelsea angry
        pcname "Dorothy, I told you I wasn't helping in any scams--"
        show chelsea blank
        "Dorothy" "Then don't! But the least you can do is see what the competition is up to."
        show chelsea sad
        "Dorothy" "Now move, move, you airheaded child!"
        hide chelsea with dissolve
    scene black with fade
    "Dorothy all but shoves you away from the booth, her frail arms carrying a surprising amount of strength for a woman so small and old."
    "With a deep sigh, you leave the booth and walk towards Bertha's."
    "Despite the on-and-off success of Dorothy's apple booth, Bertha's banana booth is booming with business, her little stand filled to the brim with eager customers waving their money for her goods."
    scene bg FarmersMarket with fade
    show chelsea blank with dissolve
    "With a crowd this big, she doesn't even need to scam anyone today."
    "You remain on the sidelines, squeezing between a few eager shoppers to get a better look at the front of the booth."
    show chelsea sad
    "You don't want to go too far in case Bertha recognizes you, but it's hard to see around the several groups of people pushing to the front of the line."
    show chelsea blank
    "After a little bit of tough maneuvering, you manage to position yourself next to one of the beams, making sure to keep yourself a safe distance away in case it gives out."
    show GCGirl at right with dissolve
    "Bertha's granddaughter is even prettier up close, with a perfectly straight smile and icy blue eyes. A warm southern accent weaves through her speech and even you feel inclined to talk to her just to hear it again."
    show chelsea confused
    "Damn. This girl really is charming."
    show chelsea blank
    hide GCGirl with dissolve
    "You try not to draw too much attention to yourself as you step closer, your gaze dropping to the item in the alluring girl's hands."
    show chelsea confused
    "It's a little clear container filled to the brim with some kind of creamy... pudding? No, ice cream! You watch as cold steam rises from the top, Bertha's banana label bright yellow on the side."
    show chelsea embarrassed
    "Just staring at the container brings a little moisture to your lips. It's so hot out this afternoon, and even just a spoonful of ice cream would be delicious..."
    show chelsea shocked
    show GOLady2 at left with dissolve
    "Bertha" "Can I help you, sugar?"
    show chelsea sad
    "Ice freezes in your veins as you hear Bertha address you from behind. You stand still, hoping that maybe she was speaking to someone else."
    "Bertha" "Sugar, I'm talking to ya. Dorothy's girl?"
    show chelsea shocked
    pause 1.0
    show chelsea sad
    "Crap. No use hiding it now."
    show chelsea happy
    "Slowly, you turn to face Bertha with an awkward grin. She smiles back, but there is nothing kind behind those cold eyes."
    pcname "Ah, hey..."
    show chelsea embarrassed
    "Bertha" "Hey, sugar."
    "Bertha" "Now what is little Dorothy's girl doing here on my side of the market? You weren't tryna {i}steal{/i} nothin', were ya?"
    show chelsea shocked
    pcname "No, of course not! I would never!"
    "Bertha" "That's good to hear. Then tell me, what can I help you with?"
    show chelsea sad
    "Your mouth goes dry as you try to think up an answer."
    pause 1.0
    show chelsea shocked
    pause 0.5
    show chelsea embarrassed
    pcname "I was just... going to buy some ice cream."
    "You point across to the container in her granddaughter's hands. You're sure Dorothy would be furious to see you handing money over to her, but now isn't the time to think of Dorothy."
    "Bertha" "Some ice cream, huh? Well you just wait right there."
    show chelsea sad
    hide GOLady2 with dissolve
    "Bertha walks away from the stand, but before you can run off, she's already wandering back with a plastic pint in hand."
    show chelsea shocked
    show GOLady2 at right with dissolve
    "Bertha smiles tightly as she places the container in your hands."
    show chelsea embarrassed
    "Bertha" "You tell Dorothy that one's on the house now, ya hear?"
    show chelsea embarrassed
    pause 1.0
    show chelsea shocked
    pause 0.5
    hide chelsea with dissolve
    "Before you can respond, another group pushes past you, fighting their way to the front. You're shoved and knocked to the back of the line, barely escaping with the container of ice cream intact."
    scene bg FarmersMarket with fade
    show chelsea blank with dissolve
    "Once you're free from the crowd, you step aside and stare down at the container."
    show chelsea embarrassed
    "Bertha's Banana Ice Cream-- made from real bananas!--with chocolate fudge drizzle. Just reading the text leaves your stomach growling."
    show chelsea blank
    "So it wasn't a scam today; she had upped her game, and she wanted Dorothy to know it."
    scene black with fade
    "You walk leisurely back to Dorothy's booth, reluctant to show her the new product. Dorothy had several apple desserts, but ice cream was trickier to make and even harder to sell outdoors. Bertha must have been planning this for weeks, if not months."
    scene bg FarmersMarket with fade
    show GOLady1 at left with dissolve
    show chelsea at center, enterScene(0.8, 0.5, 0.65, 0.55)
    "Dorothy" "There you are, child! I was wondering if you'd gone and left me."
    "Dorothy waves an accusatory finger at you as you return, but she doesn't look half as mad as she sounds. Curiosity burns in her gaze, desperate to know what her competitor is up to."
    "Dorothy" "Well? What did you learn?"
    "You hold up the plastic container. Dorothy snatches it out of your hands, her eyebrows shooting up to her hairline."
    "Dorothy" "Ice cream?"
    "She spins it over in her palms in disbelief."
    "Dorothy" "How in the hell did she manage {i}this{/i} one?"
    show chelsea confused
    pcname "I don't know. I guess she found a good way to transport it. Uh, she told me to tell you it was on the house."
    show chelsea blank
    "Dorothy snorts, rolling her eyes."
    "Dorothy" "Of course she did."
    show chelsea happy
    "The old woman ducks under her booth to grab two plastic spoons. She offers you one before digging into the pint."
    show chelsea confused
    "She immediately spits the ice cream back out, gagging."
    show chelsea confused
    "Confused, you dig in and take a bite as well. A disgusting taste {i}and{/i} texture hits your tongue. You spit it out onto the ground, reaching for another leftover water bottle to get rid of the taste."
    show chelsea angry
    pcname "What {i}was{/i} that?!"
    show chelsea sad
    "Dorothy" "That old fool! This isn't ice cream at all-- she just mushed some bananas together and shoved cheap chocolate on top!"
    show chelsea confused
    "You look back at the stand, even more confused. If the ice cream was bad-- or not even real in this case-- why were there so many customers?"
    pcname "Do you think it's just the one she gave us?"
    show chelsea blank
    "Dorothy" "It could be... but I doubt it."
    "Dorothy heaved a heavy sigh before taking another bite. She grimaced, once more spitting the remains onto the ground."
    show chelsea sad
    "Dorothy" "Or it could be a mix. That's a risky scheme you're throwing there, Bertha... Some good, some bad. Hm."
    pcname "Why would she do that, though? There's no point in serving bad ice cream to your customers."
    show chelsea confused
    "Dorothy" "Unless it's just to your competitors. Look-- half the people there sell things here, too."
    show chelsea blank
    "You look back at the crowd and, sure enough, you recognize a few faces from the nearby booths."
    show chelsea confused
    pcname "I don't get it."
    show chelsea blank
    "Dorothy" "There isn't anywhere else to get something cold around here except maybe some water bottles, if you're lucky."
    "Dorothy" "But bringing a freezer full of ice cream in? You've got the whole town biting."
    "Dorothy" "Kids are crying, complaining, making a mess. You buy 'em some ice cream to shut them up, and even if it tastes bad, if it's a hot enough day, no one will complain."
    show chelsea sad
    "Dorothy" "But if your competitors try to warn customers against it because the ones they had were bad, and other customers are saying it's delicious, you'll assume the competitors don't want you to eat it so they can get your money instead."
    "Dorothy" "It brings down their own credibility and they don't even realize it."
    "Dorothy shakes her head in frustration."
    show chelsea confused
    pcname "But why ice cream? Why not like, chocolate covered bananas or something? That's easier."
    show chelsea blank
    "Dorothy" "Harder to mess that up, I assume. I don't know. Does it look like I live in Bertha's mind?"
    "From how easily Dorothy deducted what Bertha was doing, you want to tell her yes, but decide to keep your mouth shut instead. That's probably not what she wants to hear right now."
    show chelsea confused
    pcname "Alright. Then what do we do?"
    show chelsea blank
    "Dorothy sighs, staring out across the marketplace."
    "Dorothy" "Nothing today. We don't have the resources to compete with that."
    "Dorothy" "But it's supposed to get colder over the next few days. Maybe we can whip something up that'll bring them here instead..."
    show chelsea embarrassed
    pcname "What about apple cider?"
    "Dorothy" "Aha! Now there's an idea. Apple cider... Mmm. My mother used to make that every fall."
    show chelsea blank
    "Dorothy" "It's settled. As long as the weather cools back down like it's supposed to, we'll prepare apple cider for next week."
    "Dorothy" "I'm leaving you in charge of getting everything we need for selling it. I'll make it."
    show chelsea shocked
    pause 1.0
    show chelsea confused
    pcname "Wait, me? You want me to market the whole thing? But I don't know the first thing about--"
    show chelsea sad
    "Dorothy" "I didn't ask for backtalk, girl. I gave you an order. Now don't start up any nonsense with me."
    show chelsea blank
    "Dorothy looks back at Bertha's booth with a new, hopeful gleam in her eyes. When she turns back to you there's a new confidence in her step."
    if applescam == True:
        "Dorothy" "Now, the market's ending soon. Let's get our extra pay for the day and go home, alright?"
        pcname "Sure."
        show chelsea sad at moveSprite(0.5, 0.2, 0.55)
        "You take up your usual positions behind the counter, and as the next customer approaches, you do your best to look weak and sickly as you help."
        "Based on Dorothy's hard glares you can tell it's not the most convincing act, but it seems to be enough to garner some sympathy from the man across from you."
        show chelsea shocked
        "After a few minutes, the man leans forward on the table and Dorothy nudges the crate out of the way. The table falls and, with it, all of the apples."
        show chelsea blank
        "There are gasps. There are apologies. And then there's $200 in Dorothy's hand being split between the two of you."
        show chelsea embarrassed
        "Dorothy doesn't hide her grin once the man leaves and she presses the bundle of cash into your palm. You stuff it in your pocket, secretly pleased with the easiest part of your job."
        pause 1.0
        show chelsea sad
        "Then you look at all the fruit you have to clean up and groan. It was too good to be true."
        "You spend the rest of your afternoon cleaning up at the market and helping Dorothy place her produce and props away before leaving the closed market."
        scene bg FarmersMarket with fade
        show chelsea blank with dissolve
        "As she drives away, you think back on your idea for the apple cider. It would be delicious to have and you're sure it would do well in cold weather, but you had nearly forgotten about the leg scam in your haste to come up with a solution."
        show chelsea sad
        "The extra money has been nice so far. Will that all go away when you help Dorothy branch out with new products?"
        scene black with fade
        "You hope not, but you clutch the money in your palm a little tighter as you leave the parking lot."
        $ Cash += 100
    elif True:
        "Dorothy" "Now, the market's ending soon. I still need to get my extra pay for the night, so you start planning our marketing strategy."
        show chelsea confused
        pcname "Uh, sure."
        show chelsea blank
        pause 1.0
        hide chelsea with dissolve
        "Dorothy waves you off and takes over the front of the stall while you recline back in the chair."
        scene black with fade
        "You can't help but wince as you hear the inevitable crash of the booth and apples rolling once more on the ground."
        "You really hope this cider works out, if only so you don't have to witness anymore scams with this lunatic of an old woman."
    jump events_end_period

label farmersmarket7:
    scene bg FarmersMarket
    "By the time you arrive back at the farmer's market, Dorothy already has her booth set up with two large thermos canisters of apple cider."
    $ clothes, hair = casualwear
    show chelsea sad at center, enterScene(0.8, 0.5, 0.6, 0.5)
    "It's a good day for it too, considering how the cold wind hits your back and cuts right through your clothes. You fold your arms over your chest in a weak attempt to ward off the cold."
    show chelsea blank
    "It seems the cider has been working while you've been gone; there is already a large crowd around the booth, each customer clamoring to get the next cup."
    show chelsea sad
    "Your arms are heavy with the marketing materials Dorothy requested as you approach the booth: stickers, flyers, and whatever posters you didn't just spend the past hour stapling across town. All for some cider."
    show chelsea happy
    "But whereas Bertha's ice cream was atrocious, Dorothy's cider is actually {i}good,{/i} regardless of who you're serving."
    show chelsea embarrassed
    "You serve a cup for yourself now, welcoming the spiced liquid as it warms up your body."
    show chelsea shocked
    show GOLady1 at left with dissolve
    "Dorothy" "Don't you be drinking all our merchandise, girl! We still have customers to serve!"
    "Dorothy's voice cuts through the crowd, casting a small glare in your direction before she rushes to greet the next customer."
    show chelsea sad
    pcname "I just spent the past hour telling everyone about your booth. Can't I have a little break?"
    show chelsea shocked
    "Dorothy" "Does it look like you have time for that?"
    pause 1.0
    show chelsea blank
    "Dorothy gestures across the crowd. You sigh, setting your cup down and moving to greet the next customer."
    scene bg FarmersMarket with fade
    "You keep up with the pace of the crowd for a while, and the customers' faces turn into a nondescript blur of random features as you repeat your spiel again and again and again."
    show chelsea happy with dissolve
    pcname "Hi there, what can I get for you today?"
    show GCGirl at right with dissolve
    "Bertha's Granddaughter" "So you're selling cider now? That's smart."
    pause 1.0
    show chelsea shocked
    "You blink, surprised to find Bertha's Granddaughter in front of you. She's even cuter today, with a warm knitted scarf and autumn leaf embroidered cardigan."
    show chelsea confused
    "But why is she at your stall?"
    pcname "Um... Yeah. We are."
    show chelsea blank
    "You look back at Dorothy for some kind of cue, but she doesn't even notice Bertha's relative; she's got her own hands full with other customers."
    show chelsea laugh
    "You turn back to the dark-haired girl and give her your best customer service smile. Just because she works for her grandmother's booth doesn't mean you have to be rude, after all."
    pcname "Did you want some?"
    show chelsea embarrassed
    "Bertha's Granddaughter" "Yes, two cups please."
    hide chelsea with dissolve
    "She holds up two fingers for emphasis. You nod, making your way over to the thermos to fill two foam cups up."
    "You slap some stickers on the side with the little logo you made for Dorothy and pass them back to her."
    show chelsea laugh with dissolve
    pcname "Here you go! I hope you enjoy."
    show chelsea embarrassed
    "Bertha's Granddaughter" "Thanks! I'm sure we will."
    hide GCGirl with dissolve
    pause 1.0
    show chelsea blank
    "You watch as she slips back through the crowd, ducking through the bundled up figures until she disappears entirely in the sea of coats and scarves."
    scene black with fade
    "As you serve up the next group of customers, the granddaughter's presence completely slips from your mind."
    "You fall into a sort of repetitive cycle for the next hour: greeting guests, ringing up drinks, and filling up the cups with steamy cider before passing them off."
    "You hardly even sell the actual apples for the day, instead finding yourself preoccupied with the apple cider."
    "Unfortunately, the thermos containers run out before your customers do, and near the end of the farmer's market you find yourself having to turn customers away."
    scene bg FarmersMarket with fade
    "Once the crowd slows down and news of the apple cider shortage has spread, Dorothy heaves a sigh and collapses back into her chair."
    show GOLady1 at left with dissolve
    "Dorothy" "I've never seen the market that busy before. It was a madhouse!"
    show chelsea sad with dissolve
    pcname "Tell me about it. My feet are aching..."
    show chelsea embarrassed
    "But you can't help feeling a little satisfied by your diligent work. Thanks to you, Dorothy's booth was a huge hit, and you even managed to sell out of the cider completely!"
    show chelsea blank
    "Dorothy" "Don't complain about aching feet until you're my age."
    hide GOLady1 with dissolve
    "Dorothy stretches in her chair. You're reminded of a tired, lazy cat basking in the sun. There is a look of deep satisfaction on her face, as though she's just caught her biggest prey yet."
    "Then she looks at Bertha's booth."



    show GOLady1:
        ypos 5.0
        linear 0.5 ypos 0.0
    pause 0.5
    show chelsea confused
    "Dorothy sits up at once, nearly falling out of the chair as she does so. Her hands grip the seat's arms, the fabric twisting under her palms."
    show chelsea shocked
    "Dorothy" "Why do {i}they{/i} have my cider?!"
    show chelsea blank
    "You glance back at Bertha's booth; it's hardly been touched today, still packed with bananas and related desserts. Bertha and her granddaughter huddle together and converse, cupping the two foam cups of apple cider between them."
    show chelsea blank
    "Dorothy whips her attention back to you with an accusatory glare."
    "Dorothy" "Did you serve either of them?"
    show chelsea shocked
    pcname "You didn't say we couldn't sell to them."
    "Dorothy" "Because that should have been obvious!"
    show chelsea angry
    pcname "How come? It's cold out; they just wanted some cider. Besides, it adds to our sales."
    show chelsea blank
    "Dorothy shakes her head, as if the movement can wipe away the sight of her enemy sharing cider with her granddaughter."
    "Dorothy" "You don't think about things in the long run, girl! You practically gave them the recipe. They'll find a way to use it, I know they will."
    show chelsea confused
    pcname "That seems a little far fetched, don't you think?"
    show chelsea blank
    pcname "They only serve banana-related products. It's not like they're going to make banana cider or something."
    "Dorothy's lips purse together into a tiny pucker on her face. She stares back at Bertha's booth, distrustful."
    "Dorothy" "Maybe, maybe not. It may not be cider, but it'll get those wheels turning in her head. I'm telling you now, we shouldn't have sold her that cider."
    show chelsea confused
    "You struggle not to roll your eyes. You feel as though she's taking this entire thing out of proportion."
    show chelsea blank
    "So what if Bertha and her granddaughter had some apple cider? Surely they would have figured out a way to sell something warm when it got cold out anyways."
    "Dorothy is giving them too much credit."
    hide GOLady1 with dissolve
    "Dorothy clicks her tongue but moves to the register to start an early count of their sales."
    show chelsea laugh
    "As you start to clean up, a customer quickly rushes to your booth, his face purple with anger."
    show GHCMan at right with dissolve
    pause 1.0
    show chelsea sad
    pause 1.0
    show chelsea laugh
    "You feel your smile falter at his approach."
    pcname "Hello sir, how may I--"
    show chelsea shocked
    "He slams four foam cups onto the booth, his fist carrying most of the weight. You jump, glancing back at the crate to see if the leg fell. It doesn't."
    "Angry Customer" "I want a refund!"
    pcname "I'm sorry?"
    show chelsea sad
    "Angry Customer" "You heard me! I want a refund! {i}Now!{/i}"
    pcname "I-I don't..."
    show chelsea shocked
    show GOLady1 at center, moveSprite(0.75, 0.75, 0.0) with dissolve
    "Dorothy" "What seems to be the problem here, sir?"
    "Dorothy steps up behind you, the picturesque version of a warm, happy grandmother."
    show chelsea sad
    "However, you've been with her long enough to know now that there is an iciness behind the sweet mask, a sort of coldness in her gaze that sends chills down your spine."
    "The customer doesn't see it at all."
    show chelsea shocked
    "Angry Customer" "I'll tell you what the problem is; you're taking advantage of our poor community, and I won't have it!"
    show chelsea sad
    "A spike of fear runs through you. Does he know about the faulty leg on the table? Who told him, or was he himself a victim?"
    if applescam == True:
        "You try to recall all the poor saps you and Dorothy fooled, but the list is so long that you can't even remember properly. Your mind draws a blank."
    elif True:
        "You try to recall all the poor people Dorothy had fooled, but the list is so long that you can't even remember properly. Some of them were even too painful to watch."
        "If this man was someone she scammed, you have no recollection of him."
    show chelsea blank
    "While you inwardly panic at the brewing conflict, Dorothy handles him with ease, feigning confusion and cocking her head to the side for effect."
    "Dorothy" "I'm not sure I know what you mean, sir. Could you explain to me what you're talking about?"
    "You'll give her this; she's a good actress. Even you feel inclined to believe her innocence as she addresses the man in front of her with a sweet, grandmotherly attitude."
    show chelsea confused
    "Being old has it's advantages, you suppose. Who would think an elderly old granny is capable of malice?"
    show chelsea blank
    "The angry man falters, and you detect a hint of shame on his face as he reconsiders his position. You almost wonder if he'll leave, but it seems pride wins, forcing him to straighten up and address Dorothy with unjustified confidence."
    show chelsea confused
    "Angry Customer" "I've heard that there's something in this cider that's making kids sick. Now I want a refund or I'll need to speak to whoever's in charge here!"
    show chelsea blank
    "Dorothy" "Sick?"
    "You notice her gaze cut back to Bertha's booth, but she continues speaking."
    "Dorothy" "{i}I{/i} haven't heard of anyone getting sick from my cider. In fact, I've been drinking it all day, and I've been fine."
    "Dorothy" "My granddaughter here has been doing the same thing, haven't you, [pcname]?"
    show chelsea embarrassed
    "You quickly nod along, eager for this man to leave so you can go home. Running the market stall is hard enough work on top of everything else you have going on; you just want to curl up in front of your TV and stream something."
    show chelsea blank
    "Angry Customer" "And you think I ought to believe you, the ladies that run this booth? Of course you'll defend your own product!"
    "Angry Customer" "Now listen here, just give me the refund so I can leave."
    "Dorothy" "I'm afraid I can't do that, sir. You've already finished off all of the cider."
    show chelsea shocked
    "Angry Customer" "This is bullshit! I paid good money for this, and now that people are getting sick, you won't own up to your mistakes?!"
    show chelsea blank
    "Dorothy" "If you felt so sick, why did you keep drinking it?"
    "Angry Customer" "{i}I{/i} didn't, but that girl--"
    "Dorothy" "What girl?"
    "Angry Customer" "The one right over there! Look at her!"
    show chelsea shocked
    pause 1.0
    show chelsea sad
    "He waves an angry finger back at Bertha's booth where, sure enough, you can vaguely see her granddaughter lying down with a cloth to her head. Bright red bumps cover her body and you realize with sickening dread that they're hives."
    "Dorothy notices as well, her eyes narrowing to slits."
    show chelsea blank
    "Angry Customer" "If that's what your cider does to customers, then I want a refund! You're lucky I don't sue!"
    "Angry Customer" "If my daughters end up like that, I just might!"
    show chelsea shocked
    "Dorothy drops her grandmotherly act at once, the innocence melting from her face like ice cream on a summer day."
    show chelsea blank
    "Dorothy" "Have your daughters shown any symptoms?"
    "Angry Customer" "Er, no--"
    "Dorothy" "Then how can you be sure these claims are true?"
    "The man says nothing."
    "Dorothy" "Young man-- if I can still call you that at this age-- you have come here to accuse me of, what? {i}Poisoning{/i} my {i}own{/i} cider? Is that what that girl told you?"
    "Angry Customer" "She didn't say {i}poisoned{/i}, but..."
    "Dorothy" "What that young girl over there is displaying is clearly an allergic reaction. Now, to {i}what{/i} I don't know, but that isn't a problem with the cider so much as the person drinking it."
    show chelsea sad
    "Angry Customer" "You're going to blame that poor girl for having a reaction to something {i}you{/i} made?!"
    show chelsea shocked
    "Dorothy" "If she's foolish enough to drink apple cider knowing full well she's allergic to something in it, then yes, I will."
    show chelsea blank
    "Dorothy" "Now, is there a problem with {i}your{/i} girls? Because if not, I have no refunds to give out."
    "Angry Customer" "I-- No, but--"
    show chelsea sad
    "Dorothy" "Sir, if you don't leave my booth at once I will {i}have{/i} to get the police involved. You are scaring my poor granddaughter and, quite frankly, I do not feel safe around you."
    "You don't feel very scared, but you certainly find yourself keeping your distance from their argument."
    show chelsea blank
    "Dorothy doesn't look frightened either-- if anything, you suspect {i}she{/i} might be the one to attack him, but the man's gaze flickers over both of you and a shameful blush reaches his face."
    "Angry Customer" "...Right. Have a nice day, ma'am."
    hide GHCMan with dissolve
    show chelsea confused
    "He turns around and walks away, his movements stiff and awkward. You aren't sure whether you should feel impressed or embarrassed by Dorothy's guilt-tripping."
    show chelsea shocked
    "Dorothy clenches her fists at her side, face red with rage. It's the angriest you've ever seen the old woman."
    show chelsea shocked
    pcname "Dorothy...?"
    hide GOLady1 with dissolve
    pause 1.0
    show chelsea sad
    "Before you can convince her otherwise, she marches toward Bertha's booth."
    "Nothing good can come from this."
    show chelsea shocked
    pcname "I-- Dorothy, wait!"
    scene black with fade
    "Locking the cash box in her car, you rush after her, careful not to push anyone out of the way as you try to catch up."
    pcname "Dorothy! Dorothy!"
    "The old woman doesn't turn around, not even so much as acknowledging you're there as she storms over to her enemy's booth."
    scene bg FarmersMarket with fade
    "Once you're close enough, you can hear Bertha relaying a sympathetic sob story to one of her customers, her own granddaughter still laying behind her on the ground."
    show GOLady2 at right with dissolve
    "Bertha" "It's awful I tell you. There were no signs saying what was in it, and my poor baby girl just starts coughin' and wheezin' and now the poor thing is trying to rest it off."
    "Bertha's Customer" "That's awful! I'm so sorry to hear that. Is there anything I can do?"
    "Bertha" "No, no, she just needs rest is all. She already took some medicine."
    "Bertha" "I just say, you ought to avoid that apple booth over there. That woman is careless with a capital C-- Oh, speak of the devil and he shall appear."
    show GOLady1 as GOLady12 with dissolve
    "Bertha's eyes lock onto Dorothy's and you can practically hear the crackle of electricity in the air between them."
    show chelsea sad at left, enterScene(-0.2, 0.2, 0.7, 0.6)
    "Dorothy stops in front of Bertha's booth, earning a harsh glare from the customer beside her. You stumble in late, wary to intervene."
    "Bertha" "What's wrong, Dorothy? You came here to finish the job?"
    show chelsea blank
    "Bertha gestures toward her sick granddaughter, making her voice loud enough for anyone standing nearby to hear."
    "Bertha" "Poor thing ain't doing well as it is after trying that sorry excuse of an apple cider. Haven't you done enough?"
    show chelsea sad
    "A few glances and glares are tossed your way, and you suspect that this woman and the angry man from before are not the only customers she's told this to."
    show chelsea blank
    "Bertha" "I know we're competitors and all, but this is over the line, even for you, Dorothy."
    "Dorothy" "The fact you would use your own granddaughter as a sort of bait is {i}sickening{/i}, Bertha."
    "Bertha" "I would never! How dare you accuse me of such things, that is my {i}granddaughter{/i}!"
    show chelsea shocked
    "Dorothy" "I know who the bitch is! This isn't the first time I've met her."
    pause 1.0
    show chelsea blank
    "There are audible gasps around her, but Dorothy doesn't seem to care. You hang back and watch, unsure of whether to intervene or not."
    "Dorothy" "I know that she's just as much of a conniving snake as you are. Maybe even more, if she's willing to risk her own health for some pathetic has-been banana stand."
    show GOLady2 at moveSprite(1.0, 0.8, 0.2)
    "Bertha leans forward, teeth clenched as she hisses in Dorothy's face."
    show chelsea sad
    "Bertha" "Take it back, you raggedy old cow."
    "Dorothy" "Make me, you overgrown whale."
    "There's a stillness in the air as the old women glare at each other head on."
    scene black with fade
    "Then all hell breaks loose."
    scene black with dissolve
    "You aren't sure who threw the first punch, but suddenly fists are flying, and Dorothy and Bertha are swinging their old arms in the air and bruising each other's faces."
    "Dorothy moves with surprising agility as she jumps over the booth, knocking down several displays in her haste to land the next punch."
    "But Bertha carries more weight and manages to knock Dorothy away. Dorothy stumbles but catches herself on the side of the booth."
    "You see her move forward, ready to strike again, but she notices the precarious placement of the booth's awning structure and shoves the pillar out of the way."
    "Bertha reaches for it, desperate to cover her scheme, but it's too late."
    "Bertha" "No!"
    scene black with dissolve
    "The banana booth comes tumbling down, raining potassium across the parking lot."
    "Dorothy spits on the produce."
    "Dorothy" "Serves you right, you old goat! You didn't even have any safety measures in place! You can't run a trick beam in these conditions!"
    "Customer" "Trick beam...?"
    "One of the passing customers nearby slows down, raising an eyebrow at the stand. A few others slow down as well, and you recognize a couple in the crowd as even victims to Bertha's scheme."
    "Customer 2" "Did she say trick beam...?"
    "Customer 3" "That's what I heard."
    "Customer 1" "You mean she's been scamming people this whole time?!"
    "Customer 3" "That's what it sounds like."
    "Customer 4" "I just paid her for damages last week!"
    scene black with dissolve
    "The crowd builds around the two old ladies, but neither Dorothy nor Bertha seem to notice the growing mob around them. They're too busy throwing fists and hits and kicks-- anything that lands."
    "Bertha towers over Dorothy and nearly steps on her own granddaughter in her attempt to yank the old woman back."
    "Dorothy is faster-- she moves with a swiftness that you hadn't even thought possible at that age. She dives out from behind the booth and makes a run for her own booth."
    scene black with dissolve
    "Bertha pursues her, yelling a string of insults and curses during her chase."
    "The crowd follows, both infuriated and fascinated by the spectacle. You almost want to take your phone out and record the scene yourself."
    "Customer 2" "Hey Deb, isn't that the booth you had to pay damages for?"
    "Deb" "The banana one?"
    "Customer 2" "No, no, the apple one."
    "Deb" "Yeah... Yeah it is, actually!"
    "You can sense a dangerous turning point in the crowd as they begin piecing the scam together."
    "You never expected it to come tumbling down like this, but you can't say you're surprised that it finally caught up to them."
    scene black with dissolve
    "Dorothy dives behind her booth and searches for something in the backseat of her car."
    "She doesn't get very far; Bertha grabs her by the leg and drags her out of the backseat."
    "Dorothy kicks at her. She lands a hit on Bertha's chin and the old woman howls in pain, throwing her head back--"
    scene black with dissolve
    "--Far enough for her wig to fall off."
    "More gasps echo across the crowd, including your own."
    "Bertha briefly acknowledges the crowd-- acknowledges the shame and embarrassment of her situation-- but she's in too deep now."
    "With an angry yell, Bertha tackles Dorothy to the ground."
    menu farmersmarketparticipate:
        "Film the scene and sell it to news stations." if True:
            "There's no way social media wouldn't eat this up, and news stations would definitely pay money for local footage like this!"
            scene black with dissolve
            "Pulling out your phone, you immediately start recording the remains of the fight."
            "Bertha pins Dorothy to the ground, hands around her neck. Dorothy struggles for a moment, then kicks the larger woman square in the crotch."
            "You wince as Bertha wails, her grip slipping. Dorothy squeezes out from underneath Bertha in time to climb atop her booth's tabletop."
            scene black with dissolve
            "The table wiggles and you glimpse at the crate-- it's out of position."
            "Oh no."
            pcname "Dorothy--"
            "Dorothy" "This is for Frank, you heartless man-stealing {i}bitch!{/i}"
            "Dorothy preps her jump."
            scene black with dissolve
            "The table crashes underneath her."
            "She falls backward onto the display, her apples rolling out into the parking lot. You can hear the sounds of customers realizing the scam in place, but you're too focused on Dorothy and Bertha's fight to care."
            "Both old ladies moan, their age finally catching up to them as they try and fail to stand back up."
            "You stand, shocked, your phone still recording as the women moan and groan through the pain."
            "Sirens sound off nearby, soon followed by police. Apparently someone had called them as soon as the fight began."
            scene black with fade
            "Two uniformed policemen walk in and address the situation while a few other uniformed women direct the crowd away."
            "You turn off your recording and leave, positive that you won't be seeing Bertha {i}or{/i} Dorothy at the farmer's market any longer."
            "As you walk out, you manage to contact one of the local news stations and sell the fight you recorded for their story tonight."
            if applescam == True:
                "You may not be able to make money off of the scam anymore, but at least you're getting paid for the video!"
            elif True:
                "It's a good thing you didn't participate in the scam; and at least you get paid a good chunk from the video!"
            $ Cash += 300
        "Try to break up the fight." if True:
            "As you hear sirens sounding in the distance, you know this can only end badly."
            scene black with dissolve
            "You hurry into the booth and try to put yourself between them."
            "Bertha has Dorothy pinned to the ground, but before she can do anything, you pull the old woman off."
            "Bertha reels on you, furious."
            pcname "You both need to stop--"
            scene black with dissolve
            "Bertha doesn't care; she hits you in the jaw, her impact surprisingly painful. You gasp in pain and clutch your face."
            "Dorothy" "Don't hit her, you bitch!"
            scene black with dissolve
            "Somehow, Dorothy managed to crawl out from underneath Bertha and stand atop the tabletop of her own booth."
            pcname "Seriously, you both need to stop. The police are coming--"
            "But neither of them listen to you. Dorothy holds herself tall, ignoring the purple bruises forming across her wrinkled skin."
            "Dorothy" "This is for Frank, you heartless man-stealing {i}bitch!{/i}"
            "Dorothy preps her jump onto Bertha. In that split second, you notice the crate moved out of the way and the bum leg giving out."
            "It's a second too late."
            scene black with dissolve
            pcname "Dorothy--!"
            "The table crashes underneath her."
            "She falls backward onto the display, her apples rolling out into the parking lot. You can hear the sounds of customers realizing the scam in place, but you're too focused on Dorothy and Bertha's fight to care."
            "Both old ladies moan, their age finally catching up to them as they try and fail to stand back up."
            "Bertha harumphs in triumph, but as she tries to move forward, one of the fallen apples slides under her foot and sends her flat on her back."
            scene black with fade
            "Both of the old women are groaning in pain when two uniformed policemen walk in and address the situation while a few other uniformed women direct the crowd away."
            "Once the older women are taken care of, one of the policemen walks up to you and requests your variation of the story."
            "It takes all of an hour between each of you telling your stories, an ambulance driving both Bertha and Dorothy to the hospital, and the head of the farmer's market to arrive and officially declare the elderly women banned from any future events."
            "Once everything is settled, you're free to go home. You leave, exhausted by the day's events."
            "You're positive that you won't be seeing Bertha {i}or{/i} Dorothy any longer."
    jump events_end_period
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
