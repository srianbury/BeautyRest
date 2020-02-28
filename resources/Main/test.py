import unittest
from .resource import Main


class TestGetUrl(unittest.TestCase):
    def setUp(self):
        self.resource = Main()


    def test_with_query_and_2_args(self):
        expected = 'https://www.google.com/search?q=mysearch&lang=eng&time=4'
        args = {
            'url': 'https://www.google.com/search?q=mysearch',
            'lang': 'eng',
            'time': '4'
        }
        actual = self.resource._get_url(args)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
