screen townmap():
    add "map"
    key "K_b" action Jump("room2")
    imagebutton:
        xpos 646
        ypos 28
        idle "schoolidle"
        hover "schoolhover"
        action Jump("schoolevents")
    imagebutton:
        xpos 827
        ypos 258
        idle "houseidle"
        hover "househover"
        action Jump("home2")
    imagebutton:
        xpos 295
        ypos 331
        idle "mallidle"
        hover "mallhover"
        action Jump("shop2")
    imagebutton:
        xpos 511
        ypos 312
        idle "cafeidle"
        hover "cafehover"
        action If(job=='cafe', Jump("cafe"))
    imagebutton:
        xpos 109
        ypos 865
        idle "baridle"
        hover "barhover"
        action If(job=='bar', Jump("bar"))
    imagebutton:
        xpos 966
        ypos 546
        idle "bakeryidle"
        hover "bakeryhover"
        action If(job=='bakery', Jump("bakery"))
    imagebutton:
        xpos 87
        ypos 539
        idle "walkidle"
        hover "walkhover"
        action Jump("walkevents")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
