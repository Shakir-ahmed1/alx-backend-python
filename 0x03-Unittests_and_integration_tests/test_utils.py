#!/usr/bin/env python3
""" testing case for acces_nasted_map in utils """
from utils import access_nested_map, get_json
import unittest
from unittest.mock import Mock, patch
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

    @parameterized.expand(
            [
                ({}, ("a",)),
                ({"a": 1}, ("a", "b")),
            ]
    )
    def test_access_nested_map_exception(self, nasted_map, path):
        """ a test method """
        with self.assertRaises(KeyError):
            access_nested_map(nasted_map, path)


class TestGetJson(unittest.TestCase):
    """ test case for get_json """
    @parameterized.expand([
         ("http://example.com", {"payload": True}),
         ("http://holberton.io", {"payload": False})
        ])
    def test_get_json(self, test_url, test_payload):
        """ test case for get_json """
        with patch("utils.requests.get") as get_mock:
            get_mock.return_value.json.return_value = test_payload
            data = get_json(test_url)
            get_mock.assert_called_with(test_url)
            self.assertEqual(data, test_payload)


if __name__ == "__main__":
    unittest.main()
