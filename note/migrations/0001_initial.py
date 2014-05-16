# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Note'
        db.create_table(u'note_note', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('note', self.gf('django.db.models.fields.TextField')()),
            ('date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'note', ['Note'])


    def backwards(self, orm):
        # Deleting model 'Note'
        db.delete_table(u'note_note')


    models = {
        u'note.note': {
            'Meta': {'object_name': 'Note'},
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['note']