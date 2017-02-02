#!/usr/bin/python3
# -*-coding:utf-8 -*
import curses
import os
import sys
import time
from proc import *

def fill_line(screen, y, x_max):#{
    x = 1
    while x < (x_max - 1):#{
        screen.addstr(y, x, "_", curses.color_pair(1) | curses.A_BOLD)
        x += 1
    #}
    return screen
#}
    
def fill_space(screen):#{
    max_y, max_x = screen.getmaxyx()
    y = 1
    while y < (max_y - 1):#{
        x = 1
        while x < (max_x - 1):#{
            screen.addstr(y, x, " ", curses.color_pair(4))
            x += 1
            y += 1
        #}
    #}
    return screen
#}
        
def page_proc(screen):#{
    list_proc = proc()
    i = 0
    page_tab = []
    max_y, max_x = screen.getmaxyx()
    while i < len(list_proc) - 2:#{
        y = 0
        tab = []
        while y < max_y - 5 and max_y > 5:#{
            #print i, list_proc[i] , len(list_proc) - 1
            tab.append(list_proc[i])
            i += 1
            y += 1
        page_tab.append(tab)
        #}
    #}
    return page_tab
#}

def get_input(string):#{
    screen.clear()
    screen.border(0)
    screen.addstr(2, 2, string)
    screen.refresh()
    inpute = screen.getstr(10, 10, 60)
    return inpute
#}

def cmd(string):#{
    system("clear")
    res = system(string)
    print ""
    if res == 0:
        print "Command executed correctly"
    else:
        print "Command terminated with error"
    raw_input("Press enter")
    print ""
#}