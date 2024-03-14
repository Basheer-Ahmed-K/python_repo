import unittest
from src.lineara_algebra.driver import linearAlgebra


class TestLinearAlgebre(unittest.TestCase):
    def test_one(self):
        self.assertEquals(linearAlgebra(), 0.0)
        '''2
1.1 1.1
1.1 1.1'''

    def test_two(self):
        self.assertEquals(linearAlgebra(), 0.11)
        '''2
1.1 1.1
1.1 1.2'''

    def test_three(self):
        self.assertEquals(linearAlgebra(), 6.0)
        '''3
1 2 3
4 5 6
1 2 1'''
