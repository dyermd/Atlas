# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'File.date'
        db.add_column(u'file_file', 'date',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 6, 4, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'File.date'
        db.delete_column(u'file_file', 'date')


    models = {
        u'file.file': {
            'Meta': {'object_name': 'File'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'file_path': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'file_type': ('django.db.models.fields.CharField', [], {'default': "'BAM'", 'max_length': '25'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_primary': ('django.db.models.fields.BooleanField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ts_run_report': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['file']