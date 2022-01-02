label KateText_GardenParty:
    call screen TextingScene("Kate",
     [
          TextMessage("Kate, did you see the flyer for the garden party up at work?", sender = False),
          TextMessage("I did!!! It looks like so much fun!! :D"),
          TextMessage("Right? Wanna go together? It's at the park this Saturday.", sender = False),
          TextMessage("I wish I could.\n:( I have to work."),
          TextMessage("Boo! Won't anyone switch shifts with you?", sender = False),
          TextMessage("I already tried.\n:( Everyone has stuff going on that day."),
          TextMessage("It's okay though!! It's an annual thing, so I'll just go next year! :)"),
          TextMessage("I guess it's good to look on the bright side.", sender = False),
          TextMessage("Still sad you can't go this year though. :(", sender = False),
          TextMessage("That's okay!! Maybe we can go together next year? :)"),
          TextMessage("Yeah, that would be a lot of fun!", sender = False),
     ])

    jump textevent_end

label KateText_TVShow:
    call screen TextingScene("Kate",
     [
          TextMessage("Hi Kate!", sender = False),
          TextMessage("How's it going?", sender = False),
          TextMessage("Things are great!! :D"),
          TextMessage("I have the day off, so I'm just trying to figure out what I want to watch. >3<"),
          TextMessage("Nice! What are your options?", sender = False),
          TextMessage("Hrm... Well, I'm torn between Royal Roses and The Pink Ribbon Letter. :c"),
          TextMessage("They're both just so good! >//<"),
          TextMessage("What do you think I should watch? D:"),
     ])

    menu KateText_TVChoice:
        "Royal Roses." if True:
            call screen TextingScene("Kate",
               [
                    TextMessage("Go with Royal Roses. It's the last season, isn't it?", sender = False),
                    TextMessage("Yeah!! I've been avoiding it bc I don't want it to end >n<"),
                    TextMessage("You should watch that one. It'll give you some time to recover when it ends.", sender = False),
                    TextMessage("You're probably right... It's going to be a teary ending. ;__;"),
                    TextMessage("Thanks [pcname]!! I'm gonna go watch that now! :3"),
                    TextMessage("No problem, enjoy!", sender = False),
               ])
        "The Pink Ribbon Letter." if True:

            call screen TextingScene("Kate",
               [
                    TextMessage("You should watch The Pink Ribbon Letter. It's brand new, right?", sender = False),
                    TextMessage("Yeah, the first season just came out!! :)"),
                    TextMessage("Go watch that then, you'll have a lot of fun with it.", sender = False),
                    TextMessage("Plus you have the whole day to binge it so you don't need to stress out about watching it when you get off your shift.", sender = False),
                    TextMessage("That's a good point!!"),
                    TextMessage("Okay, I'm gonna go watch that then!! Thanks, [pcname]! :3"),
                    TextMessage("Np, enjoy!", sender = False),
               ])

    jump textevent_end



label KateText_PenguinSurprise:
    call screen TextingScene("Kate",
     [
          TextMessage("Hey Kate, how's it going?", sender = False),
          TextMessage("Really well!! >< I'm waiting on the mail!"),
          TextMessage("Okay lol. Are you expecting a package or something?", sender = False),
          TextMessage("Yesh!! >3<"),
          TextMessage("OMG!!! [pcname] it's HERE!!!"),
          TextMessage("IT'S SO CUTE!!! AHHHH!! <3 <3 <3 <3 <3"),
          TextMessage("What is it??", sender = False),
          TextMessage("AHHHH! JUST LOOK AT HOW CUTE SHE IS!!! <3 <3 <3"),
          TextMessage("KPSS", image = True),
          TextMessage("SHE IS SO SQUISHY AND SOFT!! EVEN BETTER THAN I IMAGINED! ;A;"),
          TextMessage("I LOVE HER~~! >////< <3"),
          TextMessage("Aw lol, that's really cute!", sender = False),
          TextMessage("Did you order it for yourself?", sender = False),
          TextMessage("Mhm!! She's been sold out everywhere ;A; I didn't think I'd be able to get her, but HERE SHE IS!! <3"),
          TextMessage("LOL, well I'm glad you got her :) Have you come up with a name for her?", sender = False),
          TextMessage("GACK! oAo I haven't even thought of that yet!!"),
          TextMessage("Um... Ummmm... Ummmmm!!!"),
          TextMessage("I'll name her Lady Berry!! For the little strawberry on her head!! >//< <3"),
          TextMessage("That sounds like a pretty good name!", sender = False),
          TextMessage("She's so cuuuuute~~!! ;~; I'll cuddle her forever!! <3 <3 <3"),
          TextMessage("LOL, as long as you leave room so I can join you!", sender = False),
     ])

    jump textevent_end

label KateText_CantSleep:
    call screen TextingScene("Kate",
     [
          TextMessage("Hey Kate!", sender = False),
          TextMessage("Hi [pcname]!!"),
          TextMessage("What're you up to?", sender = False),
          TextMessage("Nothing really~ I was gonna take a nap but I can't sleep. :c"),
          TextMessage("Really? Why not?", sender = False),
          TextMessage("I was watching some videos and a trailer for a scary movie came up :("),
          TextMessage("I keep trying to think of something else, but then I see that guy with the axe and I'm too awake to sleep! ;_;"),
     ])

    menu KateText_SleepySuggestions:
        "Try counting sheep!" if True:
            call screen TextingScene("Kate",
               [
                    TextMessage("You should try counting sheep!", sender = False),
                    TextMessage("There's a reason people recommend it so much. They wouldn't say it if it didn't work.", sender = False),
                    TextMessage("Hmmm... Maybe...!"),
                    TextMessage("But every time I close my eyes, I keep seeing the trailer. :c"),
                    TextMessage("You could always count axe guys if sheep aren't working. :P", sender = False),
                    TextMessage("That's not very nice! ;n;"),
                    TextMessage("I'll try one more time but if I can't fall asleep, I think I'll skip my nap today."),
                    TextMessage("That sounds like a good compromise.", sender = False)
               ])
        "Rewatch the trailer and give them all funny voices!" if True:

            call screen TextingScene("Kate",
               [
                    TextMessage("You know what I do when I see a really freaky trailer?", sender = False),
                    TextMessage("I watch it again.", sender = False),
                    TextMessage("Ehh?! oAo"),
                    TextMessage("How is that supposed to help me sleep? ;A;"),
                    TextMessage("Lol, you didn't let me finish!", sender = False),
                    TextMessage("I'll rewatch the trailer, but I turn the volume down and give everyone really silly voices.", sender = False),
                    TextMessage("When you do that, it becomes funnier to watch.", sender = False),
                    TextMessage("I don't know... The trailer was really creepy... ;n;"),
                    TextMessage("But if [pcname] says it works, maybe I'll try it..."),
                    TextMessage("If it doesn't, you can always blame me lol", sender = False),
                    TextMessage("I'll give it a try ;3; Thank you, [pcname]!!"),
                    TextMessage("No problem! :) Sleep tight!", sender = False),
               ])
        "Drink some warm milk." if True:

            call screen TextingScene("Kate",
               [
                    TextMessage("What if you warmed up some milk?", sender = False),
                    TextMessage("When I'm having a lot of trouble sleeping, I'll drink some warm milk with honey in it.", sender = False),
                    TextMessage("Hmmm that's not a bad idea!! :D"),
                    TextMessage("Maybe I'll give it a try >//<"),
                    TextMessage("Thank you, [pcname]!!! <3 <3 <3"),
                    TextMessage("Sure thing :)", sender = False),
               ])
        "Do you want me to come over?" if True:

            call screen TextingScene("Kate",
               [
                    TextMessage("Aw, that sounds awful, Kate. :(", sender = False),
                    TextMessage("Do you want me to come over?", sender = False),
                    TextMessage("Nuuu, it's okay. ;n;"),
                    TextMessage("I think I'll just skip my nap for now"),
                    TextMessage("Are you sure? I don't mind coming over.", sender = False),
                    TextMessage("Yeah, but thank you [pcname]!! <3"),
                    TextMessage("Talking to you makes me feel better. :3"),
                    TextMessage("I'm glad I can help. :)", sender = False),
               ])

    jump textevent_end

label KateText_Weather:
    call screen TextingScene("Kate",
     [
          TextMessage("Hey, do you work today?", sender = False),
          TextMessage("It's supposed to rain, so make sure you have an umbrella!", sender = False),
          TextMessage(";A; I wish I saw this earlier!!"),
          TextMessage("I have the day off but I had some errands to run so I'm not anywhere near home... ;_;"),
          TextMessage("Do you want me to find you and bring you one?", sender = False),
          TextMessage("Nuu, it's okay!! I'll pick one up at the store. I could use a new one anyway. c:"),
          TextMessage("Isn't it weird how as kids we loved jumping in puddles? Now if I get any dirty water on my skirt I'm sad! ^^;"),
          TextMessage("Yeah, I guess it is sort of weird. When did we stop doing that kind of stuff?", sender = False),
          TextMessage("I don't know ;~;"),
          TextMessage("Maybe I'll get some rain boots and see if it's still fun!"),
          TextMessage("If you do, let me know.", sender = False),
          TextMessage("...;n;"),
          TextMessage("It's not as much fun anymore."),
          TextMessage("Aw lol. Well thanks for the update.", sender = False),
     ])

    jump textevent_end



label KateText_Busy1:
    call screen TextingScene("Kate",
     [
          TextMessage("Hi Kate, what're you up to?", sender = False),
          TextMessage("Kate?", sender = False),
          TextMessage("At work rn, we're really busy!! Sowwie!!! ;__;"),
     ])

    jump textevent_end

label KateText_Busy2:
    $ katebusy = renpy.random.randint(1,4)
    if katebusy == 1:
        call screen TextingScene("Kate",
          [
               TextMessage("Hey Kate!", sender = False),
          ])
    if katebusy == 2:
        call screen TextingScene("Kate",
          [
               TextMessage("Yo.", sender = False),
               TextMessage("Katie!", sender = False),
          ])
    if katebusy == 3:
        call screen TextingScene("Kate",
          [
               TextMessage("Hey, you around?", sender = False),
          ])
    if katebusy == 4:
        call screen TextingScene("Kate",
          [
               TextMessage("Hey Kate, how's it going?", sender = False),
          ])
    "You wait a few minutes for her to respond, but there is none."
    pcname "Must be busy."
    jump textevent_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
