# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Protein_Protein.analysis'
        db.add_column(u'interaction_protein_protein', 'analysis',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['analysis.Analysis'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Protein_Compound.analysis'
        db.add_column(u'interaction_protein_compound', 'analysis',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['analysis.Analysis'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Compound_Compound.analysis'
        db.add_column(u'interaction_compound_compound', 'analysis',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['analysis.Analysis'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Protein_Protein.analysis'
        db.delete_column(u'interaction_protein_protein', 'analysis_id')

        # Deleting field 'Protein_Compound.analysis'
        db.delete_column(u'interaction_protein_compound', 'analysis_id')

        # Deleting field 'Compound_Compound.analysis'
        db.delete_column(u'interaction_compound_compound', 'analysis_id')


    models = {
        u'analysis.analysis': {
            'Meta': {'object_name': 'Analysis'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'parameters': ('django.db.models.fields.TextField', [], {}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['source.Source']"}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'Pending'", 'max_length': '15'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'Transposon'", 'max_length': '30'})
        },
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
            'smiles': ('django.db.models.fields.TextField', [], {}),
            'structure_2d': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
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
            'analysis': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analysis.Analysis']", 'null': 'True', 'blank': 'True'}),
            'article': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['article.Article']"}),
            'compound1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'compound1'", 'to': u"orm['compound.Compound']"}),
            'compound2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'compound2'", 'to': u"orm['compound.Compound']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'side_effect': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['compound.Side_Effect']"}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['source.Source']"})
        },
        u'interaction.protein_compound': {
            'Meta': {'object_name': 'Protein_Compound'},
            'analysis': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analysis.Analysis']", 'null': 'True', 'blank': 'True'}),
            'article': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['article.Article']"}),
            'compound': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['compound.Compound']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'protein': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['protein.Protein']"}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['source.Source']"})
        },
        u'interaction.protein_protein': {
            'Meta': {'object_name': 'Protein_Protein'},
            'analysis': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analysis.Analysis']", 'null': 'True', 'blank': 'True'}),
            'article': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['article.Article']"}),
            'detection_method': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pmi_detection'", 'to': u"orm['annotation.Annotation']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interaction_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pmi_interaction'", 'to': u"orm['annotation.Annotation']"}),
            'protein1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'protein1'", 'to': u"orm['protein.Protein']"}),
            'protein2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'protein2'", 'to': u"orm['protein.Protein']"}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['source.Source']"})
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
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['interaction']