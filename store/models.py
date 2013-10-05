from django.db import models
from datetime import datetime
# Create your models here.
class Catalog(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=150)
    publisher = models.CharField(max_length=300)
    description = models.TextField()
    pub_date = models.DateTimeField(default=datetime.now)

    def __unicode__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey('CatalogCategory',  related_name='products')
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=150)
    description = models.TextField()
    photo = models.ImageField(upload_to='product_photo', blank=True)
    manufacturer = models.ForeignKey('Manufacturer', related_name='Manufacturers')
    #manufacturer = models.CharField(max_length=300, blank=True)
    price_in_dollars = models.DecimalField(max_digits=6,  decimal_places=2)
    quantity = models.IntegerField(default=0)
    part_number = models.CharField(max_length=100)
    condition = models.CharField(max_length=100)


    def __unicode__(self):
        return "%s - %s" % (self.name, self.manufacturer)

class CatalogCategory(models.Model):
    catalog = models.ForeignKey('Catalog', related_name='categories')
    parent = models.ForeignKey('self', blank=True, null=True,
                             related_name='children')
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=150)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='category_photo', blank=True, null=True)
    is_featured = models.BooleanField(blank=True, default=False)

    def __unicode__(self):
        if self.parent:
            return u'%s: %s - %s' % (self.catalog.name, self.parent.name, self.name)
        return u'%s: %s' % (self.catalog.name, self.name)

class Manufacturer(models.Model):
    name = models.CharField(max_length=300)

    def __unicode__(self):
        return self.name
