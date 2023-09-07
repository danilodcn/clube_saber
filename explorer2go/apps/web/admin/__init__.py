from django.contrib import admin

from explorer2go.apps.web.models.contact import Contact
from explorer2go.apps.web.models.page import Page, PageSection
from explorer2go.apps.web.models.product import Product
from explorer2go.apps.web.models.site import Site, SiteTheme

from .contact_admin import ContactModelAdmin
from .page_admin import PageModelAdmin, PageSectionModelAdmin
from .product_admin import ProductModelAdmin
from .site_admin import SiteModelAdmin, SiteThemeModelAdmin

admin.site.register(SiteTheme, SiteThemeModelAdmin)

admin.site.register(Contact, ContactModelAdmin)
admin.site.register(Page, PageModelAdmin)
admin.site.register(PageSection, PageSectionModelAdmin)
admin.site.register(Product, ProductModelAdmin)
admin.site.register(Site, SiteModelAdmin)
