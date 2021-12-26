"""[This file includes the board generating methods]"""

import os
import random
import csv


class Board:

    """This class generates two boards for the game:
        one with actual values and one that is shown to the player
    """

    def __init__(self, level: str):
        """[Constructor for Board class, creates new gameboard]

        Args:
            level (string): [represents the chosen level of the game]
        """
        self.grid_values = []
        self.player_view = []
        self.mine_squares = []
        self.dimension = 0
        self.create_mine_squares(level)
        self.flags = len(self.mine_squares)
        self.mines = len(self.mine_squares)
        self.create_hidden_board(self.mine_squares)
        self.create_player_board()

    def create_mine_squares(self, level):
        """[method generates the square coordinates where
            in the gameboard the mines will be assigned to]

        Args:
            mines ([integer]): [number of mines needed]
            dimension ([integer]): [width of gameboard]

        Returns:
            [list]: [contains tuples of (row,column) values that the mines will be assigned to]
        """

        mine_count = 0

        dirname = os.path.dirname(__file__)
        file_path = os.path.join(dirname,"data", "specs.csv")

        with open(file_path, encoding = 'UTF_8') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == level:
                    self.dimension = int(row[1])
                    mine_count = int(row[2])
                    break

        count = 0

        while count < mine_count:
            num = random.randint(0, (self.dimension * self.dimension) - 1)

            row = num // self.dimension
            column = num % self.dimension

            if (row, column) not in self.mine_squares:
                count = count+1
                self.mine_squares.append((row, column))

        return self.mine_squares

    def add_mines(self, mine_squares):
        """[adds mines to hidden board]

        Args:
            mine_squares ([list]): [list which has coordinates where to assign mines]
        """

        for mine in mine_squares:
            row = mine[0]
            column = mine[1]

            self.grid_values[row][column] = 'M'

    def create_hidden_board(self, mine_squares):
        """[creates the hidden gameboard with mine locations and numbers]

            Args:
                mine_squares ([list]): [list which has coordinates where to assign mines]
            """
        self.grid_values = [[0 for y in range(self.dimension)]
                            for x in range(self.dimension)]
        self.add_mines(mine_squares)
        self.add_numbers_to_squares()

    def add_numbers_to_squares(self):
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

    def create_player_board(self):
        """[creates the board that is visible to the player,
        and is updated with values from opened squares throughout the game]
        """
        self.player_view = [
            ['*' for y in range(self.dimension)] for x in range(self.dimension)]
