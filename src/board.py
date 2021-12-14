"""[This file includes the board generating methods]
    """


class Board:

    """This class generates two boards for the game:
        one with actual values and one that is shown to the player
    """

    def __init__(self, mine_squares: list, grid_width: int):
        """[Constructor for Board class, creates new gameboard]

        Args:
            mine_squares (list): [list which has coordinates where to assign mines]
            grid_width (int): [width of gameboard]
        """
        self.flags = len(mine_squares)
        self.mines = len(mine_squares)
        self.dimension = grid_width
        self.grid_values = []
        self.player_view = []
        self._create_hidden_board(mine_squares)
        self._create_player_board()

    def _create_hidden_board(self, mine_squares):
        """[creates the hidden gameboard with mine locations and numbers]

        Args:
            mine_squares ([list]): [list which has coordinates where to assign mines]
        """
        self.grid_values = [
            [0 for y in range(self.dimension)] for x in range(self.dimension)]
        self._add_mines(mine_squares)
        self._add_numbers_to_squares()

    def _create_player_board(self):
        """[creates the board that is visible to the player]
        """
        self.player_view = [
            ['*' for y in range(self.dimension)] for x in range(self.dimension)]

    def _add_mines(self, mine_squares):
        """[adds mines to hidden board]

        Args:
            mine_squares ([list]): [list which has coordinates where to assign mines]
        """

        for mine in mine_squares:
            row = mine[0]
            column = mine[1]

            self.grid_values[row][column] = 'M'

    def _add_numbers_to_squares(self):
        """[if square is not mine, method checks it's neighbours to see 
            how many mines are nearby and assigns number values accordingly]
        """
        for row in range(self.dimension):
            for column in range(self.dimension):

                if self.grid_values[row][column] == 'M':
                    continue

                if row > 0 and self.grid_values[row-1][column] == 'M':
                    self.grid_values[row][column] = self.grid_values[row][column] + 1

                if column > 0 and self.grid_values[row][column-1] == 'M':
                    self.grid_values[row][column] = self.grid_values[row][column] + 1

                if row < self.dimension-1 and self.grid_values[row+1][column] == 'M':
                    self.grid_values[row][column] = self.grid_values[row][column] + 1

                if column < self.dimension-1 and self.grid_values[row][column+1] == 'M':
                    self.grid_values[row][column] = self.grid_values[row][column] + 1

                if row > 0 and column > 0 and self.grid_values[row-1][column-1] == 'M':
                    self.grid_values[row][column] = self.grid_values[row][column] + 1

                if (row < self.dimension-1 and column > 0
                        and self.grid_values[row+1][column-1] == 'M'):
                    self.grid_values[row][column] = self.grid_values[row][column] + 1

                if (row < self.dimension-1 and column < self.dimension-1
                        and self.grid_values[row+1][column+1] == 'M'):
                    self.grid_values[row][column] = self.grid_values[row][column] + 1

                if (row > 0 and column < self.dimension-1
                        and self.grid_values[row-1][column+1] == 'M'):
                    self.grid_values[row][column] = self.grid_values[row][column] + 1


def print_board(self):
    """[prints board for gameview. ]
    """
    for row in self.player_view:
        for square in row:
            print(square, end=" ")
        print()
