# Create your views here.
from django.http import HttpResponse
from django.views import generic
from django.shortcuts import render
from store.models import CatalogCategory, Product
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render_to_response

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

def listing(request):
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 50)

    page = request.GET.get('page')

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render_to_response('store/products.html', {"product_list": products})

class CategoryView(generic.ListView):
    paginate_by = 50
    template_name = 'store/products.html'

    def get_queryset(self):
        return Product.objects.filter(category__id=self.kwargs['pk'])

class ProductsView(generic.ListView):
    model = Product

    template_name = 'store/products.html'
    paginate_by = 50
    #context_object_name = 'products'
    def get_queryset(self):
        mfg = self.request.GET.get('manufacturer')
        if mfg:
            return Product.objects.filter(manufacturer__name__exact=mfg)
        else:
            return Product.objects.all()
