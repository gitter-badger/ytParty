from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^player/$', views.index),
    url(r'^player/(?P<party_token>\w+)/$', views.player, name='player'),
)
