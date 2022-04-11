"""
File: BeeperRow.py
Name:
-------------------------
This program makes Karel fill up
Street 1 with beepers
(This program should be world insensitive)
"""

from karel.stanfordkarel import *


def main():
    while facing_east():
        while front_is_clear():
            put_beeper()
            move()
        for i in range(2):
            turn_left()
        put_beeper()
        while front_is_clear():
            pick_beeper()
            move()
        for i in range(2):
            turn_left()
        pick_beeper()
    pass

















####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)