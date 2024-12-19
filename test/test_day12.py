import unittest
from src import day12

class TestDay12(unittest.TestCase):
    def test_part_one(self):
        input = "AAAA\nBBCD\nBBCC\nEEEC"
        input = input.split()
        result = day12.part_one(input)
        self.assertEqual(result, 140)

    def test_part_one_complex(self):
        input = "RRRRIICCFF\nRRRRIICCCF\nVVRRRCCFFF\nVVRCCCJFFF\nVVVVCJJCFE\nVVIVCCJJEE\nVVIIICJJEE\nMIIIIIJJEE\nMIIISIJEEE\nMMMISSJEEE"
        input = input.split()
        result = day12.part_one(input)
        self.assertEqual(result, 1930)

    def test_part_two(self):
        input = "AAAA\nBBCD\nBBCC\nEEEC"
        input = input.split()
        result = day12.part_two(input)
        self.assertEqual(result, 80)