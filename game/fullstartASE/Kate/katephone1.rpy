label kate_phone1:
    play sound PhoneVibration
    "You're just starting to drift to sleep when your phone vibrates."
    "Sighing, you pick it up - squinting past the glow of the screen - to see who's texting you."

    call screen TextingScene("Kate",
    [
        TextMessage("[pcname]!!! I had the WORST DREAM"),
        TextMessage("Nightmare")
    ])

    menu katePhoneChoice1:
        "What will you do?"
        "Reply." if True:

            call screen TextingScene("Kate",
            [
                TextMessage("What happened?", sender = False),
                TextMessage("SPIDERS"),
                TextMessage("EVERYWHERE")
            ])

            menu katePhoneChoice2:
                "What will you say?"
                "That's all?" if True:

                    call screen TextingScene("Kate",
                    [
                        TextMessage("That's all?", sender = False),
                        TextMessage("Sorry! I'll let you sleep!"),
                        TextMessage("That would be great", sender = False)
                    ])
                "That's awful!" if True:

                    call screen TextingScene("Kate",
                    [
                        TextMessage("That's awful!", sender = False),
                        TextMessage("I was soooooo scared!"),
                        TextMessage("I bet! Are you okay now?", sender = False),
                        TextMessage("I think so"),
                        TextMessage("Thx [pcname]"),
                        TextMessage("Anytime. Sweet dreams!", sender = False),
                        TextMessage("Hope so!!")
                    ])

                    jump events_end_period
        "Ignore." if True:

            pass

    pcname "Ugh!"

    "Putting the phone down, you roll back over."

    jump events_end_period
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
