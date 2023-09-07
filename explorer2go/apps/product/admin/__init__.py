from django.contrib import admin

from explorer2go.apps.product.models.product import Product

from .product_admin import ProductModelAdmin

admin.site.register(Product, ProductModelAdmin)
