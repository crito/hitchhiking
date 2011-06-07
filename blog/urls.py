from django.conf.urls.defaults import *
from django.views.generic import list_detail
from models import Post
#from blog import views

post_list = {
    'queryset': Post.objects.filter(status=2),
    }

urlpatterns = patterns('',
    (r'^$', list_detail.object_list, post_list, 'post_list'),
    #(r'(?P<slug>\w+)/$', {}, views.post_detail, 'post_detail'),
    (r'(?P<slug>[\w-]+)/$', list_detail.object_detail, dict(post_list, slug_field="slug"), 'post_detail'),
)

