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
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('start', self.gf('django.db.models.fields.CharField')(default='Hasebroekstraat', max_length=200, blank=True)),
            ('end_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('destination', self.gf('django.db.models.fields.CharField')(default='Spuistraat', max_length=200, blank=True)),
            ('video', self.gf('django.db.models.fields.URLField')(default='http://stream.30loops.net:8000/hitchhiking.ogg', max_length=200)),
            ('gpx_file', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('poster', self.gf('django.db.models.fields.URLField')(default='http://mariazendre.org/media/poster/1.png', max_length=200)),
        ))
        db.send_create_signal('hitchhiker', ['Itinerary'])

        # Adding model 'Position'
        db.create_table('hitchhiker_position', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('longitude', self.gf('django.db.models.fields.FloatField')()),
            ('latitude', self.gf('django.db.models.fields.FloatField')()),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('itinerary', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hitchhiker.Itinerary'])),
        ))
        db.send_create_signal('hitchhiker', ['Position'])

        # Adding model 'Location'
        db.create_table('hitchhiker_location', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('position', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hitchhiker.Position'])),
        ))
        db.send_create_signal('hitchhiker', ['Location'])


    def backwards(self, orm):
        
        # Deleting model 'Itinerary'
        db.delete_table('hitchhiker_itinerary')

        # Deleting model 'Position'
        db.delete_table('hitchhiker_position')

        # Deleting model 'Location'
        db.delete_table('hitchhiker_location')


    models = {
        'hitchhiker.itinerary': {
            'Meta': {'ordering': "['start_date']", 'object_name': 'Itinerary'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'destination': ('django.db.models.fields.CharField', [], {'default': "'Spuistraat'", 'max_length': '200', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'gpx_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'poster': ('django.db.models.fields.URLField', [], {'default': "'http://mariazendre.org/media/poster/1.png'", 'max_length': '200'}),
            'start': ('django.db.models.fields.CharField', [], {'default': "'Hasebroekstraat'", 'max_length': '200', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'video': ('django.db.models.fields.URLField', [], {'default': "'http://stream.30loops.net:8000/hitchhiking.ogg'", 'max_length': '200'})
        },
        'hitchhiker.location': {
            'Meta': {'object_name': 'Location'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'position': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['hitchhiker.Position']"})
        },
        'hitchhiker.position': {
            'Meta': {'ordering': "['timestamp']", 'object_name': 'Position'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'itinerary': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['hitchhiker.Itinerary']"}),
            'latitude': ('django.db.models.fields.FloatField', [], {}),
            'longitude': ('django.db.models.fields.FloatField', [], {}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['hitchhiker']
