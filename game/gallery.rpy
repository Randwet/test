

pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.RPY'>>>>

init python:
    from collections import defaultdict


    config.gl2 = True

    class Graphic(object):
        """
        Class which holds the name and seen values of an image
        to be used to populate the sets in the gallery with unlocked 
        CG's and backgrounds.

        Takes 1 argument: name
        """
        def __init__(self, name):
            self._name = name
            self._seen = renpy.seen_image(name)
        
        
        
        @property
        def name(self):
            return self._name
        
        
        
        @property
        def seen(self):
            return self._seen
        
        
        
        def updateSeen(self):
            self._seen = renpy.seen_image(self._name)

    class CGSet(object):
        """
        Class which holds sets of CG's and backgrounds. This
        is used to populate the gallery with a number of sets
        of CG's that the user can click on to then view the CG's
        and backgrounds associated with the set.

        Takes no arguments.
        """
        def __init__(self):
            self._sets = defaultdict(list)
            self._showAll = False
        
        
        
        @property
        def sets(self):
            return self._sets
        
        
        
        @property
        def showAll(self):
            return self._showAll
        
        
        
        @showAll.setter
        def showAll(self, value):
            self._showAll = value
        
        
        
        
        def addImageSet(self, setName, *images):
            _ = []
            
            
            
            if not isinstance(setName, basestring):
                raise ValueError("setName can only be a string. You inputted a value of {}".format(type(setName)))
            elif setName not in ["Bakery", "Cafe", "Kate", "Matt", "Violet", "Damien", "Town", "Extra"]: 
                raise ValueError("{} is not a listed gallery section used in Uni. Was the section added to the list or spelled properly?".format(setName))
            
            
            if len(images) == 0:
                raise ValueError("The images variable's length cannot be 0. Please provide at least 1 string containing an image's name.")
            
            
            
            
            for image in images:
                if isinstance(image, basestring):
                    if not renpy.has_image(image):
                        raise ValueError("No image named {} could be found. Did you type the name in properly?".format(image))
                    else:
                        _.append(Graphic(image))
                elif isinstance(image, tuple):
                    for tupleImage in image:
                        if not renpy.has_image(tupleImage):
                            raise ValueError("No image named {} could be found. Did you type the name in properly?".format(tupleImage))
                        else:
                            _.append(Graphic(image))
                else:
                    raise TypeError("{} is of {}. Please only type in strings or tuples of strings.".format(image, type(image)))
            
            
            
            self._sets[setName].append(_)
        
        
        
        
        def getThumbnail(self, section):
            for picture in section:
                picture.updateSeen()
                
                if picture.seen or self._showAll:
                    return picture.name
            
            return "gui/gallery/GalleryBlank.png"
        
        
        
        
        def getViewableList(self, section):
            _ = []
            
            if self._showAll:
                return section
            
            for picture in section:
                picture.updateSeen()
                
                if picture.seen: 
                    _.append(picture)
            
            return _





    gallery = CGSet()



transform hoverAnimation:
    on hover:
        linear 0.2 alpha 0.5
    on idle:
        linear 0.2 alpha 1.0


"Screen which displays the first unlocked image in an image set for every possible image set associated with the clicked on button."
"Takes no arguments."





screen Gallery(pageDefault=gallery.sets.get("Bakery")):
    default page = pageDefault

    zorder 100
    modal True tag gallery




    imagemap:
        auto "gui/gallery/main-gallery-%s.png"

        hotspot (1671, 157, 61, 61) action Hide("Gallery")


        hotspot (260, 226, 370, 76) action SetScreenVariable("page", gallery.sets.get("Bakery"))
        hotspot (260, 310, 370, 76) action SetScreenVariable("page", gallery.sets.get("Cafe"))
        hotspot (260, 393, 370, 76) action SetScreenVariable("page", gallery.sets.get("Damien"))
        hotspot (260, 477, 370, 76) action SetScreenVariable("page", gallery.sets.get("Kate"))
        hotspot (260, 561, 370, 76) action SetScreenVariable("page", gallery.sets.get("Matt"))
        hotspot (260, 646, 370, 76) action SetScreenVariable("page", gallery.sets.get("Violet"))
        hotspot (260, 729, 370, 76) action SetScreenVariable("page", gallery.sets.get("Town"))
        hotspot (260, 813, 370, 76) action SetScreenVariable("page", gallery.sets.get("Extra"))

    if page != None:
        side "c r":
            xalign 0.71
            yalign 0.55

            vpgrid id "gBar":
                cols 3

                draggable True
                mousewheel True

                ysize 660



                for section in page:
                    frame:
                        background "#cbbcb1"

                        margin (5, 5, 5, 5)
                        padding (5, 5, 5, 5)



                        $ _ = gallery.getThumbnail(section)


                        if _ == "gui/gallery/GalleryBlank.png":
                            add _ at scaledown(0.15)


                        else:
                            imagebutton idle _ action Show("GalleryDetails", images = gallery.getViewableList(section)) at hoverAnimation, scaledown(0.15)



            vbar:
                xsize 25


                thumb_offset 97
                top_gutter 97
                bottom_gutter 97


                unscrollable "hide"


                value YScrollValue("gBar")

                base_bar "gui/gallery/scrollbar.png"
                thumb "gui/gallery/scrollbar-handle.png"

"Screen which displays all the unlocked images in an image set and depending on the user's choice, will display a larger version of a chosen image. Clicking on the larger image will show a fullscreen version of that image."
"Takes one argument: images"






screen GalleryDetails(images):
    default pictureIndex = 0

    zorder 100
    modal True tag gallery




    imagemap:
        auto "gui/gallery/gallery-detail-%s.png"



        hotspot (1671, 157, 61, 61) action Hide("GalleryDetails")


        hotspot (661, 763, 204, 137) action Show("FullScreen", picture = images[pictureIndex].name)


        hotspot (892, 763, 204, 137) keysym "K_LEFT" action If(pictureIndex - 1 >= 0, SetScreenVariable("pictureIndex", pictureIndex - 1))


        hotspot (1121, 763, 204, 137) keysym "K_RIGHT" action If(pictureIndex + 1 < len(images), SetScreenVariable("pictureIndex", pictureIndex + 1))


        hotspot (1351, 763, 204, 137) action Show("Gallery")


        hotspot (260, 226, 370, 76) action Show("Gallery", pageDefault = gallery.sets.get("Bakery"))
        hotspot (260, 310, 370, 76) action Show("Gallery", pageDefault = gallery.sets.get("Cafe"))
        hotspot (260, 393, 370, 76) action Show("Gallery", pageDefault = gallery.sets.get("Damien"))
        hotspot (260, 477, 370, 76) action Show("Gallery", pageDefault = gallery.sets.get("Kate"))
        hotspot (260, 561, 370, 76) action Show("Gallery", pageDefault = gallery.sets.get("Matt"))
        hotspot (260, 646, 370, 76) action Show("Gallery", pageDefault = gallery.sets.get("Violet"))
        hotspot (260, 729, 370, 76) action Show("Gallery", pageDefault = gallery.sets.get("Town"))
        hotspot (260, 813, 370, 76) action Show("Gallery", pageDefault = gallery.sets.get("Extra"))




    imagebutton idle images[pictureIndex].name:
        keysym "K_RETURN"
        action Show("FullScreen", picture = images[pictureIndex].name) at scaledown(0.47) xalign 0.6455 yalign 0.4


    side "c r":
        xalign 0.87
        yalign 0.4



        vpgrid id "gdBar":
            cols 1

            draggable True
            mousewheel True

            xsize 100
            ysize 508

            spacing 5

            for index, picture in enumerate(images):
                frame:
                    background "#cbbcb1"
                    padding (2, 2, 2, 2)

                    imagebutton idle picture.name action SetScreenVariable("pictureIndex", index) at hoverAnimation, scaledown(0.05)



        vbar:
            xsize 25
            ysize 652


            thumb_offset 97
            top_gutter 97
            bottom_gutter 97


            value YScrollValue("gdBar")


            unscrollable "hide"

            base_bar "gui/gallery/scrollbar.png"
            thumb "gui/gallery/scrollbar-handle.png"

            at scaledown(0.78)


"Screen that shows the player's selected image in its full dimensions. Takes 1 argument: picture"



screen FullScreen(picture):
    zorder 100
    modal True

    imagebutton idle picture keysym "K_RETURN" action Hide("FullScreen") xalign 0.5 yalign 0.5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
