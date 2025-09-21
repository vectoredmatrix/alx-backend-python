#!/usr/bin/env python3
import unittest
from unittest.mock import patch

from utils import memoize


class TestMemoize(unittest.TestCase):
    """Unit tests for the memoize decorator"""

    def test_memoize(self):
        """Test that memoize caches result after first call"""

        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        test_instance = TestClass()

        with patch.object(TestClass, "a_method", return_value=42) as mock_method:
            # First call should call a_method
            result1 = test_instance.a_property()
            # Second call should return cached value without calling a_method again
            result2 = test_instance.a_property()

            # Both calls should return the same result
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

            # Ensure a_method was called only once due to memoization
            mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
