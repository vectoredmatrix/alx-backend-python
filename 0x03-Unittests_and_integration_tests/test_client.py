#!/usr/bin/env python3
"""
Unit tests for client.GithubOrgClient
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized

from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Unit tests for GithubOrgClient"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the expected payload"""

        # Arrange
        expected_payload = {"login": org_name, "id": 1}
        mock_get_json.return_value = expected_payload

        # Act
        client = GithubOrgClient(org_name)
        result = client.org

        # Assert
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )
        self.assertEqual(result, expected_payload)

    def test_public_repos_url(self):
        """Test that _public_repos_url returns expected value"""

        # Arrange
        expected_url = "https://api.github.com/orgs/test-org/repos"
        payload = {"repos_url": expected_url}

        with patch.object(GithubOrgClient, "org", new_callable=unittest.mock.PropertyMock) as mock_org:
            mock_org.return_value = payload

            # Act
            client = GithubOrgClient("test-org")
            result = client._public_repos_url

            # Assert
            self.assertEqual(result, expected_url)


if __name__ == "__main__":
    unittest.main()
