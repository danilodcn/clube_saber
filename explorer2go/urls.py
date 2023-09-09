from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from explorer2go.apps.product import urls as product_urls
from explorer2go.apps.web import urls as web_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(web_urls)),
    path('product/', include(product_urls)),
    path('__debug__/', include('debug_toolbar.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
