from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Property(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Property/')
    price = models.IntegerField(default=0)
    description = models.TextField(max_length=10000) 
    places = models.ForeignKey('Place', related_name='property_place', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', related_name='property_category', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
       
 
class PropertyImages(models.Model):
    property = models.ForeignKey(Property, related_name='property_image', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='propertyimages/')
    def __str__(self):
        return str(self.property)

 
    
        

class Place(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='places/')
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=40)
    
    def __str__(self):
        return self.name
        
        

class PropertyReview(models.Model):
    author = models.ForeignKey(User, related_name='review_author', on_delete=models.CASCADE)
    property = models.ForeignKey(Property, related_name='review_property', on_delete=models.CASCADE)
    rate = models.IntegerField(default=0)
    feedback = models.TextField(max_length=2000)
    