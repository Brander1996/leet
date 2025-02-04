import unittest
from leetcode6 import Solution

class TestLeetcode6(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_nextZigZagCoordinatites(self):
        self.assertEqual(self.solution.nextZigZagCoordinates((1,0), 4)[0], 2)
        self.assertEqual(self.solution.nextZigZagCoordinates((1,0), 4)[1], 0)

        self.assertEqual(self.solution.nextZigZagCoordinates((3,0), 4)[0], 2)
        self.assertEqual(self.solution.nextZigZagCoordinates((3,0), 4)[1], 1)

        self.assertEqual(self.solution.nextZigZagCoordinates((2,1), 4)[0], 1)
        self.assertEqual(self.solution.nextZigZagCoordinates((2,1), 4)[1], 2)

        self.assertEqual(self.solution.nextZigZagCoordinates((1,2), 4)[0], 0)
        self.assertEqual(self.solution.nextZigZagCoordinates((1,2), 4)[1], 3)

        self.assertEqual(self.solution.nextZigZagCoordinates((0,3), 4)[0], 1)
        self.assertEqual(self.solution.nextZigZagCoordinates((0,3), 4)[1], 3)

        self.assertEqual(self.solution.nextZigZagCoordinates((1,0), 5)[0], 2)
        self.assertEqual(self.solution.nextZigZagCoordinates((1,0), 5)[1], 0)

        self.assertEqual(self.solution.nextZigZagCoordinates((4,0), 5)[0], 3)
        self.assertEqual(self.solution.nextZigZagCoordinates((4,0), 5)[1], 1)

        self.assertEqual(self.solution.nextZigZagCoordinates((3,1), 5)[0], 2)
        self.assertEqual(self.solution.nextZigZagCoordinates((3,1), 5)[1], 2)

        
        