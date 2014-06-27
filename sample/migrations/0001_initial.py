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
            ('plate', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True)),
        ))
        db.send_create_signal(u'sample', ['Sample'])

        # Adding model 'Uses_File'
        db.create_table(u'sample_uses_file', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sample', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sample.Sample'])),
            ('file', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['file.File'])),
        ))
        db.send_create_signal(u'sample', ['Uses_File'])

        # Adding model 'Sample_Relationship'
        db.create_table(u'sample_sample_relationship', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sample1', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sample1', to=orm['sample.Sample'])),
            ('sample2', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sample2', to=orm['sample.Sample'])),
            ('role1', self.gf('django.db.models.fields.CharField')(default='Normal', max_length=15)),
            ('role2', self.gf('django.db.models.fields.CharField')(default='Normal', max_length=15)),
        ))
        db.send_create_signal(u'sample', ['Sample_Relationship'])


    def backwards(self, orm):
        # Deleting model 'Sample'
        db.delete_table(u'sample_sample')

        # Deleting model 'Uses_File'
        db.delete_table(u'sample_uses_file')

        # Deleting model 'Sample_Relationship'
        db.delete_table(u'sample_sample_relationship')


    models = {
        u'file.file': {
            'Meta': {'object_name': 'File'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'file_path': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'file_type': ('django.db.models.fields.CharField', [], {'default': "'BAM'", 'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_primary': ('django.db.models.fields.BooleanField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ts_run_report': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'})
        },
        u'sample.sample': {
            'Meta': {'object_name': 'Sample'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'plate': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'})
        },
        u'sample.sample_relationship': {
            'Meta': {'object_name': 'Sample_Relationship'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'role1': ('django.db.models.fields.CharField', [], {'default': "'Normal'", 'max_length': '15'}),
            'role2': ('django.db.models.fields.CharField', [], {'default': "'Normal'", 'max_length': '15'}),
            'sample1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sample1'", 'to': u"orm['sample.Sample']"}),
            'sample2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sample2'", 'to': u"orm['sample.Sample']"})
        },
        u'sample.uses_file': {
            'Meta': {'object_name': 'Uses_File'},
            'file': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['file.File']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sample': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sample.Sample']"})
        }
    }

    complete_apps = ['sample']