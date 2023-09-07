from django.contrib.auth.models import User
from django.test import SimpleTestCase

from explorer2go.apps.web.models.page import Page

from .factories.product_factories import PageFactory


class TestCreateContact(SimpleTestCase):
    @classmethod
    def setUpClass(cls):
        cls.page: Page = PageFactory.create()

    def test_access_page(self):
        response = self.client.get(f'/page/{self.page.slug}')
        self.assertEqual(response.status_code, 200)

    def test_user_logged_should_be_back_office_link_enabled(self):
        user = User.objects.create(
            username='test', email='test@test.org', is_staff=True
        )
        user.set_password('123')
        user.save()

        self.client.force_login(user)
        response = self.client.get(f'/page/{self.page.slug}')
        excepted = """
            <span class="px-1">
            Backoffice
            </span>
        """
        self.assertEqual(response.status_code, 200)
        self.assertInHTML(excepted, response.content.decode())

    def test_should_be_back_office_link_disabled(self):
        self.client.logout()
        response = self.client.get(f'/page/{self.page.slug}')
        excepted = 'Backoffice'
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(excepted, response.content.decode())
