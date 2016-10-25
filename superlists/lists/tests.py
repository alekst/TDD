from django.core.urlresolvers import resolve
from django.test import TestCase
from lists.views import home_page

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        # resolve is an internal function to Django, which resolves URLs to functions (func)
        self.assertEqual(found.func, home_page)
