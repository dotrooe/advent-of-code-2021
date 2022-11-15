import unittest

from day01.sonar_sweep import measure_increases
from utils.file_utils import read_num_list


class SonarSweepTestCase(unittest.TestCase):

    def test_should_pass_advent_of_code_part_one_example(self):
        arr = read_num_list("example-input.txt")
        self.assertEqual(7, measure_increases(arr))


if __name__ == '__main__':
    unittest.main()
