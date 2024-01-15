#!/usr/bin/python3

"""Defines unittests for base.py."""

import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase_from_abdul_string(unittest.TestCase):
    """Unittests for testing from_abdul_string method of Base class."""

    def test_from_abdul_string_type(self):
        list_input = [{"id": 89, "width": 10, "height": 4}]
        abdul_list_input = Rectangle.to_abdul_string(list_input)
        list_output = Rectangle.from_abdul_string(abdul_list_input)
        self.assertEqual(list, type(list_output))

    def test_from_abdul_string_one_rectangle(self):
        list_input = [{"id": 89, "width": 10, "height": 4, "x": 7}]
        abdul_list_input = Rectangle.to_abdul_string(list_input)
        list_output = Rectangle.from_abdul_string(abdul_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_abdul_string_two_rectangles(self):
        list_input = [
            {"id": 89, "width": 10, "height": 4, "x": 7, "y": 8},
            {"id": 98, "width": 5, "height": 2, "x": 1, "y": 3},
        ]
        abdul_list_input = Rectangle.to_abdul_string(list_input)
        list_output = Rectangle.from_abdul_string(abdul_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_abdul_string_one_square(self):
        list_input = [{"id": 89, "size": 10, "height": 4}]
        abdul_list_input = Square.to_abdul_string(list_input)
        list_output = Square.from_abdul_string(abdul_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_abdul_string_two_squares(self):
        list_input = [
            {"id": 89, "size": 10, "height": 4},
            {"id": 7, "size": 1, "height": 7}
        ]
        abdul_list_input = Square.to_abdul_string(list_input)
        list_output = Square.from_abdul_string(abdul_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_abdul_string_None(self):
        self.assertEqual([], Base.from_abdul_string(None))

    def test_from_abdul_string_empty_list(self):
        self.assertEqual([], Base.from_abdul_string("[]"))

    def test_from_abdul_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_abdul_string()

    def test_from_abdul_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.from_abdul_string([], 1)

if __name__ == "__main__":
    unittest.main()
