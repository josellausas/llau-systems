from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class LlauSysAuthToken(TestCase):
    def setUp(self):
        self.url = reverse('api_token')
        self.user = User.objects.create_user('foo', 'myemail@test.com', 'bar')

    def test_get_not_allowed(self):
        """Check that all menu options exist"""
        response = self.client.get(self.url, follow=True)
        self.assertEquals(405, response.status_code)

    def test_post_returns_token(self):
        response = self.client.post(
            self.url,
            {'username': 'foo', 'password': 'bar'},
            follow=True
        )
        self.assertEquals(200, response.status_code)
        self.assertIsNotNone(response.json()['token'])

    def test_invalid_auth_no_token(self):
        response = self.client.post(
            self.url,
            {'username': 'foo', 'password': 'baz'},
            follow=True
        )
        self.assertEquals(400, response.status_code)
        self.assertTrue('token' not in response.json())
