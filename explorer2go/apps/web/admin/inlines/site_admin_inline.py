from django.contrib import admin

from explorer2go.apps.web.models.site import GradientSiteTheme, SiteSocialMedia


class SiteSocialMediaInlineAdmin(admin.TabularInline):
    model = SiteSocialMedia
    extra = 0


class GradientSiteThemeInlineAdmin(admin.TabularInline):
    model = GradientSiteTheme
    extra = 0
