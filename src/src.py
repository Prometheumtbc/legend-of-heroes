from time import *
from random import *
from pynput import keyboard
from playsound import playsound
import os, sys, random, json


# define globals

global name
global HP
global MP
global frag
global step
global over
global seed
global opened
global played
global saved


def cls():  
    os.system('cls' if os.name=='nt' else 'clear')

def prints(x):
    for i in x:
        print(i, end="", flush=True)
        sleep(.001)

def loadGlobalJSON():
    with open("config\global.json") as f:
        raw = json.read(json.load(f))
        opened = raw.get("hasOpened")
        played = raw.get("hasPlayed")
        saved = raw.get("hasSaved")

def boot():
    
    prints("Please enter a seed. Leave blank for a random seed.")
    x = str(input())

    if x == "":
        seed = random.randrange(sys.maxsize)
    else:
        seed = x

    random.seed(seed)
 
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
            

def north():
    print ("To go north press n then enter")
 
def east():
    print ("To go east press e then enter")
 
def south():
    print ("to go south press s then enter")
 
def west():
    print ("To go west press w then enter")

def overlay():
    print(name)
    print("[ HP: " + str(HP))
    print("[ MP: " + str(MP))
    print("")
    print("[ FRAG: " + str(frag))
    print("[ STEP: " + str(step))
    print("[ OVER: " + str(over))
    print("\n\n")

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
 
