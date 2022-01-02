label MattText_SayingHi:
    call screen TextingScene("Matt",
    [
        TextMessage("Hi, Matt.", sender = False),
        TextMessage("Who said you could text me?"),
        TextMessage("I have your number. Isn't that what it's there for?", sender = False),
        TextMessage("You craving my dick already? You're more of a slut than I thought."),
        TextMessage("I was just saying hi.", sender = False),
        TextMessage("You wouldn't be texting me if you were just saying hi."),
        TextMessage("Too bad I don't work on your schedule. I got shit to do."),
        TextMessage("Have fun getting off by yourself."),
    ])

    jump textevent_end

label MattText_Sociology:
    call screen TextingScene("Matt",
    [
        TextMessage("Hey Matt, did you finish the Sociology assignment yet?", sender = False),
        TextMessage("Matt? You there?", sender = False),
        TextMessage("Matt???", sender = False),
        TextMessage("What?"),
        TextMessage("Did you finish the assignment for Sociology?", sender = False),
        TextMessage("Hello??", sender = False),
        TextMessage("Yeah, I finished it."),
        TextMessage("What did you do yours on? I'm really stuck. I can't think of a topic.", sender = False),
        TextMessage("I did it on annoying whores that think I'm willing to waste my time talking about a shit assignment at school."),
        TextMessage("Did you even do the assignment?", sender = False),
        TextMessage("Someone else is working on that for me."),
        TextMessage("If you weren't such a dumb bimbo you'd think of getting someone else to do it, too."),
        TextMessage("You could get in serious trouble for that.", sender = False),
        TextMessage("You gonna snitch on me?"),
        TextMessage("That's what I thought."),
        TextMessage("Keep your mouth shut unless you're using it to suck me off."),
    ])

    jump textevent_end



label MattText_MaidPhoto:
    call screen TextingScene("Matt",
    [
        TextMessage("What's up?", sender = False),
        TextMessage("I'm feeling bored. Send something over."),
        TextMessage("Like what??", sender = False),
        TextMessage("Do I need to spell it out for you? A picture. Make it something good."),
        TextMessage("Okay, give me just a minute...", sender = False),
        TextMessage("Well? Don't keep me waiting, slut. Send it over."),
        TextMessage("ChelseaMaidSelfie", image = True, sender = False),
        TextMessage("What do you think?", sender = False),
        TextMessage("Hot. I can think of a few uses for that."),
        TextMessage("You just have that kind of shit lying around?"),
        TextMessage("It was a halloween costume one year. It's a little small on me now, but...", sender = False),
        TextMessage("Fuck, you're such a slut."),
        TextMessage("Next time I come over you better be wearing that."),
        TextMessage("I'll give you something to clean up. ;)"),
    ])

    if defymatt:
        if club == "track":
            call screen TextingScene("Matt", [TextMessage("Yeah, whatever.", sender = False)])
        elif club == "cheer":
            call screen TextingScene("Matt", [TextMessage("When don't you?", sender = False)])
        elif club == "yearbook":
            call screen TextingScene("Matt", [TextMessage("Okay... ///", sender = False)])
    elif True:
        if club == "track":
            call screen TextingScene("Matt", [TextMessage("Yeah, I'm sure you will ;)", sender = False)])
        elif club == "cheer":
            call screen TextingScene("Matt", [TextMessage("Yes, Matt~ ;)", sender = False)])
        elif club == "yearbook":
            call screen TextingScene("Matt", [TextMessage("Please do... ///", sender = False)])

    jump textevent_end

label MattText_MidnightMusic:
    call screen TextingScene("Matt",
    [
        TextMessage("Are you asleep?", sender = False),
        TextMessage("Matt?", sender = False),
        TextMessage("I fucking was until you started blowing up my phone."),
        TextMessage("What do you want?"),
        TextMessage("I couldn't sleep so I was watching some videos...", sender = False),
        TextMessage("I found this song I think you'd like. Here.", sender = False),
        TextMessage("https:\\\\www.mus3cally.com\\bitches-be-...", sender = False),
        TextMessage("Why the fuck are you sending me music in the middle of the night?"),
        TextMessage("This is the shit you woke me up for?"),
        TextMessage("Sorry. I didn't think your phone would wake you up...", sender = False),
        TextMessage("Well it did."),
    ])

    menu MattText_Music:
        "Did you like the song?" if True:
            call screen TextingScene("Matt",
            [
                TextMessage("Did you like the song at least?", sender = False),
                TextMessage("It's trash. They play this shit on the radio every day."),
                TextMessage("I've already heard it a million times by now."),
                TextMessage("Really? Oh. I hadn't heard it before.", sender = False),
                TextMessage("Of course you didn't. You live under a rock."),
                TextMessage("I'm going to bed. Don't text me again tonight."),
            ])
        "Goodnight, Matt." if True:

            call screen TextingScene("Matt",
            [
                TextMessage("Okay, sorry...", sender = False),
                TextMessage("I'll let you go back to sleep now. Night.", sender = False),
                TextMessage("If you're going to let me sleep then stop fucking texting me."),
                TextMessage("Don't make me regret giving you my number."),
            ])

    jump textevent_end

label MattText_20Questions:
    call screen TextingScene("Matt",
    [
        TextMessage("Hey Matt, wanna play a game?", sender = False),
        TextMessage("I'll think of a word and you have to guess what it is.", sender = False),
        TextMessage("You can ask me twenty yes or no questions, but that's it.", sender = False),
        TextMessage("Sure. I'll play."),
        TextMessage("Really??", sender = False),
        TextMessage("But you have to be the one guessing."),
        TextMessage("And if you guess wrong, I get to punish you for it later."),
        TextMessage("Got it?"),
    ])

    menu MattText_Game:
        "Sure, let's play!" if True:
            call screen TextingScene("Matt",
            [
                TextMessage("Yeah. Let's play.", sender = False),
                TextMessage("Good. Let's make it harder on you and cut it down to five questions."),
                TextMessage("How am I supposed to guess it in only five questions??", sender = False),
                TextMessage("Figure it out."),
                TextMessage("Go."),
                TextMessage("Okay, um...", sender = False),
                TextMessage("Is it a person?", sender = False),
                TextMessage("No"),
                TextMessage("Is an object?", sender = False),
                TextMessage("Yes"),
                TextMessage("Is it big?", sender = False),
                TextMessage("Yes"),
                TextMessage("Careful, [pcname]. You only have two questions left."),
                TextMessage("Hmm...", sender = False),
                TextMessage("So it's a big object... That can be anything.", sender = False),
                TextMessage("Time's ticking."),
                TextMessage("Okay, okay. Uh...", sender = False),
                TextMessage("Is it sexy?", sender = False),
                TextMessage("Definitely."),
                TextMessage("Okay. Can you insert it somewhere?", sender = False),
                TextMessage("Yes"),
                TextMessage("Time's up. What do you think it is?"),
            ])

            menu MattText_Game2:
                "Your dick" if True:
                    call screen TextingScene("Matt",
                    [
                        TextMessage("Is it your dick?", sender = False),
                        TextMessage("Nope. Wrong."),
                        TextMessage("What?? But it's obviously your dick.", sender = False),
                        TextMessage("Nope. It was a dildo."),
                        TextMessage("Looks like I get to punish someone later."),
                        TextMessage("You better look forward to it, slut."),
                        TextMessage("We should play this more often."),
                    ])

                    jump textevent_end
                "A dildo." if True:

                    call screen TextingScene("Matt",
                    [
                        TextMessage("Your dick would be too obvious.", sender = False),
                        TextMessage("Is it a dildo?", sender = False),
                        TextMessage("Damn. Yeah, it's a dildo."),
                        TextMessage("I made it easy for you, tho. You should thank me for not making it harder."),
                        TextMessage("Well?"),
                    ])

                    if defymatt:
                        call screen TextingScene("Matt", [TextMessage("You didn't go easy on me, you made it harder. And I still guessed it...", sender = False)])
                        call screen TextingScene("Matt", [TextMessage("This is the last time I play this crap with you. It was a dumb idea anyway.")])
                    elif True:
                        call screen TextingScene("Matt", [TextMessage("Thank you for going easy on me, Matt...", sender = False)])

                    jump textevent_end
        "I changed my mind." if True:

            call screen TextingScene("Matt",
            [
                TextMessage("Hm... Maybe not.", sender = False),
                TextMessage("I change my mind. I don't really feel like playing right now...", sender = False),
                TextMessage("Backing out already? You're such a weak little bitch."),
                TextMessage("Fine. No game, but maybe I'll punish you anyway for backing down on the offer."),
                TextMessage("See you around, slut."),
            ])

            jump textevent_end



label MattText_Busy:
    call screen TextingScene("Matt",
    [
        TextMessage("Hey, Matt.", sender = False),
        TextMessage("Matt.", sender = False),
        TextMessage("Hello?", sender = False),
    ])

    jump textevent_end

label MattText_Busy2:
    $ mattbusy = renpy.random.randint(1,4)
    if mattbusy == 1:
        call screen TextingScene("Matt",
        [
            TextMessage("Hey.", sender = False),
            TextMessage("What? I'm busy"),
            TextMessage("Oh I'll message you later then.", sender = False),
        ])
    if mattbusy == 2:
        call screen TextingScene("Matt",
        [
            TextMessage("What are you doing?", sender = False),
        ])
        "You wait a few minutes for him to respond, but there is none."
        pcname "He must be busy."
    if mattbusy == 3:
        call screen TextingScene("Matt",
        [
            TextMessage("Hey, you around?", sender = False),
            TextMessage("Running errands"),
            TextMessage("Ok", sender = False),
        ])
    if mattbusy == 4:
        call screen TextingScene("Matt",
        [
            TextMessage("Hey Matt, how's it going?", sender = False),
        ])
        "You wait a few minutes for him to respond, but there is none."
        pcname "He must be busy."
    jump textevent_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
