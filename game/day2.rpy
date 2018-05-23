label secondDay:
    
    scene bgStreet
    with fade
    
    "It's the second day of my new high school."
    
    "Sourdough has morning archery practice everyday, and since I know my way around I didn't wake up early with her."
    
    "Even with waking up an hour later, all I want to do is crawl back into my warm, soft bed."
    
    "I trudge to school and see Touma as I walk in."
    
    scene bgHallway
    with dissolve 
    show td smile
    with moveinbottom
    
    "[name]" "Good morning Touma!"
        
    td "Hey [name]. It was great getting ramen together yesterday. Let me know how it goes with those girls."
    
    
##################################################################################################

label lunchBreak:
    
    scene bgClassroom
    with fade
    
    if secondDay:
        "It's finally my lunch break."
        "I think about the different girls I met yesterday. This could be an opportunity to get to know one of them better."
        
        show td smile
        with dissolve   

        td "Hey [name], where are you spending your lunch break today?"
        td "If you go where you met one of the girls yesterday, you might be able to find her there again!"
    
    else:
        "Morning classes pass and it's time for my lunch break."
         
        show td smile
        with dissolve
        
        $ randMsg = renpy.random.choice(["Yo, where are you spending your lunch break today?", "Hey, what are your plans for lunch?", 
            "Off to see anyone on your lunch break?", "Where are you going today for lunch?"])
        
        td "[randMsg]"
    
    menu:
        
        "Eat in the classroom":
            hide tdSmile
            jump btDate1
        
        "Go to the cafeteria":
            hide tdSmile
            jump mpDate1
        
        "Dare the rooftop":
            hide tdSmile
            jump pDate1
        
        "Eat alone":
            hide tdSmile
            $ eatAloneCount += 1
            jump eatAlone

#############################################################################################

label afterschool:
    
    scene bgClassroom
    with fade
    
    if secondDay:
        "The final bell rings and everyone starts to pack up for the day." 
        
        "This might be a good chance to spend some time with a girl I met yesterday."
    
        show td smile
        with dissolve
    
        td "Hey [name], what are you up to after school today? Off to find one of those girls again to hang out with?"
    
        show td wink
        "He winks."
        
        show td smile
        
    else:
        
        "Class is finally over for the day."
        
        show td smile
        with dissolve
 
        $ randMsg = renpy.random.choice(["Hey, what are you up to after class today?", "Spending your time after school with anyone special?", 
            "Any plans after school today?", "Yo man, what's your plan after class?"])
        
        td "[randMsg]" 
    
    $ secondDay = False
        
    menu:
        
        "Help out the student council":
            jump wbDate1
        
        "Study in the library":
            jump bDate1
        
        "Walk home with Sourdough":
            $ datesDone["sd"] = max(1, datesDone["sd"])
            jump sdDate1
        
        "Go home alone":
            $ walkAloneCount += 1
            jump walkAlone
            
#################################################################################

label night:
    
    scene bgBedroom
    with fade
    
    $ randMsg = renpy.random.choice(["I get ready for bed and check my phone before going to sleep.", "Ready to unwind for the night, I check my phone before going to bed.", 
        "After finishing up for the night, I check my phone messaging app.", "It's evening now, and I check my phone before going to sleep."])
    
    "[randMsg]"
    
    #for Touma
    $ randMeme = renpy.random.randint(1,3)
    
    call screen phone
            
            

    
    
    
    
    

     
     # This ends the game.

    return