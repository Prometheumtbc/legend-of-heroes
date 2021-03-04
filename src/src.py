from time import *
from random import *
from pynput import keyboard
import os, sys, random, json

def cls():  
    os.system('cls' if os.name=='nt' else 'clear')

def prints(x):
    for i in x:
        print(i, end="", flush=True)
        sleep(.001)
 
def title():  

        sleep(1)

        print (u"\u001b[30;1m   __                           _          __                                  ")
        print ("  / /  ___  __ _  ___ _ __   __| |   ___  / _|   /\  /\___ _ __ ___   ___  ___ ")
        print (" / /  / _ \/ _` |/ _ \ '_ \ / _` |  / _ \| |_   / /_/ / _ \ '__/ _ \ / _ \/ __|")
        print ("/ /__|  __/ (_| |  __/ | | | (_| | | (_) |  _| / __  /  __/ | | (_) |  __/\__ \ ")
        print ("\____/\___|\__, |\___|_| |_|\__,_|  \___/|_|   \/ /_/ \___|_|  \___/ \___||___/")

        sleep(.15)
        cls()

        print (u"\u001b[0m   __                           _          __                                  ")
        print ("  / /  ___  __ _  ___ _ __   __| |   ___  / _|   /\  /\___ _ __ ___   ___  ___ ")
        print (" / /  / _ \/ _` |/ _ \ '_ \ / _` |  / _ \| |_   / /_/ / _ \ '__/ _ \ / _ \/ __|")
        print ("/ /__|  __/ (_| |  __/ | | | (_| | | (_) |  _| / __  /  __/ | | (_) |  __/\__ \ ")
        print ("\____/\___|\__, |\___|_| |_|\__,_|  \___/|_|   \/ /_/ \___|_|  \___/ \___||___/")

        sleep(.15)
        cls()

        print (u"\u001b[37;1m   __                           _          __                                  ")
        print ("  / /  ___  __ _  ___ _ __   __| |   ___  / _|   /\  /\___ _ __ ___   ___  ___ ")
        print (" / /  / _ \/ _` |/ _ \ '_ \ / _` |  / _ \| |_   / /_/ / _ \ '__/ _ \ / _ \/ __|")
        print ("/ /__|  __/ (_| |  __/ | | | (_| | | (_) |  _| / __  /  __/ | | (_) |  __/\__ \ ")
        print ("\____/\___|\__, |\___|_| |_|\__,_|  \___/|_|   \/ /_/ \___|_|  \___/ \___||___/ \u001b[0m")

        sleep(1)
 
def castle():
 
    castle = [
    "*                                 |>>>                    +        ",
    "+          *                      |                   *       +",
    "                    |>>>      _  _|_  _   *     |>>>           ",
    "           *        |        |;| |;| |;|        |                 *",
    "     +          _  _|_  _    \\\.    .  /    _  _|_  _       +",
    " *             |;|_|;|_|;|    \\\: +   /    |;|_|;|_|;|",
    "               \\\..      /    ||:+++. |    \\\.    .  /           *",
    "      +         \\\.  ,  /     ||:+++  |     \\\:  .  /",
    "                 ||:+  |_   _ ||_ . _ | _   _||:+  |       *",
    "          *      ||+++.|||_|;|_|;|_|;|_|;|_|;||+++ |          +",
    "                 ||+++ ||.    .     .      . ||+++.|   *",
    "+   *            ||: . ||:.     . .   .  ,   ||:   |               *",
    "         *       ||:   ||:  ,     +       .  ||: , |      +",
    "  *              ||:   ||:.     +++++      . ||:   |         *",
    "     +           ||:   ||.     +++++++  .    ||: . |    +",
    "           +     ||: . ||: ,   +++++++ .  .  ||:   |             +",
    "                 ||: . ||: ,   +++++++ .  .  ||:   |        *",
    "                 ||: . ||: ,   +++++++ .  .  ||:   |"
    ]

    for i in castle:
        print(i)
        sleep(.01)

def saveNew():
    None

def load():
    None    

def north():
    print ("To go north press n then enter")
 
def east():
    print ("To go east press e then enter")
 
def south():
    print ("to go south press s then enter")
 
def west():
    print ("To go west press w then enter")
 
 
def setup():
    global name
    global HP
    global MP
    global frag
    global step
    global over
    global seed
    global lvl
    global exp
    global progHex
 
    prints("What is your name, warrior? ")
    name = input()
    seed = random.randrange(sys.maxsize)
    random.seed(seed)
    HP = randint(5,20)
    MP = randint(5,20)
    frag = randint(25,75)
    step = randint(25,75)
    over = randint(25,75)
    progHex = "000000000000"
 
def villager():
    global npcname
    global response
 
    responses = ["Hi", "Are you a hero?", "Are you from this village?", "There has been a dark shadow cast across the village"]
    npcnamechoice = ["Roger", "Dexter", "Sarah", "Susan"]
 
    random.shuffle(npcnamechoice)
    npcname = npcnamechoice[0]
 
    prints("\n["+npcname+":] Hello, my name is "+npcname+", Would you like to talk to me?\n")
    random.shuffle(responses)
    prints("Press y to talk to the villager")
 
    if input() == "y":
        print ("["+npcname+":] " +responses[0])
    else:
        print("["+npcname+":] Goodbye")
 
def enemy():
    global enemyHP
    global enemyMP
    global enemyname
 
    enemyHP = randint(5,20)
    enemyMP = randint(5,20)
    enemyname = "Ogre"
 
    print ("\nSuddenly you hear a roar, and from the shadows you see an "+enemyname+" coming straight at you....")
    print ("Your enemy has " + " " + str(enemyHP) + " " + "Health Points")
    print ("Your enemy has " + " " + str(enemyMP) + " " + "Magic Points")

def save():
    global _dict

    _dict = {
                {
            "location": {
                "x": x,
                "y": y
            },

            "playerStats": {
                "hp": HP,
                "mp": MP,
                "lvl": lvl,
                "exp": exp,
                "step": step,
                "over": over,
                "frag": frag
            },

            "internal": {
                "seed": seed,
                "ver": ""
            },

            "progression": {
                "code": progHex
            }
        }
    }
 
 
cls()
title()
castle()
setup()
 
global name
global HP
global MP
global move
global enemyHP
global x
global y

 
prints("Welcome to Middle Earth, " + name)
sleep(2)
prints("\nYour health is " + str(HP))
prints("\nYour magic skill is " + str(MP))
prints("\nFrag - " + str(frag))
prints("\nStep - " + str(step))
prints("\nOver - " + str(over))
 
 
print ("Would you like to venture out into the land?")
 
if input() == "y":
    print ("You are in your home, with a roaring fireplace in front of you, above the fire you can see your sword and shield")
    print ("Would you like to take your sword and shield? Press y then enter to continue")
 
    if input() == "y":
        weapons = ["sword", "shield", "lance", "mace"]
        random.shuffle(weapons)
        print ("You are now carrying your" + " " + weapons[0] + " " + "and your" + " " + weapons[1])
        print ("Armed with your " + weapons[0] + " " + "and " + weapons[1] + " you swing open the door to your home and see a green valley gleaming in the sunshine.")
 
    else:
        print ("You choose not to take your weapons")
        print ("Armed with your sense of humour, You swing open the door to see a green valley full of opportunity awaiting you.")
 
else:
    print ("You stay at home, sat in your favourite chair watching the fire grow colder. Middle Earth no longer has a hero.")
    print ("Game Over")
    sys.exit(0)
    
print ("In the distance to the north you can see a small village, to the east you can see a river and to the west a field of wild flowers.")
 
print ("\n")
north()
east()
west()
 
move = input("Where would you like to go? ")
 
if move == 'n':
    print ("\nYou move to the north, walking in the sunshine.")
    print ("A villager is in your path and greets you")
 
elif move == 'e':
    print ("\nYou walk to the river which lies to the east of your home.")
    print ("A villager is in your path and greets you")
 
elif move == 'w':
    print ("\nYou walk to the field of wild flowers, stopping to take in the beauty")
    print ("A villager is in your path and greets you\n")
 
villager()
enemy()
sleep(3)
 
fight = input("Do you wish to fight?" )
 
if fight == "y":
 
    while HP > 0:
        hit = randint(0,5)
        print ("You swing your sword and cause " + str(hit) + " of damage")
        enemyHP = enemyHP - hit
        print (enemyHP)
        enemyhit = randint(0,5)
        print ("The ogre swings a club at you and causes " + str(enemyhit) + " of damage")
        HP = HP - enemyhit
        print (HP)
 
else:
    print ("You turn and run away from the ogre")
 

print ("   _       _                 _")
print ("  /_\   __| |_   _____ _ __ | |_ _   _ _ __ ___")
print (" //_\\ / _` \ \ / / _ \ '_ \| __| | | | '__/ _ \ ")
print ("/  _  \ (_| |\ V /  __/ | | | |_| |_| | | |  __/")
print ("\_/ \_/\__,_| \_/ \___|_| |_|\__|\__,_|_|  \___|")
 
print ("                     _ _")
print ("  __ ___      ____ _(_) |_ ___")
print (" / _` \ \ /\ / / _` | | __/ __|")
print ("| (_| |\ V  V / (_| | | |_\__ \ ")
print (" \__,_| \_/\_/ \__,_|_|\__|___/")
 
print (" _   _  ___  _   _")
print ("| | | |/ _ \| | | |")
print ("| |_| | (_) | |_| |")
print (" \__, |\___/ \__,_|")
print (" |___/")