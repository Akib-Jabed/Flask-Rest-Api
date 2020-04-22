import json
from tests.base_case import BaseCase


class UserLoginTest(BaseCase):

    def test_successful_login(self):
        email = "admin@email.com"
        password = "123456"
        payload = json.dumps({
            "email": email,
            "password": password
        })
        self.app.post('/api/auth/signup',
                      headers={"Content-Type": "application/json"},
                      data=payload)
        response = self.app.post('/api/auth/login',
                                 headers={"Content-Type": "application/json"},
                                 data=payload)

        self.assertEqual(str, type(response.json['token']))
        self.assertEqual(200, response.status_code)
