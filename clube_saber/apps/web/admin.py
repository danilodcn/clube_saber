from django.contrib import admin
from django.utils.html import mark_safe  # type: ignore

from .models import (
    Contact,
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
    readonly_fields = ('get_page_url',)
    list_display = ('__str__', 'get_page_url')

    @mark_safe
    @admin.decorators.display(description='url')
    def get_page_url(self, obj: Page):
        return '<a href="/{base}/{slug}">/{base}/{slug}</a>'.format(
            base='page', slug=obj.slug
        )


class SiteModelAdmin(admin.ModelAdmin):
    inlines = [SiteSocialMediaInlineAdmin]


admin.site.register(Contact)
admin.site.register(Page, PageModelAdmin)
admin.site.register(Site, SiteModelAdmin)
admin.site.register(PageSection, PageSectionAdmin)
