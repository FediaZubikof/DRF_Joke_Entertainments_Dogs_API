from django.urls import path

from . import views

app_name = 'joke'

urlpatterns = [
    path('joke/', views.JokeViewSet.as_view(), name='joke'),
    path('entertainments/', views.EntertainmentsViewSet.as_view(), name='entertainments'),
    path('dogs_photo/', views.DogsPhotoViewSet.as_view(), name='dogs-photo'),
    path('get_dogs_photo/', views.RandomPhotoViewSet.as_view(), name='get-dogs-photo'),
    path('get_entertainments/', views.RandomEntertainmentsViewSet.as_view(), name='get-entertainments'),
    path('get_joke/', views.RandomJokeViewSet.as_view(), name='get-joke'),
]
