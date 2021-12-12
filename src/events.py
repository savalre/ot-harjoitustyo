"""This file handles game events, such as flagging the mines and user commands"""

import board


def open_square(gameboard, command: str):

    square = __check_input(gameboard, command)

    if square is False:
        print("Wrong input! Try again!\n")
        return (False, 0)

    else:

        row = int(square[0])-1
        column = int(square[1])-1

        if len(square) == 3 and square[2] == 'F':
            __process_flags(gameboard, row, column)
            return (False, 0)

        if gameboard.player_view[row][column] == 'F':
            return (False, 0)

        gameboard.player_view[row][column] = gameboard.grid_values[row][column]

        check_win = __check_if_won(gameboard, row, column)

        if check_win is True:
            return (True, 1)
        # TRUE,1 on voitto. TRUE,0 on häviö. FALSE,0 on peli jatkuu

        game_over = __check_if_lost(gameboard, row, column)

        if game_over is True:
            return (True, 0)

        if game_over is False and gameboard.grid_values[row][column] == 0:
            __open_all_zero_squares(gameboard, row, column)
            return(False, 0)

        if check_win is False:
            return(False, 0)


def __check_input(gameboard, command):
    command.strip()

    square = command.split()

    if not square[0].isnumeric():
        return False

    if len(square) > 3 or len(square) < 2:
        return False

    if len(square) == 3 and square[2] != 'F':
        return False

    if int(square[0]) > gameboard.dimension or int(square[0]) < 1:
        return False

    if int(square[1]) > gameboard.dimension or int(square[1]) < 1:
        return False

    return square


def __check_if_won(gameboard, row, column):
    counter = 0
    rws = row
    clmn = column
    for rws in range(gameboard.dimension):
        for clmn in range(gameboard.dimension):
            if gameboard.player_view[rws][clmn] != 'M':
                if gameboard.player_view[rws][clmn] != '*':
                    if gameboard.player_view[rws][clmn] != 'F':
                        counter = counter+1

    mines_from_squares = (gameboard.dimension *
                          gameboard.dimension) - gameboard.mines
    if counter == mines_from_squares:
        return True

    return False


def __check_if_lost(gameboard, row, column):
    if gameboard.grid_values[row][column] == 'M':
        for row in range(gameboard.dimension):
            for column in range(gameboard.dimension):
                if gameboard.grid_values[row][column] == 'M':
                    if gameboard.player_view[row][column] == 'F': # todo WTF =_=
                        gameboard.player_view[row][column] = 'F'
                    else:
                        gameboard.player_view[row][column] = 'M'

                if (gameboard.player_view[row][column] == 'F'
                        and gameboard.grid_values[row][column] != 'M'):
                    gameboard.player_view[row][column] = 'X'

        return True

    return False


def __open_all_zero_squares(gameboard, row, column):
    visited = []

    __get_square_neighbours(gameboard, row, column, visited)


def __get_square_neighbours(gameboard, row, column, visited):

    if [row, column] not in visited:
        visited.append([row, column])

        if gameboard.grid_values[row][column] == 0:

            gameboard.player_view[row][column] = 0

            if row > 0:
                __get_square_neighbours(gameboard, row-1, column, visited)

            if column > 0:
                __get_square_neighbours(gameboard, row, column-1, visited)

            if row < gameboard.dimension-1:
                __get_square_neighbours(gameboard, row+1, column, visited)

            if column < gameboard.dimension-1:
                __get_square_neighbours(gameboard, row, column+1, visited)

            if row < gameboard.dimension-1 and column > 0:
                __get_square_neighbours(gameboard, row+1, column-1, visited)

            if row > 0 and column < gameboard.dimension-1:
                __get_square_neighbours(gameboard, row-1, column+1, visited)

            if row < gameboard.dimension-1 and column < gameboard.dimension-1:
                __get_square_neighbours(gameboard, row+1, column+1, visited)

            if row > 0 and column > 0:
                __get_square_neighbours(gameboard, row-1, column-1, visited)

        if gameboard.grid_values[row][column] != 0 and gameboard.grid_values[row][column] != 'M':
            gameboard.player_view[row][column] = gameboard.grid_values[row][column]


def __process_flags(gameboard, row, column):

    if gameboard.player_view[row][column] == 'F':
        gameboard.player_view[row][column] = '*'
        gameboard.flags = gameboard.flags+1
        return

    if gameboard.player_view[row][column] != '*':
        return

    if gameboard.player_view[row][column] != 'F' and gameboard.flags > 0:
        gameboard.player_view[row][column] = 'F'
        gameboard.flags = gameboard.flags-1
