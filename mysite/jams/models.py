from django.db import models


class Songs(models.Model):
    name = models.CharField(max_length=200)
    genre = models.ManyToManyField('Genres')
    artist = models.ManyToManyField('Artists')
    album = models.ForeignKey(on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Artists(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Albums(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Genres(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
