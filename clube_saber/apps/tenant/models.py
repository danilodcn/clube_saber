from django.db import models
from django_tenants.models import DomainMixin, TenantMixin


class Tenant(TenantMixin):
    name = models.CharField('Nome', max_length=100)

    created_at = models.DateTimeField('Data de Criação', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)


class Domain(DomainMixin):
    ...
