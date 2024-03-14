import unittest

from src.mean_var_std.util import MeanVarStd


class TestMeanVarStd(unittest.TestCase):
    def test_one(self):
        self.assertEqual(MeanVarStd(), "[1.5 3.5] [1. 1.] 1.11803398875")
        '''2 2
1 2
3 4'''

    def test_two(self):
        self.assertEqual(MeanVarStd(),"[1.5 3. ] [1.   0.25] 0.82915619759")
        '''2 2
1 2
3 3'''

    def test_three(self):
        self.assertEqual(MeanVarStd(), "[1. 1. 1.] [0. 0. 0.] 0.0")
        '''3 3
1 1 1
1 1 1
1 1 1'''
