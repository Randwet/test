label DamienText_Dentist:
    call screen TextingScene("Damien",
    [
        TextMessage("Heyyyy", sender = False),
        TextMessage("How's it going?", sender = False),
        TextMessage("Could be better. Just left the dentist :("),
        TextMessage("Doesn't sound like you had fun. :P", sender = False),
        TextMessage("Does anyone ever have fun at the dentist? I want to meet these masochists."),
        TextMessage("Lmao xD Fair point.", sender = False),
        TextMessage("Did they find anything?", sender = False),
        TextMessage("Yeah, apparently I need to lay off the choco-puffs... They found like, 3 cavities."),
        TextMessage("Yikes!! Did you get them all taken care of?", sender = False),
        TextMessage("Yeah they just gave me the fillings then and there."),
        TextMessage("My jaw is seriously killing me. I can't feel my tongue but everything else is wearing off. T__T"),
        TextMessage("Ouch.", sender = False),
        TextMessage("DCCS", image = True),
        TextMessage("LOL", sender = False),
        TextMessage("That sucks, Damien. Feel better soon!", sender = False),
        TextMessage("I'll try. TT_TT"),
    ])

    jump textevent_end

label DamienText_Lunch:
    call screen TextingScene("Damien",
    [
        TextMessage("Hey Damien, watcha up to?", sender = False),
        TextMessage("Hey [pcname]!!"),
        TextMessage("Nm, I'm trying to decide on what to eat. I'm starving and the house is basically empty. T_T"),
        TextMessage("Maybe I'll just order something."),
        TextMessage("What do you think I should get, [pcname]?"),
    ])

    menu DamienLunch:
        "What should Damien eat?"
        "Tacos!" if True:

            call screen TextingScene("Damien",
            [
                TextMessage("There's a new taco place that opened up nearby.", sender = False),
                TextMessage("You could always try that.", sender = False),
                TextMessage("Oooh, tacos do sound really good right now..."),
                TextMessage("Alright, tacos it is! :D"),
                TextMessage("Thanks, [pcname]."),
                TextMessage("No problem.", sender = False),
            ])
        "Pizza!" if True:

            call screen TextingScene("Damien",
            [
                TextMessage("You can't really go wrong with pizza.", sender = False),
                TextMessage("That's true."),
                TextMessage("Yeah, I guess I'll just order that. Thanks, [pcname]! <3"),
                TextMessage("Sure thing. :)", sender = False),
            ])
        "Just Make Something." if True:

            call screen TextingScene("Damien",
            [
                TextMessage("You shouldn't waste your money ordering food.", sender = False),
                TextMessage("Just make something at home.", sender = False),
                TextMessage("Ehhh.... But that isn't as fun... :("),
                TextMessage("You're right tho... Alright, I'll just make something."),
                TextMessage("Thanks, [pcname]!"),
                TextMessage("Np :)", sender = False),
            ])

    jump textevent_end



label DamienText_FunFact:
    call screen TextingScene("Damien",
    [
        TextMessage("Fun Fact: Whale vomit is used in some perfumes.", sender = False),
        TextMessage("I can't tell if this is you asking me to buy you perfume or to avoid it at all costs. :P"),
        TextMessage("Is that actually a fun fact???"),
        TextMessage("No, not really.", sender = False),
        TextMessage("It ruined my day so I can't be the only one cursed with this information.", sender = False),
        TextMessage("Okay. Well since we're sharing facts..."),
        TextMessage("About 12,000 people die from falling down the stairs each year."),
        TextMessage("wHY WOULD YOU BURDEN ME WITH THIS INFORMATION", sender = False),
        TextMessage("Fun fact of the day. xD"),
        TextMessage("There is nothing fun about that!! Death is on my doorstep!", sender = False),
        TextMessage("I'm sorry, do you plan on yeeting yourself down the stairs anytime soon??"),
        TextMessage("Do I need to come over there and install a safety ramp or something? Lol"),
        TextMessage("No one PLANS on falling down the stairs!!", sender = False),
        TextMessage("How many of those falls do you think were actually accidents and the rest just a cover for murder?", sender = False),
        TextMessage("Fun Fact: Toddlers' teeth are behind their eyes.", sender = False),
        TextMessage("That is the creepiest thing you could have told me."),
        TextMessage("Where are you reading these from? and WHY? xD"),
        TextMessage("I was bored and found a clickbait article.", sender = False),
        TextMessage("And you couldn't watch cute animal videos like a normal person? xD"),
        TextMessage("Apparently not lol.", sender = False),
        TextMessage("Fun fact: you're more likely to get a virus from a religious site than a porn site."),
        TextMessage("The more you know~"),
        TextMessage("LOL, I'll keep that in mind.", sender = False),
        TextMessage(";)"),
    ])

    jump textevent_end

label DamienText_VideoGames:
    call screen TextingScene("Damien",
    [
        TextMessage("Hey Damien, you're pretty in-the-know about a lot of video games and stuff, right?", sender = False),
        TextMessage("Well I don't want to toot my own horn but... xD"),
        TextMessage("Why? What's up?"),
        TextMessage("I want to try to get into them more, but I don't know where to start.", sender = False),
        TextMessage("Help me out?", sender = False),
    ])

    if damienconfidence >= 50:
        call screen TextingScene("Damien", [TextMessage("Hell yeah, I can definitely help!!")])
    elif True:
        call screen TextingScene("Damien", [TextMessage("You want my help?? I guess I can try...")])

    call screen TextingScene("Damien", [TextMessage("What kind of genre of games are you interested in?")])

    menu DamienVGGenre:
        "What kind of video games are you interested in?"
        "Shooter." if True:

            call screen TextingScene("Damien",
            [
                TextMessage("I'm really interested in shooter games.", sender = False),
                TextMessage("I want to sneak around and hunt people down lol.", sender = False),
                TextMessage("Lol, that's a really popular genre. You're not alone."),
                TextMessage("I don't really play shooters myself, but my little brother loves them."),
                TextMessage("He plays a lot of Special Ops 2: Shots Fired."),
                TextMessage("Not really my thing, but he talks about it all the time, so you should give it a try. :)"),
                TextMessage("Thanks babe. I'll check it out then. :)", sender = False),
            ])
        "Simulation." if True:

            call screen TextingScene("Damien",
            [
                TextMessage("I've been looking into some simulation games lately...", sender = False),
                TextMessage("They seem really calm and relaxing, which is what I'm looking for.", sender = False),
                TextMessage("Oh yeah, I play some simulation games here and there."),
                TextMessage("I recommend trying out HouseMate if you're interested in controlling like, people and families and stuff."),
                TextMessage("I play a lot of Town Tycoon when I'm bored. xD I like building my own cities and stuff."),
                TextMessage("There's a ton of different simulation and tycoon games out there, but those two are my favorite."),
                TextMessage("Sweet, thanks babe. I'll give them a try. :)", sender = False),
                TextMessage("Let me know how you like them! :D"),
            ])
        "Role-playing." if True:

            call screen TextingScene("Damien",
            [
                TextMessage("I think I want to try a role-playing type game.", sender = False),
                TextMessage("It would be pretty fun to customize my character and play as someone else.", sender = False),
                TextMessage("Yessss omg they're so much fun!!!"),
                TextMessage("They're my favorite games. I have so many I could rec to you lol"),
                TextMessage("There's Royal Heart Online, Fighting Wars 4, Backblade: Realms of the Deep, Borderlust, Fusion Realms, Dragonscape, Infinite Theft, uhh..."),
                TextMessage("That's a lot...", sender = False),
                TextMessage("Haha, yeah, I guess I kind of went overboard... ^^;"),
                TextMessage("I suggest just looking through a few online and seeing what catches your eye."),
                TextMessage("If you end up with Backblade: Realms of the Deep, let me know! They have multiplayer so we can play together online. :)"),
                TextMessage("I'll look into it! It would be fun to play online with you. :)", sender = False),
                TextMessage("Definitely!! :D"),
            ])
        "Puzzle." if True:

            call screen TextingScene("Damien",
            [
                TextMessage("They're kind of old school, but I like puzzle games.", sender = False),
                TextMessage("They're pretty simple and look fun to solve.", sender = False),
                TextMessage("Oh yeah, my mom plays a lot of those on her phone."),
                TextMessage("She's been really into something called Numbered Tea Party lately."),
                TextMessage("I don't really know much about it, tho."),
                TextMessage("Lemme look it up", sender = False),
                TextMessage("...Your MOM has been playing this?", sender = False),
                TextMessage("Yeah, why?"),
                TextMessage("Uh... Maybe you should look it up yourself.", sender = False),
                TextMessage("..."),
                TextMessage("......"),
                TextMessage("........."),
                TextMessage("mOM WHAT THE FUCK--"),
                TextMessage("That's uh, not a lot of clothes. At all.", sender = False),
                TextMessage("I didn't know they let those kind of games in the app store tbh.", sender = False),
                TextMessage("Well thanks for the recommendation I guess lmao", sender = False),
                TextMessage("Uhhh you're welcome I think...?"),
            ])
        "Strategy." if True:

            call screen TextingScene("Damien",
            [
                TextMessage("I've been looking at a lot of strategy games lately.", sender = False),
                TextMessage("I want something that will distract me and make me think.", sender = False),
                TextMessage("Oh sweet! I love strategy games. I have so many on my console lol"),
                TextMessage("If you haven't already, check out Mutiny. I got it for my birthday last year and it's pretty addicting."),
                TextMessage("What's it about?", sender = False),
                TextMessage("You play as a cabin boy to a pirate ship and can either choose to join a mutiny of the captain or not."),
                TextMessage("All of your choices lead to whether you successfuly mutiny or prevent one from happening."),
                TextMessage("It takes a while to play, but it's a really great game if you have a lot of time to kill."),
                TextMessage("That sounds fun! I'll check it out then. :)", sender = False),
                TextMessage("Thanks babe!", sender = False),
                TextMessage("Yeah, no problem. :)"),
            ])

    jump textevent_end

label DamienText_TurtleVideo:
    call screen TextingScene("Damien",
    [
        TextMessage("https:\\\\www.cutevideos.org\\turt...", sender = False),
        TextMessage("Look at this video I found! Isn't it so cute?", sender = False),
        TextMessage("OMG. That turtle is adorable! TToTT"),
        TextMessage("Look at him trying to eat that strawberry!"),
        TextMessage("Right? He's so cute! I just want to pet his little shell ;n;", sender = False),
        TextMessage("Lol, same here"),
        TextMessage("Thanks for sending this. I was having a kind of crappy day before."),
        TextMessage("This seriously just made my day. <3"),
        TextMessage("Aw. Well I'm glad I can help <3", sender = False),
        TextMessage("You always do :)"),
    ])

    jump textevent_end


label DamienText_Busy:
    if club == "track":
        call screen TextingScene("Damien", [TextMessage("Hey D, what's up?", sender = False)])
    elif club == "cheer":
        call screen TextingScene("Damien", [TextMessage("Damien~", sender = False)])
    elif club == "yearbook":
        call screen TextingScene("Damien", [TextMessage("Hi...!", sender = False)])

    call screen TextingScene("Damien",
    [
        TextMessage("Damien?", sender = False),
        TextMessage("Ah, sorry [pcname], I just got this!"),
        TextMessage("I'm trying to beat this level on my game rn, but I'll text you later!"),
    ])

    jump textevent_end

label DamienText_Busy2:
    $ damienbusy = renpy.random.randint(1,4)
    if damienbusy == 1:
        call screen TextingScene("Damien",
        [
            TextMessage("Hey Damien what are you doing right now?", sender = False),
            TextMessage("Busy atm ttyl")
        ])
    if damienbusy == 2:
        call screen TextingScene("Damien",
        [
            TextMessage("How's things? ^^", sender = False),
        ])
        "You wait a few minutes for him to respond, but there is none."
        pcname "He must be busy."
    if damienbusy == 3:
        call screen TextingScene("Damien",
        [
            TextMessage("Hey, you around?", sender = False),
        ])
        "You wait a few minutes for him to respond, but there is none."
        pcname "He must be busy."
    if damienbusy == 4:
        call screen TextingScene("Damien",
        [
            TextMessage("Hey Damien!", sender = False),
        ])
        "You wait a few minutes for him to respond, but there is none."
        pcname "He must be busy."
    jump textevent_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
