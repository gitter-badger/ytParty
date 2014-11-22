from django.conf.urls import patterns, url

from . import views
from . import api

urlpatterns = patterns(
    url(r'^$', views.index_view, name='index'),
    url(r'^player/$', views.index_view),
    url(r'^player/(?P<party_token>\d+)/$', views.player_view, name='player'),

    # api urls

    url(r'^api/get_queue/(?P<party_token>\d+)/', api.get_queue),
    url(r'^api/add_video/(?P<party_token>\d+)/(?P<video_token>[a-zA-Z0-9]{11})/(?P<user_id>\d+)/',
        api.add_video),
    url(r'^api/upvote_video/(?P<party_token>\d+)/(?P<video_id>\d+)/',
        api.upvote_video)
)
