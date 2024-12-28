import unittest
from src import day6

class TestDay6(unittest.TestCase):
    def test_part_one(self):
        input = "....#.....\n\
.........#\n\
..........\n\
..#.......\n\
.......#..\n\
..........\n\
.#..^.....\n\
........#.\n\
#.........\n\
......#..."
        result = day6.part_one(input)
        self.assertEqual(result, 41)
    
    def test_part_two(self):
        input = "....#.....\n\
.........#\n\
..........\n\
..#.......\n\
.......#..\n\
..........\n\
.#..^.....\n\
........#.\n\
#.........\n\
......#..."
        result = day6.part_two(input)
        self.assertEqual(result, 6)