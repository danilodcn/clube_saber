import random

import factory

from clube_saber.apps.web.models.page import Page, Product
from clube_saber.apps.web.models.product import ProductTag
from clube_saber.apps.web.models.site import Site


class SiteFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Site


class ProductTagFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductTag

    name = factory.Faker('sentence', nb_words=4)


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Faker('catch_phrase')
    price = factory.LazyFunction(lambda *_: random.randrange(1, 200))
    number_of_installments = factory.LazyFunction(
        lambda *_: random.randint(1, 30)
    )

    @factory.post_generation
    def groups(self, create, extracted, **kwargs):
        if not create:
            return
        ProductTagFactory.create_batch(random.randint(1, 10), product=self)


class PageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Page

    slug = factory.Faker('slug')
    title = factory.Faker('catch_phrase')
    subtitle = factory.Faker('sentence', nb_words=200)

    image = factory.django.ImageField(color='blue')
    stamp = factory.django.ImageField(color='yellow')

    product = factory.SubFactory(ProductFactory)
