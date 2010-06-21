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

def archive(request):
    all_trips = Itinerary.objects.filter(active=False)
    active_trip = Itinerary.objects.filter(active=True)
    
    # Fill an array with three trips per row.
    nr_trips = len(all_trips)
    nr_rows = (nr_trips + 3 - 1) / 3

    l = list(all_trips)
    trips = []
    for i in range(nr_rows):
        trips.append([])
        cells = 0
        while cells < 3:
            try:
                t = l.pop()
            except:
                trips[i].append(None)
                break

            trips[i].append(t)
            cells += 1
    
    return render_to_response('hitchhiker/archive.html', {
        'all_trips': trips},
        context_instance=RequestContext(request))
