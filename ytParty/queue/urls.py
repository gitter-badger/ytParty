from django.conf.urls import patterns, url

from queue import views

urlpatterns = patterns('',
    url(r'^$', views.index_view, name='index'),
    url(r'^player/$', views.index_view),
    url(r'^player/(?P<party_token>\w+)/$', views.player_view, name='player'),
)
