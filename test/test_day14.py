import unittest
from src import day14

class TestDay14(unittest.TestCase):
    def test_part_one(self):
        roboters = []
        text = "p=0,4 v=3,-3\np=6,3 v=-1,-3\np=10,3 v=-1,2\np=2,0 v=2,-1\np=0,0 v=1,3\np=3,0 v=-2,-2\np=7,6 v=-1,-3\np=3,0 v=-1,-2\np=9,3 v=2,3\np=7,3 v=-1,2\np=2,4 v=2,-3\np=9,5 v=-3,-3"
        
        text = text.replace("p=", "")
        text = text.replace("v=", "")
        text = text.replace(",", " ")
        text = text.split("\n")
        for roboter in text:
            pos_x, pos_y, vel_x, vel_y = roboter.split()
            roboters.append((int(pos_x), int(pos_y), int(vel_x), int(vel_y)))
        day14.no_of_rows = 7
        day14.no_of_cols = 11
        res = day14.part_one(roboters)

        self.assertEqual(res, 12)