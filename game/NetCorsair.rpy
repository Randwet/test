


image nointernet = "gui/laptop/nointernet.png"

screen NetCorsair():
    modal True
    zorder 100

    add "nointernet"

    timer 3.5 action Hide("NetCorsair")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
