"HOW TO ADD TO CONTACT LIST:"
"To add a contact, you type the following: chelseaContacts.contactsListed['real_name'] = 'nickname'"
"EXAMPLE 1: $ chelseaContacts.contactsListed['Violet'] = 'Violet<3'"
"EXAMPLE 2: $ chelseaContacts.contactsListed['Kate'] = 'Kate'"
"HOW TO DISPLAY TEXT MESSAGES: To display text as a text message, you type the following: call screen TextingScene('real_name', [TextMessage('message')])"
"Example 1 - Displaying One Text Message: call screen TextingScene('Violet', [TextMessage('Hey girl!!!')])"
"Example 2 - Displaying Multiple Messages: call screen TextingScene('Violet', [ TextMessage('Hi Violet', sender = False), TextMessage('Soooooooo'), TextMessage('Remember Felicia from my math class?') ])"
"Example 3 - Displaying an Image Text Message: image tempImage = 'images/testTextImage.png'"
"call screen TextingScene('Violet', [ TextMessage('tempImage', image = True, sender = False), TextMessage('I love it!') ])"
"Example 4 - Displaying an Image Text Message 2: call screen TextingScene('Violet', [ TextMessage('images/testTextImage.png', image = True, sender = False), TextMessage('I love it!') ])"
"Example 5 - Displaying an Image Text Message in Landscape Mode: call screen TextingScene('Violet', [TextMessage('images/TestLandscape.png', sender = True, image = True, landscape = True)])"
"Example 6 - Displaying Text Messages With Choices: call screen TextingScene('Violet', [ TextMessage('It's a waste of money.', sender = False), TextMessage('Wow'), TextMessage('Jealous much?') ])"
"menu violetPhone3Response3: 'What will you say?'"
"'Sorry.': call screen TextingScene('Violet', [ TextMessage('Sorry.', sender = False), TextMessage('It's fine'), TextMessage('I deal with this a lot') ])"
"'Rolling your eyes, you try to be patient with her.'"
"call screen TextingScene('Violet', [ TextMessage('You should see the pics it takes'), TextMessage('Send one', sender = False), TextMessage('After you were so mean?'), TextMessage('Maybe if you're nice I'll send a really cute one later'), TextMessage('Gtg! Update to install'), TextMessage('Cya!', sender = False) ])"
"'With a sigh, you tuck your phone away.'"
"pcname 'She's so spoiled...'"
"jump events_end_period"
"'I gtg.': call screen TextingScene('Violet', [TextMessage('I gtg', sender = False)])"
"'You slide your phone into your pocket.' 'Though it vibrates half a dozen times, you ignore it.'"
"jump events_end_period"
"NOTES: When you want a text message to be Chelsea's, set sender to False."
"When you want a text message to be from the person Chelsea is speaking to, either leave out 'sender', or set sender to True."
"When you want a text message to be an image, set image to True."
"IF YOU ENCOUNTER AN ERROR OR BUG: Let @NocturneLight know in full detail what it was and he will fix it. He clearly screwed something up."

















































































pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.RPY'>>>>

init python:
    class TextMessage:
        
        
        def __init__(self, message, sender = True, image = False, landscape = False):
            self._sender = sender
            self._message = message
            self._image = image
            self._landscape = landscape
        
        
        
        @property
        def sender(self):
            return self._sender
        
        
        @property
        def message(self):
            return self._message
        
        
        
        @property
        def image(self):
            return self._image
        
        
        
        @property
        def landscape(self):
            return self._landscape

    class TextConversation:
        
        
        def __init__(self):
            self._contact = None
            self._nickname = None
            self._textHistory = []
        
        
        @property
        def textHistory(self):
            return self._textHistory
        
        
        @textHistory.setter
        def textHistory(self, list):
            self._textHistory.extend(list)
        
        
        @property
        def contact(self):
            return self._contact
        
        
        @contact.setter
        def contact(self, name):
            self._contact = name
        
        
        @property
        def nickname(self):
            return self._nickname
        
        
        @nickname.setter
        def nickname(self, nickname):
            self._nickname = nickname

    class OngoingTextMessages:
        
        
        def __init__(self):
            self._textLog = []
            self._imageList = []
        
        
        @property
        def textLog(self):
            return self._textLog
        
        
        @textLog.setter
        def textLog(self, convo):
            
            match = False
            
            
            
            convo = getConversation(convo[0], convo[1])
            
            
            
            if len(self._textLog) == 0:
                for text in convo.textHistory:
                    if text.image:
                        self.addImage(text.message)
                
                self._textLog.append(convo)
            
            
            elif len(self._textLog) > 0:
                for i, value in enumerate(self._textLog):
                    if value.contact == convo.contact:
                        match = True
                        
                        
                        
                        self._textLog[i].nickname = convo.nickname
                        self._textLog[i].textHistory = convo.textHistory
                        
                        
                        for text in convo.textHistory:
                            if text.image:
                                self.addImage(text.message)
                        
                        
                        
                        self._textLog.insert(0, self._textLog.pop(i))
                        
                        
                        break
                    else:
                        match = False
                
                
                
                if not match:
                    for text in convo.textHistory:
                        if text.image:
                            self.addImage(text.message)
                    
                    self._textLog.insert(0, convo)
        
        
        @property
        def imageList(self):
            return self._imageList
        
        
        @imageList.setter
        def imageList(self, image):
            self._imageList.append(image)
        
        
        
        def addImage(self, message):
            if self._imageList.count(message) == 0:
                self._imageList.append(message)
        
        
        def getMessageHistory(self, name):
            for conversation in self._textLog:
                if conversation._contact == name:
                    return conversation.textHistory


    class ContactList:
        
        
        def __init__(self):
            self._contactsListed = {}
        
        
        @property
        def contactsListed(self):
            return self._contactsListed
        
        
        @contactsListed.setter
        def contactsListed(self, id, name):
            self._contactsListed[id] = name
        
        
        
        def getKey(self, val):
            keys = list(self._contactsListed.keys())
            values = list(self._contactsListed.values())
            
            return keys[values.index(val)]
        
        
        def updateTextingNames(self, name, nickname):
            
            if len(chelseaTexts.textLog) > 0:
                
                
                for person in chelseaTexts.textLog:
                    if person.contact == name:
                        person.nickname = nickname


    def getConversation(name, convo):
        log = TextConversation()
        _ = chelseaContacts.contactsListed
        
        log.contact = name
        
        if name in _.keys():
            log.nickname = _[name]
        else:
            log.nickname = name
        
        log.textHistory = convo
        
        return log


    def addTextMessage(name, message, sender, image = False, landscape = False):
        chelseaTexts.textLog = (name, [TextMessage(message, sender = sender, image = image, landscape = landscape)])




default chelseaTexts = OngoingTextMessages()



default chelseaContacts = ContactList()



style messageListName:
    color "#ffffff"
    layout "nobreak"
    line_spacing 5
    hover_color "#e9933b"

style messageListMessage:
    color "#ffffff"
    layout "nobreak"
    line_spacing 5
    font "OpenSans-SemiBoldItalic.ttf"

style contactMessage:
    color "#ffffff"
    layout "subtitle"
    font "OpenSans-SemiBoldItalic.ttf"

style contactName:
    color "#ffffff"
    layout "subtitle"
    line_spacing 10

style contactInteract:
    color "#ffffff"
    layout "subtitle"
    hover_color "#e9933b"



transform scaledown(value):
    zoom value

transform movePhone:
    on hide:
        linear 0.3 yalign 25.0
    on show:

        yalign 25.0
        linear 0.3 yalign 0.5

transform appearDisappear:
    on hide:
        linear 0.3 alpha 0
    on show:

        alpha 0
        linear 0.3 alpha 1

transform fastAppearDisappear:
    on show:
        alpha 0
        pause 0.2
        linear 0.1 alpha 1
    on hide:

        alpha 1
        linear 0.1 alpha 0

transform prevMessageMove:
    yanchor -100
    linear 0.2 yanchor 10

transform newMessageAppear:
    parallel:
        yanchor -100
        linear 0.2 yanchor 10
    parallel:
        alpha 0
        linear 0.2 alpha 1

"The phone that can be brought up by the player at any time. Shows the home screen before any other screen."



screen PhoneInterface():

    zorder 100
    modal True tag phone


    add "black" alpha 0.9 at appearDisappear
    add chelseaPhone xalign 0.5 yalign 0.5 at movePhone


    imagebutton auto chelPhoneBack:
        xalign 0.38
        yalign 0.16
        keysym "K_UP"
        action Hide("PhoneInterface") at fastAppearDisappear


    vbox at fastAppearDisappear:
        xalign 0.5
        yalign 0.3
        spacing 10




        hbox:
            imagebutton auto "gui/phoneUI/cameraicon-%s.png":

                action Show("PhoneGallery")

            null width 40

            imagebutton auto "gui/phoneUI/contactsicon-%s.png":

                action Show("Contacts")

            null width 40

            imagebutton auto "gui/phoneUI/messagesicon-%s.png":

                action Show("Messages")


        hbox:
            imagebutton auto "gui/phoneUI/bugicon-%s.png":

                action OpenURL("https://docs.google.com/forms/d/e/1FAIpQLScDPfEZ91ga2AFWpV17K8HvH1dGFRh2bbZyynSzEoBxHG1v2Q/viewform")

"A screen which shows Chelsea's current contacts list. The screen is blank if no contacts have been added."



screen Contacts():

    zorder 100
    modal True tag phone


    add "black" alpha 0.9 at appearDisappear
    add chelseaPhone xalign 0.5 yalign 0.5 at movePhone


    imagebutton auto chelPhoneBack:
        xalign 0.38
        yalign 0.16
        keysym "K_UP"
        action Show("PhoneInterface") at fastAppearDisappear

    frame at fastAppearDisappear:
        background "#00000000"

        xalign 0.5
        yalign 0.5
        xysize (500, 625)

        has viewport:
            draggable True
            mousewheel True

        vbox:

            $ _ = chelseaContacts.contactsListed.values()


            $ _ = sorted(_, key = unicode.lower)


            for contacts in _:
                frame:
                    background "#bc3739"
                    xfill True
                    margin (0, 10, 0, 10)
                    padding (0, -5, 0, -5)

                    textbutton contacts text_style "messageListName" xalign 0.5 action Show("ContactOptions", selectedContact = contacts)

"Displays thumbnails of all the images received through text currently, and lets a user click on one to view the image at its full size."



screen PhoneGallery():

    default imageSelected = (False, "")


    zorder 100
    modal True tag phone


    add "black" alpha 0.9 at appearDisappear
    add chelseaPhone xalign 0.5 yalign 0.5 at movePhone


    imagebutton auto chelPhoneBack:
        xalign 0.38
        yalign 0.16
        keysym "K_UP"
        action Show("PhoneInterface") at fastAppearDisappear

    frame at fastAppearDisappear:
        background "#00000000"

        xalign 0.5
        yalign 0.5
        xysize (500, 625)

        has vbox
        frame:
            background "#00000000"
            xfill True




            ysize 421



            if imageSelected[0]:
                imagebutton:
                    xalign 0.5

                    idle imageSelected[1]
                    action Show("ImageView", chosenImage = imageSelected[1], nickname = None, fromGallery = True)
                    at scaledown(0.46)

        viewport:
            draggable True
            mousewheel "horizontal"


            xinitial 1000000000

            has hbox
            for currentImage in chelseaTexts.imageList:
                frame:
                    background "#00000000"
                    padding (10, 10, 10, 10)




                    ymaximum 204

                    imagebutton:
                        idle currentImage
                        action SetScreenVariable("imageSelected", (True, currentImage))
                        at scaledown(0.185)

"Shows the list of ongoing conversations on Chelsea's phone. This displays the contact's name and the last message to occur in the conversation."



screen Messages():

    zorder 100
    modal True tag phone


    add "black" alpha 0.9 at appearDisappear
    add chelseaPhone xalign 0.5 yalign 0.5 at movePhone


    imagebutton auto chelPhoneBack:
        xalign 0.38
        yalign 0.16
        keysym "K_UP"
        action Show("PhoneInterface") at fastAppearDisappear



    frame at fastAppearDisappear:
        xalign 0.5
        yalign 0.5
        xysize (500, 625)

        background "#00000000"

        has viewport:
            draggable True
            mousewheel True

        vbox:
            for log in chelseaTexts.textLog:
                frame:
                    background "#bc3739"
                    margin (20, 10, 20, 10)
                    ysize 140

                    has vbox

                    textbutton "[log.contact]" text_style "messageListName" action Show("CurrentTextConversations", nickname = log.nickname, history = log.textHistory)

                    viewport:
                        draggable True
                        ymaximum 50


                        $ _ = log.textHistory[-1]


                        if not _.image:
                            text _.message style "messageListMessage"

                        else:
                            text "{color=#fefcc7}*Image*{/color}" line_spacing 5

"The screen where the user has the option to try to trigger a texting scene with a character or change their contacts' names."



screen ContactOptions(selectedContact):
    default _ = chelseaContacts.getKey(selectedContact)


    zorder 100
    modal True tag phone


    add "black" alpha 0.9
    add chelseaPhone xalign 0.5 yalign 0.5


    imagebutton auto chelPhoneBack:
        xalign 0.38
        yalign 0.16
        keysym "K_UP"
        action Show("Contacts")

    frame:
        xalign 0.5
        yalign 0.5
        xysize (500, 625)

        background "#00000000"

        has vbox:
            xalign 0.5

        text "What do you want to do with {color=#ff0000}[selectedContact]{/color}?" color "#000000" text_align 0.5 xalign 0.5


        frame:
            xfill True
            margin (0, 15, 0, 15)

            background "#bc3739"





            textbutton "Text [_].":
                xalign 0.5
                text_style "contactInteract"
                action Hide("ContactOptions"), SetVariable("goingto", "message" + _.lower()), Call("events_run_period")


        frame:
            xfill True
            margin (0, 15, 0, 15)

            background "#bc3739"

            textbutton "Change [_]'s Name." text_style "contactInteract" xalign 0.5 action Show("ContactInputScreen", value = selectedContact, key = _)

"The screen where the user changes the name of a phone contact. https://www.renpy.org/doc/html/screen_actions.html#input-values"



screen ContactInputScreen(value, key):
    default _ = value


    zorder 100
    modal True tag phone


    add "black" alpha 0.9
    add chelseaPhone xalign 0.5 yalign 0.5


    imagebutton auto chelPhoneBack:
        xalign 0.38
        yalign 0.16
        keysym "K_UP"
        action Show("ContactOptions", selectedContact = value) at fastAppearDisappear

    frame:
        xalign 0.5
        yalign 0.5
        xysize (500, 625)

        background "#00000000"

        has vbox:
            xalign 0.5

        text "Enter [value]'s new name:" color "#000000"


        input:
            xalign 0.5
            value ScreenVariableInputValue("_", default = True)
            length 24



        frame:
            background "#bc3739"

            xalign 0.5
            margin (0, 100, 0, 0)

            textbutton "Confirm":
                keysym "K_RETURN"
                text_style "contactInteract"
                action SetDict(chelseaContacts.contactsListed, key, _), Function(chelseaContacts.updateTextingNames, key, _), Show("ContactOptions", selectedContact = _)

"Plays out the newly added text messages as a 'scene'."


screen TextingScene(name, messageList):
    zorder 100
    modal True





    if len(messageList) == 1:

        key "dismiss":
            action Return(0), Function(addTextMessage, name, messageList[0].message, messageList[0].sender, image = messageList[0].image, landscape = messageList[0].landscape)
    else:

        key "dismiss":
            action Hide("TextingScene"), Function(addTextMessage, name, messageList[0].message, messageList[0].sender, image = messageList[0].image, landscape = messageList[0].landscape), Show("TextingScene", name = name, messageList = messageList[1:])


    add "black" alpha 0.9
    add chelseaPhone xalign 0.5 yalign 0.5
    add "gui/phoneBack_idle.png" xalign 0.38 yalign 0.16

    frame:
        xalign 0.5
        yalign 0.5
        xysize (500, 625)

        background "#00000000"

        has viewport:
            draggable True
            mousewheel True
            yinitial 1000000000

        vbox:

            $ _ = chelseaTexts.getMessageHistory(name)

            if _ != None and len(_) > 0:

                for response in _[-200:]:
                    frame at prevMessageMove:
                        xminimum 200
                        xmaximum (325 if not response.landscape else 485)


                        bottom_margin 15


                        padding (10, 10, 10, 10)



                        if not response.sender:
                            xpos (175 if not response.landscape else 0)
                            background "#5966ed"

                        else:
                            background "#d9398c"

                        vbox:

                            if response.sender:
                                $ _ = chelseaContacts.contactsListed

                                if name in _.keys():
                                    text _[name] style "contactName"
                                else:
                                    text name style "contactName"

                            else:
                                text "[pcname]" style "contactName"



                            if response.image:
                                add response.message at scaledown(0.5 if not response.landscape else 0.48)




                            else:
                                text response.message style "contactMessage"


            frame at newMessageAppear:
                xminimum 200
                xmaximum (325 if not messageList[0].landscape else 485)


                bottom_margin 15


                padding (10, 10, 10, 10)



                if not messageList[0].sender:
                    xpos (175 if not messageList[0].landscape else 0)
                    background "#5966ed"

                else:
                    background "#d9398c"

                vbox:

                    if messageList[0].sender:

                        $ _ = chelseaContacts.contactsListed



                        if name in _.keys():
                            text _[name] style "contactName"
                        else:
                            text name style "contactName"

                    else:
                        text "[pcname]" style "contactName"



                    if messageList[0].image:
                        add messageList[0].message at scaledown(0.5 if not messageList[0].landscape else 0.48)




                    else:
                        text messageList[0].message style "contactMessage"

"Displays your history of texts with a contact."


screen CurrentTextConversations(nickname, history):

    zorder 100
    modal True tag phone


    add "black" alpha 0.9
    add chelseaPhone xalign 0.5 yalign 0.5


    imagebutton auto chelPhoneBack:
        xalign 0.38
        yalign 0.16
        keysym "K_UP"
        action Show("Messages") at fastAppearDisappear

    frame:
        xalign 0.5
        yalign 0.5
        xysize (500, 625)

        background "#00000000"

        has viewport:
            draggable True
            mousewheel True
            yinitial 1000000000

        vbox:
            for response in history[-200:]:
                frame:
                    xminimum 200
                    xmaximum (325 if not response.landscape else 485)


                    bottom_margin 15


                    padding (10, 10, 10, 10)



                    if not response.sender:
                        xpos (175 if not response.landscape else 0)
                        background "#5966ed"

                    else:
                        background "#d9398c"

                    vbox:

                        if response.sender:
                            text nickname style "contactName"

                        else:
                            text "[pcname]" style "contactName"



                        if response.image:
                            imagebutton:
                                idle response.message
                                action Show("ImageView", history = history, nickname = nickname, chosenImage = response.message)
                                at scaledown(0.5 if not response.landscape else 0.48)
                        else:
                            text response.message style "contactMessage"

"Displays the chosen texting CG at its full size."


screen ImageView(history=None, fromGallery=False, nickname, chosenImage):

    zorder 100
    modal True tag phone


    add "#000000" alpha 0.9


    add chosenImage xalign 0.5 yalign 0.5


    if not fromGallery:
        textbutton "Back":
            xalign 0.5
            yalign 0.96
            keysym "K_UP"
            action Show("CurrentTextConversations", history = history, nickname = nickname)

    else:
        textbutton "Back":
            xalign 0.5
            yalign 0.96
            keysym "K_UP"
            action Show("PhoneGallery")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
