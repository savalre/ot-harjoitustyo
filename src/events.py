#This class handles game events, such as flagging the mines and user commands
from board import *


def open_square(gameboard, command:str):
    square = command.split()
    row = int(square[0])-1
    column = int(square[1])-1

    gameboard.player_view[row][column] = gameboard.grid_values[row][column]

    game_over = __check_if_lost(gameboard, row, column)

    return game_over

def __check_if_lost(gameboard, row:int, column:int):
    print("tänne on tultu")
    if gameboard.grid_values[row][column] == 'M':

        for x in range(gameboard.n):
            for y in range(gameboard.n):
                if gameboard.grid_values[x][y] == 'M':
                    gameboard.player_view[x][y] = 'M'

        return True
