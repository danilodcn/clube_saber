from django.test import SimpleTestCase

from clube_saber.apps.web.models.page import Page

from .factories import PageFactory


class TestCreateContact(SimpleTestCase):
    @classmethod
    def setUpClass(cls):
        cls.page: Page = PageFactory.create()

    def test_access_page(self):
        response = self.client.get(f'/page/{self.page.slug}')
        self.assertEqual(response.status_code, 200)
