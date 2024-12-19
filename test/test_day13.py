import unittest
from src import day13

class TestDay13(unittest.TestCase):
    def test_part_one(self):
        text = "Button A: X+94, Y+34\nButton B: X+22, Y+67\nPrize: X=8400, Y=5400\n\nButton A: X+26, Y+66\nButton B: X+67, Y+21\nPrize: X=12748, Y=12176\n\nButton A: X+17, Y+86\nButton B: X+84, Y+37\nPrize: X=7870, Y=6450\n\nButton A: X+69, Y+23\nButton B: X+27, Y+71\nPrize: X=18641, Y=10279"
        text = text.replace("X", "")
        text = text.replace("Y", "")
        text = text.replace("=", "")
        text = text.replace(",", "")
        text = text.replace("\n\n", "\n")
        text = text.split("\n")

        button_a = ()
        button_b = ()
        prize = ()
        bandits = []
        for i, row in enumerate(text):
            if not row:
                continue
            if i % 3 == 0:
                _, _, x, y = row.split()
                button_a = int(x), int(y)
            elif i % 3 == 1:
                _, _, x, y = row.split()
                button_b = int(x), int(y)
            else:
                _, x, y = row.split()
                prize = int(x), int(y)
                bandits.append((button_a, button_b, prize))
                button_a = ()
                button_b = ()
                prize = ()
        
        result = day13.part_one(bandits)
        self.assertEqual(result, 480)