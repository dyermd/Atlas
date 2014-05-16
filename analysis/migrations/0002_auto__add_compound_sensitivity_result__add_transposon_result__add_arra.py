# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Compound_Sensitivity_Result'
        db.create_table(u'analysis_compound_sensitivity_result', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('analysis', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['analysis.Analysis'])),
            ('sample', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sample.Sample'])),
            ('compound', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['compound.Compound'])),
            ('ic50', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'analysis', ['Compound_Sensitivity_Result'])

        # Adding model 'Transposon_Result'
        db.create_table(u'analysis_transposon_result', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('analysis', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['analysis.Analysis'])),
            ('sample', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sample.Sample'])),
            ('protein', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['protein.Protein'])),
            ('position', self.gf('django.db.models.fields.IntegerField')()),
            ('coverage', self.gf('django.db.models.fields.IntegerField')()),
            ('frequency', self.gf('django.db.models.fields.FloatField')()),
            ('sequence', self.gf('django.db.models.fields.TextField')()),
            ('strand', self.gf('django.db.models.fields.CharField')(default='coding', max_length=10)),
            ('location', self.gf('django.db.models.fields.CharField')(default='exon', max_length=10)),
            ('distance', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'analysis', ['Transposon_Result'])

        # Adding model 'Array_Result'
        db.create_table(u'analysis_array_result', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('analysis', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['analysis.Analysis'])),
            ('sample', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sample.Sample'])),
            ('protein', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['protein.Protein'])),
            ('normalized_value', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'analysis', ['Array_Result'])

        # Adding model 'Compound_Interaction_Result'
        db.create_table(u'analysis_compound_interaction_result', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('analysis', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['analysis.Analysis'])),
            ('sample', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sample.Sample'])),
            ('compound', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['compound.Compound'])),
            ('protein', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['protein.Protein'])),
            ('p_value', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'analysis', ['Compound_Interaction_Result'])

        # Adding model 'Coverage_Stat_Result'
        db.create_table(u'analysis_coverage_stat_result', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('analysis', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['analysis.Analysis'])),
            ('sample', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sample.Sample'])),
            ('mapped_reads', self.gf('django.db.models.fields.IntegerField')()),
            ('percent_on_target', self.gf('django.db.models.fields.FloatField')()),
            ('average_coverage', self.gf('django.db.models.fields.FloatField')()),
            ('uniformity_of_coverage', self.gf('django.db.models.fields.FloatField')()),
            ('percent_1x', self.gf('django.db.models.fields.FloatField')()),
            ('percent_20x', self.gf('django.db.models.fields.FloatField')()),
            ('percent_100x', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'analysis', ['Coverage_Stat_Result'])

        # Adding model 'Mutation_Result'
        db.create_table(u'analysis_mutation_result', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('analysis', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['analysis.Analysis'])),
            ('sample', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sample.Sample'])),
            ('protein', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['protein.Protein'])),
            ('position', self.gf('django.db.models.fields.IntegerField')()),
            ('category', self.gf('django.db.models.fields.CharField')(default='Homozygous', max_length=15)),
            ('type', self.gf('django.db.models.fields.CharField')(default='Reference', max_length=15)),
            ('total_coverage', self.gf('django.db.models.fields.IntegerField')()),
            ('reference_coverage', self.gf('django.db.models.fields.IntegerField')()),
            ('variant_coverage', self.gf('django.db.models.fields.IntegerField')()),
            ('reference_call', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('variant_call', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('frequency', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'analysis', ['Mutation_Result'])

        # Adding field 'Analysis.source'
        db.add_column(u'analysis_analysis', 'source',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='1', to=orm['source.Source']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Compound_Sensitivity_Result'
        db.delete_table(u'analysis_compound_sensitivity_result')

        # Deleting model 'Transposon_Result'
        db.delete_table(u'analysis_transposon_result')

        # Deleting model 'Array_Result'
        db.delete_table(u'analysis_array_result')

        # Deleting model 'Compound_Interaction_Result'
        db.delete_table(u'analysis_compound_interaction_result')

        # Deleting model 'Coverage_Stat_Result'
        db.delete_table(u'analysis_coverage_stat_result')

        # Deleting model 'Mutation_Result'
        db.delete_table(u'analysis_mutation_result')

        # Deleting field 'Analysis.source'
        db.delete_column(u'analysis_analysis', 'source_id')


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
        u'analysis.array_result': {
            'Meta': {'object_name': 'Array_Result'},
            'analysis': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analysis.Analysis']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'normalized_value': ('django.db.models.fields.FloatField', [], {}),
            'protein': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['protein.Protein']"}),
            'sample': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sample.Sample']"})
        },
        u'analysis.compound_interaction_result': {
            'Meta': {'object_name': 'Compound_Interaction_Result'},
            'analysis': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analysis.Analysis']"}),
            'compound': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['compound.Compound']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'p_value': ('django.db.models.fields.FloatField', [], {}),
            'protein': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['protein.Protein']"}),
            'sample': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sample.Sample']"})
        },
        u'analysis.compound_sensitivity_result': {
            'Meta': {'object_name': 'Compound_Sensitivity_Result'},
            'analysis': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analysis.Analysis']"}),
            'compound': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['compound.Compound']"}),
            'ic50': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sample': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sample.Sample']"})
        },
        u'analysis.coverage_stat_result': {
            'Meta': {'object_name': 'Coverage_Stat_Result'},
            'analysis': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analysis.Analysis']"}),
            'average_coverage': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mapped_reads': ('django.db.models.fields.IntegerField', [], {}),
            'percent_100x': ('django.db.models.fields.FloatField', [], {}),
            'percent_1x': ('django.db.models.fields.FloatField', [], {}),
            'percent_20x': ('django.db.models.fields.FloatField', [], {}),
            'percent_on_target': ('django.db.models.fields.FloatField', [], {}),
            'sample': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sample.Sample']"}),
            'uniformity_of_coverage': ('django.db.models.fields.FloatField', [], {})
        },
        u'analysis.mutation_result': {
            'Meta': {'object_name': 'Mutation_Result'},
            'analysis': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analysis.Analysis']"}),
            'category': ('django.db.models.fields.CharField', [], {'default': "'Homozygous'", 'max_length': '15'}),
            'frequency': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {}),
            'protein': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['protein.Protein']"}),
            'reference_call': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'reference_coverage': ('django.db.models.fields.IntegerField', [], {}),
            'sample': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sample.Sample']"}),
            'total_coverage': ('django.db.models.fields.IntegerField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'Reference'", 'max_length': '15'}),
            'variant_call': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'variant_coverage': ('django.db.models.fields.IntegerField', [], {})
        },
        u'analysis.transposon_result': {
            'Meta': {'object_name': 'Transposon_Result'},
            'analysis': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analysis.Analysis']"}),
            'coverage': ('django.db.models.fields.IntegerField', [], {}),
            'distance': ('django.db.models.fields.IntegerField', [], {}),
            'frequency': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'default': "'exon'", 'max_length': '10'}),
            'position': ('django.db.models.fields.IntegerField', [], {}),
            'protein': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['protein.Protein']"}),
            'sample': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sample.Sample']"}),
            'sequence': ('django.db.models.fields.TextField', [], {}),
            'strand': ('django.db.models.fields.CharField', [], {'default': "'coding'", 'max_length': '10'})
        },
        u'compound.compound': {
            'Meta': {'object_name': 'Compound'},
            'lam_id': ('django.db.models.fields.CharField', [], {'max_length': '25', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'smiles': ('django.db.models.fields.TextField', [], {}),
            'structure_2d': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        u'protein.protein': {
            'Meta': {'object_name': 'Protein'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'gene_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'sequence': ('django.db.models.fields.TextField', [], {}),
            'taxonomy_id': ('django.db.models.fields.IntegerField', [], {'default': '9606'}),
            'uniprot_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'primary_key': 'True'})
        },
        u'sample.sample': {
            'Meta': {'object_name': 'Sample'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'file_type': ('django.db.models.fields.CharField', [], {'default': "'BAM'", 'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'source.source': {
            'Meta': {'object_name': 'Source'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['analysis']
