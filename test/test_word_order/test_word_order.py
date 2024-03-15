import unittest

from src.word_order.util import wordOrder


class TestWordOrder(unittest.TestCase):
    def test_one(self):
        self.assertEqual(wordOrder(),"['3', [2, 1, 1]]")
        '''4
bcdef
abcdefg
bcde
bcdef'''
