from django.db import models

#class WorldBorders(models.Model):
#        # Regular Django fields corresponding to the attributes in the
#    # world borders shapefile.
#    name = models.CharField(max_length=50)
#    area = models.IntegerField()
#    pop2005 = models.IntegerField('Population 2005')
#    fips = models.CharField('FIPS Code', max_length=2)
#    iso2 = models.CharField('2 Digit ISO', max_length=2)
#    iso3 = models.CharField('3 Digit ISO', max_length=3)
#    un = models.IntegerField('United Nations Code')
#    region = models.IntegerField('Region Code')
#    subregion = models.IntegerField('Sub-Region Code')
#    lon = models.FloatField()
#    lat = models.FloatField()

    # GeoDjango-specific: a geometry field (MultiPolygonField), and
    # overriding the default manager with a GeoManager instance.
#    mpoly = models.MultiPolygonField()
#    objects = models.GeoManager()

    # So the model is pluralized correctly in the admin.
#    class Meta:
#                verbose_name_plural = "World Borders"

#    # Returns the string representation of the model.
#    def __unicode__(self):
#                return self.name

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



