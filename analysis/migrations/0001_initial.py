# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Analysis'
        db.create_table(u'analysis_analysis', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('type', self.gf('django.db.models.fields.CharField')(default='Transposon', max_length=30)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('parameters', self.gf('django.db.models.fields.TextField')()),
            ('status', self.gf('django.db.models.fields.CharField')(default='Pending', max_length=15)),
        ))
        db.send_create_signal(u'analysis', ['Analysis'])


    def backwards(self, orm):
        # Deleting model 'Analysis'
        db.delete_table(u'analysis_analysis')


    models = {
        u'analysis.analysis': {
            'Meta': {'object_name': 'Analysis'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'parameters': ('django.db.models.fields.TextField', [], {}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'Pending'", 'max_length': '15'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'Transposon'", 'max_length': '30'})
        }
    }

    complete_apps = ['analysis']