from import_export import admin, fields, resources

from clube_saber.apps.web.models.contact import Contact


class ContactResource(resources.ModelResource):
    class Meta:
        model = Contact
        exclude = ['updated_at']
        export_order = ['id', 'email', 'reason', 'page', 'page_url']

    reason = fields.Field('get_reason_display', 'tipo')
    page = fields.Field('page__title', 'página')
    page_url = fields.Field('page__slug', 'url da página')

    @classmethod
    def get_display_name(cls):
        return 'Exportação padrão'

    def dehydrate_page_url(self, obj: Contact):
        return f'page/{obj.page.slug}'


class ContactModelAdmin(admin.ExportMixin, admin.admin.ModelAdmin):
    resource_classes = (ContactResource,)
    list_display = ('__str__', 'created_at')
    list_filter = ('created_at',)
