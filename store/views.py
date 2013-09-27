# Create your views here.
from django.http import HttpResponse
from django.views import generic
from django.shortcuts import render
from store.models import CatalogCategory, Product

def index(request):
    cc_list = CatalogCategory.objects.all()
    context = {'cc_list': cc_list,  'fuu': 'fuuuu!!!'}
    return render(request, 'store/categories.html', context)

def products(request):
    products = Product.objects.all()
    context = {'products': products }

    return render(request, 'store/products.html', context)


class DetailView(generic.DetailView):
    model = Product
    template_name = 'store/product_detail.html'

class ProductsView(generic.ListView):
    model = Product

    template_name = 'store/products.html'
    #context_object_name = 'products'
    def get_queryset(self):
        mfg = self.request.GET.get('manufacturer')
        if mfg:
            return Product.objects.filter(manufacturer__name__exact=mfg)
        else:
            return Product.objects.all()
