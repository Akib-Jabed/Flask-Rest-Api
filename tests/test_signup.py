import json
from tests.base_case import BaseCase


class SignUpTest(BaseCase):

    def test_successful_signup(self):
        payload = json.dumps({
            "email": "admin@email.com",
            "password": "123456"
        })

        response = self.app.post('/api/auth/signup',
                                 headers={"Content-Type": "application/json"},
                                 data=payload)
        self.assertEqual(str, type(response.json['id']))
        self.assertEqual(200, response.status_code)
