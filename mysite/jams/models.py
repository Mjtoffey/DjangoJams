from django.db import models


class Songs(models.Model):
    name = models.CharField(max_length=200)
    genre = models.ManyToManyField('Genres', related_name='songs')
    artist = models.ForeignKey('Artists', on_delete=models.SET_NULL, null=True)
    album = models.ForeignKey('Albums', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Artists(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Albums(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey('Artists', on_delete=models.CASCADE)
    genre = models.ForeignKey('Genres', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


class Genres(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
