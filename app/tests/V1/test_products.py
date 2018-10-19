import unittest
import json

from app import create_app


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.products = {
            "name": "James",
            "price": 2000
        }
