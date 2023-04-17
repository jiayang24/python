"""
File: Steeplechase.py
Name: Jiayang chung
---------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
        if front_is_clear():
            move()
        else:
             jump()
             turn_left()

def jump():
    """
    pre-condition: Karel is on the left, facing east
    post-condition:Karel is on the upper left, facing North
    """
    up()
    cross()
    down()
def up():
    """
    pre-condition: Karel is on the left, facing east
    post-condition: Karel is at the upper left, facing North
    """
    while not front_is_clear():
        turn_left()
        # Karel is facing North, wall is on the right
        while not right_is_clear():
         move()
        turn_right()
def turn_right():
    for i in range(3):
        turn_left()
def cross():
    """
    pre-condition: Karel is ot the upper left, facing North
    post-condition: Karel is at the upper right, facing South
    """
    move()
    turn_right()

def down():
    while front_is_clear():
        move()





# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
