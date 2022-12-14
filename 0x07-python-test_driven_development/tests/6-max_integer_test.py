#!/usr/bin/python3

"""
Test for max_integer function

Module to Test: 6-max_integer
Author: Ifeanyichukwu Ifeanyichukwu
Date: Dec. 29, 2022
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMax_integerFunction(unittest.TestCase):
    """Function test case"""

    def test_correct_type(self):
        """Tests for correct type"""
        pass

    def test_correct_return_value(self):
        """Tests for correct return output"""
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([1, 5, 2]), 5)
        self.assertEqual(max_integer([5, 4, 1]), 5)
        self.assertEqual(max_integer([-1, 0, 1]), 1)
        self.assertEqual(max_integer([-2, -1, -3]), -1)
        self.assertEqual(max_integer([2]), 2)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)


if __name__ == '__main__':
    unittest.main()
