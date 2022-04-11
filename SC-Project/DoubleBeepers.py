"""
File: DoubleBeepers.py
Name:
-------------------------------
TODO:
"""

from karel.stanfordkarel import *
def turn_back():
    for i in range(2):
        turn_left()
def double_beeper():
    pick_beeper()
    move()
    turn_back()
    for i in range(2):
        put_beeper()
    move()
    turn_back()
def set_beeper():
    pick_beeper()
    turn_back()
    move()
    put_beeper()
    turn_back()
    move()
    """
    Karel will double the beepers
    """
def main():
    while not on_beeper():
        move()
    while on_beeper():
        double_beeper()
    move()
    while on_beeper():
        set_beeper()
    turn_back()
    while front_is_clear():
        move()
    turn_back()














####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)