import unittest
import json
from server import app
from common import constants
from resources.Main.resource import Main


class TestEndpoint(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
    
    def test_should_run(self):
        self.assertEqual(True, True)

    def test_missing_required_param_code(self):
        expected = 400
        actual = self.app.get(Main().route).status_code
        self.assertEqual(expected, actual)

    def test_missing_required_param_message(self):
        expected = constants.ERROR_PARAM_URL
        response = self.app.get(Main().route)
        actual = response.json['message']['url']
        self.assertEqual(expected, actual)
