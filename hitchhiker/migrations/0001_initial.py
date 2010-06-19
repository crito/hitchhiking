# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Itinerary'
        db.create_table('hitchhiker_itinerary', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('end_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('gpx_file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal('hitchhiker', ['Itinerary'])


    def backwards(self, orm):
        
        # Deleting model 'Itinerary'
        db.delete_table('hitchhiker_itinerary')


    models = {
        'hitchhiker.itinerary': {
            'Meta': {'object_name': 'Itinerary'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {}),
            'gpx_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['hitchhiker']
