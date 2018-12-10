from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name="detail"),
    url(r'list/add/$', views.ListCreate.as_view(), name='list-add'),
    url(r'list/(?P<pk>[0-9]+)/$', views.ListUpdate.as_view(), name='list-update'),
    url(r'(?P<pk>[0-9]+)/delete/$', views.ListDelete.as_view(), name='list-delete'),
    url(r'^song/add/$', views.SongCreate.as_view(), name='song-add'),
]
