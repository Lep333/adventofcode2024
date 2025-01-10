import unittest
from src import day23

class TestDay23(unittest.TestCase):
    def test_day23(self):
        input = "kh-tc\n\
qp-kh\n\
de-cg\n\
ka-co\n\
yn-aq\n\
qp-ub\n\
cg-tb\n\
vc-aq\n\
tb-ka\n\
wh-tc\n\
yn-cg\n\
kh-ub\n\
ta-co\n\
de-co\n\
tc-td\n\
tb-wq\n\
wh-td\n\
ta-ka\n\
td-qp\n\
aq-cg\n\
wq-ub\n\
ub-vc\n\
de-ta\n\
wq-aq\n\
wq-vc\n\
wh-yn\n\
ka-de\n\
kh-ta\n\
co-tc\n\
wh-qp\n\
tb-vc\n\
td-yn"
        input = input.split("\n")
        input = [el.split("-") for el in input]
        res = day23.part_one(input)
        self.assertEqual(res, 7)