from django.contrib import admin

from explorer2go.apps.web.models.page import PageSectionContent


class PageSectionContentInlineAdmin(admin.StackedInline):
    model = PageSectionContent
    extra = 0
