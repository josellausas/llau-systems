from django.test import TestCase, Client

from bs4 import BeautifulSoup
import re



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
        # self.assertIn("Services", content)
        # self.assertIn("Technologies", content)
        # self.assertIn("Open Source", content)

    def test_links(self):
        # Grab all the links from the homepage
        res = self.client.get("/")
        self.assertEqual(200, res.status_code)
        soup = BeautifulSoup(res.content, 'html.parser')
        
        # Check that all links work
        checked = {}
        for link in soup.find_all('a'):
            url = link.get('href')
            if (url is not None) and ("http" not in url):
                if url not in checked:
                    response = self.client.get(url, follow=True)
                    checked[url] = response.status_code
                    self.assertEqual(
                        200, 
                        response.status_code, 
                        f"Failed to GET {link.get('href')}"
                )


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
    
    def test_links(self):
        # Grab all the links from the homepage
        res = self.client.get("/services", follow=True)
        self.assertEqual(200, res.status_code)
        soup = BeautifulSoup(res.content, 'html.parser')
        
        # Check that all links work
        checked = {}
        for link in soup.find_all('a'):
            url = link.get('href')
            if (url is not None) and ("http" not in url):
                if url not in checked:
                    response = self.client.get(url, follow=True)
                    checked[url] = response.status_code
                    self.assertEqual(
                        200, 
                        response.status_code, 
                        f"Failed to GET {link.get('href')}"
                )


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
        self.assertIn("Projects", content)

    def test_context(self):
        self.assertIn('Projects', self.response.context['title'])

    def test_links(self):
        # Grab all the links from the homepage
        res = self.client.get("/projects", follow=True)
        self.assertEqual(200, res.status_code)
        soup = BeautifulSoup(res.content, 'html.parser')
        
        # Check that all links work
        checked = {}
        for link in soup.find_all('a'):
            url = link.get('href')
            if (url is not None) and ("http" not in url):
                if url not in checked:
                    response = self.client.get(url, follow=True)
                    checked[url] = response.status_code
                    self.assertEqual(
                        200, 
                        response.status_code, 
                        f"Failed to GET {link.get('href')}"
                )


class LlauSysTechnologiesTests(TestCase):
    def setUp(self):
        self.response = self.client.get("/tech", follow=True)

    def test_tech_content(self):
        """Check that all menu options exist"""
        # Check that the rendered context contains 5 customers.
        # self.assertEqual(len(response.context['customers']), 5)
        self.assertEquals(200, self.response.status_code)
        content = self.response.content.decode("utf-8")
        self.assertIn("Technologies", content)

    def test_context(self):
        self.assertIn('Technologies', self.response.context['title'])


class LlauSysBlogTests(TestCase):
    def setUp(self):
        self.response = self.client.get("/blog", follow=True)

    def test_tech_content(self):
        """Check that all menu options exist"""
        # Check that the rendered context contains 5 customers.
        # self.assertEqual(len(response.context['customers']), 5)
        self.assertEquals(200, self.response.status_code)
        content = self.response.content.decode("utf-8")
        self.assertIn("Blog", content)

    def test_context(self):
        self.assertIn('Blog', self.response.context['title'])


class LlauSysContactTests(TestCase):
    def setUp(self):
        self.response = self.client.get("/contact", follow=True)

    def test_tech_content(self):
        """Check that all menu options exist"""
        # Check that the rendered context contains 5 customers.
        # self.assertEqual(len(response.context['customers']), 5)
        self.assertEquals(200, self.response.status_code)
        content = self.response.content.decode("utf-8")
        self.assertIn("Contact", content)

    def test_context(self):
        self.assertIn('Contact', self.response.context['title'])
