from django.contrib import admin
from store.models import Catalog, Product, CatalogCategory, Manufacturer

class UncategorizedProduct(Product):
    class Meta:
        proxy = True


class Uncategorized_Product_Admin(admin.ModelAdmin):
    search_fields = ['name']
    list_per_page = 300

    def queryset(self, request):
        return Product.objects.filter(category__name='Uncategorized')


class Categorized_Product_Admin(admin.ModelAdmin):
    class Meta:
        verbose_name = "Categorized Product"
        verbose_name_plural = "Categorized Products"

    search_fields = ['name']
    list_per_page = 300

    def queryset(self, request):
        return Product.objects.exclude(category__name='Uncategorized')

admin.site.register(UncategorizedProduct, Uncategorized_Product_Admin)
admin.site.register(Product, Categorized_Product_Admin)
admin.site.register(Catalog)
admin.site.register(CatalogCategory)
admin.site.register(Manufacturer)
