import unittest
from src import day18

class TestDay18(unittest.TestCase):
    def test_part_one(self):
        input = "5,4\n\
4,2\n\
4,5\n\
3,0\n\
2,1\n\
6,3\n\
2,4\n\
1,5\n\
0,6\n\
3,3\n\
2,6\n\
5,1\n\
1,2\n\
5,5\n\
2,5\n\
6,5\n\
1,4\n\
0,4\n\
6,4\n\
1,1\n\
6,1\n\
1,0\n\
0,5\n\
1,6\n\
2,0"
        input = input.split("\n")
        for i, line in enumerate(input):
            input[i] = list(map(int, line.split(",")))
        dimension = 7
        field = day18.build_map(input, 12, dimension)
        result, _= day18.part_one(field, (0,0), (6,6))
        self.assertEqual(result, 22)

    def test_part_two(self):
        input = "5,4\n\
4,2\n\
4,5\n\
3,0\n\
2,1\n\
6,3\n\
2,4\n\
1,5\n\
0,6\n\
3,3\n\
2,6\n\
5,1\n\
1,2\n\
5,5\n\
2,5\n\
6,5\n\
1,4\n\
0,4\n\
6,4\n\
1,1\n\
6,1\n\
1,0\n\
0,5\n\
1,6\n\
2,0"
        input = input.split("\n")
        for i, line in enumerate(input):
            input[i] = list(map(int, line.split(",")))
        dimension = 7
        result = day18.part_two(input, dimension, (0,0), (6,6), 0)
        self.assertEqual(result[0], 6)
        self.assertEqual(result[1], 1)