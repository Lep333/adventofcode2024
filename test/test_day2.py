import unittest
from src import day2

class TestDay2(unittest.TestCase):
    def test_part_one(self):
        input = "7 6 4 2 1\n\
1 2 7 8 9\n\
9 7 6 2 1\n\
1 3 2 4 5\n\
8 6 4 4 1\n\
1 3 6 7 9"
        input = day2.parse(input)
        result = day2.part_one(input)
        self.assertEqual(result, 2)

    def test_part_two(self):
        input = "7 6 4 2 1\n\
1 2 7 8 9\n\
9 7 6 2 1\n\
1 3 2 4 5\n\
8 6 4 4 1\n\
1 3 6 7 9"
        input = day2.parse(input)
        result = day2.part_two(input)
        self.assertEqual(result, 4)