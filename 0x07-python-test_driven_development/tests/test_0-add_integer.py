#!/usr/bin/python3

"""
Unit test for module 0-add_integer
"""

import sys
import unittest
from importlib import import_module
sys.path.insert(1, '../')


class ModuleTestCase(unittest.TestCase):
    """Unit tests for module 0-add_integer

    Attributres:
        add_integer: function to use for tests
    """
    def setUp(self):
        """Sets up the test function"""
        self.add_integer = import_module('0-add_integer').add_integer

    def tearDown(self):
        """Deletes the test function"""
        del self.add_integer

    def test_integer_float_add(self):
        """Test addition between integers and floats"""
        self.assertEqual(self.add_integer(20, 5), 25)
        self.assertEqual(self.add_integer(20, 5.2), 25)
        self.assertEqual(self.add_integer(5.3, 20), 25)

    def test_integer_string_add(self):
        """Tests addition between integers and strings"""
        self.assertRaises(TypeError, self.add_integer, 20, 'twenty')
        self.assertRaises(TypeError, self.add_integer, 'twenty', 3)

    def test_integer_list_dict_set_add(self):
        """Tests addition between integers and (lists, dicts, sets)"""
        self.assertRaises(TypeError, self.add_integer, 20, [1, 2])
        self.assertRaises(TypeError, self.add_integer, [1], 2)
        self.assertRaises(TypeError, self.add_integer, 20, {'a': 1})
        self.assertRaises(TypeError, self.add_integer, {'a': 3}, 20)
        self.assertRaises(TypeError, self.add_integer, 2, {1, 2})
        self.assertRaises(TypeError, self.add_integer, {1, 2}, 4)

    def test_float_string_add(self):
        """Tests addition between floats and strings"""
        self.assertRaises(TypeError, self.add_integer, 20.1, '2')
        self.assertRaises(TypeError, self.add_integer, 'two', 20)

    def test_float_list_dict_set_add(self):
        """Test addition between floats and (lists, dicts, sets..)"""
        self.assertRaises(TypeError, self.add_integer, 20.2, [1])
        self.assertRaises(TypeError, self.add_integer, [1], 2.5)
        self.assertRaises(TypeError, self.add_integer, 20.2, {'a': 3})
        self.assertRaises(TypeError, self.add_integer, {'b': 4}, 5.5)
        self.assertRaises(TypeError, self.add_integer, 20.9, {1, 2, 3})
        self.assertRaises(TypeError, self.add_integer, {20.2, 4}, [1])


if __name__ == '__main__':
    unittest.main()
