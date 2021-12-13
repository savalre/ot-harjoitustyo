""" This file includes game loop and textual UI """

import sys
import tkinter
import random
from board import *
from events import open_square

#window = tkinter.Tk()
#window.title("TkInter example")
# window.mainloop()


def select_level():
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


def grid_width(level):
    grid = 0

    if level == "Easy":
        grid = 10

    if level == "Medium":
        grid = 16

    if level == "Hard":
        grid = 30

    return grid


def mines_count(level):
    mines = 0

    if level == "Easy":
        mines = 10

    if level == "Medium":
        mines = 40

    if level == "Hard":
        mines = 99

    return mines


def get_random_squares(mines, dimension):
    count = 0

    mine_squares = []

    while count < mines:
        num = random.randint(0, (dimension * dimension) - 1)

        row = num // dimension
        column = num % dimension

        if (row, column) not in mine_squares:
            count = count+1
            mine_squares.append((row, column))

    return mine_squares


def main():
    print(" ")
    print("Welcome to Minesweeper!\nPlease choose what you want to do!\n")
    print(" ")
    command = int(
        input("Press 1 if you want to play, press 2 if you want to quit \n"))

    if command == 2:
        sys.exit()

    if command == 1:
        level = select_level()
        width = grid_width(level)
        mines = mines_count(level)
        mines_squares = get_random_squares(mines, width)
        gameboard = Board(mines_squares, width)

    end = False

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
                print("YOU WON! CONGRATULATIONS!")
                end = True
            else:
                print("You hit a mine! Game over!")
                end = True


if __name__ == '__main__':
    main()
