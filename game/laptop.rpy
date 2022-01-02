init:
    $ desktop_bgs={"Denki Airi":"Backgrounds/Denki Airi 1080p.png","Classroom":"Backgrounds/ClassroomE.jpg","City":"Backgrounds/City/CityMorning.jpg"}

screen laptop_button():
    textbutton "Laptop" action Show("laptop")

screen laptop():
    tag laptop
    add "gui/laptop/laptop.png"
    if global_desktop!="":
        add im.Scale(global_desktop,1746,937) pos 88,88
    if cheatmode == False:
        textbutton "{size=15}Cheat Mode: OFF{/size}" action ToggleVariable("cheatmode",true_value=None) xpos 1600 ypos 1000
    if cheatmode == True:
        textbutton "{size=15}{b}Cheat Mode: ON{/b}{/size}" action ToggleVariable("cheatmode",false_value=None) xpos 1600 ypos 1000
        if renpy.variant("touch"):
            text "{size=16}Touch the kitchen cupboard to access.{/size}" xpos 1500 ypos 1025
        else:
            text "{size=16}Press 5 in the living room.{/size}" xpos 1580 ypos 1030
        text "{size=16}Achievements disabled.{/size}" xpos 1580 ypos 1047

    imagemap:
        idle "gui/laptop/icons-inactive.png"
        hover "gui/laptop/icons-active.png"

        hotspot (135, 124, 140, 164) action Show("ach")
        hotspot (132, 310, 160, 174) action Show("NetCorsair")
        hotspot (135, 523, 138, 143) action Show("Gallery")
        hotspot (135, 692, 140, 173) action NullAction()
        hotspot (326, 125, 147, 165) action Show("change_bg")
        hotspot (327, 310, 147, 175) action Jump("homework")
        hotspot (330, 521, 137, 143) action Hide("laptop"),Hide("sub_laptop"),Jump("room2")



screen change_bg():
    modal True
    vbox:
        xalign 0.5
        yalign 0.5
        for i in desktop_bgs:
            textbutton i action SetVariable("global_desktop", desktop_bgs[i])
        textbutton "Remove" action SetVariable("global_desktop", "")
        textbutton "Close" action Hide("change_bg")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
