"""this class generates two boards for the game:
    one with actual values and one that is shown to the player"""

import random


class Board:

    def __init__(self, level: str, grid_width: int):
        self.level = level
        self.flags = 0
        self.mines = 0
        self.dimension = grid_width
        self.grid_values = []
        self.player_view = []
        self.__create_hidden_board(self.grid_values)
        self.__create_player_board(self.player_view)

    def __create_hidden_board(self, grid_values):
        self.grid_values = [
            [0 for y in range(self.dimension)] for x in range(self.dimension)]
        add_mines(self, self.level, self.grid_values)
        add_numbers_to_squares(self, self.grid_values)

    def __create_player_board(self, player_view):
        self.player_view = [
            ['*' for y in range(self.dimension)] for x in range(self.dimension)]


def add_mines(self, level: str, grid_values):
    if self.level == "Easy":
        self.mines = 10
        self.flags = 10

    if self.level == "Medium":
        self.mines = 40
        self.flags = 40

    if self.level == "Hard":
        self.mines = 99
        self.flags = 99

    count = 0

    while count < self.mines:
        num = random.randint(0, (self.dimension * self.dimension) - 1)

        row = num // self.dimension
        column = num % self.dimension

        if grid_values[row][column] != 'M':
            count = count+1
            grid_values[row][column] = 'M'


def add_numbers_to_squares(self, grid_values):
    for row in range(self.dimension):
        for column in range(self.dimension):

            if grid_values[row][column] == 'M':
                continue

            if row > 0 and grid_values[row-1][column] == 'M':
                grid_values[row][column] = grid_values[row][column] + 1

            if column > 0 and grid_values[row][column-1] == 'M':
                grid_values[row][column] = grid_values[row][column] + 1

            if row < self.dimension-1 and grid_values[row+1][column] == 'M':
                grid_values[row][column] = grid_values[row][column] + 1

            if column < self.dimension-1 and grid_values[row][column+1] == 'M':
                grid_values[row][column] = grid_values[row][column] + 1

            if row > 0 and column > 0 and grid_values[row-1][column-1] == 'M':
                grid_values[row][column] = grid_values[row][column] + 1

            if row < self.dimension-1 and column > 0 and grid_values[row+1][column-1] == 'M':
                grid_values[row][column] = grid_values[row][column] + 1

            if (row < self.dimension-1 and column < self.dimension-1
                    and grid_values[row+1][column+1] == 'M'):
                grid_values[row][column] = grid_values[row][column] + 1

            if row > 0 and column < self.dimension-1 and grid_values[row-1][column+1] == 'M':
                grid_values[row][column] = grid_values[row][column] + 1

def print_board(self):
    for row in self.player_view:
        for square in row:
            print(square, end = " ")
        print()