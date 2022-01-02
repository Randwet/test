label cheer4:
    scene bg Gym
    "You're really feeling the adrenaline pump through your veins as you arrive to practice today."
    "It feels like there's an electric energy in the room and everyone in the squad is on the same page."
    "As you practice cheers and perform halftime dances, you feel confident and light on your feet, easily moving into the next step without missing a beat."
    "You go through the motions a few times, rehearsing from start to finish over the course of a couple of hours."
    "By the time the music stops, you're feeling refreshed and pumped for the day ahead."
    show MV Smile with dissolve
    "Vicky claps her hands at the end of your routine and nods in approval."
    show MV Laugh
    "Vicky" "Good job, girls! Nice energy today."
    show MV Smile
    show Tracy Smile at midright with dissolve
    "Tracy beams, no doubt accrediting your success to her good leadership."
    show Tracy Laugh
    "Tracy" "You heard her, girls. Keep practicing like that and we'll be ready before you know it!"
    show Tracy Smile
    "Tracy waves one pom-pom'ed hand toward the locker rooms as means of dismissal."
    show Tracy Blank
    "Tracy" "Let's hit the showers!"
    scene bg Lockeroom with fade
    "You follow the other girls into the locker rooms, heading straight for one of the unoccupied shower stalls."
    $ clothes = "naked"
    show chelsea embarrassed with dissolve
    "The warm water feels nice and relaxing against your muscles, grounding you down from the excessive energy you felt earlier."
    scene bg Lockeroom with fade
    "By the time you're dried off and changed into your usual clothes, most of your teammates have already left."
    "You lag behind, packing up your cheerleading uniform, when you see Tracy approach you from between the lockers."
    show Tracy Blank with dissolve
    "Tracy" "Great job today, [pcname]! You almost have that routine nailed down."
    $ clothes, hair = casualwear
    show chelsea happy at left with dissolve
    show Tracy Smile
    pcname "Aw, thanks! I was really feeling it today."
    show Tracy Laugh
    show chelsea embarrassed
    "Tracy" "I could tell. You were giving it your all! That's what I like to see."
    show Tracy Blank
    show chelsea happy
    "Tracy" "You've been making a lot of progress since joining us."
    show Tracy Laugh
    show chelsea blank
    "Tracy" "I was totally worried at first that the new girls would hold us back, but you've really proved me wrong!"
    show Tracy Smile
    menu cheerprogress:
        "I'm so glad you said that!" if True:
            show chelsea happy
            "You beam at her, enthused by her positive attitude."
            show chelsea laugh
            pcname "Seriously? Thanks, Tracy! I'm so glad you said that."
            show chelsea embarrassed
            pcname "I've been practicing super hard, so it's nice to see my hard work noticed."
        "I'm happy to be making progress." if True:
            show chelsea embarrassed
            "You smile uncertainly, not sure whether to take that as an insult or a compliment."
            show Tracy Question
            pcname "Thanks, Tracy."
            show Tracy Smile
            pcname "I'm just happy I'm making progress."
    show Tracy Laugh
    "Tracy" "Totally! It can be super intimidating when you're new, but you have nothing to worry about, [pcname]!"
    show chelsea confused
    show Tracy Smile
    "Tracy smiles at you and takes a seat on the bench, motioning for you to do the same. Odd; usually your conversations end there."
    "You plop down beside her, intrigued."
    show chelsea blank
    show Tracy Question
    "Tracy" "I feel like I haven't really gotten to know you much outside of cheer. What kind of stuff do you do?"
    show Tracy Smile
    menu cheerinterests:
        "I have a job." if True:
            pcname "Well, most of my time outside of school is taken up by my job."
            show Tracy Question
            "Tracy" "A job?"
            "Tracy's lips part in surprise, as though the idea of a high schooler working outside of school is something new to her."
            show chelsea embarrassed
            show Tracy Smile
            "Maybe cheerleaders don't usually work outside of school and club..."
            show Tracy Laugh
            "Tracy composes herself, a new interest taking hold of her as she leans in closer to you."
            show chelsea blank
            show Tracy Question
            "Tracy" "Where do you work?"
            if job == "bakery":
                show chelsea laugh
                show Tracy Smile
                pcname "I work at a bakery in town. The one by the hair salon."
                show chelsea happy
                show Tracy Blank
                "Tracy" "Ohh! I've been there before!"
                show chelsea embarrassed
                "Tracy" "My mom loves your fresh bread. She's always getting a loaf to bring home for dinner."
                show Tracy Smile
                "You smile, a little proud of your work there. Even if you had very little to do with it."
                show chelsea blank
                show Tracy Question
                "Tracy" "Do a lot of cute guys come in to buy anything? Or maybe you have some hot coworkers?"
                show chelsea embarrassed
            elif job == "cafe":
                show chelsea laugh
                show Tracy Smile
                pcname "I work at a maid cafe in town."
                show chelsea embarrassed
                show Tracy Blank
                "Tracy" "A maid cafe... Oh! I think I know the one!"
                show Tracy Question
                "Tracy" "It's down the street from a pet salon, right?"
                show chelsea happy
                show Tracy Smile
                pcname "Yeah, that's the one."
                show chelsea embarrassed
                show Tracy Laugh
                "Tracy" "How cute! I bet you have a {i}ton{/i} of cute guys come in to see you all dressed up, huh?"
                show Tracy Smile
                "You feel heat rise up your neck as you recall all of the men that wanted a little {i}extra{/i} with their order, but you don't feel a need to tell Tracy about that."
                show Tracy Question
            elif job == "bar":
                show chelsea laugh
                show Tracy Question
                pcname "I work at a bar downtown."
                show chelsea blank
                "Tracy" "A bar?"
                show Tracy Smile
                "The shock is clear on her face. She catches herself, considering."
                show Tracy Tired
                "Tracy" "Well, you are eighteen. I guess it's not that unusual..."
                show chelsea embarrassed
                show Tracy Question
                "Tracy" "Is it a new bar? Do you get any cute guys you get to serve?"
                "Your face heats up as you recall just how you ended up with that job in the first place, but Tracy doesn't need to know about that."
            pcname "I don't know about that."
            "Tracy" "What about outside of work then? Anyone cute catch your eye?"
        "I have a cat." if catadopt:
            pcname "Well, I have a cat."
            show chelsea embarrassed
            show Tracy Blank
            "Tracy" "Oh my god, a cat? How cute!"
            show Tracy Laugh
            "Tracy" "I want to get one so badly, but my dad's allergic."
            show Tracy Question
            "Tracy" "What's his name?"
            show chelsea laugh
            show Tracy Smile
            pcname "[kittenname]."
            show Tracy Laugh
            "Tracy" "Aww, that's adorable! You're so lucky. [pcname]."
            show chelsea embarrassed
            show Tracy Question
            "Tracy" "But your cat can't be the only man in your life, right? How about any cute boys?"
        "I don't do much." if True:
            show chelsea shocked
            "You try to think of some hobby or activity you do regularly, but nothing really comes to mind."
            show chelsea blank
            show Tracy Question
            pcname "I like to go exploring around town sometimes... Other nights I stay at home..."
            show chelsea embarrassed
            pcname "I guess you could say I'm a homebody? I don't do much."
            show Tracy Tired
            show chelsea blank
            "Disappointment flickers over Tracy's face; clearly she was hoping for something a little more exciting."
            "Yet, it seems she won't be deterred."
            show chelsea embarrassed
            show Tracy Question
            "Tracy" "Well, what about cute guys? There has to be someone you're crushing on, right?"
    show Tracy Laugh
    "Tracy winks at you, waiting eagerly for your response."
    show Tracy Smile
    if mattsubmissive:
        show chelsea sad
        "You think of Matt and all of the dirty things you've done together."
        show chelsea embarrassed
        "He's not a boyfriend by any means-- at least, you don't think so-- but you would be lying if you said you didn't find him attractive."
        show Tracy Question
        pcname "There's... someone like that."
        "Tracy" "Oh yeah? What's he like?"
        show Tracy Blank
        show chelsea sad
        "Tracy" "I bet he's really strong and athletic, right?"
        pcname "Er..."
        show chelsea blank
        show Tracy Smile
        "You don't actually know much about Matt's hobbies, but you definitely don't see him as the kind of guy to go playing sports on the weekends. Unless that sport is sex..."
    elif damienrelate == "dating":
        show chelsea happy
        "You smile a little as you think of Damien. He's not {i}conventionally{/i} attractive by any means, but you certainly think he's cute."
        show chelsea embarrassed
        show Tracy Blank
        pcname "I have a pretty cute boyfriend, if that's what you mean."
        show Tracy Question
        "Tracy" "Ooh! A boyfriend? What's he like?"
        show Tracy Laugh
        show chelsea happy
        "Tracy" "I bet he's strong and athletic, right?"
        show chelsea laugh
        show Tracy Smile
        "You have to hold yourself back from laughing. Damien may have some muscle, but he's a far cry from athletic."
        show chelsea embarrassed
    elif violetrelate == "Sub" or violetrelate == "Dom":
        show chelsea embarrassed
        "You don't think Violet qualifies as a 'cute guy', but there's no denying your attraction to her."
        pcname "Not a guy really, but..."
    elif katerelate == "girlfriend":
        show chelsea embarrassed
        "Your heart warms a little at the thought of Kate and all of her adorable habits. She may not be a guy, but she's the cutest thing you've ever seen."
        show Tracy Question
        pcname "Not really a guy, but I have a cute girlfriend."
        show chelsea blank
        show Tracy Smile
        "Tracy" "A girlfriend, huh? Hm."
        show Tracy Tired
        "Tracy seems conflicted in her reaction, as though there's some internal debate going on in her mind before she responds."
        show chelsea confused
        show Tracy Blank
        "Tracy" "Some guys find that really hot, you know? Two girls dating."
        show chelsea blank
    elif True:
        "You try to think of someone, but no one comes to mind. At least, no one that you can really picture yourself having a relationship with."
        show chelsea embarrassed
        "You shake your head and shrug."
        show Tracy Question
        pcname "Not really. I guess I haven't really thought about it."
        show chelsea blank
        show Tracy Tired
        "Tracy frowns, obviously disappointed with this news."
        show chelsea confused
        show Tracy Smile
        "But she picks herself up quickly, and it's almost as if you hadn't spoken at all."
        show chelsea blank
    show Tracy Laugh
    "Tracy" "For me, I really like jocks. A guy that plays sports and is just {i}super{/i} ripped is really hot, don't you think?"
    show Tracy Tired
    show chelsea embarrassed
    "Tracy" "They can just lift you up, or throw you {i}down{/i}."
    show chelsea laugh
    show Tracy Laugh
    "She leans in and giggles, like she's sharing some kind of secret between the two of you."
    show chelsea embarrassed
    show Tracy Question
    "Tracy" "Have you seen them right after a game? When they start to take their shirts off..."
    show Tracy Tired
    "She fans herself, swooning at the mental image."
    "Tracy" "Now {i}that{/i} is hot."
    show chelsea shocked
    show Tracy Question
    show MV Blank at right with dissolve
    "Before you can respond, Vicky's head pops around the corner, her eyebrow raised at the two of you."
    show chelsea blank
    "Vicky" "Come on girls, wrap it up. I have a meeting to get to and I need to lock down the gym."
    hide MV Blank with dissolve
    show Tracy Blank
    "Tracy" "Oh, right! Coming!"
    show Tracy Laugh
    show chelsea embarrassed
    pause 1.0
    hide Tracy with dissolve
    "Tracy shares another secretive smile with you and winks before leaving the locker room."
    scene black with fade
    "Vicky watches you scramble to get your things and exit before locking up the room."
    jump events_end_period

label cheer5:
    scene bg Lockeroom
    "You arrive to practice earlier than usual and head straight for the locker room for some private time."
    $ clothes = "cheer"
    show chelsea at right with dissolve
    "After changing into your cheer uniform, you relax against one of the benches and flip through a discarded magazine, eyeing up makeup and dresses that are four times out of your pay grade."
    show chelsea happy
    "A few of your squad members start filing in to change as well, greeting you briefly before mingling amongst themselves."
    show chelsea blank
    show Olivia Sad
    "As you reach the end of your magazine, Olivia sits on the other side and peers down at the glossy paper, frowning at the skinny model on the page."
    "Olivia" "She's so pretty..."
    show chelsea sad
    pcname "Yeah. Her shoes cost more than my rent, though."
    show chelsea blank
    "You flip the magazine closed and disregard it somewhere else on the bench for the next girl to find."
    show chelsea confused
    show Olivia Tired
    "Olivia shifts at your side, biting down hard on her lip. She clearly has something to say but is reluctant to voice her opinion."
    show chelsea embarrassed
    show Olivia Sad
    "You relax beside her and wait, hoping she'll find the courage to start the conversation herself."
    show Olivia Embarrassed
    "After a few moments of awkward silence, Olivia looks around the emptying room, trying to keep her voice light and casual."
    show chelsea blank
    show Olivia Blank
    "Olivia" "How are you liking being on the cheer squad, [pcname]?"
    show Olivia Happy
    menu cheerenjoyment:
        "I really like it." if True:
            $ Oliviacorruption +=1
            show chelsea embarrassed
            "You weren't sure what to expect from being on a cheerleading squad at first, but this has been better than you imagined."
            show chelsea laugh
            show Olivia Confused
            "Not only do you feel more confident, but with the way practices have been going, you feel way more flexible and healthy."
            show chelsea happy
            show Olivia Embarrassed
            pcname "It's great!"
            show chelsea embarrassed
            pcname "I'm really glad I signed up. Everyone here really works together and makes it a fun place to be."
            show Olivia Sad
            "Olivia's lips briefly slip into a frown. She plays with the end of her ponytail, uncertain."
            show chelsea blank
            show Olivia Confused
            "Olivia" "O-Oh... Is that so..."
            show chelsea embarrassed
            show Olivia Blank
            pcname "Plus it gave me a chance to meet cool girls like you."
            show chelsea laugh
            show Olivia Embarrassed
            "You wink at her, hoping to boost her confidence. Olivia smiles a little, flattered."
            show chelsea embarrassed
            show Olivia Laughing
            "Olivia" "I'm glad to have met you too, [pcname]."
            show chelsea sad
            show Olivia Confused
            "Olivia" "It's just... I don't know. It feels different for me. In a bad way."
            show Olivia Blank
            "Olivia" "I've been wondering if I should just quit..."
        "It's okay, but..." if True:
            show Olivia Confused
            "You shrug, not particularly attached to the group as a whole."
            show chelsea sad
            "While your experience on the squad has been fun, it's not like the whole thing has been a walk in the park."
            show chelsea blank
            show Olivia Sad
            pcname "It's okay, I guess."
            show chelsea sad
            show Olivia Blank
            pcname "I don't really like how some things are handled, but there's nothing I can really do about that."
            show chelsea blank
            show Olivia Happy
            "Olivia looks relieved to hear you say that, her shoulders visibly relaxing."
            show chelsea shocked
            show Olivia Confused
            "Olivia" "That's exactly how I feel! Honestly, I've been debating if I should just quit..."
    show chelsea confused
    show Olivia Sad
    pcname "Quit? How come?"
    show chelsea sad
    pcname "That seems pretty drastic, don't you think?"
    show Olivia Confused
    "Olivia" "I don't know... The things Vicky keeps pushing for just don't sit right with me."
    show chelsea blank
    show Olivia Blank
    "Olivia" "She's always commenting on my weight, or telling me that I don't look as cute as the rest of the squad."
    "Olivia" "Who wants to stick around and hear negative stuff like that the whole time?"
    show Olivia Sad
    menu vickypushing:
        "Vicky has been pretty cruel to you." if True:
            show chelsea sad
            "Your heart goes out to her; the things Vicky has said to Olivia and a couple of the other girls has been borderline cruel, even if that isn't her intention."
            show chelsea angry
            show Olivia Happy
            pcname "I get where you're coming from. Vicky can be really harsh on you and some of the other girls."
            show Olivia Embarrassed
            pcname "I don't like how she talks to you."
            show chelsea blank
            show Olivia Confused
            "Olivia" "Exactly! I don't either. It really hurts, you know? Now I'm constantly watching my food intake and it's made eating miserable..."
            show chelsea sad
            show Olivia Sad
            pcname "That's terrible. You shouldn't feel bad for eating, Olivia. Everyone needs to."
            show chelsea blank
            show Olivia Confused
            "Olivia" "I know, but I can't help it..."
        "I think she just wants what's best for the team." if True:
            $ Oliviacorruption +=1
            show chelsea sad
            show Olivia Confused
            pcname "I don't think she's trying to single you out personally; she has problems with all of us."
            show chelsea embarrassed
            pcname "I think she just really wants what's best for the team."
            show chelsea blank
            show Olivia Blank
            "Olivia" "But what does my weight have to do with what's best for the team?"
            show Olivia Sad
            pcname "I don't always agree with what Vicky says, but I think I get what she's trying to go for."
            show chelsea happy
            pcname "We all have our own stuff to improve on and we should be working on them together as a team."
            show chelsea sad
            "At least, that's what you've gathered from her talks. Olivia, on the other hand, seems doubtful."
            show Olivia Confused
            "Olivia" "I guess so..."
            show chelsea blank
    show Olivia Sad
    "Olivia sighs, leaning back on her elbows."
    show chelsea sad
    show Olivia Confused
    "Olivia" "It's not just that, though. This new routine is killing me. I just can't get it down."
    show Olivia Tired
    "Olivia" "And if I try to talk about it to Vicky, she's just going to say my boobs are too big and get in the way. That's not helpful."
    show chelsea angry
    show Olivia Sad
    pcname "No... No, that isn't really helpful at all."
    show chelsea sad
    show Olivia Confused
    "Olivia" "I don't know what to do. I don't want to let the team down, but I don't know why I'm struggling so hard in the first place."
    show Olivia Confused at center, moveSprite(0.8, 0.8, 0.0) with move
    show Tracy Laugh with dissolve
    show chelsea shocked
    show Olivia Blank
    "Tracy" "If you're really serious about it, Olivia, I'm happy to help you!"
    show Tracy Smile
    "You both jump as Tracy appears between you, a cheery smile planted on her face. How long has she been listening to you talk?"
    show chelsea sad
    "You secretly hope she didn't hear the things said about Vicky. The last thing Olivia needs is more discouragement..."
    show chelsea blank
    "But Olivia's eyes widen in surprise with Tracy's arrival, a sort of cautious hope hanging on her expression."
    show Olivia Confused
    show Tracy Question
    "Olivia" "You will? You don't have to do that, I mean... You're probably busy..."
    show Tracy Laugh
    show Olivia Happy
    "Tracy" "Nonsense! I want my team to be the best there is, so if someone is struggling, I'm happy to help!"
    show Tracy Question
    show Olivia Embarrassed
    "Tracy" "You do want to do your best, don't you, Olivia?"
    show Olivia Embarrassed
    show Tracy Laugh
    "Your friend nods, a light blush spreading over her cheeks. Tracy grins."
    show Tracy Blank
    "Tracy" "Great! We'll set up a time to get together and practice alone."
    show Olivia Blank
    show Tracy Laugh
    "Olivia" "Ah, thanks, Tracy..."
    show chelsea shocked
    show Olivia Confused
    show Tracy Question
    "Vicky enters the locker room then, her claps giving away her presence before she appears before you."
    show MV Blank at left with dissolve
    "Vicky" "Enough chit-chat, girls! Time to head out and start practice!"
    scene black with fade
    "You all get up at once and file out into the gym, Olivia seeming a little more confident than she had this morning."
    jump events_end_period
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
