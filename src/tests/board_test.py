import unittest
from board import Board


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.mine_squares = [(0, 2), (1, 3), (3, 1), (3, 3), (4, 2)]
        self.board = Board(self.mine_squares, 5)

    def test_board_generates_mines_and_numbers_correctly(self):
        m = 'M'
        expected_values = [
            [0, 1, m, 2, 1],
            [0, 1, 2, m, 1],
            [1, 1, 3, 2, 2],
            [1, m, 3, m, 1],
            [1, 2, m, 2, 1]
        ]

        self.assertEqual(self.board.grid_values, expected_values)

    def test_player_view_board_is_generated_correctly(self):
        c = '*'

        expected_values = [
            [c, c, c, c, c],
            [c, c, c, c, c],
            [c, c, c, c, c],
            [c, c, c, c, c],
            [c, c, c, c, c]
        ]

        self.assertEqual(self.board.player_view, expected_values)

    def test_correct_amount_of_flags(self):
        flag_count = len(self.mine_squares)

        self.assertEqual(self.board.flags, flag_count)

    def test_correct_amount_of_mines(self):
        mine_count = len(self.mine_squares)

        self.assertEqual(self.board.mines, mine_count)
