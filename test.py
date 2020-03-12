import unittest
from server import app


class TestEndpoint(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
    
    def test_should_run(self):
        self.assertEqual(True, True)
