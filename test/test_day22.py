import unittest
from src import day22

class TestDay22(unittest.TestCase):
    def test_part_one(self):
        input = [123]
        result = day22.part_one(input, 10)
        self.assertEqual(result, 5908254)
    
    def test_part_one2(self):
        input = [1, 10, 100, 2024]
        result = day22.part_one(input, 2000)
        self.assertEqual(result, 37327623)
    
    def test_part_two(self):
        input = [1, 2, 3, 2024]
        result = day22.part_two(input, 2000)
        self.assertEqual(result, 23)