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
    (r'^hitchhiking/map/$', 'hitchhiker.views.map', {}, 'map'),
    # past itineraries (archive)
    (r'^hitchhiking/archive/$', 'hitchhiker.views.archive', {}, 'archive'),
    (r'^hitchhiking/new_map/$', 'hitchhiker.views.new_map', {}, 'new_map'),
    (r'^hitchhiking/points/$', 'hitchhiker.views.get_points', {}, 'get_points'),
    (r'^hitchhiking/points/(?P<itinerary_id>\d+)/$', 'hitchhiker.views.get_points', {}, 'get_points_itinerary'),
#    (r'^hitchhiking/points2/$', 'hitchhiker.views.get_points2', {}, 'get_points2'),
#    (r'^hitchhiking/points2/(?P<itinerary_id>\d+)/$', 'hitchhiker.views.get_points2', {}, 'get_points_itinerary2'),
    # past itinerary detail (object from archive)
    (r'^hitchhiking/(?P<object_id>\d+)/$', 'hitchhiker.views.past_trip', {}, 'past_trip'),
    (r'^hitchhiking/position/$', PositionHandler()),
    (r'^hitchhiking/(?P<itinerary_id>\d+).gpx$', 'hitchhiker.views.get_gpx', {}, 'gpx'),
    (r'^hitchhiking/contact/', include('contact_form.urls')),
    (r'^hitchhiking/blog/', include('blog.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
