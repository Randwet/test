

label kate_phone_short1:
    play sound PhoneVibration
    "Your phone vibrates."

    call screen TextingScene("Kate",
    [
        TextMessage("[pcname]! I was just thinking about you!"),
        TextMessage("<3"),
        TextMessage("Thanks Kate!", sender = False),
    ])

    jump events_end_period

label kate_phone_short2:
    play sound PhoneVibration
    "Suddenly, you feel your phone vibrate."

    call screen TextingScene("Kate",
    [
        TextMessage("I miss you!"),
        TextMessage("<3")
    ])

    "You can't help but smile."

    call screen TextingScene("Kate", [TextMessage("Thanks Kate!", sender = False)])

    jump events_end_period



label kate_phone_short3:
    play sound PhoneVibration
    "Your phone vibrates on the night stand."

    call screen TextingScene("Kate",
    [
        TextMessage("Have a great day tomorrow!"),
        TextMessage("Thanks Kate! You too!", sender = False)
    ])

    jump events_end_period

label kate_phone_short4:
    play sound PhoneVibration
    "You snuggle into your blankets and close your eyes."
    "{i}BZZT{/i}"
    "{i}BZZT{/i}... {i}BZZT{/i}"
    "With a sigh, you open one eye and peek at your phone."

    call screen TextingScene("Kate",
    [
        TextMessage("Hey I know it's late"),
        TextMessage("But I can't find my phone"),
        TextMessage("Oh"),
        TextMessage("SORRY!!!!!!")
    ])

    "Sighing again, you can't help but smile."

    pcname "Oh, Kate..."

    jump events_end_period


label kate_phone_short5:
    play sound PhoneVibration
    "Sitting on the edge of your bed, you plug your phone in and set an alarm."

    call screen TextingScene("Kate",
    [
        TextMessage("Here's a reminder to all of my friends"),
        TextMessage("You're loved! <3"),
        TextMessage("Thanks Kate! You too!", sender = False)
    ])

    "Smiling, you set your phone on the night stand and slide into bed."

    jump events_end_period




label kate_phone_short6:
    play sound PhoneVibration
    "As you leave the school, your phone vibrates."

    call screen TextingScene("Kate",
    [
        TextMessage("Can't wait to work with you today!"),
        TextMessage("See you soon!", sender = False)
    ])

    jump events_end_period

label kate_phone_short7:
    play sound PhoneVibration
    "As you close your locker, your phone vibrates."

    call screen TextingScene("Kate",
    [
        TextMessage("I hope your day is going well!!!"),
        TextMessage("Thanks! You too!", sender = False)
    ])

    jump events_end_period

label kate_phone_short8:
    play sound PhoneVibration
    "You're walking home when your phone vibrates."

    call screen TextingScene("Kate",
    [
        TextMessage("Hope school wasn't too bad!"),
        TextMessage("See you soon!", sender = False)
    ])

    jump events_end_period
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
