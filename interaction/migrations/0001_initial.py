# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Protein_Protein'
        db.create_table(u'interaction_protein_protein', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('protein1', self.gf('django.db.models.fields.related.ForeignKey')(related_name='protein1', to=orm['protein.Protein'])),
            ('taxonomy1_id', self.gf('django.db.models.fields.IntegerField')(default=9606)),
            ('protein2', self.gf('django.db.models.fields.related.ForeignKey')(related_name='protein2', to=orm['protein.Protein'])),
            ('taxonomy2_id', self.gf('django.db.models.fields.IntegerField')(default=9606)),
            ('article', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['article.Article'])),
            ('detection_method', self.gf('django.db.models.fields.related.ForeignKey')(related_name='pmi_detection', to=orm['annotation.Annotation'])),
            ('interaction_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='pmi_interaction', to=orm['annotation.Annotation'])),
        ))
        db.send_create_signal(u'interaction', ['Protein_Protein'])


    def backwards(self, orm):
        # Deleting model 'Protein_Protein'
        db.delete_table(u'interaction_protein_protein')


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
            'pubmed_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.TextField', [], {}),
            'year_published': ('django.db.models.fields.IntegerField', [], {})
        },
        u'interaction.protein_protein': {
            'Meta': {'object_name': 'Protein_Protein'},
            'article': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['article.Article']"}),
            'detection_method': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pmi_detection'", 'to': u"orm['annotation.Annotation']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interaction_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pmi_interaction'", 'to': u"orm['annotation.Annotation']"}),
            'protein1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'protein1'", 'to': u"orm['protein.Protein']"}),
            'protein2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'protein2'", 'to': u"orm['protein.Protein']"}),
            'taxonomy1_id': ('django.db.models.fields.IntegerField', [], {'default': '9606'}),
            'taxonomy2_id': ('django.db.models.fields.IntegerField', [], {'default': '9606'})
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