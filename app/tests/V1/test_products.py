import unittest

from flask import json

from app import create_app

POST_PRODUCT_URL = '/api/v1/products'
GET_SINGLE_PRODUCT = '/api/v1/products/1'
GET_ALL_PRODUCTS = '/api/v1/products'


class ProductTest(unittest.TestCase):
  def setUp(self):
    """Initialize app and define test variables"""
    self.app = create_app('testing')
    self.client = self.app.test_client()
    self.products = {
        "name": "Playstation 4",
        "price": 40000,
        "quantity": 3
    }
    self.empty_products = {"name": "", "quantity": 5, "price": 3000}
    self.empty_price = {"name": "xbox", "quantity": 5, "price": ""}
    self.empty_quantity = {"name": "xbox", "quantity": "", "price": 5000}

  def login(self):
    res = self.client.post(
        '/api/v1/login',
        data=json.dumps(
            dict(email="vitalispaul48@live.com", password="manu2012")
        ),
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
    self.assertTrue(data['message'] == 'Product created successfully!')
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
    self.assertIn("Playstation 4", str(res.data))

  def test_get_each_product(self):
    """Test API can get a single record by using it's id."""
    '''Add a product'''
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
    self.assertIn('Playstation 4', str(res.data))

  def test_empty_products(self):
    res = self.client.post(POST_PRODUCT_URL,
                           content_type='application/json',
                           data=json.dumps(self.empty_products),
                           headers=dict(Authorization="Bearer " + self.login())
                           )
    data = json.loads(res.get_data().decode("UTF-8"))
    self.assertTrue(data['message'] == 'Product name cannot be empty')
    self.assertEqual(res.status_code, 400)


if __name__ == "__main__":
  unittest.main()
