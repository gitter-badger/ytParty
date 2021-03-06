from django.conf.urls import patterns, url

from . import views
from . import api

urlpatterns = patterns('',
                       url(r'^$', views.index_view, name='index'),
                       url(r'^player/$', views.player_view),
                       url(r'^player/(?P<party_token>\w+)/(?P<video_token>.{11})/$', views.player_view),
                       url(r'^player/(?P<party_token>\w+)/$', views.player_view),
                       url(r'^party/(?P<party_token>\w+)/$', views.party_view, name='party'),
                       url(r'^create_party/$', views.create_party_view, name='party_creation_view'),
                       url(r'^create_party/(?P<party_name>\w+)/$', views.create_party_view, name='party_creation_view'),

                       # api urls

                       url(r'^api/get_queue/(?P<party_token>\w+)/(?P<user_id>\d+)/$', api.get_queue),
                       url(r'^api/add_video/(?P<party_token>\w+)/(?P<video_token>.{11})/(?P<user_id>\d+)/$',
                           api.add_video),
                       url(r'^api/vote_video/(?P<video_id>\d+)/(?P<delta>[\-]?\d+)/(?P<user_id>\d+)$',
                           api.vote_video),
                       url(r'^api/get_next_video/(?P<party_token>\w+)/$', api.get_next_video),
                       url(r'^api/end_video/(?P<video_id>\d+)/$', api.video_end),
                       url(r'^api/get_current/(?P<party_token>\w+)/$', api.get_current_video),
)
