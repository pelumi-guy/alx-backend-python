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

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        A method that uses the assertRaises context manager
        to test that a KeyError is raised for given input
        """

        self.assertRaises(KeyError, access_nested_map, nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    A class that inherits from unittest.TestCase
    for carrying out unit test on utils.get_json
    """
    @parameterized.expand(
        [
            ('http://example.com', {'payload': True}),
            ('http://holberton.io', {'payload': False})
        ]
    )
    def test_get_json(self, url, expected_output):
        """
        A method to test that utils.get_json returns the expected result.
        """
        mock_response = Mock()
        mock_response.json.return_value = expected_output
        with patch('requests.get', return_value=mock_response):
            response = get_json(url)

            self.assertEqual(response, expected_output)


class TestMemoize(unittest.TestCase):
    """
    Class for testing the utils.memoize decorator
    """

    def test_memoize(self):
        """
        Method to test utils.memoize
        """

        class TestClass:
            """
            Mock test class for testing
            """

            def a_method(self):
                """
                Mock test object method
                """
                return 42

            @memoize
            def a_property(self):
                """
                Mock test object method
                """
                return self.a_method()

        test_obj = TestClass()

        with patch.object(test_obj, 'a_method') as mock_method:
            mock_method.return_value = 42

            result1 = test_obj.a_property
            result2 = test_obj.a_property

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            mock_method.assert_called_once()
