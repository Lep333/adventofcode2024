import unittest
from src import day5

class TestDay5(unittest.TestCase):
    def test_part_one(self):
        input = "47|53\n\
97|13\n\
97|61\n\
97|47\n\
75|29\n\
61|13\n\
75|53\n\
29|13\n\
97|29\n\
53|29\n\
61|53\n\
97|53\n\
61|29\n\
47|13\n\
75|47\n\
97|75\n\
47|61\n\
75|61\n\
47|29\n\
75|13\n\
53|13\n\
\n\
75,47,61,53,29\n\
97,61,53,29,13\n\
75,29,13\n\
75,97,47,61,53\n\
61,13,29\n\
97,13,75,29,47"

        result = day5.part_one(input)
        self.assertEqual(result, 143)

    def test_part_two(self):
        input = "47|53\n\
97|13\n\
97|61\n\
97|47\n\
75|29\n\
61|13\n\
75|53\n\
29|13\n\
97|29\n\
53|29\n\
61|53\n\
97|53\n\
61|29\n\
47|13\n\
75|47\n\
97|75\n\
47|61\n\
75|61\n\
47|29\n\
75|13\n\
53|13\n\
\n\
75,47,61,53,29\n\
97,61,53,29,13\n\
75,29,13\n\
75,97,47,61,53\n\
61,13,29\n\
97,13,75,29,47"

        result = day5.part_two(input)
        self.assertEqual(result, 123)