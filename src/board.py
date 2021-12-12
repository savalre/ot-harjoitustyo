

class Board:

    """this class generates two boards for the game:
    one with actual values and one that is shown to the player"""


    def __init__(self, mine_squares: list, grid_width: int):
        self.flags = len(mine_squares)
        self.mines = len(mine_squares)
        self.dimension = grid_width
        self.grid_values = []
        self.player_view = []
        self._create_hidden_board(mine_squares)
        self._create_player_board()

    def _create_hidden_board(self, mine_squares):
        self.grid_values = [
            [0 for y in range(self.dimension)] for x in range(self.dimension)]
        self._add_mines(mine_squares)
        self._add_numbers_to_squares()

    def _create_player_board(self):
        self.player_view = [
            ['*' for y in range(self.dimension)] for x in range(self.dimension)]


    def _add_mines(self, mine_squares):

        for mine in mine_squares:
            row = mine[0]
            column = mine[1]

            self.grid_values[row][column] = 'M'

    def _add_numbers_to_squares(self):
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

                if row < self.dimension-1 and column > 0 and self.grid_values[row+1][column-1] == 'M':
                    self.grid_values[row][column] = self.grid_values[row][column] + 1

                if (row < self.dimension-1 and column < self.dimension-1
                        and self.grid_values[row+1][column+1] == 'M'):
                    self.grid_values[row][column] = self.grid_values[row][column] + 1

                if row > 0 and column < self.dimension-1 and self.grid_values[row-1][column+1] == 'M':
                    self.grid_values[row][column] = self.grid_values[row][column] + 1

def print_board(self):
    for row in self.player_view:
        for square in row:
            print(square, end = " ")
        print()