#!/usr/bin/python3
# -*-coding:utf-8 -*

import curses
from tool import *

def init_curses():#{
    screen = curses.initscr()
    curses.noecho()
    curses.cbreak
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_CYAN)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_CYAN)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_CYAN)
    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLUE)
    screen.keypad(True)
    screen.clear()
    screen.border(0)
    fill_space(screen)
    return (screen)
#}

init_curses()