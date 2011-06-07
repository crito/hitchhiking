from django.conf.urls.defaults import *
from django.views.generic import list_detail
from django.views.generic.simple import direct_to_template
from hitchhiking.hitchhiker.models import Itinerary, Position, Location
from hitchhiking.hitchhiker.views import PositionHandler
from django.views.generic.simple import redirect_to

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

itinerary_list = {
    "queryset": Itinerary.objects.all(),
}

urlpatterns = patterns('',
    # Example:
    (r'^$', direct_to_template, {'template': 'home.html'}),

    # current itinerary (or redirect to about)
    (r'^hitchhiking/$', 'hitchhiking.hitchhiker.views.home', {}, 'home'),
    (r'^hitchhiking/map/$', 'hitchhiking.hitchhiker.views.map', {}, 'map'),
    # past itineraries (archive)
    (r'^hitchhiking/archive/$', 'hitchhiking.hitchhiker.views.archive', {}, 'archive'),
    (r'^hitchhiking/new_map/$', 'hitchhiking.hitchhiker.views.new_map', {}, 'new_map'),
    (r'^hitchhiking/points/$', 'hitchhiking.hitchhiker.views.get_points', {}, 'get_points'),
    (r'^hitchhiking/points/(?P<itinerary_id>\d+)/$', 'hitchhiking.hitchhiker.views.get_points', {}, 'get_points_itinerary'),
#    (r'^hitchhiking/points2/$', 'hitchhiking.hitchhiker.views.get_points2', {}, 'get_points2'),
#    (r'^hitchhiking/points2/(?P<itinerary_id>\d+)/$', 'hitchhiking.hitchhiker.views.get_points2', {}, 'get_points_itinerary2'),
    # past itinerary detail (object from archive)
    (r'^hitchhiking/(?P<object_id>\d+)/$', 'hitchhiking.hitchhiker.views.past_trip', {}, 'past_trip'),
    (r'^hitchhiking/position/$', PositionHandler()),
    (r'^hitchhiking/(?P<itinerary_id>\d+).gpx$', 'hitchhiking.hitchhiker.views.get_gpx', {}, 'gpx'),
    (r'^hitchhiking/contact/', include('contact_form.urls')),
    (r'^hitchhiking/blog/', include('hitchhiking.blog.urls')),
    (r'^contact/', include('contact_form.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
