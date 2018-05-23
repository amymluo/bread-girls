screen phone:
    add "gui/phonescreen/phonescreen.png"
    
    $ currY = 148
    
    if datesDone["sd"] > 0:
        imagebutton:
            auto "gui/phonescreen/sd_%s.png" 
            xpos 492 ypos currY focus_mask True 
            action Jump("sdChat")
            
        $ currY += 67
        
    imagebutton:
        auto "gui/phonescreen/td_%s.png"
        xpos 492 ypos currY focus_mask True
        action Jump("tdChat")
        
##########################################################################
    
label tdChat:
    
    scene bgPhone
    
    show tdName:
        xalign 0.5
        yalign 0.165
    
    if randMeme == 1:
        show meme1:
            xalign 0.45
            yalign 0.29
            
    elif randMeme == 2:
        show meme2:
            xalign 0.45
            yalign 0.29 
    else:
        show meme3:
            xalign 0.45
            yalign 0.29
    
    menu:
        "Chat with Touma and go to sleep":
            window hide
            $ renpy.pause(0.5)
            play sound "textSent.ogg"
            $ renpy.pause(0.8)
            show mcTdResp:
                xalign 0.57
                yalign 0.5
            $ renpy.pause()
            jump lunchBreak
            
        "Go back":
            call screen phone
            

label sdChat:
    
    scene bgPhone
    
    show sdName:
        xalign 0.5
        yalign 0.165
        
    if datesDone["sd"] == 1:
        # set up weekend date
        menu:
            "Set up weekend date":
                $ datesDone["sd"] = max(2, datesDone["sd"])
                jump sdDate2
                
            "Go back":
                call screen phone
        
    else:
        # ask to school festival
        menu:
            "Ask to go to the school festival together":
                $ datesDone["sd"] = max(3, datesDone["sd"])
                jump sdDate3
                
            "Go back":
                call screen phone
        
        
        
        