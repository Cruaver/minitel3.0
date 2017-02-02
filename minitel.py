#!/usr/bin/python3
# -*-coding:utf-8 -*

import curses
from curses import panel
from os import *
from tool import *
from info_generale import *
from display_proc import *
from conf_curses import *

infos_hardware_choos = {
    '1' : "cpu",
    '2' : "memory",
    '3' : "disk"
}

def display_submenu_info1():#{
    choice = 0
    
    while choice != ord('4'):#{
        screen = init_curses()
        screen.addstr(2, 2, "Please select your choice with numpad 1 to 4")
        screen.addstr(4, 4, "1 - Display CPU information")
        screen.addstr(5, 4, "2 - Display memory")
        screen.addstr(6, 4, "3 - Display memory left")
        screen.addstr(7, 4, "4 - Exit")
        screen.refresh()
        choice = screen.getch()
        if choice != ord('4'):#{
            curses.endwin()
            system("clear")
            infos_hardware(infos_hardware_choos[chr(choice)])
            raw_input("for close press enter")
        #}
    #}
    curses.endwin()
    return 1
#}

submenu_generale = {
    '1' : version_os,
    '2' : uptime,
    '3' : version_kernel,
    '4' : display_submenu_info1,
    '5' : limit_open_file,
    '6' : limit_open_proc,
    '7' : installed_package
}



def display_info_generale():#{
    choice = 0

    while choice != ord('8'):#{
        screen = init_curses()
        screen.addstr(2, 2, "Please select your choice with numpad 1 to 8")
        screen.addstr(4, 4, "1 - Version du systeme d" + str(unichr(96)) + "exploitation")
        screen.addstr(5, 4, "2 - Uptime")
        screen.addstr(6, 4, "3 - Version du Kernel")
        screen.addstr(7, 4, "4 - Informations Hardware")
        screen.addstr(8, 4, "5 - Limite de fichiers ouverts")
        screen.addstr(9, 4, "6 - Limite de processus ouverts")
        screen.addstr(10, 4, "7 - paquets installes")
        screen.addstr(11, 4, "8 - Exit")
        screen.refresh()
        choice = screen.getch()
        if choice != ord('8'):#{
            if choice != ord('4'):#{
                curses.endwin()
                system("clear")
            #}
            res = submenu_generale[chr(choice)]()
            if res == 0:
                raw_input("for close press enter")
        #}
    #}
    curses.endwin()
#}

menu_minitel = {
   '1': display_info_generale,
   #'2': display_info_reseau,
   '3': display_info_proc
}


def init_minitel():#{
    choice = 0
    
    while choice != ord('4'):#{
        screen = init_curses()
        screen.addstr(2, 2, "Please select your choice with numpad 1 to 4")
        screen.addstr(4, 4, "1 - Informations generales")
        screen.addstr(5, 4, "2 - Reseaux")
        screen.addstr(6, 4, "3 - Processus")
        screen.addstr(7, 4, "4 - Exit")
        screen.refresh()
        choice = screen.getch()
        if choice != ord('4'):#{
            curses.endwin()
            system("clear")
            menu_minitel[chr(choice)]()
        #}
    #}
    system("clear")
    curses.endwin()
#}

init_minitel()
