label sdDate1:
    
    if datesDone["sd"] > 1:
        scene bgHallway
        with dissolve
        
        "Sourdough and I walk home together."
        jump night

    "[name]" "I'm gonna see if Sourdough wants to walk home together."
    td "Alrighty, smell ya later."
    
    hide td smile with moveoutbottom
        
    scene bgHallway
    with dissolve
        
    "I wait outside Sourdough’s classroom a few doors down as she’s putting away her things."
        
    show sd smile at right
    with dissolve
        
    sd "Hey [name], how’s school life treating you so far?"
        
    menu:
        "It’s been pretty good! I’m really lucky to have Touma Dachi in my class.":
            sd "Oh yeah, Touma. Great dude."
            sd "He’s actually the vice president of the archery club."
                
        "Great! I met some pretty interesting people already.":
            sd "Look at you go, tricking people into being your friend already."
            sd "You’ll have to tell me about them later."

                
        "Besides my hallucinations of sentient br***, school’s just school.":
            show sd neutral at right
            sd "That’s good to hear. School’s not that different no matter where you go I guess."
                
    "[name]" "So Sourdough, do you want to walk home together? Ya know, since we live so close anyways."
        
    show sd smile at right
    show sd smile at center with move
        
    sd "Sure! It’ll be just like the good ol’ days."
    sd "You, telling me conspiracy theories. Me, keeping you from getting lost walking to your own door."
        
    scene bgStreet with dissolve
        
    show sd smile with dissolve
        
    "[name]" "Hey, so I just got the new Go Kart Gold 8, if you wanted to come over and play a few rounds."
    "[name]" "But if you have homework or something…."
        
    "I trail off."
    
    show sd laugh
        
    sd "UHH HELL YEAH! I’ve been dying to play the new Go Kart Gold."
    sd "I heard the graphics got so much better and the driving mechanics are crazy."
        
    show sd smile
        
    "What was I worried about? Sourdough used to come over all the time for video games."
        
    "It’s been less frequent since we entered high school, but we have pretty similar tastes in games."
        
    show sd smile at right
    with move
        
    show sd laugh at right
        
    sd "I bet I’ll kick your ass in Star Lane!"

    "[name]" "You wish!"
    
    scene bgBedroom with fade
        
    show sd smile at left with dissolve
        
    sd "It's been forever since I came over. Glad to see not much has changed."
        
    "I kick some clothes out of the way as we head into my room. It’s kind of a mess, but it’s never bothered Sourdough."
         
    "She plops herself on my bed as I set up the console."
        
    "It’s just Sourdough, and it’s nothing out of the ordinary. But for some reason my heartbeat picks up a little."
        
    "We’ve known each other since forever, but it’s been so long. I forgot how nice it was hanging out with her."
    
    hide sd smile with dissolve
        
    "We play a few practice rounds, yelling profanities at each other."
        
    "Go Kart Gold is known to break friendships… but god is it worth it."
        
    "Sourdough crosses the finish line of Star Lane milliseconds before me."
        
    show sd laugh with dissolve
        
    sd "HOOO BOY I’M ON A ROLL, GET WRECKED LOSER!!"
        
    "[name]" "BULLSHIT YOU USED A MUSHROOM RIGHT AT THE FINISH LINE."
        
    show sd smile
        
    "She sticks her tongue out at me."
        
    "[name]" "Fine, rematch?"
        
    show sd sad
        
    sd "As much as I would love to toast you again— and I definitely would— I have to go home for dinner."
        
    scene bgStreet
    
    show sd smile with dissolve
        
    "I walk Sourdough to the door and wave as she heads down the street to her house."
        
    "[name]" "Seeya tomorrow at school."
        
    sd "Yeah, of course. We should do this again, It was a lot of fun."
        
    jump night