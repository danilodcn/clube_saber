from import_export.admin import ImportExportModelAdmin

from clube_saber.apps.web.admin.inlines.product_tags_inline import (
    ProductTagInlineAdmin,
)


class ProductModelAdmin(ImportExportModelAdmin):
    inlines = (ProductTagInlineAdmin,)
