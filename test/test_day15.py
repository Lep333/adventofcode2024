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
        self.assertEqual(result, 207+306+105)
    
    def test_part_two_big(self):
        text = "##########\n\
#..O..O.O#\n\
#......O.#\n\
#.OO..O.O#\n\
#..O@..O.#\n\
#O#..O...#\n\
#O..O..O.#\n\
#.OO.O.OO#\n\
#....O...#\n\
##########\n\
\n\
<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^\n\
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v\n\
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<\n\
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^\n\
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><\n\
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^\n\
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^\n\
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>\n\
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>\n\
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"
        field, instructions = text.split("\n\n")
        field = field.split()
        result = day15.part_two((field, instructions))
        self.assertEqual(result, 9021)