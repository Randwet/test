transform thumbnail_size:
    size (400,240)
    xanchor 0.5
    xpos 0.8
    ypos 0.08

init python:
    def buy_room(id):
        bedroom_catalogue_entries[id][2] = True
        store.Cash -= bedroom_catalogue_entries[id][0]
        
        if id not in bought_room:
            bought_room.append(id)


default bedroom_catalogue_entries = {
    "Basic": [0, "Basic", True, 0],
    "Eco": [200, "Eco", False, 0],
    "Elegant": [300, "Elegant", False, 0],
    "Girly": [200, "Girly", False, 0],
    "Goth": [400, "Goth", False, 0],
    "Kawaii": [450, "Kawaii", False, 0],
    "Sporty": [300, "Sporty", False, 0],
    "None": [0, "None", False, 0],
    "None": [0, "None", False, 0]
}

default bedroom_catalogue_show_order = ["Basic", "Eco", "Elegant", "Girly", "Goth", "Kawaii", "Sporty", "None", "None"]
default bought_room = ["Basic"]
default using_room = "Basic"

init python:
    def change_bedroom(bedroom_string):
        global BedENH
        global BedDNH
        global BedNNH
        global BedEH
        global BedDH
        global BedNH
        
        BedENH="Backgrounds/Bedroom/"+ bedroom_string + "/Evening NHL.jpg"
        BedDNH="Backgrounds/Bedroom/"+ bedroom_string + "/Day NHL.jpg"
        BedNNH="Backgrounds/Bedroom/"+ bedroom_string + "/Night NHL.jpg"
        BedEH="Backgrounds/Bedroom/"+ bedroom_string + "/Evening HL.jpg"
        BedDH="Backgrounds/Bedroom/"+ bedroom_string + "/Day HL.jpg"
        BedNH="Backgrounds/Bedroom/"+ bedroom_string + "/Night HL.jpg"
        
        global using_room
        using_room = bedroom_string


screen roomDesign():
    tag wardrobe
    add "Backgrounds/Shop.jpg"

    default wd_page = 0
    imagemap:
        ground "RoomCatalog/catalogue-inactive.png"
        idle "RoomCatalog/catalogue-inactive.png"
        hover "RoomCatalog/catalogue-active.png"


        if len(bedroom_catalogue_entries)>wd_page*3+3:
            hotspot (1778, 520, 59, 58) action SetScreenVariable("wd_page", wd_page+1)
        if wd_page>0:
            hotspot (70, 520, 59, 58) action SetScreenVariable("wd_page", wd_page-1)

    imagebutton:
        idle "gui/catalogue/BackActive.png"
        hover "gui/catalogue/BackInactive.png"
        action Jump("shop2")
        xpos 1780
        ypos 205

    for i in range(wd_page*3,wd_page*3+3):
        if bedroom_catalogue_show_order[i]=="None":
            text ""
        else:
            frame:
                background None
                xmaximum 330
                ymaximum 670
                ypos 280
                xpos 180+i%3*520

                if bedroom_catalogue_entries[bedroom_catalogue_show_order[i]][1] in bought_room:
                    if using_room == bedroom_catalogue_show_order[i]:
                        add "RoomCatalog/room-button-selected.png"
                        add "Backgrounds/Bedroom/"+ bedroom_catalogue_show_order[i] + "/Day NHL.jpg" at thumbnail_size

                        imagebutton:
                            xpos 0.38
                            yalign 0.8
                            idle "RoomCatalog/in-use-button.png"
                            hover "RoomCatalog/in-use-button.png"
                    else:
                        add "RoomCatalog/room-button-idle.png"
                        add "Backgrounds/Bedroom/"+ bedroom_catalogue_show_order[i] + "/Day NHL.jpg" at thumbnail_size

                        imagebutton:
                            xpos 0.38
                            yalign 0.8
                            idle "RoomCatalog/select-button-idle.png"
                            hover "RoomCatalog/select-button-hover.png"
                            action Function(change_bedroom, bedroom_catalogue_show_order[i])

                    text bedroom_catalogue_show_order[i] xpos 0.8 yalign 0.52 xanchor 0.5 font "GochiHand-Regular.ttf" size 54 color "#bc3739"

                else:
                    add "RoomCatalog/room-button-idle.png"
                    add "Backgrounds/Bedroom/"+ bedroom_catalogue_show_order[i] + "/Day NHL.jpg" at thumbnail_size

                    imagebutton:
                        xpos 0.38
                        yalign 0.8
                        idle "RoomCatalog/buy-button-idle.png"
                        hover "RoomCatalog/buy-button-hover.png"

                        sensitive (bedroom_catalogue_entries[bedroom_catalogue_show_order[i]][3] < store.corruption or bedroom_catalogue_entries[bedroom_catalogue_show_order[i]][3] == 0) and bedroom_catalogue_entries[bedroom_catalogue_show_order[i]][2] == False and (Cash == bedroom_catalogue_entries[bedroom_catalogue_show_order[i]][0] or Cash > bedroom_catalogue_entries[bedroom_catalogue_show_order[i]][0])
                        action Function(buy_room, id=bedroom_catalogue_entries[bedroom_catalogue_show_order[i]][1])

                    $ price = bedroom_catalogue_entries[bedroom_catalogue_show_order[i]][0]
                    text 'Cost: $[price]' xpos 0.8 yalign 0.59 xanchor 0.5 size 26 font "OpenSans-ExtraBold.ttf"
                    text bedroom_catalogue_show_order[i] xpos 0.8 yalign 0.52 xanchor 0.5 font "GochiHand-Regular.ttf" size 54 color "#cc7072"


label roomDesign:
    hide screen player_stats
    call screen roomDesign
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
