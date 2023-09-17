from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from explorer2go.apps.web.models.product import Product

from .site import Site

IMAGE_ACCEPT_EXTENSIONS = (
    'png',
    'jpeg',
    'gif',
    'jpg',
    'webp',
    'ico',
    'svg',
)

VIDEO_ACCEPT_EXTENSIONS = ('mp4', 'mov', 'wmv', 'webm')

MEDIA_ACCEPT_EXTENSIONS = *IMAGE_ACCEPT_EXTENSIONS, *VIDEO_ACCEPT_EXTENSIONS

FILE_ACCEPT_EXTENSIONS = (
    *MEDIA_ACCEPT_EXTENSIONS,
    'pdf',
    'xlsx',
    'xls',
    'json',
    'txt',
)


class Page(models.Model):
    slug = models.SlugField(
        _('Slug'), max_length=500, db_index=True, unique=True
    )
    site = models.ForeignKey(
        Site, models.CASCADE, related_name='pages', null=True
    )
    enabled = models.BooleanField('Habilitado', default=True, db_index=True)
    title = models.CharField('Título', max_length=500, null=True, blank=True)
    subtitle = models.TextField('Subtítulo', null=True, blank=True)
    action = models.CharField(
        'Botão de ação', max_length=500, null=True, blank=True
    )
    header_file = models.FileField(
        'Arquivo do header',
        upload_to='upload/page',
        validators=(
            FileExtensionValidator(
                allowed_extensions=MEDIA_ACCEPT_EXTENSIONS,
            ),
        ),
    )
    stamp_file = models.FileField(
        'Arquivo do selo',
        upload_to='upload/page',
        validators=(
            FileExtensionValidator(
                allowed_extensions=IMAGE_ACCEPT_EXTENSIONS,
            ),
        ),
    )
    guarantee_of_satisfaction = models.TextField(
        'Texto de garantia de satisfação', null=True, blank=True
    )
    product = models.ForeignKey(
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
        IMAGE = 1, 'foco na mídia'
        TEXT = 2, 'foco no conteúdo'

    type = models.PositiveSmallIntegerField(
        'Tipo de seção', choices=PageSectionType.choices, db_index=True
    )
    enabled = models.BooleanField('Habilitado', default=True, db_index=True)
    page = models.ForeignKey(
        Page,
        models.CASCADE,
        verbose_name='Página',
        related_name='sections',
        null=False,
        blank=False,
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
    section = models.ForeignKey(
        PageSection,
        models.CASCADE,
        related_name='page_contents',
        null=False,
        blank=False,
    )
    title = models.CharField('Título', max_length=500, null=True, blank=True)
    content = models.TextField('Conteúdo', null=True, blank=True)

    file = models.FileField(
        'Arquivo',
        upload_to='upload/page/section',
        validators=(
            FileExtensionValidator(
                allowed_extensions=FILE_ACCEPT_EXTENSIONS,
            ),
        ),
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
