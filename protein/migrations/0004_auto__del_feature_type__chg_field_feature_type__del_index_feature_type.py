# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Feature_Type'
        db.delete_table(u'protein_feature_type')


        # Renaming column for 'Feature.type' to match new field type.
        db.rename_column(u'protein_feature', 'type_id', 'type')
        # Changing field 'Feature.type'
        db.alter_column(u'protein_feature', 'type', self.gf('django.db.models.fields.CharField')(max_length=10))
        # Removing index on 'Feature', fields ['type']
        db.delete_index(u'protein_feature', ['type_id'])


    def backwards(self, orm):
        # Adding index on 'Feature', fields ['type']
        db.create_index(u'protein_feature', ['type_id'])

        # Adding model 'Feature_Type'
        db.create_table(u'protein_feature_type', (
            ('type', self.gf('django.db.models.fields.CharField')(max_length=25, primary_key=True)),
        ))
        db.send_create_signal(u'protein', ['Feature_Type'])


        # Renaming column for 'Feature.type' to match new field type.
        db.rename_column(u'protein_feature', 'type', 'type_id')
        # Changing field 'Feature.type'
        db.alter_column(u'protein_feature', 'type_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['protein.Feature_Type']))

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
        u'protein.annotated_with': {
            'Meta': {'object_name': 'Annotated_With'},
            'annotation': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'protein_annotation'", 'to': u"orm['annotation.Annotation']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'protein': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['protein.Protein']"})
        },
        u'protein.feature': {
            'Meta': {'object_name': 'Feature'},
            'chromosome': ('django.db.models.fields.IntegerField', [], {}),
            'end_position': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['protein.Feature_Model']"}),
            'protein': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['protein.Protein']"}),
            'start_position': ('django.db.models.fields.IntegerField', [], {}),
            'strand': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'CDS'", 'max_length': '10'})
        },
        u'protein.feature_model': {
            'Meta': {'object_name': 'Feature_Model'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['source.Source']"}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
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