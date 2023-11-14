import requests
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Joke, Entertainments
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

