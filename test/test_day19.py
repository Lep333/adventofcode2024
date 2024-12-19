import unittest
from src import day19

class TestDay19(unittest.TestCase):
    def test_part_one(self):
        input = "r, wr, b, g, bwu, rb, gb, br\n\
\n\
brwrr\n\
bggr\n\
gbbr\n\
rrbgbr\n\
ubwu\n\
bwurrg\n\
brgr\n\
bbrgwb"
        input = day19.parse(input)
        result = day19.part_one(*input)
        self.assertEqual(result, 6)

    def test_part_two(self):
        input = "r, wr, b, g, bwu, rb, gb, br\n\
\n\
brwrr\n\
bggr\n\
gbbr\n\
rrbgbr\n\
ubwu\n\
bwurrg\n\
brgr\n\
bbrgwb"
        input = day19.parse(input)
        result = day19.part_two(*input)
        self.assertEqual(result, 16)