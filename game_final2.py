import enemies as enemies
import items as items
import speech_recognition as sr 
import os
import random
from sense_hat import SenseHat
import time

sense = SenseHat()
sense.set_rotation(90)

l=[231,132,234]
p=[43,113,37]
f=[14,70,10]
b=[145,92,19]
y=[240,220,11]
m=[193,109,24]
g=[99,81,81]
n=[183,113,53]
i=[86,78,70]
t=[250,222,11]
r=[223,70,13]
u=[4,61,242]
h=[237,188,170]
s=[139,144,163]
x=[108,187,62]
z=[231,143,40]
e=[0,0,0]
w=[255,255,255]

DM_1 = [
l,l,l,l,l,l,l,l,
l,l,e,l,l,e,l,l,
l,l,e,l,l,e,l,l,
l,l,l,l,l,l,l,l,
l,l,l,e,e,l,l,l,
l,l,e,l,l,e,l,l,
l,l,l,e,e,l,l,l,
l,l,l,l,l,l,l,l
]
#sense.set_pixels(DM_1)


DM_2 = [
l,l,l,l,l,l,l,l,
l,l,e,l,l,e,l,l,
l,l,e,l,l,e,l,l,
l,l,l,l,l,l,l,l,
l,e,l,l,l,l,e,l,
l,l,e,e,e,e,l,l,
l,l,l,l,l,l,l,l,
l,l,l,l,l,l,l,l,
]
#sense.set_pixels(DM_2)


pokal = [
e,e,e,e,e,e,e,e,
e,t,t,t,t,t,e,e,
e,t,t,t,t,t,e,e,
e,t,t,t,t,t,e,e,
e,e,t,t,t,e,e,e,
e,e,e,t,e,e,e,e,
e,e,e,t,e,e,e,e,
e,e,t,t,t,e,e,e
]
#sense.set_pixels(pokal)


wizard_1 = [
e,e,e,e,u,e,e,e,
e,e,e,u,u,u,e,e,
e,e,e,y,y,y,e,e,
e,u,u,u,u,u,u,u,
e,e,h,w,h,w,h,e,
e,e,s,s,s,s,s,e,
e,e,s,e,e,e,s,e,
e,e,s,s,s,s,s,e
]
#sense.set_pixels(wizard_1)


wizard_2 = [
e,e,e,e,u,e,e,e,
e,e,e,u,u,u,e,e,
e,e,e,y,y,y,e,e,
e,u,u,u,u,u,u,u,
e,e,h,r,h,r,h,e,
e,e,s,s,s,s,s,e,
e,e,s,s,e,e,s,e,
e,e,s,s,s,s,s,e
]
#sense.set_pixels(wizard_2)



enemy_1_1 = [
m,m,m,m,m,m,m,m,
m,m,m,m,m,m,m,m,
m,e,m,m,m,m,e,m,
m,e,e,m,m,e,e,m,
m,m,m,m,m,m,m,m,
e,m,m,m,m,w,m,m,
m,e,e,e,e,e,e,m,
m,m,m,m,m,m,m,m
]
#sense.set_pixels(enemy_1_1)



enemy_1_2 = [
m,m,m,m,m,m,m,m,
m,m,m,m,m,m,m,m,
m,e,m,m,m,m,e,m,
m,e,e,m,m,e,e,m,
m,m,m,m,m,m,m,m,
m,m,m,m,m,w,m,m,
e,e,e,e,e,e,e,m,
m,m,m,m,m,m,m,m
]
#sense.set_pixels(enemy_1_2)


enemy_2_1 = [
g,g,g,g,g,g,g,g,
g,e,g,g,g,g,e,g,
g,g,e,g,g,e,g,g,
g,g,g,g,g,g,g,g,
g,g,g,g,g,g,g,g,
g,e,e,e,e,e,e,g,
g,e,g,g,g,w,g,g,
g,g,g,g,g,g,g,g
]
#sense.set_pixels(enemy_2_1)


enemy_2_2 = [
g,g,g,g,g,g,g,g,
g,e,g,g,g,g,e,g,
g,g,e,g,g,e,g,g,
g,g,g,g,g,g,g,g,
g,g,g,g,g,g,g,g,
g,e,e,e,e,e,e,g,
g,g,w,g,g,w,g,g,
g,g,g,g,g,g,g,g
]
#sense.set_pixels(enemy_2_2)


enemy_3_1 = [
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r,
r,e,e,r,r,e,e,r,
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r,
r,e,e,e,e,e,e,r,
r,r,r,r,r,w,r,r,
r,r,r,r,r,r,r,r
]
#sense.set_pixels(enemy_3_1)


enemy_3_2 = [
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r,
r,e,e,r,r,e,e,r,
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r,
r,r,e,e,e,e,r,r,
r,r,r,r,r,w,r,r,
r,r,r,r,r,r,r,r
]
#sense.set_pixels(enemy_3_2)


treasure_1 =  [
e,e,e,e,e,e,e,e,
e,e,n,n,n,n,e,e,
e,n,n,n,n,n,n,e,
e,i,i,i,i,i,i,e,
e,n,n,i,i,n,n,e,
e,n,n,n,n,n,n,e,
e,n,n,n,n,n,n,e,
e,e,e,e,e,e,e,e
]
#sense.set_pixels(treasure_1)


treasure_2 = [
e,e,n,n,n,n,e,e,
e,i,i,i,i,i,i,e,
e,e,t,t,t,t,e,e,
e,i,i,i,i,i,i,e,
e,n,n,i,i,n,n,e,
e,n,n,n,n,n,n,e,
e,n,n,n,n,n,n,e,
e,e,e,e,e,e,e,e
]
#sense.set_pixels(treasure_2)


forest_1 = [
e,e,e,e,e,y,y,e,
e,e,p,e,f,y,y,y,
e,e,p,e,f,f,y,e,
e,p,p,p,f,f,e,e,
e,p,p,p,f,f,f,e,
p,p,p,p,p,f,e,e,
p,p,p,p,p,f,f,e,
e,e,b,e,b,e,e,e
]
#sense.set_pixels(forest_1)


forest_2 = [
e,e,e,e,e,y,y,e,
e,e,p,e,f,y,y,y,
e,e,p,e,f,y,y,e,
e,p,p,p,f,f,f,e,
p,p,p,p,f,f,e,e,
p,p,p,p,p,f,f,e,
e,p,p,p,p,f,e,e,
e,e,b,e,b,e,e,e
]
#sense.set_pixels(forest_2)


dragon_1 = [
e,e,e,e,e,e,e,e,
e,e,e,x,e,e,e,e,
e,x,x,w,e,x,x,e,
e,x,x,x,e,x,e,e,
z,e,e,x,x,e,e,x,
e,e,e,x,x,x,x,x,
e,e,e,x,x,x,x,e,
e,e,e,e,x,e,e,e
]
#sense.set_pixels(dragon_1)


dragon_2 = [
e,e,e,e,e,e,e,e,
e,e,e,e,x,e,e,e,
e,x,x,w,e,e,e,e,
y,z,x,x,e,x,x,e,
z,e,e,x,x,x,e,x,
e,e,e,x,x,x,x,x,
e,e,e,x,x,x,x,e,
e,e,e,e,x,e,e,e
]
#sense.set_pixels(dragon_2)


you_ded = [
s,s,s,s,s,s,s,s,
e,s,e,s,s,e,s,e,
s,e,s,s,s,s,e,s,
e,s,e,s,s,e,s,e,
s,s,s,s,s,s,s,s,
s,e,e,e,e,e,e,s,
s,s,s,s,r,r,r,s,
s,s,s,s,s,r,s,s
]
#sense.set_pixels(you_ded)



#DEFINITIONEN--------------------------------------------

class Enemy:
    def __init__(self, name, hp, damage, AC):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.AC = AC
 
    def is_alive(self):
        return self.hp > 0

Goblin=Enemy("Goblin",2,2,"10")
Rat=Enemy("Rat",2,2,"10")
Bandit=Enemy("Bandit",2,2,"10")
Wizard=Enemy("Wizard",20,5,"15")
Boar=Enemy("Boar",20,5,"15")
Orc=Enemy("Orc",25,5,"14")
Dragon=Enemy("Dragon",6,3,"14")

def recognize_speech_from_mic(recognizer, microphone):
    """Transcribe speech from recorded from `microphone`.

    Returns a dictionary with three keys:
    "success": a boolean indicating whether or not the API request was
               successful
    "error":   `None` if no error occured, otherwise a string containing
               an error message if the API could not be reached or
               speech was unrecognizable
    "transcription": `None` if speech could not be transcribed,
               otherwise a string containing the transcribed text
    """
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response object accordingly
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response

#DAMAGERANDOMIZER--------------------------------------------------------------------------------


def randam(n):
    if n == 0:
        os.system('echo "0" | festival --tts')
    elif n == 1:
        os.system('echo "1" | festival --tts')
    elif n == 2:
        os.system('echo "2" | festival --tts')
    elif n == 3:
        os.system('echo "3" | festival --tts')
    


#ENCOUNTER--------------------------------------------------------------------------------------
def encounter(n):
    if n == 1:
        goblin()
    elif n == 2:
        rat()
    elif n == 3:
        bandit()

def goblin():
    os.system('echo "A Goblin appears" | festival --tts')
    sense.set_pixels(enemy_1_2)
    list = [0,1,2]
    while Goblin.hp > 0:
        sense.show_message("AC :" + Goblin.AC)
        sense.set_pixels(enemy_1_2)
        os.system('echo "Hero roll your die is it higher then the AC?" | festival --tts')
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()
        answer = recognize_speech_from_mic(recognizer, microphone)
        #answer = "yes"
        if answer == "no":
            os.system('echo "The Goblin attacks you" | festival --tts')
            dn = random.choice(list)
            #dn=0
            os.system('echo "you take " | festival --tts')
            randam(dn)
            os.system('echo " damage" | festival -tts')
            os.system('echo "Is the Hero slain" | festival --tts')
            recognizer = sr.Recognizer()
            microphone = sr.Microphone()
            answer = recognize_speech_from_mic(recognizer, microphone)
            if answer == "yes":
                sense.set_pixels(you_ded)
                os.system('echo "You are dead and the Vinnermoore succums to darkness" | festival --tts')
                
        else:
            os.system('echo "The Goblin looses 2 health" | festival --tts')
            Goblin.hp = Goblin.hp - 2
        
def rat():
    os.system('echo "A Giant Rat appears" | festival --tts')
    sense.set_pixels(enemy_2_2)
    list = [0,1,2]
    while Rat.hp > 0:
        sense.show_message("AC :" + Goblin.AC)
        sense.set_pixels(enemy_2_2)
        os.system('echo "Hero roll your die is it higher then the AC?" | festival --tts')
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()
        answer = recognize_speech_from_mic(recognizer, microphone)
        #answer = "yes"
        if answer == "no":
            os.system('echo "The Giant Rat bites you" | festival --tts')
            dn = random.choice(list)
            #dn=0
            os.system('echo "you take " | festival --tts')
            randam(dn)
            os.system('echo " damage" | festival -tts')
            os.system('echo "Is the Hero slain" | festival --tts')
            recognizer = sr.Recognizer()
            microphone = sr.Microphone()
            answer = recognize_speech_from_mic(recognizer, microphone)
            if answer == "yes":
                sense.set_pixels(you_ded)
                os.system('echo "You are dead and the Vinnermoore succums to darkness" | festival --tts')
        else:
            os.system('echo "The Rat looses 2 health" | festival --tts')
            Rat.hp = Rat.hp - 2

def bandit():
    os.system('echo "A bandit appears" | festival --tts')
    sense.set_pixels(enemy_3_1)
    list = [0,1,2]
    while Bandit.hp > 0:
        sense.show_message("AC :" + Bandit.AC)
        sense.set_pixels(enemy_3_1)
        os.system('echo "Hero roll your die is it higher then the AC?" | festival --tts')
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()
        answer = recognize_speech_from_mic(recognizer, microphone)
        #answer = "yes"
        if answer == "no":
            os.system('echo "The Bandit attacks you with his rusty blade" | festival --tts')
            dn = random.choice(list)
            #dn=0
            os.system('echo "you take " | festival --tts')
            randam(dn)
            os.system('echo " damage" | festival -tts')
            os.system('echo "Is the Hero slain" | festival --tts')
            recognizer = sr.Recognizer()
            microphone = sr.Microphone()
            answer = recognize_speech_from_mic(recognizer, microphone)
            if answer == "yes":
                sense.set_pixels(you_ded)
                os.system('echo "You are dead and the Vinnermoore succums to darkness" | festival --tts')
        else:
            os.system('echo "The bandit looses 2 health" | festival --tts')
            Bandit.hp = Bandit.hp - 2

def dragon():
    os.system('echo "The way is lit by natural skylights, and you can see the night sky outside." | festival --tts')
    os.system('echo "deep inside the cave, you hear growling and snarling. the evil dragon awaits you" | festival --tts')
    sense.set_pixels(dragon_1)
    list = [1,2,3]
    while Dragon.hp > 0:
        sense.show_message("AC :" + Dragon.AC)
        sense.set_pixels(dragon_1)
        os.system('echo "Hero roll your die is it higher then the AC?" | festival --tts')
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()
        answer = recognize_speech_from_mic(recognizer, microphone)
        #answer = "yes"
        if answer == "no":
            os.system('echo "The Dragon attacks you with his fiery breath" | festival --tts')
            dn = random.choice(list)
            dn=0
            os.system('echo "you take " | festival --tts')
            randam(dn)
            os.system('echo " damage" | festival -tts')
            os.system('echo "Is the Hero slain" | festival --tts')
            recognizer = sr.Recognizer()
            microphone = sr.Microphone()
            answer = recognize_speech_from_mic(recognizer, microphone)
            if answer == "yes":
                sense.set_pixels(you_ded)
                os.system('echo "You are dead and the Vinnermoore succums to darkness" | festival --tts')
        else:
            os.system('echo "The dragon looses 3 health" | festival --tts')
            Dragon.hp = Dragon.hp - 3
    
#SPIEL--------------------------------------------------------------------------

sense.set_pixels(wizard_1)
os.system('echo "Vinnermoore is in need of adventurers to get rid of the dragon terrorizing it" | festival --tts')
os.system('echo "Your Adventure starts at the forest gates" | festival --tts')
sense.set_pixels(forest_1)
os.system('echo "You start your track into the woods" | festival --tts')
os.system('echo "You follow the dark path until you come upon a crossroad" | festival --tts')
os.system('echo "The trees around you rustle and you sense a hostile presence" | festival --tts')
list = [1,2,3]
encounter(random.choice(list))
#encounter(1)
os.system('echo "You are victorious and defeated your enemy." | festival --tts')
sense.set_pixels(treasure_2)
os.system('echo "The battles so far have hardened you. Add 2 to your Quality dice rolls." | festival --tts')
os.system('echo "Now which way to go" | festival --tts')
sense.set_pixels(forest_1)
os.system('echo "One path to the left follows the river" | festival --tts')
os.system('echo "To the right, more trees await" | festival --tts')
os.system('echo "Do you go left of right" | festival --tts')
recognizer = sr.Recognizer()
microphone = sr.Microphone()
answer = recognize_speech_from_mic(recognizer, microphone)
if answer == "right":
    os.system('echo "You follow the river along the woods." | festival --tts')
    os.system('echo "On the Riverbank you come across the Dragons cavern" | festival --tts')
    dragon()
else:
    os.system('echo "You continue your trek into the woods." | festival --tts')
    os.system('echo "onward, you can see the lair in which the dragon resides." | festival --tts')
    dragon()

os.system('echo "You slay the beast. Behind the cadaver you find your treasure" | festival --tts')
sense.set_pixels(pokal)
os.system('echo "Victorious, you return into the village." | festival --tts')
os.system('echo "Thank you for playing hero. come back if you want to tempt fate again" | festival --tts')
