from django.conf.urls import patterns, url
from store import views
from django.views import generic
from store.models import Product

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    #   store/products
    url(r'^products/$', views.ProductsView.as_view(), name='Products'),

    #   store/products/id/slug
    url(r'^products/(?P<pk>\d+)/.*$', views.DetailView.as_view(),
        name='Product Detail'),
    url(r'^[-\w]+/C(?P<pk>\d+)/$', views.CategoryView.as_view(),
    name='Category Listing')
)
