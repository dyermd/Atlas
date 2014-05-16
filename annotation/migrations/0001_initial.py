# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Annotation_Model'
        db.create_table(u'annotation_annotation_model', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['source.Source'])),
            ('version', self.gf('django.db.models.fields.CharField')(max_length=25)),
        ))
        db.send_create_signal(u'annotation', ['Annotation_Model'])

        # Adding model 'Annotation'
        db.create_table(u'annotation_annotation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('model', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['annotation.Annotation_Model'])),
            ('annotation_id', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'annotation', ['Annotation'])


    def backwards(self, orm):
        # Deleting model 'Annotation_Model'
        db.delete_table(u'annotation_annotation_model')

        # Deleting model 'Annotation'
        db.delete_table(u'annotation_annotation')


    models = {
        u'annotation.annotation': {
            'Meta': {'object_name': 'Annotation'},
            'annotation_id': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['annotation.Annotation_Model']"})
        },
        u'annotation.annotation_model': {
            'Meta': {'object_name': 'Annotation_Model'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['source.Source']"}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        u'source.source': {
            'Meta': {'object_name': 'Source'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['annotation']