import unittest
import events
from board import Board

class TestEvents(unittest.TestCase):
    def setUp(self):
        self.events = Board("Easy",10)
    
    
