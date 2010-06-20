from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

from hitchhiker.models import Itinerary

def home(request):
    active_trip = Itinerary.objects.filter(active=True)
    if active_trip:
        print active_trip[0].destination
        return render_to_response('hitchhiker/active_trip.html', {   
            'itinerary': active_trip[0]}, 
            context_instance=RequestContext(request))
    else:
        return redirect('/hitchhiking/about/')
