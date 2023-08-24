from django.contrib import admin

from clube_saber.apps.web.models.product import ProductTag


class ProductTagInlineAdmin(admin.TabularInline):
    model = ProductTag
    extra = 0
