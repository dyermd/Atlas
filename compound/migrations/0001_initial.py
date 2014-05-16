# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Compound'
        db.create_table(u'compound_compound', (
            ('lam_id', self.gf('django.db.models.fields.CharField')(max_length=25, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('smiles', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'compound', ['Compound'])

        # Adding model 'Compound_Xref'
        db.create_table(u'compound_compound_xref', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('compound', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['compound.Compound'])),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['source.Source'])),
            ('xref', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'compound', ['Compound_Xref'])

        # Adding model 'Patent'
        db.create_table(u'compound_patent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('compound', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['compound.Compound'])),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['source.Source'])),
            ('patent_id', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('expiration_year', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'compound', ['Patent'])


    def backwards(self, orm):
        # Deleting model 'Compound'
        db.delete_table(u'compound_compound')

        # Deleting model 'Compound_Xref'
        db.delete_table(u'compound_compound_xref')

        # Deleting model 'Patent'
        db.delete_table(u'compound_patent')


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
        u'compound.patent': {
            'Meta': {'object_name': 'Patent'},
            'compound': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['compound.Compound']"}),
            'expiration_year': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'patent_id': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
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