from typing import Any, Dict
from django.shortcuts import redirect, render
from django.views.generic import ListView , DetailView , CreateView
from .models import *
from django.views.generic.edit import FormMixin
from .forms import *
from .filters import *
from django_filters.views import FilterView
# Create your views here.

class PropertyList(FilterView):
    model = Property
    paginate_by = 6
    filterset_class = PropertyFilter
    template_name = 'property/property_list.html' 


class PropertyDetail(FormMixin , DetailView):
    model = Property
    template_name = 'property/property_detail.html'
    form_class = PropertyBookForm
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["related"] = Property.objects.filter(category=self.get_object().category)[:3]
        return context
    
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            myform = form.save(commit = False)
            myform.property = self.get_object()
            myform.user = request.user
            myform.save()
            
            return redirect('/')
        else:
            print('not valid')
            

class AddListing(CreateView):
    pass
    

