label shop2:
    show bg Shop
    if damienmall:
        $ goingto = "town"
        $ clothes, hair = casualwear

        call eventengine from _call_eventengine_88
    $ clothes, hair = casualwear
    show screen player_stats()
    "You have [Cash] dollars remaining. What would you like to buy?"
    if catadopt == True:
        if catbedbought == True and catpostbought == True:
            menu catshop1:
                "Bedroom Styles" if True:
                    call screen roomDesign with dissolve
                "Outfits" if True:
                    call screen Catalog with fade
                "Buy Cat Food $50" if catfood <= 51:
                    if Cash >=50:
                        $ foodmessage = 1
                        $ cathungry = 0
                        $ catfood = 100
                        $ Cash -=50
                        "You bought cat food for [kittenname]!"
                        jump shop2
                    elif True:
                        "You don't have enough money!"
                        jump shop2
                "Leave" if True:
                    jump city2
        elif True:
            menu catshop2:
                "Bedroom Styles" if True:
                    call screen roomDesign with dissolve
                "Outfits" if True:
                    call screen Catalog with fade
                "Cat Stuff" if True:
                    call screen catshop with dissolve
                "Leave" if True:
                    jump city2
    elif True:
        menu normalshop:
            "Bedroom Styles" if True:
                call screen roomDesign with dissolve
            "Outfits" if True:
                hide screen player_stats
                call screen Catalog with fade
                show screen player_stats
            "Leave" if True:
                jump city2

jump shop2
label buycatpost:
    if Cash >= 75:
        $ catpostbought = True
        $ Cash-=75
        "You bought a scratching post for [kittenname]!"
        jump shop2
    elif True:
        "You don't have enough money to buy this!"
        jump catshop2
label buycatbed:
    if Cash >= 75:
        $ catbedbought = True
        $ Cash-=75
        "You bought a bed for [kittenname]!"
        jump shop2
    elif True:
        "You don't have enough money to buy this!"
        jump catshop2
label buycatfood:
    if Cash >=50:
        $ foodmessage = 1
        $ cathungry = 0
        $ catfood = 100
        $ Cash -=50
        "You bought cat food for [kittenname]!"
        jump catshop2
    elif True:
        "You don't have enough money!"
        jump catshop2
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
