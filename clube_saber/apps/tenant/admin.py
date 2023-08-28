from django.contrib import admin
from django_tenants.admin import TenantAdminMixin

from .models import Tenant


@admin.register(Tenant)
class ClientAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'created_at')


def each_context(request):

    context = admin.sites.AdminSite.each_context(admin.site, request)
    try:
        tenant: Tenant = request.tenant
        context['site_header'] = f'Administração {tenant.name}'
        context['site_title'] = f'{tenant.name}'
    except Exception:
        ...
    return context


admin.site.each_context = each_context
