"""
File: BeeperRowAdv.py
Name:
------------------------------
This program makes Karel fill up
Street 1 with some beepers already
existed
(This should be world insensitive)
"""

from karel.stanfordkarel import *

def turn_back():
    for i in range(2):
        turn_left()
def main():
    """
    Karel will fill the first Street in any world
    """
    put_beeper
    while front_is_clear():
        if on_beeper():
            move()
        else:
            put_beeper()
            move()
    put_beeper()
    turn_back()
    while front_is_clear():
        pick_beeper()
        move()
    turn_back()
    pass












####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)