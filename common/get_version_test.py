import unittest
from .get_version import get_version


class TestGetVersion(unittest.TestCase):    
    def test_should_get_version(self):
        expected = 'v1'
        actual = get_version()
        self.assertEqual(expected, actual)
