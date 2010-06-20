from django.shortcuts import render_to_response, redirect, get_object_or_404
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

def past_trip(request, object_id):
    past_trip = get_object_or_404(Itinerary, pk=object_id)

    return render_to_response('hitchhiker/past_trip.html', {
            'itinerary': past_trip}, 
            context_instance=RequestContext(request))
    else:
        return redirect('/hitchhiking/about/')
