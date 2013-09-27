from django.conf.urls import patterns, url
from store import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    #   store/products
    url(r'^products/$', views.ProductsView.as_view(), name='Products'),

    #   store/products/id/slug
    url(r'^products/(?P<pk>\d+)/.*$', views.DetailView.as_view(),
        name='Product Detail')

    )
