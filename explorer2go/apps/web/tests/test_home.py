from django.test import TestCase


class TestHome(TestCase):
    def test_home_page_redirect_to_admin(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/admin')
