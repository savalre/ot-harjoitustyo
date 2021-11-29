#This class handles game events, such as flagging the mines and user commands
from board import *

def open_square(gameboard, command:str):
    square = command.split()
    row = int(square[0])-1
    column = int(square[1])-1

    gameboard.player_view[row][column] = gameboard.grid_values[row][column]
