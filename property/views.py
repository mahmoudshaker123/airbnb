from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import *

# Create your views here.

class PropertyList(ListView):
    model = Property
    paginate_by = 6 
    


class PropertyDetail(DetailView):
    model = Property
    template_name = 'property/property_detail.html'


    