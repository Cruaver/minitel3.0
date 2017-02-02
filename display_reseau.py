#!/usr/bin/python3
# -*-coding:utf-8 -*

import curses
from curses import *
from os import *
from tool import *
from info_reseau import *
from conf_curses import *

submenu_reseau = {
    '1' : get_ip,
    '2' : is_interface,
    '3' : get_debit,
    '4' : routes
}

def display_info_reseau():#{
    choice = 0
    
    while choice != ord('5'):#{
        screen = init_curses()
        screen.addstr(2,2, "Please select your choice with numpad 1 to 5", curses.color_pair(2) | curses.A_BOLD)
        screen.addstr(4,4, "1 - Display IP", curses.color_pair(2))
        screen.addstr(5,4, "2 - Display Interface", curses.color_pair(2))
        screen.addstr(6,4, "3 - Display debit", curses.color_pair(2))
        screen.addstr(7,4, "4 - Display route", curses.color_pair(2))
        screen.addstr(8,4, "5 - Exit", curses.color_pair(2))
        screen.refresh()
        choice = screen.getch()
        if choice != ord('5'):#{
            curses.endwin()
            system("clear")
            res = submenu_reseau[chr(choice)]()
            if res == 0:#{
                system("setterm -term linux -back blue -fore white")
                raw_input("for close press enter")
                system("setterm -term linux -back black -fore white")
            #}
        #}
    #}
    curses.endwin()
#}
