from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *

class PostList(ListView):
    model = Post
    paginate_by = 6

class PostDetail(DetailView):
    model = Post

    