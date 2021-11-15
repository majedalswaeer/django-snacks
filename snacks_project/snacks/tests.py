from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse
# Create your tests here.

class SnacksTests(SimpleTestCase):
    def test_home_page_status_code(self):
        url=reverse("home")
        response=self.client.get(url)
        self.assertEqual(response.status_code, 200)
        #(actual,expected)
        
    def test_home_page_template(self):
        url=reverse("home")
        response=self.client.get(url)
        self.assertTemplateUsed(response, "home.html")
        #(actual,expected)

    def test_aboutus_page_status_code(self):
        url=reverse("aboutus")
        response=self.client.get(url)
        self.assertEqual(response.status_code, 200)
        #(actual,expected)
        
    def test_aboutus_page_template(self):
        url=reverse("aboutus")
        response=self.client.get(url)
        self.assertTemplateUsed(response, "aboutus.html")
        #(actual,expected)

    def test_base_page_status_code(self):
        url=reverse("base")
        response=self.client.get(url)
        self.assertEqual(response.status_code, 200)
        #(actual,expected)
        
    def test_base_page_template(self):
        url=reverse("aboutus")
        response=self.client.get(url)
        self.assertTemplateUsed(response, "base.html")
        #(actual,expected)