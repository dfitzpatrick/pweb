from django.contrib import admin
from store.models import Catalog, Product, CatalogCategory, Manufacturer

admin.site.register(Catalog)
admin.site.register(Product)
admin.site.register(CatalogCategory)
admin.site.register(Manufacturer)
