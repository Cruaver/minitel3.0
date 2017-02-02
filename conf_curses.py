#!/usr/bin/python3
# -*-coding:utf-8 -*

import curses

def init_curses():#{

    screen = curses.initscr()
    curses.noecho()
    curses.cbreak
    screen.keypad(True)
    screen.clear()
    screen.border(0)
    return (screen)
#}
