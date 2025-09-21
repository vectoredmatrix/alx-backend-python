#!/usr/bin/env python3
"""Unit tests for utils.access_nested_map (Tasks 0 & 1)."""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Tests for access_nested_map function."""

    @parameterized.expand([
        ({"a": 1}, ["a"], 1),
        ({"a": {"b": 2}}, ["a"], {"b": 2}),
        ({"a": {"b": 2}}, ["a", "b"], 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Task 0:
        Test that access_nested_map returns the expected result
        for different nested maps and paths.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "'a'"),
        ({"a": 1}, ("a", "b"), "'b'"),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_message):
        """
        Task 1:
        Test that access_nested_map raises KeyError
        for missing keys, and check the exception message.
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        self.assertEqual(str(context.exception), expected_message)


if __name__ == "__main__":
    unittest.main()
