import unittest
import json

from app import create_app


POST_SALES_URL = '/api/v1/sales'
GET_EACH_SALE = '/api/v1/sales/1'
GET_ALL_SALES = '/api/v1/sales'


class BaseTest(unittest.TestCase):
  def setUp(self):
    self.app = create_app()
    self.client = self.app.test_client()
    self.sales = {"name": "Shoes", "price": 2000}

  def login(self):
    res = self.client.post('/api/v1/login', data=json.dumps(
        dict(username="Paul", password="1234")),
        content_type='application/json')
    return json.loads(res.get_data().decode("UTF-8"))['access_token']

  def test_post_sales(self):
    """TEST an API can create a sale record(POST)"""
    res = self.client.post(
        POST_SALES_URL,
        content_type='application/json',
        data=json.dumps(self.sales),
        headers=dict(Authorization="Bearer " + self.login())
    )
    data = json.loads(res.get_data().decode("UTF-8"))
    self.assertEqual(res.status_code, 201)

  def test_get_all_sales(self):
    res = self.client.post(
        POST_SALES_URL,
        content_type='application/json',
        data=json.dumps(self.sales),
        headers=dict(Authorization="Bearer " + self.login())
    )
    self.assertEqual(res.status_code, 201)
    res = self.client.get(GET_ALL_SALES)
    self.assertEqual(res.status_code, 200)
    self.assertIn("Shoes", str(res.data))

  def test_get_each_sale(self):
    """Test API can get a single sale record by using it's id."""

    res = self.client.post(
        POST_SALES_URL,
        content_type='application/json',
        data=json.dumps(self.sales),
        headers=dict(Authorization="Bearer " + self.login())
    )
    self.assertEqual(res.status_code, 201)
    res = self.client.get(GET_EACH_SALE)
    data = json.loads(res.get_data().decode("UTF-8"))
    self.assertEqual(res.status_code, 200)
    self.assertIn('Shoes', str(res.data))


if __name__ == "__main__":
  unittest.main()
