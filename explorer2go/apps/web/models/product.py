from django.db import models


class Product(models.Model):
    name = models.CharField('Nome', max_length=250, null=True, blank=False)
    price = models.DecimalField(
        'Preço', decimal_places=2, max_digits=12, null=True
    )
    number_of_installments = models.PositiveSmallIntegerField(
        'Número de parcelas', null=True
    )

    created_at = models.DateTimeField('Data de Criação', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self) -> str:
        return f'{self.name} - {self.number_of_installments}x'


class ProductTag(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='tags'
    )
    name = models.CharField('Nome', max_length=250, null=True, blank=False)

    created_at = models.DateTimeField('Data de Criação', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self) -> str:
        return f'{self.name}'
