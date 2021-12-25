""" This file includes game loop and textual UI """

import sys
import os
import random
from board import *
from events import open_square
from ui import *

def clear():
    os.system("clear")      

def select_level():
    """[Gives an integer value to players level choice that grid_width() uses]

    Returns:
        [integer]: [represents selected level]
    """
    return_value = ""

    level = int(
        input("Choose level by typing number:\n1 Easy\n2 Medium\n3 Hard\n"))

    if level == 1:
        return_value = "Easy"

    if level == 2:
        return_value = "Medium"

    if level == 3:
        return_value = "Hard"

    return return_value

def main():
    """
    This is the gameloop
    """
    game_off = False

    while not game_off:
        clear()
        print(" ")
        print("Welcome to Minesweeper!\nPlease choose what you want to do!\n")
        print(" ")
        command = int(
            input("Press 1 if you want to play, press 2 if you want to quit \n"))

        if command == 2:
            sys.exit()

        if command == 1:
            clear()
            level = select_level()



        game = Ui(level)
        game.game_loop()

  
    """
        while not end:
            print(" ")
            for x in gameboard.player_view:
                for y in x:
                    print(y, end=" ")
                print()

            print("Open a square by typing row number SPACE column number (e.g. 1 2)\n")
            print("Flag a mine by typing F after row and column number (e.g. 1 2 F)\n")
            print("Unflag a mine by flagging a square again.\n")
            print(f"You have {gameboard.flags} flags left")
            command = input("Exit by typing e\n")

            if command == "e":
                sys.exit()

            check_game_status = open_square(gameboard, command)

            if check_game_status[0] is True:
                print_board(gameboard)
                if check_game_status[1] == 1:
                    print("Hihhihhii, kutittaa! Voitit pelin :)")
                    end = True
                else:
                    print("Hmmm :/ Hävisit pelin!")
                    end = True
        clear()
    """

if __name__ == '__main__':
    main()
