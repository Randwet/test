label aliceatschool:
    $ AliceClothes = 0
    show chelsea blank at right
    "Another day of school wading through the crowds of students as they all move to their next classes."
    show chelsea confused
    "In the corner of your eye you spot someone familiar walk by you. You're sure you've seen her somewhere before."
    "Out of curiousity you turn your head towards her."
    show chelsea shocked
    show Alice Blank with dissolve
    "It's Alice!"
    "You had no idea that she went to this school. How had you not managed to see her before? Did she recently transfer here?"
    show chelsea confused
    pcname "Alice?"
    show Alice Confused
    A "Huh?"
    "She looks at you as though you just interrupted a deep train of thought."
    show Alice Neutral
    A "Oh! [pcname]?"
    show chelsea happy
    pcname "Yeah, you never told me that you went to East Uni. How hadn't we seen each other before."
    show Alice Thinking
    A "We probably just have different classes I guess?"
    show Alice Blank
    show chelsea blank
    pcname "I suppose so."
    show Alice Happy
    A "Hey are you doing anything after school?"
    show Alice Blank
    show chelsea happy
    if job == "bakery":
        pcname "I work at a Bakery."
        show Alice Happy
        A "That sounds really nice."
        show Alice Blank
        pcname "It can be stressful sometimes."
    elif job == "cafe":
        pcname "Actually I work at a maid cafe after school."
        show Alice Thinking
        A "A Maid Cafe?"
        show Alice Confused
        A "Emilia's Maid Cafe?"
        show Alice Blank
        pcname "Yep! That's the one. Have you been there before?"
        show Alice Neutral
        A "No, but I see when I'm walking to the arcade sometimes."
    elif job == "bar":
        pcname "I work at a bar close to downtown after school."
        show Alice Confused
        A "A bar? That's suprising."
        show Alice Blank
        show chelsea confused
        pcname "Why is that?"
        show Alice Neutral
        show chelsea blank
        A "Doesn't seem like the kind of place you'd work at."
    show Alice Happy
    A "Anyway, why don't you come to the arcade with Samantha and I?"
    show chelsea confused
    pcname "Who is Samantha?"
    show chelsea blank
    show Alice Laughing
    A "Oh she's my best friend, we hang out at the arcade a lot."
    show Alice Happy
    A "I'll introduce you two when we meet up."
    show Alice Blank
    show chelsea happy
    pcname "Okay! I might be a bit late though getting there."
    show Alice Neutral
    A "That's okay. We usually stay there pretty late anyway."
    show Alice Blank
    pcname "I'll see you there then."
    show Alice Happy
    A "Awesome!"
    "With that she waves goodbye to you and heads off to class."
jump events_end_period
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
