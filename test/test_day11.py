import unittest
from src import day11

class TestDay11(unittest.TestCase):
    def test_part_one(self):
        input = "125 17"
        input = input.split()
        result = day11.part_one(input)
        self.assertEqual(result, 55312)