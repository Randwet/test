label VioletText_FacialRec:
    call screen TextingScene("Violet",
    [
        TextMessage("Hey Violet, what kind of moisturizer do you use?", sender = False),
        TextMessage("I'm trying to find something that won't make my skin too oily.", sender = False),
        TextMessage("I use Verbana Lake by Victoria Russo."),
        TextMessage("Here's a link."),
        TextMessage("https:\\\\www.victorialuxury.com\\verbana-collec..."),
        TextMessage("The one in peach smells great."),
        TextMessage("That's over $100?!", sender = False),
        TextMessage("Yeah, it's on sale right now. Usually it's around $250."),
        TextMessage("I was looking for something more in the $20-40 range...", sender = False),
        TextMessage("Do they even sell moisturizer that cheap?"),
        TextMessage("You don't want to be stingy with moisturizer. Cheap stuff will only ruin your skin."),
        TextMessage("Yeah, I guess", sender = False),
    ])

    jump textevent_end

label VioletText_Prague:
    call screen TextingScene("Violet",
    [
        TextMessage("Hey Vi, wanna hang out this weekend?", sender = False),
        TextMessage("We could go to Glamour and try out the new makeup there.", sender = False),
        TextMessage("You know I want to! The new collection just came out, too."),
        TextMessage("But I can't. My dad's having a dinner party with the minister of Prague."),
        TextMessage("I'll be out of the country until tomorrow."),
        TextMessage("Out of the country??", sender = False),
        TextMessage("Well yeah, it's not like the minister is going to come here."),
        TextMessage("Anyway, I'll fill you in on the gossip later, but the minister's daughters are total attention whores."),
        TextMessage("They're always causing a scene. I wonder what they'll do tonight."),
        TextMessage("Last time we visited they were blackmailing the minister's new wife."),
        TextMessage("omg", sender = False),
        TextMessage("LOL right?"),
        TextMessage("Well, have fun, I guess?", sender = False),
        TextMessage("As much fun as I usually do."),
    ])

    jump textevent_end





label VioletText_LookBetterDom:
    call screen TextingScene("Violet", [TextMessage("Do you think I would look better in a skirt or leggings?")])

    menu violet_SkirtLeggings:
        "A skirt." if True:
            call screen TextingScene("Violet", [TextMessage("I really like seeing you in a skirt.", sender = False)])

            if club == "track":
                call screen TextingScene("Violet", [TextMessage("It's easier to eat you out that way.", sender = False)])
            elif club == "cheer":
                call screen TextingScene("Violet", [TextMessage("It's easier to pleasure you that way. ;)", sender = False)])
            elif club == "yearbook":
                call screen TextingScene("Violet", [TextMessage("It's easier to kiss your thighs... and everything else...", sender = False)])

            call screen TextingScene("Violet",
            [
                TextMessage("Easy? I don't want to make things easy on you."),
                TextMessage("But if you can convince me, maybe I'll wear a special skirt just for you."),
            ])

            if club == "track":
                call screen TextingScene("Violet", [TextMessage("Your bare thighs look really hot in a skirt. I just want to grab and squeeze them around my head.", sender = False)])
            elif club == "cheer":
                call screen TextingScene("Violet", [TextMessage("I love seeing your bare legs, Vi. I just want to get down and lick them from the ankle up~", sender = False)])
            elif club == "yearbook":
                call screen TextingScene("Violet", [TextMessage("I really like looking at your bare legs... I just want to reach down and touch myself looking at your thighs...", sender = False)])

            call screen TextingScene("Violet",
            [
                TextMessage("Hm. My legs do look great in skirts, don't they?"),
                TextMessage("Alright. I'll wear one tomorrow, but you aren't allowed to touch my legs at all."),
                TextMessage("Thanks for the help~ <3"),
            ])
        "Leggings." if True:

            call screen TextingScene("Violet", [TextMessage("You look amazing in leggings, Vi.", sender = False)])

            if club == "track":
                call screen TextingScene("Violet", [TextMessage("It's easier to rub you off without anything in my way.", sender = False)])
            elif club == "cheer":
                call screen TextingScene("Violet", [TextMessage("It's easier to stare at your ass that way. ;)", sender = False)])
            elif club == "yearbook":
                call screen TextingScene("Violet", [TextMessage("It's easier to grind on you without anything in the way...", sender = False)])

            call screen TextingScene("Violet",
            [
                TextMessage("Easy? I don't want to make things easy on you."),
                TextMessage("But if you can convince me, maybe I'll wear some extra tight leggings just for you."),
            ])

            if club == "track":
                call screen TextingScene("Violet", [TextMessage("Seriously Vi, your legs so fucking hot in leggings. I want you to bury my face between your thighs in them.", sender = False)])
            elif club == "cheer":
                call screen TextingScene("Violet", [TextMessage("You have no idea how wet you in leggings makes me, Vi. I want to lick your pussy through the fabric just to touch you. <3", sender = False)])
            elif club == "yearbook":
                call screen TextingScene("Violet", [TextMessage("You look so good in leggings, Vi... I think you underestimate how wet I am thinking about it...", sender = False)])

            call screen TextingScene("Violet",
            [
                TextMessage("Hm. My legs do look great in leggings, don't they?"),
                TextMessage("Alright. I'll wear some tomorrow, but you aren't allowed to touch my legs at all."),
                TextMessage("Thanks for the help~ <3"),
            ])

    jump textevent_end

label VioletText_Bitch:
    call screen TextingScene("Violet",
    [
        TextMessage("I saw a puppy today that reminded me of you.", sender = False),
        TextMessage("Excuse me?"),
        TextMessage("It had the softest fur and prettiest eyes. <3", sender = False),
        TextMessage("I thought you were about to call me a bitch and I was ready to end you."),
        TextMessage("I'm still not sure I shouldn't."),
        TextMessage("omg no I didn't mean it like that!", sender = False),
        TextMessage("It just looked super pretty and reminded me of you.", sender = False),
        TextMessage("It had shiny black fur and its eyes were so cute.", sender = False),
        TextMessage("And the collar was purple and sparkly and had little gemstones all over it <3", sender = False),
        TextMessage("A collar? That sounds more like you, [pcname]."),
        TextMessage("Since you like bitches so much, I should make you wear one."),
        TextMessage("I seriously wasn't trying to call you a bitch, I'm sorry.", sender = False),
        TextMessage("Too late."),
        TextMessage("You better be ready to make it up to me later."),
        TextMessage("Yes, Violet.", sender = False),
    ])

    jump textevent_end


label VioletText_BubbleBath:
    call screen TextingScene("Violet",
    [
        TextMessage("Hey, Vi.", sender = False),
        TextMessage("What's up?", sender = False),
        TextMessage("Washing up."),
        TextMessage("Tell me, [pcname], do you like bubble baths?"),
    ])

    menu Violet_Bath:
        "Yeah, I love bubble baths." if True:
            call screen TextingScene("Violet",
            [
                TextMessage("Yeah, I love bubble baths.", sender = False),
                TextMessage("How come?", sender = False),
                TextMessage("Then you'll enjoy this."),
                TextMessage("VBS", image = True),
                TextMessage("Do you like it?"),
                TextMessage("Yes, definitely!", sender = False),
            ])

            if club == "track":
                call screen TextingScene("Violet", [TextMessage("Fuck, you look so hot, Vi.", sender = False)])
            elif club == "cheer":
                call screen TextingScene("Violet", [TextMessage("I wish I was in the bath with you~ ;)", sender = False)])
            elif club == "yearbook":
                call screen TextingScene("Violet", [TextMessage("You look so pretty...", sender = False)])

            call screen TextingScene("Violet",
            [
                TextMessage("I thought you would appreciate it"),
                TextMessage("Since you're feeling so good about it, go masturbate for one minute exactly to this picture."),
                TextMessage("I don't care where you are. Go do it."),
                TextMessage("And text me when you're done."),
                TextMessage("Yes, Vi.", sender = False),
            ])
        "I'm not really into baths." if True:

            call screen TextingScene("Violet",
            [
                TextMessage("They're not really my thing. Showering is easier.", sender = False),
                TextMessage("Why? What's up?", sender = False),
                TextMessage("Hm. I was going to reward you with a picture of me in the bath, but maybe not."),
                TextMessage("Since you're not into baths and everything."),
                TextMessage("I can be into baths if it's you in one!", sender = False),
                TextMessage("I don't know. What would I get out of it?"),
                TextMessage("Oh, actually, I have an idea."),
                TextMessage("Here you go."),
                TextMessage("VBS", image = True),
                TextMessage("Do you like it?"),
                TextMessage("Yes, definitely!", sender = False),
            ])

            if club == "track":
                call screen TextingScene("Violet", [TextMessage("Fuck, you look so hot, Vi.", sender = False)])
            elif club == "cheer":
                call screen TextingScene("Violet", [TextMessage("I think I might start to like baths now~ ;)", sender = False)])
            elif club == "yearbook":
                call screen TextingScene("Violet", [TextMessage("You look so pretty...", sender = False)])

            call screen TextingScene("Violet",
            [
                TextMessage("I thought you would appreciate it"),
                TextMessage("Too bad you don't like baths, so you don't get to do anything with it."),
                TextMessage("I can't even use the picture for later?", sender = False),
                TextMessage("Nope."),
                TextMessage("But I'll keep the shower in mind for next time."),
                TextMessage("If you're being good, that is."),
            ])

    jump textevent_end

label VioletText_WouldYouRather:
    call screen TextingScene("Violet",
    [
        TextMessage("Hey Vi, you wanted me to text you?", sender = False),
        TextMessage("Yeah. We're going to play a game."),
        TextMessage("You know how would you rather works, right?"),
        TextMessage("Yeah...?", sender = False),
        TextMessage("Good. It would be pretty stupid if you didn't."),
        TextMessage("Here's how it's going to go: for every answer you give me that I like, I'll reward you."),
        TextMessage("Everything else, I'll punish you. Got it?"),
        TextMessage("Yeah, I understand.", sender = False),
        TextMessage("Good. Let's start."),
        TextMessage("Would you rather be handcuffed or blindfolded during sex?"),
    ])

    menu VioletWYR_Q1:
        "Handcuffed." if True:
            call screen TextingScene("Violet",
            [
                TextMessage("Handcuffed.", sender = False),
                TextMessage("Good girl."),
                TextMessage("You can start off by touching your nipples. Now."),
                TextMessage("Yes, Vi.", sender = False),
            ])
        "Blindfolded." if True:

            call screen TextingScene("Violet",
            [
                TextMessage("Blindfolded.", sender = False),
                TextMessage("Hm. That still gives you too much freedom to do what you want."),
                TextMessage("Go put on a porn video, put it on max volume, and pull up another tab."),
                TextMessage("You're not allowed to touch yourself or watch it, but you have to keep listening to it."),
            ])

    call screen TextingScene("Violet",
    [
        TextMessage("Next question."),
        TextMessage("Would you rather call out the wrong name in bed or have me call out the wrong name?"),
    ])

    menu VioletWYR_Q2:
        "I call out the wrong name." if True:
            call screen TextingScene("Violet",
            [
                TextMessage("I would rather be the one to do it.", sender = False),
                TextMessage("Ugh. Seriously?"),
                TextMessage("It would piss me off if you called me the wrong name."),
                TextMessage("Go write me a list of all the names you think you can call me during sex."),
                TextMessage("I'll spank you for each one I don't like."),
            ])
        "Violet calls out the wrong name." if True:

            call screen TextingScene("Violet",
            [
                TextMessage("I would rather you do it.", sender = False),
                TextMessage("Good answer."),
                TextMessage("I would be super pissed if you called me something else."),
                TextMessage("You can go rub your clit for thirty seconds."),
            ])

    call screen TextingScene("Violet",
    [
        TextMessage("Okay.", sender = False),
        TextMessage("Would you rather accidentally send a dirty text to your boss or your best friend?"),
    ])

    menu VioletWYR_Q3:
        "To my boss." if True:
            call screen TextingScene("Violet",
            [
                TextMessage("I'd rather text my boss...", sender = False),
                TextMessage("Are you serious? You wouldn't rather send me a dirty text by mistake?"),
                TextMessage("You would be my best friend?", sender = False),
                TextMessage("I thought that was obvious. DUH."),
                TextMessage("But since you like your boss so much, go text him something dirty."),
                TextMessage("Wait, Vi, are you serious?", sender = False),
                TextMessage("Did I stutter? Go text him. Send me a screenshot to show me you did, too."),
                TextMessage("What should I say?", sender = False),
                TextMessage("Figure it out yourself."),
                TextMessage("[Image here]", sender = False), 
                
                TextMessage("That's so boring."),
                TextMessage("I'll let it slide for now, but come up with something better next time."),
            ])
        "To my best friend." if True:

            call screen TextingScene("Violet",
            [
                TextMessage("To my best friend.", sender = False),
                TextMessage("And that's obviously me, right?"),
                TextMessage("Yeah, of course.", sender = False),
                TextMessage("Hm, I like it, but you aren't losing much."),
                TextMessage("I'd rather you were sending me dirty texts than anyone else, though."),
                TextMessage("Alright. Go touch yourself until you cum."),
            ])

    call screen TextingScene("Violet",
    [
        TextMessage("This was more fun than I thought."),
        TextMessage("I'll think of some better questions to ask you next time."),
        TextMessage("I look forward to what you pick next time."),
    ])

    jump textevent_end



label VioletText_PublicMasturbation:
    call screen TextingScene("Violet",
    [
        TextMessage("Where are you right now?", sender = False),
        TextMessage("I'm at a restaurant with my parents."),
        TextMessage("Are you sitting beside one of them?", sender = False),
        TextMessage("No."),
        TextMessage("Good. Reach down and start masturbating under the table.", sender = False),
        TextMessage("With my parents here??"),
        TextMessage("Did I stutter?", sender = False),
        TextMessage("No..."),
        TextMessage("Are you touching yourself?", sender = False),
        TextMessage("Yes."),
        TextMessage("Good. Put two fingers inside yourself. Masturbate for three minutes.", sender = False),
        TextMessage("You better cum, because you're not allowed to touch yourself for the rest of the day.", sender = False),
        TextMessage("Yes, [pcname]."),
        TextMessage("omg, my mom just asked if I'm sick. She said my face was all red."),
        TextMessage("Time's up.", sender = False),
        TextMessage("What did you tell her?", sender = False),
        TextMessage("I told her I'm fine, just overheating a little."),
        TextMessage("Brb, gotta clean up."),
        TextMessage("Clean up with your mouth. Lick your fingers clean.", sender = False),
        TextMessage("omg seriously? They're going to notice."),
        TextMessage("Then figure out something to tell them.", sender = False),
        TextMessage("Did you do it?", sender = False),
        TextMessage("Yeah..."),
        TextMessage("Good. Enjoy your meal. ;)", sender = False),
    ])

    jump textevent_end

label VioletText_BathroomPhoto:
    call screen TextingScene("Violet",
    [
        TextMessage("I'm horny. Are you home?", sender = False),
        TextMessage("Yeah, I'm just watching some videos."),
        TextMessage("Do you want me to come over?"),
        TextMessage("No.", sender = False),
        TextMessage("Go into your bathroom and strip down.", sender = False),
        TextMessage("I want you to sit on your sink and touch yourself.", sender = False),
        TextMessage("Then send me a photo of you doing it.", sender = False),
        TextMessage("What kind of angle do you want?"),
    ])

    if club == "track":
        call screen TextingScene("Violet", [TextMessage("I don't care as long as I see that dripping pussy.", sender = False)])
    elif club == "cheer":
        call screen TextingScene("Violet", [TextMessage("Let me see that wet little pussy~ ;)", sender = False)])
    elif club == "yearbook":
        call screen TextingScene("Violet", [TextMessage("Whatever you think is best.", sender = False)])
        call screen TextingScene("Violet", [TextMessage("But make sure it's good.", sender = False)])

    call screen TextingScene("Violet",
    [
        TextMessage("VSS", image = True),
        TextMessage("How does this look, [pcname]? Do you like it?"),
    ])

    menu violet_bathroomselfie:
        "This is perfect." if True:
            call screen TextingScene("Violet",
            [
                TextMessage("This is perfect. Exactly what I was looking for.", sender = False),
            ])
        "Could be better." if True:

            if club == "track":
                call screen TextingScene("Violet", [TextMessage("Is that supposed to get me off?", sender = False)])
            elif club == "cheer":
                call screen TextingScene("Violet", [TextMessage("Huh. I guess that's not your best angle. :/", sender = False)])
            elif club == "yearbook":
                call screen TextingScene("Violet", [TextMessage("I think it could be better...", sender = False)])
            call screen TextingScene("Violet",
            [
                TextMessage("Should I retake it?"),
                TextMessage("No, I'll make it work. I don't want it to go to waste.", sender = False),
            ])

    call screen TextingScene("Violet",
    [
        TextMessage("Am I good to stop now?"),
        TextMessage("I have a nail appointment I need to get to, so..."),
        TextMessage("Did I say you can stop?", sender = False),
        TextMessage("You're going to keep touching yourself for the next ten minutes.", sender = False),
        TextMessage("But I'll be late for my nails!"),
        TextMessage("Hmm, good point.", sender = False),
        TextMessage("Twenty minutes.", sender = False),
        TextMessage("If you stop a minute earlier, I'll be very. Very. upset.", sender = False),
        TextMessage("Next time, invite me to get my nails done, too.", sender = False),
    ])

    jump textevent_end


label VioletText_ButtplugShopping:
    call screen TextingScene("Violet",
    [
        TextMessage("Hey Vi. What are you up to right now?", sender = False),
        TextMessage("I'm about to go out shopping."),
        TextMessage("Can I get you anything?"),
        TextMessage("You can.", sender = False),
    ])

    if club == "track":
        call screen TextingScene("Violet", [TextMessage("There's a new signed jersey for Addam Rhiork. Grab it for me.", sender = False)])
    elif club == "cheer":
        call screen TextingScene("Violet", [TextMessage("There's a limited edition makeup pallet at Glamour from StarrySkyCo. Pick it up for me.", sender = False)])
    elif club == "yearbook":
        call screen TextingScene("Violet", [TextMessage("There's a new book out that I want...", sender = False)])
        call screen TextingScene("Violet", [TextMessage("It's called Beneath the Night by Christina Pellenki.", sender = False)])

    call screen TextingScene("Violet",
    [
        TextMessage("I can do that."),
        TextMessage("Anything else?"),
        TextMessage("Yeah. Before you go, look through your drawers and find a buttplug.", sender = False),
        TextMessage("I want you to wear that the entire time you're out.", sender = False),
        TextMessage("I don't have one to wear right now, though..."),
        TextMessage("Then when you go out, buy one, and shove it in after you purchase it.", sender = False),
        TextMessage("I'm going out shopping with my dad! I can't buy that with him around."),
        TextMessage("Can't or won't?", sender = False),
        TextMessage("Are you telling me no, Violet?", sender = False),
        TextMessage("No, I'm not telling you no..."),
        TextMessage("Then what are you going to do?", sender = False),
        TextMessage("I'm going to buy a buttplug while I'm out and wear it around the mall as soon as I get it."),
        TextMessage("Good girl. You can leave my stuff in the mailbox when you're done shopping.", sender = False),
        TextMessage("I don't get to see you?"),
        TextMessage("Bad girls who argue don't get to see me, no.", sender = False),
        TextMessage("Text me when the stuff's here. And don't take out that buttplug until I tell you to.", sender = False),
        TextMessage("Okay, [pcname]. I won't."),
        TextMessage("Are you at the mall?", sender = False),
        TextMessage("Yeah, I'm looking at all the buttplugs now."),
        TextMessage("I split up with my dad for a bit, but I don't have a lot of time."),
        TextMessage("I want to pick what one you get. Describe them to me.", sender = False),
        TextMessage("There's a pink one with a fake diamond in it, a plain blue one, and a purple one with a tail at the end."),
        TextMessage("What one do you like?", sender = False),
        TextMessage("I like the pink one, but it's up to you."),
    ])

    menu VioletText_ButtplugChoice:
        "Pink with diamond." if True:
            call screen TextingScene("Violet",
            [
                TextMessage("Get the pink one with the diamond.", sender = False),
                TextMessage("That one suits you best, I think.", sender = False),
                TextMessage("Okay. Thanks, [pcname]!"),
            ])
        "Plain blue one." if True:
            call screen TextingScene("Violet",
            [
                TextMessage("Get the blue one.", sender = False),
                TextMessage("I'm not sure you deserve something as cute as the diamond right now", sender = False),
                TextMessage("Oh, okay..."),
            ])
        "Purple with tail." if True:
            call screen TextingScene("Violet",
            [
                TextMessage("Get the one with the tail.", sender = False),
                TextMessage("How am I supposed to hide the tail?!"),
                TextMessage("I don't know? Figure it out. That's your job.", sender = False),
                TextMessage("I want you to get the one with the tail. It's hot.", sender = False),
                TextMessage("If that's what you want..."),
            ])

    call screen TextingScene("Violet",
    [
        TextMessage("Now be a good girl and put it in.", sender = False),
        TextMessage("Heading to the bathroom now."),
        TextMessage("Just got it in. I have to wear this all day?"),
        TextMessage("wear it as long as I say so. I'll tell you when to stop.", sender = False),
        TextMessage("Okay."),
    ])

    jump textevent_end

label VioletText_PickyClothes:
    call screen TextingScene("Violet",
    [
        TextMessage("Hey Vi, did you pick out your clothes for tomorrow yet?", sender = False),
        TextMessage("Not yet. I haven't had a chance to."),
        TextMessage("Good. I'm going to pick them out.", sender = False),
        TextMessage("What do you have planned tomorrow?", sender = False),
        TextMessage("After school I'm going antiquing with my mom, and then my family's going yachting with some of my dad's business partners."),
        TextMessage("We're having a chef come aboard to make us fresh sushi from the ocean."),
        TextMessage("Wow. Okay.", sender = False),
        TextMessage("Let's make you wear...", sender = False),
    ])

    menu VioletText_ClothingChoice:
        "A dress." if True:
            call screen TextingScene("Violet",
            [
                TextMessage("You'll look really cute in a nautical dress.", sender = False),
                TextMessage("Do you have something like that?", sender = False),
                TextMessage("Yeah. I have some matching heels for it, too. Should I wear those?"),
                TextMessage("Definitely. You'll look really cute in that.", sender = False),
                TextMessage("Add some nautical jewelry to go with it, too.", sender = False),
                TextMessage("Okay. I'll do that. <3"),
            ])
        "Slacks and a blazer." if True:
            call screen TextingScene("Violet",
            [
                TextMessage("You're going to be doing a lot of walking tomorrow, so I want you in something comfortable.", sender = False),
                TextMessage("Wear a tight pair of slacks and a blazer.", sender = False),
                TextMessage("Do you have dressy shoes that won't hurt your feet?", sender = False),
                TextMessage("Yeah, I have a few pairs that would look nice."),
                TextMessage("Good. Wear one of those.", sender = False),
                TextMessage("Take lots of pictures of the water for me while you're out.", sender = False),
                TextMessage("I will! <3"),
            ])
        "An innertube and floaties." if True:
            call screen TextingScene("Violet",
            [
                TextMessage("I want you in an innertube and floaties.", sender = False),
                TextMessage("For the whole day.", sender = False),
                TextMessage("Are you being serious??"),
                TextMessage("These are important people to my dad. My parents will kill me if I embarrass them."),
                TextMessage("I thought I was the one in charge here?", sender = False),
                TextMessage("Innertube and floaties. I don't care what you wear under it, but if you keep it up, that'll be the only thing you're wearing.", sender = False),
                TextMessage("Understood?", sender = False),
                TextMessage("Yeah. I understand."),
                TextMessage("Good. Have a nice night, Vi.", sender = False),
                TextMessage("Enjoy your day out tomorrow. <3", sender = False),
            ])

    jump textevent_end


label VioletText_Busy:
    call screen TextingScene("Violet",
    [
        TextMessage("Hi, Violet", sender = False),
        TextMessage("What's up?", sender = False),
        TextMessage("Can't talk now, on a jet to Paris."),
        TextMessage("Text me later."),
    ])

    jump textevent_end

label VioletText_Busy2:
    $ violetbusy = renpy.random.randint(1,4)
    if violetbusy == 1:
        call screen TextingScene("Violet",
        [
            TextMessage("Hey Violet!", sender = False),
        ])
    if violetbusy == 2:
        call screen TextingScene("Violet",
        [
            TextMessage("What are you doing?", sender = False),
        ])
    if violetbusy == 3:
        call screen TextingScene("Violet",
        [
            TextMessage("Hey, you around?", sender = False),
        ])
    if violetbusy == 4:
        call screen TextingScene("Violet",
        [
            TextMessage("Hey Violet, how's it going?", sender = False),
        ])
    "You wait a few minutes for her to respond, but there is none."
    pcname "She must be busy."
    jump textevent_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
