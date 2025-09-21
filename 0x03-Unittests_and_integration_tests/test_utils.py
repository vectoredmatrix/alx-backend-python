#!/usr/bin/env python3
"""
Unit tests for the utils module.

Covers:
- access_nested_map
- get_json
- memoize
"""

import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock

from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Unit tests for the access_nested_map function."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test that access_nested_map returns expected values
        for valid nested_map and path.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Test that access_nested_map raises KeyError
        for invalid keys in path.
        """
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception), repr(path[-1]))


class TestGetJson(unittest.TestCase):
    """Unit tests for the get_json function."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """
        Test that get_json returns expected result
        and requests.get is called once with test_url.
        """
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        with patch(
                "utils.requests.get", 
                return_value=mock_response
        ) as mock_get:
            result = get_json(test_url)

            self.assertEqual(result, test_payload)
            mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Unit tests for the memoize decorator."""

    def test_memoize(self):
        """
        Test that memoize caches results after the first call
        and does not call the original method again.
        """

        class TestClass:
            """Dummy class to test memoize decorator."""

            def a_method(self):
                """Simple method returning 42."""
                return 42

            @memoize
            def a_property(self):
                """Property decorated with memoize."""
                return self.a_method()

        test_instance = TestClass()

        with patch.object(
            TestClass,
            "a_method",
            return_value=42
        ) as mock_method:
            result1 = test_instance.a_property()
            result2 = test_instance.a_property()

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
