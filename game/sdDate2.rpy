label sdDate2:
    
    scene bgStreet
    with fade
    
    "It's Saturday morning and I walk to Sourdough's house to meet her for our picnic today."
    
    show sd date neutral
    with dissolve
    
    "I'm surprised to see her dressed so cute. She’s wearing a sundress and has on a bunch of girly accessories I haven’t seen her wear."
    
    show sd date smile
    
    "When she sees me, she smiles and I can feel my heart skip a beat."
    
    "I guess I’m used to seeing her when we hang out at her house in our pajamas, or at school in uniform. The yellow color suits her."
    
    menu:
        "Good morning! You look nice.":
            show sd date laugh
            "She blushes a little."
            sd "Let’s go loser."
        "Let's go":
            show sd date smile
            sd "Dude I'm so excited."
    
    scene bgPark with fade
    
    show sd date smile at left
    with dissolve
    
    "At the park, we walk around together for a few minutes before stopping by the edge of the pond."
    
    sd "There are so many ducks here. And they’re not like the ducks in Battleground Age: Pacific™ that fly away when you go near them."
    
    show sd date neutral at left
    show sd date neutral at center with move
    
    sd "These ducks fear neither man nor God."
    
    "She walks closer to the ducks and they completely ignore her."
    
    menu:
        "Let's feed them some br***":
            show sd date sad
            sd "You want to watch br*** get ripped apart and have their soft flesh devoured by ducks?"
            sd "That’s…. that’s kind of fucked up [name]."
            
            menu: 
                "Oh, sorry! I guess I was being insensitive.":
                    show sd date neutral
                    sd "It’s alright. We can give them some of our popcorn."
                    
                "Right sorry. It’s not really healthy for them to be eating all those carbs anyways.":
                    show sd date sad:
                        zoom 1.15
                        yalign 0.25
                    sd "Are you implying something about br***? Are you saying br*** makes you fat?"
                    "[name]" "I just -"
                    show sd date sad:
                        zoom 1.35
                        yalign 0.15
                    sd "Is **** too unhealthy? Not good enough for you?"
                    "[name]" "No! No, it’s just the ducks — I didn’t mean th-"
                    show sd date neutral:
                        zoom 1.0
                        yalign 1.0
                    sd "Hm. Whatever. It’s fine."
                    sd "Let’s give them some of our popcorn."
                    
        "They look hungry":
            show sd date smile
            sd "Let’s feed them some of our popcorn!"

        "*Quack quack*":
            show sd date laugh
            sd "Haha weirdo. Let’s feed them some of our popcorn!"
    
    "[name]" "Do you think we’ll have enough to share?"
    
    show sd date smile
    sd "Don’t worry, we have plenty of food."
    
    show sd date neutral
    sd "Plus, look into their deep, dark duck eyes — they’re practically begging for popcorn....They’re soulless...unforgiving...br*** eating duck eyes..."
    
    show sd date laugh
    sd "Let’s feed them!"
    
    show sd date laugh at right
    with move
    sd "Look, that duck looks like my sister!"
    
    "[name]" "You...don't have a sister."
    
    show sd date smile at right
    sd "Got me there."
    
    "For a moment we laugh together about the ducks, while throw popcorn one after the other."
    "The birds hungrily devour the bits of puffy corn we offer them."
    
    show sd date neutral at right
    sd "Oh. I think we went through the entire bag"
    
    "[name]" "Already?"
    
    sd "Eh, at least we have other stuff to eat."
    
    "I look into the picnic basket Sourdough packed for us to see what we have left. There’s deli meat, cheese, lettuce, and some fruit." 
    
    show sd date smile at right
    "These are all the ingredients to make a sandwich except for the... Well i guess that’s not important."
    
    sd "I was thinking we can have like one of those fancy party platters with sliced fruit, meat, and cheese."
    
    menu:
        "Swagolo let's go":
            show sd date sad at right
            sd "Swagolo? Is this how dead God is?"
            "I shrug."
            
        "Like a charcuterie?":
            sd "Sure Mr. Fancypants, whatever the fuck that is."
            
    show sd date smile at right
    show sd date smile at center with move
    
    sd "We can eat at my favorite spot in the park. We're lucky it's such a nice day out."
    
    "She grabs my wrist and leads me down the sidewalk."
    
    hide sd date smile with dissolve
    "A few trees are blocking the way of a turn, and I almost crash into a biker."
    
    scene bgPark with hpunch
    
    "???" "Whoa, sorry about th- Hey [name], it’s you! Crazy bumping into you here."
    
    show td wkd with dissolve
    "The biker is none other than my best friend Touma."
    
    show sd date smile at right with dissolve
    sd "Hey Touma! What's up?"
    
    "[name]" "Hi Touma, I didn't know you liked biking."
    
    td "I didn't have a lot of homework this weekend"

    
    
    
    
    
    


    
    
    
    $ num = datesDone["sd"]
    
    "I have a picnic with Sourdough. This is date [num]."
    
    jump night