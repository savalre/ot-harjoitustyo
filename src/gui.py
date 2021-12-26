"""[summary]

    Returns:
        [type]: [description]
    """
import os
import pygame
from board import Board
from events import open_square, process_flags


class GUI():

    """[summary]
    """

    def __init__(self, level: str):
        """[summary]

        Args:
            level (str): [description]
        """
        self.gameboard = Board(level)
        pygame.init()
        self.empty = pygame.image.load(os.path.join('src/pictures', 'empty.png'))
        self.mine = pygame.image.load(os.path.join('src/pictures', 'mine.png'))
        self.flag = pygame.image.load(os.path.join('src/pictures', 'flag.png'))
        self.not_mine = pygame.image.load(os.path.join('src/pictures', 'was_not.png'))
        # lista jossa numerot 1 - 8 ja niiden polut ja lue ne siitä, silloin ei tarvitse ladata uudestaan kuvia
        self.side = 30
        self.if_solved = (False, 1)
        self.footer_pos = 0
        self.text_center = 0
        self.screen = pygame.display.set_mode(self.__get_screen_size())
        pygame.display.set_caption("Minesweeper")

    def __get_screen_size(self):
        """[summary]

        Args:
            level ([type]): [description]

        Returns:
            [type]: [description]
        """
        size_value = self.side * self.gameboard.dimension
        screen_size = (size_value, size_value+40)
        self.footer_pos = size_value+10
        self.text_center = size_value//2
        return screen_size

    def print_gameboard(self):
        """[summary]
        """
        for row in range(len(self.gameboard.player_view)):
            for column in range(len(self.gameboard.player_view)):

                square = self.gameboard.player_view[row][column]
                if square == 'M':
                    self.screen.blit(
                        self.mine, (row*self.side, column*self.side))

                if square == '*':
                    self.screen.blit(
                        self.empty, (row*self.side, column*self.side))

                elif square != 'M':
                    if square == 'X':
                        self.screen.blit(
                        self.not_mine, (row*self.side, column*self.side))
                    elif square == 'F':
                        self.screen.blit(
                        self.flag, (row*self.side, column*self.side))
                    else:
                        command = os.path.join('src/pictures', ('pict' + str(square) + '.png'))
                        image = pygame.image.load(command)
                        image = image.convert()
                        self.screen.blit(image, (row*self.side, column*self.side))

        font = pygame.font.Font(None, 30)
        message = ""

        if self.if_solved == (True,0):
            message = "YOU HIT A MINE! GAME OVER!"
        elif self.if_solved == (True,1):
            message = "WOHOO, YOU WIN!"
        else:
            message = f"FLAGS REMANING: {self.gameboard.flags}"

        text = font.render(message, True, (225,225,225))
        self.screen.blit(text,(self.text_center//len(message),self.footer_pos)) #x,y


    def game_loop(self):
        """[summary]
        """
        end = False
        pygame.display.update()
        clock = pygame.time.Clock()

        while not end:
            self.screen.fill((131, 139, 139))

            self.print_gameboard()

            pygame.display.flip()

            clock.tick(60)

            if self.if_solved == (True, 1):
                pygame.time.delay(2000)
                end = True

            if self.if_solved == (True, 0):
                pygame.time.delay(2000)
                end = True

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    end = True

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                    pos = pygame.mouse.get_pos()
                    row = pos[0] // self.side
                    column = pos[1] // self.side
                    if all(x < len(self.gameboard.player_view) for x in (row, column)):
                        process_flags(self.gameboard, row, column)
                        pygame.display.update()

                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    row = pos[0] // self.side
                    column = pos[1] // self.side
                    if all(x < len(self.gameboard.player_view) for x in (row, column)):
                        self.if_solved = open_square(self.gameboard, row, column)
        pygame.quit()
