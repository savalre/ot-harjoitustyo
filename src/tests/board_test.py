import unittest
from board import Board

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board(10, "Easy")
    
    def board_generated(self):
        self.assertNotEqual(self.board, None)