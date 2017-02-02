#!/usr/bin/python3
# -*-coding:utf-8 -*

import curses
from curses import panel
from os import *
from tool import *

menu_minitel = {1 : display_info_generale(screen)}

def display_info_generale(win):#{
    choice = 0

    while choice != ord('4'):#{
        screen = curses.initscr()
        screen.clear()
        screen.border(0)
        screen.addstr(2, 2, "Please select your choice with numpad 1 to 8")
        screen.addstr(4, 4, "1 - Version du système d’exploitation")
        screen.addstr(5, 4, "2 - Uptime")
        screen.addstr(6, 4, "3 - Version du Kernel")
        screen.addstr(7, 4, "4 - Informations Hardware")
        screen.addstr(8, 4, "5 - Limite de fichiers ouverts")
        screen.addstr(9, 4, "6 - Limite de processus ouverts")
        screen.addstr(10, 4, "7 - paquets installés")
        screen.addstr(11, 4, "8 - Exit")
        screen.refresh()
        choice = screen.getch()
    #}
#}
        
def init_minitel():#{
    choice = 0
    
    while check != ord('4'):#{
        screen = curses.initscr()
        screen.clear()
        screen.border(0)
        screen.addstr(2, 2, "Please select your choice with numpad 1 to 4")
        screen.addstr(4, 4, "1 - Informations générales")
        screen.addstr(5, 4, "2 - Réseaux")
        screen.addstr(6, 4, "3 - Processus")
        screen.addstr(7, 4, "4 - Exit")
        screen.refresh()
        choice = screen.getch()
        if x == ord('1'):
            #display_info_generale(screen)
            curses.endwin()
            print menu_minitel['1']
        #if x == ord('2'):
        #if x == ord('3'):
    #}
    curses.endwin()
#}

init_minitel()
