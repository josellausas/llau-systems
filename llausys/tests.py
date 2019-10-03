from django.test import TestCase, Client


class LlauSysHomeTests(TestCase):
    def setUp(self):
        self.response = self.client.get("/")

    def test_home_menu(self):
        """Check that all menu options exist"""
        # Check that the rendered context contains 5 customers.
        # self.assertEqual(len(response.context['customers']), 5)
        self.assertEquals(200, self.response.status_code)
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
        self.content = self.response.content.decode("utf-8")

    def test_url_regex(self):
        """Also responds to service/"""
        response = self.client.get("/service", follow=True)
        self.assertEquals(200, response.status_code)

    def test_services_content(self):
        """Check that all menu options exist"""
        self.assertEquals(200, self.response.status_code)
        self.assertIn("Services", self.content)

    def test_context(self):
        self.assertIn('Services', self.response.context['title'])


class LlauSysProjectsTests(TestCase):
    def setUp(self):
        self.response = self.client.get("/projects", follow=True)

    def test_url_regex(self):
        """Also responds to project/"""
        response = self.client.get("/project", follow=True)
        self.assertEquals(200, response.status_code)

    def test_projects_content(self):
        """Check that all menu options exist"""
        self.assertEquals(200, self.response.status_code)
        content = self.response.content.decode("utf-8")
        self.assertIn("Projects</h2>", content)


class LlauSysTechnologiesTests(TestCase):
    def setUp(self):
        self.response = self.client.get("/tech", follow=True)

    def test_tech_content(self):
        """Check that all menu options exist"""
        # Check that the rendered context contains 5 customers.
        # self.assertEqual(len(response.context['customers']), 5)
        self.assertEquals(200, self.response.status_code)
        content = self.response.content.decode("utf-8")
        self.assertIn("Technologies</h2>", content)


class LlauSysBlogTests(TestCase):
    def setUp(self):
        self.response = self.client.get("/blog", follow=True)

    def test_tech_content(self):
        """Check that all menu options exist"""
        # Check that the rendered context contains 5 customers.
        # self.assertEqual(len(response.context['customers']), 5)
        self.assertEquals(200, self.response.status_code)
        content = self.response.content.decode("utf-8")
        self.assertIn("Blog</h2>", content)


class LlauSysContactTests(TestCase):
    def setUp(self):
        self.response = self.client.get("/contact", follow=True)

    def test_tech_content(self):
        """Check that all menu options exist"""
        # Check that the rendered context contains 5 customers.
        # self.assertEqual(len(response.context['customers']), 5)
        self.assertEquals(200, self.response.status_code)
        content = self.response.content.decode("utf-8")
        self.assertIn("Contact</h2>", content)
