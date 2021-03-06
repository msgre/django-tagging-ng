# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tag'
        db.create_table(u'tagging_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50, db_index=True)),
        ))
        db.send_create_signal(u'tagging', ['Tag'])

        # Adding model 'TaggedItem'
        db.create_table(u'tagging_taggeditem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag', self.gf('django.db.models.fields.related.ForeignKey')(related_name='items', to=orm['tagging.Tag'])),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal(u'tagging', ['TaggedItem'])

        # Adding unique constraint on 'TaggedItem', fields ['tag', 'content_type', 'object_id']
        db.create_unique(u'tagging_taggeditem', ['tag_id', 'content_type_id', 'object_id'])

        # Adding model 'Synonym'
        db.create_table(u'tagging_synonym', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50, db_index=True)),
            ('tag', self.gf('django.db.models.fields.related.ForeignKey')(related_name='synonyms', to=orm['tagging.Tag'])),
        ))
        db.send_create_signal(u'tagging', ['Synonym'])


    def backwards(self, orm):
        # Removing unique constraint on 'TaggedItem', fields ['tag', 'content_type', 'object_id']
        db.delete_unique(u'tagging_taggeditem', ['tag_id', 'content_type_id', 'object_id'])

        # Deleting model 'Tag'
        db.delete_table(u'tagging_tag')

        # Deleting model 'TaggedItem'
        db.delete_table(u'tagging_taggeditem')

        # Deleting model 'Synonym'
        db.delete_table(u'tagging_synonym')


    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'tagging.synonym': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Synonym'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'synonyms'", 'to': u"orm['tagging.Tag']"})
        },
        u'tagging.tag': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'})
        },
        u'tagging.taggeditem': {
            'Meta': {'unique_together': "(('tag', 'content_type', 'object_id'),)", 'object_name': 'TaggedItem'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'items'", 'to': u"orm['tagging.Tag']"})
        }
    }

    complete_apps = ['tagging']