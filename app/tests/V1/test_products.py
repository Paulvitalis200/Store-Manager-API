import unittest
from flask import json

from app import create_app

POST_PRODUCT_URL = '/api/v1/products'
GET_SINGLE_PRODUCT = '/api/v1/products/1'
GET_ALL_PRODUCTS = '/api/v1/products'


class BaseTest(unittest.TestCase):
    def setUp(self):
        """Initialize app and define test variables"""
        self.app = create_app()
        self.client = self.app.test_client()
        self.products = {
            "name": "Playstation 4",
            "price": 40000
        }

    def login(self):
        res = self.client.post('/api/v1/login', data=json.dumps(
            dict(username="Paul", password="1234")),
            content_type='application/json')
        return json.loads(res.get_data().decode("UTF-8"))['access_token']

    def test_post_product(self):
        """TEST whether the API can create a product(POST)"""
        res = self.client.post(POST_PRODUCT_URL,
                               content_type='application/json',
                               data=json.dumps(self.products),
                               headers=dict(Authorization="Bearer " + self.login())
                               )
        data = json.loads(res.get_data().decode("UTF-8"))
        self.assertTrue(data['message'] == 'product created succesfully')
        self.assertEqual(res.status_code, 201)

    def test_get_all_products(self):
        res = self.client.post(POST_PRODUCT_URL,
                               content_type='application/json',
                               headers=dict(Authorization="Bearer " + self.login()),
                               data=json.dumps(self.products))
        self.assertEqual(res.status_code, 201)
        res = self.client.get(GET_ALL_PRODUCTS,
                              data=json.dumps(self.products),
                              headers=dict(Authorization="Bearer " + self.login()),
                              content_type='application/json')

        self.assertEqual(res.status_code, 200)
        self.assertIn("Paul", str(res.data))

    def test_get_each_product(self):
        """Test API can get a single record by using it's id."""
        res = self.client.post(POST_PRODUCT_URL,
                               content_type='application/json',
                               headers=dict(Authorization="Bearer " + self.login()),
                               data=json.dumps(self.products))
        self.assertEqual(res.status_code, 201)
        res = self.client.get(GET_SINGLE_PRODUCT,
                              data=json.dumps(self.products),
                              headers=dict(Authorization="Bearer " + self.login()),
                              content_type='application/json')
        data = json.loads(res.get_data().decode("UTF-8"))
        self.assertEqual(res.status_code, 200)
        self.assertIn('Paul', str(res.data))


if __name__ == "__main__":
    unittest.main()
