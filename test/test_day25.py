import unittest
from src import day25

class TestDay25(unittest.TestCase):
    def test_part_one(self):
        input = "#####\n\
.####\n\
.####\n\
.####\n\
.#.#.\n\
.#...\n\
.....\n\
\n\
#####\n\
##.##\n\
.#.##\n\
...##\n\
...#.\n\
...#.\n\
.....\n\
\n\
.....\n\
#....\n\
#....\n\
#...#\n\
#.#.#\n\
#.###\n\
#####\n\
\n\
.....\n\
.....\n\
#.#..\n\
###..\n\
###.#\n\
###.#\n\
#####\n\
\n\
.....\n\
.....\n\
.....\n\
#....\n\
#.#..\n\
#.#.#\n\
#####"
        input = input.split("\n\n")
        input = [el.split("\n") for el in input]
        result = day25.part_one(input)
        self.assertEqual(result, 3)