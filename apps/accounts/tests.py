from django.test import TestCase

class TestLogin(TestCase):
    def setUp(self):
        pass

    def test_login_endpoint(self):
        """Check login endpoint"""
        self.response = self.client.get("/login")
        self.assertEquals(200, self.response.status_code)
        content = self.response.content.decode("utf-8")
        self.assertIn("Login", content)
