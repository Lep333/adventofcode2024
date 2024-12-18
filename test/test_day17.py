import unittest
from src import day17

class TestDay17(unittest.TestCase):
    def test_part_one(self):
        input = "Register A: 729\n\
Register B: 0\n\
Register C: 0\n\
\n\
Program: 0,1,5,4,3,0"
        input = day17.parse(input)
        result = day17.part_one(input)
        self.assertEqual(result, "4,6,3,5,6,3,5,2,1,0")

    def test_part_two(self):
        input = "Register A: 2024\n\
Register B: 0\n\
Register C: 0\n\
\n\
Program: 0,3,5,4,3,0"
        input = day17.parse(input)
        result = day17.part_two(input)
        self.assertEqual(result, 117440)