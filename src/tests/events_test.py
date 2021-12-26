import unittest
import events
from board import Board

class TestEvents(unittest.TestCase):
    def setUp(self):
        self.gameboard = Board("Easy")
        m = 'M'
        self.gameboard.grid_values= [
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

        self.assertEqual(self.gameboard.grid_values, expected_values)

    def test_opening_numbered_square_shows_value_in_player_view(self):
        events.open_square(self.gameboard, 0 , 0)

        shown_value = self.gameboard.player_view[0][0]

        self.assertEqual(shown_value, 1)

    def test_opening_nonmine_square_game_continues(self):
        return_value = events.open_square(self.gameboard, 9, 1)

        self.assertEqual(return_value, (False, 0))

    def test_opening_mine_square_ends_game_as_lost(self):
        return_value = events.open_square(self.gameboard, 0, 1)

        self.assertEqual(return_value, (True, 0))

    def test_square_can_be_flagged(self):
        events.process_flags(self.gameboard, 5, 0)

        flag = self.gameboard.player_view[5][0]

        self.assertEqual(flag, "F")

    def test_square_can_be_unflagged(self):
        events.process_flags(self.gameboard,4,5)

        events.process_flags(self.gameboard,4,5)

        square_value = self.gameboard.player_view[4][5]

        self.assertEqual(square_value, "*")

    def test_flagged_square_cant_be_opened(self):
        events.process_flags(self.gameboard,7,2)

        return_value = events.open_square(self.gameboard, 7, 2)

        self.assertEqual(return_value, (False,0))

    def test_open_square_cant_be_flagged(self):
        events.open_square(self.gameboard, 0, 0)

        events.process_flags(self.gameboard, 0, 0)

        self.assertEqual(self.gameboard.player_view[0][0], 1)

    def test_opening_non_mine_squares_ends_game_as_win(self):

        for row in range(self.gameboard.dimension-1):
            for column in range(self.gameboard.dimension-1):
                if row == 0 and column == 0:
                    continue
                if self.gameboard.grid_values[row][column] == 'M':
                    continue
              
                events.open_square(self.gameboard, row+1, column+1)

        open_last_square = events.open_square(self.gameboard, 0, 0)
        self.assertEqual(open_last_square, (True,1))
