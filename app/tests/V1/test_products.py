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

    def test_post_product(self):
        """TEST whether the API can create a product(POST)"""
        res = self.client.post("/api/v1/products", content_type='application/json', data=json.dumps(self.products))
        data = json.loads(res.get_data().decode("UTF-8"))
        self.assertEqual(res.status_code, 201)

    def test_get_all_products(self):
        res = self.client.post("api/v1/products", content_type='application/json', data=json.dumps(self.products))
        self.assertEqual(res.status_code, 201)
        res = self.client.get("api/v1/products")
        self.assertEqual(res.status_code, 200)
        self.assertIn("James", str(res.data))

    def test_get_each_product(self):
        """Test API can get a single record by using it's id."""
        res = self.client.post('/api/v1/products', content_type='application/json', data=json.dumps(self.products))
        self.assertEqual(res.status_code, 201)
        res = self.client.get("/api/v1/products/1")
        data = json.loads(res.get_data().decode("UTF-8"))
        self.assertEqual(res.status_code, 200)
        self.assertIn('James', str(res.data))


if __name__ == "__main__":
    unittest.main()
