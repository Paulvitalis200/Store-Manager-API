import unittest
import json
import sys

from app import create_app


REGISTER_URL = '/api/v1/register'
LOGIN_URL = '/api/v1/login'


class UserTestCase(unittest.TestCase):

    def setUp(self):
        """Setup"""
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.register_user = {"email": "test@live.com", "password": "123456789", "username": "testuser"}
        self.register_user_empty_email = {"email": "", "password": "123456789", "username": "test"}
        self.register_user_invalid_email = {"email": "testlive.com", "password": "123456789", "username": "testuser"}
        self.login_user_empty_email = {"email": "", "password": "123456789"}
        self.login_user_empty_password = {"email": "vitalispaul48@live.com", "password": ""}
        self.register_user_empty_password = {"email": "test@live.com", "password": "", "username": "testuser"}
        self.register_user_short_password = {"email": "test@live.com", "password": "manu", "username": "test"}
        self.register_user_empty_username = {"email": "test@live.com", "password": "123456789", "username": ""}
        self.login_user = {"email": "vitalispaul48@live.com", "password": "manu2012"}

    def test_sign_up_success(self):
        """TEST user can register successfully"""
        res = self.client.post(REGISTER_URL, data=json.dumps(self.register_user),
                               content_type='application/json')
        resp_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 201)
        self.assertEqual(resp_data['message'], 'User was created succesfully!')

    def test_sign_up_empty_email(self):
        """TEST empty email sign up"""
        res = self.client.post(REGISTER_URL, data=json.dumps(self.register_user_empty_email),
                               content_type='application/json')
        resp_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 400)

    def test_sign_up_invalid_email(self):
        """TEST invalid email"""
        res = self.client.post(REGISTER_URL, data=json.dumps(self.register_user_invalid_email),
                               content_type='application/json')
        resp_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 400)

    def test_sign_up_empty_username(self):
        """TEST empty username in signup"""
        res = self.client.post(REGISTER_URL, data=json.dumps(self.register_user_empty_username),
                               content_type='application/json')
        resp_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 400)

    def test_sign_up_empty_password(self):
        """TEST empty sign up password"""
        res = self.client.post(REGISTER_URL, data=json.dumps(self.register_user_empty_password),
                               content_type='application/json')
        resp_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 400)

    def test_sign_up_short_password(self):
        """TEST short sign up password"""
        res = self.client.post(REGISTER_URL, data=json.dumps(self.register_user_short_password),
                               content_type='application/json')
        resp_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 400)

    def test_login_success(self):
        """TEST successful login"""
        res_login = self.client.post(LOGIN_URL, data=json.dumps(self.login_user),
                                     content_type='application/json')
        resp_data = json.loads(res_login.data.decode())
        self.assertTrue(resp_data['access_token'])
        self.assertEqual(res_login.status_code, 200)
        self.assertEqual(resp_data['message'], 'User logged in succesfully!')

    def test_login_empty_email(self):
        """TEST empty email on login"""
        res_login = self.client.post(LOGIN_URL, data=json.dumps(self.login_user_empty_email),
                                     content_type='application/json')

        resp_data = json.loads(res_login.data.decode())
        self.assertEqual(res_login.status_code, 400)

    def test_login_empty_password(self):
        """TEST empty login password"""
        res_login = self.client.post(LOGIN_URL, data=json.dumps(self.login_user_empty_password),
                                     content_type='application/json')
        resp_data = json.loads(res_login.data.decode())
        self.assertEqual(res_login.status_code, 400)
