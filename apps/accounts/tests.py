from django.test import TestCase

class TestLogin(TestCase):
    def setUp(self):
        pass

    def test_signup_endpoint(self):
        """Check signup endpoint"""
        self.response = self.client.get("/signup", follow=True)
        self.assertEquals(200, self.response.status_code)
        content = self.response.content.decode("utf-8")
        self.assertIn("Signup", content)

    def test_login_endpoint(self):
        """Check login endpoint"""
        self.response = self.client.get("/login", follow=True)
        self.assertEquals(200, self.response.status_code)
        content = self.response.content.decode("utf-8")
        self.assertIn("Login", content)

    def test_logout_endpoint(self):
        """Check logout endpoint"""
        self.response = self.client.get("/logout", follow=True)
        self.assertEquals(200, self.response.status_code)
        content = self.response.content.decode("utf-8")
        self.assertIn("Logout", content)
