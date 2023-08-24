from django.contrib import admin

from clube_saber.apps.web.models.contact import Contact
from clube_saber.apps.web.models.page import Page, PageSection
from clube_saber.apps.web.models.site import Site

from .contact_admin import ContactModelAdmin
from .page_admin import PageModelAdmin, PageSectionModelAdmin
from .site_admin import SiteModelAdmin

admin.site.register(Contact, ContactModelAdmin)
admin.site.register(Page, PageModelAdmin)
admin.site.register(Site, SiteModelAdmin)
admin.site.register(PageSection, PageSectionModelAdmin)
