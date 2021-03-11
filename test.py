from time import sleep
import os
import ctypes
import msvcrt
import subprocess

from ctypes import wintypes

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


print("This game is best played in fullscreen.")

maximize_console()
sleep(5)

print("\n\n\n\n\n                     `.-//+/:.`       `--------.`       .------------        `-://:-.       .-------------`    .--------.              .`           .`                         ")
print("                   .ohdmmmmmmdy:      odddddddddhs-     ydddddddddddh     `:shdmmmmdhs.    `dddddddddddddd`    hho-----:/s/           /h/           y-                         ")
print("                  :dmmmyo+oymmmd.    `dmmmmmmmmmmmd`   -mmmmdddddddd/    -ydmmdyyhmmmmy    :dddddddddddddo    :y-h-      `h:        `o+:h`         -y                          ")
print("                  hmmmd-`  .yyyy.    /mmmmmmmmmmmmm.   smmmd------..`   .dmmmo.` `hdddh    `.....+s......`    y: -h-      y:       -s:  y/         s/                          ")
print("                  ymmmmdhyso+:``     hmmmmmmmmmmmms   `dmmmdhhhhhh.     smmmd`    .....          y-          .h   -y-   `/s`      /s.   :h`       .h`                          ")
print("                  `:syhddmmmmds     -mmmmmmmmmmmh+`   +mmmmddddddh     .dmmm+                   -h           oo````:h:-/o:`     `o+`     y/       +o                           ")
print("                /sss+ `.-:hmmmd`    smmmdhhhyyo:.     hmmmy------.     +mmmm-   `syyy+          o/          `d+/////+ho.`      -s:       :h`     `h.                           ")
print("                smmmd+:-:odmmd+    .dmmmo````        :mmmmhsssssss.    /mmmmho+ohmmmh.         `h`          /s       -y-      /s.         y/     :dyyyyyyyyyyys                ")
print("                -hmmmmmmmmmdy:     ommmd.            ymmmmmmmmmmmd      odmmmmmmmdh+`          +o           h/........:h-   `ss.........../h     ymmmmmmmmmmmm/                ")
print("                 `:+ssyss+:.       /+++/             ++++++++++++:       ./ossso/-`            :.          `+////////////   :+/////////////+`   `+++++++++++++`                ")
sleep(1000)