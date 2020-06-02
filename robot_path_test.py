import unittest
from robot_path import Robot

class TestRobotPath(unittest.TestCase):
  
    def test_3_2(self):
        self.assertEqual( 3, Robot().findPath((0,0), (3,2)) )

    def test_1_1(self):
        self.assertEqual( 1, Robot().findPath((0,0), (1,1)) )

if __name__ == '__main__':
    unittest.main()