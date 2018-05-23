

play music "bgmusic.ogg"


# The game starts here.

label start:

    # background
    scene bgStreet


    # These display lines of dialogue.
    
    python:
        name = renpy.input("What is your name?")
        name = name.strip() or "Bread Fucker"
    
    "*Yaaaaawn*"
    
    "As I trudge my way down the street, I can feel the blinding morning sun mocking me."
    
    "It's my first day as a second year at my new high school. I just transferred, and it's the middle of the school year."
    
    "I'm a bit nervous, but at least I'll be with my childhood friend Sourdough."
    
    # Character
    
    show sd smile with moveinleft
    sd "Hey sleepyhead."

    "[name]" "Good morning, Sourdough."
    
    "It's an hour before school usually starts, but Sourdough has morning practice everyday for archery club."
    
    "I would never wake up at this ungodly hour for school, I don't know how she does it."

    "[name]" "Thanks for walking to school with me today."
    "[name]" "I don't want to get lost on the first day."

    show sd laugh
    sd "Don't worry about it [name]! Haha it's just like middle school again."
    
    sd "I know you're not a morning person, but at least you'll have time to explore the school before class starts."

    # At school
    scene bgHallway
    with dissolve

    show sd smile
    with dissolve

    sd "Well, I'm off to archery club. Try not to get lost!"
    
    hide sd smile
    with dissolve

    "Looks like I have a lot time to kill before the bell rings."
    
    # Variables
    $ classDone = False
    $ hallDone = False
    $ libDone = False
    $ cafDone = False
    $ roofDone = False
    
    jump exploreChoice

label exploreChoice:
    
    menu:

        "Go find my classroom." if classDone == False:
            $ classDone = True
            jump meetBaguette

        "Wander the halls" if hallDone == False:
            $ hallDone = True
            jump meetLoaf

        "Head to the library" if libDone == False:
            $ libDone = True
            jump meetBagel

        "See what's cooking in the cafeteria" if cafDone == False:
            $ cafDone = True
            jump meetMelonpan

        "Check out the rooftop" if roofDone == False:
            $ roofDone = True
            jump meetPizza

        "Wait for the bell to ring":
            jump firstDay
        
        
label meetBaguette:
    
    scene bgClassroom
    with dissolve
    
    "I meet Baguette."
    jump exploreChoice
    

label meetLoaf:
    
    scene bgHallway
    with dissolve
    
    "I meet Loaf Bread."
    jump exploreChoice
    

label meetBagel:
    
    scene bgLib
    with dissolve
    
    "I meet Bagel."
    jump exploreChoice


label meetMelonpan:
    
    scene bgCaf
    with dissolve
    
    show mp smile
    with dissolve
    
    "I meet Melon Pan."
    jump exploreChoice


label meetPizza:
    
    scene bgRoof
    with dissolve
    
    "I meet Pizza."
    jump exploreChoice


label firstDay:
    
    scene bgClassroom
    with dissolve
    
    "I explore a bit and walk back to my classroom as the first class is about to start."
    
    "I do double-take in the doorway."
    
    "There's no way I could mistake that mop of spiky brown hair, broad shoulders, and distinctive laugh."
    
    "Is that... my middle school friend Touma Dachi?"
    
    "He's chatting with a group of friends and spots me as I walk in."
    
    show td smile with dissolve
    
    td "[name]!"
    
    "[name]" "Touma! It's been so long. How've you been man?"
    
    td "Better now that you're here."
    td "I knew we were getting a transfer student today, but I never thought it'd be you!"
    
    "[name]" "It's nice having a familiar face in my class."
    
    "[name]" "I was kinda worried transferring in the middle of the year, especially since Sourdough is in a different class."
    
    show td wink
    td "Don't worry [name], I got your back."
    
    hide td wink with dissolve
    
    "Our teacher comes in to start class. He’s a pudgy middle-aged man with glasses who looks bored out of his mind." 
    
    "I’m asked to introduce myself in front of the class."
    
    "As I’m standing in front of the class, I see the girl from earlier, Baguette was it? She’s staring out the window like an anime protagonist."

    "I spend my lunch break with Touma in the classroom. We catch up with everything that’s happened these past two years."
    
    "It’s nice that even though we have such different interests, we can still get along so well."
    "Touma’s super involved, he’s in the student council, archery, and drama club. I would basically call him a Renaissance man. "

    "Class is what I expect it to be. Even after transferring schools, not much is different in terms of material covered."
    
    "Teachers are boring, and classes are pretty standard."
    
    "After a long day, I gather my things and start to head for the door when I lock eyes with a familiar face."
    
    show td smile with dissolve
    
    td "Hey [name]! Heading home for the day? Lets walk together, I mean, if you haven’t already made better friends than me."
    
    show td laugh
    "He laughs awkwardly."
    
    show td smile
    "[name]" "Come on, it’s only been one day. Though I did meet some.. kinda interesting students."
    
    scene bgStreet with dissolve
    
    show td smile with dissolve
    
    "We start walking out and the sun's setting in the distance. At one street corner, I start to smell something really delicious."

    td "That ramen shop is amazing. Best place in this town, you have to try it sometime."
    
    menu:

        "Why don’t we go right now? I’m starving.":
            jump ramenDate
    
        "I’ll put it on my list. I’ll definitely check it out later.":
            "I spend some time with Touma. We chatted and traded numbers."
            jump secondDay


label ramenDate:
    
    td "Great idea, me too."
    
    scene bgRamen
    with dissolve
    
    show td smile at left
    with dissolve
    
    td "So at the latest student council meeting, the president - "

    "[name]" "Oh Wheat, right? I actually met her this morning."

    td "Already? Wow, Wheat really is friends with everybody."
    td "You did say you met some ‘interesting students’, who else did you meet?"

    "[name]" "Let's see, you know Sourdough of course, but I also talked to a really imaginative first-year who thought she was a superhero or something, a kinda intimidating girl smoking on the roof, a really quiet girl in the library, and the French girl in our class."

    "Touma looks down at his ramen bowl."

    td "All girls, huh?  Did any of them… catch your rye?"
    
    show td wink

    "He playfully nudges your shoulder and you can feel the heat rising in your cheeks."

    menu:
        "Some of them were pretty cute...":
            $ coolbeans = 0
        
        "Haha, who knows?":
            $ coolbeans = 0
            
        "Nah, it’s too early to say.":
            $ coolbeans = 0
     
    show td smile 
    td "Well if you need any advice, I’m your guy. I’ll help you anyway that I can!" 
    
    td "And keep me updated, okay? Live out the high school romance that all of us wish we had."
    
    "You pay for your ramen and trade numbers with Touma."
    
    jump secondDay
