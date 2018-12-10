from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import List, Song


class IndexView(generic.ListView):
    template_name = 'music/index.html'

    def get_queryset(self):
        return List.objects.all()


class DetailView(generic.DetailView):
    template_name = 'music/detail.html'
    model = List


class ListCreate(CreateView):
    model = List
    fields = ['list_name']


class ListUpdate(UpdateView):
    model = List
    fields = ['list_name']


class ListDelete(DeleteView):
    model = List
    success_url = reverse_lazy('music:index')


class SongCreate(CreateView):
    model = Song
    fields = ['song_name', 'artist_name']


class SongDelete(DeleteView):
    model = Song
    success_url = reverse_lazy('music:index')