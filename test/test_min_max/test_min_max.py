import unittest
from src.min_max.driver import MinMax


class TestMinMax(unittest.TestCase):
    def test_one(self):
        self.assertEquals(MinMax(), 3)

    '''4 2
2 5
3 7
1 3
4 0'''

    def test_two(self):
        self.assertEquals(MinMax(), 7)
    '''4 2
2 5
8 7
1 4
4 0'''

    def test_three(self):
        self.assertEquals(MinMax(), 2)
    '''3 2
2 5
1 4
4 0'''
