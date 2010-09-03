from django.conf.urls.defaults import *
from django.views.generic import list_detail
from blog.models import Post

post_list = {
    'queryset': Post.objects.all(),
    }

urlpatterns = patterns('',
    (r'^$', list_detail.object_list, post_list),
)

