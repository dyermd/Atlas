# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'File.file_type'
        db.alter_column(u'file_file', 'file_type', self.gf('django.db.models.fields.CharField')(max_length=50))

    def backwards(self, orm):

        # Changing field 'File.file_type'
        db.alter_column(u'file_file', 'file_type', self.gf('django.db.models.fields.CharField')(max_length=25))

    models = {
        u'file.file': {
            'Meta': {'object_name': 'File'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'file_path': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'file_type': ('django.db.models.fields.CharField', [], {'default': "'BAM'", 'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_primary': ('django.db.models.fields.BooleanField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ts_run_report': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['file']