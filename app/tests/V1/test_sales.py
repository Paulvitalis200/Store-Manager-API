import unittest
from flask import json

from app import create_app

POST_SALE_URL = '/api/v1/sales'
GET_EACH_SALE = '/api/v1/sales/1'
GET_ALL_SALES = '/api/v1/sales'


class SalesTest(unittest.TestCase):
  def setUp(self):
    """Initialize app and define test variables"""
    self.app = create_app('testing')
    self.client = self.app.test_client()
    self.sales = {
        "description": "Piano black",
        "items": {"id": 1, "name": "Playstation 4", "price": 20000, "quantity": 3}
    }

    self.empty_sale_description = {
        "description": "",
        "items": {"id": 1, "name": "Playstation 4", "price": 20000, "quantity": 3}
    }
    self.empty_sale_items = {
        "description": "Piano black",
        "items": ""
    }

  def login(self):
    res = self.client.post(
        '/api/v1/login',
        data=json.dumps(
            dict(email="vitalispaul48@live.com", password="manu2012")
        ),
        content_type='application/json')
    return json.loads(res.get_data().decode("UTF-8"))['access_token']

  def test_post_sale(self):
    """TEST whether the API can create a product(POST)"""
    res = self.client.post(POST_SALE_URL,
                           content_type='application/json',
                           data=json.dumps(self.sales),
                           headers=dict(Authorization="Bearer " + self.login())
                           )
    resp_data = json.loads(res.data.decode())
    self.assertTrue(resp_data['message'] == 'Sale record created successfully!')
    self.assertEqual(res.status_code, 201)

  def test_get_all_sales(self):
    """TEST whether the API can get all product(POST)"""
    res = self.client.post(POST_SALE_URL,
                           content_type='application/json',
                           headers=dict(Authorization="Bearer " + self.login()),
                           data=json.dumps(self.sales))
    self.assertEqual(res.status_code, 201)
    res = self.client.get(GET_ALL_SALES,
                          headers=dict(Authorization="Bearer " + self.login()),
                          content_type='application/json')
    resp_data = json.loads(res.data.decode())
    self.assertTrue(resp_data['message'] == 'Sales records retrieved successfully!')
    self.assertTrue(resp_data['status'] == 'ok')
    self.assertEqual(res.status_code, 200)

  def test_get_each_sale(self):
    """Test API can get a single record by using it's id."""
    '''Add a product'''
    res = self.client.post(POST_SALE_URL,
                           content_type='application/json',
                           headers=dict(Authorization="Bearer " + self.login()),
                           data=json.dumps(self.sales))
    self.assertEqual(res.status_code, 201)
    res = self.client.get(GET_EACH_SALE,
                          data=json.dumps(self.sales),
                          headers=dict(Authorization="Bearer " + self.login()),
                          content_type='application/json')
    data = json.loads(res.get_data().decode("UTF-8"))
    self.assertEqual(res.status_code, 200)
    self.assertIn('Playstation 4', str(res.data))

  def test_empty_sale_description(self):
    res = self.client.post(POST_SALE_URL,
                           content_type='application/json',
                           data=json.dumps(self.empty_sale_description),
                           headers=dict(Authorization="Bearer " + self.login())
                           )
    resp_data = json.loads(res.data.decode())
    self.assertTrue(resp_data['message'] == 'Sale description can not be empty')
    self.assertEqual(res.status_code, 400)

  def test_empty_sale_items(self):
    res = self.client.post(POST_SALE_URL,
                           content_type='application/json',
                           data=json.dumps(self.empty_sale_items),
                           headers=dict(Authorization="Bearer " + self.login())
                           )
    resp_data = json.loads(res.data.decode())
    self.assertTrue(resp_data['message'] == 'Sale items can not be empty')
    self.assertEqual(res.status_code, 400)

  def test_create_sale(self):
    res = self.client.post(POST_SALE_URL,
                           content_type='application/json',
                           data=json.dumps(self.sales),
                           headers=dict(Authorization="Bearer " + self.login())
                           )
    resp_data = json.loads(res.data.decode())
    self.assertTrue(resp_data['message'] == 'Sale record created successfully!')
    self.assertEqual(res.status_code, 201)


if __name__ == "__main__":
  unittest.main()
