import unittest
from leetcode6 import Solution
from coordinate import Coordinate

class TestLeetcode6(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_nextZigZagCoordinatites(self):
        self.assertEqual(self.solution.nextZigZagCoordinates(Coordinate(1,0), 4).getX(), 2)
        self.assertEqual(self.solution.nextZigZagCoordinates(Coordinate(1,0), 4).getY(), 0)

        self.assertEqual(self.solution.nextZigZagCoordinates(Coordinate(3,0), 4).getX(), 2)
        self.assertEqual(self.solution.nextZigZagCoordinates(Coordinate(3,0), 4).getY(), 1)

        self.assertEqual(self.solution.nextZigZagCoordinates(Coordinate(2,1), 4).getX(), 1)
        self.assertEqual(self.solution.nextZigZagCoordinates(Coordinate(2,1), 4).getY(), 2)

        self.assertEqual(self.solution.nextZigZagCoordinates(Coordinate(1,2), 4).getX(), 0)
        self.assertEqual(self.solution.nextZigZagCoordinates(Coordinate(1,2), 4).getY(), 3)

        self.assertEqual(self.solution.nextZigZagCoordinates(Coordinate(0,3), 4).getX(), 1)
        self.assertEqual(self.solution.nextZigZagCoordinates(Coordinate(0,3), 4).getY(), 3)

        self.assertEqual(self.solution.nextZigZagCoordinates(Coordinate(1,0), 5).getX(), 2)
        self.assertEqual(self.solution.nextZigZagCoordinates(Coordinate(1,0), 5).getY(), 0)

        self.assertEqual(self.solution.nextZigZagCoordinates(Coordinate(4,0), 5).getX(), 3)
        self.assertEqual(self.solution.nextZigZagCoordinates(Coordinate(4,0), 5).getY(), 1)

        self.assertEqual(self.solution.nextZigZagCoordinates(Coordinate(3,1), 5).getX(), 2)
        self.assertEqual(self.solution.nextZigZagCoordinates(Coordinate(3,1), 5).getY(), 2)

        
        