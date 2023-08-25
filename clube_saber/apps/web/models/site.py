from dataclasses import dataclass
from decimal import Decimal
from functools import cached_property

from colorfield.fields import ColorField
from django.core import validators
from django.db import models


@dataclass
class Gradient:
    color: str
    percentage: Decimal


class SiteTheme(models.Model):
    primary_color = ColorField('Cor primária')
    secondary_color = ColorField('Cor secundária')
    error_color = ColorField('Cor Erro')

    created_at = models.DateTimeField('Data de Criação', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Tema do site'
        verbose_name_plural = 'Temas do site'

    def __str__(self) -> str:
        return f'{self.pk} - tema do site'

    @cached_property
    def gradients(self):
        from clube_saber.apps.web.functools.list_gradients import (
            list_gradients,
        )

        return list_gradients(self)


class GradientSiteTheme(models.Model):
    class Type(models.enums.TextChoices):
        primary = 'primary', 'Primário'
        button = 'button', 'Botão'

    site_theme = models.ForeignKey(SiteTheme, models.CASCADE)
    type = models.CharField(
        'Tipo', choices=Type.choices, max_length=10, db_index=True
    )
    color = ColorField('Cor')
    percentage = models.DecimalField(
        'Porcentagem',
        max_digits=5,
        decimal_places=2,
        validators=(
            validators.MaxValueValidator(100),
            validators.MinValueValidator(0),
        ),
    )
    created_at = models.DateTimeField('Data de Criação', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Gradiente do site'
        verbose_name_plural = 'Gradientes do site'
        ordering = ('type', 'percentage')

    def __str__(self) -> str:
        return f'{self.pk} - tema do site'


class Site(models.Model):
    logo = models.ImageField(
        'Imagem', null=False, blank=False, upload_to='upload/site'
    )
    name = models.CharField('Nome', max_length=250)
    enabled = models.BooleanField('Habilitado', default=True, db_index=True)
    site_theme = models.ForeignKey(
        SiteTheme, models.CASCADE, related_name='site'
    )

    created_at = models.DateTimeField('Data de Criação', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self) -> str:
        return f'{self.name}'


class SiteSocialMedia(models.Model):
    site = models.ForeignKey(
        Site, models.CASCADE, related_name='social_medias'
    )
    name = models.CharField('Nome', max_length=250)
    icon = models.CharField('Ícone', max_length=250)
    url = models.URLField('URL')
    enabled = models.BooleanField('Habilitado', default=True, db_index=True)

    created_at = models.DateTimeField('Data de Criação', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Mídia social'
        verbose_name_plural = 'Mídias sociais'

    def __str__(self) -> str:
        return f'{self.name}'
