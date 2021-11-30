# This class handles game events, such as flagging the mines and user commands
import board


def open_square(gameboard, command: str):
    command.strip()

    square = command.split()

    if not square[0].isnumeric():
        print("Wrong input! Try again!")
        return

    row = int(square[0])-1
    column = int(square[1])-1

    gameboard.player_view[row][column] = gameboard.grid_values[row][column]

    game_over = __check_if_lost(gameboard, row, column)

    if game_over is False and gameboard.grid_values[row][column] == 0:
        __open_all_zero_squares(gameboard, row, column)

    return game_over


def __check_if_lost(gameboard, row, column):
    if gameboard.grid_values[row][column] == 'M':

        for row in range(gameboard.dimension):
            for column in range(gameboard.dimension):
                if gameboard.grid_values[row][column] == 'M':
                    gameboard.player_view[row][column] = 'M'

        return True
    return False


def __open_all_zero_squares(gameboard, row, column):
    visited = []

    __get_square_neighbours(gameboard, row, column,visited)


def __get_square_neighbours(gameboard, row, column,visited):

    if [row, column] not in visited:
        visited.append([row, column])

        if gameboard.grid_values[row][column] == 0:

            gameboard.player_view[row][column] = 0

            if row > 0:
                __get_square_neighbours(gameboard, row-1, column,visited)

            if column > 0:
                __get_square_neighbours(gameboard, row, column-1,visited)

            if row < gameboard.dimension-1:
                __get_square_neighbours(gameboard, row+1, column,visited)

            if column < gameboard.dimension-1:
                __get_square_neighbours(gameboard, row, column+1,visited)

            if row < gameboard.dimension-1 and column > 0:
                __get_square_neighbours(gameboard, row+1, column-1,visited)

            if row > 0 and column < gameboard.dimension-1:
                __get_square_neighbours(gameboard, row-1, column+1,visited)

            if row < gameboard.dimension-1 and column < gameboard.dimension-1:
                __get_square_neighbours(gameboard, row+1, column+1,visited)

            if row > 0 and column > 0:
                __get_square_neighbours(gameboard, row-1, column-1,visited)

        if gameboard.grid_values[row][column] != 0 and gameboard.grid_values[row][column] != 'M':
            gameboard.player_view[row][column] = gameboard.grid_values[row][column]
