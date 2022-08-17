from django.db.models import Q
from rest_framework import serializers
from .models import Movie, Screen, Theatre, Show
from datetime import datetime


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class TheatreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theatre
        fields = '__all__'


class ScreenSerializer(serializers.ModelSerializer):
    theatre = TheatreSerializer()

    class Meta:
        model = Screen
        fields = '__all__'


class ShowSerializer(serializers.ModelSerializer):

    def validate(self, data):
        screen = data["screen"]
        start = data["start"]
        end = data["end"]
        if end <= start:
            raise serializers.ValidationError("Show end time must be after start time")
        start_end = Show.objects.filter(screen=screen).filter(Q(Q(start__gte=start, end__lte=end) |
                                                                Q(end__gte=end, start__lte=end) |
                                                                Q(start__lte=start, end__gte=start))
                                                              ).values('start', 'end')
        if start_end:
            raise serializers.ValidationError("Show timings overlaps with another existing show in this screen")
        # no validation error case
        return data

    def create(self, validated_data):
        return Show.objects.create(**validated_data)

    class Meta:
        model = Show
        fields = "__all__"


class ShowTheatreSerializer(serializers.ModelSerializer):
    screen = ScreenSerializer()

    class Meta:
        model = Show
        fields = "__all__"


class ShowMovieSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()

    class Meta:
        model = Show
        fields = "__all__"

