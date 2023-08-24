from django.contrib import admin

from clube_saber.apps.web.admin.inlines.site_admin_inline import (
    SiteSocialMediaInlineAdmin,
)


class SiteModelAdmin(admin.ModelAdmin):
    inlines = [SiteSocialMediaInlineAdmin]
