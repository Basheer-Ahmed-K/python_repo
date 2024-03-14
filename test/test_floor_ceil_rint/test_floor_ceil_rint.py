import unittest

import numpy

from src.floor_ceil_Rint.util import FloorCeilRint


class FloorCeilrint(unittest.TestCase):
    def test_one(self):
        arr = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9]
        expected_output = numpy.array([[1., 2., 3., 4., 5., 6., 7., 8., 9.], [2., 3., 4., 5., 6., 7., 8., 9., 10.],
                                       [1., 3., 4., 4., 6., 7., 8., 9., 10.]])
        self.assertEquals(FloorCeilRint(arr), expected_output)
