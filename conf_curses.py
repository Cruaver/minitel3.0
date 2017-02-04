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
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_WHITE)
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

def title(menu, screen):
    screen.addstr (2,1, "M     M  I  N    N  I  N    N  TTTTTTT  EEEEE  L         3333         00", curses.color_pair(4) | curses.A_BOLD)
    screen.addstr (3,1, "M M M M  I  N N  N  I  N N  N     T     E      L        3    3      0   0", curses.color_pair(4) | curses.A_BOLD)
    screen.addstr (4,1, "M  M  M  I  N  N N  I  N  N N     T     EEEE   L            3      0     0", curses.color_pair(4) | curses.A_BOLD)
    screen.addstr (5,1, "M     M  I  N   NN  I  N   NN     T     E      L        3    3      0   0    ", curses.color_pair(4) | curses.A_BOLD)
    screen.addstr (6,1, "M     M  I  N    N  I  N    N     T     EEEEE  LLLLL     3333   0    00 ", curses.color_pair(4) | curses.A_BOLD)
    file_line(screen, 8);
