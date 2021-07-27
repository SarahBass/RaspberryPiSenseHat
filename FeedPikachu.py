####################################
#
#Sarah Bass
#Raspberry Pi feed pikachu
#
####################################

from sense_hat import SenseHat
import time
import sys, pygame
from pygame import mixer
from pygame.locals import *

pygame.init()
sense = SenseHat()

pikachuSongs =  ["pikachusound1.mp3", "Pikachusound2.mp3"]

########################################################################
#color library codes
#magenta
m = (255,0,255)
#red
r = (255, 0, 0)
#empty or black
e = (0,0,0)
#white
w = (255,255,255)
#cyan blue
b = (0,255,255)
#orange
o = (255, 165,0)
#yellow
y = (255, 255, 0)
#green
g = (0, 255, 0)
#deep pink
dp = (255, 20, 147)
#purple
p = (138, 43, 226)
#brown
br = (210, 105, 30)
#peachy skin tone
sk = (255, 228, 196)
#deepgreen
dg = (0,128,0)
#deep blue
db = (0, 0, 225)


rainbowicon1 = [
    m, m, m, m, m, m, m, m,
    r, r, r, r, r, r, r, r,
    o, o, o, o, o, o, o, o,
    y, y, y, y, y, y, y, y,
    g, g, g, g, g, g, g, g,
    b, b, b, b, b, b, b, b,
    p, p, p, p, p, p, p, p,
    dp, dp, dp, dp, dp, dp, dp, dp
    ]

rainbowicon2 = [
    dp, dp, dp, dp, dp, dp, dp, dp,
    m, m, m, m, m, m, m, m,
    r, r, r, r, r, r, r, r,
    o, o, o, o, o, o, o, o,
    y, y, y, y, y, y, y, y,
    g, g, g, g, g, g, g, g,
    b, b, b, b, b, b, b, b,
    p, p, p, p, p, p, p, p 
    ]

rainbowPikachu = [
    p, e, p, p, p, p, e, p,
    dp, y, dp, dp, dp, dp, y, dp, 
    m, y, y, y, y, y, y, m,
    r, y, e, y, y, e, y, r,
    o, dp, y, y, y, y, dp, o,
    y, b, y, o, o, b, b, o, 
    g, o, y, o, o, y, o, g,
    b, y, y, br, br, y, y, b]


pikachu = [
    b, e, b, b, b, b, e, b,
    b, y, b, b, b, b, y, b, 
    b, y, y, y, y, y, y, b,
    b, y, e, y, y, e, y, b,
    b, dp, y, y, y, y, dp, o,
    b, b, y, o, o, b, b, o, 
    b, o, y, o, o, y, o, b,
    b, y, y, br, br, y, y, b]

pikachu1 = [
    b, e, e, b, b, b, b, e,
    b, b, y, o, b, b, b, o,
    b, b, b, y, y, y, y, o,
    o, o, b, y, e, y, y, e,
    o, o, b, dp, y, y, y, dp,
    b, o, b, y, o, o, o, b,
    b, o, y, o, y, o, y, b,
    b, b, y, o, br, br, o, b]

pikachuflip = [
    e, b, b, b, b, e, e, b,
    o, b, b, b, o, y, b, b,
    o, y, y, y, y, b, b, b,
    e, y, y, e, y, b, o, o,
    dp, y, y, y, dp, b, o, o,
    b, o, o, o, y, b, o, b,
    b, y, o, y, o, y, o, b,
    b, o, br, br, o, y, b, b]

pikachuleft = [
    e, b, b, b, b, e, e, b,
    o, b, b, b, o, y, b, b, 
    o, y, y, y, y, b, o, o, 
    e, y, y, e, y, b, o, o, 
    dp, y, y, y, dp, b, o, b,
    b, o, o, o, y, y, y, b,
    b, y, y, o, o, o, o, b,
    o, b, o, b, b, b, b, o,
    ]

pikachuright = [
    b, e, e, b, b, b, b, e,
    b, b, y, o, b, b, b, o, 
    o, o, b, y, y, y, y, o, 
    o, o, b, y, e, y, y, e,
    b, o, b, dp, y, y, y, dp,
    b, y, y, y, o, o, o, b,
    b, o, o, o, o, y, y, b,
    o, b, b, b ,b, o, b, o]


empty = [
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e]


apple = [
    e, e, e, e, e, g, e, e,
    e, r, r, r, g, r, r, e,
    r, w, dp, r, r, r, r, r,
    r, dp,r, r, r, r, r, r,
    r, r, r, r, r, r, r, r,
    r, r, r, r, r, r, r, r,
    e, r, r, r, r, r, r, e,
    e, e, r, r, r, r, e, e]

watermelon = [
    e, e, e, e, e, e, e, e,
    w, r, e, r, r, r, r, w,
    w, r, r, r, r, e, r, w,
    w, r, r, e, r, r, r, w,
    g, w, r, r, r, r, w, g,
    dg, g, w, w, w, w, g, dg,
    e, dg, g, g, g, g, dg, e,
    e, e, e, e, e, e, e, e]

pineapple = [
    e, e, g, e, g, e, g, e,
    e, e, e, g, g, g, e, e,
    e, e, o, dg, g, br, e, e,
    e, o, br, o, br, o, br, e,
    e, br, o, br, o, br, br, e,
    e, o, br, o, br, o, br, e,
    e, br, o, br, o, br, br, e,
    e, e, br, br, br, br, e, e]

banana = [
    e, e, e, e, e, y, y, e,
    e, e, e, e, e, e, o, y,
    e, e, e, e, e, o, br, o,
    y, y, y, y, y, y, br, y,
    o, y, y, y, y, br, y, y,
    br, o, o, br, br, y, y, y,
    o, y, y, y, y, y, y, e,
    e, o, y, y, y, y, e, e]

cherry =[
    e, e, e, e, g, g, g, e,
    e, e, e, g, e, g, e, e,
    e, e, g, e, e, g, e, e,
    e, e, g, e, e, r, r, e,
    e, r, r, e, r, r, w, r,
    r, r, w, r, e, r, r, r,
    r, r, r, r, e, r, r, e,
    e, r, r, e, e, e, e, e]

peach = [
    e, e, sk, sk, sk, dp, e, e,
    e, sk, sk, sk, sk, sk, dp, e,
    sk, sk, sk, sk, sk, sk, sk, dp,
    sk, sk, sk, sk, sk, sk, sk, dp,
    dp, sk, dp, sk, sk, sk, sk, dp,
    e, dp, dp, dp, sk, sk, dp, e,
    g, g, dp, dp, dp, dp, dp, g,
    e, e, e, e, g, g, g, e]

pear = [
    e, e, e, br, dg, g, e,e, 
    e, e, g, g, e, dg, g, e,
    e, g, y, g, g, e, e, e,
    e, g, y, g, g, e, e, e,
    g, y, g, g, g, dg, e, e,
    g, y, g, g, g, dg, e, e,
    dg, g, g, g, dg, dg, e, e,
    e, dg, dg, dg, dg, e, e, e]

orange = [
    e, e, r, r, g, g, e, e,
    e, o, o, o, dg, g, r, e,
    o, y, y, o, o, o, r, r,
    o, y, y, o, o, o, r, r,
    o, o, o, o, o, o, r, r,
    o, y, o, o, o, o, r, r,
    e, o, o, o, o, r, r, e,
    e, e, r, r, r, r, e, e]

grape = [
    e, e, e, e, e, e, e, g,
    e, e, b, b, e, b, w, e,
    e, e, db, db, db, b, b, e,
    e, b, db, e, w, db, db, e,
    e, b, db, b, b, db, b, w,
    e, db, db, db, db, db, b, b,
    b, db, b, w, db, db, db, e,
    b, db, b, b, e, b, b, e]

strawberry = [
    e, e, r, r, g, g, e, g,
    e, r, w, r, r, dg, g, e,
    e, w, r, r, g, g, dg, g,
    m, o, r, r, g, g, r, g,
    r, r, r, o, r, r, r, r,
    r, r, r, r, r, r, r, r,
    r, o, r, r, r, r, r, e,
    m, r, r, r, m, e, e, e]

tomato = [
    e, e, e, e, e, e, e, e,
    e, dg, e, g, g, e, dg, e,
    e, r, dg, dg, dg, dg, r, e,
    r, dg, r, dg, dg, r, dg, r,
    r, w, dp, r, r, r, r, r,
    r, dp, r, r, r, r, r, r,
    r, r, r, r, r, r, r, r,
    e, r, r, r, r, r, r, e]

radish = [
    e, g, g, e, g, g, g, e,
    g, e, g, g, g, e, g, g,
    e, e, e, g, e, e, e, e,
    e, dp, dp, dp, dp, dp, e, e,
    dp, sk, sk, dp, sk, sk, dp, e,
    w, w, w,sk, w, w, w, e,
    e, w, w, w, w, w, e, e,
    e, e, e, w, e, e, e, e]

pizza = [
    o, o, o, o, e, e, e, e,
    br, br, br, o, o, o, e, e,
    y, r, y, br, br, o, o, e,
    r, r, r, y,  y, br, o, e,
    y, r, y, y, y, br, o, o,
    y, y, y, y, r, r, br, o,
    y, r, r, y, r, r, br, o,
    y, r, r, y, y, y, br, o]

pancakes = [
    e, br, br, y, y, br, br, e,
    br, br, br, y, y, br, br, br,
    sk, br, br, br, br, br, br, sk,
    b, sk, m, sk, sk, sk, sk, br,
    sk, br, m, br, br, br, br, sk,
    br, sk, m, sk, sk, sk, sk, br,
    sk, br, m, br, br, br, br, sk,
    e, sk, m, sk, sk, sk, sk, e]

raspberry = [
        g, g, g, e, e, g, g, g,
        g, g, g, m, r, g, g, g,
        e, r, m, e, e, r, m, e,
        e, m, r, m, r, m, r, e,
        e, r, m, r, m, r, m, e,
        e, m, r, m, r, m, r, e,
        e, e, m, r, r, m, e, e,
        e, e, e, e, e, e, e, e]

blueberry = [
    e, e, e, r, br, e, e, e,
    e, e, e, br, e, e, e, e,
    e, db, b, br, b, b, e, e,
    dp, b, b, b, b, w, b, e,
    db, b, b, b, w, w, b, e,
    db, b, b, b, b, b, b, e,
    db, db, b, b, b, b, db, e,
    e, db, db, db, db, db, e, e]

cake = [
    e, e, e, r, r, w, w, e,
    e, e, w, r, r, w, w, w,
    e, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    br, sk, sk, br, br, sk, sk, br,
    sk, br, br, sk, sk, br, br, sk,
    br, br, br, br, br, br, br, br,
    sk, w, w, w, w, w, w, sk]


########################################################################
    

#character = [readfilearray()]

#def readfilearray():
#    infile = open(filename)

def pikachuAnimate():
            mixer.music.set_volume(0.7)
            time.sleep(0.5)
            sense.set_pixels(rainbowicon1)
            time.sleep(0.5)
            sense.set_pixels(rainbowicon2)
            time.sleep(0.5)
            sense.set_pixels(rainbowPikachu)
            time.sleep(0.5)
            sense.set_pixels(pikachu)
            time.sleep(0.1)
            mixer.music.load(pikachuSongs[0])
            mixer.music.play()
            sense.set_pixels(pikachuright)
            time.sleep(0.5)
            sense.set_pixels(pikachu)
            time.sleep(0.5)
            sense.set_pixels(pikachu1)
            time.sleep(0.5)
            sense.set_pixels(pikachuflip)
            time.sleep(0.5)
            sense.set_pixels(pikachuleft)
            time.sleep(0.5)
            sense.set_pixels(pikachuflip)
            time.sleep(0.5)
            sense.set_pixels(pikachu1)
            sense.set_pixels(pikachu)
            time.sleep(0.5)
            
print ("Welcome to FEED PIKACHU")


pikachuAnimate()         
userinput = "pikachu"      
while not (userinput == "yes") or (userinput =="YES") or (userinput =="Yes") or (userinput =="y"):  
    userinput = (input("Quit?: Yes. Play: ENTER FOOD HERE: "))
    if (userinput == "apple"):
            mixer.music.set_volume(0.7)
            time.sleep(0.5)
            sense.set_pixels(rainbowicon1)
            time.sleep(0.5)
            sense.set_pixels(rainbowicon2)
            time.sleep(0.5)
            sense.set_pixels(apple)
            time.sleep(0.5)
            mixer.music.load("Pikachusound2.mp3")
            mixer.music.play()
            time.sleep(0.5)
            sense.set_pixels(pikachu1)
            time.sleep(0.5)
    elif (userinput == "watermelon"):
            mixer.music.set_volume(0.7)
            time.sleep(0.5)
            sense.set_pixels(rainbowicon1)
            time.sleep(0.5)
            sense.set_pixels(rainbowicon2)
            time.sleep(0.5)
            sense.set_pixels(watermelon)
            time.sleep(0.5)
            mixer.music.load("Pikachusound2.mp3")
            mixer.music.play()
            time.sleep(0.5)
            sense.set_pixels(pikachu1)
            time.sleep(0.5)

    elif (userinput == "banana"):
            mixer.music.set_volume(0.7)
            time.sleep(0.5)
            sense.set_pixels(rainbowicon1)
            time.sleep(0.5)
            sense.set_pixels(rainbowicon2)
            time.sleep(0.5)
            sense.set_pixels(banana)
            time.sleep(0.5)
            mixer.music.load("Pikachusound2.mp3")
            mixer.music.play()
            time.sleep(0.5)
            sense.set_pixels(pikachu1)
            time.sleep(0.5)

    elif (userinput == "pineapple"):
            mixer.music.set_volume(0.7)
            time.sleep(0.5)
            sense.set_pixels(rainbowicon1)
            time.sleep(0.5)
            sense.set_pixels(rainbowicon2)
            time.sleep(0.5)
            sense.set_pixels(pineapple)
            time.sleep(0.5)
            mixer.music.load("Pikachusound2.mp3")
            mixer.music.play()
            time.sleep(0.5)
            sense.set_pixels(pikachu1)
            time.sleep(0.5)

    elif (userinput == "pear"):
            mixer.music.set_volume(0.7)
            time.sleep(0.5)
            sense.set_pixels(rainbowicon1)
            time.sleep(0.5)
            sense.set_pixels(rainbowicon2)
            time.sleep(0.5)
            sense.set_pixels(pear)
            time.sleep(0.5)
            mixer.music.load("Pikachusound2.mp3")
            mixer.music.play()
            time.sleep(0.5)
            sense.set_pixels(pikachu)
            time.sleep(0.5)

    elif (userinput == "peach"):
            mixer.music.set_volume(0.7)
            time.sleep(0.5)
            sense.set_pixels(rainbowicon1)
            time.sleep(0.5)
            sense.set_pixels(rainbowicon2)
            time.sleep(0.5)
            sense.set_pixels(peach)
            time.sleep(0.5)
            mixer.music.load("Pikachusound2.mp3")
            mixer.music.play()
            time.sleep(0.5)
            sense.set_pixels(pikachu)
            time.sleep(0.5)

    elif (userinput == "cherry"):
            mixer.music.set_volume(0.7)
            time.sleep(0.5)
            sense.set_pixels(rainbowicon1)
            time.sleep(0.5)
            sense.set_pixels(rainbowicon2)
            time.sleep(0.5)
            sense.set_pixels(cherry)
            time.sleep(0.5)
            mixer.music.load("Pikachusound2.mp3")
            mixer.music.play()
            time.sleep(0.5)
            sense.set_pixels(pikachu1)
            time.sleep(0.5)

    elif (userinput == "orange"):
            mixer.music.set_volume(0.7)
            time.sleep(0.5)
            sense.set_pixels(rainbowicon1)
            time.sleep(0.5)
            sense.set_pixels(rainbowicon2)
            time.sleep(0.5)
            sense.set_pixels(orange)
            time.sleep(0.5)
            mixer.music.load("Pikachusound2.mp3")
            mixer.music.play()
            time.sleep(0.5)
            sense.set_pixels(pikachuleft)
            time.sleep(0.5)

    elif (userinput == "pancakes"):
            mixer.music.set_volume(0.7)
            time.sleep(0.5)
            sense.set_pixels(rainbowicon1)
            time.sleep(0.5)
            sense.set_pixels(rainbowicon2)
            time.sleep(0.5)
            sense.set_pixels(pancakes)
            time.sleep(0.5)
            mixer.music.load("Pikachusound2.mp3")
            mixer.music.play()
            time.sleep(0.5)
            sense.set_pixels(pikachuflip)
            time.sleep(0.5)

    elif (userinput == "radish"):
            mixer.music.set_volume(0.7)
            time.sleep(0.5)
            sense.set_pixels(rainbowicon1)
            time.sleep(0.5)
            sense.set_pixels(rainbowicon2)
            time.sleep(0.5)
            sense.set_pixels(radish)
            time.sleep(0.5)
            mixer.music.load("Pikachusound2.mp3")
            mixer.music.play()
            time.sleep(0.5)
            sense.set_pixels(pikachu1)
            time.sleep(0.5)
            
    elif (userinput == "pizza"):
            mixer.music.set_volume(0.7)
            time.sleep(0.5)
            sense.set_pixels(rainbowicon1)
            time.sleep(0.5)
            sense.set_pixels(rainbowicon2)
            time.sleep(0.5)
            sense.set_pixels(pizza)
            time.sleep(0.5)
            mixer.music.load("Pikachusound2.mp3")
            mixer.music.play()
            time.sleep(0.5)
            sense.set_pixels(pikachu)
            time.sleep(0.5)

    elif (userinput == "tomato"):
            mixer.music.set_volume(0.7)
            time.sleep(0.5)
            sense.set_pixels(rainbowicon1)
            time.sleep(0.5)
            sense.set_pixels(rainbowicon2)
            time.sleep(0.5)
            sense.set_pixels(tomato)
            time.sleep(0.5)
            mixer.music.load("Pikachusound2.mp3")
            mixer.music.play()
            time.sleep(0.5)
            sense.set_pixels(pikachuflip)
            time.sleep(0.5)

    elif (userinput == "cake"):
            mixer.music.set_volume(0.7)
            time.sleep(0.5)
            sense.set_pixels(rainbowicon1)
            time.sleep(0.5)
            sense.set_pixels(rainbowicon2)
            time.sleep(0.5)
            sense.set_pixels(cake)
            time.sleep(0.5)
            mixer.music.load("Pikachusound2.mp3")
            mixer.music.play()
            time.sleep(0.5)
            sense.set_pixels(pikachuflip)
            time.sleep(0.5)

    elif (userinput == "grapes"):
            mixer.music.set_volume(0.7)
            time.sleep(0.5)
            sense.set_pixels(rainbowicon1)
            time.sleep(0.5)
            sense.set_pixels(rainbowicon2)
            time.sleep(0.5)
            sense.set_pixels(grape)
            time.sleep(0.5)
            mixer.music.load("Pikachusound2.mp3")
            mixer.music.play()
            time.sleep(0.5)
            sense.set_pixels(pikachu)
            time.sleep(0.5)

    elif (userinput == "strawberry"):
            mixer.music.set_volume(0.7)
            time.sleep(0.5)
            sense.set_pixels(rainbowicon1)
            time.sleep(0.5)
            sense.set_pixels(rainbowicon2)
            time.sleep(0.5)
            sense.set_pixels(strawberry)
            time.sleep(0.5)
            mixer.music.load("Pikachusound2.mp3")
            mixer.music.play()
            time.sleep(0.5)
            sense.set_pixels(pikachu)
            time.sleep(0.5)

    elif (userinput == "blueberry"):
            mixer.music.set_volume(0.7)
            time.sleep(0.5)
            sense.set_pixels(rainbowicon1)
            time.sleep(0.5)
            sense.set_pixels(rainbowicon2)
            time.sleep(0.5)
            sense.set_pixels(blueberry)
            time.sleep(0.5)
            mixer.music.load("Pikachusound2.mp3")
            mixer.music.play()
            time.sleep(0.5)
            sense.set_pixels(pikachu)
            time.sleep(0.5)

    elif (userinput == "raspberry"):
            mixer.music.set_volume(0.7)
            time.sleep(0.5)
            sense.set_pixels(rainbowicon1)
            time.sleep(0.5)
            sense.set_pixels(rainbowicon2)
            time.sleep(0.5)
            sense.set_pixels(raspberry)
            time.sleep(0.5)
            mixer.music.load("Pikachusound2.mp3")
            mixer.music.play()
            time.sleep(0.5)
            sense.set_pixels(pikachu1)
            time.sleep(0.5)
        
    else:
        time.sleep(0.5)
        sense.set_pixels(pikachu)
        time.sleep(0.5)
        sense.set_pixels(pikachu1)
        time.sleep(0.5)
        sense.set_pixels(pikachuflip)
        time.sleep(0.5)
        sense.set_pixels(pikachuleft)
        time.sleep(0.5)
        sense.set_pixels(pikachuflip)
        time.sleep(0.5)
        sense.set_pixels(pikachuleft)
        time.sleep(0.5)
        sense.set_pixels(pikachu1)
        time.sleep(0.5)
        


#Stop the mixer
input('\nEnter "quit" to quit: ')
#Ask user to stop program
if input == "quit" or "Quit" or "QUIT" or "Stop" or "stop":
        sense.clear()
        mixer.music.stop()