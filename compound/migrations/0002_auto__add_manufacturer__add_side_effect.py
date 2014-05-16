# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Manufacturer'
        db.create_table(u'compound_manufacturer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('compound', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['compound.Compound'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('contact_info', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'compound', ['Manufacturer'])

        # Adding model 'Side_Effect'
        db.create_table(u'compound_side_effect', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('compound', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['compound.Compound'])),
            ('side_effect', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['source.Source'])),
            ('probability', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'compound', ['Side_Effect'])


    def backwards(self, orm):
        # Deleting model 'Manufacturer'
        db.delete_table(u'compound_manufacturer')

        # Deleting model 'Side_Effect'
        db.delete_table(u'compound_side_effect')


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
            'compound': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['compound.Compound']"}),
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