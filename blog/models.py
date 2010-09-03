from django.db import models
from django.template.defaultfilters import slugify
from django.db.models import permalink

from hitchhiker.models import Itinerary
import datetime

class Post(models.Model):
    """Blog post model."""
    STATUS_CHOICES = (
        (1, 'Draft'),
        (2, 'Public'),
    )
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=200, blank=True)
    body = models.TextField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    publish = models.DateTimeField(default=datetime.datetime.now, blank=True, null=True)
    itinerary = models.ForeignKey(Itinerary, blank=True, null=True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        ordering = ['-publish']
        get_latest_by = 'publish'

    def __unicode__(self):
        return u'%s' % self.title
       
    def save(self):
        self.slug = slugify(self.title)
        super(Post, self).save()

    @permalink
    def get_absolute_url(self):
        return ('post_detail', None, {'slug': self.slug,})

