from django.urls import path

from . import views

app_name = 'joke'

urlpatterns = [
    path('joke/', views.JokeViewSet.as_view(), name='joke'),
    path('entertainments/', views.EntertainmentsViewSet.as_view(), name='entertainments'),
    path('dogs_photo/', views.DogsPhotoViewSet.as_view(), name='dogs-photo'),
]
