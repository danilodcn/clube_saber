from django.contrib import admin

from .models import Domain, Tenant

# from django_tenants.admin import TenantAdminMixin


class DomainInlineAdmin(admin.TabularInline):
    model = Domain
    extra = 0


@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    inlines = (DomainInlineAdmin,)


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
