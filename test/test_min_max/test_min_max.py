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
