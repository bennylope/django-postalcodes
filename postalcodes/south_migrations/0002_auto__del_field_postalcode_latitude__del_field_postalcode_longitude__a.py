# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'PostalCode.latitude'
        db.delete_column('postalcodes_postalcode', 'latitude')

        # Deleting field 'PostalCode.longitude'
        db.delete_column('postalcodes_postalcode', 'longitude')

        # Adding field 'PostalCode.location'
        db.add_column('postalcodes_postalcode', 'location',
                      self.gf('django.contrib.gis.db.models.fields.PointField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'PostalCode.latitude'
        db.add_column('postalcodes_postalcode', 'latitude',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=9, decimal_places=6, blank=True),
                      keep_default=False)

        # Adding field 'PostalCode.longitude'
        db.add_column('postalcodes_postalcode', 'longitude',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=9, decimal_places=6, blank=True),
                      keep_default=False)

        # Deleting field 'PostalCode.location'
        db.delete_column('postalcodes_postalcode', 'location')


    models = {
        'postalcodes.postalcode': {
            'Meta': {'object_name': 'PostalCode'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['postalcodes']