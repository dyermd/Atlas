# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Sample'
        db.create_table(u'sample_sample', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'sample', ['Sample'])

        # Adding model 'Sample_File'
        db.create_table(u'sample_sample_file', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sample', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sample.Sample'])),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('fileType', self.gf('django.db.models.fields.CharField')(default='BAM', max_length=10)),
        ))
        db.send_create_signal(u'sample', ['Sample_File'])


    def backwards(self, orm):
        # Deleting model 'Sample'
        db.delete_table(u'sample_sample')

        # Deleting model 'Sample_File'
        db.delete_table(u'sample_sample_file')


    models = {
        u'sample.sample': {
            'Meta': {'object_name': 'Sample'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'sample.sample_file': {
            'Meta': {'object_name': 'Sample_File'},
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'fileType': ('django.db.models.fields.CharField', [], {'default': "'BAM'", 'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sample': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sample.Sample']"})
        }
    }

    complete_apps = ['sample']