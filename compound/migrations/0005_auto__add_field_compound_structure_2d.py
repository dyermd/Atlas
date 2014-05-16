# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Compound.structure_2d'
        db.add_column(u'compound_compound', 'structure_2d',
                      self.gf('django.db.models.fields.files.ImageField')(default='blank', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Compound.structure_2d'
        db.delete_column(u'compound_compound', 'structure_2d')


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
        u'compound.annotated_with': {
            'Meta': {'object_name': 'Annotated_With'},
            'annotation': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'compound_annotation'", 'to': u"orm['annotation.Annotation']"}),
            'compound': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['compound.Compound']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'compound.compound': {
            'Meta': {'object_name': 'Compound'},
            'lam_id': ('django.db.models.fields.CharField', [], {'max_length': '25', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'smiles': ('django.db.models.fields.TextField', [], {}),
            'structure_2d': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        u'compound.compound_xref': {
            'Meta': {'object_name': 'Compound_Xref'},
            'compound': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['compound.Compound']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['source.Source']"}),
            'xref': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'compound.manufacturer': {
            'Meta': {'object_name': 'Manufacturer'},
            'compound': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['compound.Compound']"}),
            'contact_info': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'compound.patent': {
            'Meta': {'object_name': 'Patent'},
            'compound': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['compound.Compound']"}),
            'expiration_year': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'patent_id': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['source.Source']"})
        },
        u'compound.side_effect': {
            'Meta': {'object_name': 'Side_Effect'},
            'compound1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'compoundA'", 'to': u"orm['compound.Compound']"}),
            'compound2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'compoundB'", 'to': u"orm['compound.Compound']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'probability': ('django.db.models.fields.FloatField', [], {}),
            'side_effect': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['source.Source']"})
        },
        u'source.source': {
            'Meta': {'object_name': 'Source'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['compound']