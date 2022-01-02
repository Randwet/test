









init:



    $ event("schoolintro", "goingto=='school'", "daycount==1", event.once(), priority=1)
    $ event("jobhunt", "goingto=='town'", "daycount==1", event.once(), priority=1)
    $ event("introwalk", "goingto=='town'", "daycount<1", priority = 5)


    $ event("schooleventback", "goingto=='school'", event.once(), priority=1)
    $ event("schoolrandom01", "goingto=='school'", event.random(.30), priority=100)
    $ event("schoolrainyday", "goingto=='school'", event.random(.30), priority=100)
    $ event("genericschool", "goingto=='school'", event.solo())
    $ event("schoollunchtacos", "goingto=='school'", "day==2", event.random(.50), priority=90)
    $ event("schoolbully", "goingto=='school'", "daycount == 5", event.once(), priority=1)
    $ event("schoolfriends01", "goingto== 'school'", "daycount == 4", event.once(), priority=1)
    $ event("teacherstain", "goingto=='school'", "deskstain==True", event.once(), priority=10)
    $ event("booksknockoff", "goingto=='school'", "daycount>4", event.once(), priority=50)
    $ event("schoolrainygym", "goingto=='school'", event.once(), event.random (.25), priority=30)
    $ event("schoolmacbeth", "goingto=='school'", event.once(), event.random (.25), priority=30)
    $ event("schoolmacbeth2", "goingto=='school'", event.happened("schoolmacbeth"), event.once(), event.random (.25), priority=30)
    $ event("schoolmacbeth3", "goingto=='school'", event.happened("schoolmacbeth2"), event.once(), event.random (.25), priority=30)
    $ event("schoolhistoryfieldtrip", "goingto=='school'", event.random (.1), event.once(), priority=35)
    $ event("schoolhistorydocumentary", "goingto=='school'", event.random (.25), priority=30)
    $ event("schoolbullieshomework", "goingto=='school'","homeworkgirls == True", event.once(), event.random (.44), priority=10)
    $ event("schoolbullieshomework2", "goingto=='school'","copyhomework == True","homeworkgirls == True", event.once(), event.random (.44), priority=10)
    $ event("schoolbullieshomework2_steal", "goingto=='school'","'homeworkgirls == True'",event.happened("schoolbullieshomework2"), event.once(), event.random (.44), priority=10)
    $ event("schoolpeprally", "goingto=='school'", event.random (.15), priority=30)
    $ event("schoolfiredrill", "goingto=='school'", event.random (.1), priority=30)
    $ event("schoollunchcupcake", "goingto=='school'", event.random (.15), priority=30)



    $ event("matt_intro", "goingto=='school'", "daycount == 3", "mattsubmissive == True", "mattchain == 1", event.once(), priority=1)
    $ event("matt_scene1", "goingto=='school'", "mattsubmissive == True", "mattchain == 2", "daycount == 9", event.once(), priority=1)
    $ event("matt_cafeteriaspill", "goingto=='school'", "defymatt == True", "daycount == 15", event.happened("matt_scene1"), event.once(), priority=1)
    $ event("matt_scene2", "goingto=='school'", "mattsubmissive == True", "mattchain == 3", "daycount == 16", event.once(), priority=2)
    $ event("matt_blackmail_endgame", "goingto=='school'", "defymatt == True", "endgame == True", "mattchain > 1", event.happened("matt_scene2"), event.once(), priority=1)
    $ event("bully_gangbang", "goingto=='school'", "mattsubmissive == True", "mattchain == 5", "bullytelloff == 1", event.random(.60), event.once(), priority=10)
    $ event("matt_scene3", "goingto=='school'", "mattsubmissive == True", "mattchain == 4", "daycount == 19", event.once(), priority=1)
    $ event("matt_scene4", "goingto=='work'", "mattsubmissive == True", "mattchain == 5", "daycount == 32", event.happened("matt_scene3"), event.once(), priority=2)
    $ event("matt_scene5", "goingto=='textwork'", "mattsubmissive == True", "mattchain == 5", "daycount == 33", event.happened("matt_scene4"), event.once(), priority=2)
    $ event("MattMafiaResolution", "goingto== 'school'", "MafiaFavorMatt == True", "daycount == 37", event.happened("matt_scene5"), event.once(), priority=1)
    $ event("MattMafiaResolution2", "goingto== 'school'", "MafiaFavorMatt == True", "daycount == 40", event.happened("MattMafiaResolution"), event.once(), priority=1)
    $ event("MattMafiaResolution3", "MafiaFavorMatt == True", "daycount == 43", event.happened("MattMafiaResolution2"), event.once(), priority=1)
    $ event("matt_bullydamien", "goingto=='school'", "mattsubmissive == True", "MafiaFavorMatt == False", "daycount == 37", event.happened("matt_scene5"), event.once(), priority=2)
    $ event("matt_lending", "goingto=='school'", "mattsubmissive == True", "daycount == 40", event.happened("matt_bullydamien"), event.once(), priority=2)
    $ event("conference_intro", "goingto=='textschool'", "daycount==43", event.once(), priority=2)

    $ event("ptconference", "goingto=='school'", "daycount==45", event.happened("conference_intro"), event.once(), priority=1)

    $ event("matt_subspace", "goingto=='textwork'", "mattsubmissive == True", "daycount==45", event.happened("ptconference"), event.once(), priority=2)
    $ event("matt_petplay2", "goingto=='textwork'", "mattsubmissive == True", "daycount==51", event.happened("matt_subspace"), event.once(), priority=2)


    $ event("damienintro", "goingto=='school'", "bullytelloff == 1", "daycount == 8", event.once(), priority=1)
    $ event("damienlunch", "goingto=='school'", "damienevents == 1", "daycount == 11", event.once(), priority=1)
    $ event("damiencoffee", "goingto=='textwake'", "coffeeflag == True", "day==6", "daycount == 13", event.once(), priority=1)
    $ event("damienmovie", "goingto=='textbed' or goingto=='town'", "daypart=='Dusk'", "movieflag == True", "day==7", "daycount == 14", event.once(), priority=1)

    $ event("damien_lunchwviolet", "goingto=='school'", "damientelloff==False", event.happened("damienmovie"), "daycount == 18", event.once(), priority=1)
    $ event("damien_festivalmorning", "goingto=='textwake'", "day==7", "damienfestivalflag==True", "daycount== 21", event.once(), priority=1)
    $ event("damien_mallinvite", "goingto=='textwake'", "damienrelate=='dating'", "daycount== 34", event.happened("damien_festivalmorning"), event.once(), priority=2)
    $ event("damien_mall", "goingto=='town'", "damienmall==True", event.happened("damien_mallinvite"), event.once(), priority=1)
    $ event("damien_clubvisit_track", "goingto=='club'", "club=='track'", "damienrelate=='dating'", event.happened("track1"), event.happened("damien_mall"), event.once(), priority=1)
    $ event("damien_clubvisit_cheer", "goingto=='club'", "club=='cheer'", "damienrelate=='dating'", event.happened("cheer1"), event.happened("damien_mall"), event.once(), priority=1)
    $ event("damien_clubvisit_yearbook", "goingto=='club'", "club=='yearbook'", "damienrelate=='dating'", event.happened("year_mrdavis1"), event.happened("damien_mall"), event.once(), priority=1)
    $ event("damien_boardgame", "goingto=='town'", "day==7","daycount== 42","damienrelate=='dating'", event.happened("damien_mall"), event.once(), priority=1)
    $ event("damien_homecoming", "goingto=='textwork'", "homecoming==True", "daycount== 47", event.happened("damien_boardgame"), event.once(), priority=2)
    $ event("damien_homecoming_alt", "goingto=='textwork'", "damienrelate=='dating'", "homecoming==False", "daycount==47", event.happened("damien_boardgame"), event.once(), priority=2)

    $ event("damien_missingpanties", "goingto=='school'","damienrelate=='dating'", "daycount==50", event.happened("damien_homecoming"), event.once(), priority=1)
    $ event("damien_missingpanties", "goingto=='school'","damienrelate=='dating'", "daycount==50", event.happened("damien_homecoming_alt"), event.once(), priority=1)
    $ event("damien_aquarium", "goingto=='textwake'","damienrelate=='dating'", "daycount==56", event.happened("damien_missingpanties"), event.once(), priority=1)
    $ event("damien_conveniencestore", "goingto=='textschool'","damienrelate=='dating'", "daycount==60", event.happened("damien_aquarium"), event.once(), priority=1)
    $ event("damien_flowers", "goingto=='textwake'","damienrelate=='dating'", "daycount==63", event.happened("damien_conveniencestore"), event.once(), priority=1)
    $ event("matt_damienconflict1", "goingto=='school'", "damienrelate=='dating'", "MafiaFavorMatt == False", "mattsubmissive == True", "daycount == 72", event.happened("damien_flowers"), event.once(), priority=1)
    $ event("matt_damienconflict2", "goingto=='school'", "damienrelate=='dating'","daycount == 73", event.happened("matt_damienconflict1"), event.once(), priority=1)


    $ event("violetlunch1", "goingto=='school'", "violetscenes == 1", "daycount == 10", event.once(), priority=1)
    $ event("violetlunch2", "goingto=='school'", "violetscenes == 2", "daycount == 12", event.once(), priority=1)
    $ event("violetlunch3", "goingto=='school'", "violetscenes == 4", "daycount == 17", event.once(), priority=1)
    $ event("violetwork1", "goingto=='work'", "violetscenes == 3", "daycount == 15", event.once(), priority=1)
    $ event("violetdate1apart", "violetdate1place=='apartment'", "day==6", "violetscenes == 5", "daycount == 20", event.once(), priority=1)
    $ event("violetdate1rest", "goingto=='town'","violetdate1place=='restaurant'", "day==6", "violetscenes == 5", "daycount == 20", event.once(), priority=1)
    $ event("violetlunchoption1", "goingto=='school'", "violetscenes > 1", "damienevents > 1","daycount < 18", event.random(.38), event.once(), priority=10)
    $ event("violetlunch4", "goingto=='school'", "violetscenes == 6", "daycount == 24", event.once(), priority=1)
    $ event("violetdate2", "goingto=='textwake'", "violetdateflag == True", "day==6", "violetscenes == 7", "daycount==27", event.once(), priority=1)
    $ event("violethomeroom1", "goingto=='school'", "violetscenes == 8", "daycount == 30", event.once(), priority=10)
    $ event("violetdom1", "violetrelate=='Dom'", "goingto=='school'", "daycount == 31", event.once(), priority=10)
    $ event("violetdom2", "goingto=='textwork'", event.happened("violetdom1"), "daycount == 32", event.once(), priority=10)
    $ event("violetdom3", "goingto=='school'", event.happened("violetdom2"), "daycount == 36", event.once(), priority=10)
    $ event("violetdom3_date", "goingto=='textwake'", "violetdateflag == True", "day==7", "daycount == 42", event.happened("violetdom3"), event.once(), priority=1)
    $ event("violetsub1", "violetrelate=='Sub'", "goingto=='school'", "daycount == 31", event.once(), priority=10)
    $ event("violetsub2", "goingto=='textwork'", event.happened("violetsub1"), "daycount == 32", event.once(), priority=10)
    $ event("violetsub3", "goingto=='school'", event.happened("violetsub2"), "daycount == 36", event.once(), priority=10)
    $ event("violetsub3_date", "goingto== 'textwake'", "violetdateflag == True", "day==7", "daycount == 42", event.happened("violetsub3"), event.once(), priority=1)
    $ event("violetdom4_car", "goingto=='textwork'", "violetrelate=='Dom'", "day==4", "daycount == 46 or daycount == 59 ", event.happened("violetdom3_date"), event.once(), priority=1)

    $ event("violetdom5_carresolution", "goingto=='school'", "violetrelate=='Dom'","daycount == 47 or daycount == 60", event.happened("violetdom4_car"), event.once(), priority=1)
    $ event("violetdom5_afterwork", "goingto=='textwork'", "violetrelate=='Dom'","daycount == 47 or daycount == 60", event.happened("violetdom5_carresolution"), event.once(), priority=1)

    $ event("violetdom6_date", "goingto=='textwork'", "violetrelate=='Dom'","daycount == 59 or daycount == 64", event.happened("violetdom5_afterwork"), event.once(), priority=1)
    $ event("violetdom7_music", "goingto=='textwake'", "violetrelate=='Dom'", "day==6", "daycount == 69", event.happened("violetdom6_date"), event.once(), priority=1)
    $ event("violetsub_orgasmcontrol", "goingto=='school'", "violetrelate=='Sub'", "daycount == 43", event.happened("violetsub3_date"), event.once(), priority=1)


    $ event("violetsub4_branch1", "goingto=='school'", "violetrelate=='Sub'","daycount == 44", event.happened("violetsub_orgasmcontrol"), event.once(), priority=1)
    $ event("violetsub4_branch2", "goingto=='school'", "violetrelate=='Sub'", "daycount == 51", event.happened("violetsub4_branch1"), event.once(), priority=1)
    $ event("violetsub4_branch3", "goingto=='school'", "violetrelate=='Sub'", "daycount == 59", event.happened("violetsub4_branch2"), event.once(), priority=1)

    $ event("violetsub4_shop", "goingto=='textwork'", "violetrelate=='Sub'", "violetsub4choice=='shop'", event.once(), priority=1)
    $ event("violetsub4_dinner", "goingto=='textwork'", "violetrelate=='Sub'", "violetsub4choice=='dinner'", event.once(), priority=1)
    $ event("violetsub4_violethouse", "goingto=='textwork'", "violetrelate=='Sub'", "violetsub4choice=='violethouse'", event.once(), priority=1)
    $ event("violetsub4_clean", "goingto=='textwork'", "violetrelate=='Sub'", "violetsub4choice=='clean'", event.once(), priority=1)
    $ event("matt_violetconflict", "goingto=='textwork'", "violetscenes >= 9","MafiaFavorMatt == False","mattsubmissive == True", "daycount == 71", event.happened("matt_petplay2",), event.once(), priority=1)




    $ event ("kate_flowerinvite", "katerelate=='friend'", "goingto=='textwork'", "job=='cafe'","daycount==26", event.happened("kate_sick2"), event.once(), priority=20)
    $ event ("kate_flowerfest", "katerelate=='friend'", "goingto=='textwake'", "katefestival==True","daycount==28", "day==7", event.happened("kate_flowerinvite"), event.once(), priority=1)
    $ event ("kate_girlfriend_aftermath", "katerelate=='girlfriend'", "goingto=='work'", "job=='cafe'","daycount==29", event.happened("kate_flowerfest"), event.once(), priority=10)
    $ event ("kate_cookies", "katerelate=='girlfriend'", "goingto=='work'", "job=='cafe'","daycount==32", event.happened("kate_girlfriend_aftermath"), event.once(), priority=20)
    $ event ("kate_firstdate", "katerelate=='girlfriend'", "goingto=='textwake'","turndownkate == False","daycount==35", "day == 7", event.happened("kate_cookies"), event.once(), priority=20)
    $ event ("kate_makeout", "katerelate=='girlfriend'", "goingto=='work'", "job=='cafe'", "daycount==38", event.happened("kate_firstdate"), event.once(), priority=20)
    $ event ("kate_trouble1", "katerelate=='girlfriend'", "goingto=='work'", "job=='cafe'", "daycount == 39", event.happened("kate_makeout"), event.once(), priority=20)
    $ event ("kate_puppies", "katerelate=='girlfriend'", "goingto=='town'", "daycount == 41", event.happened("kate_firstdate"), event.once(), priority=20)
    $ event ("kate_dating_phone_short1", "katerelate=='girlfriend'", "TextCheck==True", event.random(.12), event.once(), priority=100)
    $ event ("kate_dating_phone_short2", "katerelate=='girlfriend'", "TextCheck==True", "goingto=='textbed'", event.random(.12), event.once(), priority=100)
    $ event ("kate_dating_phone_short3", "katerelate=='girlfriend'", "TextCheck==True", "goingto=='textschool'", event.random(.12), event.once(), priority=100)
    $ event ("kate_buttons", "katerelate=='girlfriend'", "goingto=='work'", "job=='cafe'","daycount == 44", event.happened("kate_puppies"), event.once(), priority=20)
    $ event ("kate_cupcakes", "katerelate=='girlfriend'", "goingto=='work'", "job=='cafe'", "daycount == 47", event.happened("kate_trouble1"), event.once(), priority=20)
    $ event ("kate_zoodate", "katerelate=='girlfriend'", "goingto=='town'", "job=='cafe'", "day == 6", event.happened("kate_cupcakes"), event.once(), priority=20)
    $ event ("kate_sleepover", "katerelate=='girlfriend'", "goingto=='work'", "job=='cafe'", "daycount == 54", event.happened("kate_buttons"), event.once(), priority=20)
    $ event ("kate_handholding", "katerelate=='girlfriend'", "goingto=='work'", "job=='cafe'","daycount == 57", event.happened("kate_sleepover"), event.once(), priority=20)
    $ event ("kate_hickey", "katerelate=='girlfriend'", "goingto=='work'", "job=='cafe'","daycount == 58", event.happened("kate_handholding"), event.once(), priority=20)
    $ event ("kate_routelock", "katerelate=='girlfriend'", "goingto=='work'", "job=='cafe'", "daycount == 59", event.happened("kate_hickey"), event.once(), priority=20)
    $ event ("KateConflicts_Violet", "violetscenes >= 9", "katerelate=='girlfriend'", "goingto=='work'", "job=='cafe'", event.random(.60), event.once(), event.happened("kate_hickey"), priority=15)
    $ event ("KateConflicts_Matt","mattchain > 3", "MafiaFavorMatt == False", "katerelate=='girlfriend'", "goingto=='cafe'", "job=='work'", event.random(.60), event.once(), event.happened("kate_hickey"), priority=15)
    $ event ("KateConflicts_Damien","damienrelate == 'dating'", "katerelate=='girlfriend'", "goingto=='work'", "job=='cafe'", event.random(.60), event.once(), event.happened("kate_hickey"), priority=15)





    $ event("cheer_generic", "goingto=='club'", "club=='cheer'", event.solo(), priority=100)
    $ event("cheer_first_meeting", "goingto=='club'", "club=='cheer'", event.once(), priority=5)
    $ event("cheer_tracy_intro", "goingto=='club'", "club=='cheer'", event.once(), priority=6)
    $ event("cheer_olivia_intro", "goingto=='club'", "club=='cheer'", event.once(), priority=7)
    $ event("cheer1", "goingto=='club'", "club=='cheer'", event.happened("cheer_olivia_intro"), event.once(), priority=20)
    $ event("cheer2", "goingto=='club'", "club=='cheer'", event.happened("cheer1"), event.once(), priority=20)
    $ event("cheer3", "goingto=='club'", "club=='cheer'", event.happened("cheer2"), event.once(), priority=20)
    $ event("cheer4", "goingto=='club'", "daycount > 30", "club=='cheer'", event.happened("cheer3"), event.once(), priority=20)
    $ event("cheer5", "goingto=='club'", "club=='cheer'", event.happened("cheer4"), event.once(), priority=20)
    $ event("cheer6", "goingto=='club'", "daycount > 45", "club=='cheer'", event.happened("cheer5"), event.once(), priority=20)
    $ event("cheer7", "goingto=='club'", "club=='cheer'", event.happened("cheer6"), event.once(), priority=20)
    $ event("cheer8", "goingto=='club'", "club=='cheer'", event.happened("cheer7"), event.once(), priority=20)


    $ event("track_generic", "goingto=='club'", "club=='track'", event.solo(), priority=200)
    $ event("track_first_meeting", "goingto=='club'", "club=='track'", event.once(), priority=5)
    $ event("track_august_intro", "goingto=='club'", "club=='track'", event.once(), priority=6)
    $ event("track_ryan_intro", "goingto=='club'", "club=='track'", event.once(), priority=7)
    $ event("track1", "goingto=='club'", "club=='track'", event.happened("track_ryan_intro"), event.once(), priority=7)
    $ event("track2", "goingto=='club'", "club=='track'", event.happened("track1"), event.once(), priority=7)
    $ event("track3", "goingto=='club'", "club=='track'", event.happened("track2"), event.once(), priority=7)
    $ event("track4", "goingto=='club'", "daycount > 30", "club=='track'", event.happened("track3"), event.once(), priority=7)
    $ event("track5", "goingto=='club'", "club=='track'", event.happened("track4"), event.once(), priority=7)
    $ event("track6", "goingto=='club'", "daycount > 45", "club=='track'", event.happened("track5"), event.once(), priority=7)
    $ event("track7", "goingto=='club'", "club=='track'", event.happened("track6"), event.once(), priority=7)
    $ event("track8", "goingto=='club'", "club=='track'", event.happened("track7"), event.once(), priority=7)


    $ event("year_generic", "goingto=='club'", "club=='yearbook'", event.solo(), priority=200)
    $ event("year_first_meeting", "goingto=='club'", "club=='yearbook'", event.once(), priority=5)
    $ event("year_sophie_intro", "goingto=='club'", "club=='yearbook'", event.once(), priority=6)
    $ event("year_levi_intro", "goingto=='club'", "club=='yearbook'", event.once(), priority=7)
    $ event("year_sophie1", "goingto=='club'", "club=='yearbook'", event.happened("year_levi_intro"), event.once(), priority=20)
    $ event("year_levi1", "goingto=='club'", "club=='yearbook'", event.happened("year_levi_intro"), event.once(), priority=20)
    $ event("year_mrdavis1", "goingto=='club'", "club=='yearbook'", event.happened("year_sophie1"), event.once(), priority=20)
    $ event("year_sophie2", "goingto=='club'", "daycount > 30", "club=='yearbook'", event.happened("year_sophie1"), event.once(), priority=20)
    $ event("year_levi2", "goingto=='club'", "club=='yearbook'", event.happened("year_levi1"), event.once(), priority=20)
    $ event("year_sophie3", "goingto=='club'",  "daycount > 45", "club=='yearbook'", event.happened("year_levi1"), event.once(), priority=20)
    $ event("year_mrdavis2", "goingto=='club'", "club=='yearbook'", event.happened("year_sophie3"), event.once(), priority=20)
    $ event("year_levi2", "goingto=='club'", "club=='yearbook'", event.happened("year_mrdavis2"), event.once(), priority=20)


    $ event("generictown", "goingto=='town'", event.solo())
    $ event("townbadarea", "goingto=='town'", "daypart == 'Dusk'", event.random(.16), priority=40)
    $ event("townlottery", "goingto=='town'", "lottostand > 0", event.random(.30), priority=40)
    $ event("townToxin", "goingto=='town'", event.random(.17), event.once(), priority=70)
    $ event("towncoffee", "goingto=='town'", event.random(.30), event.once(), priority=30)
    $ event("towncoffee2", "goingto=='town'", event.happened ("towncoffee"), event.random(.20), event.once(), priority=30)
    $ event("towncoffee3", "goingto=='town'", "coffeescenes == 1", event.happened ("towncoffee2"), event.random(.20), event.once(), priority=30)
    $ event("townkitten", "goingto=='town'", event.random(.25), event.once(), priority=30)
    $ event("townkitten2", "goingto=='town'", "kittenscenes == 1", event.happened ("townkitten"), event.random(.20), event.once(), priority=30)
    $ event("townkitten3", "goingto=='town'", "kittenscenes == 2", event.happened ("townkitten2"), event.random(.32), event.once(), priority=30)
    $ event("townkitten4", "goingto=='town'", "kittenscenes == 3", "findkittenhome == True", event.happened ("townkitten3"), event.random(.20), event.once(), priority=30)
    $ event("townkaraoke", "goingto=='town'", "karaokeleave == True", event.random(.55), priority=25)
    $ event("townkaraoke2", "goingto=='town'","karaokescenes == 1", event.happened ("townkaraoke"), event.random(.55), event.once(), priority=30)
    $ event("townkaraoke3", "goingto=='town'", event.happened ("townkaraoke2"), event.random(.55), event.once(), priority=30)
    $ event("townkaraoke4", "goingto=='town'", "meetmafia == True", event.happened ("townkaraoke3"), event.random(.55), event.once(), priority=30)
    $ event("townkaraoke5", "goingto=='town'", "meetmafia == True", "daycount > 18", event.happened ("townkaraoke4"), event.random(.70), event.once(), priority=20)
    $ event("townbookstore", "goingto=='town'", event.random(.10), priority=60)
    $ event("towncatcall", "goingto=='town'", event.random(.28), event.once(), priority=30)
    $ event("towncatcall2", "goingto=='town'", event.happened ("towncatcall"), event.random(.28), event.once(), priority=30)
    $ event("towncatcall3", "goingto=='town'", "corruption >=5", event.happened ("towncatcall2"), event.random(.28), event.once(), priority=30)
    $ event("towncatcall4", "goingto=='town'", "corruption >=5", event.happened ("towncatcall3"), event.random(.28), event.once(), priority=30)
    $ event("towncatcall5", "goingto=='town'", "corruption >=10", event.happened ("towncatcall4"), event.random(.28), event.once(), priority=30)
    $ event("towncatcall6", "goingto=='town'", "corruption >=20", "daypart=='Dusk'", "catcallflashing == True", event.happened ("towncatcall5"), event.random(.28), event.once(), priority=30)
    $ event("towncatcall7", "goingto=='town'", "corruption >=25", "daypart=='Dusk'", "catcalltouching == True", event.happened ("towncatcall6"), event.random(.28), event.once(), priority=30)
    $ event("towncatcall8", "goingto=='town'", "daypart=='Dusk'", "catcalloral == True", event.happened ("towncatcall7"), event.random(.25), event.once(), priority=30)
    $ event("farmersmarket", "goingto=='town'", event.random(.40), "marketscenes == 0", priority=30)
    $ event("farmersmarket2", "goingto=='town'", "marketscenes == 1", event.happened ("farmersmarket"), event.random(.40), event.once(), priority=30)
    $ event("farmersmarket3", "goingto=='town'", "marketscenes == 2", event.happened ("farmersmarket2"), event.random(.40), event.once(), priority=30)
    $ event("farmersmarket4", "goingto=='town'", "grannywork == True", event.happened ("farmersmarket3"), event.random(.40), event.once(), priority=30)
    $ event("farmersmarket5", "goingto=='town'", event.happened ("farmersmarket4"), event.random(.40), event.once(), priority=30)
    $ event("farmersmarket6", "goingto=='town'", event.happened ("farmersmarket5"), event.random(.40), event.once(), priority=30)
    $ event("farmersmarket7", "goingto=='town'", event.happened ("farmersmarket6"), event.random(.40), event.once(), priority=30)
    $ event("stripclub", "goingto=='town'", "daypart=='Dusk'", "corruption >=10", "stripclubvisit==False", event.random(.40), priority=29)
    $ event("townfakeid", "goingto=='town'", "daypart=='Dusk'", "fakerid == 1", event.happened ("stripclub"), event.random(.40), priority=20)
    $ event("stripclub2", "goingto=='town'", "daypart=='Dusk'", "fakerid == 2","corruption >=15", event.happened ("stripclub"), event.random(.40), priority=30)
    $ event("stripclub3", "goingto=='town'", "daypart=='Dusk'", "corruption >=20", event.happened ("stripclub2"), event.random(.40), event.once(), priority=30)
    $ event("stripclub4", "goingto=='town'", "daypart=='Dusk'", "corruption >=20", "bouncerflirt == True", event.happened ("stripclub3"), event.random(.40), event.once(), priority=30)
    $ event("stripclub5", "goingto=='town'", "daypart=='Dusk'", "day == 5", "corruption >=20", "bouncerflirt == True", event.happened ("stripclub4"), event.random(.99), event.once(), priority=30)
    $ event("stripclub6", "goingto=='town'", "daypart=='Dusk'", "day == 5", "corruption >=20", event.happened ("stripclub5"), event.random(.40), event.once(), priority=30)
    $ event("stripclub7", "goingto=='town'", "daypart=='Dusk'", "day == 5", "corruption >=20", "privateclient == True", event.happened ("stripclub6"), event.random(.40), event.once(), priority=30)
    $ event("stripclub8", "goingto=='town'", "daypart=='Dusk'", "day == 5", "corruption >=20", event.happened ("stripclub7"), event.random(.40), event.once(), priority=30)
    $ event("carwash01", "goingto=='town'", "daypart =='Afternoon'", "daycount >= 7", event.random(.35), event.once(), priority=30)
    $ event("carwash02", "goingto=='town'", "daypart =='Afternoon'", "daycount >= 32", "corruption >=10", event.random(.35), event.happened ("carwash01"), priority=30)

    $ event("aliceintrotown", "goingto=='town'", "daycount >= 31", event.random(.60), event.once(), priority=20)
    $ event("aliceatschool", "goingto=='school'", "daycount >= 38", event.happened ("aliceintrotown"), event.random(.60), event.once(), priority=20)


    $ event("bully_gangrape", "goingto=='town'", "mattslap == 1", "bullytelloff == 1", "daypart == 'Dusk'", event.random(.40), event.once(), priority=10)




    $ event("genericworkbakery", "goingto=='work'", "job=='bakery'", event.solo())
    $ event("bakeryrandom01", "goingto=='work'", "job=='bakery'", event.random(.47), priority=60)
    $ event("bakeryrandom02", "goingto=='work'", "job=='bakery'", event.happened("bakery_correct2"), event.random(.45), priority=60)
    $ event("bakeryrandom03", "goingto=='work'", "job=='bakery'", event.random(.3), priority=50)
    $ event("bakerycustomer01", "goingto=='work'", "job=='bakery'", event.random(.2), priority=40)
    $ event("bakerykittens", "goingto=='work'", "job=='bakery'", event.random(.12), priority=30)
    $ event("bakery_mistake1", "goingto=='work'", "job=='bakery'", "daycount == 8", event.once(), priority=20)
    $ event("bakery_correct1", "goingto=='work'", "job=='bakery'", "daycount == 9", event.happened("bakery_mistake1"), event.once(), priority=20)
    $ event("bakery_mistake2", "goingto=='work'", "job=='bakery'", "daycount == 10", "bakerychain==1", event.once(), priority=20)
    $ event("bakery_correct2", "goingto=='work'", "job=='bakery'", "daycount == 11", event.happened("bakery_mistake2"), event.once(), priority=20)
    $ event("bakery_mistake3", "goingto=='work'", "job=='bakery'", "daycount == 12", "bakerychain==2", event.once(), priority=20)
    $ event("bakery_correct3", "goingto=='work'", "job=='bakery'", "daycount == 16", event.happened("bakery_mistake3"), event.once(), priority=20)


    $ event("lisa_event1", "goingto=='work'", "job=='bakery'", "daycount == 17", event.happened("bakery_correct3"), event.once(), priority=19)
    $ event("lisa_event2", "goingto=='work'", "job=='bakery'", "daycount == 18", event.happened("lisa_event1"), event.once(), priority=19)
    $ event("lisa_event3", "goingto=='work'", "job=='bakery'", "daycount == 19", event.happened("lisa_event2"), event.once(), priority=19)
    $ event("lisa_event4", "goingto=='work'", "job=='bakery'", "daycount == 22", event.happened("lisa_event3"), event.once(), priority=19)
    $ event("bakery_study", "goingto=='work'", "job=='bakery'", "daycount == 23", event.happened("lisa_event4"), event.once(), priority=20)
    $ event("bakery_test", "goingto=='work'", "job=='bakery'", "daycount == 25", event.happened("bakery_study"), event.once(), priority=20)
    $ event("bakery_muffins", "goingto=='work'", "job=='bakery'", "daycount == 26", event.happened("bakery_test"), event.once(), priority=20)
    $ event("bakery_actdumb", "goingto=='work'", "job=='bakery'", "daycount == 29", event.happened("bakery_muffins"), event.once(), priority=20)
    $ event("bakery_mall", "goingto=='town'", "daypart =='Afternoon'", "job=='bakery'", "lisa_gotomall == True", "daycount == 35", "day==7", event.once(), priority=1)
    $ event("bakery_makeup", "goingto=='work'", "job=='bakery'", "lisa_gotomall == True", "daycount == 36", event.happened("bakery_mall"), event.once(), priority=20)
    $ event("bakery_catalogue", "goingto=='work'", "job=='bakery'", "bakerymakeup == False", "'bakeryhalfmakeup == False'", "daycount == 37", event.happened("bakery_makeup"), event.once(), priority=20)

    $ event("bakery_shoppingwLisa", "goingto=='town'", "job=='bakery'", "shoppingwlisa == False", "bakerymakeup == True", event.happened( "bakery_catalogue"), event.once(), priority=1)
    $ event("bakery_shoppingwLisaA", "goingto=='town'", "job=='bakery'", "shoppingwlisa == False", "bakerymakeup2 == True", event.happened("bakery_makeup"), event.once(), priority=1)
    $ event("bakery_shoppingwLisaB", "goingto=='town'", "job=='bakery'", "shoppingwlisa == False",  "bakerymakeup2 == True", event.happened("bakery_catalogue"), event.once(), priority=1)
    $ event("bakery_shoppingwLisaC", "goingto=='town'", "job=='bakery'", "shoppingwlisa == False", "bakerymakeup == True", event.happened("bakery_makeup",), event.once(), priority=1)

    $ event("bakery_flirtwkeith", "goingto=='work'", "job=='bakery'", "shoppingwlisa == True", "daycount == 43", event.once(), priority=20)
    $ event("bakery_blondemeeting", "goingto=='work'", "job=='bakery'", "daycount == 44", event.happened("bakery_flirtwkeith"), event.once(), priority=20)
    $ event("bakery_salon", "goingto=='work'", "job=='bakery'", "bakery_bimbo1 == True", "daycount == 45", event.happened("bakery_blondemeeting"), event.once(), priority=20)
    $ event("bakery_uniform", "goingto=='work'", "job=='bakery'", "daycount == 46", event.happened("bakery_salon"), event.once(), priority=20)
    $ event("bakery_stuffing", "goingto=='work'", "job=='bakery'", "daycount == 50", event.happened("bakery_uniform"), event.once(), priority=20)
    $ event("bakery_implants", "goingto=='work'", "job=='bakery'", "daycount == 51", event.happened("bakery_stuffing"), event.once(), priority=20)
    $ event("bakery_loan", "goingto=='work'", "job=='bakery'", "daycount == 52", event.happened("bakery_implants"), event.once(), priority=20)
    $ event("bakery_consultationsetup", "goingto=='work'", "job=='bakery'", "daycount == 57", event.happened("bakery_loan"), event.once(), priority=20)
    $ event("bakery_consultation", "goingto=='textwake'", "job=='bakery'", "daycount == 62", event.happened("bakery_consultationsetup"), event.once(), priority=20)
    $ event("bakery_consultationresult", "goingto=='work'", "job=='bakery'", "daycount == 65", event.happened("bakery_consultation"), event.once(), priority=20)
    $ event("bakery_surgery", "goingto=='textwake'", "job=='bakery'", "bakeryboobjobapprove == True", "daycount == 69", event.happened("bakery_consultationresult"), event.once(), priority=20)
    $ event("bakery_routelock", "goingto=='work'", "job=='bakery'", "bakeryroutelock == True", "daycount == 71", event.happened("bakery_surgery"), event.once(), priority=20)


    $ event("bakery_conflicts_school", "goingto=='school'", "bakery_blonde == True", "daycount == 46", event.once(), priority=1)
    $ event("bakery_conflicts_violetsub", "goingto=='textwork'", "violetdateflag == True", event.happened("bakery_conflicts_school"), "violetrelate == 'Sub'", "bakery_blonde == True", "daycount==46", event.once(), priority=1)
    $ event("bakery_conflicts2_matt", "goingto=='school'", "job=='bakery'", "mattsubmissive==True", event.happened("bakery_consultation"), event.once(), priority=1)
    $ event("bakery_conflicts2_violet", "goingto=='school'", "job=='bakery'", "violetscenes == 10", "bakeryboobjobapprove==True", event.happened("bakery_consultationsetup"),"daycount == 58", event.once(), priority=1)
    $ event("bakery_conflicts2_violet2", "goingto=='work'", "job=='bakery'", event.happened("bakery_conflicts2_violet"), "daycount == 58", event.once(), priority=1)
    $ event("bakery_damienconflict2", "goingto=='textwork'", "job=='bakery'", "damienrelate == 'dating'", "daycount == 52", event.happened("bakery_loan"), event.once(), priority=1)
    $ event("bakery_damienconflict3", "goingto=='work'", "job=='bakery'", "damienrelate == 'dating'", "daycount == 53", event.happened("bakery_damienconflict2"), event.once(), priority=1)




    $ event ("genericworkcafe", "goingto=='work'", "job=='cafe'", event.solo())
    $ event ("caferandom01", "goingto=='work'", "job=='cafe'", event.random(.45), priority=50)
    $ event ("caferandom02", "goingto=='work'", "job=='cafe'", event.random(.20), priority=49)
    $ event ("caferandom03", "goingto=='work'", "job=='cafe'", event.random(.27), priority=48)
    $ event ("cafeworker", "goingto=='work'", "job=='cafe'", "daycount==5", event.once(), priority=40)
    $ event ("cafe_event1", "goingto=='work'", "job=='cafe'", "cafeshirt < 3","daycount==8", priority=20)


    $ event ("cafe_kate1", "goingto=='work'", "job=='cafe'", "cafeshirt > 3","daycount==12",event.happened("cafe_event1"), event.once(), priority=1)
    $ event ("cafe_event2", "goingto=='work'", "job=='cafe'","cafeshirt > 3", event.once(),"daycount==16", event.happened("cafe_event1"), priority=1)
    $ event ("cafe_kate2", "goingto=='work'", "job=='cafe'","cafeshirt > 3", event.once(),"daycount==18", event.happened("cafe_kate1"), event.happened("cafe_event2"), priority=1)
    $ event ("cafe_event3", "goingto=='work'", "job=='cafe'","cafeshirt > 3", event.once(),"daycount==22", event.happened("cafe_event2"), priority=1)
    $ event ("cafe_kate3", "goingto=='work'", "job=='cafe'", "cafepanties==True","daycount==23", event.once(), priority=15)
    $ event ("cafe_event4", "goingto=='work'", "job=='cafe'", event.once(), "daycount==26", event.happened("cafe_event3"), priority=15)
    $ event ("kate_intro", "goingto=='work'", "job=='cafe'","daycount==2", event.once(), priority=1)
    $ event ("kate_picked_on", "katerelate=='friend'", "goingto=='work'", "job=='cafe'", "daycount==4", event.happened("kate_intro"), event.once(), priority=19)
    $ event ("kate_ice_cream", "katerelate=='friend'", "goingto=='work'", "job=='cafe'", "daycount==9", event.happened("kate_picked_on"), event.once(), priority=1)
    $ event ("kate_stands_up", "katerelate=='friend'", "goingto=='work'", "job=='cafe'","daycount==10", event.happened("kate_ice_cream"), event.once(), priority=1)
    $ event ("kate_friendship_end", "katerelate=='enemy'", "goingto=='work'", "job=='cafe'","daycount==24", event.happened("cafe_kate3"), event.once(), priority=1)
    $ event ("kate_walking_family", "katerelate=='friend'", "goingto=='town'", "job=='cafe'","daycount==14", event.happened("kate_stands_up"), event.once(), priority=1)
    $ event ("kate_sick", "katerelate=='friend'", "corruptkate==False", "goingto=='work'", "job=='cafe'","daycount==19", event.happened("kate_walking_family"), event.once(), priority=20)
    $ event ("kate_sick2", "katesickflag==True", "goingto=='textwork'", "job=='cafe'", event.happened("kate_sick"), event.once(), priority=1)





    $ event ("cafe_event5", "goingto=='work'", "job=='cafe'", event.once(),"daycount==29", event.happened("cafe_event4"), priority=15)
    $ event ("cafe_event6", "goingto=='work'", "job=='cafe'", "daycount==31", event.once(), event.happened("cafe_event5"), priority=15)
    $ event ("cafe_event7", "goingto=='work'", "job=='cafe'","daycount==33", event.once(), event.happened("cafe_event6"), priority=15)
    $ event ("cafe_event8", "goingto=='work'", "job=='cafe'", "cafesex==True","daycount==36", event.once(), event.happened("cafe_event7"), priority=15)
    $ event ("cafe_raise", "goingto=='work'", "job=='cafe'","daycount==40", event.once(), priority=15)

    $ event ("cafeconflict1_Matt", "mattchain > 3", "MafiaFavorMatt == False", "goingto=='school'", "job=='bar'", event.random(.60), event.once(), event.happened("bar_intro"), priority=15)
    $ event ("cafeconflict1_Damien","damienrelate == 'dating'", "goingto=='school'", "job=='bar'", event.random(.60), event.once(), event.happened("bar_intro"), priority=15)
    $ event ("cafeconflict1_VioletSub","violetrelate == 'Sub'", "goingto=='school'", "job=='bar'", event.random(.60), event.once(), event.happened("bar_intro"), priority=1)
    $ event ("cafeconflict1_VioletSub2", "violetrelate == 'Sub'", "goingto=='textwork'", "job=='bar'", event.once(), event.happened("cafeconflict1_VioletSub"), priority=1)
    $ event ("cafeconflict1_VioletDom","violetrelate == 'Dom'", "goingto=='work'", "job=='bar'", event.random(.60), event.once(), event.happened("bar_intro"), priority=1)
    $ event ("cafeconflict1_Damien","damienrelate == 'dating'", "goingto=='school'", "job=='bar'", event.random(.60), event.once(), event.happened("bar_intro"), priority=15)
    $ event ("cafeconflict1_Damien_afterwork","damienrelate == 'dating'", "goingto=='work'", "job=='bar'", "damienrelate=='dating'", event.random(.60), event.once(), event.happened("cafeconflict1_Damien_afterwork"), priority=15)


    $ event ("bar_random01", "goingto=='work'", "job=='bar'", event.random(.45), priority=70)
    $ event ("bar_random02", "goingto=='work'", "job=='bar'", event.random(.45), priority=70)
    $ event ("bar_random03", "goingto=='work'", "job=='bar'", event.random(.50), priority=70)
    $ event ("bar_random04", "goingto=='work'", "job=='bar'", event.random(.50), priority=70)
    $ event ("bar_random05", "goingto=='work'", "job=='bar'", event.random(.50), priority=70)
    $ event ("bar_intro", "goingto=='work'", "job=='bar'", event.happened("cafe_event8"), event.once(), priority=1)
    $ event ("bar_scene1", "goingto=='work'", "job=='bar'", "daycount > 39", event.happened("bar_intro"), event.once(), priority=3)
    $ event ("bar_scene1_domviolet","violetrelate=='Dom'", "violetbarpickup == True", "goingto=='textwork'", "job=='bar'", event.happened("bar_scene1"), event.once(), priority=1)
    $ event ("bar_scene2", "goingto=='work'", "job=='bar'", event.happened("bar_scene1"), event.once(), priority=1)
    $ event ("bar_scene3", "goingto=='work'", "job=='bar'", event.happened("bar_scene2"), event.once(), priority=1)
    $ event ("bar_scene3_leaving", "goingto=='textwork'", "job=='bar'", event.happened("bar_scene3"), event.once(), priority=3)
    $ event ("bar_scene4", "goingto=='work'", "job=='bar'", event.happened("bar_scene3"), event.once(), priority=1)
    $ event ("bar_scene4_prostitution", "goingto=='textwork'","barprostitution == True", "job=='bar'", event.happened("bar_scene4"), event.once(), priority=1)




    $ event("MrDText_CoffeeShopPickup", "goingto=='messagemr. d'", event.happened("towncoffee3"), event.once(), priority=2)
    $ event("MrDText_Roleplay", "goingto=='messagemr. d'", event.happened("MrDText_CoffeeShopPickup"),event.random(.45), event.once(), priority=2)
    $ event("MrDText_Roleplaymistresskinkcomplete", "goingto=='messagemr. d'", "mistresskinkcomplete == True", event.happened("MrDText_CoffeeShopPickup"),event.random(.45), event.once(), priority=2)
    $ event("MrDText_Roleplaypatientkinkcomplete", "goingto=='messagemr. d'", "patientkinkcomplete == True", event.happened("MrDText_CoffeeShopPickup"),event.random(.45), event.once(), priority=2)
    $ event("MrDText_Roleplaybosskinkcomplete", "goingto=='messagemr. d'", "bosskinkcomplete == True", event.happened("MrDText_CoffeeShopPickup"),event.random(.45), event.once(), priority=2)
    $ event("MrDText_Roleplay2", "goingto=='messagemr. d'", event.happened("MrDText_Roleplay"),event.random(.45), "daycount>30", event.once(), priority=2)
    $ event("MrDText_Roleplay2mistresskinkcomplete", "goingto=='messagemr. d'", "mistresskinkcomplete == True", event.happened("MrDText_Roleplaymistresskinkcomplete"),event.random(.45), event.once(), priority=2)
    $ event("MrDText_Roleplay2patientkinkcomplete", "goingto=='messagemr. d'", "patientkinkcomplete == True", event.happened("MrDText_Roleplaypatientkinkcomplete"),event.random(.45), event.once(), priority=2)
    $ event("MrDText_Roleplay2bosskinkcomplete", "goingto=='messagemr. d'", "bosskinkcomplete == True", event.happened("MrDText_Roleplaybosskinkcomplete"),event.random(.45), event.once(), priority=2)
    $ event("MrDText_Roleplay3", "goingto=='messagemr. d'", event.happened("MrDText_Roleplay2"),event.random(.45),"daycount > 32", event.once(), priority=2)
    $ event("MrDText_Roleplay3mistresskinkcomplete", "goingto=='messagemr. d'", "mistresskinkcomplete == True", event.happened("MrDText_Roleplay2mistresskinkcomplete"),event.random(.45), event.once(), priority=2)
    $ event("MrDText_Roleplay3patientkinkcomplete", "goingto=='messagemr. d'", "patientkinkcomplete == True", event.happened("MrDText_Roleplay2patientkinkcomplete"),event.random(.45), event.once(), priority=2)
    $ event("MrDText_Roleplay3bosskinkcomplete", "goingto=='messagemr. d'", "bosskinkcomplete == True", event.happened("MrDText_Roleplay2bosskinkcomplete"),event.random(.45), event.once(), priority=2)
    $ event("MrDText_GhostedEND", "goingto=='messagemr. d'", "mistresskinkcomplete == True","patientkinkcomplete == True","bosskinkcomplete == True", event.solo(), priority=1)
    $ event("MrDText_Ghosting", "goingto=='messagemr. d'", event.solo(), priority=3)


    $ event("MattText_SayingHi", "goingto=='messagematt'", event.random(.50), event.once(), priority=2)
    $ event("MattText_Sociology", "goingto=='messagematt'", event.random(.50), event.once(), priority=2)
    $ event("MattText_MaidPhoto", "mattchain > 1", "goingto=='messagematt'", event.random(.50), event.once(), priority=2)
    $ event("MattText_MidnightMusic", "daypart=='Dusk'", "mattchain > 1", "goingto=='messagematt'", event.random(.40), event.once(), priority=2)
    $ event("MattText_20Questions", "mattchain > 1", "goingto=='messagematt'", event.random(.50), event.once(), priority=2)
    $ event("MattText_Busy", "goingto=='messagematt'", event.solo(), priority=2)
    $ event("MattText_Busy2", "goingto=='messagematt'", event.solo(), priority=1)


    $ event("kate_phone_short1", "katerelate=='friend'", "TextCheck==True", "job=='cafe'", event.happened("kate_intro"), event.random(.33), event.once(), priority=100)
    $ event("kate_phone_short2", "katerelate=='friend'", "TextCheck==True", "job=='cafe'", event.happened("kate_intro"), event.random(.33), event.once(), priority=100)

    $ event("kate_phone_short3", "katerelate=='friend'", "TextCheck==True", "job=='cafe'", "goingto=='textbed'", event.happened("kate_intro"), event.random(.33), event.once(), priority=100)
    $ event("kate_phone_short4", "katerelate=='friend'", "TextCheck==True", "job=='cafe'", "goingto=='textbed'", event.happened("kate_intro"), event.random(.33), event.once(), priority=100)
    $ event("kate_phone_short5", "katerelate=='friend'", "TextCheck==True", "job=='cafe'", "goingto=='textbed'", event.happened("kate_intro"), event.random(.33), event.once(), priority=100)

    $ event("kate_phone_short6", "katerelate=='friend'", "TextCheck==True", "job=='cafe'", "goingto=='textschool'", "workday==True", event.happened("kate_intro"), event.random(.33), event.once(), priority=100)
    $ event("kate_phone_short7", "katerelate=='friend'", "TextCheck==True", "job=='cafe'", "goingto=='textschool'", "workday==True", event.happened("kate_intro"), event.random(.33), event.once(), priority=100)
    $ event("kate_phone_short8", "katerelate=='friend'", "TextCheck==True", "job=='cafe'", "goingto=='textschool'", "workday==True", event.happened("kate_intro"), event.random(.33), event.once(), priority=100)
    $ event("kate_phone1", "katerelate=='friend'", "TextCheck==True", "goingto=='textbed'", "job=='cafe'", event.happened("kate_intro"), event.random(.33), event.once(), priority=100)
    $ event("kate_phone2", "katerelate=='friend'", "TextCheck==True", "goingto=='textwork'", "job=='cafe'", event.happened("kate_intro"), event.random(.33), event.once(), priority=100)

    $ event("KateText_GardenParty", "goingto=='messagekate'", event.happened("kate_picked_on"), event.random(.50), event.once(), priority=1)
    $ event("KateText_TVShow", "goingto=='messagekate'", event.happened("kate_ice_cream"), event.random(.50), event.once(), priority=1)
    $ event("KateText_CantSleep", "goingto=='messagekate'", "katerelate=='girlfriend'", event.happened("kate_stands_up"), event.random(.50), event.once(), priority=1)
    $ event("KateText_Weather", "goingto=='messagekate'","katerelate=='girlfriend'", event.happened("kate_stands_up"), event.random(.50), event.once(), priority=1)
    $ event("KateText_PenguinSurprise", "goingto=='messagekate'","katerelate=='girlfriend'", event.happened("kate_stands_up"), event.random(.50), event.once(), priority=1)
    $ event("KateText_Busy1", "goingto=='messagekate'", "acts >= 2", event.happened("kate_intro"), event.solo(), priority=99)
    $ event("KateText_Busy2", "goingto=='messagekate'", event.happened("kate_intro"), event.solo(), priority=99)



    $ event("damien_phone2", "goingto=='textbed'", "TextCheck==True", event.happened("damienmovie"), "damientelloff==False", event.once(), priority=1)
    $ event("damien_phone3", "goingto=='textschool'", "TextCheck==True", event.happened("damienlunch"), "damientelloff==False", event.random(.52), event.once(), priority=100)

    $ event("DamienText_Dentist", "goingto=='messagedamien'", event.happened("damienlunch"), event.random(.50), event.once(), priority=1)
    $ event("DamienText_FunFact", "goingto=='messagedamien'", event.happened("damienlunch"), event.random(.50), event.once(), priority=1)
    $ event("DamienText_Lunch", "goingto=='messagedamien'", event.happened("damienmovie"), event.random(.50), event.once(), priority=1)
    $ event("DamienText_VideoGames", "goingto=='messagedamien'", event.happened("damien_mall"), event.random(.50), event.once(), priority=1)
    $ event("DamienText_TurtleVideo", "goingto=='messagedamien'", event.happened("damien_boardgame"), event.random(.50), event.once(), priority=1)
    $ event("DamienText_Busy", "goingto=='messagedamien'", event.happened("damienlunch"), event.solo(), priority=3)
    $ event("DamienText_Busy2", "goingto=='messagedamien'", event.solo(), priority=3)


    $ event("violet_phone1", "TextCheck==True", "day<6", "goingto=='textbed'", event.happened("schoolfriends01"), event.random(.33), event.once(), priority=100)
    $ event("violet_phone2", "TextCheck==True", "goingto=='textschool'", "violetscenes>5", event.random(.33), event.once(), priority=100)
    $ event("violet_phone3", "TextCheck==True", "goingto=='textwork'", event.happened("violetwork1"), event.random(.33), event.once(), priority=100)
    $ event("VioletText_FacialRec", "goingto=='messageviolet'", event.random(.50), event.once(), priority=1)
    $ event("VioletText_Prague", "goingto=='messageviolet'", event.random(.50), event.once(), priority=1)
    $ event("VioletText_LookBetterDom",  "violetrelate=='Dom'", "violetdateflag == True", "goingto=='messageviolet'", event.random(.50), event.once(), priority=1)
    $ event("VioletText_Bitch",  "violetrelate=='Dom'", "violetdateflag == True", "goingto=='messageviolet'", event.random(.50), event.once(), priority=1)
    $ event("VioletText_BubbleBath",  "violetrelate=='Dom'", "violetdateflag == True", "goingto=='messageviolet'", event.random(.50), event.once(), priority=1)
    $ event("VioletText_WouldYouRather",  "violetrelate=='Dom'", "violetdateflag == True", "goingto=='messageviolet'", event.random(.50), event.once(), priority=1)
    $ event("VioletText_PublicMasturbation", "violetrelate=='Sub'", "violetdateflag == True", "goingto=='messageviolet'", event.random(.50), event.once(), priority=1)
    $ event("VioletText_BathroomPhoto", "violetrelate=='Sub'", "violetdateflag == True", "goingto=='messageviolet'", event.random(.50), event.once(), priority=1)
    $ event("VioletText_ButtplugShopping", "violetrelate=='Sub'", "violetdateflag == True", "goingto=='messageviolet'", event.random(.50), event.once(), priority=1)
    $ event("VioletText_PickyClothes", "violetrelate=='Sub'", "violetdateflag == True", "goingto=='messageviolet'", event.random(.50), event.once(), priority=1)
    $ event("VioletText_Busy", "goingto=='messageviolet'", event.solo(), event.once(), priority=3)
    $ event("VioletText_Busy2", "goingto=='messageviolet'", event.solo(), priority=3)


    $ event("notextmessage","goingto=='textschool'","TextCheck==True",event.solo(),priority=50)
    $ event("notextmessage","goingto=='textbed'","TextCheck==True",event.solo(),priority=50)
    $ event("notextmessage","goingto=='textwork'","TextCheck==True",event.solo(),priority=50)



    $ event("dream1", "goingto=='bed'", event.random(.50), event.once(), priority=99)
    $ event("katedream", "goingto=='bed'", "katedream == True", "persistent.feet == True", "persistent.yuri == True", event.once(), priority=99)
    $ event("violetdream01", "goingto=='bed'", "violetscenes == 2", "persistent.yuri == True", "persistent.femdom == True", "persistent.spanking == True", event.random(.55), event.once(), priority=99)
    $ event("mona_dream_scene", "goingto=='bed'", event.random(.55), "corruption > 10", "persistent.tentacles ==True", event.once(), priority=99)
    $ event("misty_dream_scene", "goingto=='bed'", "persistent.femdom == True", "persistent.yuri == True", event.random(.55), event.happened("kate_stands_up"), event.once(), priority=99)
    $ event("huhndoener_dream_scene", "goingto=='bed'", "persistent.multiplepairings == True", "persistent.anal == True", event.random(.55), event.happened("damienmovie"), event.once(), priority=99)
    $ event("monsi7_dream_scene","goingto=='bed'", "persistent.yuri == True", event.random(.55), event.happened("kate_stands_up"), event.once(), priority=99)
    $ event("ruby_chelseas_magical_dream", "goingto=='bed'", "persistent.yuri == True", "persistent.tentacles == True", "persistent.futa == True", "persistent.anal == True", event.random(.55), event.once(), priority=99)
    $ event("rubyrose_videogame", "corruption > 15", "goingto=='bed'", "persistent.degradation == True", "persistent.exhibition == True", event.random(.55), event.once(), priority=99)
    $ event("dradonus_violetparty", "goingto=='bed'","persistent.femdom == True", "persistent.submission == True", "persistent.exhibition == True", "persistent.spanking == True", "persistent.yuri == True", event.happened("violetdom3_date"), event.random(.55), event.once(), priority=99)
    $ event("GaMa", "goingto=='bed'", "catcalltouching==True", "persistent.multiplepairings == True", event.random(.55), event.once(), priority=99)
    $ event("PandoraReed", "goingto=='bed'", "violetrelate=='Dom'","persistent.femdom == True","persistent.futa == True", event.happened("violetdom2"), event.random(.55), event.once(), priority=99)
    $ event("dream_command_unit", "goingto=='bed'","persistent.anal == True", "club=='cheer'", event.random(.50), event.once(), priority=99)
    $ event("VioletFuta", "goingto=='bed'","persistent.futa == True","persistent.anal == True", "violetscenes == 8", event.random(.50), event.once(), priority=99)
    $ event("KaraokeThreesome", "goingto=='bed'","persistent.multiplepairings == True", "mattsubmissive == True", "bullytelloff == 1", event.random(.50), event.once(), priority=99)







label genericschool:
    "Nothing exciting happens at school today."
    jump events_end_period



label generictown:
    "You take a short walk around the city, but nothing interesting happens."
    jump events_end_period




label genericworkbakery:
    "You head into work for the day."
    "Other than the boss scrutinizing you, nothing much happened."
    jump events_end_period





label genericworkcafe:
    "You head into work for the day."
    "Nothing much happened."
    jump events_end_period


label notextmessage:
    jump events_end_period
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
