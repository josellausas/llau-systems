from django.test import (TestCase, Client)

class LlauSysHomeTests(TestCase):
    def setUp(self):
        self.response = self.client.get("/")

    def test_home_exists(self):
        self.assertEquals(200, self.response.status_code)

    def test_home_menu(self):
        """Check that all menu options exist"""
        # Check that the rendered context contains 5 customers.
        # self.assertEqual(len(response.context['customers']), 5)
        content = self.response.content.decode("utf-8")
        self.assertIn("Home", content)
        self.assertIn("Services", content)
        self.assertIn("Projects", content)
        self.assertIn("Technologies", content)
        self.assertIn("Blog", content)
        self.assertIn("Contact", content)

class LlauSysServicesTests(TestCase):
    def setUp(self):
        self.response = self.client.get("/services", follow=True)

    def test_services_exists(self):
        self.assertEquals(200, self.response.status_code)

    def test_services_content(self):
        """Check that all menu options exist"""
        # Check that the rendered context contains 5 customers.
        # self.assertEqual(len(response.context['customers']), 5)
        content = self.response.content.decode("utf-8")
        self.assertIn("Services", content)