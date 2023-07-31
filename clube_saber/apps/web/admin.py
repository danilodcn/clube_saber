from django.contrib import admin

from .models import (
    Page,
    PageSection,
    PageSectionContent,
    Site,
    SiteSocialMedia,
)


class PageSectionContentInlineAdmin(admin.StackedInline):
    model = PageSectionContent
    extra = 0


class SiteSocialMediaInlineAdmin(admin.TabularInline):
    model = SiteSocialMedia
    extra = 0


class PageSectionAdmin(admin.ModelAdmin):
    inlines = [PageSectionContentInlineAdmin]


class PageModelAdmin(admin.ModelAdmin):
    ...


class SiteModelAdmin(admin.ModelAdmin):
    inlines = [SiteSocialMediaInlineAdmin]


admin.site.register(Page, PageModelAdmin)
admin.site.register(Site, SiteModelAdmin)
admin.site.register(PageSection, PageSectionAdmin)
