import sys
import pygame
from board import *
from events import open_square

def select_level():
    return_value = ""

    level = int(input("Choose level by typing number:\n1 Easy\n2 Medium\n3 Hard\n"))

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

if __name__ == '__main__':
    print(" ")
    print("Welcome to Minesweeper!\nPlease choose what you want to do!\n")
    print(" ")
    command = int(input("Press 1 if you want to play, press 2 if you want to quit \n"))

    if command == 2:
        sys.exit()

    if command == 1:
        level = select_level()
        grid_width = grid_width(level)
        gameboard = Board(level, grid_width)

    end = False

    while not end:
        print(" ")
        for x in gameboard.player_view:
            for y in x:
                print(y, end = " ")
            print()

        print("Open a square by typing row number SPACE column number (e.g. 1 2)\n")
        print("Flag a mine by typing F after row and column number (e.g. 1 2 F)\n")
        print("Unflag a mine by flagging a square again.\n")
        print(f"You have {gameboard.flags} flags left")
        command = input("Exit by typing e\n")

        if command == "e":
            sys.exit()

        game_over = open_square(gameboard, command)

        if game_over is True:
            print_board(gameboard)
            print("You hit a mine! Game over!")
            end = True

#pelin voi voittaa :D:
    # pelaaja avaa kaikki turvalliset ruudut

#input handler pls ettei tarvi koko ajan rankaista mokailusta. eventtiin varmaankin
