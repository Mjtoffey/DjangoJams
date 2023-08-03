from django.db import models

class Song(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
class Artist(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=200)
class Album(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=200)
class Genre(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=200)
