from django import forms 
from .models import *

class PropertyBookForm(forms.ModelForm):
    class Meta:
        model = PropertyBook
        fields = ['date_from','date_to','guest','children']
