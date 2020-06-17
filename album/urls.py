from django.urls import path
from . import views
from .views import (
    Photohomeview,
    PhotoDetailView,
    PhotoUpdateView,
    PhotoCreateView,
    PhotoDeleteView)


urlpatterns = [
    path('', Photohomeview.as_view(), name='photohome'),
    path('photo/new', PhotoCreateView.as_view(), name='photo_create'),

    path('photo/<int:pk>/', PhotoDetailView.as_view(), name='photo_detail'),
    path('photo/<int:pk>/update/', PhotoUpdateView.as_view(), name='photo_update'),
    path('photo/<int:pk>/delete/', PhotoDeleteView.as_view(), name='photo_delete'),

] 
