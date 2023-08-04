from rest_framework import serializers
from .models import *


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artists
        field = '__all__'


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Albums
        field = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        field = '__all__'


class SongSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Songs
        field = '__all__'
