
label damien_phone3:
    play sound PhoneVibration
    "As you're walking home from school, you feel your phone vibrate."

    call screen TextingScene("Damien", [TextMessage("Hey [pcname]")])

    menu damienPhone3Response1:
        "What will you do?"
        "Reply." if True:

            call screen TextingScene("Damien",
            [
                TextMessage("Hey", sender = False),
                TextMessage("How was your day?")
            ])

            menu damienPhone3Response2:
                "What will you say?"
                "It was rough." if True:

                    call screen TextingScene("Damien",
                    [
                        TextMessage("It was rough", sender = False),
                        TextMessage("Awww sorry"),
                        TextMessage("It's fine", sender = False)
                    ])
                "Pretty good." if True:

                    call screen TextingScene("Damien",
                    [
                        TextMessage("Pretty good.", sender = False),
                        TextMessage("Great")
                    ])

            call screen TextingScene("Damien",
            [
                TextMessage("So what club did you end up joining?"),
            ])

            if club == "track":
                call screen TextingScene("Damien", [TextMessage("Track", sender = False)])
            elif club == "cheer":
                call screen TextingScene("Damien", [TextMessage("Cheerleading", sender = False)])
            elif club == "yearbook":
                call screen TextingScene("Damien", [TextMessage("Yearbook club", sender = False)])

            call screen TextingScene("Damien",
            [
                TextMessage("You?", sender = False),
                TextMessage("I want to be a veterinarian"),
                TextMessage("So I always join the biology club")
            ])

            menu damienPhone3Response3:
                "What will you say?"
                "A vet?" if True:

                    call screen TextingScene("Damien",
                    [
                        TextMessage("A vet?", sender = False),
                        TextMessage("Yeah"),
                        TextMessage("It'll take a long time but I really want to work with animals"),
                        TextMessage("I volunteered at a zoo last summer and it was amazing"),
                        TextMessage("That sounds amazing", sender = False)
                    ])
                "Interesting." if True:
                    call screen TextingScene("Damien",
                    [
                        TextMessage("Interesting", sender = False),
                        TextMessage("It's not a popular club I guess"),
                        TextMessage("But I think it's really interesting"),
                        TextMessage("Yeah", sender = False)
                    ])

            call screen TextingScene("Damien",
            [
                TextMessage("So what're you doing?"),
                TextMessage("I have work after school", sender = False),
                TextMessage("Work? Where do you work?"),
                TextMessage("At a [job]", sender = False),
                TextMessage("That's neat"),
                TextMessage("Have a good night!"),
                TextMessage("Thx!", sender = False)
            ])
        "Ignore." if True:

            pass

    jump events_end_period
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
