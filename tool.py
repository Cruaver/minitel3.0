#!/usr/bin/python3
# -*-coding:utf-8 -*
import curses
from os import *
import sys
import time
from proc import *

def fill_line(screen, y):#{
    x = 1
    max_y , max_x = screen.getmaxyx()
    while x < (max_x - 1):#{
        screen.addstr(y, x, "_", curses.color_pair(1) | curses.A_BOLD)
        x += 1
    #}
#}
    
def fill_space(screen):#{
    max_y, max_x = screen.getmaxyx()
    y = 1
    while y < (max_y - 1):#{
        x = 1
        while x < (max_x - 1):#{
            screen.addstr(y, x, ' ', curses.color_pair(1))
            x += 1
        y += 1
        #}
    #}
#}
        
def page_proc(screen):#{
    list_proc = get_process()
    i = 0
    page_tab = []
    max_y, max_x = screen.getmaxyx()
    while i < len(list_proc):#{
        y = 0
        tab = []
        while i < len(list_proc) and y < max_y - 17 and max_y > 16:#{
            tab.append(list_proc[i])
            i += 1
            y += 1
        page_tab.append(tab)
        #}
    #}
    return page_tab
#}
