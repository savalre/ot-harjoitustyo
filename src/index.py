""" This file includes game loop and textual UI """

import sys
import os
from gui import GUI


def clear():
    """[clears terminal window so the game looks cleaner]
    """
    os.system("clear")


def select_level():
    """[Assigns a string value to players level of choice]

    Returns:
        [string]: [represents selected level]
    """
    return_value = ""

    while True:

        try:
            level = int(input("Choose level by typing number:\n1 Easy\n2 Medium\n3 Hard\n"))

            if level in (1,2,3):
                if level == 1:
                    return_value = "Easy"
                elif level == 2:
                    return_value = "Medium"
                else: 
                    return_value = "Hard"

                break

        except ValueError:
            print("Wrong input, try again")

    return return_value


def main():
    """
    This is textual game loop, that lets player choose level and then creates a
    new UI object that creates the gameboard. Then main() launches the game_loop in
    GUI class
    """
    game_off = False

    while not game_off:
        clear()
        print(" ")
        print("Welcome to Minesweeper!\nPlease choose what you want to do!\n")
        print(" ")

        while True:
            try:
                command = int(input("Press 1 if you want to play, press 2 if you want to quit \n"))
                if command in(1,2):
                    break
            except ValueError:
                print("Wrong input, try again")

        if command == 2:
            sys.exit()

        if command == 1:
            clear()
            level = select_level()

        game = GUI(level)
        game.game_loop()


if __name__ == '__main__':
    main()
