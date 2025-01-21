import unittest
from src import day21

class TestDay21(unittest.TestCase):
    def test_part_one(self):
        input = ["029A", "980A", "179A", "456A", "379A"]
        result = day21.part_one(input)
        self.assertEqual(result, 126384)