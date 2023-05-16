from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Property)
admin.site.register(Place)
admin.site.register(PropertyBook)
admin.site.register(PropertyImages)
admin.site.register(PropertyReview)
admin.site.register(Category)