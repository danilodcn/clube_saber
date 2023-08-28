from django.contrib import admin
from django_tenants.admin import TenantAdminMixin

from .models import Client


@admin.register(Client)
class ClientAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'created_at')


def each_context(request):
    from clube_saber.apps.tenant.models import Client

    context = admin.sites.AdminSite.each_context(admin.site, request)
    tenant: Client = request.tenant
    context['site_header'] = f'Administração {tenant.name}'
    context['site_title'] = f'{tenant.name}'
    return context


admin.site.each_context = each_context
