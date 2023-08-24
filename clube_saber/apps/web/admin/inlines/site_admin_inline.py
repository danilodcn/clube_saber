from django.contrib import admin

from clube_saber.apps.web.models.site import SiteSocialMedia


class SiteSocialMediaInlineAdmin(admin.TabularInline):
    model = SiteSocialMedia
    extra = 0
