label violet_phone3:
    play sound PhoneVibration
    call screen TextingScene("Violet",
    [
        TextMessage("[pcname]"),
        TextMessage("You won't believe this")
    ])

    menu violetPhone3Response1:
        "What will you do?"
        "Reply." if True:

            call screen TextingScene("Violet",
            [
                TextMessage("Believe what?", sender = False),
                TextMessage("I just got the new Cyphone X!"),
            ])

            "You read her message again."
            "The Cyborg Phone X costs over $1000!"

            if paychecktotal<100:
                "That's over ten times your paycheck!"
            elif paychecktotal<200:
                "That's over five times your paycheck!"
            elif paychecktotal<300:
                "That's over three times your paycheck!"
            elif True:
                "That's a huge chunk of your paycheck!"

            call screen TextingScene("Violet", [TextMessage("Isn't that awesome?")])

            menu violetPhone3Response2:
                "What will you say?"
                "Wow!" if True:

                    call screen TextingScene("Violet",
                    [
                        TextMessage("Wow!", sender = False),
                        TextMessage("Right!?"),
                        TextMessage("How'd you afford it?", sender = False),
                        TextMessage("Please"),
                        TextMessage("My parents know better than to say no"),
                        TextMessage("Then you should have got me one too", sender = False),
                        TextMessage("LOL"),
                        TextMessage("I'll show it to you at lunch"),
                        TextMessage("Can't wait", sender = False),
                        TextMessage("<3")
                    ])

                    jump events_end_period
                "It's a waste of money." if True:

                    call screen TextingScene("Violet",
                    [
                        TextMessage("It's a waste of money.", sender = False),
                        TextMessage("Wow"),
                        TextMessage("Jealous much?")
                    ])

                    menu violetPhone3Response3:
                        "What will you say?"
                        "Sorry." if True:

                            call screen TextingScene("Violet",
                            [
                                TextMessage("Sorry.", sender = False),
                                TextMessage("It's fine"),
                                TextMessage("I deal with this a lot")
                            ])

                            "Rolling your eyes, you try to be patient with her."

                            call screen TextingScene("Violet",
                            [
                                TextMessage("You should see the pics it takes"),
                                TextMessage("Send one", sender = False),
                                TextMessage("After you were so mean?"),
                                TextMessage("Maybe if you're nice I'll send a really cute one later"),
                                TextMessage("Gtg! Update to install"),
                                TextMessage("Cya!", sender = False)
                            ])

                            "With a sigh, you tuck your phone away."

                            pcname "She's so spoiled..."

                            jump events_end_period
                        "I gtg." if True:

                            call screen TextingScene("Violet", [TextMessage("I gtg", sender = False)])

                            "You slide your phone into your pocket."
                            "Though it vibrates half a dozen times, you ignore it."

                            jump events_end_period
        "Ignore." if True:

            if club == "track":
                pcname "I'm beat; I can't talk to her right now."
            elif club == "cheer":
                pcname "I just want to relax..."
            elif club == "yearbook":
                pcname "I need a little peace and quiet right now..."

            call screen TextingScene("Violet", [TextMessage("I can see that you read it")])

            "Wincing, you put your phone back into your pocket."

            pcname "I'll never hear the end of this..."

            jump events_end_period
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
