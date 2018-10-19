import unittest
import json

from app import create_app


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.sales = {"name": "Shoes", "price": 2000}

    def test_post_sales(self):
        """TEST an API can create a sale record(POST)"""
        res = self.client.post("/api/v1/sales", content_type='application/json', data=json.dumps(self.sales))
        data = json.loads(res.get_data().decode("UTF-8"))
        self.assertEqual(res.status_code, 201)

    def test_get_all_sales(self):
        res = self.client.post("api/v1/sales", content_type='application/json', data=json.dumps(self.sales))
        self.assertEqual(res.status_code, 201)
        res = self.client.get("api/v1/sales")
        self.assertEqual(res.status_code, 200)
        self.assertIn("Shoes", str(res.data))

    def test_get_each_sale(self):
        """Test API can get a single sale record by using it's id."""

        res = self.client.post('/api/v1/sales', content_type='application/json', data=json.dumps(self.sales))
        self.assertEqual(res.status_code, 201)
        res = self.client.get("/api/v1/sales/1")
        data = json.loads(res.get_data().decode("UTF-8"))
        self.assertEqual(res.status_code, 200)
        self.assertIn('Shoes', str(res.data))


if __name__ == "__main__":
    unittest.main()
