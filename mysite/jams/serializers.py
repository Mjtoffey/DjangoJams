from rest_framework import serializers
from .models import *


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artists
        fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Albums
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = '__all__'


class SongSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Songs
        fields = '__all__'
