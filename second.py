from stanfordkarel import *


def main():
    """Karel code goes here!"""
    turn_right()
    move()
    turn_left()
    for i in range (3):
        move()
    turn_right()
    for i in range(2):
        move()
    turn_right()
    for i in range(5):
        move()
    put_beeper()


#turning right
def turn_right():
    for i in range (3):
        turn_left()

if __name__ == "__main__":
    run_karel_program()