label violet_phone2:
    play sound PhoneVibration
    "As you're grabbing your stuff from your locker, your phone vibrates."

    call screen TextingScene("Violet", [TextMessage("Hey girl!!!")])

    menu violetPhone2Response1:
        "What will you do?"
        "Reply." if True:

            call screen TextingScene("Violet",
            [
                TextMessage("Hi Violet", sender = False),
                TextMessage("Soooooooo"),
                TextMessage("Remember Felicia from my math class?")
            ])

            menu violetPhone2Response2:
                "What will you say?"
                "Nope." if True:

                    call screen TextingScene("Violet",
                    [
                        TextMessage("Nope", sender = False),
                        TextMessage("Omg you have to"),
                        TextMessage("She's so annoying"),
                        TextMessage("I talk about her all the time"),
                        TextMessage("She's the one who kisses the teacher's ass"),
                        TextMessage("Like ALL THE TIME"),
                        TextMessage("Got it", sender = False),
                        TextMessage("Anyway"),
                        TextMessage("She got caught ducking some guy in the auditorium"),
                        TextMessage("Ducking"),
                        TextMessage("DUCKING"),
                        TextMessage("OMG FUCKING!!!!!!")
                    ])
                "The pregnant one?" if True:

                    call screen TextingScene("Violet",
                    [
                        TextMessage("The pregnant one?", sender = False),
                        TextMessage("And she's not OFFICIALLY pregnant"),
                        TextMessage("But I'm sure she is"),
                        TextMessage("Felicia is the one who kisses the teacher's ass"),
                        TextMessage("Like ALL THE TIME"),
                        TextMessage("Got it", sender = False),
                        TextMessage("Anyway"),
                        TextMessage("She got caught ducking some guy in the auditorium"),
                        TextMessage("Ducking"),
                        TextMessage("DUCKING"),
                        TextMessage("OMG FUCKING!!!!!!")
                    ])

            menu violetPhone2Response3:
                "What will you say?"
                "This is hilarious." if True:

                    call screen TextingScene("Violet",
                    [
                        TextMessage("This is hilarious", sender = False),
                        TextMessage("It's not funny!"),
                        TextMessage("Of course not", sender = False),
                        TextMessage("Why are we friends!?")
                    ])

                    if violetdate1place == "restaurant":
                        call screen TextingScene("Violet",
                        [
                            TextMessage("Because I paid for your dinner the other day?", sender = False),
                            TextMessage("And it was really expensive?", sender = False),
                            TextMessage("Right <3")
                        ])
                    elif violetdate1place == "apartment":
                        call screen TextingScene("Violet",
                        [
                            TextMessage("Because I have an apartment of my own?", sender = False),
                            TextMessage("And I let you sleep in my bed?", sender = False),
                            TextMessage("Only because you don't even have a guest room")
                        ])
                "Seriously?" if True:

                    call screen TextingScene("Violet",
                    [
                        TextMessage("Seriously?", sender = False),
                        TextMessage("YES"),
                        TextMessage("Can you believe it?")
                    ])

                    if club == "track":
                        call screen TextingScene("Violet",
                        [
                            TextMessage("Was the auditorium empty?", sender = False),
                            TextMessage("That's what you're worried about?")
                        ])
                    elif club == "cheer":
                        call screen TextingScene("Violet",
                        [
                            TextMessage("Were they on the stage?", sender = False),
                            TextMessage("That's what you're worried about?")
                        ])
                    elif club == "yearbook":
                        call screen TextingScene("Violet",
                        [
                            TextMessage("How embarrassing", sender = False),
                            TextMessage("More like karma")
                        ])

            call screen TextingScene("Violet",
            [
                TextMessage("Anyway"),
                TextMessage("Her parents are pulling her out of the school"),
                TextMessage("So I don't have to deal with her anymore"),
                TextMessage("Lucky you", sender = False),
                TextMessage("Manicure appointment gtg"),
                TextMessage("Ttyl!")
            ])

            if club == "track":
                pcname "She's so... Well, Violet, I guess."
            elif club == "cheer":
                pcname "Shoot, I could use a manicure too..."
            elif club == "yearbook":
                pcname "She's too much sometimes..."

            "Slipping your phone into your pocket, you finish grabbing your things and leave."

            jump events_end_period
        "Ignore." if True:

            if club == "track":
                pcname "I just don't have the energy for her right now..."
            elif club == "cheer":
                pcname "I'll deal with her drama later..."
            elif club == "yearbook":
                pcname "It's probably not important..."

            "Slipping your phone into your pocket, you finish grabbing your things and leave."

            jump events_end_period
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
