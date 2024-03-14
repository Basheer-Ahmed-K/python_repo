import unittest
from src.string_mutation.util import *


class TestStringMutation(unittest.TestCase):
    def test_one(self):
        self.assertEquals(mutate_string("abracadabra", 5, 'k'), "abrackdabra")

    def test_two(self):
        s = "randomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomness"
        self.assertEquals(mutate_string(s,27, 'p'), "randomnessrandomnessrandomnpssrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomness")