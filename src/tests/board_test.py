import unittest
from board import Board


class TestBoard(unittest.TestCase):
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

    def test_board_has_mines_and_numbers_correctly(self):
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

    def test_player_view_board_is_generated_correctly(self):
        c = '*'

        expected_values = [
            [c, c, c, c, c, c, c, c, c, c],
            [c, c, c, c, c, c, c, c, c, c],
            [c, c, c, c, c, c, c, c, c, c],
            [c, c, c, c, c, c, c, c, c, c],
            [c, c, c, c, c, c, c, c, c, c],
            [c, c, c, c, c, c, c, c, c, c],
            [c, c, c, c, c, c, c, c, c, c],          
            [c, c, c, c, c, c, c, c, c, c],
            [c, c, c, c, c, c, c, c, c, c],
            [c, c, c, c, c, c, c, c, c, c]
        ]

        self.assertEqual(self.gameboard.player_view, expected_values)

    def test_correct_amount_of_flags(self):
        flag_count = len(self.gameboard.mine_squares)

        self.assertEqual(self.gameboard.flags, flag_count)

    def test_correct_amount_of_mines(self):
        mine_count = len(self.gameboard.mine_squares)

        self.assertEqual(self.gameboard.mines, mine_count)

    def test_grid_dimension_read_right_from_file(self):
        self.assertEqual(self.gameboard.dimension,10)