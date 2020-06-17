

from django.urls import path
from . import views
from .views import (
    Bloghomeview,
    BlogDetailView,
    BlogUpdateView,
    BlogCreateView,
    BlogDeleteView)


urlpatterns = [
    path('', Bloghomeview.as_view(), name='bloghome'),
    path('blog/new', BlogCreateView.as_view(), name='blog_add'),

    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/<int:pk>/update/', BlogUpdateView.as_view(), name='blog_update'),
    path('blog/<int:pk>/delete/', BlogDeleteView.as_view(), name='blog_delete'),
]
