from django.shortcuts import render
from property.models import *
from django.db.models import Q

# Create your views here.

def home(request):
    places = Place.objects.all()
    return render(request , 'settings/home.html' , {
        'places' : places
    })
    

def home_search(request):
    name = request.GET.get('name')
    place = request.GET.get('place')
    
    property_list = Property.objects.filter(
        Q(name__icontains=name) & Q(places__name__icontains=place)
    )
    
    context = {'property_list': property_list}
    return render(request , 'settings/home_search.html', context)
    
    
