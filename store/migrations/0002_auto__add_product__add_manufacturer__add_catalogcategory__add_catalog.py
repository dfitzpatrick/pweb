# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Product'
        db.create_table(u'store_product', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(related_name='products', to=orm['store.CatalogCategory'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=150)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('manufacturer', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Manufacturers', to=orm['store.Manufacturer'])),
            ('price_in_dollars', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('quantity', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('part_number', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('condition', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'store', ['Product'])

        # Adding model 'Manufacturer'
        db.create_table(u'store_manufacturer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal(u'store', ['Manufacturer'])

        # Adding model 'CatalogCategory'
        db.create_table(u'store_catalogcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('catalog', self.gf('django.db.models.fields.related.ForeignKey')(related_name='categories', to=orm['store.Catalog'])),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='children', null=True, to=orm['store.CatalogCategory'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=150)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'store', ['CatalogCategory'])

        # Adding model 'Catalog'
        db.create_table(u'store_catalog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=150)),
            ('publisher', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal(u'store', ['Catalog'])


    def backwards(self, orm):
        # Deleting model 'Product'
        db.delete_table(u'store_product')

        # Deleting model 'Manufacturer'
        db.delete_table(u'store_manufacturer')

        # Deleting model 'CatalogCategory'
        db.delete_table(u'store_catalogcategory')

        # Deleting model 'Catalog'
        db.delete_table(u'store_catalog')


    models = {
        u'store.catalog': {
            'Meta': {'object_name': 'Catalog'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'publisher': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '150'})
        },
        u'store.catalogcategory': {
            'Meta': {'object_name': 'CatalogCategory'},
            'catalog': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'categories'", 'to': u"orm['store.Catalog']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['store.CatalogCategory']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '150'})
        },
        u'store.manufacturer': {
            'Meta': {'object_name': 'Manufacturer'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        u'store.product': {
            'Meta': {'object_name': 'Product'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'products'", 'to': u"orm['store.CatalogCategory']"}),
            'condition': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manufacturer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Manufacturers'", 'to': u"orm['store.Manufacturer']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'part_number': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'price_in_dollars': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '150'})
        }
    }

    complete_apps = ['store']