
label bar:
    scene bg Bar with fade
    stop music fadeout 3.6
    $ goingto = "work"
    $ clothes = "bar"

    call generatebartips from _call_generatebartips
    call eventengine from _call_eventengine_7

    "Today you made $[tips] in tips!"

    $ Cash += tips
    if payday:
        $ paychecktotal = 20 * daysworked

        "Before you left work, you picked up your paycheck."
        "You made [paychecktotal] dollars!"

        $ Cash += paychecktotal
        $ daysworked = 0

    $ goingto = "textwork"
    $ TextCheck = True

    call events_run_period from _call_events_run_period_8

    $ TextCheck = False

    jump city2

label generatebartips:
    $ tips = renpy.random.randint(20, 50)
    return

label bar_random01:
    show chelsea at right with moveinright
    "You head into work just in time for the beer shipment to arrive."
    show chelsea shocked
    "You spend thirty minutes helping him unload the truck before you realize they sent the wrong shipment of beer."
    show chelsea blank
    "By the time Daniel finds out about it, the driver is long gone."
    "You end up using the beer you have, but your customers aren't very happy about it."
    jump events_end_period

label bar_random02:
    show chelsea shocked at right with dissolve
    "You head into work to find the bar is packed."
    "It's a busy night, and by the end of it you have to stay late to clean up all of the sticky tables and chairs."
    show chelsea happy
    "At least you earned some nice tips!"
    $ varrandomcash = renpy.random.randint(2,10)
    $ tips += varrandomcash
    jump events_end_period

label bar_random03:
    show chelsea at right with moveinright
    "You head into work and start your shift."
    show GCBoy with dissolve
    "About halfway through, a group of young men walk up to the bar."
    show chelsea confused
    "As they place their orders, one of them flashes you an ID. It's fake."
    show chelsea blank
    menu bar_fakeid:
        "Let it slide." if True:
            $ corruption += 1
            show chelsea happy
            "Deciding to let it go, you give them a placid smile and start on their orders."
            show chelsea blank
            "It's not like a little alcohol will hurt them, after all."
            hide GCBoy with dissolve
        "Refuse to serve him." if True:
            $ corruption -= 1
            show chelsea angry
            "You look over the ID with a frown. There's no way you can serve them. If something happens, you could go to jail!"
            if club == "track":
                pcname "Hey, I can't take this. It's fake."
            elif club == "cheer":
                pcname "Sorry guys, I can't serve you. This is fake."
            elif club == "yearbook":
                pcname "I-I can't accept this. I'm sorry. It's fake."
            show chelsea confused
            "Fake ID Guy" "No it's not! I just got this last week!"
            show chelsea blank
            "You lift the ID for them to see and poke the edges of the card with your thumb nail. It peels apart easily."
            "The guys give each other uneasy looks before walking out of the bar, grumbling amongst themselves."
            hide GCBoy with dissolve
            "At least they didn't try to put up much of a fight."
    jump events_end_period

label bar_random04:
    show chelsea at right with moveinright
    "You head into work and start your shift."
    "Near the end of the night, you notice a pretty drunk man at the end of the bar waving you down. It looks like he might have downed some other customer's glasses while they weren't looking."
    show chelsea happy
    pcname "What can I do for you, sir?"
    "Drunk" "I want- I want another! Fill me up!"
    "He slams down the empty pint in front of you."
    menu bar_drunk:
        "Cut him off." if True:
            show chelsea blank
            "He's clearly past his drinking limit, and a few glances from other customers tell you they're uncomfortable with him having more."
            if club == "track":
                pcname "Hey man, I have to cut you off. You want water or a soda or something?"
            elif club == "cheer":
                pcname "I can't do that. I can get you some water or soda, though."
            elif club == "yearbook":
                show chelsea embarrassed
                pcname "I-I'm sorry, I need to... to cut you off... Do-Do you want some water?"
            "He scoffs, clearly offended."
            show chelsea confused
            "Drunk" "I'm not {i}drunk!{/i} I just want-"
            "He stops to hiccup."
            show chelsea blank
            "Drunk" "I want another glass! I'm {i}paying{/i} you, aren't I?!"
            show chelsea happy
            pcname "Why don't I call you a cab?"
            "Drunk" "{i}No!{/i} I don't need a cab, I need a fucking {i}drink!{/i}"
            show chelsea blank
            "Seeing that he isn't going to get through to you, the man stumbles off of his stool and makes his way toward the door."
            "He collapses against a set of chairs on his way out and can't find the balance to stand up."
            "You call him a cab and a couple of kind customers help him get into it once the vehicle arrives."
            "At least you know he'll be getting home safely."
        "Indulge him." if True:
            "While he seems to be past his limit, he isn't hurting anyone..."
            "You grab him another drink, making sure to water it down heavily before handing it over."
            "He drinks it down happily, too drunk to notice. Hopefully that will sober him up."
    jump events_end_period

label bar_random05:
    show chelsea shocked at right with moveinright
    "You head into work and notice that the bar is packed."
    show chelsea blank
    "As you rush between customers, you can't help but feel like you're being watched."
    "You try to ignore it and focus on not spilling the pints of beer in your hands."
    show chelsea happy
    pcname "Enjoy!"
    show chelsea shocked
    "When you bend over to set the beer down, you feel a rough hand snake around the front of your bodice and cup your breast. It gives a hard squeeze."
    "Bar Customer" "Mmm... Just as firm as I'd hoped..."
    menu bar_grope:
        "Confront him." if True:
            $ corruption -= 2
            show chelsea angry
            "You whirl around to face him, angry and embarrassed. You push his hand away from your body."
            if club == "track":
                pcname "Hands off!"
            elif club == "cheer":
                pcname "Don't touch me, pervert!"
            elif club == "yearbook":
                pcname "D-don't touch me like that! P-Please..."
            "He laughs. It only infuriates you further."
            "Bar Customer" "Sure, sure. I got what I wanted today anyway."
            "He gives you a wink before walking back to his table across the room."
            show chelsea blank
            "Despite how busy it is, you're heavily distracted the rest of your shift and end up keeping an eye on him for most of the night."
        "Spill beer on him." if True:
            $ corruption -= 1
            show chelsea angry
            "You whirl around to face him, angry and embarrassed. A pint of beer shakes in your hand."
            "Without thinking, you dump the pint onto him."
            if club == "track":
                pcname "Get your hands off of me!"
            elif club == "cheer":
                pcname "Don't touch me, you creep!"
            elif club == "yearbook":
                show chelsea embarrassed
                "Your eyes widen in fear as you realize what you've done."
                pcname "I-I'm so sorry... B-But you shouldn't have-"
            "Bar Customer" "You're going to regret that, bitch!"
            "The customer storms off across the bar. For a moment you think he's going to leave, but then you see him approach Daniel."
            show chelsea sad
            "Daniel approaches and leads you to the back of the bar to chew you out."
            "In the end, Daniel takes $50 out of your paycheck to pay for damages, and you have to formally apologize to the customer."
            "Lost $50."
            $ Cash -= 50
        "Let it happen." if True:
            $ corruption += 1
            "You freeze for a moment, shocked."
            "The guys at your table snicker as your assailant reaches around to grab your other breast as well."
            "You try to ignore his movements and give your table an awkward smile as you continue setting beer around the table. His hands give your breasts a final squeeze before pulling away."
            "When you turn around, he's already gone into the crowd."
            show chelsea blank
            "While you didn't get to confront him, the men at your table seems to enjoy the show and tip you well for it!"
            "Gained $20!"
            $ Cash += 20
    jump events_end_period
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
