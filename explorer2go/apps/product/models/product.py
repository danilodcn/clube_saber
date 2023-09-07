import uuid

from django.db import models

from explorer2go.apps.core.types import FileType


class Product(models.Model):
    name = models.CharField('Nome', max_length=250, null=True, blank=False)
    description = models.TextField('Descrição')
    enabled = models.BooleanField('Habilitado', default=True, db_index=True)
    order = models.PositiveSmallIntegerField('ordem', null=True, db_index=True)

    price = models.DecimalField(
        'Preço', decimal_places=2, max_digits=12, null=True
    )
    number_of_installments = models.PositiveSmallIntegerField(
        'Número de parcelas', null=True
    )

    created_at = models.DateTimeField('Data de Criação', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    sku = models.UUIDField(default=uuid.uuid4)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['order', 'pk']

    def __str__(self) -> str:
        return f'{self.name} - {self.number_of_installments}x'


class ProductTag(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='tags'
    )
    name = models.CharField('Nome', max_length=250, null=True, blank=False)
    order = models.PositiveSmallIntegerField('ordem', null=True, db_index=True)

    created_at = models.DateTimeField('Data de Criação', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Tag do produto'
        verbose_name_plural = 'Tags dos produtos'
        ordering = ('order', 'name', 'pk')

    def __str__(self) -> str:
        return f'{self.name}'


class ProductFile(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='files'
    )
    order = models.PositiveSmallIntegerField('ordem', null=True, db_index=True)
    name = models.CharField('Nome', max_length=250, null=True, blank=False)
    file = models.FileField('Arquivo', upload_to='upload/product')
    type = models.CharField(
        'Tipo',
        choices=FileType.choices,
        max_length=20,
        db_index=True,
    )
    created_at = models.DateTimeField('Data de Criação', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Arquivo do produto'
        verbose_name_plural = 'Arquivos dos produtos'
        ordering = ('order', 'name', 'pk')

    def __str__(self) -> str:
        return f'{self.name}'
