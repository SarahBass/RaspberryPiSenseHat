####################################
#
#Sarah Bass
#Raspberry Pi Sense Hatpet
#
####################################

from sense_hat import SenseHat
import time
import sys, pygame
from pygame import mixer
from pygame.locals import *

pygame.init()
sense = SenseHat()

marioSongs = ("mariosound1.mp3", "mariosound2.mp3")
yoshiSongs = ("yoshisound1.mp3", "yoshisound2.mp3")
peachSongs = ("peachsound1.mp3", "peachsound2.mp3", "peachsound3.mp3")
kirbySongs = ("kirbysound1.mp3", "kirbysound2.mp3", "kirbysound3.mp3")
toadSongs = ("toadsound1.mp3", "toadsound2.mp3")
pikachuSongs =  ("pikachusound1.mp3", "pikachusound2.mp3")

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

rainbowMario = [
    p, p, p, r, r, r, w, p,
    dp, dp, dp, r, r, r, r, r,
    m, m, br, sk, br, e, sk, m,
    r, r, br, sk, sk, b, b, sk,
    o, o, o, br, sk, sk, sk, o,
    y, r, r, y, db, db, y, y,
    w, b, db, db, db, db, db, w,
    b, b, br, b, b, b, br, b]


mario = [
    b, b, b, r, r, r, w, b,
    b, b, b, r, r, r, r, r,
    b, b, br, sk, br, e, sk, b,
    b, b, br, sk, sk, sk, sk, sk,
    b, b, b, br, sk, sk, sk, b,
    b, r, r, y, db, db, y, b,
    w, b, db, db, db, db, db, w,
    b, b, br, b, b, b, br, b]

rainbowPeach = [
    p, p, p, o, p, o, p, p,
    dp, dp, dp, dp, o, dp, dp, dp,
    m, y, y, sk, y, y, y, m,
    y, y, sk, sk, e, sk, e, y,
    o, y, dp, sk, sk, sk, sk, o,
    y, y, dp, dp, dp, dp, dp, y,
    y, dp, dp, w, w, db, w, b,
    b, dp, dp, dp, dp, dp, dp, b]

peach = [
    b, b, b, o, b, o, b, b,
    b, b, b, dp, o, dp, b, b,
    b, y, y, sk, y, y, y, b,
    y, y, sk, sk, e, sk, e, y,
    b, y, dp, sk, sk, sk, sk, b,
    y, y, dp, dp, dp, dp, dp, b,
    y, dp, dp, w, w, db, w, b,
    b, dp, dp, dp, dp, dp, dp, b]

rainbowYoshi = [
    p, p, r, g, dg, g, p, p,
    dp, r, g, e, g, g, g, g,
    m, m, w, w, g, g, g, g,
    r, r, w, w, g, g, g, g,
    o, o, r, w, w, w, w, b,
    dg, r, dg, dg, w, w, dg, b,
    g, dg, g, dg, w, w, dg, dg,
    b, b, r, r, b, r, r, b]

yoshi = [
    b, b, r, g, dg, g, b, b,
    b, r, g, e, g, g, g, g,
    b, b, w, w, g, g, g, g,
    e, r, w, w, g, g, g, g,
    b, b, r, w, w, w, w, b,
    dg, r, dg, dg, w, w, dg, b,
    b, dg, g, dg, w, w, dg, dg,
    b, b, r, r, b, r, r, b]

rainbowKirby = [
    p, p, p, p, p, p, p, p,
    dp, dp, dp, dp, dp, dp, dp, dp,
    m, dp, dp, w, dp, w, dp, m,
    dp, dp, dp, e, dp, e, dp, dp,
    dp, dp, r, dp, dp, dp, r, dp,
    y, m, dp, dp, e, dp, dp, y,
    g, r, r, dp, dp, dp, m, g,
    r, r, r, m, m, m, m, b]

kirby = [
    b, b, b, b, b, b, b, b,
    b, b, dp, dp, dp, dp, b, b,
    b, dp, dp, w, dp, w, dp, b,
    dp, dp, dp, e, dp, e, dp, dp,
    dp, dp, r, dp, dp, dp, r, dp,
    m, m, dp, dp, e, dp, dp, m,
    b, r, r, dp, dp, dp, m, b,
    r, r, r, r, m, m, m, m]

rainbowToad = [
    p, p, w, w, r, r, r, p, 
    dp, w, w, w, r, r, r, w,
    m, r, r, w, w, w, w, r,
    r, r, r, w, sk, sk, sk, r,
    o, w, w, sk, e, sk, e, w,
    y, b, b, sk, sk, sk, y, y,
    g, sk, db, db, w, w, db, sk,
    b, b, br, br, b, br, br, b]

toad = [
    b, b, w, w, r, r, r, b, 
    b, w, w, w, r, r, r, w,
    b, r, r, w, w, w, w, r,
    b, r, r, w, sk, sk, sk, r,
    b, w, w, sk, e, sk, e, w,
    b, b, b, sk, sk, sk, b,b, 
    b, sk, db, db, w, w, db, sk,
    b, b, br, br, b, br, br, b]

empty = [
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e]

marioCounter = 0
kirbyCounter = 0
yoshiCounter = 0
pikachuCounter = 0
peachCounter = 0
toadCounter = 0

selectcharacter = "no"

########################################################################
    

#character = [readfilearray()]

#def readfilearray():
#    infile = open(filename)

#def characterMoveAnimate():

def chooseCharacterDisplay(chooseCharacter, marioCounter, yoshiCounter, kirbyCounter, pikachuCounter,peachCounter, toadCounter):
    

    mixer.music.set_volume(0.7)
    if chooseCharacter == "Mario" or chooseCharacter =="mario" or chooseCharacter =="MARIO":
            time.sleep(0.5)
            sense.set_pixels(rainbowicon1)
            time.sleep(0.5)
            sense.set_pixels(rainbowicon2)
            time.sleep(0.5)
            sense.set_pixels(rainbowMario)
            time.sleep(0.5)
            sense.set_pixels(mario)
            time.sleep(0.1)
            if (marioCounter == 0):
                mixer.music.load(marioSongs[0]) 
                mixer.music.play()
                marioCounter = 1 
                
            elif (marioCounter == 1):
                mixer.music.load(marioSongs[1]) 
                mixer.music.play()
                marioCounter = 0
            
    elif chooseCharacter == "Yoshi" or chooseCharacter =="yoshi" or chooseCharacter =="YOSHI":
            time.sleep(0.5)
            sense.set_pixels(rainbowicon1)
            time.sleep(0.5)
            sense.set_pixels(rainbowicon2)
            time.sleep(0.5)
            sense.set_pixels(rainbowYoshi)
            time.sleep(0.5)
            sense.set_pixels(yoshi)
            time.sleep(0.1)
            if yoshiCounter == 0:
                mixer.music.load(yoshiSongs[0]) 
                mixer.music.play()
                yoshiCounter = 1
            elif yoshiCounter == 1:
                mixer.music.load(yoshiSongs[1]) 
                mixer.music.play()
                yoshiCounter = 0
                
    elif chooseCharacter == "Kirby" or chooseCharacter =="kirby" or chooseCharacter =="KIRBY":
            time.sleep(0.5)
            sense.set_pixels(rainbowicon1)
            time.sleep(0.5)
            sense.set_pixels(rainbowicon2)
            time.sleep(0.5)
            sense.set_pixels(rainbowKirby)
            time.sleep(0.5)
            sense.set_pixels(kirby)
            time.sleep(0.1)
            if kirbyCounter == 0:
                mixer.music.load(kirbySongs[0]) 
                mixer.music.play()
                kirbyCounter = 1
            elif yoshiCounter == 1:
                mixer.music.load(kirbySongs[1]) 
                mixer.music.play()
                kirbyCounter = 0
    elif chooseCharacter == "Pikachu" or chooseCharacter =="pikachu" or chooseCharacter =="PIKACHU":
            time.sleep(0.5)
            sense.set_pixels(rainbowicon1)
            time.sleep(0.5)
            sense.set_pixels(rainbowicon2)
            time.sleep(0.5)
            sense.set_pixels(rainbowPikachu)
            time.sleep(0.5)
            sense.set_pixels(pikachu)
            time.sleep(0.1)
            if pikachuCounter == 0:
                mixer.music.load(pikachuSongs[0]) 
                mixer.music.play()
                pikachuCounter = 1
            elif yoshiCounter == 1:
                mixer.music.load(pikachuSongs[1]) 
                mixer.music.play()
                pikachuCounter = 0
    elif chooseCharacter == "Peach" or chooseCharacter =="peach" or chooseCharacter == "PEACH":
            time.sleep(0.5)
            sense.set_pixels(rainbowicon1)
            time.sleep(0.5)
            sense.set_pixels(rainbowicon2)
            time.sleep(0.5)
            sense.set_pixels(rainbowPeach)
            time.sleep(0.5)
            sense.set_pixels(peach)
            time.sleep(0.1)
            if peachCounter == 0:
                mixer.music.load(peachSongs[0]) 
                mixer.music.play()
                peachCounter = 1
            elif peachCounter == 1:
                mixer.music.load(peachSongs[1]) 
                mixer.music.play()
                peachCounter = 0
    elif chooseCharacter == "Toad" or chooseCharacter =="toad" or chooseCharacter =="TOAD":
            time.sleep(0.5)
            sense.set_pixels(rainbowicon1)
            time.sleep(0.5)
            sense.set_pixels(rainbowicon2)
            time.sleep(0.5)
            sense.set_pixels(rainbowToad)
            time.sleep(0.5)
            sense.set_pixels(toad)
            time.sleep(0.1)
            if toadCounter == 0:
                mixer.music.load(toadSongs[0]) 
                mixer.music.play()
                toadCounter =1
            elif toadCounter == 1:
                mixer.music.load(toadSongs[1]) 
                mixer.music.play()
                toadCounter = 0
    else:                 
        sense.set_pixels(empty)
        
      
while not (selectcharacter == "yes") or (selectcharacter =="YES") or (selectcharacter =="Yes") or (selectcharacter =="y"):
    
    print ("SELECT YOUR CHARACTER: ")
    print ("Pikachu, Mario, Yoshi, Kirby, Toad, Peach ")
    chooseCharacter = (input("I will select : "))
    chooseCharacterDisplay(chooseCharacter, marioCounter, yoshiCounter, kirbyCounter, pikachuCounter,peachCounter, toadCounter)
    print("ARE YOU SURE ? ")
    selectcharacter = (input("YES or NO : "))    


#Stop the mixer
input('\nEnter "quit" to quit: ')
#Ask user to stop program
if input == "quit" or "Quit" or "QUIT" or "Stop" or "stop":
        sense.clear()
        mixer.music.stop()