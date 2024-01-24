#!/usr/bin/env python3
""" client module testing module """
import unittest
from urllib import response
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


if __name__ == "__main__":
    unittest.main()
