from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from clube_saber.apps.web import urls as web_urls

urlpatterns = [path('admin/', admin.site.urls), path('', include(web_urls))]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
