from store.models import CatalogCategory
def categories(request):
    return {
        'category_list' : CatalogCategory.objects.all()
    }
