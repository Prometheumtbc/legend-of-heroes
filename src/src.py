from time import *
from random import *
from pynput import keyboard
from playsound import playsound
from ctypes import wintypes
import os, sys, random, json, ctypes, msvcrt, subprocess

kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
user32 = ctypes.WinDLL('user32', use_last_error=True)

SW_MAXIMIZE = 3

kernel32.GetConsoleWindow.restype = wintypes.HWND
kernel32.GetLargestConsoleWindowSize.restype = wintypes._COORD
kernel32.GetLargestConsoleWindowSize.argtypes = (wintypes.HANDLE,)
user32.ShowWindow.argtypes = (wintypes.HWND, ctypes.c_int)

def maximize_console(lines=None):
    fd = os.open('CONOUT$', os.O_RDWR)
    try:
        hCon = msvcrt.get_osfhandle(fd)
        max_size = kernel32.GetLargestConsoleWindowSize(hCon)
        if max_size.X == 0 and max_size.Y == 0:
            raise ctypes.WinError(ctypes.get_last_error())
    finally:
        os.close(fd)
    cols = max_size.X
    hWnd = kernel32.GetConsoleWindow()
    if cols and hWnd:
        if lines is None:
            lines = max_size.Y
        else:
            lines = max(min(lines, 9999), max_size.Y)
        subprocess.check_call('mode.com con cols={} lines={}'.format(
                                cols, lines))
        user32.ShowWindow(hWnd, SW_MAXIMIZE)

maximize_console()

def cls():  
    os.system('cls' if os.name=='nt' else 'clear')

def prints(x):
    for i in x:
        print(i, end="", flush=True)
        sleep(.001)

def loadGlobalJSON():

    global opened
    global played
    global saved

    with open("config/global.json") as f:
        raw = json.load(f)
        opened = raw.get("hasOpened")
        played = raw.get("hasPlayed")
        saved = raw.get("hasSaved")

def loadConfig():
    with open("config/config.json") as f:
        raw = json.load(f)

def fts():



def newSave():
    global seed

    prints("Enter a seed. Alternatively, leave blank for a random seed.")
    x = str(input())

    if x == "":
        seed = random.randrange(sys.maxsize)
    else:
        seed = x

    random.seed(seed)

    global name
    name = ""
    global HP
    HP = 0
    global MP
    MP = 0
    global frag
    frag = 0
    global step
    step = 0
    global over
    over = 0
    global opened
    global played
    global saved

 
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

def logo():
    print("                     `.-//+/:.`       `--------.`       .------------        `-://:-.       .-------------`    .--------.              .`           .`                         ")
    print("                   .ohdmmmmmmdy:      odddddddddhs-     ydddddddddddh     `:shdmmmmdhs.    `dddddddddddddd`    hho-----:/s/           /h/           y-                         ")
    print("                  :dmmmyo+oymmmd.    `dmmmmmmmmmmmd`   -mmmmdddddddd/    -ydmmdyyhmmmmy    :dddddddddddddo    :y-h-      `h:        `o+:h`         -y                          ")
    print("                  hmmmd-`  .yyyy.    /mmmmmmmmmmmmm.   smmmd------..`   .dmmmo.` `hdddh    `.....+s......`    y: -h-      y:       -s:  y/         s/                          ")
    print("                  ymmmmdhyso+:``     hmmmmmmmmmmmms   `dmmmdhhhhhh.     smmmd`    .....          y-          .h   -y-   `/s`      /s.   :h`       .h`                          ")
    print("                  `:syhddmmmmds     -mmmmmmmmmmmh+`   +mmmmddddddh     .dmmm+                   -h           oo````:h:-/o:`     `o+`     y/       +o                           ")
    print("                /sss+ `.-:hmmmd`    smmmdhhhyyo:.     hmmmy------.     +mmmm-   `syyy+          o/          `d+/////+ho.`      -s:       :h`     `h.                           ")
    print("                smmmd+:-:odmmd+    .dmmmo````        :mmmmhsssssss.    /mmmmho+ohmmmh.         `h`          /s       -y-      /s.         y/     :dyyyyyyyyyyys                ")
    print("                -hmmmmmmmmmdy:     ommmd.            ymmmmmmmmmmmd      odmmmmmmmdh+`          +o           h/........:h-   `ss.........../h     ymmmmmmmmmmmm/                ")
    print("                 `:+ssyss+:.       /+++/             ++++++++++++:       ./ossso/-`            :.          `+////////////   :+/////////////+`   `+++++++++++++`                ")
    print("                                                                                                                                                                               ")
    print("                                            .::-:/.   .:-://.   :::::::.``:::+:::.`/  :`   /  .::::/.   +:::::-   :    `:.` `:--::.                                            ")
    print("                                            o.:.`./-`./`-.../:` / :``````  ``o.:```::-.+: -/.//.-...//. o.:``.+/.`o-.`::.-- +.-.`./:.                                          ")
    print("                                            .:+:-.` -:`:`   -// +-+---`      o.-    +:-s/-+`//.:`   .// o.:```/./`o:++:--`  .:+:-.` -                                          ")
    print("                                           `- `.-:o-`:-:    ::/`/ /----.     o.-    :/s.s+:.-::/    -::`s:+:/+---`s+:-/o.   - `.-:o-`                                          ")
    print("                                            //.``-/`: /+.``-/`/ / :          o.-     +o-oo:/  :+.``-:`/ o.:..-o- `+-:` .+-  :/-``./`/                                          ")
    print("                                             `:/:-.-`  `:/:---` ` -          ``-     ``/``:.   `:/:---` `.-   `.- `-.   `.-  `:/:-.-.                                          ")
            

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
 
if not opened:
    fts()
else: