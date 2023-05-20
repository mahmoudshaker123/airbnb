from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *
from taggit.models import Tag
from django.db.models import Count
from django.db.models import Q


class PostList(ListView):
    model = Post
    paginate_by = 6

class PostDetail(DetailView):
    model = Post
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all().annotate(post_count = Count('post_category'))  
        context["tags"] = Tag.objects.all()
        context['recent_posts'] = Post.objects.all()[:3]
        return context
    


class PostsByCategory(ListView):
    model = Post    
    def get_queryset(self):
        slug = self.kwargs['slug']
        # filter category by slug using Q class 
        object_list = Post.objects.filter(
            Q(category__name__icontains=slug)
        )
        return object_list
    
    
class PostsByTags(ListView):
    model = Post        
    def get_queryset(self):
        slug = self.kwargs['slug']
        # filter tags by slug using Q class 
        object_list = Post.objects.filter(
            Q(tags__name__icontains=slug)
        )
        return object_list