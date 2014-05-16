# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Sample_File'
        db.delete_table(u'sample_sample_file')

        # Adding model 'Sample_Relationship'
        db.create_table(u'sample_sample_relationship', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sample1', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sample1', to=orm['sample.Sample'])),
            ('sample2', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sample2', to=orm['sample.Sample'])),
            ('role1', self.gf('django.db.models.fields.CharField')(default='Normal', max_length=15)),
            ('role2', self.gf('django.db.models.fields.CharField')(default='Normal', max_length=15)),
        ))
        db.send_create_signal(u'sample', ['Sample_Relationship'])

        # Adding field 'Sample.file'
        db.add_column(u'sample_sample', 'file',
                      self.gf('django.db.models.fields.files.FileField')(default='blank', max_length=100),
                      keep_default=False)

        # Adding field 'Sample.file_type'
        db.add_column(u'sample_sample', 'file_type',
                      self.gf('django.db.models.fields.CharField')(default='BAM', max_length=10),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'Sample_File'
        db.create_table(u'sample_sample_file', (
            ('sample', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sample.Sample'])),
            ('fileType', self.gf('django.db.models.fields.CharField')(default='BAM', max_length=10)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'sample', ['Sample_File'])

        # Deleting model 'Sample_Relationship'
        db.delete_table(u'sample_sample_relationship')

        # Deleting field 'Sample.file'
        db.delete_column(u'sample_sample', 'file')

        # Deleting field 'Sample.file_type'
        db.delete_column(u'sample_sample', 'file_type')


    models = {
        u'sample.sample': {
            'Meta': {'object_name': 'Sample'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'file_type': ('django.db.models.fields.CharField', [], {'default': "'BAM'", 'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'sample.sample_relationship': {
            'Meta': {'object_name': 'Sample_Relationship'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'role1': ('django.db.models.fields.CharField', [], {'default': "'Normal'", 'max_length': '15'}),
            'role2': ('django.db.models.fields.CharField', [], {'default': "'Normal'", 'max_length': '15'}),
            'sample1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sample1'", 'to': u"orm['sample.Sample']"}),
            'sample2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sample2'", 'to': u"orm['sample.Sample']"})
        }
    }

    complete_apps = ['sample']