from django.conf.urls import patterns, url

from . import views
from . import api

urlpatterns = patterns('',
                       url(r'^$', views.index_view, name='index'),
                       url(r'^player/$', views.index_view),
                       url(r'^player/(?P<party_token>\w+)/$', views.player_view, name='player'),

                       # api urls

                       url(r'^api/get_queue/(?P<party_token>\d+)/', api.get_queue)
)
