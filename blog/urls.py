from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('',PostList.as_view(),name='post_list'),
    path('<slug:slug>',PostDetail.as_view(), name='post_detail'),
    path('category/<str:slug>',PostsByCategory.as_view(), name='post_by_category'),
    path('tags/<slug:slug>',PostsByTags.as_view(), name='post_by_tags'),
]
