import unittest
from src import day10

class TestDay10(unittest.TestCase):
    def test_part_one_simple(self):
        input =  """0123\n1234\n8765\n9876"""
        input = input.split("\n")
        result = day10.part_one(input)
        self.assertEqual(result, 1)

    def test_part_one_complex(self):
        input = """89010123\n78121874\n87430965\n96549874\n45678903\n32019012\n01329801\n10456732"""
        input = input.split("\n")
        result = day10.part_one(input)
        self.assertEqual(result, 36)
    
    def test_part_two_complex(self):
        input = """89010123\n78121874\n87430965\n96549874\n45678903\n32019012\n01329801\n10456732"""
        input = input.split("\n")
        result = day10.part_two(input)
        self.assertEqual(result, 81)