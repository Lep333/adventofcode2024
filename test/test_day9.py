import unittest
from src import day9

class Test_Day9(unittest.TestCase):
    def test_part_one(self):
        input = "2333133121414131402"
        result = day9.part_one(input)
        self.assertAlmostEqual(result, 1928)

    def test_part_two(self):
        input = "2333133121414131402"
        result = day9.part_two(input)
        self.assertAlmostEqual(result, 2858)

    def test_move_file(self):
        input = "2333133121414131402"
        input = day9.create_file_system(input)
        day9.move_file(input, 32, 12, 3)
        self.assertTrue(input)

    def test_space_start_index(self):
        input = "2333133121414131402"
        input = day9.create_file_system(input)
        result = day9.space_start_index(input, 22, 4)
        self.assertEqual(result, -1)

    def test_space_start_index2(self):
        input = "2333133121414131402"
        input = day9.create_file_system(input)
        result = day9.space_start_index(input, 5, 3)
        self.assertEqual(result, 2)