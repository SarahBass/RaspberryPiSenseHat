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
