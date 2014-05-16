# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Article.journal'
        db.add_column(u'article_article', 'journal',
                      self.gf('django.db.models.fields.CharField')(default='blank', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Article.journal'
        db.delete_column(u'article_article', 'journal')


    models = {
        u'article.article': {
            'Meta': {'object_name': 'Article'},
            'journal': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'pubmed_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.TextField', [], {}),
            'year_published': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['article']