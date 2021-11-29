#this class generates two boards for the game: 
#one with actual values and one that is shown to the player
import random
from array import *

class Board:

    def __init__(self, level: str, grid_width: int):
        self.level = level
        self.n = grid_width
        self.grid_values = []
        self.player_view = []
        self.__create_hidden_board(self.grid_values)
        self.__create_player_board(self.player_view)
    

    def __create_hidden_board(self, grid_values):
        self.grid_values = [[0 for y in range(self.n)] for x in range(self.n)]
        add_mines(self, self.level, self.grid_values)
        add_numbers_to_squares(self, self.grid_values)

    def __create_player_board(self, player_view):
        self.player_view = [['*' for y in range(self.n)] for x in range(self.n)]
    

        
def add_mines(self, level:str, grid_values):
    if(self.level == "Easy"):
        mines = 10

    if(self.level == "Medium"):
        mines = 40
    
    if(self.level == "Hard"):
        mines = 99
    
    count = 0

    while count < mines:
        num = random.randint(0, (self.n * self.n) - 1)

        row = num // self.n
        column = num % self.n

        if grid_values[row][column] != 'M':
            count = count+1
            grid_values[row][column] = 'M'


def add_numbers_to_squares(self, grid_values):
    for x in range(self.n):
        for y in range(self.n):

            if grid_values[x][y] == 'M':
                continue

            if x > 0 and grid_values[x-1][y] == 'M':
                grid_values[x][y] = grid_values[x][y] + 1

            if y > 0 and grid_values[x][y-1] == 'M':
                grid_values[x][y] = grid_values[x][y] + 1
            
            if x < self.n-1 and grid_values[x+1][y] == 'M':
                grid_values[x][y] = grid_values[x][y] + 1
            
            if y < self.n-1 and grid_values[x][y+1] == 'M':
                grid_values[x][y] = grid_values[x][y] + 1
            
            if x > 0 and y > 0 and grid_values[x-1][y-1] == 'M':
                grid_values[x][y] = grid_values[x][y] + 1
            
            if x < self.n-1 and y > 0 and grid_values[x+1][y-1] == 'M':
                grid_values[x][y] = grid_values[x][y] + 1
            
            if x < self.n-1 and y < self.n-1 and grid_values[x+1][y+1] == 'M':
                grid_values[x][y] = grid_values[x][y] + 1

            if x > 0 and y < self.n-1 and grid_values[x-1][y+1] == 'M':
                grid_values[x][y] = grid_values[x][y] + 1

def print_board(self):
    for x in self.player_view:
        for y in x:
            print(y, end = " ")
        print()
