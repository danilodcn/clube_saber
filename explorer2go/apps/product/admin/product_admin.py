from django.contrib import admin

from explorer2go.apps.product.models.product import (
    Product,
    ProductFile,
    ProductTag,
)


class ProductTagInlineAdmin(admin.TabularInline):
    model = ProductTag
    extra = 0


class ProductFileInlineAdmin(admin.TabularInline):
    model = ProductFile
    extra = 0


class ProductModelAdmin(admin.ModelAdmin):
    model = Product
    inlines = (
        ProductTagInlineAdmin,
        ProductFileInlineAdmin,
    )
    list_display = ('id', '__str__', 'order')
    list_display_links = ('id', '__str__')
    list_filter = ('enabled', 'order')
    list_editable = ('order',)
