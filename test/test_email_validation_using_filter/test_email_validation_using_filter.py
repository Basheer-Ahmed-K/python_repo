import unittest

from src.validating_email_address_with_filter.util import ValidEmail


class TestEmailValidator(unittest.TestCase):
    def test_one(self):
        expected_output = ['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']
        self.assertEqual(ValidEmail(),expected_output)
        '''3
lara@hackerrank.com
brian-23@hackerrank.com
britts_54@hackerrank.com'''