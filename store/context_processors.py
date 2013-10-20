from store.models import CatalogCategory
def categories(request):
    return {
        'category_list' : CatalogCategory.objects.filter(
                parent__isnull=True).exclude(
                    name__exact="Uncategorized"),
        'subcategory_list': CatalogCategory.objects.filter(parent__gt=0)
    }
