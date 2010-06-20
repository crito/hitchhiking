from django.conf.urls.defaults import *
from django.views.generic import list_detail
from hitchhiking.hitchhiker.models import Itinerary

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

itinerary_list = {
    "queryset": Itinerary.objects.all(),
}

urlpatterns = patterns('',
    # Example:
    #(r'^/', include('hitchhiking.hitchhiker.urls')),

    # current itinerary (or redirect to about)
    (r'^hitchhiking/$', 'hitchhiker.views.home', {}, 'home'),
    # past itineraries (archive)
    (r'^hitchhiking/archive/$', list_detail.object_list, itinerary_list),
    # past itinerary detail (object from archive)
    (r'^hitchhiking/(?P<object_id>\d+)/$', list_detail.object_detail, itinerary_list),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
