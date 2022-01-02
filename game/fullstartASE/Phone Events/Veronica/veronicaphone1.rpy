label veronicaPhone1:
    call screen TextingScene("Veronica", [TextMessage("Hey, you start at your new school tomorrow, right?")])

    "Veronica was your best friend before the accident."
    "You've barely spoken to her since then; you're not sure if you even want to respond."

    call screen TextingScene("Veronica",
    [
        TextMessage("Yeah.", sender = False),
        TextMessage("You'll have a great day!"),
        TextMessage("I really miss you!")
    ])

    menu veronicaResponse1:
        "What will you say?"
        "I miss you too!" if True:

            call screen TextingScene("Veronica", [TextMessage("I miss you too!", sender = False)])
        "Thanks!" if True:
            call screen TextingScene("Veronica", [TextMessage("Thnx", sender = False)])

    call screen TextingScene("Veronica", [TextMessage("I can't believe you moved so far away.")])

    "You stare at the screen, debating what to say in response."

    call screen TextingScene("Veronica",
    [
        TextMessage("You have to invite me to your new place sometime."),
        TextMessage("I'm super jealous that you have your own apartment!"),
    ])

    "This is why you've lost contact... She just doesn't get it."
    "Maybe she thinks she's being supportive - trying to help you focus on the good things instead of the tragedy."
    "But she just keeps reminding you of {i}why{/i} you moved."
    "You really do miss her, but..."

    menu veronicaResponse2:
        "What will you say?"
        "We'll get together soon." if True:

            call screen TextingScene("Veronica",
            [
                TextMessage("We'll get together soon!", sender = False),
                TextMessage("Awesome!"),
                TextMessage("Gtg! Talk later!")
            ])
            return
        "You have parents." if True:
            call screen TextingScene("Veronica",
            [
                TextMessage("Don't be jealous.", sender = False),
                TextMessage("You still have parents to live with.", sender = False),
                TextMessage("OMG!"),
                TextMessage("I'm sorry!!!"),
                TextMessage("That was really insensitive of me!"),
                TextMessage("Please don't hate me, [pcname]!")
            ])

            menu veronicaResponse3:
                "What will you say?"
                "Text back." if True:

                    call screen TextingScene("Veronica",
                    [
                        TextMessage("Sorry...", sender = False),
                        TextMessage("I don't hate you.", sender = False),
                        TextMessage("I'm just tired...", sender = False),
                        TextMessage("You should get some rest!"),
                        TextMessage("Big day tomorrow!"),
                        TextMessage("I will... Thanks.", sender = False)
                    ])
                "Ignore her." if True:
                    "You just can't bring yourself to hold up your end of the conversation anymore..."

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
