import unittest

from src.piling_up.util import pillingUp


class TestPillingUp(unittest.TestCase):
    def test_one(self):
        self.assertEqual(pillingUp(),'''Yes
No
''')