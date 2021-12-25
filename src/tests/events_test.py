import unittest
import events
from board import Board


class TestEvents(unittest.TestCase):
    def setUp(self):
        self.mine_squares = [(0, 1), (9, 9), (3, 7), (3, 6), (4, 7),
                             (5, 0), (6, 4), (7, 9), (8, 8), (9, 3), ]

        self.board = Board(self.mine_squares, 10)

    def test_values_are_correct(self):
        m = 'M'
        expected_values = [
            [1, m, 1, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 2, 2, 1, 0],
            [0, 0, 0, 0, 0, 1, m, m, 2, 0],
            [1, 1, 0, 0, 0, 1, 3, m, 2, 0],
            [m, 1, 0, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 0, 1, m, 1, 0, 0, 1, 1],
            [0, 0, 0, 1, 1, 1, 0, 1, 2, m],
            [0, 0, 1, 1, 1, 0, 0, 1, m, 3],
            [0, 0, 1, m, 1, 0, 0, 1, 2, m]
        ]

        self.assertEqual(self.board.grid_values, expected_values)

    def test_opening_numbered_square_shows_value_in_player_view(self):
        events.open_square(self.board, "1 1")

        shown_value = self.board.player_view[0][0]

        self.assertEqual(shown_value, 1)

    def test_opening_nonmine_square_game_continues(self):
        return_value = events.open_square(self.board, "10 1")

        self.assertEqual(return_value, (False, 0))

    def test_opening_mine_square_ends_game_as_lost(self):
        return_value = events.open_square(self.board, "1 2")

        self.assertEqual(return_value, (True, 0))

    def test_square_can_be_flagged(self):
        events.open_square(self.board, "1 2 F")

        flag = self.board.player_view[0][1]

        self.assertEqual(flag, "F")

    def test_square_can_be_unflagged(self):
        events.open_square(self.board, "1 2 F")

        events.open_square(self.board, "1 2 F")

        square_value = self.board.player_view[0][1]

        self.assertEqual(square_value, "*")

    def test_open_square_cant_be_flagged(self):
        events.open_square(self.board, "1 1")

        events.open_square(self.board, "1 1 F")

        self.assertEqual(self.board.player_view[0][0], 1)

 """def print_board(self): tää on täällä kun voi tulostella sit näkymiä
 
        for row in self.player_view:
            for square in row:
                print(square, end=" ")
            print()


    def test_opening_zero_square_opens_neighbours(self):
            events.open_square(self.board, "10 7")""" 

    def test_opening_non_mine_squares_ends_game_as_win(self): 

            for row in range(self.board.dimension):
                for column in range(self.board.dimension):    
                    if row == 0 and column == 0:
                        continue
                    if self.board.grid_values[row][column] == 'M':
                        continue
                    
                    command = str(row+1) + " " + str(column+1)
                    events.open_square(self.board, command)

            open_last_square = events.open_square(self.board,"1 1")
            print(open_last_square)
            self.assertEqual(open_last_square, (True,1))
