from django.conf.urls.defaults import *
from django.views.generic import list_detail
from hitchhiker.models import Itinerary, Position, Location
from hitchhiker.views import PositionHandler

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
    (r'^hitchhiking/archive/$', 'hitchhiker.views.archive', {}, 'archive'),
    # past itinerary detail (object from archive)
    (r'^hitchhiking/(?P<object_id>\d+)/$', 'hitchhiker.views.past_trip', {}, 'past_trip'),
    (r'^hitchhiking/position/$', PositionHandler()),
    (r'^hitchhiking/(?P<itinerary_id>\d+).gpx$', 'hitchhiker.views.get_gpx', {}, 'gpx'),
    (r'^hitchhiking/contact/', include('contact_form.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
