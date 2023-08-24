from django.contrib import admin
from django.urls import include, path

from clube_saber.apps.web import urls as web_urls

urlpatterns = [path('admin/', admin.site.urls), path('', include(web_urls))]


admin.site.site_header = 'Administração Clube Saber'
admin.site.index_title = ''
admin.site.site_title = 'clube saber'
