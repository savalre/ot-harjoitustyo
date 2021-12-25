"""[summary]

    Returns:
        [type]: [description]
    """
import os
import csv
import pygame
from board import Board
from events import open_square, process_flags


class Ui():
    """[summary]
    """

    def __init__(self, level: str):
        """[summary]

        Args:
            level (str): [description]
        """
        self.gameboard = Board(level)
        pygame.init()
        self.empty = pygame.image.load(
            os.path.join('src/pictures', 'empty.png'))
        self.mine = pygame.image.load(os.path.join('src/pictures', 'mine.png'))
        self.flag = pygame.image.load(os.path.join('src/pictures', 'flag.png'))
        self.not_mine = pygame.image.load(
            os.path.join('src/pictures', 'was_not.png'))
        self.side = 30
        self.left = 1
        self.right = 3
        self.square = -1
        self.row = -1
        self.column = -1
        self.grid_value = -1
        self.if_solved = (False, 1)
        self.size = self.__get_screen_size(level)
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Minesweeper")

    def __get_screen_size(self, level):
        """[summary]

        Args:
            level ([type]): [description]

        Returns:
            [type]: [description]
        """
        size_value = 0

        dirname = os.path.dirname(__file__)
        file_path = os.path.join(dirname, "specs.csv")

        with open(file_path) as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == level:
                    size_value = int(row[3])
        screen_size = (size_value, size_value+50)
        return screen_size

    def game_loop(self):
        """[summary]
        """
        end = False
        pygame.display.update()
        clock = pygame.time.Clock()

        while not end:
            self.screen.fill((0,0,0))

            # tästä kans metodi, esim print board vaikka sit tänne luokkaan
            for x in range(len(self.gameboard.player_view)):
                for y in range(len(self.gameboard.player_view)):
                    square = self.gameboard.player_view[x][y]

                    if square == 'M':
                        self.screen.blit(self.mine, (x*self.side, y*self.side))

                    if square == '*':
                        self.screen.blit(self.empty, (x*self.side, y*self.side))

                    elif square != 'M':

                        if square == 'X':
                            self.screen.blit(
                                self.not_mine, (x*self.side, y*self.side))
                        elif square == 'F':
                            self.screen.blit(
                                self.flag, (x*self.side, y*self.side))
                        else:
                            command=os.path.join(
                                'src/pictures', ('pict' + str(square) + '.png'))
                            image=pygame.image.load(command)
                            image=image.convert()
                            self.screen.blit(image, (x*self.side, y*self.side))

            clock.tick(60)

            pygame.display.flip()

            if self.if_solved == (True, 1):
                pygame.time.delay(500)
                end=True

            if self.if_solved == (True, 0):
                pygame.time.delay(500)
                end=True

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    end=True

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == self.right:
                    pos=pygame.mouse.get_pos()
                    self.row=pos[0] // self.side
                    self.column=pos[1] // self.side
                    process_flags(self.gameboard, self.row, self.column)
                    pygame.display.update()

                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == self.left:
                    pos=pygame.mouse.get_pos()
                    self.row=pos[0] // self.side
                    self.column=pos[1] // self.side
                    self.if_solved=open_square(
                        self.gameboard, self.row, self.column)

        pygame.quit()
