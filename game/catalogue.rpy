init python:
    class Dress(object):
        """
        Class which holds the attributes that make up
        the Dress object. Used for displaying clothes
        in the catalog or wardrobe.

        Takes 5 arguments: name, price, description, bought, and corruption
        """
        def __init__(self, name, price, description, corruption, bought = False):
            self._name = name
            self._price = price
            self._description = description
            self._bought = bought
            self._corruption = corruption
        
        
        
        @property
        def name(self):
            return self._name
        
        
        
        @property
        def price(self):
            return self._price
        
        
        
        @property
        def description(self):
            return self._description
        
        
        
        @property
        def bought(self):
            return self._bought
        
        
        
        @bought.setter
        def bought(self, value):
            self._bought = value
        
        
        
        @property
        def corruption(self):
            return self._corruption

    class DressList(object):
        """
        List of all dresses in the game. Used for displaying
        buyable clothes in the shop and wearable clothes in
        the wardrobe.

        Takes no arguments.
        """
        def __init__(self, *dresses):
            self._dresses = dresses
        
        
        @property
        def dresses(self):
            return self._dresses
        
        
        @dresses.setter
        def dresses(self, dress):
            self._dresses.append(dress)
        
        
        
        def getBoughtDresses(self):
            return [dress for dress in self._dresses if dress.bought]
        
        
        
        def getBuyableDresses(self):
            return [dress for dress in self._dresses if dress.price > 0]


default dressList = DressList(
    
    
    
    
    
    Dress("bluedress", -1, "Blue Dress", -1),
    Dress("lavender", 80, "Aqua Lavender", 0),
    Dress("princess", 80, "Princess Pink", 0),
    Dress("rocker", 80, "Rocker", 0),
    
    Dress("flirt", 90, "Flirt", 15),
    Dress("fullfrenchmaid", 175, "Full French Maid", 0),
    Dress("stockinggarter", 75, "Stocking & Garter", 25),
    Dress("daddygirl", 100, "Daddy's Girl", 30),
    Dress("virginkiller", 50, "Virgin Killer", 35),
    Dress("halter", -1, "Halter", 0),
    Dress("mini", -1, "Mini", 0),
    Dress("sexyyukata", 100, "Sexy Yukata", 40),
    Dress("slitdress", -1, "Slit Dress", 0),
    Dress("supersubby", 75, "Super Subby", 60),
)



default hairstyles = [
    "ponytail",
    "twintail",
    "messy",
    "bun",
    "braidedponytail",
    "katehair",
    "violethair",
    "down",
]



style dressName:
    xalign 0.5

    size 35
    font "GochiHand-Regular.ttf"

style dressText:
    xalign 0.5

    size 25


"Screen which shows a list of clothes the player can preview and purchase."


screen Catalog():
    default index = 0
    default dresses = dressList.getBuyableDresses()

    zorder 100
    modal True



    add "black" alpha 0.5


    use Chelsea()



    key "K_LEFT" action If(0 + index > 0, SetScreenVariable("index", index - 1))
    key "K_RIGHT" action If(3 + index < len(dresses), SetScreenVariable("index", index + 1))


    on "hide" action With(fade)



    imagemap:
        auto "gui/shop/catalog-back-and-arrow-buttons-%s.png"



        hotspot (1780, 40, 140, 70) action Hide("Chelsea"), Return()




        hotspot (49, 508, 51, 53) action If(0 + index > 0, SetScreenVariable("index", index - 1))



        hotspot (1205, 509, 51, 52) action If(3 + index < len(dresses), SetScreenVariable("index", index + 1))

    hbox:
        xalign 0.145
        yalign 0.65

        spacing 30

        for dress in dresses[0 + index : 3 + index]:
            frame:

                xysize (331, 767)


                background "gui/shop/outfit-background.png"





                button:
                    xysize (331, 767)

                    xalign 0.5
                    yalign 0.5

                    hovered SetVariable("clothes", dress.name)
                    unhovered SetVariable("clothes", casualwear[0])

                    action NullAction()

                vbox:
                    yalign 0.5

                    fixed:
                        xcenter 0.6
                        ycenter 0.57


                        if dress.bought:
                            add "gui/shop/SoldLady.png" zoom 0.9 xcenter 0.4 yalign 0.5
                        else:

                            add "gui/shop/shop.png" zoom 0.28


                            add "Characters/Chelsea/Casual Clothes/chelsea_base_[dress.name].png" zoom 0.54


                            add "chelsea_top_[dress.name]" zoom 0.54

                    vbox:
                        xalign 0.5
                        ycenter -0.1

                        if dress.bought:

                            text dress.description style "dressName"



                            text "Cost: $[dress.price]" style "dressText" color "#767676"



                            text "Corruption: [dress.corruption]" style "dressText" color "#767676"
                        else:

                            text dress.description style "dressName"



                            text "Cost: $[dress.price]" style "dressText"



                            text "Corruption: [dress.corruption]" style "dressText"


                    if dress.bought:


                        frame:


                            xysize (211, 100)

                            xcenter 0.65
                            ycenter -0.1

                            background "gui/shop/Sold.png"
                    else:


                        imagebutton auto "gui/shop/buy-button-%s.png":
                            xalign 0.54
                            ycenter -0.1

                            action If(dress.price <= Cash and corruption >= dress.corruption, [SetVariable("Cash", Cash - dress.price), SetField(dress, "bought", True)], Show("NoCashOrCorruption", dissolve, dress))

"Screen that displays how much more money or corruption a player needs left to buy a piece of clothing."



screen NoCashOrCorruption(dress):
    zorder 100
    modal True

    add "black" alpha 0.8


    if Cash < dress.price and corruption < dress.corruption:
        default moneyLeft = dress.price - Cash
        default corruptionLeft = dress.corruption - corruption


        text "You need {color=#FF0000}[moneyLeft]{/color} more dollars and {color=#FF0000}[corruptionLeft]{/color} more corruption to buy the [dress.description] dress!":
            xalign 0.5
            yalign 0.5

            size 40
            color "#ffffff"

    elif Cash < dress.price:
        default moneyLeft = dress.price - Cash


        text "You need {color=#FF0000}[moneyLeft]{/color} more dollars to buy the [dress.description] dress!":
            xalign 0.5
            yalign 0.5

            size 40
            color "#ffffff"

    elif corruption < dress.corruption:
        default corruptionLeft = dress.corruption - corruption


        text "You need {color=#FF0000}[corruptionLeft]{/color} more corruption to buy the [dress.description] dress!":
            xalign 0.5
            yalign 0.5

            size 40
            color "#ffffff"



    timer 3.5 action Hide("NoCashOrCorruption")


    on "hide":
        action With(dissolve)

"Screen where the player can change Chelsea's clothes, her hair style, and also toggle on or off makeup on her face if on the proper route."




screen Wardrobe():
    default index = 0
    default hairIndex = hairstyles.index(casualwear[1]) + 1 if hairstyles.index(casualwear[1]) + 1 < len(hairstyles) else 0
    default dresses = dressList.getBoughtDresses()

    zorder 100
    modal True


    use Chelsea()



    key "K_LEFT" action If(0 + index > 0, SetScreenVariable("index", index - 1))
    key "K_RIGHT" action If(3 + index < len(dresses), SetScreenVariable("index", index + 1))


    on "hide" action With(fade)

    imagemap:
        auto "gui/wardrobe/back-button-and-arrows-%s.png"



        hotspot (1780, 40, 140, 70) action Hide("Chelsea"), Return()




        hotspot (48, 508, 52, 54) action If(0 + index > 0, SetScreenVariable("index", index - 1))



        hotspot (1204, 509, 52, 52) action If(3 + index < len(dresses), SetScreenVariable("index", index + 1))

    hbox:
        yalign 0.12
        spacing 5



        imagebutton auto "gui/wardrobe/default-%s.png":
            action (
                SetVariable("makeup", False),
                SetVariable("clothes", "default"),
                SetVariable("hair", "down"),
                SetVariable("casualwear", ("default", "down")),
                SetScreenVariable("hairIndex", 0)
            )



        imagebutton auto "gui/wardrobe/hairstyle-%s.png":
            action If(hairIndex < len(hairstyles) - 1,
                [
                    SetScreenVariable("hairIndex", hairIndex + 1),
                    SetVariable("casualwear", (casualwear[0], hairstyles[hairIndex])),
                    SetVariable("hair", hairstyles[hairIndex])
                ],
                [
                    SetScreenVariable("hairIndex", 0),
                    SetVariable("casualwear", (casualwear[0], hairstyles[hairIndex])),
                    SetVariable("hair", hairstyles[hairIndex])
                ])

        if makeupbutton:

            imagebutton auto "gui/wardrobe/makeup-%s.png":
                action ToggleVariable("makeup")

    hbox:
        xalign 0.145
        yalign 0.65
        spacing 30

        for dress in dresses[0 + index : 3 + index]:
            frame:

                xysize (331, 767)


                background "gui/shop/outfit-background.png"

                has vbox:
                    yalign 0.5
                    spacing -120


                text dress.description style "dressName"

                fixed:
                    xcenter 0.6
                    ycenter 0.6


                    add "gui/shop/shop.png" zoom 0.28


                    add "Characters/Chelsea/Casual Clothes/chelsea_base_[dress.name].png" zoom 0.54


                    add "chelsea_top_[dress.name]" zoom 0.54




                imagebutton auto "gui/wardrobe/wear-button-%s.png":
                    xalign 0.54
                    yoffset 70

                    action SetVariable("clothes", dress.name), SetVariable("casualwear", (dress.name, casualwear[1]))

"Displays the Chelsea sprite as a screen and refreshes the sprite every 0.1 second to update her appearance."



screen Chelsea():
    zorder 100



    add "chelsea" xalign 1.0 yalign 1.5



    timer 0.1:
        repeat True

        action Hide("Chelsea"), Show("Chelsea")


"Displays the wardrobe label and hides player stats. Upon return, jumps to the room2 screen."



label wardrobe:
    $ clothes, hair = casualwear
    hide screen player_stats

    scene bg Wardrobe
    call screen Wardrobe with fade

    show screen player_stats
    jump room2
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
