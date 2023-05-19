from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('',PostList.as_view(),name='post_list'),
    path('<slug:slug>',PostDetail.as_view(), name='post_detail'),
]
