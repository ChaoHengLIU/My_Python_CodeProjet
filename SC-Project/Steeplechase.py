"""
File: Steeplechase.py
Name: TODO:
---------------------------------
TODO:
"""

from karel.stanfordkarel import *
def turn_right():
    for i in range(3):
        turn_left()
def up():
    while not front_is_clear():
        turn_left()
        move()
        turn_right()
    move()
    turn_right()
def down():
    while front_is_clear():
        move()
    turn_left()

def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(7):
        if front_is_clear():
            move()
        up()
        down()
    turn_left()
    for i in range(15):
        move()
    turn_left()
    while front_is_clear():
        move()
    turn_left()
    while front_is_clear():
        move()
    turn_left()
    pass













####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)
