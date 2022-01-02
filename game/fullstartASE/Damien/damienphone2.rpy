label damien_phone2:
    "You slip into bed, and plug your phone into the charger."
    play sound PhoneVibration
    "Just as you close your eyes, it vibrates."

    call screen TextingScene("Damien", [TextMessage("You up?")])

    menu damienPhone2Response1:
        "What will you do?"
        "Reply." if True:

            call screen TextingScene("Damien",
            [
                TextMessage("Yep", sender = False),
                TextMessage("Okay good"),
                TextMessage("I just wanted to thank you"),
                TextMessage("Tonight was a lot of fun")
            ])

            menu damienPhone2Response2:
                "What will you say?"
                "I had fun too" if True:

                    call screen TextingScene("Damien",
                    [
                        TextMessage("I had fun too", sender = False),
                        TextMessage("You did?"),
                        TextMessage("Maybe we could hang out again sometime")
                    ])

                    menu damienPhone2Response3:
                        "What will you say?"
                        "Definitely." if True:

                            call screen TextingScene("Damien",
                            [
                                TextMessage("Definitely", sender = False),
                                TextMessage("Ok"),
                                TextMessage("Great")
                            ])
                        "Maybe." if True:
                            call screen TextingScene("Damien", [TextMessage("Maybe", sender = False)])
                "It was okay" if True:

                    call screen TextingScene("Damien", [TextMessage("It was okay", sender = False)])

            call screen TextingScene("Damien",
            [
                TextMessage("I guess I should let you sleep"),
                TextMessage("See you at school"),
                TextMessage("See ya", sender = False)
            ])
        "Ignore." if True:

            pass

    jump events_end_period
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
