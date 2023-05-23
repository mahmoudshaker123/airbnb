from django.shortcuts import render
from property.models import *
from django.db.models import Q
from django.db.models import Count
# Create your views here.

def home(request):
    places = Place.objects.all().annotate(property_count=Count('property_place'))
    category = Category.objects.all()
    return render(request , 'settings/home.html' , {
        'places' : places,
        'category' : category
    })
    

def home_search(request):
    name = request.GET.get('name')
    place = request.GET.get('place')
    
    property_list = Property.objects.filter(
        Q(name__icontains=name) & Q(places__name__icontains=place)
    )
    
    context = {'property_list': property_list}
    return render(request , 'settings/home_search.html', context)
    
    
    

def category_filter(request , category):
    category = Category.objects.get(name = category)
    property_list = Property.objects.filter( category = category )
    return render(request , 'settings/home_search.html', {'property_list': property_list} )
    
