import factory

from clube_saber.apps.web.models.page import Page, Product
from clube_saber.apps.web.models.site import Site


class SiteFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Site


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    price = 200
    number_of_installments = 3


class PageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Page

    slug = factory.Faker('slug')
    title = factory.Faker('catch_phrase')
    subtitle = factory.Faker('sentence', nb_words=200)

    image = factory.django.ImageField(color='blue')
    stamp = factory.django.ImageField(color='yellow')

    product = factory.SubFactory(ProductFactory)
