



default persistent.freemode = False
default persistent.introseen = False
default persistent.clubseen = False
default persistent.shortcutmsg = False


default day = 7
default daypart = ""
default acts = 4
default goingto = "school"
default daycount = 0
default daylimit = 75
default dayname = "Sunday"
default wenttoclub = False
default wenttoschool = False
default schoolday = False
default workday = False
default wenttowork = False
default skippedwork = False
default skippedschool = False
default skippedschoolcounter = 0
default skippedworkcounter = 0
default job = ""
default havehomework = False
default completehomework = False
default varsport = " "
default varsportwin = 0
default daysworked = 0
default payday = False
default paychecktotal = 0
default mattscore = 0
default tips = 0
default tipweight = 0
default arcadeRandomizer = 0
default playing = ""
default insult = ""
default morning = ""
default damienname = "that other boy"
default deskstain = False
default clubday = False
default trackperf = 0
default club = ""
default activity = "reading"
default cloud = ""
default damiendate = False
default katedate = False
default violetdate = False
default lisadate = False
default gradesday = 0
default catadopt = False
default catbedbought = False
default catpostbought = False
default catfood = 100
default catstuff = 0
default foodmessage = 1
default cathungry = 0
default shopmakeup = False
define flash = Fade(.25, 0.0, .75, color="#fff")
default caferaise = False


transform midright:
    xalign 0.75
    yalign 0.75

transform midleft:
    xalign 0.25
    yalign 0.25

transform moveupfast(startAlign, endAlign, moveDelta):
    ypos startAlign
    linear moveDelta ypos endAlign

transform exitScene(startAlign, endAlign, alignDelta, alphaDelta):
    parallel:
        xalign startAlign
        linear alignDelta xalign endAlign
    parallel:
        alpha 1.0
        linear alphaDelta alpha 0.0

transform enterScene(startAlign, endAlign, alignDelta, alphaDelta):
    parallel:
        xalign startAlign
        linear alignDelta xalign endAlign
    parallel:
        alpha 0.0
        linear alphaDelta alpha 1.0

transform moveSprite(startAlign, endAlign, alignDelta):
    xalign startAlign
    linear alignDelta xalign endAlign



init python:
    """
    Changes Violet's clothes when the clothes argument is set to 0, 1, or 2
    0 = Casual Outfit 1
    1 = Casual Outfit 2
    """
    def violetAttire(clothes = 0):
        global VCasualBlank
        global VCasualPout
        global VCasualAnnoyed
        global VCasualSmile
        global VCasualSuprised
        global VSubCasualBlank
        global VSubCasualHappy
        global VSubCasualSad
        global VSubCasualWorried
        
        if clothes == 0:
            VCasualBlank = "Characters/Violet/Casual/Casual Neutral.png"
            VCasualPout = "Characters/Violet/Casual/Casual Pouting.png"
            VCasualAnnoyed = "Characters/Violet/Casual/Casual Annoyed.png"
            VCasualSmile = "Characters/Violet/Casual/Casual Smile.png"
            VCasualSuprised = "Characters/Violet/Casual/Casual Suprised.png"
            
            VSubCasualBlank = "Characters/Violet/Casual/Sub/Neutral.png"
            VSubCasualHappy = "Characters/Violet/Casual/Sub/Happy.png"
            VSubCasualSad = "Characters/Violet/Casual/Sub/Sad.png"
            VSubCasualWorried = "Characters/Violet/Casual/Sub/Worried.png"
        elif clothes == 1:
            VCasualBlank = "Characters/Violet/Casual 2/Neutral.png"
            VCasualPout = "Characters/Violet/Casual 2/Pouting.png"
            VCasualAnnoyed = "Characters/Violet/Casual 2/Annoyed.png"
            VCasualSmile = "Characters/Violet/Casual 2/Smile.png"
            VCasualSuprised = "Characters/Violet/Casual 2/Suprised.png"
            
            VSubCasualBlank = "Characters/Violet/Casual 2/Sub/Neutral.png"
            VSubCasualHappy = "Characters/Violet/Casual 2/Sub/Happy.png"
            VSubCasualSad = "Characters/Violet/Casual 2/Sub/Sad.png"
            VSubCasualWorried = "Characters/Violet/Casual 2/Sub/Worried.png"
        else:
            raise NotImplementedError("Invalid number given. Input only 0 or 1.")


    """
    Changes Damien's clothes when the clothes argument is set to 0, 1, or 2.
    0 = School Uniform
    1 = Casual Outfit 1
    2 = Casual Outfit 2
    """
    def damienAttire(clothes = 0):
        global DamienAngry
        global DamienBlank
        global DamienGlare
        global DamienLaugh
        global DamienNeutral
        global DamienSad
        global DamienShocked
        global DamienSmiling
        global DamienWorrying
        
        if clothes == 0:
            DamienAngry = "Characters/Damien/School Uniform/Angry.png"
            DamienBlank = "Characters/Damien/School Uniform/Blank.png"
            DamienGlare = "Characters/Damien/School Uniform/Glaring.png"
            DamienLaugh = "Characters/Damien/School Uniform/Laughing.png"
            DamienNeutral = "Characters/Damien/School Uniform/Neutral.png"
            DamienSad = "Characters/Damien/School Uniform/Sad.png"
            DamienShocked = "Characters/Damien/School Uniform/Shocked.png"
            DamienSmiling = "Characters/Damien/School Uniform/Smiling.png"
            DamienWorrying = "Characters/Damien/School Uniform/Worrying.png"
        elif clothes == 1:
            DamienAngry = "Characters/Damien/Casual/Angry.png"
            DamienBlank = "Characters/Damien/Casual/Blank.png"
            DamienGlare = "Characters/Damien/Casual/Glaring.png"
            DamienLaugh = "Characters/Damien/Casual/Laughing.png"
            DamienNeutral = "Characters/Damien/Casual/Neutral.png"
            DamienSad = "Characters/Damien/Casual/Sad.png"
            DamienShocked = "Characters/Damien/Casual/Shocked.png"
            DamienSmiling = "Characters/Damien/Casual/Smiling.png"
            DamienWorrying = "Characters/Damien/Casual/Worrying.png"
        elif clothes == 2:
            DamienAngry = "Characters/Damien/Casual 2/Angry.png"
            DamienBlank = "Characters/Damien/Casual 2/Blank.png"
            DamienGlare = "Characters/Damien/Casual 2/Glaring.png"
            DamienLaugh = "Characters/Damien/Casual 2/Laughing.png"
            DamienNeutral = "Characters/Damien/Casual 2/Neutral.png"
            DamienSad = "Characters/Damien/Casual 2/Sad.png"
            DamienShocked = "Characters/Damien/Casual 2/Shocked.png"
            DamienSmiling = "Characters/Damien/Casual 2/Smiling.png"
            DamienWorrying = "Characters/Damien/Casual 2/Worrying.png"
        else:
            raise NotImplementedError("Invalid number given. Input only 0, 1, or 2.")


define greeting = True
define mattsubmissive = True
default mattslap = 0
default damienadvice = False
default pepmocha = False
default gangrape = False
default katerelate = "friend"
default bullytelloff = 0
define lottostand = 3
default defymatt = False
default benwa = False
default damienlove = 0
default telldamien = False
default cafesex = False
default turndownkate = False
default Showerblackmail = False
default endgame = False
default refusedbikini = False
default carwashlow = False
default secondcarrun = False
default firstcarrun = False
default acceptcaroffer = False
default karaokeleave = True
default mafiafavor = False
default underwear2 = False
default violetdom5lie = False
default violetcum = 1
default violetsub4choice = ""
default violetsub4_options = ["shop", "dinner", "violethouse", "clean"]
default alicechoice = 0
default mattdamienntr = False
default damienbreakup = False
default mattbreakup = False
default mattroutelock = False
default violetbreakup = False
default MafiaFavorMatt = False
default Oliviacorruption = 0



define Cash = 50
default intelligence = 50
default corruption = 0
define items = []


define audio.PhoneVibration = "sfx/phonevibrationfast.wav"


default tipsnotification = 0
default TextCheck = False
default violetdate1place = ""
default violetscenes = 0
default damienevents = 0
default coffeeflag = False
default movieflag = False
default damienpays = False
default damiencuddle = False
default damienhandjob = False
default damientelloff = False
default mattchain = 0
default mattphone = False
default cafeshirt = 0
default cafelap = False
default cafepanties = False
default cafecorrupt = 0
default cafeblowjob = False
default corruptkate = False
default bakerychain = 0
default katedream = False
define cafeprog = 0
default mattblackmail = 0
default order = ""
default violetrelate = "Friends"
default violetchoosefood = True
default violetgivesmassage = True
default violetgetsdrink = "True"
default violetsubdom = 5
default violetdateflag = False
default violetmaid = True
default blackmailpics = "panties"
default kateknowsaboutfamily = False
default damienknowsaboutfamily = False
default violetknowsaboutfamily = False
default katesickflag = False
default medicine = "generic"
default violetlunchsandwich = False
default violetlunchdrink = False
default violetlunchdessert = False
default violetapproval = 5
default violetdatescore = 0
default violetsub2count = 0
default damientellviolethj = False
default damienkeepquiet = False
default damienfestivalflag = False
default damienafternoonfood = False
default damienafternoongames = False
default damienafternoonshows = False
default damieneveningfood = False
default damieneveninggames = False
default damieneveningshows = False
default damienrelate = ""
default damienstaythenight = True
default damienmattthreesomedream = False
default damienvioletthreesomedream = False
default damiensexdream = False
default nilesflirt = False
default namedrop = False
default coffeebusinesscard = False
default findkittenhome = False
default meetmafia = False
default catcallflashing = False
default catcalltouching = False
default catcalloral = False
default grannypaid = False
default fakeid = False
default stripclubcount = 0
default stripclubvisit = False
default bouncerflirt = False
default bouncerhandjob = False
default poledancing = False
default playsm = False
default smchara_race = "human"
default photo_subj1 = ""
default photo_subj2 = ""
default photo_subj3 = ""
default coffeescenes = 0
default kittenscenes = 0
default karaokescenes = 0
default marketscenes = 0
default fakerid = 0
default gymchoice = 0
default Macbethread = False
default copyhomework = False
default grannywork = False
default track1_convo = ""
default track2_convo = ""
default lisa_agree = False
default bakeryagree = 0
default lisa_gotomall = False
default bakerymakeup = False
default bakeryhalfmakeup = False
default bakery_eavesdrop = False
default bakery_lisaconfront = False
default bakerymakeup2 = False
default bakery_flirtwkeith = False
default bakery_end = False
default bakery_bimbo1 = False
default bakery_blonde = False
default bakerycorrupt = 0
default shoppingwlisa = False
default damien_lunchwvioletdd = False
default bakeryuniformagree = False
default bakerystuffing = False
default bakeryconsultagree = False
default bakeryconsultagree2 = False
default bakeryboobjobapprove = False
default bakeryroutelock = False
default mattrouteend = False
default katefestival = False
default damienmall = False
default damienconfidence = 50
default damienoutfitchange = False
default damiencomicsigned = False
default damienenters = False
default damienlingeriepictures = False
default mattlingeriepictures = False
default damienlingeriepurchase = False
default damienclubbj = False
default homeworkgirls = False
default barprostitution = False
default refuseprostitution = False
default moviegenre = ""
default getintoit = False
default cheerfirst1 = True
default SlitDressSeen = False
default HalterDressSeen = False
default MiniDressSeen = False
default zoobusscene = ""
default zoo_options = ["giraffe", "penguin", "goat"]
default kateshirtswitch = True
default zooseen = ["giraffe", "penguin", "goat"]
default damienNTR = False
default negotiationsclean = False
default homecoming = False
default seotname = False
default damienexhibit1 = False
default damienexhibit2 = False
default damienexhibit3 = False
default damienexhibit1T = False
default damienexhibit1SO = False
default damienexhibit1S = False
default damienexhibit1P = False
default damienexhibit1O = False
default damienexhibit2T = False
default damienexhibit2SO = False
default damienexhibit2S = False
default damienexhibit2P = False
default damienexhibit2O = False
default violetdom4masturbate = False
default katebusy = 0
default violetbusy = 0
default damienbusy = 0
default mattbusy = 0
default mistresskink = False
default mistresskinkcomplete = False
default patientkink = False
default patientkinkcomplete = False
default bosskink = False
default bosskinkcomplete = False
default alleyscene = 0
default stripdance = False
default fuckclients = False
default applescam = False
default privateclient = False
default violetbarpickup = False
default KateDamienConfession = False
default vibrator = False


define pcname = Character("Chelsea", image = "chelsea")
default domtitle = "Mistress"
define P = ("Principal")
define T = ("Mr. Harley")
define V = ("Violet")
define m = ("Matt")
define L = ("Lisa")
define BM = ("Manager")
define K = ("Kate")
define D = ("Damien")
define Dan = ("Daniel")
define kittenname = ("Lucky")
define A = ("Alice")



image LL Blank = "Characters/The Landlord/Blank.png"
image LL Disappoint = "Characters/The Landlord/Disappointed.png"
image LL Happy = "Characters/The Landlord/Happy.png"
image LL Neutral = "Characters/The Landlord/Neutral.png"
image LL Serious = "Characters/The Landlord/Serious.png"



image P Blank = "Characters/Principal/Principal - blank.png"
image P Mad = "Characters/Principal/Principal - angry.png"
image P Laugh = "Characters/Principal/Principal - laugh.png"


default HarleyBlank = "Characters/Mr. Harley/Blank.png"
default HarleyNeutral = "Characters/Mr. Harley/Neutral.png"
default HarleyHappy = "Characters/Mr. Harley/Happy.png"
default HarleyLaugh = "Characters/Mr. Harley/Laugh.png"
default HarleyQuestion = "Characters/Mr. Harley/Question.png"
default HarleyAngry = "Characters/Mr. Harley/Angry.png"


image Harley Blank = "[HarleyBlank]"
image Harley Neutral = "[HarleyNeutral]"
image Harley Happy = "[HarleyHappy]"
image Harley Laugh = "[HarleyLaugh]"
image Harley Question = "[HarleyQuestion]"
image Harley Angry = "[HarleyAngry]"



default DamienAngry = "Characters/Damien/School Uniform/Angry.png"
default DamienBlank = "Characters/Damien/School Uniform/Blank.png"
default DamienGlare = "Characters/Damien/School Uniform/Glaring.png"
default DamienLaugh = "Characters/Damien/School Uniform/Laughing.png"
default DamienNeutral = "Characters/Damien/School Uniform/Neutral.png"
default DamienSad = "Characters/Damien/School Uniform/Sad.png"
default DamienShocked = "Characters/Damien/School Uniform/Shocked.png"
default DamienSmiling = "Characters/Damien/School Uniform/Smiling.png"
default DamienWorrying = "Characters/Damien/School Uniform/Worrying.png"





















image Damien Blank = "[DamienBlank]"
image Damien Neutral = "[DamienNeutral]"
image Damien Glare = "[DamienGlare]"
image Damien Laugh = "[DamienLaugh]"
image Damien Angry = "[DamienAngry]"
image Damien Sad = "[DamienSad]"
image Damien Shocked = "[DamienShocked]"
image Damien Happy = "[DamienSmiling]"
image Damien Worry = "[DamienWorrying]"


image DamienHigh = "Characters/Damien/DamienClothesHighConfidence.png"
image DamienLow = "Characters/Damien/DamienClothesLowConfidence.png"


image Matt Blank = "Characters/Matt/Blank.png"
image Matt Angry = "Characters/Matt/Angry.png"
image Matt Happy = "Characters/Matt/Happy.png"
image Matt Pleased = "Characters/Matt/Pleased.png"
image Matt Question = "Characters/Matt/Questioning.png"
image Matt Smirk = "Characters/Matt/Smirk.png"

image Matt Casual Blank = "Characters/Matt/Casual/Blank.png"
image Matt Casual Angry = "Characters/Matt/Casual/Angry.png"
image Matt Casual Happy = "Characters/Matt/Casual/Happy.png"
image Matt Casual Pleased = "Characters/Matt/Casual/Pleased.png"
image Matt Casual Question = "Characters/Matt/Casual/Questioning.png"
image Matt Casual Smirk = "Characters/Matt/Casual/Smirk.png"

image Matt Beaten = "Characters/Matt/Beaten/Dead.png"
image Matt Scared = "Characters/Matt/Beaten/Scared.png"


image Alex Blank = "Characters/Alex/Blank.png"
image Alex Angry = "Characters/Alex/Angry.png"
image Alex Happy = "Characters/Alex/Happy.png"
image Alex Laugh = "Characters/Alex/Laugh.png"
image Alex Serious = "Characters/Alex/Serious.png"
image Alex Neutral = "Characters/Alex/Neutral.png"


image CC Blank = "Characters/Coach Carrigan/Blank.png"
image CC BlankClosed = "Characters/Coach Carrigan/Blank_Closed.png"
image CC Serious = "Characters/Coach Carrigan/Serious.png"
image CC Neutral = "Characters/Coach Carrigan/Neutral.png"
image CC Happy = "Characters/Coach Carrigan/Happy.png"
image CC Confused = "Characters/Coach Carrigan/Confused.png"


image CClayton Blank = "Characters/Coach Clayton/Blank.png"
image CClayton Neutral = "Characters/Coach Clayton/Neutral.png"
image CClayton Angry Closed = "Characters/Coach Clayton/Angry Closed.png"
image CClayton Angry Open = "Characters/Coach Clayton/Angry Open.png"
image CClayton Happy Closed = "Characters/Coach Clayton/Happy Closed.png"
image CClayton Happy Open = "Characters/Coach Clayton/Happy Open.png"
image CClayton Laugh = "Characters/Coach Clayton/Laughing.png"
image CClayton Confused = "Characters/Coach Clayton/Question.png"
image CClayton Shocked = "Characters/Coach Clayton/Shocked.png"
image CClayton Yell = "Characters/Coach Clayton/Yell.png"


image CR Blank = "Characters/Coach Rudy/Blank.png"
image CR Neutral = "Characters/Coach Rudy/Neutral.png"
image CR Angry Closed = "Characters/Coach Rudy/Angry Closed.png"
image CR Angry Open = "Characters/Coach Rudy/Angry Open.png"
image CR Happy Closed = "Characters/Coach Rudy/Happy Closed.png"
image CR Happy Open = "Characters/Coach Rudy/Happy Open.png"
image CR Laugh Closed = "Characters/Coach Rudy/Laugh Closed.png"
image CR Laugh Open = "Characters/Coach Rudy/Laugh Open.png"
image CR Confused = "Characters/Coach Rudy/Question.png"
image CR Shocked = "Characters/Coach Rudy/Shock.png"
image CR Yell = "Characters/Coach Rudy/Yell.png"


define AugustClothes = 0
image August Angry = ConditionSwitch(
"AugustClothes == 0", "Characters/August/Angry.png",
"AugustClothes == 1", "Characters/August/Casual/Angry.png",
)
image August Blank = ConditionSwitch(
"AugustClothes == 0", "Characters/August/Blank.png",
"AugustClothes == 1", "Characters/August/Casual/Blank.png",
)
image August Confused = ConditionSwitch(
"AugustClothes == 0", "Characters/August/Confused.png",
"AugustClothes == 1", "Characters/August/Casual/Confused.png",
)
image August Happy = ConditionSwitch(
"AugustClothes == 0", "Characters/August/Happy.png",
"AugustClothes == 1", "Characters/August/Casual/Happy.png",
)
image August Laugh = ConditionSwitch(
"AugustClothes == 0", "Characters/August/Laughing.png",
"AugustClothes == 1", "Characters/August/Casual/Laughing.png",
)
image August Neutral = ConditionSwitch(
"AugustClothes == 0", "Characters/August/Neutral.png",
"AugustClothes == 1", "Characters/August/Casual/Neutral.png",
)
image August Disappointed = ConditionSwitch(
"AugustClothes == 0", "Characters/August/Disappointed.png",
"AugustClothes == 1", "Characters/August/Casual/Disappointed.png",
)


image Ryan Angry = "Characters/Ryan/Angry.png"
image Ryan Worry = "Characters/Ryan/Worried.png"
image Ryan Laugh = "Characters/Ryan/Laugh.png"
image Ryan Happy = "Characters/Ryan/Happy.png"
image Ryan Tired = "Characters/Ryan/Tired.png"


default MVBlank = "Characters/Ms Vicky/Neutral.png"
default MVLaugh = "Characters/Ms Vicky/Laughing.png"
default MVSmile = "Characters/Ms Vicky/Smile.png"
default MVTired = "Characters/Ms Vicky/Tired.png"
default MVWorried = "Characters/Ms Vicky/Worried.png"


image MV Blank = "[MVBlank]"
image MV Laugh = "[MVLaugh]"
image MV Smile = "[MVSmile]"
image MV Tired = "[MVTired]"
image MV Worried = "[MVWorried]"



default OliviaCheer1Happy = "Characters/Olivia/Happy.png"
default OliviaCheer1Sad = "Characters/Olivia/Sad.png"
default OliviaCheer1Tired = "Characters/Olivia/Tired.png"
default OliviaCheer1Confused = "Characters/Olivia/Confused.png"
default OliviaCheer1Laughing = "Characters/Olivia/Laugh.png"
default OliviaCheer1Blank = "Characters/Olivia/Neutral.png"
default OliviaCheer1Embarrassed = "Characters/Olivia/Embarrassed.png"

image Olivia Happy = "[OliviaCheer1Happy]"
image Olivia Sad = "[OliviaCheer1Sad]"
image Olivia Tired = "[OliviaCheer1Tired]"
image Olivia Confused = "[OliviaCheer1Confused]"
image Olivia Laughing = "[OliviaCheer1Laughing]"
image Olivia Blank = "[OliviaCheer1Blank]"
image Olivia Embarrassed = "[OliviaCheer1Embarrassed]"



image Tracy Angry = "Characters/Tracy/Angry.png"
image Tracy Blank = "Characters/Tracy/Blank.png"
image Tracy Laugh = "Characters/Tracy/Laughing.png"
image Tracy Question = "Characters/Tracy/Questioning.png"
image Tracy Smile = "Characters/Tracy/Smile.png"
image Tracy Tired = "Characters/Tracy/Tired.png"



image MD Blank = "Characters/Mr. Davis/Blank.png"
image MD Neutral = "Characters/Mr. Davis/Neutral.png"
image MD Open Smile = "Characters/Mr. Davis/Open Smile.png"
image MD Closed Smile = "Characters/Mr. Davis/Closed Smile.png"
image MD Laugh = "Characters/Mr. Davis/Laugh.png"
image MD Annoyed = "Characters/Mr. Davis/Annoyed.png"
image MD Worried = "Characters/Mr. Davis/Worried.png"


default SophiaBlank = "Characters/Sophie/Blank.png"
default SophiaEmbarrassed = "Characters/Sophie/Embarrassed.png"
default SophiaHappy = "Characters/Sophie/Happy.png"
default SophiaNeutral = "Characters/Sophie/Neutral.png"
default SophiaSad = "Characters/Sophie/Sad.png"
default SophiaShy = "Characters/Sophie/Shy.png"

image Sophie Blank = "[SophiaBlank]"
image Sophie Embarrassed = "[SophiaEmbarrassed]"
image Sophie Happy = "[SophiaHappy]"
image Sophie Neutral = "[SophiaNeutral]"
image Sophie Sad = "[SophiaSad]"
image Sophie Shy = "[SophiaShy]"


image Levi Blank = "Characters/Levi/Neutral.png"
image Levi Neutral = "Characters/Levi/Neutral.png"
image Levi Shocked = "Characters/Levi/Shocked.png"
image Levi Sad = "Characters/Levi/Sad.png"
image Levi Laugh = "Characters/Levi/Laugh.png"
image Levi Happy = "Characters/Levi/Smile.png"
image Levi HappyFix = "Characters/Levi/SmileGlasses.png"
image Levi Worried = "Characters/Levi/Worried.png"


default KeithBlank = "Characters/Keith/Blank.png"
default KeithNeutral = "Characters/Keith/Neutral.png"
default KeithAngry = "Characters/Keith/Angry.png"
default KeithConfused = "Characters/Keith/Confused.png"
default KeithHappy = "Characters/Keith/Smile.png"
default KeithSmirk = "Characters/Keith/Smirk.png"
default KeithLaugh = "Characters/Keith/Laughing.png"

image Keith Blank = "[KeithBlank]"
image Keith Neutral = "[KeithNeutral]"
image Keith Angry = "[KeithAngry]"
image Keith Confused = "[KeithConfused]"
image Keith Happy = "[KeithHappy]"
image Keith Smirk = "[KeithSmirk]"
image Keith Laugh = "[KeithLaugh]"


default LHappy = "Characters/Lisa/Happy.png"
default LBlank = "Characters/Lisa/Blank.png"
default LQuestion = "Characters/Lisa/Questioning.png"
default LDisappoint = "Characters/Lisa/Disappointed.png"
default LSad = "Characters/Lisa/Sad.png"

image L Happy = "[LHappy]"
image L Blank = "[LBlank]"
image L Question = "[LQuestion]"
image L Disappoint = "[LDisappoint]"
image L Sad = "[LSad]"



default VCasualBlank = "Characters/Violet/Casual/Casual Neutral.png"
default VCasualPout = "Characters/Violet/Casual/Casual Pouting.png"
default VCasualAnnoyed = "Characters/Violet/Casual/Casual Annoyed.png"
default VCasualSmile = "Characters/Violet/Casual/Casual Smile.png"
default VCasualSuprised = "Characters/Violet/Casual/Casual Suprised.png"

default VSubCasualBlank = "Characters/Violet/Casual/Sub/Neutral.png"
default VSubCasualHappy = "Characters/Violet/Casual/Sub/Happy.png"
default VSubCasualSad = "Characters/Violet/Casual/Sub/Sad.png"
default VSubCasualWorried = "Characters/Violet/Casual/Sub/Worried.png"


image V School Blank = "Characters/Violet/School Uniform/School Neutral.png"
image V School Pout = "Characters/Violet/School Uniform/School Pouting.png"
image V School Annoyed = "Characters/Violet/School Uniform/School Annoyed.png"
image V School Smile = "Characters/Violet/School Uniform/School Smile.png"
image V School Suprised = "Characters/Violet/School Uniform/School Suprised.png"

image V Casual Blank = "[VCasualBlank]"
image V Casual Pout = "[VCasualPout]"
image V Casual Annoyed = "[VCasualAnnoyed]"
image V Casual Smile = "[VCasualSmile]"
image V Casual Suprised = "[VCasualSuprised]"

image V Topless Blank = "Characters/Violet/Casual/Topless Neutral.png"
image V Topless Suprised = "Characters/Violet/Casual/Topless Suprised.png"

image V SubSchool Blank = "Characters/Violet/School Uniform/Sub/Neutral.png"
image V SubSchool Happy = "Characters/Violet/School Uniform/Sub/Happy.png"
image V SubSchool Sad = "Characters/Violet/School Uniform/Sub/Sad.png"
image V SubSchool Worried = "Characters/Violet/School Uniform/Sub/Worried.png"

image V SubCasual Blank = "[VSubCasualBlank]"
image V SubCasual Happy = "[VSubCasualHappy]"
image V SubCasual Sad = "[VSubCasualSad]"
image V SubCasual Worried = "[VSubCasualWorried]"

image V SubTopless Blank = "Characters/Violet/Casual/Sub/Topless Neutral.png"
image V SubTopless Happy = "Characters/Violet/Casual/Sub/Topless Happy.png"
image V SubTopless Sad = "Characters/Violet/Casual/Sub/Topless Sad.png"
image V SubTopless Worried = "Characters/Violet/Casual/Sub/Topless Worried.png"

image V Party Annoyed = "Characters/Violet/Casual/Party/Annoyed.png"
image V Party Blank = "Characters/Violet/Casual/Party/Neutral.png"
image V Party Pout = "Characters/Violet/Casual/Party/Pouting.png"
image V Party Smile = "Characters/Violet/Casual/Party/Smile.png"
image V Party Suprised = "Characters/Violet/Casual/Party/Suprised.png"

image V SubParty Blank = "Characters/Violet/Casual/Party/Sub/Neutral.png"
image V SubParty Happy = "Characters/Violet/Casual/Party/Sub/Happy.png"
image V SubParty Sad = "Characters/Violet/Casual/Party/Sub/Sad.png"
image V SubParty Worried = "Characters/Violet/Casual/Party/Sub/Worried.png"


image EM Happy = "Characters/Emilia/Happy.png"
image EM Blank = "Characters/Emilia/Blank.png"
image EM Neutral = "Characters/Emilia/Neutral.png"
image EM Serious = "Characters/Emilia/Serious.png"




image K Happy = "Characters/Kate/Maid/Kate Maid Happy.png"
image K Laugh = "Characters/Kate/Maid/Kate Maid Laugh.png"
image K Mad = "Characters/Kate/Maid/Kate Maid Angry.png"
image K Embarrassed = "Characters/Kate/Maid/Kate Maid Embarrassed.png"
image K Blank = "Characters/Kate/Maid/Kate Maid Blank.png"
image K Sad = "Characters/Kate/Maid/Kate Maid Sad.png"

image K Casual Happy = "Characters/Kate/Casual/Happy.png"
image K Casual Laugh = "Characters/Kate/Casual/Laugh.png"
image K Casual Mad = "Characters/Kate/Casual/Mad.png"
image K Casual Embarrassed = "Characters/Kate/Casual/Embarrassed.png"
image K Casual Blank = "Characters/Kate/Casual/Blank.png"
image K Casual Sad = "Characters/Kate/Casual/Sad.png"

image K Bar Happy = "Characters/Kate/Bar/Happy.png"
image K Bar Laugh = "Characters/Kate/Bar/Laugh.png"
image K Bar Mad = "Characters/Kate/Bar/Mad.png"
image K Bar Embarrassed = "Characters/Kate/Bar/Embarrassed.png"
image K Bar Blank = "Characters/Kate/Bar/Blank.png"
image K Bar Sad = "Characters/Kate/Bar/Sad.png"

image K Under Happy = "Characters/Kate/Underwear/Happy.png"
image K Under Laugh = "Characters/Kate/Underwear/Laugh.png"
image K Under Mad = "Characters/Kate/Underwear/Mad.png"
image K Under Embarrassed = "Characters/Kate/Underwear/Embarrassed.png"
image K Under Blank = "Characters/Kate/Underwear/Blank.png"
image K Under Sad = "Characters/Kate/Underwear/Sad.png"



image Harper Blank = "Characters/Cafe Girls/Harper/Blank.png"
image Harper Happy = "Characters/Cafe Girls/Harper/Happy.png"
image Harper Neutral = "Characters/Cafe Girls/Harper/Neutral.png"
image Harper Angry = "Characters/Cafe Girls/Harper/Angry.png"
image Harper Worried = "Characters/Cafe Girls/Harper/Worried.png"
image Harper Laugh = "Characters/Cafe Girls/Harper/Laughing.png"

image Emma Blank = "Characters/Cafe Girls/Emma/Blank.png"
image Emma Happy = "Characters/Cafe Girls/Emma/Happy.png"
image Emma Neutral = "Characters/Cafe Girls/Emma/Neutral.png"
image Emma Angry = "Characters/Cafe Girls/Emma/Angry.png"
image Emma Worried = "Characters/Cafe Girls/Emma/Worried.png"
image Emma Laugh = "Characters/Cafe Girls/Emma/Laughing.png"

image Zoey Blank = "Characters/Cafe Girls/Zoey/Blank.png"
image Zoey Happy = "Characters/Cafe Girls/Zoey/Happy.png"
image Zoey Neutral = "Characters/Cafe Girls/Zoey/Neutral.png"
image Zoey Angry = "Characters/Cafe Girls/Zoey/Angry.png"
image Zoey Worried = "Characters/Cafe Girls/Zoey/Worried.png"
image Zoey Laugh = "Characters/Cafe Girls/Zoey/Laughing.png"


image Cat Blank = "Characters/Generic/Blank.png"
image Cat Sad = "Characters/Generic/Sad.png"
image Cat Happy = "Characters/Generic/Happy.png"


image DW Blank = "Characters/Dr.White/Blank.png"
image DW Confused = "Characters/Dr.White/Confused.png"
image DW Happy = "Characters/Dr.White/Happy.png"
image DW Neutral = "Characters/Dr.White/Neutral.png"
image DW Shocked = "Characters/Dr.White/Shocked.png"


image D Blank = "Characters/Daniel/Blank.png"
image D Neutral = "Characters/Daniel/Neutral.png"
image D Confused = "Characters/Daniel/Confused.png"
image D Smirk = "Characters/Daniel/Smirk.png"
image D Happy = "Characters/Daniel/Happy.png"
image D Laugh = "Characters/Daniel/Laughing.png"
image D Mad = "Characters/Daniel/Mad.png"


define AliceClothes = 0
image Alice Angry = ConditionSwitch(
"AliceClothes == 0", "Characters/Alice/School/Angry.png",
"AliceClothes == 1", "Characters/Alice/Casual 1/Angry.png",
"AliceClothes == 2", "Characters/Alice/Casual 2/Angry.png",
)
image Alice Blank = ConditionSwitch(
"AliceClothes == 0", "Characters/Alice/School/Blank.png",
"AliceClothes == 1", "Characters/Alice/Casual 1/Blank.png",
"AliceClothes == 2", "Characters/Alice/Casual 2/Blank.png",
)
image Alice Confused = ConditionSwitch(
"AliceClothes == 0", "Characters/Alice/School/Confused.png",
"AliceClothes == 1", "Characters/Alice/Casual 1/Confused.png",
"AliceClothes == 2", "Characters/Alice/Casual 2/Confused.png",
)
image Alice Happy = ConditionSwitch(
"AliceClothes == 0", "Characters/Alice/School/Happy.png",
"AliceClothes == 1", "Characters/Alice/Casual 1/Happy.png",
"AliceClothes == 2", "Characters/Alice/Casual 2/Happy.png",
)
image Alice Laughing = ConditionSwitch(
"AliceClothes == 0", "Characters/Alice/School/Laughing.png",
"AliceClothes == 1", "Characters/Alice/Casual 1/Laughing.png",
"AliceClothes == 2", "Characters/Alice/Casual 2/Laughing.png",
)
image Alice Neutral = ConditionSwitch(
"AliceClothes == 0", "Characters/Alice/School/Neutral.png",
"AliceClothes == 1", "Characters/Alice/Casual 1/Neutral.png",
"AliceClothes == 2", "Characters/Alice/Casual 2/Neutral.png",
)
image Alice Pout = ConditionSwitch(
"AliceClothes == 0", "Characters/Alice/School/Pout.png",
"AliceClothes == 1", "Characters/Alice/Casual 1/Pout.png",
"AliceClothes == 2", "Characters/Alice/Casual 2/Pout.png",
)
image Alice Sad = ConditionSwitch(
"AliceClothes == 0", "Characters/Alice/School/Sad.png",
"AliceClothes == 1", "Characters/Alice/Casual 1/Sad.png",
"AliceClothes == 2", "Characters/Alice/Casual 2/Sad.png",
)
image Alice Thinking = ConditionSwitch(
"AliceClothes == 0", "Characters/Alice/School/Thinking.png",
"AliceClothes == 1", "Characters/Alice/Casual 1/Thinking.png",
"AliceClothes == 2", "Characters/Alice/Casual 2/Thinking.png",
)



default hair = "down"
default haircolor = "red"
default clothes = "school"
default casualwear = ("default", "down")
default implants = False
default makeup = False
default makeupbutton = False


image GCGirl = "Characters/Generic/Female Casual.png"
image GCBoy = "Characters/Generic/Boy Casual.png"
image GSBoy = "Characters/Generic/Boy Student.png"
image GSGirl = "Characters/Generic/Girl Student.png"
image GMaid = "Characters/Generic/Maid.png"
image GWaitress = "Characters/Generic/Waitress.png"
image GWaiter = "Characters/Generic/Waiter.png"
image GHCMan = "Characters/Generic/High Class.png"
image GFDoctor = "Characters/Generic/Female Doctor.png"
image GOLady1 = "Characters/Generic/Old Lady 1.png"
image GOLady2 = "Characters/Generic/Old Lady 2.png"
image GStripper = "Characters/Generic/Stripper.png"
image MPO = "Characters/Generic/MalePO.png"
image FPO = "Characters/Generic/FemalePO.png"
image Wareworker = "Characters/Generic/WarehouseWorker.png"







image map = ConditionSwitch(
"acts==4","Backgrounds/Town Map 2/Evening/Uni_Evening.jpg",
"acts==3","Backgrounds/Town Map 2/Day/Uni_Day.jpg",
"acts==2", "Backgrounds/Town Map 2/Day/Uni_Day.jpg",
"acts==1", "Backgrounds/Town Map 2/Evening/Uni_Evening.jpg",
"acts==0", "Backgrounds/Town Map 2/Night/Uni_Night.jpg",
"True", "Backgrounds/Town Map 2/Night/Uni_Night.jpg"
)
image houseidle = ConditionSwitch(
"acts==4","Backgrounds/Town Map 2/Evening/House_idle.png",
"acts==3","Backgrounds/Town Map 2/Day/House_idle.png",
"acts==2", "Backgrounds/Town Map 2/Day/House_idle.png",
"acts==1", "Backgrounds/Town Map 2/Evening/House_idle.png",
"acts==0", "Backgrounds/Town Map 2/Night/House_idle.png",
"True", "Backgrounds/Town Map 2/Night/House_idle.png"
)
image househover = ConditionSwitch(
"acts==4","Backgrounds/Town Map 2/Evening/House_hover.png",
"acts==3","Backgrounds/Town Map 2/Day/House_hover.png",
"acts==2", "Backgrounds/Town Map 2/Day/House_hover.png",
"acts==1", "Backgrounds/Town Map 2/Evening/House_hover.png",
"acts==0", "Backgrounds/Town Map 2/Night/House_hover.png",
"True", "Backgrounds/Town Map 2/Night/House_hover.png"
)
image schoolidle = ConditionSwitch(
"acts==4","Backgrounds/Town Map 2/Evening/School_idle.png",
"acts==3","Backgrounds/Town Map 2/Day/School_idle.png",
"acts==2", "Backgrounds/Town Map 2/Day/School_idle.png",
"acts==1", "Backgrounds/Town Map 2/Evening/School_idle.png",
"acts==0", "Backgrounds/Town Map 2/Night/School_idle.png",
"True", "Backgrounds/Town Map 2/Night/School_idle.png"
)
image schoolhover = ConditionSwitch(
"acts==4","Backgrounds/Town Map 2/Evening/School_hover.png",
"acts==3","Backgrounds/Town Map 2/Day/School_hover.png",
"acts==2", "Backgrounds/Town Map 2/Day/School_hover.png",
"acts==1", "Backgrounds/Town Map 2/Evening/School_hover.png",
"acts==0", "Backgrounds/Town Map 2/Night/School_hover.png",
"True", "Backgrounds/Town Map 2/Night/School_hover.png"
)
image mallidle = ConditionSwitch(
"acts==4","Backgrounds/Town Map 2/Evening/Mall_idle.png",
"acts==3","Backgrounds/Town Map 2/Day/Mall_idle.png",
"acts==2", "Backgrounds/Town Map 2/Day/Mall_idle.png",
"acts==1", "Backgrounds/Town Map 2/Evening/Mall_idle.png",
"acts==0", "Backgrounds/Town Map 2/Night/Mall_idle.png",
"True", "Backgrounds/Town Map 2/Night/Mall_idle.png"
)
image mallhover = ConditionSwitch(
"acts==4","Backgrounds/Town Map 2/Evening/Mall_hover.png",
"acts==3","Backgrounds/Town Map 2/Day/Mall_hover.png",
"acts==2", "Backgrounds/Town Map 2/Day/Mall_hover.png",
"acts==1", "Backgrounds/Town Map 2/Evening/Mall_hover.png",
"acts==0", "Backgrounds/Town Map 2/Night/Mall_hover.png",
"True", "Backgrounds/Town Map 2/Night/Mall_hover.png"
)
image cafeidle = ConditionSwitch(
"acts==4 and job=='cafe'","Backgrounds/Town Map 2/Evening/Cafe_idle.png",
"acts==4","Backgrounds/Town Map 2/Evening/Cafe_none.png",
"acts==3 and job=='cafe'","Backgrounds/Town Map 2/Day/Cafe_idle.png",
"acts==3","Backgrounds/Town Map 2/Day/Cafe_none.png",
"acts==2 and job=='cafe'", "Backgrounds/Town Map 2/Day/Cafe_idle.png",
"acts==2", "Backgrounds/Town Map 2/Day/Cafe_none.png",
"acts==1 and job=='cafe'", "Backgrounds/Town Map 2/Evening/Cafe_idle.png",
"acts==1", "Backgrounds/Town Map 2/Evening/Cafe_none.png",
"acts==0 and job=='cafe'", "Backgrounds/Town Map 2/Night/Cafe_idle.png",
"acts==0", "Backgrounds/Town Map 2/Night/Cafe_none.png",
"True", "Backgrounds/Town Map 2/Night/Cafe_idle.png"
)
image cafehover = ConditionSwitch(
"acts==4 and job=='cafe'","Backgrounds/Town Map 2/Evening/Cafe_hover.png",
"acts==4","Backgrounds/Town Map 2/Evening/Cafe_none.png",
"acts==3 and job=='cafe'","Backgrounds/Town Map 2/Day/Cafe_hover.png",
"acts==3","Backgrounds/Town Map 2/Day/Cafe_none.png",
"acts==2 and job=='cafe'", "Backgrounds/Town Map 2/Day/Cafe_hover.png",
"acts==2", "Backgrounds/Town Map 2/Day/Cafe_none.png",
"acts==1 and job=='cafe'", "Backgrounds/Town Map 2/Evening/Cafe_hover.png",
"acts==1", "Backgrounds/Town Map 2/Evening/Cafe_none.png",
"acts==0 and job=='cafe'", "Backgrounds/Town Map 2/Night/Cafe_hover.png",
"acts==0", "Backgrounds/Town Map 2/Night/Cafe_none.png",
"True", "Backgrounds/Town Map 2/Night/Cafe_hover.png"
)
image baridle = ConditionSwitch(
"acts==4 and job=='bar'","Backgrounds/Town Map 2/Evening/Bar_idle.png",
"acts==4","Backgrounds/Town Map 2/Evening/Bar_none.png",
"acts==3 and job=='bar'","Backgrounds/Town Map 2/Day/Bar_idle.png",
"acts==3","Backgrounds/Town Map 2/Day/Bar_none.png",
"acts==2 and job=='bar'", "Backgrounds/Town Map 2/Day/Bar_idle.png",
"acts==2", "Backgrounds/Town Map 2/Day/Bar_none.png",
"acts==1 and job=='bar'", "Backgrounds/Town Map 2/Evening/Bar_idle.png",
"acts==1", "Backgrounds/Town Map 2/Evening/Bar_none.png",
"acts==0 and job=='bar'", "Backgrounds/Town Map 2/Night/Bar_idle.png",
"acts==0", "Backgrounds/Town Map 2/Night/Bar_none.png",
"True", "Backgrounds/Town Map 2/Night/Bar_idle.png"
)
image barhover = ConditionSwitch(
"acts==4 and job=='bar'","Backgrounds/Town Map 2/Evening/Bar_hover.png",
"acts==4","Backgrounds/Town Map 2/Evening/Bar_none.png",
"acts==3 and job=='bar'","Backgrounds/Town Map 2/Day/Bar_hover.png",
"acts==3","Backgrounds/Town Map 2/Day/Bar_none.png",
"acts==2 and job=='bar'", "Backgrounds/Town Map 2/Day/Bar_hover.png",
"acts==2", "Backgrounds/Town Map 2/Day/Bar_none.png",
"acts==1 and job=='bar'", "Backgrounds/Town Map 2/Evening/Bar_hover.png",
"acts==1", "Backgrounds/Town Map 2/Evening/Bar_none.png",
"acts==0 and job=='bar'", "Backgrounds/Town Map 2/Night/Bar_hover.png",
"acts==0", "Backgrounds/Town Map 2/Night/Bar_none.png",
"True", "Backgrounds/Town Map 2/Night/Bar_hover.png"
)
image bakeryidle = ConditionSwitch(
"acts==4 and job=='bakery'","Backgrounds/Town Map 2/Evening/Bakery_idle.png",
"acts==4","Backgrounds/Town Map 2/Evening/Bakery_none.png",
"acts==3 and job=='bakery'","Backgrounds/Town Map 2/Day/Bakery_idle.png",
"acts==3","Backgrounds/Town Map 2/Day/Bakery_none.png",
"acts==2 and job=='bakery'", "Backgrounds/Town Map 2/Day/Bakery_idle.png",
"acts==2", "Backgrounds/Town Map 2/Day/Bakery_none.png",
"acts==1 and job=='bakery'", "Backgrounds/Town Map 2/Evening/Bakery_idle.png",
"acts==1", "Backgrounds/Town Map 2/Evening/Bakery_none.png",
"acts==0 and job=='bakery'", "Backgrounds/Town Map 2/Night/Bakery_idle.png",
"acts==0", "Backgrounds/Town Map 2/Night/Bakery_none.png",
"True", "Backgrounds/Town Map 2/Night/Bakery_idle.png"
)
image bakeryhover = ConditionSwitch(
"acts==4 and job=='bakery'","Backgrounds/Town Map 2/Evening/Bakery_hover.png",
"acts==4","Backgrounds/Town Map 2/Evening/Bakery_none.png",
"acts==3 and job=='bakery'","Backgrounds/Town Map 2/Day/Bakery_hover.png",
"acts==3","Backgrounds/Town Map 2/Day/Bakery_none.png",
"acts==2 and job=='bakery'", "Backgrounds/Town Map 2/Day/Bakery_hover.png",
"acts==2", "Backgrounds/Town Map 2/Day/Bakery_none.png",
"acts==1 and job=='bakery'", "Backgrounds/Town Map 2/Evening/Bakery_hover.png",
"acts==1", "Backgrounds/Town Map 2/Evening/Bakery_none.png",
"acts==0 and job=='bakery'", "Backgrounds/Town Map 2/Night/Bakery_hover.png",
"acts==0", "Backgrounds/Town Map 2/Night/Bakery_none.png",
"True", "Backgrounds/Town Map 2/Night/Bakery_hover.png"
)
image walkidle = ConditionSwitch(
"acts==4","Backgrounds/Town Map 2/Evening/WalkAround_idle.png",
"acts==3","Backgrounds/Town Map 2/Day/WalkAround_idle.png",
"acts==2", "Backgrounds/Town Map 2/Day/WalkAround_idle.png",
"acts==1", "Backgrounds/Town Map 2/Evening/WalkAround_idle.png",
"acts==0", "Backgrounds/Town Map 2/Night/WalkAround_idle.png",
"True", "Backgrounds/Town Map 2/Night/WalkAround_idle.png"
)
image walkhover = ConditionSwitch(
"acts==4","Backgrounds/Town Map 2/Evening/WalkAround_hover.png",
"acts==3","Backgrounds/Town Map 2/Day/WalkAround_hover.png",
"acts==2", "Backgrounds/Town Map 2/Day/WalkAround_hover.png",
"acts==1", "Backgrounds/Town Map 2/Evening/WalkAround_hover.png",
"acts==0", "Backgrounds/Town Map 2/Night/WalkAround_hover.png",
"True", "Backgrounds/Town Map 2/Night/WalkAround_hover.png"
)



image bg School = "Backgrounds/School.jpg"
image bg GymClub = "Backgrounds/MISC/Gym ClubDay.jpg"
image bg ClassroomD = "Backgrounds/Classroom.jpg"
image bg ClassroomE = "Backgrounds/ClassroomE.jpg"
image bg Lockeroom = "Backgrounds/MISC/Lockeroom.jpg"
image bg Wardrobe = "Backgrounds/MISC/Wardrobe.jpg"
image bg SchoolRestroom = "Backgrounds/School_Restroom.jpg"
image bg Bakery = "Backgrounds/Bakery/Bakery.jpg"
image bg BakeryOffice = "Backgrounds/Bakery/Bakery Office.jpg"
image bg HairSalon = "Backgrounds/Bakery/Salon.jpg"
image bg Bar = "Backgrounds/Bar/Bar.jpg"
image bg Cafe = "Backgrounds/Cafe/Cafe.jpg"
image bg CafeN = "Backgrounds/Cafe/Cafe (Night).jpg"
image bg Shop = "Backgrounds/Shop.jpg"
image bg LuxParty = "Backgrounds/MISC/VioletParty.jpg"
image bg Cafeteria = "Backgrounds/MISC/Cafeteria.jpg"
image bg Office = "Backgrounds/Office.jpg"
image bg FestD = "Backgrounds/Festival/Day.jpg"
image bg FestE = "Backgrounds/Festival/Evening.jpg"
image bg FestN = "Backgrounds/Festival/Night.jpg"
image bg Spa = "Backgrounds/MISC/Spa.jpg"
image powerout = "Backgrounds/MISC/poweroutage.png"
image mallchoose = "Backgrounds/MISC/Chooser.png"
image bg surgery = "Backgrounds/MISC/SurgeryCenter.jpg"
image bg hotel = "Backgrounds/MISC/Hotel.jpg"


image bg StripclubLobby = "Backgrounds/Stripclub/StripclubLobby.jpg"


image bg HomeE = "Backgrounds/Living Room/Living Room Afternoon.jpg"
image bg HomeD = "Backgrounds/Living Room/Living Room Day.jpg"
image bg HomeN = "Backgrounds/Living Room/Living Room Night.jpg"



image bg Gym = "Backgrounds/Clubs/Cheer/Gym Empty.jpg"
image bg Cheerlocker = "Backgrounds/Clubs/Cheer/Locker Room.jpg"

image bg Art = "Backgrounds/Clubs/Yearbook/Artroom.jpg"

image bg TrackD = "Backgrounds/Clubs/Track/Track Day.jpg"


define BedENH = "Backgrounds/Bedroom/Basic/Evening NHL.jpg"
define BedDNH = "Backgrounds/Bedroom/Basic/Day NHL.jpg"
define BedNNH = "Backgrounds/Bedroom/Basic/Night NHL.jpg"
define BedEH = "Backgrounds/Bedroom/Basic/Evening HL.jpg"
define BedDH = "Backgrounds/Bedroom/Basic/Day HL.jpg"
define BedNH = "Backgrounds/Bedroom/Basic/Night HL.jpg"

image bg RoomE = "[BedENH]"
image bg RoomD = "[BedDNH]"
image bg RoomN = "[BedNNH]"


image bg VioletHouseD = "Backgrounds/VioletHouse/Violet_House_Day.jpg"
image bg VioletHouseE = "Backgrounds/VioletHouse/Violet_House_Evening.jpg"
image bg VioletHouseN = "Backgrounds/VioletHouse/Violet_House_Night.jpg"

image bg VioletBedroom = "Backgrounds/VioletHouse/VioletRoom/violetbedroom.jpg"


image bg CityD = "Backgrounds/City/CityDay.jpg"
image bg CityE = "Backgrounds/City/CityMorning.jpg"
image bg CityN = "Backgrounds/City/CityNight.jpg"


image bg Karaoke1 = "Backgrounds/Areas/Karaoke Blank.jpg"
image bg Karaoke2 = "Backgrounds/Areas/Karaoke Maf.jpg"
image bg FarmersMarket = "Backgrounds/Areas/Farmers Market.jpg"
image bg DatePlace = "Backgrounds/Areas/ResturantCafe.jpg"


define chelseaPhone = "gui/phone.png"
define chelPhoneBack = "gui/phoneBack_%s.png"


image icon = "iconuni.png"
image bg EndGame = "Everyone.png"
image AiriLove = "airi.png"
image bg black = "Backgrounds/Black.jpg"


image catbed1 = "Characters/Cat/catbed1.png"
image catbedshop = "Characters/Cat/CatbedShop.png"
image catbed2 = "Characters/Cat/catbed.png"
image catsleep = "Characters/Cat/cat.png"
image catpost1 = "Characters/Cat/ScratchingPost1.png"
image catpostshop = "Characters/Cat/CatpostShop.png"
image catpost2 = "Characters/Cat/ScratchingPost2.png"
image catwater = "Characters/Cat/Waterbowl.png"
image catfood1 = "Characters/Cat/Foodbowl Full.png"
image catfoodshop = "Characters/Cat/CatfoodShop.png"
image catfood2 = "Characters/Cat/Foodbowl Half.png"
image catfood3 = "Characters/Cat/Foodbowl Empty.png"
image catfoodeat = "Characters/Cat/FoodBowl FullCat.png"
image catnews = "Characters/Cat/catnews.png"







image bg CafeKate = "Scenes/Cafe/Intro.png"


image bg KS1 = "Scenes/Kate Sick/1.png"
image bg KS2 = "Scenes/Kate Sick/2.png"
image bg KS3 = "Scenes/Kate Sick/3.png"
image bg KS4 = "Scenes/Kate Sick/4.png"
image bg KS5 = "Scenes/Kate Sick/5.png"
image bg KS6 = "Scenes/Kate Sick/6.png"
image bg KS7 = "Scenes/Kate Sick/7.png"
image bg KS8 = "Scenes/Kate Sick/8.png"
image bg KS9 = "Scenes/Kate Sick/9.png"
image bg KS10 = "Scenes/Kate Sick/10.png"
image bg KS11 = "Scenes/Kate Sick/11.png"


image bg KateHug = "Scenes/Kate Hug&Kiss/01.png"
image bg KateKiss = "Scenes/Kate Hug&Kiss/02.png"


image bg KateDogs = "Scenes/Kate&Dogs/Kate&Dogs.png"


image bg KCCS1 = "Scenes/Kate Couch Scene/1.png"
image bg KCCS2 = "Scenes/Kate Couch Scene/2.png"
image bg KCCS3 = "Scenes/Kate Couch Scene/3.png"

image bg KCCS5 = "Scenes/Kate Couch Scene/5.png"
image bg KCCS6 = "Scenes/Kate Couch Scene/6.png"
image bg KCCS7 = "Scenes/Kate Couch Scene/7.png"
image bg KCCS8 = "Scenes/Kate Couch Scene/8.png"
image bg KCCS9 = "Scenes/Kate Couch Scene/9.png"
image bg KCCS10 = "Scenes/Kate Couch Scene/10.png"


image bg KCP1 = "Scenes/Kate Picnic/1.png"
image bg KCP2 = "Scenes/Kate Picnic/2.png"


image KPSS = "Scenes/Phone Images/KatePenguinSelfie.png"


image bg KZD1 = "Scenes/Kate Zoo/G1.png"
image bg KZD2 = "Scenes/Kate Zoo/G2.png"
image bg KZD3 = "Scenes/Kate Zoo/G3.png"
image bg KZD4 = "Scenes/Kate Zoo/Go1.png"
image bg KZD5 = "Scenes/Kate Zoo/P1.png"


image bg KCM1 = "Scenes/Kate & Chelsea Makeout/1.png"
image bg KCM2 = "Scenes/Kate & Chelsea Makeout/2.png"
image bg KCM3 = "Scenes/Kate & Chelsea Makeout/3.png"
image bg KCM4 = "Scenes/Kate & Chelsea Makeout/4.png"
image bg KCM5 = "Scenes/Kate & Chelsea Makeout/5.png"
image bg KCM6 = "Scenes/Kate & Chelsea Makeout/6.png"
image bg KCM7 = "Scenes/Kate & Chelsea Makeout/7.png"
image bg KCM8 = "Scenes/Kate & Chelsea Makeout/8.png"
image bg KCM9 = "Scenes/Kate & Chelsea Makeout/9.png"


image bg KSS1 = "Scenes/Kate Sex Scene/1.png"
image bg KSS2 = "Scenes/Kate Sex Scene/2.png"
image bg KSS3 = "Scenes/Kate Sex Scene/3.png"
image bg KSS4 = "Scenes/Kate Sex Scene/4.png"
image bg KSS5 = "Scenes/Kate Sex Scene/5.png"
image bg KSS6 = "Scenes/Kate Sex Scene/6.png"
image bg KSS7 = "Scenes/Kate Sex Scene/7.png"


image bg CPS1 = "Scenes/Cafe Panties/1.jpg"
image bg CPS2 = "Scenes/Cafe Panties/2.png"
image bg CPS3 = "Scenes/Cafe Panties/3.png"


image bg CL1 = "Scenes/Cafe Lap Scene/01-1.png"
image bg CL2 = "Scenes/Cafe Lap Scene/02-1.png"
image bg CL3 = "Scenes/Cafe Lap Scene/03-1.png"
image bg CL4 = "Scenes/Cafe Lap Scene/04-1.png"
image bg CL5 = "Scenes/Cafe Lap Scene/05-2.png"
image bg CL6 = "Scenes/Cafe Lap Scene/06-2.png"
image bg CL7 = "Scenes/Cafe Lap Scene/07-2.png"
image bg CL8 = "Scenes/Cafe Lap Scene/08-2.png"


image bg Car1 = "Scenes/Cafe Car/001.png"
image bg Car2 = "Scenes/Cafe Car/002.png"
image bg Car3 = "Scenes/Cafe Car/003.png"
image bg Car4 = "Scenes/Cafe Car/004.png"
image bg Car5 = "Scenes/Cafe Car/005.png"
image bg Car6 = "Scenes/Cafe Car/006.png"
image bg Car7 = "Scenes/Cafe Car/007.png"
image bg Car8 = "Scenes/Cafe Car/008.png"
image bg Car9 = "Scenes/Cafe Car/009.png"


image bg CafeGrope = "Scenes/Cafe Grope/1.png"


image bg CBS1 = "Scenes/Cafe Bathroom/1.png"
image bg CBS2 = "Scenes/Cafe Bathroom/2.png"
image bg CBS3 = "Scenes/Cafe Bathroom/3.png"
image bg CBS4 = "Scenes/Cafe Bathroom/4.png"
image bg CBS5 = "Scenes/Cafe Bathroom/5.png"
image bg CBS6 = "Scenes/Cafe Bathroom/6.png"
image bg CBS7 = "Scenes/Cafe Bathroom/7.png"
image bg CBS8 = "Scenes/Cafe Bathroom/8.png"
image bg CBS9 = "Scenes/Cafe Bathroom/9.png"
image bg CBS10 = "Scenes/Cafe Bathroom/10.png"


image bg CASK1 = "Scenes/Cafe Alley 01/1.png"
image bg CASK2 = "Scenes/Cafe Alley 01/2.png"
image bg CASK3 = "Scenes/Cafe Alley 01/3.png"
image bg CASK4 = "Scenes/Cafe Alley 01/4.png"
image bg CASK5 = "Scenes/Cafe Alley 01/5.png"
image bg CASK6 = "Scenes/Cafe Alley 01/6.png"
image bg CASK7 = "Scenes/Cafe Alley 01/7.png"
image bg CASK8 = "Scenes/Cafe Alley 01/8.png"
image bg CASK9 = "Scenes/Cafe Alley 01/9.png"
image bg CASK10 = "Scenes/Cafe Alley 01/10.png"


image bg CASC1 = "Scenes/Cafe Alley 02/1.png"
image bg CASC2 = "Scenes/Cafe Alley 02/2.png"
image bg CASC3 = "Scenes/Cafe Alley 02/3.png"
image bg CASC6 = "Scenes/Cafe Alley 02/6.png"
image bg CASC7 = "Scenes/Cafe Alley 02/7.png"
image bg CASC8 = "Scenes/Cafe Alley 02/8.png"
image bg CASC9 = "Scenes/Cafe Alley 02/9.png"
image bg CASC10 = "Scenes/Cafe Alley 02/10.png"


image bg CT1 = "Scenes/Cafe Threesome/1.png"
image bg CT2 = "Scenes/Cafe Threesome/2.png"
image bg CT3 = "Scenes/Cafe Threesome/3.png"
image bg CT4 = "Scenes/Cafe Threesome/4.png"
image bg CT5 = "Scenes/Cafe Threesome/5.png"
image bg CT6 = "Scenes/Cafe Threesome/6.png"
image bg CT7 = "Scenes/Cafe Threesome/7.png"
image bg CT8 = "Scenes/Cafe Threesome/8.png"
image bg CT9 = "Scenes/Cafe Threesome/9.png"
image bg CT10 = "Scenes/Cafe Threesome/10.png"
image bg CT11 = "Scenes/Cafe Threesome/11.png"
image bg CT12 = "Scenes/Cafe Threesome/12.png"
image bg CT13 = "Scenes/Cafe Threesome/13.png"
image bg CT14 = "Scenes/Cafe Threesome/14.png"
image bg CT15 = "Scenes/Cafe Threesome/15.png"
image bg CT16 = "Scenes/Cafe Threesome/16.png"
image bg CT17 = "Scenes/Cafe Threesome/17.png"
image bg CT18 = "Scenes/Cafe Threesome/18.png"
image bg CT19 = "Scenes/Cafe Threesome/19.png"
image bg CT20 = "Scenes/Cafe Threesome/20.png"
image bg CT21 = "Scenes/Cafe Threesome/21.png"
image bg CT22 = "Scenes/Cafe Threesome/22.png"
image bg CT23 = "Scenes/Cafe Threesome/23.png"
image bg CT24 = "Scenes/Cafe Threesome/24.png"
image bg CT25 = "Scenes/Cafe Threesome/25.png"
image bg CT26 = "Scenes/Cafe Threesome/26.png"
image bg CT27 = "Scenes/Cafe Threesome/27.png"
image bg CT28 = "Scenes/Cafe Threesome/28.png"
image bg CT29 = "Scenes/Cafe Threesome/29.png"
image bg CT30 = "Scenes/Cafe Threesome/30.png"
image bg CT31 = "Scenes/Cafe Threesome/31.png"
image bg CT32 = "Scenes/Cafe Threesome/32.png"


image bg CLRS1 = "Scenes/Cafe Locker Scene/1.png"
image bg CLRS2 = "Scenes/Cafe Locker Scene/2.png"
image bg CLRS3 = "Scenes/Cafe Locker Scene/3.png"
image bg CLRS4 = "Scenes/Cafe Locker Scene/4.png"


image bg CCD1 = "Scenes/ChelseaXDaniel/1.png"
image bg CCD2 = "Scenes/ChelseaXDaniel/2.png"
image bg CCD3 = "Scenes/ChelseaXDaniel/3.png"
image bg CCD4 = "Scenes/ChelseaXDaniel/4.png"



image bg BRS1 = "Scenes/Bar Restroom Scene/1.png"
image bg BRS2 = "Scenes/Bar Restroom Scene/2.png"


image bg BGS1 = "Scenes/Bar Grope/1.png"
image bg BGS2b = "Scenes/Bar Grope/2b.png"
image bg BGS3 = "Scenes/Bar Grope/3.png"
image bg BGS4 = "Scenes/Bar Grope/4.png"
image bg BGS5 = "Scenes/Bar Grope/5.png"
image bg BGS6 = "Scenes/Bar Grope/6.png"
image bg BGS7 = "Scenes/Bar Grope/7.png"


image bg BDanielS1 = "Scenes/Bar Daniel X Chelsea/1.png"


image bg BKS1 = "Scenes/Bar Kate Scene/1.png"
image bg BKS2 = "Scenes/Bar Kate Scene/2.png"
image bg BKS3 = "Scenes/Bar Kate Scene/3.png"


image bg BMGS1 = "Scenes/Bar Muscle Guy/1.png"
image bg BMGS2 = "Scenes/Bar Muscle Guy/2.png"
image bg BMGS3 = "Scenes/Bar Muscle Guy/3.png"


image bg BHS1 = "Scenes/Bar Hotel Scene/1.png"
image bg BHS2 = "Scenes/Bar Hotel Scene/2.png"
image bg BHS3 = "Scenes/Bar Hotel Scene/3.png"


image bg BCS1 = "Scenes/Bar Couple Scene/1.png"
image bg BCS2 = "Scenes/Bar Couple Scene/2.png"
image bg BCS3 = "Scenes/Bar Couple Scene/3.png"
image bg BCS4 = "Scenes/Bar Couple Scene/4.png"
image bg BCS5 = "Scenes/Bar Couple Scene/5.png"
image bg BCS6 = "Scenes/Bar Couple Scene/6.png"
image bg BCS7 = "Scenes/Bar Couple Scene/7.png"
image bg BCS8 = "Scenes/Bar Couple Scene/8.png"
image bg BCS9 = "Scenes/Bar Couple Scene/9.png"
image bg BCS10 = "Scenes/Bar Couple Scene/10.png"
image bg BCS11 = "Scenes/Bar Couple Scene/11.png"
image bg BCS12 = "Scenes/Bar Couple Scene/12.png"
image bg BCS13 = "Scenes/Bar Couple Scene/13.png"
image bg BCS14 = "Scenes/Bar Couple Scene/14.png"
image bg BCS15 = "Scenes/Bar Couple Scene/15.png"
image bg BCS16 = "Scenes/Bar Couple Scene/16.png"
image bg BCS17 = "Scenes/Bar Couple Scene/17.png"
image bg BCS18 = "Scenes/Bar Couple Scene/18.png"


image bg BakeryLisa = "Scenes/Bakery/Intro.png"


image bg KL11 = "Scenes/KeithXLisa01/KL1-1.png"
image bg KL12 = "Scenes/KeithXLisa01/KL1-2.png"
image bg KL13 = "Scenes/KeithXLisa01/KL1-3.png"
image bg KL14 = "Scenes/KeithXLisa01/KL1-4.png"
image bg KL15 = "Scenes/KeithXLisa01/KL1-5.png"
image bg KL16 = "Scenes/KeithXLisa01/KL1-6.png"
image bg KL17 = "Scenes/KeithXLisa01/KL1-7.png"
image bg KL21 = "Scenes/KeithXLisa01/KL2-1.png"
image bg KL22 = "Scenes/KeithXLisa01/KL2-2.png"
image bg KL23 = "Scenes/KeithXLisa01/KL2-3.png"
image bg KL25 = "Scenes/KeithXLisa01/KL2-5.png"
image bg KL26 = "Scenes/KeithXLisa01/KL2-6.png"
image bg KL27 = "Scenes/KeithXLisa01/KL2-7.png"


image bg KL1 = "Scenes/KeithXLisa02/1.png"
image bg KL2 = "Scenes/KeithXLisa02/2.png"
image bg KL3 = "Scenes/KeithXLisa02/3.png"
image bg KL4 = "Scenes/KeithXLisa02/4.png"
image bg KL5 = "Scenes/KeithXLisa02/5.png"
image bg KL6 = "Scenes/KeithXLisa02/6.png"
image bg KL7 = "Scenes/KeithXLisa02/7.png"


image LPhone1 = "Scenes/Bakery/LisaPhone1.png"
image LPhone2 = "Scenes/Bakery/LisaPhone2.png"


image bg Mall1 = "Scenes/Mall Makeup/1.png"
image bg Mall2 = "Scenes/Mall Makeup/2.png"
image bg Mall3 = "Scenes/Mall Makeup/3.png"
image bg Mall4 = "Scenes/Mall Makeup/4.png"


image bg BMC1 = "Scenes/Mall Clothes/1.png"
image bg BMC2 = "Scenes/Mall Clothes/2.png"
image bg BMC3 = "Scenes/Mall Clothes/3.png"


image bg BRL1 = "Scenes/Bakery Route Lock/1.png"
image bg BRL2 = "Scenes/Bakery Route Lock/2.png"
image bg BRL3 = "Scenes/Bakery Route Lock/3.png"


image bg VDScene1 = "Scenes/DateCGs/1.png"
image bg VDScene2 = "Scenes/DateCGs/2.png"
image bg VDScene3 = "Scenes/DateCGs/3.png"
image bg KDScene1 = "Scenes/DateCGs/4.png"
image bg KDScene2 = "Scenes/DateCGs/5.png"
image bg KDScene3 = "Scenes/DateCGs/6.png"
image bg DDScene1 = "Scenes/DateCGs/7.png"
image bg DDScene2 = "Scenes/DateCGs/8.png"
image bg DDScene3 = "Scenes/DateCGs/9.png"


image bg MattGrab = "Scenes/MattGrope/MattGrab1.png"
image bg MattSlap = "Scenes/MattGrope/MattGrabSlap.png"
image bg MattScream = "Scenes/MattGrope/MattGrabScream.png"
image bg MattAccept = "Scenes/MattGrope/MattGrab2.png"


image bg MBat1 = "Scenes/Matt Bathroom/001.png"
image bg MBat2 = "Scenes/Matt Bathroom/002.png"
image bg MBat3 = "Scenes/Matt Bathroom/003.png"
image bg MBat4 = "Scenes/Matt Bathroom/004Panty.png"


image bg Mphoto = "Scenes/Matt Photo/1.png"
image ChelseaMaidSelfie = "Scenes/Phone Images/ChelseaMaidOutfit.png"


image MattPhone = "Scenes/Matt Lockerroom/MattPhone.png"
image MattPhone2 = "Scenes/Matt Lockerroom/MattPhone2.png"
image MattPhone3 = "Scenes/Matt Lockerroom/MattPhone3.png"
image bg MLock1 = "Scenes/Matt Lockerroom/001.png"
image bg MLock2 = "Scenes/Matt Lockerroom/002.png"
image bg MLock3 = "Scenes/Matt Lockerroom/003.png"
image bg MLock4 = "Scenes/Matt Lockerroom/004.png"
image bg MLock5 = "Scenes/Matt Lockerroom/005.png"
image bg MLock6 = "Scenes/Matt Lockerroom/006.png"
image bg MLock7 = "Scenes/Matt Lockerroom/007.png"
image bg MLock8 = "Scenes/Matt Lockerroom/008.png"
image bg MLock9 = "Scenes/Matt Lockerroom/009.png"
image bg MLock10 = "Scenes/Matt Lockerroom/010.png"
image bg MLock11 = "Scenes/Matt Lockerroom/011.png"
image bg MLock12 = "Scenes/Matt Lockerroom/012.png"
image bg MLock13 = "Scenes/Matt Lockerroom/013.png"
image bg MLock14 = "Scenes/Matt Lockerroom/014.png"


image bg MApt11 = "Scenes/AlexMattThreesome/1-1.png"
image bg MApt12 = "Scenes/AlexMattThreesome/1-2.png"
image bg MApt13 = "Scenes/AlexMattThreesome/1-3.png"
image bg MApt14 = "Scenes/AlexMattThreesome/1-4.png"
image bg MApt15 = "Scenes/AlexMattThreesome/1-5.png"
image bg MApt21 = "Scenes/AlexMattThreesome/2-1.png"
image bg MApt22 = "Scenes/AlexMattThreesome/2-2.png"
image bg MApt23 = "Scenes/AlexMattThreesome/2-3.png"
image bg MApt24 = "Scenes/AlexMattThreesome/2-4.png"
image bg MApt25 = "Scenes/AlexMattThreesome/2-5.png"


image bg MAA1 = "Scenes/MattAlex Alley Scene/1.jpg"
image bg MAA2 = "Scenes/MattAlex Alley Scene/2.jpg"
image bg MAA3 = "Scenes/MattAlex Alley Scene/3.jpg"
image bg MAA4 = "Scenes/MattAlex Alley Scene/4.png"
image bg MAA5 = "Scenes/MattAlex Alley Scene/5.png"
image bg MAA6 = "Scenes/MattAlex Alley Scene/6.png"
image bg MAA7 = "Scenes/MattAlex Alley Scene/7.png"
image bg MAA8 = "Scenes/MattAlex Alley Scene/8.png"
image bg MAA9 = "Scenes/MattAlex Alley Scene/9.png"
image bg MAA10 = "Scenes/MattAlex Alley Scene/10.png"
image bg MAA11 = "Scenes/MattAlex Alley Scene/11.png"
image bg MAA12 = "Scenes/MattAlex Alley Scene/12.png"
image bg MAA13 = "Scenes/MattAlex Alley Scene/13.png"
image bg MAA14 = "Scenes/MattAlex Alley Scene/14.png"
image bg MAA15 = "Scenes/MattAlex Alley Scene/15.png"


image bg MBS1 = "Scenes/Matt Blowjob/1.png"
image bg MBS2 = "Scenes/Matt Blowjob/2.png"
image bg MBS3 = "Scenes/Matt Blowjob/3.png"
image bg MBS4 = "Scenes/Matt Blowjob/4.png"
image bg MBS5 = "Scenes/Matt Blowjob/5.png"
image bg MBS6 = "Scenes/Matt Blowjob/6.png"
image bg MBS7 = "Scenes/Matt Blowjob/7.png"
image bg MBS8 = "Scenes/Matt Blowjob/8.png"
image bg MBS9 = "Scenes/Matt Blowjob/9.png"
image bg MBS10 = "Scenes/Matt Blowjob/10.png"
image bg MBS11 = "Scenes/Matt Blowjob/11.png"
image bg MBS12 = "Scenes/Matt Blowjob/12.png"
image bg MBS13 = "Scenes/Matt Blowjob/13.png"
image bg MBS14 = "Scenes/Matt Blowjob/14.png"
image bg MBS15 = "Scenes/Matt Blowjob/15.png"
image bg MBS16 = "Scenes/Matt Blowjob/16.png"
image bg MBS17 = "Scenes/Matt Blowjob/17.png"


image bg MDS1 = "Scenes/Matt Doggy/1.png"
image bg MDS2 = "Scenes/Matt Doggy/2.png"
image bg MDS3 = "Scenes/Matt Doggy/3.png"
image bg MDS4 = "Scenes/Matt Doggy/4.png"


image bg MBarS1 = "Scenes/Matt Bar/1.png"


image bg MCCS1 = "Scenes/CM/1.png"
image bg MCCS2 = "Scenes/CM/2.png"
image bg MCCS3 = "Scenes/CM/3.png"
image bg MCCS4 = "Scenes/CM/4.png"
image bg MCCS5 = "Scenes/CM/5.png"
image bg MCCS6 = "Scenes/CM/6.png"
image bg MCCS7 = "Scenes/CM/7.png"
image bg MCCS8 = "Scenes/CM/8.png"
image bg MCCS9 = "Scenes/CM/9.png"
image bg MCCS10 = "Scenes/CM/10.png"
image bg MCCS11 = "Scenes/CM/11.png"
image bg MCCS12 = "Scenes/CM/12.png"
image bg MCCS13 = "Scenes/CM/13.png"
image bg MCCS14 = "Scenes/CM/14.png"
image bg MCCS16 = "Scenes/CM/16.png"
image bg MCCS17 = "Scenes/CM/17.png"


image bg MCDCS1 = "Scenes/CMD/1.png"
image bg MCDCS2 = "Scenes/CMD/2.png"
image bg MCDCS3 = "Scenes/CMD/3.png"
image bg MCDCS4 = "Scenes/CMD/4.png"
image bg MCDCS5 = "Scenes/CMD/5.png"
image bg MCDCS6 = "Scenes/CMD/6.png"
image bg MCDCS7 = "Scenes/CMD/7.png"
image bg MCDCS8 = "Scenes/CMD/8.png"
image bg MCDCS9 = "Scenes/CMD/9.png"
image bg MCDCS10 = "Scenes/CMD/10.png"
image bg MCDCS11 = "Scenes/CMD/11.png"
image bg MCDCS12 = "Scenes/CMD/12.png"
image bg MCDCS13 = "Scenes/CMD/13.png"


image bg MattBusScene1 = "Scenes/Matt Bus/1.png"
image bg MattBusScene2 = "Scenes/Matt Bus/2.png"


image bg MBCS1 = "Scenes/Matt Bakery Conflict/1.png"
image bg MBCS2 = "Scenes/Matt Bakery Conflict/2.png"
image bg MBCS3 = "Scenes/Matt Bakery Conflict/3.png"
image bg MBCS4 = "Scenes/Matt Bakery Conflict/4.png"
image bg MBCS5 = "Scenes/Matt Bakery Conflict/5.png"
image bg MBCS6 = "Scenes/Matt Bakery Conflict/6.png"
image bg MBCS7 = "Scenes/Matt Bakery Conflict/7.png"
image bg MBCS8 = "Scenes/Matt Bakery Conflict/8.png"
image bg MBCS9 = "Scenes/Matt Bakery Conflict/9.png"


image bg MattMafia1 = "Scenes/Matt Mafia Scene/1.png"
image bg MattMafia2 = "Scenes/Matt Mafia Scene/2.png"
image bg MattMafia3 = "Scenes/Matt Mafia Scene/3.png"
image bg MattMafia4 = "Scenes/Matt Mafia Scene/4.png"
image bg MattMafia5 = "Scenes/Matt Mafia Scene/5.png"
image bg MattMafia6 = "Scenes/Matt Mafia Scene/6.png"
image bg MattMafia7 = "Scenes/Matt Mafia Scene/7.png"



image bg DMS1 = "Scenes/Damien Movie/1.png"
image bg DMS2 = "Scenes/Damien Movie/2.png"
image bg DMS3 = "Scenes/Damien Movie/3.png"


image bg DKS1 = "Scenes/Damien Festival/1.png"
image bg DKS2 = "Scenes/Damien Festival/2.png"
image bg DKS3 = "Scenes/Damien Festival/3.png"
image bg DKS4 = "Scenes/Damien Festival/4.png"


image DMSS1 = "Scenes/Phone Images/UnderwearselfiePhone.png"
image DMSS2 = "Scenes/Phone Images/Underwearselfie.png"

image DCCS = "Scenes/Phone Images/DamienCoco.png"


image bg DYS1 = "Scenes/Damien Club Scenes/Yearbook Scene/1.png"
image bg DYS2 = "Scenes/Damien Club Scenes/Yearbook Scene/2.png"
image bg DYS3 = "Scenes/Damien Club Scenes/Yearbook Scene/3.png"
image bg DYS4 = "Scenes/Damien Club Scenes/Yearbook Scene/4.png"


image bg DCS1 = "Scenes/Damien Club Scenes/Cheer Scene/1.png"
image bg DCS2 = "Scenes/Damien Club Scenes/Cheer Scene/2.png"
image bg DCS3 = "Scenes/Damien Club Scenes/Cheer Scene/3.png"
image bg DCS4 = "Scenes/Damien Club Scenes/Cheer Scene/4.png"


image bg DTS1 = "Scenes/Damien Club Scenes/Track Scene/1.png"
image bg DTS2 = "Scenes/Damien Club Scenes/Track Scene/2.png"


image bg DBS1 = "Scenes/Damien Bar/1.png"


image bg DAHS1 = "Scenes/Damien Chelsea After Homecoming/1.png"
image bg DAHS2 = "Scenes/Damien Chelsea After Homecoming/2.png"
image bg DAHS3 = "Scenes/Damien Chelsea After Homecoming/3.png"
image bg DAHS4 = "Scenes/Damien Chelsea After Homecoming/4.png"
image bg DAHS5 = "Scenes/Damien Chelsea After Homecoming/5.png"
image bg DAHS6 = "Scenes/Damien Chelsea After Homecoming/6.png"
image bg DAHS7 = "Scenes/Damien Chelsea After Homecoming/7.png"
image bg DAHS8 = "Scenes/Damien Chelsea After Homecoming/8.png"
image bg DAHS9 = "Scenes/Damien Chelsea After Homecoming/9.png"
image bg DAHS10 = "Scenes/Damien Chelsea After Homecoming/10.png"
image bg DAHS11 = "Scenes/Damien Chelsea After Homecoming/11.png"
image bg DAHS12 = "Scenes/Damien Chelsea After Homecoming/12.png"
image bg DAHS13 = "Scenes/Damien Chelsea After Homecoming/13.png"
image bg DAHS14 = "Scenes/Damien Chelsea After Homecoming/14.png"
image bg DAHS15 = "Scenes/Damien Chelsea After Homecoming/15.png"
image bg DAHS16 = "Scenes/Damien Chelsea After Homecoming/16.png"
image bg DAHS17 = "Scenes/Damien Chelsea After Homecoming/17.png"
image bg DAHS18 = "Scenes/Damien Chelsea After Homecoming/18.png"
image bg DAHS19 = "Scenes/Damien Chelsea After Homecoming/19.png"
image bg DAHS20 = "Scenes/Damien Chelsea After Homecoming/20.png"
image bg DAHS21 = "Scenes/Damien Chelsea After Homecoming/21.png"
image bg DAHS22 = "Scenes/Damien Chelsea After Homecoming/22.png"
image bg DAHS23 = "Scenes/Damien Chelsea After Homecoming/23.png"
image bg DAHS24 = "Scenes/Damien Chelsea After Homecoming/24.png"


image bg DADS1 = "Scenes/Damien Aquarium Scenes/1.png"
image bg DADS2 = "Scenes/Damien Aquarium Scenes/2.png"
image bg DADS3 = "Scenes/Damien Aquarium Scenes/3.png"
image bg DADS4 = "Scenes/Damien Aquarium Scenes/4.png"
image bg DADS5 = "Scenes/Damien Aquarium Scenes/5.png"



image bg VDomKiss = "Scenes/MCXViolet Dom/001.png"
image bg VSubKiss = "Scenes/MCXViolet Sub/001.png"


image bg VFlix = "Scenes/ApartSleep/1.png"


image bg VSpa1 = "Scenes/ApartSleep/01.png"
image bg VSpa2 = "Scenes/ApartSleep/02.png"
image bg VSpa3 = "Scenes/ApartSleep/03.png"


image bg Sleep1 = "Scenes/ApartSleep/001.png"
image bg Sleep2 = "Scenes/ApartSleep/002.png"
image bg Sleep3 = "Scenes/ApartSleep/003.png"


image bg Spa11 = "Scenes/Spa/11.png"
image bg Spa12 = "Scenes/Spa/12.png"
image bg Spa13 = "Scenes/Spa/13.png"
image bg Spa14 = "Scenes/Spa/14.png"
image bg Spa15 = "Scenes/Spa/15.png"
image bg Spa16 = "Scenes/Spa/16.png"

image bg Spa21 = "Scenes/Spa/21.png"
image bg Spa22 = "Scenes/Spa/22.png"
image bg Spa23 = "Scenes/Spa/23.png"
image bg Spa24 = "Scenes/Spa/24.png"
image bg Spa251 = "Scenes/Spa/251.png"
image bg Spa262 = "Scenes/Spa/262.png"
image bg Spa273 = "Scenes/Spa/273.png"
image bg Spa284 = "Scenes/Spa/284.png"
image bg Spa295 = "Scenes/Spa/295.png"

image bg Spa31 = "Scenes/Spa/31.png"
image bg Spa32 = "Scenes/Spa/32.png"


image bg VStrip1 = "Scenes/Violet Sub Striptease/1.png"
image bg VStrip2 = "Scenes/Violet Sub Striptease/2.png"
image bg VStrip3 = "Scenes/Violet Sub Striptease/3.png"
image bg VStrip4 = "Scenes/Violet Sub Striptease/4.png"
image bg VStrip5 = "Scenes/Violet Sub Striptease/5.png"
image bg VStrip6 = "Scenes/Violet Sub Striptease/6.png"
image bg VStrip7 = "Scenes/Violet Sub Striptease/7.png"
image bg VStrip8 = "Scenes/Violet Sub Striptease/8.png"
image bg VStrip9 = "Scenes/Violet Sub Striptease/9.png"
image bg VStrip10 = "Scenes/Violet Sub Striptease/10.png"
image bg VStrip11 = "Scenes/Violet Sub Striptease/11.png"
image bg VStrip12 = "Scenes/Violet Sub Striptease/12.png"
image bg VStrip13 = "Scenes/Violet Sub Striptease/13.png"
image bg VStrip14 = "Scenes/Violet Sub Striptease/14.png"
image bg VStrip15 = "Scenes/Violet Sub Striptease/15.png"
image bg VStrip16 = "Scenes/Violet Sub Striptease/16.png"
image bg VStrip17 = "Scenes/Violet Sub Striptease/17.png"
image bg VStrip18 = "Scenes/Violet Sub Striptease/18.png"
image bg VStrip19 = "Scenes/Violet Sub Striptease/19.png"
image bg VStrip20 = "Scenes/Violet Sub Striptease/20.png"
image bg VStrip21 = "Scenes/Violet Sub Striptease/21.png"
image bg VStrip22 = "Scenes/Violet Sub Striptease/22.png"
image bg VStrip23 = "Scenes/Violet Sub Striptease/23.png"
image bg VStrip24 = "Scenes/Violet Sub Striptease/24.png"
image bg VStrip25 = "Scenes/Violet Sub Striptease/25.png"
image bg VStrip26 = "Scenes/Violet Sub Striptease/26.png"
image bg VStrip27 = "Scenes/Violet Sub Striptease/27.png"


image bg VSSB1 = "Scenes/Violet Sub School Bathroom/1.png"
image bg VSSB2 = "Scenes/Violet Sub School Bathroom/2.png"
image bg VSSB3 = "Scenes/Violet Sub School Bathroom/3.png"


image bg VSDDS1 = "Scenes/Violet Sub Dinner Date/1.png"
image bg VSDDS2 = "Scenes/Violet Sub Dinner Date/2.png"
image bg VSDDS3 = "Scenes/Violet Sub Dinner Date/3.png"
image bg VSDDS4 = "Scenes/Violet Sub Dinner Date/4.png"
image bg VSDDS5 = "Scenes/Violet Sub Dinner Date/5.png"
image bg VSDDS6 = "Scenes/Violet Sub Dinner Date/6.png"
image bg VSDDS7 = "Scenes/Violet Sub Dinner Date/7.png"
image bg VSDDS8 = "Scenes/Violet Sub Dinner Date/8.png"
image bg VSDDS9 = "Scenes/Violet Sub Dinner Date/9.png"
image bg VSDDS10 = "Scenes/Violet Sub Dinner Date/10.png"
image bg VSDDS11 = "Scenes/Violet Sub Dinner Date/11.png"
image bg VSDDS12 = "Scenes/Violet Sub Dinner Date/12.png"
image bg VSDDS13 = "Scenes/Violet Sub Dinner Date/13.png"
image bg VSDDS14 = "Scenes/Violet Sub Dinner Date/14.png"
image bg VSDDS15 = "Scenes/Violet Sub Dinner Date/15.png"


image bg VSubBedroom1 = "Scenes/Violet Sub Bedroom/1.png"
image bg VSubBedroom2 = "Scenes/Violet Sub Bedroom/2.png"
image bg VSubBedroom3 = "Scenes/Violet Sub Bedroom/3.png"
image bg VSubBedroom4 = "Scenes/Violet Sub Bedroom/4.png"
image bg VSubBedroom5 = "Scenes/Violet Sub Bedroom/5.png"
image bg VSubBedroom6 = "Scenes/Violet Sub Bedroom/6.png"
image bg VSubBedroom7 = "Scenes/Violet Sub Bedroom/7.png"
image bg VSubBedroom8 = "Scenes/Violet Sub Bedroom/8.png"
image bg VSubBedroom9 = "Scenes/Violet Sub Bedroom/9.png"
image bg VSubBedroom10 = "Scenes/Violet Sub Bedroom/10.png"
image bg VSubBedroom11 = "Scenes/Violet Sub Bedroom/11.png"
image bg VSubBedroom12 = "Scenes/Violet Sub Bedroom/12.png"
image bg VSubBedroom13 = "Scenes/Violet Sub Bedroom/13.png"
image bg VSubBedroom14 = "Scenes/Violet Sub Bedroom/14.png"
image bg VSubBedroom15 = "Scenes/Violet Sub Bedroom/15.png"
image bg VSubBedroom16 = "Scenes/Violet Sub Bedroom/16.png"
image bg VSubBedroom17 = "Scenes/Violet Sub Bedroom/17.png"
image bg VSubBedroom18 = "Scenes/Violet Sub Bedroom/18.png"
image bg VSubBedroom19 = "Scenes/Violet Sub Bedroom/19.png"


image bg VBackseat1 = "Scenes/Violet Backseat/1.png"
image bg VBackseat2 = "Scenes/Violet Backseat/2.png"
image bg VBackseat3 = "Scenes/Violet Backseat/3.png"
image bg VBackseat4 = "Scenes/Violet Backseat/4.png"
image bg VBackseat5 = "Scenes/Violet Backseat/5.png"
image bg VBackseat6 = "Scenes/Violet Backseat/6.png"
image bg VBackseat7 = "Scenes/Violet Backseat/7.png"
image bg VBackseat11 = "Scenes/Violet Backseat/1-1.png"


image bg VDomBedroom1 = "Scenes/Violet Dom Bedroom/1.png"
image bg VDomBedroom2 = "Scenes/Violet Dom Bedroom/2.png"
image bg VDomBedroom3 = "Scenes/Violet Dom Bedroom/3.png"
image bg VDomBedroom4 = "Scenes/Violet Dom Bedroom/4.png"
image bg VDomBedroom5 = "Scenes/Violet Dom Bedroom/5.png"
image bg VDomBedroom6 = "Scenes/Violet Dom Bedroom/6.png"
image bg VDomBedroom7 = "Scenes/Violet Dom Bedroom/7.png"
image bg VDomBedroom8 = "Scenes/Violet Dom Bedroom/8.png"
image bg VDomBedroom9 = "Scenes/Violet Dom Bedroom/9.png"
image bg VDomBedroom10 = "Scenes/Violet Dom Bedroom/10.png"
image bg VDomBedroom11 = "Scenes/Violet Dom Bedroom/11.png"
image bg VDomBedroom12 = "Scenes/Violet Dom Bedroom/12.png"
image bg VDomBedroom13 = "Scenes/Violet Dom Bedroom/13.png"
image bg VDomBedroom14 = "Scenes/Violet Dom Bedroom/14.png"
image bg VDomBedroom15 = "Scenes/Violet Dom Bedroom/15.png"

image bg VDomBedroom17 = "Scenes/Violet Dom Bedroom/17.png"
image bg VDomBedroom18 = "Scenes/Violet Dom Bedroom/18.png"
image bg VDomBedroom19 = "Scenes/Violet Dom Bedroom/19.png"
image bg VDomBedroom20 = "Scenes/Violet Dom Bedroom/20.png"
image bg VDomBedroom21 = "Scenes/Violet Dom Bedroom/21.png"
image bg VDomBedroom22 = "Scenes/Violet Dom Bedroom/22.png"
image bg VDomBedroom23 = "Scenes/Violet Dom Bedroom/23.png"


image bg VDDDS1 = "Scenes/Violet Dom Dinner Date/1.png"
image bg VDDDS2 = "Scenes/Violet Dom Dinner Date/2.png"
image bg VDDDS3 = "Scenes/Violet Dom Dinner Date/3.png"
image bg VDDDS4 = "Scenes/Violet Dom Dinner Date/4.png"
image bg VDDDS5 = "Scenes/Violet Dom Dinner Date/5.png"
image bg VDDDS6 = "Scenes/Violet Dom Dinner Date/6.png"
image bg VDDDS7 = "Scenes/Violet Dom Dinner Date/7.png"
image bg VDDDS8 = "Scenes/Violet Dom Dinner Date/8.png"
image bg VDDDS9 = "Scenes/Violet Dom Dinner Date/9.png"
image bg VDDDS10 = "Scenes/Violet Dom Dinner Date/10.png"
image bg VDDDS11 = "Scenes/Violet Dom Dinner Date/11.png"
image bg VDDDS12 = "Scenes/Violet Dom Dinner Date/12.png"
image bg VDDDS13 = "Scenes/Violet Dom Dinner Date/13.png"
image bg VDDDS14 = "Scenes/Violet Dom Dinner Date/14.png"
image bg VDDDS15 = "Scenes/Violet Dom Dinner Date/15.png"


image bg VDomAD1 = "Scenes/Violet Dom After Dinner/1.png"
image bg VDomAD2 = "Scenes/Violet Dom After Dinner/2.png"
image bg VDomAD3 = "Scenes/Violet Dom After Dinner/3.png"
image bg VDomAD4 = "Scenes/Violet Dom After Dinner/4.png"
image bg VDomAD5 = "Scenes/Violet Dom After Dinner/5.png"
image bg VDomAD6 = "Scenes/Violet Dom After Dinner/6.png"
image bg VDomAD7 = "Scenes/Violet Dom After Dinner/7.png"
image bg VDomAD8 = "Scenes/Violet Dom After Dinner/8.png"
image bg VDomAD9 = "Scenes/Violet Dom After Dinner/9.png"


image VBS = "Scenes/Phone Images/VioletBath.png"
image VSS = "Scenes/Phone Images/VioletSink.png"


image bg VBarDomScene1 = "Scenes/Bar Violet Dom/1.png"
image bg VBarDomScene2 = "Scenes/Bar Violet Dom/2.png"
image bg VBarDomScene3 = "Scenes/Bar Violet Dom/3.png"
image bg VBarDomScene4 = "Scenes/Bar Violet Dom/4.png"
image bg VBarDomScene5 = "Scenes/Bar Violet Dom/5.png"
image bg VBarDomScene6 = "Scenes/Bar Violet Dom/6.png"
image bg VBarDomScene7 = "Scenes/Bar Violet Dom/7.png"
image bg VBarDomScene8 = "Scenes/Bar Violet Dom/8.png"
image bg VBarDomScene9 = "Scenes/Bar Violet Dom/9.png"
image bg VBarDomScene10 = "Scenes/Bar Violet Dom/10.png"
image bg VBarDomScene11 = "Scenes/Bar Violet Dom/11.png"
image bg VBarDomScene12 = "Scenes/Bar Violet Dom/12.png"
image bg VBarDomScene13 = "Scenes/Bar Violet Dom/13.png"
image bg VBarDomScene14 = "Scenes/Bar Violet Dom/14.png"
image bg VBarDomScene15 = "Scenes/Bar Violet Dom/15.png"


image bg VBC1 = "Scenes/VioletBarCon/1.png"
image bg VBC2 = "Scenes/VioletBarCon/2.png"


image bg CarWash1 = "Scenes/Car Wash/1.png"
image bg CarWash2 = "Scenes/Car Wash/2.png"
image bg CarWash3 = "Scenes/Car Wash/3.png"


image bg NBar1 = "Scenes/Nate&Co Bar Scene/1.png"
image bg NBar2 = "Scenes/Nate&Co Bar Scene/2.png"
image bg NBar3 = "Scenes/Nate&Co Bar Scene/3.png"
image bg NBar4 = "Scenes/Nate&Co Bar Scene/4.png"
image bg NBar5 = "Scenes/Nate&Co Bar Scene/5.png"
image bg NBar6 = "Scenes/Nate&Co Bar Scene/6.png"
image bg NBar7 = "Scenes/Nate&Co Bar Scene/7.png"
image bg NBar8 = "Scenes/Nate&Co Bar Scene/8.png"
image bg NBar9 = "Scenes/Nate&Co Bar Scene/10.png"


image bg NPark1 = "Scenes/Nate&Co Park Scene/1.png"
image bg NPark2 = "Scenes/Nate&Co Park Scene/2.png"


image bg CheerPractice = "Scenes/Cheer Practice/1.png"
image bg ClaytonCheer1 = "Scenes/Cheer Coach Clayton/1.png"
image bg ClaytonCheer2 = "Scenes/Cheer Coach Clayton/2.png"
image bg ClaytonCheer3 = "Scenes/Cheer Coach Clayton/3.png"
image bg ClaytonCheer4 = "Scenes/Cheer Coach Clayton/4.png"
image bg ClaytonCheer5 = "Scenes/Cheer Coach Clayton/5.png"
image bg ClaytonCheer6 = "Scenes/Cheer Coach Clayton/6.png"


image bg TrackRun1 = "Scenes/Track Run/1.png"
image bg TrackRun2 = "Scenes/Track Run/2.png"


image bg DavisYear1 = "Scenes/Davis Photos Scene/1.png"
image bg DavisYear2 = "Scenes/Davis Photos Scene/2.png"
image bg DavisYear3 = "Scenes/Davis Photos Scene/3.png"
image bg DavisYear4 = "Scenes/Davis Photos Scene/4.png"


define persistent.feet = False
define persistent.yuri = False
define persistent.femdom = False
define persistent.spanking = False
define persistent.multiplepairings = False
define persistent.tentacles = False
define persistent.futa = False
define persistent.anal = False
define persistent.degradation = False
define persistent.exhibition = False
define persistent.submission = False
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
