#!/usr/bin/python3
# -*-coding:utf-8 -*

import curses
from curses import *
from os import *
from tool import *
from proc import *
from conf_curses import *

def display_process():#{
    choice = 0
    page = 0
    
    while choice != ord('q') and choice != ord('Q'):#{
        screen = init_curses()
        screen.addstr(2,2, "Process List , Press 'q' for exit")
        screen.addstr(3,2, "Press '6' for next page and '4' for prev page")
        screen.addstr(5,4, "[PID]")
        screen.addstr(5,30, "[Name]")
        screen.addstr(5,50, "[Page : " + str(page) + "]")
        tab = page_proc(screen)
        i = 0
        while i < len(tab[page]):#{
            screen.addstr(6 + i,4, str(tab[page][i]['pid']))
            screen.addstr(6 + i,30, str(tab[page][i]['name']))
            i += 1
        #}
        screen.refresh()
        choice = screen.getch()
        if choice != ord('q') and choice != ord('Q'):#{
            if choice == ord('4') and page > 0:
                page -= 1
            elif choice == ord('6') and page < len(tab) - 1:
                page += 1
            curses.endwin()
            system("clear")
        #}
    #}
    curses.endwin()
    return (1)
#}

submenu_proc = {
    '1' : display_process,
    '2' : statuts_process,
    '3' : kill_process
}


def display_info_proc():#{
    choice = 0

    while choice != ord('4'):#{
        screen = init_curses()
        screen.addstr(2,2, "Please select your choice with numpad 1 to 4")
        screen.addstr(3,4, "1 - Process list")
        screen.addstr(4,4, "2 - Get process infomation")
        screen.addstr(5,4, "3 - Kill a process")
        screen.addstr(6,4, "4 - Exit")
        screen.refresh()
        choice = screen.getch()
        if choice != ord('4'):#{
            curses.endwin()
            system("clear")
            res = submenu_proc[chr(choice)]()
            if res == 0:
                raw_input("for close press enter")
        #}
    #}
    curses.endwin()
#}
