"""This file handles game events, such as flagging the mines and user commands"""


def open_square(gameboard, row: int, column: int):
    """[checks the square that player wants to open, opens the square for player
        and checks if player loses, wins, want's to flag a square or if
        game continues]

    Args:
        gameboard ([board]): [board object that is used in the current game]
        command (str): [description]

    Returns:
        [boolean]: [Returns tuple (False, 0) if game continues,
        (True, 1) if player wins with this move and (True,0) if player loses with this move]
    """

    if gameboard.player_view[row][column] == 'F':
        return (False, 0)

    grid_value = gameboard.grid_values[row][column]
    gameboard.player_view[row][column] = grid_value

    gameboard.player_view[row][column] = gameboard.grid_values[row][column]

    check_win = __check_if_won(gameboard, row, column)

    if check_win is True:
        return (True, 1)

    game_over = __check_if_lost(gameboard, row, column)

    if game_over is True:
        return (True, 0)

    if game_over is False and gameboard.grid_values[row][column] == 0:
        __open_all_zero_squares(gameboard, row, column)
        return(False, 0)

    if check_win is False:
        return(False, 0)


def __check_if_won(gameboard, row, column):
    """[counts the open squares in players board. if the number of opened squares
        equals (gameboard squares - number of mines), the game is won]

    Args:
        gameboard ([board]): [board object that is used in the current game]
        row ([integer]): [represents in which row the processed square is]
        column ([integer]): [represents in which column the processed square is]

    Returns:
        [boolean]: [returns True if game is won, False if not]
    """
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
    """[if the square that player opened contains mine, the game is lost]

    Args:
        gameboard ([board]): [board object that is used in the current game]
        row ([integer]): [represents in which row the processed square is]
        column ([integer]): [represents in which column the processed square is]

    Returns:
        [boolean]: [returns true if the game is lost, otherwise false]
    """
    if gameboard.grid_values[row][column] == 'M':
        for rw in range(gameboard.dimension):
            for clmn in range(gameboard.dimension):
                if gameboard.grid_values[rw][clmn] == 'M':
                    if gameboard.player_view[rw][clmn] == 'F':
                        gameboard.player_view[rw][clmn] = 'F'
                    else:
                        gameboard.player_view[rw][clmn] = 'M'

                if (gameboard.player_view[rw][clmn] == 'F'
                        and gameboard.grid_values[rw][clmn] != 'M'):
                    gameboard.player_view[rw][clmn] = 'X'

        return True

    return False


def __open_all_zero_squares(gameboard, row, column):
    """[creates an empty list and calls recursive __get_square_neighbours
        for the first time]

    Args:
        gameboard ([board]): [board object that is used in the current game]
        row ([integer]): [represents in which row the processed square is]
        column ([integer]): [represents in which column the processed square is]
    """
    visited = []

    __get_square_neighbours(gameboard, row, column, visited)


def __get_square_neighbours(gameboard, row, column, visited):
    """[sets square value to zero, logs that we have visited the square, then recursively
        checks the squares neighbours and opens them until no more 0 squares are met]

    Args:
        gameboard ([board]): [board object that is used in the current game]
        row ([integer]): [represents in which row the processed square is]
        column ([integer]): [represents in which column the processed square is]
        visited ([type]): [list that logs which squares are already visited]
    """

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


def process_flags(gameboard, row, column):
    """[processes the flag inputs. If the flagged square is reflagged(or deflagged in this
        case), the method closes square again. If the square isn't closed, method returns
        because only closed squares can be flagged. After flagging the square the number
        of flags available is diminished by 1]

    Args:
        gameboard ([board]): [board object that is used in the current game]
        row ([integer]): [represents in which row the processed square is]
        column ([integer]): [represents in which column the processed square is]
    """

    if gameboard.player_view[row][column] == 'F':
        gameboard.player_view[row][column] = '*'
        gameboard.flags = gameboard.flags+1
        return

    if gameboard.player_view[row][column] != '*':
        return

    if gameboard.player_view[row][column] != 'F' and gameboard.flags > 0:
        gameboard.player_view[row][column] = 'F'
        gameboard.flags = gameboard.flags-1
