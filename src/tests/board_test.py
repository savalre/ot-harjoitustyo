import unittest
from board import Board

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board("Easy",10)
    
    def test_board_generated(self):
        self.assertNotEqual(self.board, None)
    