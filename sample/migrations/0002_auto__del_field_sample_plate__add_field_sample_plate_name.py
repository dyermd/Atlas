# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Sample.plate_name'
        db.add_column(u'sample_sample', 'plate_name',
                      self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Sample.plate_name'
        db.delete_column(u'sample_sample', 'plate_name')


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
            'plate_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'})
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
