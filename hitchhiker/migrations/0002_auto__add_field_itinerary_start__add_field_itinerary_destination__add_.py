# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Itinerary.start'
        db.add_column('hitchhiker_itinerary', 'start', self.gf('django.db.models.fields.CharField')(default='Hasebroekstraat', max_length=200, blank=True), keep_default=False)

        # Adding field 'Itinerary.destination'
        db.add_column('hitchhiker_itinerary', 'destination', self.gf('django.db.models.fields.CharField')(default='Spuistraat', max_length=200, blank=True), keep_default=False)

        # Adding field 'Itinerary.video'
        db.add_column('hitchhiker_itinerary', 'video', self.gf('django.db.models.fields.URLField')(default='http://stream.30loops.net:8000/hitchhiking.ogg', max_length=200), keep_default=False)

        # Changing field 'Itinerary.gpx_file'
        db.alter_column('hitchhiker_itinerary', 'gpx_file', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True))

        # Changing field 'Itinerary.start_date'
        db.alter_column('hitchhiker_itinerary', 'start_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True))

        # Changing field 'Itinerary.end_date'
        db.alter_column('hitchhiker_itinerary', 'end_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True))


    def backwards(self, orm):
        
        # Deleting field 'Itinerary.start'
        db.delete_column('hitchhiker_itinerary', 'start')

        # Deleting field 'Itinerary.destination'
        db.delete_column('hitchhiker_itinerary', 'destination')

        # Deleting field 'Itinerary.video'
        db.delete_column('hitchhiker_itinerary', 'video')

        # Changing field 'Itinerary.gpx_file'
        db.alter_column('hitchhiker_itinerary', 'gpx_file', self.gf('django.db.models.fields.files.FileField')(max_length=100))

        # Changing field 'Itinerary.start_date'
        db.alter_column('hitchhiker_itinerary', 'start_date', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'Itinerary.end_date'
        db.alter_column('hitchhiker_itinerary', 'end_date', self.gf('django.db.models.fields.DateTimeField')())


    models = {
        'hitchhiker.itinerary': {
            'Meta': {'object_name': 'Itinerary'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'destination': ('django.db.models.fields.CharField', [], {'default': "'Spuistraat'", 'max_length': '200', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'gpx_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start': ('django.db.models.fields.CharField', [], {'default': "'Hasebroekstraat'", 'max_length': '200', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'video': ('django.db.models.fields.URLField', [], {'default': "'http://stream.30loops.net:8000/hitchhiking.ogg'", 'max_length': '200'})
        }
    }

    complete_apps = ['hitchhiker']
