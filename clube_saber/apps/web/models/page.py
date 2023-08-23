from django.db import models
from django.utils.translation import gettext_lazy as _

from .site import Site


class Product(models.Model):
    price = models.DecimalField(
        'Preço', decimal_places=2, max_digits=12, null=True
    )
    number_of_installments = models.PositiveSmallIntegerField(
        'Número de parcelas', null=True
    )


class Page(models.Model):
    slug = models.SlugField(_('Slug'), max_length=500, db_index=True)
    site = models.ForeignKey(
        Site, models.CASCADE, related_name='pages', null=True
    )
    title = models.CharField('Título', max_length=500, null=True, blank=True)
    subtitle = models.TextField('Subtítulo', null=True, blank=True)
    action = models.CharField(
        'Botão de ação', max_length=500, null=True, blank=True
    )
    image = models.ImageField(
        'Imagem',
        null=False,
        blank=False,
        upload_to='upload/page',
    )
    stamp = models.ImageField(
        'Imagem do selo', null=True, blank=True, upload_to='upload/page'
    )

    product = models.OneToOneField(
        Product, on_delete=models.PROTECT, null=True, blank=False
    )

    created_at = models.DateTimeField('Data de Criação', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Página'
        verbose_name_plural = 'Páginas'

    def __str__(self) -> str:
        return f'página: {self.title}'


class PageSection(models.Model):
    class PageSectionType(models.IntegerChoices):
        IMAGE = 1, 'imagem'
        TEXT = 2, 'texto'

    type = models.PositiveSmallIntegerField(
        'Tipo de seção', choices=PageSectionType.choices, db_index=True
    )
    page = models.ForeignKey(
        Page, models.CASCADE, related_name='sections', null=False, blank=False
    )
    title = models.CharField('Título', max_length=500, null=True, blank=True)
    order = models.PositiveSmallIntegerField('ordem', null=True, db_index=True)

    created_at = models.DateTimeField('Data de Criação', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        ordering = ('order', 'id')
        verbose_name = 'Seção da página'
        verbose_name_plural = 'Seções das páginas'

    def __str__(self) -> str:
        return f'{self.title} ({self.get_type_display()})'  # type: ignore


class PageSectionContent(models.Model):
    class PageSectionFileType(models.IntegerChoices):
        IMAGE = 1, 'imagem'
        VIDEO = 2, 'video'

    section = models.ForeignKey(
        PageSection,
        models.CASCADE,
        related_name='page_contents',
        null=False,
        blank=False,
    )
    title = models.CharField('Título', max_length=500, null=True, blank=True)
    content = models.TextField('Conteúdo', null=True, blank=True)
    type = models.PositiveSmallIntegerField(
        'Tipo de conteúdo', choices=PageSectionFileType.choices, db_index=True
    )
    file = models.FileField(
        'Arquivo', null=True, blank=True, upload_to='upload/page/section'
    )
    action = models.CharField(
        'Botão de ação', max_length=500, null=True, blank=True
    )
    enabled = models.BooleanField('Habilitado', default=False, db_index=True)
    order = models.PositiveSmallIntegerField('ordem', null=True, db_index=True)
    created_at = models.DateTimeField('Data de Criação', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        ordering = ('order', 'id')
        verbose_name = 'Conteúdo da página'
        verbose_name_plural = 'Conteúdos das páginas'
