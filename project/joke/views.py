import requests
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

from .models import Joke, Entertainments, DogsPhoto
from .serializers import JokeSerializer, EntertainmentsSerializer, DogsPhotoSerializer
from django.conf import settings


class BaseViewSet(APIView):
    permission_classes = [AllowAny]
    serializer_class = None
    api_url = None

    def post(self, request):
        response = requests.get(self.api_url)
        self.serializer_class.save_response(response.json(), response_data=response.json())
        return Response(response.json(), status=response.status_code)


class JokeViewSet(BaseViewSet):
    serializer_class = JokeSerializer
    api_url = settings.URL_JOKES


class EntertainmentsViewSet(BaseViewSet):
    serializer_class = EntertainmentsSerializer
    api_url = settings.URL_ENTERTAINMENTS


class DogsPhotoViewSet(BaseViewSet):
    serializer_class = DogsPhotoSerializer
    api_url = settings.URL_PHOTO


class RandomPhotoViewSet(APIView):
    serializer_class = DogsPhotoSerializer
    permission_classes = [AllowAny]

    def get(self, request):
        photo = DogsPhoto.objects.all().values()
        return Response(photo)


class RandomEntertainmentsViewSet(APIView):
    serializer_class = EntertainmentsSerializer
    permission_classes = [AllowAny]

    def get(self, request):
        enter = Entertainments.objects.all().values()
        return Response(enter)


class RandomJokeViewSet(APIView):
    serializer_class = JokeSerializer
    permission_classes = [AllowAny]

    def get(self, request):
        joke = Joke.objects.all().values()
        return Response(joke)
