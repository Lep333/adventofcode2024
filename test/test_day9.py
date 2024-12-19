import unittest
from src import day9

class Test_Day9(unittest.TestCase):
    def test_part_one(self):
        input = "2333133121414131402"
        result = day9.part_one(input)
        self.assertAlmostEqual(result, 1928)