$ event("VioletText_NewCar", "goingto=='messageviolet'", event.once(), priority=2)

label VioletText_NewCar:
    call screen TextingScene("Violet",
     [
          TextMessage("[pcname], help me."),
          TextMessage("I'm trying to think of a name for my new car."),
          TextMessage("You got a new car? What happened to the old one?", sender = False),
          TextMessage("It was old, duh."),
          TextMessage("I told you my dad would buy me one. He should really get better at hiding his dirty little secrets."),
          TextMessage("Now look at this bitch."),
          TextMessage("~Image Here~"),
          
          TextMessage("So? What do I call her?"),
          TextMessage("You could name it... Hmmm...", sender = False),
          TextMessage("No wait. Shut up. I have the perfect idea."),
          TextMessage("Her name is Lydia."),
          TextMessage("Anyway, I need to show her off. Later."),
     ])
jump textevent_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
