from django.shortcuts import render

# Create your views here.
from datetime import datetime

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from movies.models import Movie, Show, Theatre
from movies.serializers import MovieSerializer, ShowSerializer, TheatreSerializer, ShowTheatreSerializer, \
    ShowMovieSerializer


class ShowView(APIView):

    def get(self, request, *args, **kwargs):
        if kwargs.get("movie_id"):
            movie_id = kwargs["movie_id"]
            shows = Show.objects.filter(start__gt=datetime.now(), movie_id=movie_id).select_related("screen").\
            select_related("screen__theatre")
            serializer = ShowTheatreSerializer(shows, many=True)
        else:
            if kwargs.get("given_date"):
                given_date = kwargs["given_date"]
                shows = Show.objects.filter(start__date=given_date).values_list("movie__id")
            else:
                shows = Show.objects.filter(start__gt=datetime.now()).values_list("movie__id")
            movies = Movie.objects.filter(id__in=shows)
            serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ShowSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

