from django.db import models
from django.urls import reverse


class List(models.Model):
    list_name = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.list_name


class Song(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    song_name = models.CharField(max_length=100)
    artist_name = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.song_name + ' - ' + self.artist_name





