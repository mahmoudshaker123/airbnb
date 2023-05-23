from django.shortcuts import render
from property.models import *
from django.db.models import Q
from django.db.models import Count
from blog.models import *
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    places = Place.objects.all().annotate(property_count=Count('property_place'))
    category = Category.objects.all()
    
    #return data in home page in popular hotels and resturant and places
    
    resturant_list = Property.objects.filter(category__name = 'Restaurant')[:5]
    hotels_list = Property.objects.filter(category__name = 'Hotel')[:4]
    places_list = Property.objects.filter(category__name = 'Places')[:4]
    
    recent_posts = Post.objects.all()[:4]
    
    users_count = User.objects.all().count()
    places_count = Property.objects.filter(category__name = 'Places').count()
    hotels_count = Property.objects.filter(category__name = 'Hotel').count()
    resturant_count = Property.objects.filter(category__name = 'Restaurant').count()
    
    return render(request , 'settings/home.html' , {
        'places' : places,
        'category' : category,
        'resturant_list':resturant_list,
        'hotels_list':hotels_list,
        'places_list' :places_list,
        'recent_post':recent_posts,
        'users_count':users_count,
        'places_count':places_count,
        'hotels_count':hotels_count,
        'resturant_count':resturant_count,
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
    


def contact_us(request):
    pass