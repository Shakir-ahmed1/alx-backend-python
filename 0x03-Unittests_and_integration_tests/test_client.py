#!/usr/bin/env python3
""" client module testing module """
import unittest
from parameterized import parameterized, parameterized_class
from unittest import mock
from unittest.mock import patch, Mock, PropertyMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ self descriptive """
    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch("client.get_json")
    def test_org(self, client_name, get_mock):
        """ test the org method """
        org = "https://api.github.com/orgs/{}".format(client_name)
        cli = GithubOrgClient(client_name)
        cli.org()
        get_mock.assert_called_once_with(org)

    @patch("client.GithubOrgClient.org", new_callable=PropertyMock,
           return_value={"repos_url": "abcde"})
    def test_public_repos_url(self, mock_get):
        """ test the _public_repos_url """
        cli = GithubOrgClient("any")
        result = cli._public_repos_url
        self.assertEqual(result, "abcde")

    @patch("client.get_json",
           return_value=[{"name": "a", "license": {"key": "yes"}}])
    def test_public_repos(self, mock_get):
        """ test public_repos method"""
        with patch("client.GithubOrgClient._public_repos_url",
                   return_value="a1"):
            cli = GithubOrgClient("abcd")
            result = cli.public_repos("yes")
            self.assertEqual(result, ["a"])


if __name__ == "__main__":
    unittest.main()
