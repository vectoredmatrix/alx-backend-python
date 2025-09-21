#!/usr/bin/env python3
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized

import utils


class TestGetJson(unittest.TestCase):
    """Unit tests for utils.get_json function"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch("utils.requests.get")
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test utils.get_json returns expected payload and calls requests.get"""
        # Arrange: create mock response
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        # Act: call function under test
        result = utils.get_json(test_url)

        # Assert: check requests.get was called once with correct URL
        mock_get.assert_called_once_with(test_url)

        # Assert: check return value equals payload
        self.assertEqual(result, test_payload)


if __name__ == "__main__":
    unittest.main()
