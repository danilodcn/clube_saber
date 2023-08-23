from django.db import models


class Site(models.Model):
    logo = models.ImageField(
        'Imagem', null=False, blank=False, upload_to='upload/site'
    )
    name = models.CharField('Nome', max_length=250)
    enabled = models.BooleanField(
        'Habilitado', null=True, blank=True, db_index=True
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
    enabled = models.BooleanField(
        'Habilitado', null=True, blank=True, db_index=True
    )

    created_at = models.DateTimeField('Data de Criação', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Mídia social'
        verbose_name_plural = 'Mídias sociais'

    def __str__(self) -> str:
        return f'{self.name}'
