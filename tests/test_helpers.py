import sys
import unittest
from datetime import datetime, timezone

import most_active_cookie


class TestHelpers(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """This is run once before all tests"""
        print("Python version: " + sys.version + "\n")

    def setUp(self):
        """This is run before each individual test"""
        pass

    def test_process(self):
        """test process_logfile() method"""
        logfile = open('tests/test_cases/test1.in', 'r')
        output = most_active_cookie.process_logfile(logfile)
        logfile.close()
        expected = [(datetime(year=2018, month=12, day=9, hour=14, minute=19, tzinfo=timezone.utc), 'AtY0laUfhglK3lC7'),
                    (datetime(2018, 12, 9, 10, 13, tzinfo=timezone.utc), 'SAZuXPGUrfbcn5UA'),
                    (datetime(2018, 12, 9, 7, 25, tzinfo=timezone.utc), '5UAVanZf6UtGyKVS'),
                    (datetime(2018, 12, 9, 6, 19, tzinfo=timezone.utc), 'AtY0laUfhglK3lC7'),
                    (datetime(2018, 12, 8, 22, 3, tzinfo=timezone.utc), 'SAZuXPGUrfbcn5UA'),
                    (datetime(2018, 12, 8, 21, 30, tzinfo=timezone.utc), '4sMM2LxV07bPJzwf'),
                    (datetime(2018, 12, 8, 9, 30, tzinfo=timezone.utc), 'fbcn5UAVanZf6UtG'),
                    (datetime(2018, 12, 7, 23, 30, tzinfo=timezone.utc), '4sMM2LxV07bPJzwf')]

        self.assertListEqual(output, expected)

    def test_cookie_freq(self):
        """test get_cookie_freq() method"""
        logs = [(datetime(2010, 12, 9), 'B'),
                (datetime(2010, 12, 9), 'B'),
                (datetime(2010, 12, 9), 'B'),
                (datetime(2010, 12, 9), 'B'),
                (datetime(2010, 12, 9), 'B'),
                (datetime(2010, 12, 9), 'B')]
        output = most_active_cookie.get_cookie_freq(logs)
        expected = {
            'B': 6,
        }
        self.assertDictEqual(output, expected)

    def test_cookie_freq_2(self):
        """test get_cookie_freq() method"""
        logs = [(datetime(2010, 12, 9), 'A'),
                (datetime(2010, 12, 9), 'B'),
                (datetime(2010, 12, 9), 'C'),
                (datetime(2010, 12, 9), 'D'),
                (datetime(2010, 12, 9), 'E'),
                (datetime(2010, 12, 9), 'F')]
        output = most_active_cookie.get_cookie_freq(logs)
        expected = {
            'A': 1,
            'B': 1,
            'C': 1,
            'D': 1,
            'E': 1,
            'F': 1,
        }
        self.assertDictEqual(output, expected)

    def test_common_cookie(self):
        """test get_most_common_cookie() method"""
        cookie_freq = {
            'A': 2,
            'B': 3,
            'C': 4,
            'E': 4,
            'F': 4,
        }

        output = most_active_cookie.get_most_common_cookie(cookie_freq)
        expected = ['C', 'E', 'F']
        self.assertCountEqual(output, expected)


if __name__ == "__main__":
    unittest.main()
