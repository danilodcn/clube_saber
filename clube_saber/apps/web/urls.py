from django.urls import path

from clube_saber.apps.web.views import home, landing_page

urlpatterns = [
    path('', home),
    path('page/<str:slug>', landing_page),
]
