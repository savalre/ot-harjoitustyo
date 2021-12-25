import os
import csv
import pygame
from board import Board

class Ui():
    def __init__(self,level:str):
        self.gameboard = Board(level)
        pygame.init()
        self.empty = pygame.image.load(os.path.join('src/pictures', 'empty.png'))
        self.mine = pygame.image.load(os.path.join('src/pictures', 'mine.png'))
        self.flag = pygame.image.load(os.path.join('src/pictures', 'flag.png'))
        self.width = 30
        self.height = 30
        self.left = 1
        self.right = 3
        self.black = 0,0,0
        self.mouse_click = ""
        self.square = -1
        self.grid_value = 0
        self.size = self.__get_screen_size(level)
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Minesweeper")

    def __get_screen_size(self,level):
        size_value = 0

        dirname = os.path.dirname(__file__)
        file_path = os.path.join(dirname, "specs.csv")

        with open(file_path) as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == level:
                    size_value = int(row[3])
        screen_size = (size_value, size_value)
        return screen_size

    def game_loop(self):

        end = False
        pygame.display.update()

        clock = pygame.time.Clock()
        while not end:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    end = True
                
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == self.right:
                    self.mouse_click = 'right'
                    pos = pygame.mouse.get_pos()
                    row = pos[0] // self.width
                    column = pos[1] // self.height
                    grid_value = self.gameboard.grid_values[row][column]
                    self.gameboard.player_view[row][column] = grid_value

                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == self.left:
                    self.mouse_click = 'left'
                    pos = pygame.mouse.get_pos()
                    row = pos[0] // 30
                    column = pos[1] // 30
                    grid_value = self.gameboard.grid_values[row][column]
                    self.gameboard.player_view[row][column] = grid_value

            self.screen.fill(self.black)

            for x in range(len(self.gameboard.player_view)):
                for y in range(len(self.gameboard.player_view)):
                    square = self.gameboard.player_view[x][y]

                    if self.mouse_click == 'right':
                        self.screen.blit(self.flag, (x*30,y*30))

                    if square == 'M':
                        self.screen.blit(self.mine, (x*30, y*30))

                    if square == '*':
                        self.screen.blit(self.empty, (x*30, y*30))

                    elif square != 'M':
                        command = os.path.join(
                            'src/pictures', ('pict' + str(square) + '.png'))
                        image = pygame.image.load(command)
                        image = image.convert()
                        self.screen.blit(image, (x*30, y*30))

            clock.tick(60)

            pygame.display.flip()

        pygame.quit()
