label kate_phone2:
    play sound PhoneVibration
    "As you're leaving work, your phone vibrates."

    call screen TextingScene("Kate", [TextMessage("I had the WORST customer tonight")])

    menu katePhone2Response1:
        "What will you do?"
        "Reply" if True:

            call screen TextingScene("Kate",
            [
                TextMessage("What happened?", sender = False),
                TextMessage("This old guy kept complaining about everything I did"),
                TextMessage("He even said I was too happy"),
                TextMessage("Why come to a maid cafe if you don't want to see cute stuff and happy girls?"),
                TextMessage("And then he LEFT HIS DENTURES ON HIS PLATE"),
                TextMessage("Ewwwww!", sender = False),
                TextMessage("I didn't see them and I threw them away"),
                TextMessage("I had to dig them out of the trash"),
                TextMessage("Wash them"),
                TextMessage("And then he blamed me for the whole thing")
            ])

            menu katePhone2Response2:
                "What will you say?"
                "What a jerk!" if True:

                    call screen TextingScene("Kate",
                    [
                        TextMessage("What a jerk!", sender = False),
                        TextMessage("I know! T-T"),
                        TextMessage("It was awful"),
                        TextMessage("Thanks for letting me vent though"),
                        TextMessage("I need to get a shower"),
                        TextMessage("Ttyl!!!")
                    ])

                    "Laughing, you put your phone away."
                "You touched them!?" if True:

                    call screen TextingScene("Kate",
                    [
                        TextMessage("You touched them!?", sender = False),
                        TextMessage("What else could I do?? T-T"),
                        TextMessage("That is so gross", sender = False),
                        TextMessage("I feel gross!"),
                        TextMessage("I need to get a shower"),
                        TextMessage("Ttyl!!!")
                    ])

                    "Grimacing, you put your phone away."
        "Ignore." if True:

            "You don't feel like talking about work right now, so you slip your phone back into your pocket."

    jump events_end_period
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
