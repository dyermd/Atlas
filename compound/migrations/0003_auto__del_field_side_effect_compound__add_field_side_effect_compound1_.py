# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Side_Effect.compound'
        db.delete_column(u'compound_side_effect', 'compound_id')

        # Adding field 'Side_Effect.compound1'
        db.add_column(u'compound_side_effect', 'compound1',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='blank', related_name='compoundA', to=orm['compound.Compound']),
                      keep_default=False)

        # Adding field 'Side_Effect.compound2'
        db.add_column(u'compound_side_effect', 'compound2',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='blank', related_name='compoundB', to=orm['compound.Compound']),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Side_Effect.compound'
        db.add_column(u'compound_side_effect', 'compound',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='blank', to=orm['compound.Compound']),
                      keep_default=False)

        # Deleting field 'Side_Effect.compound1'
        db.delete_column(u'compound_side_effect', 'compound1_id')

        # Deleting field 'Side_Effect.compound2'
        db.delete_column(u'compound_side_effect', 'compound2_id')


    models = {
        u'compound.compound': {
            'Meta': {'object_name': 'Compound'},
            'lam_id': ('django.db.models.fields.CharField', [], {'max_length': '25', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'smiles': ('django.db.models.fields.TextField', [], {})
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
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['compound']