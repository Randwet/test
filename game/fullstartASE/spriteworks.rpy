
image chelsea_base_underwear:
    "Characters/Chelsea/Base/chelsea_base_underwear_[underwear2].png"

image chelsea_top_school:
    "Characters/Chelsea/School Clothes/chelsea_top_school_[implants].png"

image chelsea_top_bluedress:
    "Characters/Chelsea/Casual Clothes/chelsea_top_bluedress_[implants].png"

image chelsea_top_daddygirl:
    "Characters/Chelsea/Casual Clothes/chelsea_top_daddygirl_[implants].png"

image chelsea_top_default:
    "Characters/Chelsea/Casual Clothes/chelsea_top_default_[implants].png"

image chelsea_top_flirt:
    "Characters/Chelsea/Casual Clothes/chelsea_top_flirt_[implants].png"

image chelsea_top_fullfrenchmaid:
    "Characters/Chelsea/Casual Clothes/chelsea_top_fullfrenchmaid_[implants].png"

image chelsea_top_halter:
    "Characters/Chelsea/Casual Clothes/chelsea_top_halter_[implants].png"

image chelsea_top_lavender:
    "Characters/Chelsea/Casual Clothes/chelsea_top_lavender_[implants].png"

image chelsea_top_mini:
    "Characters/Chelsea/Casual Clothes/chelsea_top_mini_[implants].png"

image chelsea_top_princess:
    "Characters/Chelsea/Casual Clothes/chelsea_top_princess_[implants].png"

image chelsea_top_rocker:
    "Characters/Chelsea/Casual Clothes/chelsea_top_rocker_[implants].png"

image chelsea_top_sexyyukata:
    "Characters/Chelsea/Casual Clothes/chelsea_top_sexyyukata_[implants].png"

image chelsea_top_slitdress:
    "Characters/Chelsea/Casual Clothes/chelsea_top_slitdress_[implants].png"

image chelsea_top_stockinggarter:
    "Characters/Chelsea/Casual Clothes/chelsea_top_stocking&garter_[implants].png"

image chelsea_top_supersubby:
    "Characters/Chelsea/Casual Clothes/chelsea_top_supersubby_[implants].png"

image chelsea_top_virginkiller:
    "Characters/Chelsea/Casual Clothes/chelsea_top_virginkiller_[implants].png"

image chelsea_top_cheer:
    "Characters/Chelsea/School Clothes/chelsea_top_cheer_[implants].png"

image chelsea_top_track:
    "Characters/Chelsea/School Clothes/chelsea_top_track_[implants].png"

image chelsea_top_bakerynew:
    "Characters/Chelsea/Bakery Clothes/chelsea_top_bakerynew_[implants].png"

image chelsea_top_underwear:
    "Characters/Chelsea/Base/chelsea_top_underwear_[underwear2]_[implants].png"

image chelsea_top_naked:
    "Characters/Chelsea/Base/chelsea_top_naked_[implants].png"


layeredimage chelsea:

    always "chelsea_base"



    always "chelsea_hair_[hair]_[haircolor]"



    if True:
        "chelsea_base_[clothes]"



    if True:
        "chelsea_top_[clothes]"




    group face:
        attribute blank default:
            "Characters/Chelsea/Expressions/chelsea_face_[makeup]_blank.png"

        attribute angry:
            "Characters/Chelsea/Expressions/chelsea_face_[makeup]_angry.png"

        attribute confused:
            "Characters/Chelsea/Expressions/chelsea_face_[makeup]_confused.png"

        attribute sad:
            "Characters/Chelsea/Expressions/chelsea_face_[makeup]_sad.png"

        attribute embarrassed:
            "Characters/Chelsea/Expressions/chelsea_face_[makeup]_embarrassed.png"

        attribute happy:
            "Characters/Chelsea/Expressions/chelsea_face_[makeup]_happy.png"

        attribute laugh:
            "Characters/Chelsea/Expressions/chelsea_face_[makeup]_laugh.png"

        attribute shocked:
            "Characters/Chelsea/Expressions/chelsea_face_[makeup]_shocked.png"



    always "chelsea_bangs_[hair]_[haircolor]"


label spritetest4:
    $ casualwear = (clothes, hair)

    "This is what we're wearing now."

    $ hair = "ponytail"
    $ clothes = "cheer"

    "Wearing the cheerleader attire."

    $ clothes, hair = casualwear

    "Now we're going back to our original outfit."

label spritetest3:
    menu optional_name4:
        "Go blonde?"
        "Yes." if True:

            $ haircolor = "blonde"
        "No." if True:
            $ haircolor = "red"

    $ hair = "down"

    "Down."

    $ hair = "ponytail"

    "Ponytail."

    $ hair = "twintail"

    "Twintail."

    $ hair = "bun"

    "Bun."

    jump spritetest


label spritetest2:
    hide chelsea with dissolve

    menu optional_name3:
        "Get implants?"
        "Yes" if True:

            $ implants = True
        "No" if True:

            $ implants = False


    $ clothes = "bluedress"
    show chelsea at center with fade


    "Blue Dress."

    $ clothes = "daddygirl"
    show chelsea at center with fade


    "Daddy's Girl."

    $ clothes = "default"
    show chelsea at center with fade


    "Default."

    $ clothes = "flirt"
    show chelsea at center with fade


    "Flirt."

    $ clothes = "fullfrenchmaid"
    show chelsea at center with fade


    "Full French Maid."

    $ clothes = "halter"
    show chelsea at center with fade


    "Halter."

    $ clothes = "lavender"
    show chelsea at center with fade


    "Lavender."

    $ clothes = "mini"
    show chelsea at center with fade


    "Mini."

    $ clothes = "princess"
    show chelsea at center with fade


    "Princess."

    $ clothes = "rocker"
    show chelsea at center with fade


    "Rocker."

    $ clothes = "sexyyukata"
    show chelsea at center with fade


    "Sexy Yukata."

    $ clothes = "slitdress"
    show chelsea at center with fade


    "Slit Dress."

    $ clothes = "stockinggarter"
    show chelsea at center with fade


    "Stocking & Garterbelt."

    $ clothes = "supersubby"
    show chelsea at center with fade


    "Super Subby."

    $ clothes = "virginkiller"
    show chelsea at center with fade


    "Virgin Killer."

    $ clothes = "cheer"
    show chelsea at center with fade


    "Cheerleader."

    $ clothes = "track"
    show chelsea at center with fade


    "Track."

    $ clothes = "school"
    show chelsea at center with fade


    "School."

    $ clothes = "cafe"
    show chelsea at center with fade


    "Cafe."

    $ clothes = "cafecorrupt"
    show chelsea at center with fade


    "Cafe Corrupt."

    $ clothes = "bar"
    show chelsea at center with fade


    "Bar."

    $ clothes = "bakery"
    show chelsea at center with fade


    "Bakery."

    $ clothes = "bakerycorrupt"
    show chelsea at center with fade


    "Bakery Corrupt."

    $ clothes = "bakerynew"
    show chelsea at center with fade


    "Bakery New."

    $ underwear2 = False
    $ clothes = "underwear"
    show chelsea at center with fade


    "Underwear 1."

    $ underwear2 = True
    show chelsea at center with fade


    "Underwear 2"

    $ clothes = "naked"
    show chelsea at center with fade


    "Naked."

    return

label spritetest:













    show chelsea at center

    menu optional_name1:
        "Which test do you want to do?"
        "Casual Wear Test." if True:

            jump spritetest4
        "Hair Test." if True:

            jump spritetest3
        "Torso Test." if True:

            jump spritetest2
        "Expression Test" if True:

            pass

    pcname @ happy "Default."

    pcname @ angry "Angry."

    pcname @ confused "Confused."

    pcname @ sad "Sad."

    pcname @ embarrassed "Embarrassed."

    pcname @ happy "Happy."

    pcname @ laugh "Laugh."

    pcname @ shocked "Shocked."

    menu optional_name2:
        "Turn on Makeup?"
        "Yes." if True:

            $ makeup = True
            show chelsea blank
            jump spritetest
        "No." if True:

            pass

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
