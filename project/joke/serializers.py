from rest_framework import serializers
from .models import Joke, Entertainments, DogsPhoto


class ResponseHandling:
    def save_response(self, response_data):
        joke_id = response_data.get("id")
        joke_category = response_data.get("type")
        joke_setup = response_data.get("setup")
        joke_punchline = response_data.get("punchline")

        Joke.objects.create(
            joke_id=joke_id,
            joke_category=joke_category,
            joke_setup=joke_setup,
            joke_punchline=joke_punchline,
        )


class JokeSerializer(serializers.ModelSerializer, ResponseHandling):
    class Meta:
        model = Joke
        fields = '__all__'


class ResponseHandling:
    def save_response(self, response_data):
        activity = response_data.get('activity')
        type = response_data.get('type')
        participants = response_data.get('participants')
        price = response_data.get('price')
        key = response_data.get('key')
        accessibility = response_data.get('accessibility')

        Entertainments.objects.create(
            category=type,
            entertainment=activity,
            participants=participants,
            price=price,
            accessibility=accessibility,
            entertainment_id=key,
        )


class EntertainmentsSerializer(serializers.ModelSerializer, ResponseHandling):
    class Meta:
        model = Entertainments
        fields = ('category',
                  'entertainment',
                  'participants',
                  'price',
                  'accessibility',
                  'entertainment_id',
                  )


class ResponseHandling:
    def save_response(self, response_data):
        link = response_data.get('message')
        status = response_data.get('status')

        DogsPhoto.objects.create(
            link=link,
            status=status,
        )


class DogsPhotoSerializer(serializers.ModelSerializer, ResponseHandling):
    model = DogsPhoto
    fields = ('link',
              'status',
              'start_data',
              )



