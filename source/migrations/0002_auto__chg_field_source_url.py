# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Source.url'
        db.alter_column(u'source_source', 'url', self.gf('django.db.models.fields.URLField')(max_length=200))

    def backwards(self, orm):

        # Changing field 'Source.url'
        db.alter_column(u'source_source', 'url', self.gf('django.db.models.fields.CharField')(max_length=100))

    models = {
        u'source.source': {
            'Meta': {'object_name': 'Source'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['source']