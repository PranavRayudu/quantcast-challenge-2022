import subprocess
import sys
import unittest


class TestFormatting(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """This is run once before all tests"""
        print("Python version: " + sys.version + "\n")

    def setUp(self):
        """This is run before each individual test"""
        self.maxDiff = None

    def test_1(self):
        """integration test 1"""
        expected, output = run_test_case('tests/test_cases/test1.in -d 2018-12-09',
                                         'tests/test_cases/test1.out')
        self.assertEqual(output, expected)

    def test_2(self):
        """integration test 2"""
        expected, output = run_test_case('tests/test_cases/test2.in -d 2020-1-1',
                                         'tests/test_cases/test2.out')
        self.assertEqual(output, expected)


def run_test_case(args, output_file):
    # start the subprocess
    proc = subprocess.Popen('python -u most_active_cookie.py {}'.format(args).split(),
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT,
                            universal_newlines=True)

    # read the submitted output
    output = proc.stdout.read()
    proc.stdout.close()
    proc.terminate()

    # get the expected output
    expected_file = open(output_file, 'r')
    expected = expected_file.read()
    expected_file.close()

    output = output.strip()
    expected = expected.strip()

    # return the expected and actual output
    return expected, output


if __name__ == "__main__":
    unittest.main()
