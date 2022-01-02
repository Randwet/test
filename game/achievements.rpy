
init python:
    class Ach:
        def __init__(self,name="",unlocked_info="",locked_info="",active_pic="", inactive_pic="", unlocked=False):
            self.name=name
            self.unlocked_info=unlocked_info
            self.locked_info=locked_info
            self.active_pic=active_pic
            self.inactive_pic=inactive_pic
            self.unlocked=unlocked

    def unlock_ach(item):
        if item.name not in persistent.achievements:
            persistent.achievements.append(item.name)
            item.unlocked=True

    lottery=Ach("Lottery Winner!","Wow! You actually managed to win the lottery! What are you going to do with all that extra cash?", "Do you think it's possible to win the lottery?",
    active_pic="gui/achicons/LotteryUnlocked.png",
    inactive_pic="gui/achicons/LotteryLocked.png", unlocked=False)

    rich=Ach("Rich","Huh, either you cheated or you actually managed to save up $6000! That's seriously impressive! Did you even buy anything?!", "This is a lot of money. Save up $6000.",
    active_pic="gui/achicons/DollarSignsUnlocked.png",
    inactive_pic="gui/achicons/DollarSignsLocked.png", unlocked=False)

    piggy=Ach("Stockpile", "You did actually manage to save $2000. Well done!", "Save up $2000.",
    active_pic="gui/achicons/PiggyBankUnlocked.png",
    inactive_pic="gui/achicons/PiggyBanklocked.png", unlocked=False)

    wallet=Ach("Frugal", "You've saved up $1000! That's great! Keep going!", "Saving up your funds is important for the long run. Save up $1000.",
    active_pic="gui/achicons/WalletUnlocked.png",
    inactive_pic="gui/achicons/WalletLocked.png", unlocked=False)

    corrupt=Ach("Corrupted", "You've managed to become fully corrupted. Not sure if that is a good or bad thing.", "Time to have a little bit of devilish fun. Reach 100 Corruption",
    active_pic="gui/achicons/CorruptedUnlocked.png",
    inactive_pic="gui/achicons/CorruptedLocked.png", unlocked=False)

    kinkygf=Ach("Dominant Girlfriend", "So you and Violet huh? Kinda figured she'd be into all that kinky stuff.", "Find a girlfriend and have her be your Dom.",
    active_pic="gui/achicons/VioUnlocked.png",
    inactive_pic="gui/achicons/VioLocked.png", unlocked=False)

    bed=Ach("Indecisive Decorator", "Not sure if you're just a shopaholic or you really like all those rooms. Now, which one are you going to use?", "Why buy one room style when you can buy all of them?",
    active_pic="gui/achicons/BedUnlocked.png",
    inactive_pic="gui/achicons/BedLocked.png", unlocked=False)

    aplus=Ach("Honor Roll", "Great job keeping those grades up! I'm proud!", "Think you can manage to keep your grades at A+ for a month?",
    active_pic="gui/achicons/APlusUnlocked.png",
    inactive_pic="gui/achicons/APlusLocked.png", unlocked=False)

    ouch=Ach("Ouch!", "Ouch! You think he deserved that slap? Yeah.. probably.", "Slap a student as hard as you can!",
    active_pic="gui/achicons/OuchUnlocked.png",
    inactive_pic="gui/achicons/OuchLocked.png", unlocked=False)

    airi=Ach("Airi!", "You've named yourself after our beloved cyberbunny girl. Perhaps there is some connection between you two?", "Secret.",
    active_pic="gui/achicons/NameUnlocked.png",
    inactive_pic="gui/achicons/NameLocked.png", unlocked=False)

    all_ach=[lottery,rich,piggy,wallet,corrupt,bed,aplus,ouch,kinkygf,airi]
    unlocked_ach=[]

    if not persistent.achievements:
        persistent.achievements=[]

    for i in persistent.achievements:
        for a in all_ach:
            if i==a.name:
                a.unlocked=True


screen ach():
    modal True
    add "gui/ach/achievement-laptop-bg.png"
    add "gui/ach/achievement-achievement-info-boxes.png"

    frame:
        background None
        has side "c r":
            area (220, 250, 1005, 635)
        viewport id "ach_vp":
            mousewheel True
            draggable True
            has vbox:
                spacing 15
            for i in range(0,(len(all_ach)/5)+1):
                hbox:
                    spacing 15
                    for a in range(i*5,((i*5)+5 if (i*5)+5<len(all_ach) else len(all_ach))):
                        frame:
                            maximum 165,162
                            minimum 165,162
                            background None
                            if all_ach[a].unlocked:
                                imagebutton idle "gui/ach/achievement-icon-box-inactive.png" hover "gui/ach/achievement-icon-box-active.png" action Show("hovered_ac", item=all_ach[a])
                                add all_ach[a].active_pic xalign 0.5 yalign 0.5
                            else:
                                imagebutton idle "gui/ach/achievement-icon-box-no-achievement-yet.png" action Show("hovered_ac", item=all_ach[a])
                                add all_ach[a].inactive_pic xalign 0.5 yalign 0.5
        vbar:
            value YScrollValue("ach_vp")
            xysize 46,639
            pos 0, -20
            top_bar "gui/ach/achievements-scrollbar-full.png"
            bottom_bar "gui/ach/achievements-scrollbar-empty.png"
            thumb "gui/ach/achievements-scrollbar-slider-handle.png"
            thumb_offset 23
            top_gutter -10
            bottom_gutter -10

    imagemap:
        alpha False
        idle "gui/ach/close-menu-inactive.png"
        hover "gui/ach/close-menu-active.png"

        hotspot (1660, 108, 153, 22) action Hide("ach"),Hide("hovered_ac")

screen hovered_ac(item):
    frame:
        background None
        has side "c r":
            area (1355, 211, 386, 710)
        viewport id "info_vp":
            mousewheel True
            draggable True

            has frame:
                background None
                xmaximum 346
            vbox:
                spacing 15
                text item.name size 30 color "#ffffff"
                if item.unlocked:
                    text item.unlocked_info color "#ffffff"
                else:
                    text item.locked_info color "#ffffff"

        vbar:
            value YScrollValue("info_vp")
            xysize 8,645
            pos -30, 20
            top_bar "gui/ach/achievement-info-scrollbar-full.png"
            bottom_bar "gui/ach/achievement-info-scrollbar-empty.png"
            thumb None
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
