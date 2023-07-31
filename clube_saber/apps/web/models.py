from django.db import models
from django.utils.translation import gettext_lazy as _


class Site(models.Model):
    logo = models.ImageField('Imagem', null=False, blank=False)
    name = models.CharField('Nome', max_length=250)


class SiteSocialMedia(models.Model):
    site = models.ForeignKey(
        Site, models.CASCADE, related_name='social_medias'
    )
    name = models.CharField('Nome', max_length=250)
    icon = models.CharField('Ícone', max_length=250)
    url = models.URLField('URL')


class Page(models.Model):
    slug = models.SlugField(_('Slug'), max_length=500)
    site = models.ForeignKey(
        Site, models.CASCADE, related_name='pages', null=True
    )
    title = models.CharField('Título', max_length=500, null=True, blank=True)
    subtitle = models.TextField('Subtítulo', null=True, blank=True)
    action = models.CharField(
        'Botão de ação', max_length=500, null=True, blank=True
    )
    price = models.DecimalField(
        'Preço', decimal_places=2, max_digits=12, null=True
    )
    number_of_installments = models.PositiveSmallIntegerField(
        'Número de parcelas', null=True
    )
    image = models.ImageField('Imagem', null=True, blank=True)
    stamp = models.ImageField('Imagem do selo', null=True, blank=True)

    created_at = models.DateTimeField('Data de Criação', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)


class PageSection(models.Model):
    class PageSectionType(models.IntegerChoices):
        IMAGE = 1, 'imagem'
        TEXT = 2, 'texto'

    type = models.PositiveSmallIntegerField(
        'Tipo de seção', choices=PageSectionType.choices
    )
    page = models.ForeignKey(
        Page, models.CASCADE, related_name='sections', null=False, blank=False
    )
    title = models.CharField('Título', max_length=500, null=True, blank=True)
    order = models.PositiveSmallIntegerField('ordem', null=True)

    created_at = models.DateTimeField('Data de Criação', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        ordering = ('order', 'id')


class PageSectionContent(models.Model):
    section = models.ForeignKey(
        PageSection,
        models.CASCADE,
        related_name='page_contents',
        null=False,
        blank=False,
    )
    title = models.CharField('Título', max_length=500, null=True, blank=True)
    content = models.TextField('Conteúdo', null=True, blank=True)
    image = models.ImageField('Imagem', null=True, blank=True)

    action = models.CharField(
        'Botão de ação', max_length=500, null=True, blank=True
    )
    order = models.PositiveSmallIntegerField('ordem', null=True)
    created_at = models.DateTimeField('Data de Criação', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        ordering = ('order', 'id')
