from django.db import models

class Itinerary(models.Model):
    active = models.BooleanField(default=False)
    start_date = models.DateTimeField(null=True, blank=True)
    start = models.CharField(max_length=200, blank=True, default="Hasebroekstraat")
    end_date = models.DateTimeField(null=True, blank=True)
    destination = models.CharField(max_length=200, blank=True, default="Spuistraat")
    video = models.URLField(default="http://stream.30loops.net:8000/hitchhiking.ogg")
    gpx_file = models.FileField(upload_to="gpx", blank=True)
    poster = models.URLField(default="http://mariazendre.org/media/poster/1.png")

    class Meta:
        ordering = ['start_date']
        verbose_name_plural = 'Itineraries'

    def __unicode__(self):
        return '%s itinerary started on %s' % (
                ('Active' if self.active else 'Past'),
                str(self.start_date))


class Position(models.Model):
    longitude = models.FloatField()
    latitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    itinerary = models.ForeignKey(Itinerary)

    class Meta:
        ordering = ['timestamp']

    def __unicode__(self):
        return "%s/%s" % (self.longitude, self.latitude)

class Location(models.Model):
    name = models.CharField(max_length=128, blank=True)
    description = models.TextField(blank=True)
    position = models.ForeignKey(Position)

    def __unicode__(self):
        return "%s (%s/%s)" % (self.name, self.position.longitude, self.position.latitude)
