"""
File: PotholeFilling.py
Name: TODO:
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *

"""
TODO:
"""
def turn_right():
    for i in range(3):
        turn_left()

def turn_back():
    for i in range(2):
        turn_left()

def filling_hole():
    move()
    turn_right()
    move()
    for i in range(99):
        put_beeper()
    turn_back()
    move()
    turn_right()
    move()

def picking_hole():
    move()
    turn_left()
    move()
    for i in range(99):
        pick_beeper()
    turn_back()
    move()
    turn_left()
    move()
def main():
    for i in range(3):
        filling_hole()
    turn_back()
    for i in range(3):
        picking_hole()
    turn_back()











####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)
