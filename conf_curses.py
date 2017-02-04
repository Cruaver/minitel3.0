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
    curses.cbreak()
    curses.noecho()
    screen.keypad(True)
    screen.clear()
    screen.border(0)
    fill_space(screen)
    footer(screen)
    return (screen)
#}

def footer(screen):#{
    max_y , max_x = screen.getmaxyx()
    screen.addstr(max_y - 2, 1, "(C) kabro_c, lorill_j, selatn_r, naze_g", curses.color_pair(2) | curses.A_BOLD)
    return (screen)
#}
