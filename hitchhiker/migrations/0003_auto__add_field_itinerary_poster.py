# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Itinerary.poster'
        db.add_column('hitchhiker_itinerary', 'poster', self.gf('django.db.models.fields.URLField')(default='http://mariazendre.org/media/poster/1.png', max_length=200), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Itinerary.poster'
        db.delete_column('hitchhiker_itinerary', 'poster')


    models = {
        'hitchhiker.itinerary': {
            'Meta': {'object_name': 'Itinerary'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'destination': ('django.db.models.fields.CharField', [], {'default': "'Spuistraat'", 'max_length': '200', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'gpx_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'poster': ('django.db.models.fields.URLField', [], {'default': "'http://mariazendre.org/media/poster/1.png'", 'max_length': '200'}),
            'start': ('django.db.models.fields.CharField', [], {'default': "'Hasebroekstraat'", 'max_length': '200', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'video': ('django.db.models.fields.URLField', [], {'default': "'http://stream.30loops.net:8000/hitchhiking.ogg'", 'max_length': '200'})
        }
    }

    complete_apps = ['hitchhiker']
