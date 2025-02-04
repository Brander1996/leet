import unittest
from coordinate import Coordinate

class TestCoordinatesClass(unittest.TestCase):
    # def setUp(self):
    #     self.my_list = []
    #     for i in range(50,15, -4): 
    #         for j in range(0, 10, 2):
    #             self.my_list.append(Coordiate(i,j))
    #     for i in self.my_list:
    #         print(i)
    #     print("length of the list is:", len(self.my_list))

    def test_getX(self):
        self.assertEqual(Coordinate(50, -1).getX(), 50)
        self.assertEqual(Coordinate(-20, -1).getX(), -20)

    def test_getY(self):
        self.assertEqual(Coordinate(50, -1).getY(), -1)
        self.assertEqual(Coordinate(-20, -20).getY(), -20)

