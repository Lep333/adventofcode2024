import unittest
from src import day16

class TestDay16(unittest.TestCase):
    def test_part_one(self):
        input = "###############\n\
#.......#....E#\n\
#.#.###.#.###.#\n\
#.....#.#...#.#\n\
#.###.#####.#.#\n\
#.#.#.......#.#\n\
#.#.#####.###.#\n\
#...........#.#\n\
###.#.#####.#.#\n\
#...#.....#.#.#\n\
#.#.#.###.#.#.#\n\
#.....#...#.#.#\n\
#.###.#.#.#.#.#\n\
#S..#.....#...#\n\
###############"
        input = input.split()
        result = day16.part_one(input)
        self.assertEqual(result, 7036)

    def test_part_two(self):
        input = "###############\n\
#.......#....E#\n\
#.#.###.#.###.#\n\
#.....#.#...#.#\n\
#.###.#####.#.#\n\
#.#.#.......#.#\n\
#.#.#####.###.#\n\
#...........#.#\n\
###.#.#####.#.#\n\
#...#.....#.#.#\n\
#.#.#.###.#.#.#\n\
#.....#...#.#.#\n\
#.###.#.#.#.#.#\n\
#S..#.....#...#\n\
###############"
        input = input.split()
        result = day16.part_two(input)
        self.assertEqual(result, 45)