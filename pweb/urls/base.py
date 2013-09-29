from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from store.models import CatalogCategory

admin.autodiscover()

class CustomIndexTemplateView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(CustomIndexTemplateView, self).get_context_data(**kwargs)
        context['CATEGORIES'] = CatalogCategory.objects.all()
        return context


urlpatterns = patterns('',
    # Home Page -- Replace as you prefer
    url(r'^$', CustomIndexTemplateView.as_view(template_name='home.html'),
        name='home'),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^store/', include('store.urls')),
)
