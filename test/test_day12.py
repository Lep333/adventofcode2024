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

    def test_part_two2(self):
        input = "EEEEE\n\
EXXXX\n\
EEEEE\n\
EXXXX\n\
EEEEE"
        input = input.split()
        result = day12.part_two(input)
        self.assertEqual(result, 236)

    def test_part_two3(self):
        input = "AAAAAA\n\
AAABBA\n\
AAABBA\n\
ABBAAA\n\
ABBAAA\n\
AAAAAA"
        input = input.split()
        result = day12.part_two(input)
        self.assertEqual(result, 368)

    def test_part_two4(self):
        input = "RRRRIICCFF\n\
RRRRIICCCF\n\
VVRRRCCFFF\n\
VVRCCCJFFF\n\
VVVVCJJCFE\n\
VVIVCCJJEE\n\
VVIIICJJEE\n\
MIIIIIJJEE\n\
MIIISIJEEE\n\
MMMISSJEEE"
        input = input.split()
        result = day12.part_two(input)
        self.assertEqual(result, 1206)

    def test_part_two5(self):
        input = "OOOOO\n\
OXOXO\n\
OOOOO\n\
OXXXO\n\
AOOOO"
        input = input.split()
        result = day12.part_two(input)
        self.assertEqual(result, 19*18+4+3*4+2*4)

    def test_part_two6(self):
        input = "WWWWWW\n\
WWWWWW\n\
WWWMWW\n\
WWMMWW"
        input = input.split()
        result = day12.part_two(input)
        self.assertEqual(result, 21*10 + 3*6)

    def test_part_two7(self):
        input = "OOOOO\n\
OXXXO\n\
OXXXO\n\
OXXXO\n\
OOOOO"
        input = input.split()
        result = day12.part_two(input)
        self.assertEqual(result, 16*8+9*4)

    def test_part_two8(self):
        input = "AABBB\n\
BBAAA\n\
BAAAA"
        input = input.split()
        result = day12.part_two(input)
        self.assertEqual(result, 80)