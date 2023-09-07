from django.contrib import admin

from explorer2go.apps.web.models.product import ProductTag


class ProductTagInlineAdmin(admin.TabularInline):
    model = ProductTag
    extra = 0
