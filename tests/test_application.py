from importlib import import_module
from unittest import TestCase

from django.core.handlers.wsgi import WSGIHandler


class TestDjangoApplication(TestCase):
    def test_application_has_wsgi_module(self):
        wsgi = import_module('explorer2go.wsgi')
        application = wsgi.application

        self.assertIsInstance(application, WSGIHandler)
