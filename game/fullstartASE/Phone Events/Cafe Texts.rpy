label MrDText_CoffeeShopPickup:
    call screen TextingScene("Mr. D",
     [
          TextMessage("I guess I should pick up where we left off. :)", sender = False),
          TextMessage("I squirm as you rub against my panties in the coffee shop.", sender = False),
          TextMessage("I slip my fingers in and stroke the outside of your pussy from across the table."),
          TextMessage("I put one finger in. Two. Three. I'm stroking you inside, one finger at a time."),
          TextMessage("How does that feel, baby? Are you touching yourself?"),
          TextMessage("So good... And yeah, I am.", sender = False),
          TextMessage("Good. Don't stop. Pretend it's my fingers slamming into your wet little cunt."),
          TextMessage("I grab your hand and grind against it while you slam your fingers into me.", sender = False),
          TextMessage("Oh fuck yeah. I pull my cock out under the table and start stroking myself."),
          TextMessage("I reach over and play with your head while you finger me.", sender = False),
          TextMessage("I'm getting my precum all over your hands."),
          TextMessage("I wrap your hand around my cock and hump into it while my other hand strokes your clit."),
          TextMessage("Are you soaked yet, baby? Tell me all about it."),
          TextMessage("I am. My panties are soaked.", sender = False),
          TextMessage("Tell me more."),
          TextMessage("They're soaked through. I feel it dripping through my panties and down my legs...", sender = False),
          TextMessage("I'm so ready for you. I need you in me now...", sender = False),
          TextMessage("Tell me you're cumming."),
          TextMessage("I'm cumming! Just from your fingers deep inside of me, I'm cumming...!", sender = False),
          TextMessage("Fuck, there's cum all over my pants now haha."),
          TextMessage("Text me again when you're up for another round. ;)"),
     ])

    jump textevent_end




label MrDText_Roleplaymistresskinkcomplete:
    jump MrDText_Roleplay
label MrDText_Roleplay2mistresskinkcomplete:
    jump MrDText_Roleplay2
label MrDText_Roleplay3mistresskinkcomplete:
    jump MrDText_Roleplay3
label MrDText_Roleplaypatientkinkcomplete:
    jump MrDText_Roleplay
label MrDText_Roleplay2patientkinkcomplete:
    jump MrDText_Roleplay2
label MrDText_Roleplay3patientkinkcomplete:
    jump MrDText_Roleplay3
label MrDText_Roleplaybosskinkcomplete:
    jump MrDText_Roleplay
label MrDText_Roleplay2bosskinkcomplete:
    jump MrDText_Roleplay2
label MrDText_Roleplay3bosskinkcomplete:
    jump MrDText_Roleplay3
label MrDText_Roleplay:
    if mistresskinkcomplete == True:
        call screen TextingScene("Mr. D",
          [
               TextMessage("Want to sext about the married man and mistress again?", sender = False),
               TextMessage("Not really feeling that today."),
               TextMessage("What if we try some other roleplay? What else are you into?"),
          ])
    elif patientkinkcomplete == True:
        call screen TextingScene("Mr. D",
          [
               TextMessage("Want to sext about the doctor and patient some more?", sender = False),
               TextMessage("Not really feeling that today."),
               TextMessage("What if we try some other roleplay? What else are you into?"),
          ])
    elif bosskinkcomplete == True:
        call screen TextingScene("Mr. D",
          [
               TextMessage("Want to sext about the boss and his assistant some more?", sender = False),
               TextMessage("Not really feeling that today."),
               TextMessage("What if we try some other roleplay? What else are you into?"),
          ])
    elif True:

        call screen TextingScene("Mr. D",
          [
               TextMessage("Want to sext about the coffee shop again?", sender = False),
               TextMessage("Not really feeling that today."),
               TextMessage("What if we try some roleplay? What are you into?"),
          ])

    menu MrD_Roleplay:
        "Married Man and Mistress." if mistresskinkcomplete == False:
            call screen TextingScene("Mr. D",
               [
                    TextMessage("Well... I could always be your mistress. I don't even know if you're actually married.", sender = False),
                    TextMessage("I can be married if you want me to be. ;)"),
                    TextMessage("Won't your wife be mad if she finds out you're taking me on this expensive vacation?", sender = False),
                    TextMessage("So I'm a sugar daddy huh? xD"),
                    TextMessage("Don't you worry about her. This trip is just for you and me. ;)"),
                    TextMessage("I take you out to the balcony where you can see the beach. You're just wearing a tiny see-through slip."),
                    TextMessage("I run my hands over your body, pushing the fabric around while I kiss along your neck."),
                    TextMessage("I tilt my head back and let you kiss me, leaning back so I can rub my ass against your crotch."),
                    TextMessage("I unzip my pants and press my long, hard dick against your ass. I squeeze your cheeks around it while I hump your backside."),
                    TextMessage("My pussy is all wet... It's getting all over that slip.", sender = False),
                    TextMessage("I remove your dress and bend you over against the balcony."),
                    TextMessage("I keep kissing and biting down your back until my tongue is in your pussy. I start slowly outside, then in..."),
                    TextMessage("Yes, baby... Do I taste better than your wife?", sender = False),
                    TextMessage("So much better. You taste fucking amazing. My wife doesn't even compare to your pussy."),
                    TextMessage("I lick you inside and out, my face covered in your cum."),
                    TextMessage("I reach down and rub my clit while you eat me out. I'm so wet down there, just dripping on your face.", sender = False),
                    TextMessage("I slide your dress off and toss it over the balcony before thrusting into you from behind."),
                    TextMessage("Mmm... I hold onto the edge of the balcony railing while you fuck me with your hard dick.", sender = False),
                    TextMessage("Your body is naked, viewable to anyone passing by."),
                    TextMessage("Do you wave to any of them? Do you like how they stare at you getting fucked?"),
                    TextMessage("Yes... I let them look...", sender = False),
                    TextMessage("You don't have a choice. I grab your breasts and squeeze hard while I pound you against the balcony railing."),
                    TextMessage("You're so much younger than my wife, so much more willing to take whatever I give you."),
                    TextMessage("I can fuck you like this for hours and you would still be able to go for more."),
                    TextMessage("Keep going. Keep fucking me for hours, however long you want as long as you keep fucking me!", sender = False),
                    TextMessage("Fuck, baby. You got me too excited this time. I was hoping to hold out a little longer."),
                    TextMessage("You're done already?", sender = False),
                    TextMessage("For now, but give it a little bit. I'll be ready for you again soon and we can pick up where we left off. ;)"),
               ])

            $ mistresskink = True

        "Doctor and Patient." if patientkinkcomplete == False:
            call screen TextingScene("Mr. D",
               [
                    TextMessage("I wouldn't mind being a patient... and you could be my sexy doctor that needs to take care of me. :)", sender = False),
                    TextMessage("What seems to be ailing you, ma'am? ;) I came as soon as I could."),
                    TextMessage("I don't know. My body just feels so hot all of the sudden, and... it's embarrassing...", sender = False),
                    TextMessage("You can tell me. I am a doctor, after all."),
                    TextMessage("I sit beside you on the bed and caress your face."),
                    TextMessage("Well I'm all wet. I feel so warm and wet... down there...", sender = False),
                    TextMessage("I feel like there's this terrible itch that I can't scratch.", sender = False),
                    TextMessage("You'll help me, right?", sender = False),
                    TextMessage("Of course. Let's see here..."),
                    TextMessage("I push your gown aside and start thumbing your clit."),
                    TextMessage("How does that feel?"),
                    TextMessage("Oohh... It feels good, doctor. It feels really, really good.", sender = False),
                    TextMessage("Please don't stop.", sender = False),
                    TextMessage("And how about this?"),
                    TextMessage("I keep rubbing your clit, but I insert a finger inside of you and stroke, watching for your reaction."),
                    TextMessage("My body arches toward you. I can't help it; each time you touch me, I move toward you.", sender = False),
                    TextMessage("I think I know the problem here."),
                    TextMessage("You do?", sender = False),
                    TextMessage("Then please help me, doctor. I feel even more wet... I can't stop...", sender = False),
                    TextMessage("Don't worry, I'll make you feel all better. ;)"),
                    TextMessage("I slide more fingers in, one at a time, stroking the inside of your tight, wet cunt."),
                    TextMessage("My pussy clenches around your hand. I'm whimpering, begging for more."),
                    TextMessage("I slide more fingers in, pumping them in and out of your pussy."),
                    TextMessage("Fuck, the office is calling. G2g."),
                    TextMessage("Wait, right now??", sender = False),
                    TextMessage("Yeah, sorry. Text me again later."),
               ])

            $ patientkink = True

        "Boss and his Assistant." if bosskinkcomplete == False:
            call screen TextingScene("Mr. D",
               [
                    TextMessage("We could pretend that I work for you.", sender = False),
                    TextMessage("Yeah? Maybe you slept your way into a promotion. ;)"),
                    TextMessage("Or I'm the new girl, and you need to welcome me into your office.", sender = False),
                    TextMessage("Lol, you thought this out, didn't you? I like it."),
                    TextMessage("Right this way, miss. Wouldn't want you getting lost on our tour."),
                    TextMessage("Is this your office? It looks so nice.", sender = False),
                    TextMessage("It is, isn't it? I've got a perfect view of the city here."),
                    TextMessage("Although, it doesn't compare to our new intern in the slightest. ;)"),
                    TextMessage("Why don't you come take a look?"),
                    TextMessage("I take your hand and lead you to the window. My hands rest on your waist while you look at the city."),
                    TextMessage("It's beautiful.", sender = False),
                    TextMessage("Your hands feel so warm... I can't believe how cold your office is.", sender = False),
                    TextMessage("Yes, it does get chilly. But allow me to help warm you up even further."),
                    TextMessage("I reach down under your skirt, feeling up your thighs, then your pussy."),
                    TextMessage("Mr. D, this is really inappropriate... What if someone saw?", sender = False),
                    TextMessage("Let them. I can just fire them if they do anything."),
                    TextMessage("You want me, don't you?"),
                    TextMessage("I do... I need you. Really badly. Can't you feel it?", sender = False),
                    TextMessage("Yes, you're already wet through your panties. What a naughty girl."),
                    TextMessage("I didn't know I was hiring a whore for an intern."),
                    TextMessage("I can't help it. You're the reason I applied.", sender = False),
                    TextMessage("I just got so excited looking at you... thinking about you... what you could do to me...", sender = False),
                    TextMessage("There's plenty I would like to do to you. Just you wait. ;)"),
                    TextMessage("I cup your pussy in my hand and stroke your clit with my thumb through the fabric."),
                    TextMessage("My interns don't usually wear thongs to their first day, you know."),
                    TextMessage("I wanted to make sure you knew what I wanted.", sender = False),
                    TextMessage("Brb, meeting to go to."),
                    TextMessage("You don't want to sext during your meeting?", sender = False),
                    TextMessage("Not today, but we'll see. ;)"),
               ])

            $ bosskink = True

    jump textevent_end

label MrDText_Roleplay2:
    if mistresskink == True:
        call screen TextingScene("Mr. D",
          [
               TextMessage("Are you ready to continue?", sender = False),
               TextMessage("Sure. You wanna move inside from the balcony?"),
               TextMessage("That works for me.", sender = False),
               TextMessage("Alright. I turn you around and pick you up, my tongue pushing down your throat while I carry you inside and toss you on the bed."),
               TextMessage("Have you fucked your wife here before?", sender = False),
               TextMessage("Yeah, I used to take her here, but she thinks I sold it. Now I just bring hot little things like you around instead."),
               TextMessage("I throw you down on the bed and roll you onto your stomach. Face down, ass up, I shove myself back into your waiting pussy."),
               TextMessage("My back arches as I take each of your thrusts. I moan loudly, my voice carrying out to the beach.", sender = False),
               TextMessage("So you do want to be heard, huh? ;)"),
               TextMessage("I'm getting a call from my wife. I answer it while I'm dick-deep in your little pussy."),
               TextMessage("Fuck. Can she hear me moaning?", sender = False),
               TextMessage("I shove my hand over your mouth to keep you quiet. She has no idea I have a hot, young piece of ass riding my dick right now."),
               TextMessage("I try to moan loader so she can hear.", sender = False),
               TextMessage("Fuck, you're so naughty."),
               TextMessage("She starts asking about what the noise is. I tell her it's an upset animal while I slam into your pussy."),
               TextMessage("I clench my pussy around you, each inch of you filling me up...", sender = False),
               TextMessage("Lol, you should feel how wet I am right now. I'll need to change my panties after this.", sender = False),
               TextMessage("You shouldn't be wearing panties in the first place. ;)"),
               TextMessage("I set the phone down and let my wife talk while I'm busy fucking you. I hold your arms behind your back so you can't grab the phone."),
               TextMessage("What's she talking about?", sender = False),
               TextMessage("About her way, work, whatever. I keep telling her yes or whatever she wants to hear while I'm pounding away."),
               TextMessage("I want to tell her what a good fuck her husband is. ;)", sender = False),
               TextMessage("I bet you do. ;)"),
               TextMessage("I feel your thighs tighten around me as I finish in you, filling your open pussy with my cum."),
               TextMessage("Now I'm really dripping lol", sender = False),
               TextMessage("Can we keep going? I'm almost there.", sender = False),
               TextMessage("I g2g, but I'll help finish you up later. ;)"),
          ])
    elif patientkink == True:
        call screen TextingScene("Mr. D",
          [
               TextMessage("How was work?", sender = False),
               TextMessage("I'm still at it. Gotta treat my patient right. ;)"),
               TextMessage("I pull my hand back from your wet pussy and stick my fingers in your mouth."),
               TextMessage("Will this help me, doctor?", sender = False),
               TextMessage("Absolutely. Now just lay back and relax, I'll take care of everything."),
               TextMessage("If you say so...", sender = False),
               TextMessage("I lay back on the bed and open wide, sucking on your fingers.", sender = False),
               TextMessage("How do you taste?"),
               TextMessage("Mmmm... Sweeter than I expected.", sender = False),
               TextMessage("Are you tasting yourself right now?"),
               TextMessage("I am.", sender = False),
               TextMessage("Fuck, that's hot. Yeah, keep licking it up. Taste your sweet little pussy all over my fingers."),
               TextMessage("I want to taste you, too."),
               TextMessage("I press my tongue against your cunt and lick slooowly across your slit."),
               TextMessage("Do you think this is helping your mysterious illness?"),
               TextMessage("Yes, but it's making it hard to breathe... And I feel like my body is moving on its own...", sender = False),
               TextMessage("That's just part of the treatment."),
               TextMessage("I stick my tongue in your pussy and eat. you. up."),
               TextMessage("I wish you were here right now so I could see how hard you are.", sender = False),
               TextMessage("Baby you wouldn't just be seeing it, you would be feeling it against your hot little body."),
               TextMessage("I climb over you and rub my crotch against yours. I want you to feel how horny you made me."),
               TextMessage("It's so big, doc. What are you going to do with it?", sender = False),
               TextMessage("I'm going to fuck you until you feel all better. And then maybe some more after, for good measure. ;)"),
               TextMessage("What are you waiting for? I need treatment right away.", sender = False),
               TextMessage("Only you can fix it.", sender = False),
               TextMessage("I take my cock out of my pants and shove it into your dripping pussy."),
               TextMessage("Do you push it all in? Or are you going a little bit at a time?", sender = False),
               TextMessage("All in. I shove myself in until your pussy is tight around me and can't take any more."),
               TextMessage("Yesss, I can feel you in me just filling me up. You feel so good inside of me.", sender = False),
               TextMessage("Doc?", sender = False),
               TextMessage("Doc??", sender = False),
          ])
    elif bosskink == True:
        call screen TextingScene("Mr. D",
          [
               TextMessage("How'd the meeting go, boss? Did you think about me?", sender = False),
               TextMessage("I couldn't stop thinking about you. About all the things I wanted to do to you."),
               TextMessage("I slide my hands along your stockings and hoist you up onto my desk. It's already cleared off and ready."),
               TextMessage("Do you do this sort of thing often with your coworkers?", sender = False),
               TextMessage("Only the really pretty ones. ;)"),
               TextMessage("I slide your skirt up and finger you around the thong, pumping my fingers quickly in and out of your wet pussy."),
               TextMessage("Is this the kind of welcome you wanted?"),
               TextMessage("I can't complain.", sender = False),
               TextMessage("I curl my fingers inside of you, using my thumb to rub at your clit."),
               TextMessage("How wet are you right now?"),
               TextMessage("I'm dripping. Your fingers feel so gooooood.", sender = False),
               TextMessage("Damn right they do."),
               TextMessage("I slowly pull them in and out of your gaping pussy, curling them up inside before sloooowly pulling them back out."),
               TextMessage("Do you like that? Or is that too slow?"),
               TextMessage("Faster... please...", sender = False),
               TextMessage("That's what I like to hear."),
               TextMessage("I ram my fingers into you faster and harder, sliding more of my hand in while I go."),
               TextMessage("My dick is already rock hard just looking at you take my hand. I pull my fingers out and lick the juices away."),
               TextMessage("My body is literally shuddering at the image of that. Fuck...", sender = False),
               TextMessage("Are you going to be a good little intern and take my dick, too? Or was my hand too much for you?"),
               TextMessage("No! I'll take it, please...", sender = False),
               TextMessage("Are you sure? If anyone finds out you fucked your boss, they might say some nasty things about you."),
               TextMessage("I don't care. Please, I just really need you in me...", sender = False),
               TextMessage("Please?", sender = False),
               TextMessage("Hello?", sender = False),
          ])

    jump textevent_end

label MrDText_Roleplay3:
    if mistresskink == True:
        call screen TextingScene("Mr. D",
          [
               TextMessage("Ready to get me off?", sender = False),
               TextMessage("Sure."),
               TextMessage("I throw you down onto your back and hold your hands over your head while I slip back inside of you."),
               TextMessage("If you thought I was done, you're sadly mistaken. ;)"),
               TextMessage("Yesss, fuck me hard!", sender = False),
               TextMessage("My wife hears that. I have to tell her that it's the TV, meanwhile I'm spreading your legs wide for me."),
               TextMessage("I wrap my legs around you and squeeze hard. I want to feel you so deep in me...", sender = False),
               TextMessage("I use a hand to pinch and twist your nipples. Sometimes I lean down to bite and suck them. I have no idea what my wife is talking about anymore."),
               TextMessage("Your hands feel so good, I like how rough you are with me.", sender = False),
               TextMessage("I like how young and tight you are. You can barely fit anymore in you, but I keep going until you're screaming."),
               TextMessage("I move my body with yours, rubbing my clit against you while you fill me up again and again.", sender = False),
               TextMessage("I keep going, more and more and more, your body shuddering against me..."),
               TextMessage("Did you cum?"),
               TextMessage("Yeah, I just finished.", sender = False),
               TextMessage("Cool."),
          ])
        $ mistresskink = False
        $ mistresskinkcomplete = True
    elif patientkink == True:
        call screen TextingScene("Mr. D",
          [
               TextMessage("Hey! Sorry to leave you hanging, I got distracted."),
               TextMessage("I guess I'm not the only patient you're treating, huh?", sender = False),
               TextMessage("I guess you could say that lol"),
               TextMessage("But you're certainly the sexiest right now."),
               TextMessage("I can feel your pussy tightening around my throbbing dick. I grab your hips and pull out slooowly, then thrust back in."),
               TextMessage("I'm rocking you hard against the hospital bed. I love watching your tits bounce."),
               TextMessage("I love feeling you fuck me... and making them bounce... and just pleasuring me as hard as you can.", sender = False),
               TextMessage("You'll need to be quiet in case any of the nurses walk by. I don't think they'd approve of my practice."),
               TextMessage("But you're doing such a good job! I feel better already.", sender = False),
               TextMessage("Maybe we'll just need to ask them to join us instead, right?"),
               TextMessage("Then they'll see what a good doctor I am. ;)"),
               TextMessage("I try to cover my mouth while you fuck me, but you feel so good, I don't know if I can keep it in.", sender = False),
               TextMessage("You better be quiet. I could lose my job... but damn, this pussy would be worth it."),
               TextMessage("I push your legs up to your chest and slam into you. I want your body to be quaking by the time you cum."),
               TextMessage("You won't have to wait very long! Fuck, I can almost feel you shoving me down and having your way with me.", sender = False),
               TextMessage("Are you gonna cum?"),
               TextMessage("Yes, oh yes!", sender = False),
               TextMessage("Tell me you're cumming. Say it."),
               TextMessage("I'm cumming!!", sender = False),
               TextMessage("Fuck... That was really good...", sender = False),
               TextMessage("Yeah, my bedding is soaked lol."),
               TextMessage("Guess I should put this in the wash."),
               TextMessage("Yeah, probably.", sender = False),
          ])
        $ patientkink = False
        $ patientkinkcomplete = True
    elif bosskink == True:
        call screen TextingScene("Mr. D",
          [
               TextMessage("Are you there?", sender = False),
               TextMessage("Yeah, sorry, got caught up in some stuff."),
               TextMessage("I sit back on my chair and take my hard dick out of my pants. I can't take my eyes off your pussy."),
               TextMessage("Why don't you show me how badly you want it? Come impress your boss."),
               TextMessage("I climb off of the desk and straddle you in your chair, my pussy dripping down through my thong onto your nice pants.", sender = False),
               TextMessage("Careful. You'll have to pay for these if they get ruined."),
               TextMessage("Of course, you can always make it up to me with your body. ;)"),
               TextMessage("I choose the second option.", sender = False),
               TextMessage("Moving my thong to the side, I position myself over your dick and slide down.", sender = False),
               TextMessage("Ahhh fuck, yeah. You're going to be a good member of our team."),
               TextMessage("Gripping your hips, I bounce you up and down on top of me, my dick coated with your wet fluids."),
               TextMessage("I can feel your dick deep inside of me, pounding away...", sender = False),
               TextMessage("Your tits are bouncing nicely through your shirt. I reach over and take one in my mouth through your shirt, biting down."),
               TextMessage("You feel so good. Yes, yes, yessss!", sender = False),
               TextMessage("I slam into your body hard, filling you up with my cum."),
               TextMessage("Are you cumming yet?"),
               TextMessage("Yes, yes, yessss!", sender = False),
               TextMessage("Oh fuck yes. You're so fucking hot."),
               TextMessage("That was good. I'll make sure to keep you on payroll. ;)"),
               TextMessage("Lol, thanks.", sender = False),
          ])
        $ bosskink = False
        $ bosskinkcomplete = True

    jump textevent_end



label MrDText_Ghosting:
    call screen TextingScene("Mr. D",
     [
          TextMessage("Hey, Mr. D", sender = False),
          TextMessage("Mr D?", sender = False),
          TextMessage("Hello?", sender = False),
     ])
    "He must be busy with something."

    jump textevent_end

label MrDText_GhostedEND:
    call screen TextingScene("Mr. D",
     [
          TextMessage("Hey, Mr. D", sender = False),
          TextMessage("Mr D?", sender = False),
          TextMessage("Hello? You there?", sender = False),
     ])
    "After waiting for some time still no reponse. You feel like you may have been ghosted."

    jump textevent_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
