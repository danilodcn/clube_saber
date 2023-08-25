from django.contrib import admin

from clube_saber.apps.web.admin.inlines.site_admin_inline import (
    GradientSiteThemeInlineAdmin,
    SiteSocialMediaInlineAdmin,
)


class SiteModelAdmin(admin.ModelAdmin):
    inlines = [SiteSocialMediaInlineAdmin]


class SiteThemeModelAdmin(admin.ModelAdmin):
    inlines = [GradientSiteThemeInlineAdmin]
