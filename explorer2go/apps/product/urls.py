from django.urls import path

from .views.items_list import ProductListView

urlpatterns = [
    path('list', ProductListView.as_view()),
]
