import json
from tests.base_case import BaseCase


class MovieCreationTest(BaseCase):

    def test_successful_movie_create(self):
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
        login_token = response.json['token']

        movie_payload = {
            "name": "Star Wars: The Rise of Skywalker",
            "casts": ["Daisy Ridley", "Adam Driver"],
            "genres": ["Fantasy", "Sci-fi"]
        }

        response = self.app.post('/api/movies',
                                 headers={"Content-Type": "application/json",
                                          "Authorization": f"Bearer {login_token}"},
                                 data=json.dumps(movie_payload))

        self.assertEqual(str, type(response.json['id']))
        self.assertEqual(200, response.status_code)
