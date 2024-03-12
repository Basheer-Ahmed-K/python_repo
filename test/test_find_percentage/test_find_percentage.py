import unittest

from src.find_percentage.util import findPercentage


class TestFindPercentage(unittest.TestCase):
    def test_one(self):
        result = findPercentage()
        self.assertEquals(result, 50.00)

    # def test_two(self):
    #     arr = [25, 26.5, 28]
    #     self.assertEquals(findPercentage(arr), 26.50)

    # def test_three(self):
    #     arr = [52, 56, 60]
    #     self.assertEquals(findPercentage(arr), 56.00)

    # def test_three(self):
    #     arr = [49, 46, 43]
    #     self.assertEquals(findPercentage(arr), 46.00)


if __name__ == '__main__':
    unittest.main()

# 2
# basheer 10 20 30
# ahmed 40 50 60
# ahmed

# output = 50.00
