#Note how you can just import the new library like a python module. The syntax in the Cython file has given us an easy to use python interface to our C++ Rectangle class.

import unittest
import rectangle_wrapper


class TestBasic(unittest.TestCase):

    def setUp(self):   
        self.app = rectangle_wrapper.PyRectangle(2,4,6,8)

    def test_getLength(self):
        self.assertEqual(self.app.getLength(), 4)
    
    def test_getHeight(self):
        self.assertEqual(self.app.getHeight(), 4)

    def test_getArea(self):
        self.assertEqual(self.app.getArea(), 16)

if __name__ == '__main__':
    unittest.main()