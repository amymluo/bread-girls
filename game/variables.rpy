# Variables in the game / setup

# Characters
define sd = Character("Sourdough")
define wb = Character ("Wheat")
define bt = Character ("Baguette")
define mp = Character ("Melon Pan")
define b = Character("Bagel")
define p = Character("Pizza")
define td = Character ("Touma Dachi")

##############################################

# Images

# Touma Dachi Images
image td smile = "touma.png"
image td laugh = "toumalaugh.png"
image td blush = "toumablush.png"
image td wink = "toumawink.png"

image td wkd = "toumdaweekend.png"
image td wkd smile = "toumawkdsmile.png"
image td wkd wave = "toumawkdwave.png"
image td wkd smile wave = "toumawkdsmilewave.png"
image td wkd pout = "toumawkdpout.png"


# Sourdough Images
image sd smile = "sourdough.png"
image sd laugh = "sourdoughlaugh.png"
image sd neutral = "sourdoughneutral.png"
image sd sad = "sourdoughsad.png"

image sd date smile = "sourdate.png"
image sd date laugh = "sourdatelaugh.png"
image sd date blush = "sourdateblush.png"
image sd date neutral = "sourdateneutral.png"
image sd date sad = "sourdatesad.png"

# Melon Pan
image mp smile = "melon.png"

# BackgroundImages
image bgClassroom = "classroom.jpg"
image bgHallway = "hallway.png"
image bgLib = "library.jpg"
image bgCaf = "cafeteria.jpg"
image bgRoof = "rooftop.jpg"
image bgStreet = "street.jpg"
image bgRamen = "ramen.jpg"
image bgBedroom = "bedroom.jpg"
image bgPark = "park.jpg"

####################################################

# Phone
image bgPhone = "phoneScreen.png"

# Touma Dachi
image tdName = "phone/td/name.png"
image meme1 = "phone/td/meme1.png"
image meme2 = "phone/td/meme2.png"
image meme3 = "phone/td/meme3.png"
image mcTdResp = "phone/td/mcResp.png"

# Sourdough
image sdName = "phone/sd/name.png"

#####################################################

#Counters

default secondDay = True

# Touma
default eatAloneCount = 0
default walkAloneCount = 0
 
# Sourdough
default datesDone = {"sd" : 0}

default points = {"sd" : 0}

###########################################################