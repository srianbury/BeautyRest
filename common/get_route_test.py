import unittest
from .get_route import get_route

class TestGetPath(unittest.TestCase):
    def test_should_get_1_path(self):
        expected = '/v1/soup'
        actual = get_route(['soup'])
        self.assertEqual(expected, actual)
