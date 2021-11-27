from board import *

def select_level():
    return_value = ""

    level = int(input("Choose level by typing number:\n1 Easy\n2 Medium\n3 Hard\n"))
    
    if(level == 1):
        return_value = "Easy"
    
    if(level == 2):
        return_value = "Medium"

    if(level == 3):
        return_value = "Hard"

    return return_value

def grid_width(level):
    grid = 0

    if(level == "Easy"):
        grid = 10
    
    if(level == "Medium"):
        grid = 16

    if(level == "Hard"):
        grid = 30

    return grid


__name__ == '__main__'

print("Welcome to Minesweeper!\nPlease choose what you want to do!\n")
print(" ")
command = int(input("Press 1 if you want to play, press 2 if you want to quit "))

if command == 2:
    exit()

if command == 1:
    level = select_level()
    grid_width = grid_width(level)
    gameboard = Board(level, grid_width)

end = False

while not end:
    print(" ")
    for x in gameboard.grid_values:
        for y in x:
            print(y, end = " ")
        print(" ")

    command = input("You can't play the game yet, but this is how the game generates the values of gameboard. Exit by typing e\n")
    
    if command == "e":
        exit()