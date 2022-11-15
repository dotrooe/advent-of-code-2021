import unittest

from day01.sonar_sweep import measure_increases, measure_increases_of_triplets
from utils.file_utils import read_num_list


class SonarSweepTestCase(unittest.TestCase):

    def test_should_pass_advent_of_code_part_one_example(self):
        arr = read_num_list("example-input.txt")
        self.assertEqual(7, measure_increases(arr))

    def test_should_pass_advent_of_code_part_two_example(self):
        arr = read_num_list("example-input.txt")
        self.assertEqual(5, measure_increases_of_triplets(arr))


if __name__ == '__main__':
    unittest.main()
