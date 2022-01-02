













define config.name = _("Uni")




define gui.show_name = True




define config.version = "0.37.96"


define cheatmode = False
define config.console = False


define config.mouse = {"default":[ ("gui/cursor.png", 1, 1) ] }




define gui.about = _p("""
:Credits:

Director: Hizor

Lead Writer: BainDrenal

Writer: Emily Chaise

Programmers: Kenpachi Ramasan, ArizonaIdentities, NocturneLight

CG & Character Artist: Houpoartist & Bluereist

Background Artist: Lansfield

U.I Artist: Sasquatchii



Title Music: http://www.purple-planet.com


!Thank you for your Support!

""")






define build.name = "Uni"






define config.has_sound = True
define config.has_music = True
define config.has_voice = False













define config.main_menu_music = "movies/Tranquility.ogg"










define config.enter_transition = dissolve
define config.exit_transition = dissolve




define config.intra_transition = dissolve




define config.after_load_transition = dissolve




define config.end_game_transition = dissolve
















define config.window = "auto"
define config.rollback_enabled = True



define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)







default preferences.text_cps = 0





default preferences.afm_time = 15
















define config.save_directory = "Uni2-saves"







define config.window_icon = "gui/iconuni.png"





init python:


















    build.archive("scripts", "all")



    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)


    build.classify("game/**.ogg", 'archive')
    build.classify("game/**.rpy", 'scripts')
    build.classify("game/**.rpyc", 'scripts')
    build.classify('game/**.png', 'archive')
    build.classify('game/**.jpg', 'archive')
    build.classify('game/**.mkv', 'archive')




    build.documentation('*.html')
    build.documentation('*.txt')
    build.change_icon_i686 = True
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
