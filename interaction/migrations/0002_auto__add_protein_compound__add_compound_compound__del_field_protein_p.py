# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Protein_Compound'
        db.create_table(u'interaction_protein_compound', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('compound', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['compound.Compound'])),
            ('protein', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['protein.Protein'])),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['source.Source'])),
        ))
        db.send_create_signal(u'interaction', ['Protein_Compound'])

        # Adding model 'Compound_Compound'
        db.create_table(u'interaction_compound_compound', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('compound1', self.gf('django.db.models.fields.related.ForeignKey')(related_name='compound1', to=orm['compound.Compound'])),
            ('compound2', self.gf('django.db.models.fields.related.ForeignKey')(related_name='compound2', to=orm['compound.Compound'])),
            ('side_effect', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['compound.Side_Effect'])),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['source.Source'])),
        ))
        db.send_create_signal(u'interaction', ['Compound_Compound'])

        # Deleting field 'Protein_Protein.taxonomy1_id'
        db.delete_column(u'interaction_protein_protein', 'taxonomy1_id')

        # Deleting field 'Protein_Protein.taxonomy2_id'
        db.delete_column(u'interaction_protein_protein', 'taxonomy2_id')


    def backwards(self, orm):
        # Deleting model 'Protein_Compound'
        db.delete_table(u'interaction_protein_compound')

        # Deleting model 'Compound_Compound'
        db.delete_table(u'interaction_compound_compound')

        # Adding field 'Protein_Protein.taxonomy1_id'
        db.add_column(u'interaction_protein_protein', 'taxonomy1_id',
                      self.gf('django.db.models.fields.IntegerField')(default=9606),
                      keep_default=False)

        # Adding field 'Protein_Protein.taxonomy2_id'
        db.add_column(u'interaction_protein_protein', 'taxonomy2_id',
                      self.gf('django.db.models.fields.IntegerField')(default=9606),
                      keep_default=False)


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
        u'article.article': {
            'Meta': {'object_name': 'Article'},
            'journal': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'pubmed_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.TextField', [], {}),
            'year_published': ('django.db.models.fields.IntegerField', [], {})
        },
        u'compound.compound': {
            'Meta': {'object_name': 'Compound'},
            'lam_id': ('django.db.models.fields.CharField', [], {'max_length': '25', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'smiles': ('django.db.models.fields.TextField', [], {})
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
        u'interaction.compound_compound': {
            'Meta': {'object_name': 'Compound_Compound'},
            'compound1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'compound1'", 'to': u"orm['compound.Compound']"}),
            'compound2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'compound2'", 'to': u"orm['compound.Compound']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'side_effect': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['compound.Side_Effect']"}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['source.Source']"})
        },
        u'interaction.protein_compound': {
            'Meta': {'object_name': 'Protein_Compound'},
            'compound': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['compound.Compound']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'protein': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['protein.Protein']"}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['source.Source']"})
        },
        u'interaction.protein_protein': {
            'Meta': {'object_name': 'Protein_Protein'},
            'article': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['article.Article']"}),
            'detection_method': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pmi_detection'", 'to': u"orm['annotation.Annotation']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interaction_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pmi_interaction'", 'to': u"orm['annotation.Annotation']"}),
            'protein1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'protein1'", 'to': u"orm['protein.Protein']"}),
            'protein2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'protein2'", 'to': u"orm['protein.Protein']"})
        },
        u'protein.protein': {
            'Meta': {'object_name': 'Protein'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'gene_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'sequence': ('django.db.models.fields.TextField', [], {}),
            'taxonomy_id': ('django.db.models.fields.IntegerField', [], {'default': '9606'}),
            'uniprot_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'primary_key': 'True'})
        },
        u'source.source': {
            'Meta': {'object_name': 'Source'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['interaction']