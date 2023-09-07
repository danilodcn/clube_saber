from django.db import models
from django_tenants.models import DomainMixin, TenantMixin
from django.conf import settings


class Tenant(TenantMixin):
    name = models.CharField('Nome', max_length=100)
    favicon = models.ImageField('Ícone', null=True, blank=False)
    manager = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        models.PROTECT,
        verbose_name="Gerente",
        null=True,
        blank=False
    )
    created_at = models.DateTimeField('Data de Criação', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)


class Domain(DomainMixin):
    ...
