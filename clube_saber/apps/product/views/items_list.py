from django.views.generic import ListView

from ..models.product import Product


class ProductListView(ListView):
    model = Product
    queryset = Product.objects.filter(enabled=True)
