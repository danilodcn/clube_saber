from django.apps import AppConfig


class ProductConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'explorer2go.apps.product'
    verbose_name = 'Produto'
    verbose_name_plural = 'Produtos'
