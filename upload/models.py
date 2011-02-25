from django.db import models
from django.template.defaultfilters import filesizeformat
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
import datetime

class Upload(models.Model):
    """Uploaded files."""
    file = models.FileField(upload_to='media/uploads',)
    timestamp = models.DateTimeField(default=datetime.datetime.now)
    notes = models.CharField(max_length=255, blank=True)
    #content_type = models.ForeignKey(ContentType)
    #object_id = models.PositiveIntegerField()

    #content_object = generic.GenericForeignKey()

    class Meta:
        ordering = ['-timestamp',]
 
    def __unicode__(self):
        return u"%s" % (self.file)
 
    @property
    def size(self):
        return filesizeformat(self.file.size)
