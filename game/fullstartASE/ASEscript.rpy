label start:
    default global_desktop = ""
    stop music fadeout 5.3
    $ clothes, hair = casualwear
    $ quick_menu = "False"
    window hide
    show screen intro1 with fade
    $ renpy.pause(5.0)
    hide screen intro1 with fade
    show screen intro2 with fade
    $ renpy.pause(6.0)
    hide screen intro2 with fade
    show screen intro3 with fade
    $ renpy.pause(6.0)
    hide screen intro3 with fade
    show screen intro4 with fade
    $ renpy.pause(6.0)
    hide screen intro4 with fade
    show screen intro5 with fade
    $ renpy.pause(5.0)
    hide screen intro5 with fade
    show screen intro6 with fade
    $ renpy.pause(3.0)
    hide screen intro6 with fade
    if persistent.freemode == True:
        menu freemode:
            "{size=31}Would you like to play the game in Free Mode? Free Mode allows you to set the number of days that you wish to play until the game ends!{/size}"
            "Yes, I would like to enter Free Mode" if True:
                window auto
                label freenumber:
                    $ daylimit = int(renpy.input("How many number of days would you like to play?", default= daylimit, allow= '0123456789', length=3))
                    $ renpy.pause
                    if daylimit == 0:
                        "It cannot be 0. Nice Try."
                        $ daylimit = 75
                        jump freenumber
                    elif True:
                        pass
            "No, I want to play the game normally." if True:
                pass
    elif True:
        pass
    window auto

label charactername:
    $ day = 7
    show chelsea with fade
    $ tempname = renpy.input("Might be a good time to introduce yourself, huh?", default="Chelsea", length=12)
    $ renpy.pause

    $ tempname = tempname.strip()

    if tempname == "":
        $ tempname = "Chelsea"

    menu:
        "[tempname]. Is this the name that you go by?"
        "Yes, of course!" if True:

            $ pcname = Character(tempname, image = "chelsea")

            "Alright, [pcname] it is!"

            hide chelsea with dissolve
        "No, I made a mistake!" if True:

            jump charactername

    if pcname == "Airi" or pcname == "Denki Airi":
        $ unlock_ach(airi)

    if persistent.introseen == True:
        menu skipintro:
            "Would you like to skip the introduction?"
            "Yes." if True:
                $ daycount +=1
                menu skipintrochoosejob:
                    "Choose your job."
                    "Bakery." if True:
                        $ job = "bakery"
                    "Cafe." if True:
                        $ job = "cafe"
                menu skipintromatt:
                    "How did you react to Matt?"
                    "Stop him." if True:
                        $ mattsubmissive = False
                        menu:
                            "How did you deal with Matt?"
                            "Slapped Him!" if True:
                                $ mattslap = 1
                                pass
                            "Screamed." if True:
                                pass
                    "Let him grope you." if True:
                        $ mattsubmissive = True
                        $ mattchain = 1
                        $ corruption += 1
                "It sounds like you had quite an interesting first day!"
                "But tomorrow is when things really begin."
                $ day = 2
                jump fullstart
            "No." if True:
                pass
    elif True:
        pass
    scene bg HomeN with fade
    $ renpy.block_rollback()
    "You just finished putting the rest of your stuff away, and have decided to relax on the nice, warm, and comfy couch."
    show chelsea happy at right with moveinright
    pcname "*Yawn*"
    show chelsea blank
    pcname "Ugh, I can't believe I start school tomorrow..."
    play sound PhoneVibration
    "Your phone vibrates."
    call veronicaPhone1 from _call_veronicaPhone1

    show chelsea sad at left with moveinleft
    "Tears prick your eyes."
    pcname "It's just too hard talking to her after everything..."
    show chelsea confused
    "Your thoughts are interrupted by a knock on the door."
    pcname @ blank "Just a minute!"
    "You glance around the room, wondering who could possibly be knocking. What if they're going to rob you?"
    show chelsea confused
    "Would they knock? Probably not... But what if it's just to get you to open the door?"
    show chelsea shocked
    "No forced entry and the police might not believe you were robbed at all!"
    "Should you hide? Grab a weapon?"
    "Voice" "[pcname]? I'm the landlord."
    show chelsea happy
    "Relief floods you; his voice {i}does{/i} sound like the man you spoke to about the apartment."
    show chelsea embarrassed
    "You unlock the door and open it with a sheepish smile."
    show LL Happy at right with moveinright
    "Landlord" "Well hello there. It's nice to finally meet you."
    pcname "Yeah, sorry, I was just..."
    "You pause, trying to think up a good excuse, but he just laughs."
    show chelsea happy
    show LL Neutral
    "Landlord" "I understand. You're all alone here, right? I don't blame you for being cautious."
    show chelsea blank
    show LL Disappoint
    "Landlord" "Sorry for coming by so late. I just wanted to make sure you got settled in all right."
    menu landlord_settled:
        "No problem!" if True:
            show chelsea happy
            show LL Happy
            "Landlord" "Great. I'd like to go over a few things with you quick then."
        "I was going to bed, actually." if True:
            "Landlord" "Sorry about that. I'll try to make this quick."
    show chelsea blank
    show LL Serious
    "Landlord" "As we discussed, rent is $[rent]."
    "Landlord" "It's due promptly the first of every month. I'll come by to pick it up in the morning."
    show LL Neutral
    "Landlord" "We have a waiting list for these apartments, so we don't tolerate missing or late payments."
    "Landlord" "If you can't pay on time, you'll be evicted."
    show LL Blank
    "You nod; you had to pay first month's rent and a security deposit before you moved in."
    show LL Serious
    "Landlord" "I expect to find the place reasonably clean when I come for rent, and you already know we don't allow pets."
    show LL Blank
    "You nod again. This was all in the lease you signed."
    show LL Happy
    "Landlord" "Great. If anything breaks, feel free to call me anytime."
    show chelsea happy
    pcname "Thanks!"
    "He smiles, looking around the room one last time."
    show chelsea blank
    "Landlord" "All right, then I'll see you next month, [pcname]."
    hide LL Happy with moveoutright
    pcname "Ugh, I should get to bed. Tomorrow's my first day of school in over a year."
    pcname "Wouldn't want to oversleep..."
    hide chelsea with moveoutleft
    scene bg RoomN
    $ clothes = 'naked'
    show chelsea at right with moveinleft
    "Walking to the bedroom, you strip off your clothes and slip into bed."
    "It's still strange - even after a year - not to hear the sounds of your parents moving about as you try to sleep."
    "The unfamiliar room, the silence... It's hard to sleep, but eventually you do."
    hide chelsea with dissolve
    scene bg RoomN with fade
    jump endday

label fullstart:
    show screen player_stats()
    call wakeup from _call_wakeup
    return


label laptop:
    call screen laptop

label homework:
    if havehomework:
        if completehomework == True:
            "You've already done your homework!"
            jump laptop
        elif completehomework==False and acts == 4 and day < 6:
            "There's no time to do your homework before school!"
            jump laptop
        elif completehomework == False and acts >0:
            if workday == True and wenttowork == False and skippedwork == False and daycount > 1:
                "You don't have time to do your homework right now. It's almost time for your shift to start!"
                jump laptop
            "You begin working on your homework."
            $ homeworkgirls = True
            if intelligence >= 40:
                $ acts += 1
                "It was extremely easy and you finish it quickly."
            elif intelligence > 30 and intelligence < 40:
                "It takes you some time, but you finish it soon enough."
            elif intelligence < 30 and intelligence > 20:
                "You don't remember how to answer some of the questions in the homework, it takes you a while, but with the help of the internet you finish it."
            elif intelligence < 20:
                "You struggle with the questions as you hardly know how to answer any of them. Still, you're determined to finish it, and with the help of the internet you manage to do so."
                "Even if it did take you a few hours."
            elif True:
                pass
            $ acts -= 1
            call dayparteval from _call_dayparteval
            $ completehomework = True
            jump laptop
        elif completehomework== False and acts == 0:
            "You're too tired to do your homework."
            jump laptop

        if daycount == 1:
            "You open your laptop and begin working on your homework."
            "It was extremely easy and you finish it quickly."
            $ completehomework = True
            jump laptop
    elif True:
        "You don't have any homework."
        jump laptop

label home2:
    if acts == 4:
        scene bg HomeE
    elif acts == 2 or acts == 3:
        scene bg HomeD
    elif acts == 1:
        scene bg HomeE
    elif acts == 0:
        scene bg HomeN

    call screen home2()
    jump home2

label room2:
    if acts == 4:
        scene bg RoomE
    elif acts == 2 or acts == 3:
        scene bg RoomD
    elif acts == 1:
        scene bg HomeE
    elif acts == 0:
        scene bg RoomN

    if bought_room == ("Basic", "Eco", "Elegant", "Girly", "Goth", "Kawaii", "Sporty"):
        $ unlock_ach(bed)

    call screen room2()

    jump room2

label city2:
    scene map
    if persistent.shortcutmsg == False:
        show bg black with dissolve
        "You can press b on the keyboard to quickly travel back to the bedroom."
        $ persistent.shortcutmsg = True
        hide bg black with dissolve
    if catfood <= 50 and foodmessage == 1:
        show bg black with dissolve
        "Looks like [kittenname]'s food bowl is starting to get low. Might need to pick up more catfood soon."
        $ foodmessage +=1
    if catfood <= 1 and foodmessage == 2:
        show bg black with dissolve
        show Cat Sad at catleft
        "Mew!"
        "[kittenname] paws at the foodbowl. Time to buy the cat more catfood!"
        $ cathungry += 1
        hide Cat Sad with dissolve
        hide bg black with dissolve
    if cathungry == 7:
        show bg black with dissolve
        $ foodmessage = 0
        "It seems that after not being fed for so long [kittenname] has run away."
        hide bg black with dissolve
    call screen townmap() with dissolve
    jump city2

label bed2:
    if acts > 1:
        "It's too early to go to bed!"
        jump room2
    elif True:
        scene bg RoomN
        show black with dissolve
        $ goingto = "textbed"
        $ TextCheck = True
        call events_run_period from _call_events_run_period_5
        $ TextCheck = False
        $ goingto = "bed"
        stop music fadeout 3.6
        "Eventually, you fall asleep."
        call events_run_period from _call_events_run_period_1
        call eventengine from _call_eventengine

label wakeup:

    if catadopt == True:
        $ catstuff = renpy.random.randint(1,5)
        $ catfood -= 15
    $ renpy.block_rollback()
    scene bg RoomE with fade
    $ daycount += 1
    if cheatmode == False:
        if intelligence > 39:
            $ gradesday += 1
        if gradesday > 29 and daycount > 29:
            $ unlock_ach(aplus)
            $ gradesday = 30
        if Cash >= 1000:
            $ unlock_ach(wallet)
        if Cash >= 2000:
            $ unlock_ach(piggy)
        if Cash >= 6000:
            $ unlock_ach(rich)
        if corruption >= 100:
            $ unlock_ach(corrupt)
    call dayeval from _call_dayeval
    "[morning]"
    if daycount == 1:
        show chelsea at right with moveinright
        pcname "Mmmmnn..."
        show chelsea confused
        pcname "*Yawn* What time is it?"
        show chelsea blank
        "You look at the clock. It's 7AM."
        pcname @ confused "Maybe... five more minutes?"
        pcname "No! I need to get up. Ugh, if I can."
        "After a few minutes of trying - and failing - to force your weary body out of bed, you finally stand up."
        pcname @ shocked "Oh right, the school uniform..."
        hide chelsea with moveoutright
        "After a few minutes of searching, you find a box that says \"East Uni High.\""
        "Soon, you're dressed. You grab your backpack and you're ready to go."
        $ clothes = 'school'
        show chelsea happy at right with moveinright
        pcname "I don't want to be late!"
        hide chelsea with dissolve
        show screen player_stats()

        jump room2
    if daycount < daylimit:

        call newday from _call_newday
    elif daycount >= daylimit:
        scene bg black with fade
        scene bg EndGame with dissolve
        pause 3.0
        $ persistent.freemode = True
        show powerout with dissolve
        "You've reached the end of the current build! Congrats!"
        "Thank you for playing Uni. We hope that you've enjoyed what there is so far!"
        "It's taken a long time getting this far, but we've enjoyed every step that we've taken and will continue to take with you, our amazing community, at our backs."
        "Please consider donating to our Patreon so that we can continue developing the game, and adding onto your favorite routes!"
        pause 1.0
        scene bg black with dissolve
        pause 0.9
        $ renpy.full_restart()

label dayeval:
    call calendarcompute from _call_calendarcompute
    call dayparteval from _call_dayparteval_1
    if day > 7:
        $ coffeeflag = False
        $ day = 1
    if day == 1:
        $ clubday = False
        $ schoolday = True
        $ workday = True
        $ payday = False
        $ dayname = "Monday:"
    elif day == 2:
        $ clubday = False
        $ schoolday = True
        $ workday = True
        $ payday = False
        $ dayname = "Tuesday:"
    elif day == 3:
        $ clubday = False
        $ schoolday = True
        $ workday = True
        $ payday = False
        $ dayname = "Wednesday:"
    elif day == 4:
        $ clubday = False
        $ schoolday = True
        $ workday = True
        $ payday = False
        $ dayname = "Thursday:"
    elif day == 5:
        $ clubday = False
        $ schoolday = True
        $ workday = True
        $ dayname = "Friday:"
        $ payday = True
    elif day == 6:
        $ clubday = True
        $ schoolday = False
        $ workday = False
        $ payday = False
        $ dayname = "Saturday:"
    elif day == 7:
        $ clubday = True
        $ schoolday = False
        $ workday = False
        $ payday = False
        $ dayname = "Sunday:"
    $ morning = renpy.random.randint(1,5)
    if morning == 1:
        $ morning = "You wake up with a start, but immediately fall back onto your pillows."
    elif morning == 2:
        $ morning = "You wake up and stretch."
    elif morning == 3:
        $ morning = "The sounds of birds singing outside your window wakes you a few minutes before your alarm goes off."
    elif morning == 4:
        $ morning = "Your alarm goes off, startling you."
    elif morning == 5:
        $ morning = "You blink your eyes and look around; it's morning already."
    return

label newday:
    $ goingto = "textwake"
    $ TextCheck = True
    call events_run_period from _call_events_run_period_7
    $ TextCheck = False
    if acts == 4:
        if schoolday and not wenttoschool:
            $ schoolmorning = renpy.random.randint(1,3)
            if schoolmorning == 1:
                pcname "Time for school, I guess..."
            elif schoolmorning == 2:
                pcname "Another day of school..."
            elif schoolmorning == 3:
                pcname "Guess I should get ready to go to school."
        elif not schoolday:
            pcname "It's the weekend! Now, what should I do today?"
        elif not schoolday and alleyscene == 1:
            "While you really don't want to get out of bed today, you do have a club meeting to go to."
            $ alleyscene -= 1
    call dayparteval from _call_dayparteval_4
    if rentdue == True:
        call payrent from _call_payrent
    jump room2

label eventengine:
    if acts > 0:
        if goingto == "school" and not wenttoschool:
            if catadopt == True:
                $ catstuff = renpy.random.randint(1,5)
            $ acts -= 2
        elif goingto == "school" and wenttoschool:
            "School's over for the day!"
            jump city2
        elif goingto == "school" and skippedschool:
            "School's out for the day!"
            jump city2
        if goingto == "work":
            if workday == True and skippedwork == True or wenttowork == True:
                "Your shift is over."
                jump city2
            if schoolday and wenttoschool == False and skippedschool == False:
                "You don't want to be late to school!"
                jump city2
            if workday == False:
                pcname "Today's my day off!"
                jump city2
            elif True:
                $ acts -= 1
                if catadopt == True:
                    $ catstuff = renpy.random.randint(1,5)
                $ wenttowork = True
                $ daysworked += 1
        if goingto == "town":
            if schoolday and wenttoschool == False and skippedschool == False:
                if daycount == 1:
                    "You can't skip your first day of school!"
                    jump schoolevents
                "You can't skip school!"
                jump city2
            elif workday and wenttowork == False and daycount > 1:
                "It's almost time for you to clock into work!"
                jump city2
            elif True:
                $ goingto = "town"
                if catadopt == True:
                    $ catstuff = renpy.random.randint(1,5)
                $ acts -= 1
        if goingto == "club":
            $ wenttoclub = True
            if catadopt == True:
                $ catstuff = renpy.random.randint(1,5)
            $ acts -= 2
        call events_run_period from _call_events_run_period
    if goingto == "bed" and acts <= 1:
        jump endday
    if acts == 0:
        pcname "*Yawn* I'm getting tired. I should probably go to bed..."
        call dayparteval from _call_dayparteval_2
        jump city2
    call dayparteval from _call_dayparteval_3
    return

label endday:

    if skippedschool:
        if havehomework:
            $ intelligence -= 5
        $ intelligence -= 1
    $ acts = 4
    $ day += 1
    $ skippedwork = False
    $ skippedschool = False
    $ wenttoschool = False
    $ wenttowork = False
    $ wenttoclub = False
    $ goingto = ""

    if violetapproval > 10:
        $ violetapproval = 10
    elif violetapproval < 0:
        $ violetapproval = 0
    call events_end_day from _call_events_end_day
    jump wakeup

label dayparteval:
    if acts == 4:
        $ daypart = "Morning"
    if acts == 3:
        $ daypart = "Noon"
    if acts == 2:
        $ daypart = "Afternoon"
    if acts == 1:
        $ daypart = "Dusk"
    if acts < 1:
        $ daypart = "Night"
    return




label splashscreen:
    if renpy.variant("pc"):
        $ renpy.movie_cutscene("movies/HizorGames.mkv")
    elif True:
        pass
    show screen warning
    $ renpy.pause(6.0)
    hide screen warning with fade
    show screen patreon
    show AiriLove at right
    $ renpy.pause(6.0)
    hide AiriLove with dissolve
    hide screen patreon with fade
    scene black with dissolve

    return

label cheattestroomhall:
    "Warning: Using some options in the cheat menu may break the game."
    menu cheatoptions001:
        "Cash" if True:
            menu cheatoptions003:
                "Cash +5" if True:
                    $ Cash+=5
                    jump cheatoptions003
                "Cash +10" if True:
                    $ Cash+=10
                    jump cheatoptions003
                "Cash +50" if True:
                    $ Cash+=50
                    jump cheatoptions003
                "Cash +100" if True:
                    $ Cash+=100
                    jump cheatoptions003
                "Cash +500" if True:
                    $ Cash+=500
                    jump cheatoptions003
                "Return" if True:
                    jump cheattestroomhall
        "Grades" if True:

            menu cheatoptions002:
                "Grades +1" if True:
                    $ intelligence+=1
                    jump cheatoptions002
                "Grades +5" if True:
                    $ intelligence+=5
                    jump cheatoptions002
                "Grades +10" if True:
                    $ intelligence+=10
                    jump cheatoptions002
                "Return" if True:
                    jump cheattestroomhall
        "Club" if True:
            menu cheatoptions004:
                "Track" if True:
                    $ club = "track"
                    jump cheattestroomhall
                "Cheer" if True:
                    $ club = "cheer"
                    jump cheattestroomhall
                "Yearbook" if True:
                    $ club = "yearbook"
                    jump cheattestroomhall
                "Return" if True:
                    jump cheattestroomhall
        "Corruption" if True:
            menu cheatoptions006:
                "Corruption +1" if True:
                    $ corruption+=1
                    jump cheatoptions006
                "Corruption +5" if True:
                    $ corruption+=5
                    jump cheatoptions006
                "Corruption +10" if True:
                    $ corruption+=10
                    jump cheatoptions006
                "Corruption -5" if True:
                    $ corruption-=5
                    jump cheatoptions006
                "Return" if True:
                    jump cheattestroomhall
        "Other" if True:

            menu cheatoptions005:
                "Give Cat" if True:
                    $ catadopt = True
                    jump cheatoptions005
                "Give Catbed" if True:
                    $ catbedbought = True
                    jump cheatoptions005
                "Give Scratching Post" if True:
                    $ catpostbought = True
                    jump cheatoptions005
                "Randomize Cat" if True:
                    $ catstuff = renpy.random.randint(1,4)
                    jump cheatoptions005
                "Return" if True:
                    jump cheattestroomhall
        "Unlock Gallery" if True:
            $ gallery.showAll = True

            "All CGs and backgrounds in the gallery are temporarily unlocked!"

            jump cheatoptions001
        "Return" if True:
            jump home2
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
