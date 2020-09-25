from django.test import SimpleTestCase
from django.urls import reverse, resolve
from conversations.views import home, search

class TestUrls(SimpleTestCase):
    def test_list_url_is_resolved(self):
        url = reverse('home')
        print(resolve(url))
        self.assertEquals(resolve(url).func, home)

class TestUrls(SimpleTestCase):
    def test_list_url_is_resolved(self):
        url = reverse('search')
        print(resolve(url))
        self.assertEquals(resolve(url).func, search)