#!/usr/bin/env python3
"""
Test Client
"""
from parameterized import parameterized
from utils import access_nested_map
from unittest import TestCase


class TestAccessNestedMap(TestCase):
    """
    A class that inherits from unittest.TestCase
    for carrying out unit test on utils.access_nested_map
    """
    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2)
        ]
    )
    def test_access_nested_map(self, nested_map, path, expected_output):
        """
        A method to test that utils.access_nested_map
        returns what it is supposed to
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_output)
