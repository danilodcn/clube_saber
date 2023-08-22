from django.db import models
from django.utils.translation import gettext_lazy as _


class Site(models.Model):
    logo = models.ImageField(
        'Imagem', null=False, blank=False, upload_to='upload/site'
    )
    name = models.CharField('Nome', max_length=250)

    def __str__(self) -> str:
        return f'{self.name}'


class SiteSocialMedia(models.Model):
    site = models.ForeignKey(
        Site, models.CASCADE, related_name='social_medias'
    )
    name = models.CharField('Nome', max_length=250)
    icon = models.CharField('Ícone', max_length=250)
    url = models.URLField('URL')

    class Meta:
        verbose_name = 'Mídia social'
        verbose_name_plural = 'Mídias sociais'

    def __str__(self) -> str:
        return f'{self.name}'


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
    price = models.DecimalField(
        'Preço', decimal_places=2, max_digits=12, null=True
    )
    number_of_installments = models.PositiveSmallIntegerField(
        'Número de parcelas', null=True
    )
    image = models.ImageField(
        'Imagem', null=True, blank=True, upload_to='upload/page'
    )
    stamp = models.ImageField(
        'Imagem do selo', null=True, blank=True, upload_to='upload/page'
    )

    created_at = models.DateTimeField('Data de Criação', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Página'
        verbose_name_plural = 'Páginas'

    def __str__(self) -> str:
        return f'página: {self.title}'


class Contact(models.Model):
    class ReasonChoices(models.IntegerChoices):
        UNKNOWN = 1, 'Desconhecido'
        DOUBT = 2, 'Dúvida'
        SUGGESTION = 3, 'Sugestão'
        CRITICIZE = 4, 'Crítica'

    page = page = models.ForeignKey(
        Page, models.CASCADE, related_name='contacts', null=False, blank=False
    )
    email = models.CharField('Email', max_length=250, null=True, blank=False)
    reason = models.PositiveSmallIntegerField(
        'Rasão', choices=ReasonChoices.choices
    )
    message = models.TextField('Mensagem')

    created_at = models.DateTimeField('Data de Criação', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'

    def __str__(self):
        return f'{self.pk} - {self.email}'


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
    order = models.PositiveSmallIntegerField('ordem', null=True, db_index=True)

    created_at = models.DateTimeField('Data de Criação', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        ordering = ('order', 'id')
        verbose_name = 'Seção da página'
        verbose_name_plural = 'Seções das páginas'

    def __str__(self) -> str:
        return f'{self.title} ({self.get_type_display()})'


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
    image = models.ImageField(
        'Imagem', null=True, blank=True, upload_to='upload/page/section'
    )

    action = models.CharField(
        'Botão de ação', max_length=500, null=True, blank=True
    )
    order = models.PositiveSmallIntegerField('ordem', null=True, db_index=True)
    created_at = models.DateTimeField('Data de Criação', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        ordering = ('order', 'id')
        verbose_name = 'Conteúdo da página'
        verbose_name_plural = 'Conteúdos das páginas'
