import unittest
from .resource import Main


class TestGetUrl(unittest.TestCase):
    def setUp(self):
        self.resource = Main()

    
    def test_plain(self):
        expected = 'https://www.google.com/'
        args = {
            'url': 'https://www.google.com/'
        }
        actual = self.resource._get_url(args)
        self.assertEqual(expected, actual)

    
    def test_with_query(self):
        expected = 'https://www.google.com/search?q=mysearch'
        args = {
            'url': 'https://www.google.com/search?q=mysearch'
        }
        actual = self.resource._get_url(args)
        self.assertEqual(expected, actual)


    def test_with_query_and_2_args(self):
        expected = 'https://www.google.com/search?q=mysearch&lang=eng&time=4'
        args = {
            'url': 'https://www.google.com/search?q=mysearch',
            'lang': 'eng',
            'time': '4'
        }
        actual = self.resource._get_url(args)
        self.assertEqual(expected, actual)
    