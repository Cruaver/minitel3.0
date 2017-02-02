#!/usr/bin/python3
# -*-coding:utf-8 -*

import curses
from tool import *

def init_curses():#{
    screen = curses.initscr()
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLUE)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLUE)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLUE)
    screen.keypad(True)
    screen.clear()
    screen.border(0)
    fill_space(screen)
    return (screen)
#}
