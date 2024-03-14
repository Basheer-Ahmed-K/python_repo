import unittest
from src.time_delta.util import time_delta


class TimeDelta(unittest.TestCase):

    def test_time_delta(self):
        test_cases = [
            {
                't1': 'Sun 10 May 2015 13:54:36 -0700',
                't2': 'Sun 10 May 2015 13:54:36 -0000',
                'expected_output': '25200'
            },
            {
                't1': 'Sat 02 May 2015 19:54:36 +0530',
                't2': 'Fri 01 May 2015 13:54:36 -0000',
                'expected_output': '88200'
            }
        ]

        for test_case in test_cases:
            output = time_delta(test_case['t1'], test_case['t2'])
            self.assertEqual(output, test_case['expected_output'])

    def test_time_delta2(self):
        test_cases = [
            {
                't1': 'Sat 24 Mar 2170 03:47:07 +0430',
                't2': 'Mon 30 Dec 2272 20:27:41 -1000',
                'expected_output': '3243222634'
            },
            {
                't1': 'Tue 03 Apr 2277 16:39:34 +0930',
                't2': 'Mon 06 Mar 2034 02:29:42 -0600',
                'expected_output': '7670759992'
            }
        ]
        for test_case in test_cases:
            output = time_delta(test_case['t1'], test_case['t2'])
            self.assertEquals(output, test_case['expected_output'])


'''2
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000'''
