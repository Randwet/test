label damien_phone1:
    play sound PhoneVibration
    "As you get ready to walk home, you feel your phone vibrate."

    call screen TextingScene("Damien",
    [
        TextMessage("Hey"),
        TextMessage("You off work?")
    ])

    menu damienPhoneResponse1:
        "What will you do?"
        "Reply." if True:

            call screen TextingScene("Damien",
            [
                TextMessage("Yep", sender = False),
                TextMessage("Good day?")
            ])

            menu damienPhoneResponse2:
                "What will you say?"
                "Great!" if True:

                    call screen TextingScene("Damien",
                    [
                        TextMessage("Great!", sender = False),
                        TextMessage("Glad to hear it")
                    ])
                "Not really." if True:
                    call screen TextingScene("Damien",
                    [
                        TextMessage("Not really.", sender = False),
                        TextMessage("I'm sorry!"),
                        TextMessage("It's ok", sender = False)
                    ])

            call screen TextingScene("Damien",
            [
                TextMessage("So I never asked"),
                TextMessage("Do you even like coffee?")
            ])

            menu damienPhoneResponse3:
                "What will you say?"
                "Of course." if True:

                    call screen TextingScene("Damien",
                    [
                        TextMessage("Of course", sender = False),
                        TextMessage("Okay good"),
                        TextMessage("I was worried")
                    ])
                "Not really." if True:
                    call screen TextingScene("Damien",
                    [
                        TextMessage("Not really", sender = False),
                        TextMessage("Oh"),
                        TextMessage("Well"),
                        TextMessage("I mean... they have other stuff too..."),
                        TextMessage("It's fine!", sender = False),
                        TextMessage("I'm sure it's great", sender = False),
                        TextMessage("OK good")
                    ])

            call screen TextingScene("Damien",
            [
                TextMessage("I guess I'll see you Saturday then?"),
                TextMessage("Yep! See ya!", sender = False)
            ])
        "Ignore." if True:

            pass

    jump events_end_period
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
