import unittest
from src import day8

class TestDay8(unittest.TestCase):
    def test_part_one(self):
        input = "............\n\
........0...\n\
.....0......\n\
.......0....\n\
....0.......\n\
......A.....\n\
............\n\
............\n\
........A...\n\
.........A..\n\
............\n\
............"
        input = day8.parse(input)
        result = day8.part_one(input)
        self.assertEqual(result, 14)

    def test_part_two(self):
        input = "T.........\n\
...T......\n\
.T........\n\
..........\n\
..........\n\
..........\n\
..........\n\
..........\n\
..........\n\
.........."
        input = day8.parse(input)
        result = day8.part_two(input)
        self.assertEqual(result, 9)   