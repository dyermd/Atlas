# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Protein'
        db.create_table(u'protein_protein', (
            ('uniprot_id', self.gf('django.db.models.fields.CharField')(max_length=100, primary_key=True)),
            ('gene_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('sequence', self.gf('django.db.models.fields.TextField')()),
            ('taxonomy_id', self.gf('django.db.models.fields.IntegerField')(default=9606)),
        ))
        db.send_create_signal(u'protein', ['Protein'])

        # Adding model 'Protein_Xref'
        db.create_table(u'protein_protein_xref', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('protein', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['protein.Protein'])),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['source.Source'])),
            ('xref', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'protein', ['Protein_Xref'])


    def backwards(self, orm):
        # Deleting model 'Protein'
        db.delete_table(u'protein_protein')

        # Deleting model 'Protein_Xref'
        db.delete_table(u'protein_protein_xref')


    models = {
        u'protein.protein': {
            'Meta': {'object_name': 'Protein'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'gene_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'sequence': ('django.db.models.fields.TextField', [], {}),
            'taxonomy_id': ('django.db.models.fields.IntegerField', [], {'default': '9606'}),
            'uniprot_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'primary_key': 'True'})
        },
        u'protein.protein_xref': {
            'Meta': {'object_name': 'Protein_Xref'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'protein': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['protein.Protein']"}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['source.Source']"}),
            'xref': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'source.source': {
            'Meta': {'object_name': 'Source'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['protein']