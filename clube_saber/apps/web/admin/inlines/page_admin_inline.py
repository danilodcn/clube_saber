from django.contrib import admin

from clube_saber.apps.web.models.page import PageSectionContent


class PageSectionContentInlineAdmin(admin.StackedInline):
    model = PageSectionContent
    extra = 0
