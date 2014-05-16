# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Article'
        db.create_table(u'article_article', (
            ('pubmed_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.TextField')()),
            ('year_published', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'article', ['Article'])


    def backwards(self, orm):
        # Deleting model 'Article'
        db.delete_table(u'article_article')


    models = {
        u'article.article': {
            'Meta': {'object_name': 'Article'},
            'pubmed_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.TextField', [], {}),
            'year_published': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['article']