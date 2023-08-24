from django.contrib import admin
from django.utils.html import mark_safe  # type: ignore

from clube_saber.apps.web.admin.inlines.page_admin_inline import (
    PageSectionContentInlineAdmin,
)
from clube_saber.apps.web.models.page import Page


class PageSectionModelAdmin(admin.ModelAdmin):
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
