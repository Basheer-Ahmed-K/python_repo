import unittest
from src.calendar_module.util import printDay


class CalendarModule(unittest.TestCase):

    def test_one(self):
        self.assertEquals(printDay("08", "05", "2015"), "WEDNESDAY")

    def test_two(self):
        self.assertEquals(printDay("02", '29', '2004'),"SUNDAY")

    def test_three(self):
        self.assertEquals(printDay("08","05","2999"), "MONDAY")
