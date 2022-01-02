label violet_phone1:
    play sound PhoneVibration
    "While you're getting ready for bed, your phone vibrates."

    call screen TextingScene("Violet",
    [
        TextMessage("[pcname]."),
        TextMessage("Text me.")
    ])

    menu violetPhoneResponse1:
        "What will you do?"
        "Reply" if True:

            call screen TextingScene("Violet",
            [
                TextMessage("What's up?", sender = False),
                TextMessage("Finally!"),
                TextMessage("What are you wearing tomorrow?"),
                TextMessage("What?", sender = False),
                TextMessage("To school. What are you wearing?"),
            ])

            if club == "track":
                call screen TextingScene("Violet", [TextMessage("Whatever I pick up in the morning?", sender = False)])
            elif club == "cheer":
                call screen TextingScene("Violet", [TextMessage("Not sure. I need to do laundry.", sender = False)])
            elif club == "yearbook":
                call screen TextingScene("Violet", [TextMessage("Idk?", sender = False)])

            call screen TextingScene("Violet",
            [
                TextMessage("Ugh. Okay. What color at least?"),
                TextMessage("I'm really not sure.", sender = False),
                TextMessage("You're impossible!"),
                TextMessage("Why does it matter?", sender = False),
                TextMessage("It's usually not a problem because you're so out of fashion."),
                TextMessage("But we wore the same shade of blue today."),
                TextMessage("Oh.", sender = False),
                TextMessage("Whatever. I'm wearing purple so wear something different."),
                TextMessage("Got it?")
            ])

            menu violetPhoneResponse2:
                "What will you say?"
                "I think I'm wearing purple." if True:

                    call screen TextingScene("Violet",
                    [
                        TextMessage("I think I'm wearing purple.", sender = False),
                        TextMessage("Seriously!?"),
                        TextMessage("Fine."),
                        TextMessage("I'll wear red."),
                        TextMessage("Wait I think my purple shirt is dirty.", sender = False),
                        TextMessage("Quit fucking with me [pcname]"),
                        TextMessage("I'm wearing purple"),
                        TextMessage("DO NOT WEAR PURPLE"),
                        TextMessage("Purple got it see you tomorrow.", sender = False)
                    ])

                    "Giggling to yourself, you put your phone on the night stand."

                    jump events_end_period
                "Got it." if True:

                    call screen TextingScene("Violet",
                    [
                        TextMessage("Got it.", sender = False),
                        TextMessage("Good."),
                        TextMessage("Now that that's settled I'm going to bed."),
                        TextMessage("Have a good night!", sender = False)
                    ])

                    "You roll your eyes as you set your phone aside."
                    "She takes everything so seriously..."

                    jump events_end_period
        "Ignore" if True:

            if club == "track":
                pcname "She's always so demanding..."
            elif club == "cheer":
                pcname "I don't think I can handle her right before bed."
            elif club == "yearbook":
                pcname "I hope she's not mad, but..."

            "You put the phone down on your night stand with a sigh."

            jump events_end_period
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
