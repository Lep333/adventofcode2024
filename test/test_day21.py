import unittest
from src import day21

class TestDay21(unittest.TestCase):
    def test_part_one(self):
        input = ["029A", "980A", "179A", "456A", "379A"]
        result = day21.part_one(input)
        self.assertEqual(result, 126384)

    def test_part_two(self):
        input = ["029A", "980A", "179A", "456A", "379A"]
        result = day21.part_two(input, n = 2)
        self.assertEqual(result, 126384)

    def test_part_two2(self):
        input = ["029A"]
        result = day21.part_two(input, n = 3)
        self.assertEqual(result, 5974)

    def test_part_two3(self):
        input = ["456A"]
        result = day21.part_two(input, n = 3)
        self.assertEqual(result, 75696)

    def test_get_instruction_up(self):
        numeric_keypad = {}
        numeric_keypad["0"] = (1, 0)
        numeric_keypad["A"] = (2, 0)
        numeric_keypad["1"] = (0, 1)
        numeric_keypad["2"] = (1, 1)
        numeric_keypad["3"] = (2, 1)
        numeric_keypad["4"] = (0, 2)
        numeric_keypad["5"] = (1, 2)
        numeric_keypad["6"] = (2, 2)
        numeric_keypad["7"] = (0, 3)
        numeric_keypad["8"] = (1, 3)
        numeric_keypad["9"] = (2, 3)
        result = day21.get_instruction(numeric_keypad, "A", "7")
        self.assertEqual(result[0], "^^^<<A")

    def test_get_instruction_down(self):
        numeric_keypad = {}
        numeric_keypad["0"] = (1, 0)
        numeric_keypad["A"] = (2, 0)
        numeric_keypad["1"] = (0, 1)
        numeric_keypad["2"] = (1, 1)
        numeric_keypad["3"] = (2, 1)
        numeric_keypad["4"] = (0, 2)
        numeric_keypad["5"] = (1, 2)
        numeric_keypad["6"] = (2, 2)
        numeric_keypad["7"] = (0, 3)
        numeric_keypad["8"] = (1, 3)
        numeric_keypad["9"] = (2, 3)
        result = day21.get_instruction(numeric_keypad, "1", "0")
        self.assertEqual(result[0], ">vA")

    def test(self):
        dir_keypad = {}
        dir_keypad["<"] = (0, 0)
        dir_keypad["v"] = (1, 0)
        dir_keypad[">"] = (2, 0)
        dir_keypad["^"] = (1, 1)
        dir_keypad["A"] = (2, 1)
        result = day21.get_instruction(dir_keypad, "A", "<")
        self.assertEqual(result[0], "v<<A")
        print("aha")

    def test_keypad_right(self):
        dir_keypad = {}
        dir_keypad["<"] = (0, 0)
        dir_keypad["v"] = (1, 0)
        dir_keypad[">"] = (2, 0)
        dir_keypad["^"] = (1, 1)
        dir_keypad["A"] = (2, 1)
        result = day21.get_instruction(dir_keypad, "<", "A")
        self.assertEqual(result[0], ">>^A")

    def test_keypad_v(self):
        dir_keypad = {}
        dir_keypad["<"] = (0, 0)
        dir_keypad["v"] = (1, 0)
        dir_keypad[">"] = (2, 0)
        dir_keypad["^"] = (1, 1)
        dir_keypad["A"] = (2, 1)
        result = day21.get_instruction(dir_keypad, "A", "v")
        self.assertEqual(result[0], "v<A")

    def test_keypad_A(self):
        dir_keypad = {}
        dir_keypad["<"] = (0, 0)
        dir_keypad["v"] = (1, 0)
        dir_keypad[">"] = (2, 0)
        dir_keypad["^"] = (1, 1)
        dir_keypad["A"] = (2, 1)
        result = day21.get_instruction(dir_keypad, "v", "A")
        self.assertEqual(result[0], ">^A")