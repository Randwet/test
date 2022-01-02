init offset = -1










style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)









screen home2():
    if cheatmode == True:
        if renpy.variant("pc"):
            key "K_5" action Jump("cheattestroomhall")
        if renpy.variant("touch"):
            imagebutton:
                xysize (308,160)
                idle Null()
                ypos 120
                action Jump("cheattestroomhall")
    if acts == 4:
        imagemap:
            ground 'images/Backgrounds/Living Room/Living Room Afternoon.jpg'
            hover 'images/Backgrounds/Living Room/Living Room Afternoon (Highlighted).jpg'

            hotspot (472,136,258,490) action Jump("room2")
            hotspot (1562,194,296,574) action Jump("city2")

    if acts == 3:
        imagemap:
            ground 'images/Backgrounds/Living Room/Living Room Day.jpg'
            hover 'images/Backgrounds/Living Room/Living Room Day (Highlighted).jpg'

            hotspot (472,136,258,490) action Jump("room2")
            hotspot (1562,194,296,574) action Jump("city2")

    if acts == 2:
        imagemap:
            ground 'images/Backgrounds/Living Room/Living Room Day.jpg'
            hover 'images/Backgrounds/Living Room/Living Room Day (Highlighted).jpg'

            hotspot (472,136,258,490) action Jump("room2")
            hotspot (1562,194,296,574) action Jump("city2")

    if acts == 1:
        imagemap:
            ground 'images/Backgrounds/Living Room/Living Room Night.jpg'
            hover 'images/Backgrounds/Living Room/Living Room Night (Highlighted).jpg'

            hotspot (472,136,258,490) action Jump("room2")
            hotspot (1562,194,296,574) action Jump("city2")
    if acts < 1:
        imagemap:
            ground 'images/Backgrounds/Living Room/Living Room Night.jpg'
            hover 'images/Backgrounds/Living Room/Living Room Night (Highlighted).jpg'

            hotspot (472,136,258,490) action Jump("room2")
            hotspot (1562,194,296,574) action Jump("city2")

    if catadopt == True:
        add 'catwater' xpos 544 ypos 860
        if catpostbought == True:
            add 'catpost1' xpos 250 ypos 750
            if catstuff == 2:
                add 'catpost2' xpos 234 ypos 722
        if catstuff == 4:
            add 'catnews' xpos 745 ypos 360
        if catfood >=50:
            add 'catfood1' xpos 420 ypos 850
            if catstuff == 3:
                add 'catfoodeat' xpos 420 ypos 815
        if catfood <=49 and catfood >=1:
            add 'catfood2' xpos 420 ypos 850
        if catfood < 0:
            $ catfood = 0
        if catfood == 0:
            add 'catfood3' xpos 420 ypos 850


screen room2():
    if acts == 4:
        imagemap:
            ground '[BedENH]'
            hover '[BedEH]'

            hotspot (8,116,421,964) action Jump("home2")
            hotspot (467,219,420,673) action Jump("wardrobe")
            hotspot (888,536,435,237) action Jump("laptop")
            hotspot (1329,465,591,576) action Jump("bed2")

    if acts == 3:
        imagemap:
            ground '[BedDNH]'
            hover '[BedDH]'

            hotspot (8,116,421,964) action Jump("home2")
            hotspot (467,219,420,673) action Jump("wardrobe")
            hotspot (888,536,435,237) action Jump("laptop")
            hotspot (1329,465,591,576) action Jump("bed2")

    if acts == 2:
        imagemap:
            ground '[BedDNH]'
            hover '[BedDH]'

            hotspot (8,116,421,964) action Jump("home2")
            hotspot (467,219,420,673) action Jump("wardrobe")
            hotspot (888,536,435,237) action Jump("laptop")
            hotspot (1329,465,591,576) action Jump("bed2")

    if acts == 1:
        imagemap:
            ground '[BedNNH]'
            hover '[BedNH]'

            hotspot (8,116,421,964) action Jump("home2")
            hotspot (467,219,420,673) action Jump("wardrobe")
            hotspot (888,536,435,237) action Jump("laptop")
            hotspot (1329,465,591,576) action Jump("bed2")

    if acts < 1:
        imagemap:
            ground '[BedNNH]'
            hover '[BedNH]'

            hotspot (8,116,421,964) action Jump("home2")
            hotspot (467,219,420,673) action Jump("wardrobe")
            hotspot (888,536,435,237) action Jump("laptop")
            hotspot (1329,465,591,576) action Jump("bed2")
    if catadopt == True:
        if catbedbought == True:
            add 'catbed1' xpos 1450 ypos 870
        if catstuff == 1:
            if catbedbought == True:
                add 'catbed2' xpos 1450 ypos 870
            else:
                add 'catsleep' xpos 1800 ypos 700
            if catstuff == 5:
                if catbedbought == True:
                    add 'catbed1' xpos 1450 ypos 870



screen player_stats():
    zorder 100

    use homework_notification

    imagemap:

        ground "gui/money-amount-idle.png"
        hover "gui/money-amount-hover.png"


        hotspot (1621, 33, 300, 67) action Show("cash_amount") hovered ShowTransient("cash_amount") unhovered Hide("cash_amount")
        key "K_1" action ToggleScreen("cash_amount")


        hotspot (1476, 115, 444, 67) action Show("time_and_day") hovered ShowTransient("time_and_day") unhovered Hide("time_and_day")
        key "K_2" action ToggleScreen("time_and_day")


        hotspot (0, 15, 129, 67) action ToggleScreen("stats")
        key "K_3" action ToggleScreen("stats")






        imagebutton auto "gui/phoneUI/phoneicon-%s.png":
            xalign 0.97
            yalign 0.96
            keysym "K_UP"
            action SensitiveIf("message" not in goingto and "bed" not in goingto), ToggleScreen("PhoneInterface")

screen stats():

    imagemap:

        ground "gui/stats-menu-idle.png"
        hover "gui/stats-menu-hover.png"


        hotspot (206, 110, 57, 14) action Hide("stats")


    vbox:
        xalign 0.01 yalign 0.13
        text "[dayname]"
        text "Day: [daycount]"

    vbox:
        xalign 0.01 yalign 0.23
        if intelligence >= 40:
            text ("{size=28}Grades: A{/size}")
        elif intelligence < 40 and intelligence >= 30:
            text ("{size=28}Grades: B{/size}")
        elif intelligence < 30 and intelligence >= 20:
            text ("{size=28}Grades: C{/size}")
        elif intelligence < 20:
            text ("{size=28}Grades: F{/size}")
        if intelligence < 0:
            $ intelligence = 0
        elif intelligence > 50:
            $ intelligence = 50
        bar value intelligence range 50 xmaximum 240 ymaximum 30 ysize 30 xsize 240
    vbox:
        if corruption < 0:
            $ corruption = 0
        if corruption > 100:
            $ corruption = 100
        xalign 0.01 yalign 0.313
        text ("{size=28}Corruption: [corruption]{/size}")
        bar value corruption range 100 xmaximum 240 ymaximum 30 ysize 30 xsize 240


screen cash_amount():

    zorder 100
    imagemap:

        ground "gui/cash-amount-hover.png"
    hbox:
        xalign 0.965 yalign 0.0422
        text "{size=28} {color=#ffffff}    Cash:  $[Cash]{/size}{/color}"


screen time_and_day():
    zorder 100
    imagemap:

        ground "gui/calendar-hover.png"
    hbox:
        xalign 0.973 yalign 0.121
        text "{size=28} {color=#ffffff} [dayname]{/size}{/color}"
        text "{size=28} {color=#ffffff}[daypart]{/size}{/color}"


screen catshop():
    if catpostbought == False:
        add 'catpostshop' xpos 200 ypos 350
        textbutton "Buy $75" action Jump("buycatpost") xpos 300 ypos 600
    if catbedbought == False:
        add 'catbedshop' xpos 1300 ypos 500
        textbutton "Buy $75" action Jump("buycatbed") xpos 1440 ypos 600
    add 'catfoodshop' xpos 750 ypos 460
    textbutton "Buy $50" action Jump("buycatfood") xpos 830 ypos 600
    textbutton "{b}Return{/b}" action Jump("shop2") xpos 875 ypos 900





screen homework_notification():



    zorder 3000 tag menu

    if havehomework and not completehomework:
        add "gui/homework-notification.png"

    else:
        imagemap:

            ground "gui/homework-icon-inactive.png"
            hover "gui/homework-icon-inactive-rollover.png"

            hotspot (145, 15, 79, 67) action Show("no_homework") hovered ShowTransient("no_homework") unhovered Hide("no_homework")

screen no_homework():
    zorder 100
    imagemap:

        ground "gui/homework-icon-inactive-rollover.png"







screen homework_notification2():

    zorder 3000

    imagemap:

        ground "gui/homework-icon-inactive.png"
        hover "gui/homework-icon-inactive-rollover.png"

        hotspot (145, 15, 79, 67) action Show("no_homework") hovered ShowTransient("no_homework") unhovered Hide("no_homework")






style fet_scrollbar:
    xpos 50
    ypos 0
    xminimum 30
    xmaximum 30
    yminimum 477
    ymaximum 477
    base_bar "gui/Dream Settings/scrollbar-empty.png"
    bar_vertical True
    bar_invert True
    thumb im.Scale("gui/Dream Settings/scrollbar-full.png",30,30)
    thumb_offset 13
    top_gutter 8
    bottom_gutter 8


screen DreamSettings():
    tag menu

    imagemap:
        ground "gui/Dream Settings/dream-settings-inactive.png"
        idle "gui/Dream Settings/dream-settings-inactive.png"
        hover "gui/Dream Settings/dream-settings-active.png"

        hotspot (1615, 152, 305, 75) action ShowMenu('history')
        hotspot (1615, 237, 305, 75) action ShowMenu('save')
        hotspot (1615, 322, 305, 75) action ShowMenu('load')
        hotspot (1615, 407, 305, 75) action ShowMenu('preferences')
        hotspot (1615, 492, 305, 75) action MainMenu()
        hotspot (1615, 577, 305, 75) action ShowMenu("DreamSettings")
        hotspot (1615, 662, 305, 75) action ShowMenu("about")
        hotspot (1615, 747, 305, 75) action OpenURL("https://www.patreon.com/hizorgames")
        hotspot (1615, 832, 305, 75) action ShowMenu("help")
        hotspot (1615, 917, 305, 75) action Quit(confirm=not main_menu)
        hotspot (1781, 43, 139, 69) action Return()

    $ fet_list=["Feet","Femdom", "Yuri", "Spanking", "Multiple Pairings", "Tentacles", "Futa", "Anal", "Degradation", "Submission", "Exhibition"]
    $ fet_vars=["feet","femdom", "yuri", "spanking","multiplepairings","tentacles","futa","anal","degradation","submission","exhibition"]
    $ fet_rows=0
    $ fet_count=0

    frame:
        background None
        area (0,500,1500,510)
        viewport id "fet_scroller":
            draggable True
            mousewheel True
            has frame:
                background None
                area (140,0,1490,920)
            for i in range(0,len(fet_list)):
                frame:
                    background "gui/Dream Settings/fetish-background-rectangle.png"
                    xmaximum 436
                    ymaximum 213
                    xpos 140 + fet_count%3*450
                    ypos fet_rows*230

                    text fet_list[i] xalign 0.05 yalign 0.05

                    imagebutton:
                        idle "gui/Dream Settings/off-button.png"
                        selected_idle "gui/Dream Settings/off-button-active.png"
                        hover "gui/Dream Settings/off-button-active.png"
                        xalign 0.85
                        yalign 0.9
                        action SetField(persistent, fet_vars[i], False)

                    imagebutton:
                        idle "gui/Dream Settings/on-button-inactive.png"
                        selected_idle "gui/Dream Settings/on-button-active.png"
                        hover "gui/Dream Settings/on-button-active.png"
                        xalign 0.15
                        yalign 0.9
                        action SetField(persistent, fet_vars[i], True)

                $ fet_count+=1
                if fet_count%3==0:
                    $ fet_rows+=1

        vbar value YScrollValue("fet_scroller") style "fet_scrollbar"















screen say(who, what):

    use abc

    style_prefix "say" tag menu
    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"




    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0




init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos












screen input(prompt):
    style_prefix "input"

    window:
        if renpy.variant("touch"):
            yalign 0
        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width










screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action




define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")
    yalign 0.46





screen warning():
    zorder 2000
    text "WARNING:" xalign 0.5 yalign 0.25 size 75 color "#ff0000"
    text "This game is intended for an adult audience." xalign 0.5 yalign 0.4 size 55 color "#ff0000"
    text "If you are not over the age of maturity" xalign 0.5 yalign 0.53 size 55 color "#ff0000"
    text "in your country, please exit this game!" xalign 0.5 yalign 0.6 size 55 color "#ff0000"
    text "All characters in this game are fictional and over 18." xalign 0.5 yalign 0.73 size 55 color "#ff0000"
    text "Any resemblance to real people or events is coincidental." xalign 0.5 yalign .8 size 55 color "#ff0000"





screen patreon():
    zorder 2000
    text "Check out our Patreon!" xalign 0.5 yalign 0.25 size 75 color "#ffffff"
    text "If you enjoy this game and would like to receive news, the latest builds," xalign 0.5 yalign 0.4 size 42 color "#ffffff"
    text "or want to support the game's development then follow us on Patreon!" xalign 0.5 yalign 0.46 size 42 color "#ffffff"
    text "{b}{a=https://www.patreon.com/hizorgames}Hizor Games at Patreon.com{/a}{/b}" xalign 0.5 yalign 0.6 size 52 color "#f963ab"
    text "Thanks! ^-^" xalign 0.5 yalign 0.8 size 42 color "#ffffff"





screen intro1():
    zorder 2000
    add "images/backgrounds/Black.jpg"
    text "Three years ago, you and your parents were in a terrible car accident while" xalign 0.5 yalign 0.45 size 35 color "#eae7b7"
    text "on vacation. Miraculously, you survived - but your parents were not so lucky." xalign 0.5 yalign 0.5 size 35 color "#eae7b7"





screen intro2():
    zorder 2000
    add "images/backgrounds/Black.jpg"
    text "With no other relatives to speak of, you spent a year getting your life back together." xalign 0.5 yalign 0.5 size 35 color "#eae7b7"





screen intro3():
    zorder 2000
    add "images/backgrounds/Black.jpg"
    text "Now you finally have a fresh start. You have a new apartment in the city of Uni." xalign 0.5 yalign 0.45 size 35 color "#eae7b7"
    text "The first month is paid for, but you'll have to find a job if you plan on staying for long." xalign 0.5 yalign 0.5 size 35 color "#eae7b7"





screen intro4():
    zorder 2000
    add "images/backgrounds/Black.jpg"
    text "You'll have to balance your expenses, your life, and finish high school after a year-long absence." xalign 0.5 yalign 0.5 size 35 color "#eae7b7"





screen intro5():
    zorder 2000
    add "images/backgrounds/Black.jpg"
    text "Eighteen, and already so much responsibility. You'll need all the luck and help you can get." xalign 0.5 yalign 0.5 size 35 color "#eae7b7"




screen intro6():
    zorder 2000
    add "images/backgrounds/Black.jpg"
    text "Welcome to Uni." xalign 0.5 yalign 0.5 size 35 color "#eae7b7"








screen abc():
    tag menu
    imagemap:
        ground "gui/quick-menu-inactiveAndroid.png"
        hover "gui/quick-menu-activeAndroid.png"
        selected_idle "gui/quick-menu-activeAndroid.png"
        hotspot (167, 726, 112, 63) action HideInterface()
        hotspot (711, 720, 177, 59) action ShowMenu('history')
        hotspot (899, 720, 146, 59) action Skip()
        hotspot (1057, 720, 150, 59) action Preference("auto-forward", "toggle")
        hotspot (1217, 720, 160, 59) action ShowMenu('load')
        hotspot (1388, 720, 160, 59) action ShowMenu('save')
        hotspot (1558, 720, 174, 59) action ShowMenu('preferences')









































screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Start") action Start()

        else:

            textbutton _("History") action ShowMenu("history")

            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")

        textbutton _("Preferences") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu()
        textbutton _("Dream Settings") action ShowMenu("DreamSettings")
        textbutton _("About") action ShowMenu("about")
        textbutton _("Visit Patreon") action OpenURL("https://www.patreon.com/hizorgames")

        if renpy.variant("pc"):


            textbutton _("Help") action ShowMenu("help")


            textbutton _("Quit") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")














screen main_menu():
    tag menu

    imagemap:
        ground 'gui/tsidle.png'
        hover 'gui/TS11080.png'

        hotspot (27, 375, 448, 83) action Start()
        hotspot (27, 458, 448, 83) action ShowMenu('load')
        hotspot (27, 541, 448, 83) action ShowMenu('preferences')
        hotspot (27, 624, 448, 83) action ShowMenu('DreamSettings')

        hotspot (27, 707, 448, 83) action OpenURL("https://www.patreon.com/hizorgames")
        hotspot (27, 790, 448, 83) action Quit(confirm=False)
    text "[config.version]" xpos 1750 ypos 1020 color "#000000"
    text "" at small_papers_animated()
    text "" at large_papers_animated()


transform small_papers_animated():
    linear 0.0 xpos 400 ypos 500
    block:
        Frame("gui/papers animation/back1.png")
        linear 4.5 xpos -200 ypos -500
        pause renpy.random.random()*renpy.random.randint(2,4)
        Frame("gui/papers animation/back2.png")
        linear 0.0 xpos 400 ypos 500
        linear 4.5 xpos -200 ypos -500
        pause renpy.random.random()*renpy.random.randint(2,4)
        Frame("gui/papers animation/back3.png")
        linear 0.0 xpos 400 ypos 500
        linear 4.0 xpos -200 ypos -500
        linear 0.0 xpos 400 ypos 500
        pause renpy.random.random()*renpy.random.randint(2,4)
        repeat

transform large_papers_animated():
    linear 0.0 xpos 300 ypos 500
    block:
        pause renpy.random.random()*renpy.random.randint(2,4)
        Frame("gui/papers animation/mid1.png")
        linear 3.5 xpos 1000 ypos -500
        pause renpy.random.random()*renpy.random.randint(2,4)
        Frame("gui/papers animation/front.png")
        linear 0.0 xpos -1000 ypos 500
        linear 3.5 xpos 1000 ypos -500
        pause renpy.random.random()*renpy.random.randint(2,4)
        Frame("gui/papers animation/mid2.png")
        linear 0.0 xpos -1000 ypos 500
        linear 4.0 xpos 1000 ypos -500
        linear 0.0 xpos -1000 ypos 500
        repeat











screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        has hbox


        frame:
            style "game_menu_navigation_frame"

        frame:
            style "game_menu_content_frame"

            if scroll == "viewport":

                viewport:
                    yinitial yinitial
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True

                    side_yfill True

                    has vbox
                    transclude

            elif scroll == "vpgrid":

                vpgrid:
                    cols 1
                    yinitial yinitial

                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True

                    side_yfill True

                    transclude

            else:

                transclude

    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45









screen about():
    tag menu





    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")


            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")



define gui.about = ""


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size












screen save():
    tag menu


    use file_slots(_("Save"))


screen load():
    tag menu


    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))



    use game_menu(title):

        fixed:


            order_reverse True

            button:
                style "page_label"
                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value


            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"
                xalign 0.5
                yalign 0.5
                spacing gui.slot_spacing
                for i in range(gui.file_slot_cols * gui.file_slot_rows):
                    $ slot = i + 1
                    button:
                        action FileAction(slot)
                        has vbox
                        add FileScreenshot(slot) xalign 0.5
                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        textbutton "{b}{color=#FFF}Delete{/c}{/b}" action FileDelete(slot):
                            style "delete_save_style"
                            xalign 0.5
                            yalign 0.4
                        key "save_delete" action FileDelete(slot)




            hbox:
                style_prefix "page"
                xalign 0.5
                yalign 1.0
                spacing gui.page_spacing
                textbutton _("<") action FilePagePrevious()
                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")


                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()

style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style delete_save_style:
    color "#000"

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")








screen preferences():
    tag menu


    use game_menu(_("Preferences"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "radio"
                    label _("Rollback Side")
                    textbutton _("Disable") action Preference("rollback side", "disable")
                    textbutton _("Left") action Preference("rollback side", "left")
                    textbutton _("Right") action Preference("rollback side", "right")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))




            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675










screen history():




    predict False tag menu

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:


                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"



                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what

        if not _history_list:
            label _("The dialogue history is empty.")




define gui.history_allow_tags = set()


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5








screen help():
    tag menu


    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0















screen confirm(message, yes_action, no_action):


    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 45

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 150

            textbutton _("Yes") action yes_action
            textbutton _("No") action no_action


    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")









screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        has hbox:
            spacing 9

        text _("Skipping")

        text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"



transform delayed_blink(delay, cycle):
    alpha .5

    pause delay
    block:

        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:


    font "DejaVuSans.ttf"









screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")









screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing


        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)



        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            has fixed:
                yfit gui.nvl_height is None

            if d.who is not None:

                text d.who:
                    id d.who_id

            text d.what:
                id d.what_id




define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")







style pref_vbox:
    variant "medium"
    xsize 675



screen quick_menu():


    variant "touch"

    zorder 100

    hbox:
        style_prefix "quick"

        xalign 0.9
        yalign 1.0

        textbutton _("Back") action Rollback()
        textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_pref_vbox:
    variant "small"
    xsize None

style slider_pref_slider:
    variant "small"
    xsize 900
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
