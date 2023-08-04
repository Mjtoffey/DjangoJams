from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *


class GenreListView(generics.ListCreateAPIView):
    queryset = Genres.objects.all()
    serializer_class = GenreSerializer


class ArtistListView(generics.ListCreateAPIView):
    queryset = Artists.objects.all()
    serializer_class = ArtistSerializer


class AlbumListView(generics.ListCreateAPIView):
    queryset = Albums.objects.all()
    serializer_class = AlbumSerializer


class SongListView(generics.ListCreateAPIView):
    queryset = Songs.objects.all()
    serializer_class = SongSerializer
