import random

import factory

from explorer2go.apps.web.models.site import GradientSiteTheme, Site, SiteTheme


class SiteThemeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = SiteTheme

    @factory.post_generation
    def _gradients(self, create, extracted, **kwargs):
        if not create:
            return
        GradientSiteThemeFactory.create_batch(
            random.randint(1, 20), site_theme=self
        )


class GradientSiteThemeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = GradientSiteTheme

    type = factory.Iterator(
        GradientSiteTheme.Type.choices, getter=lambda c: c[0]
    )
    percentage = factory.LazyFunction(lambda *_: random.randrange(0, 100))
    color = factory.Faker('color')


class SiteFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Site

    site_theme = factory.SubFactory(SiteThemeFactory)
