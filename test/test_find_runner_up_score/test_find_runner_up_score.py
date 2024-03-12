import unittest
from src.find_runner_up_score.util import runnerUp


class TestFindRunnerUpScore(unittest.TestCase):
    def test_one(self):
        arr = [2, 3, 6, 6, 5]
        self.assertEquals(runnerUp(arr), 5)

    def test_two(self):
        arr = [57, 57, -57, 57]
        self.assertEquals(runnerUp(arr), -57)

    def test_three(self):
        arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 6]
        self.assertEquals(runnerUp(arr), 5)


if __name__ == '__main__':
    unittest.main()
