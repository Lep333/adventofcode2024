import unittest
from src import day15

class TestDay15(unittest.TestCase):
    def test_part_one(self):
        text = "########\n\
#..O.O.#\n\
##@.O..#\n\
#...O..#\n\
#.#.O..#\n\
#...O..#\n\
#......#\n\
########\n\
\n\
<^^>>>vv<v>>v<<"
        field, instructions = text.split("\n\n")
        field = field.split()
        result = day15.part_one((field, instructions))
        self.assertEqual(result, 2028)

    def test_part_two(self):
        text = "#######\n\
#...#.#\n\
#.....#\n\
#..OO@#\n\
#..O..#\n\
#.....#\n\
#######\n\
\n\
<vv<<^^<<^^"
        field, instructions = text.split("\n\n")
        field = field.split()
        result = day15.part_two((field, instructions))
        self.assertEqual(result, 9021)