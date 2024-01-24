#!/usr/bin/env python3
""" testing case for acces_nasted_map in utils """
from utils import access_nested_map
import unittest
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """ access nested map testing case """
    @parameterized.expand(
            [
                ({"a": 1}, ("a",), 1),
                ({"a": {"b": 2}}, ("a",), {"b": 2}),
                ({"a": {"b": 2}}, ("a", "b"), 2)
            ]
    )
    def test_access_nested_map(self, nasted_map, path, expected):
        """ a test method """
        self.assertEqual(access_nested_map(nasted_map, path), expected)


if __name__ == "__main__":
    unittest.main()
