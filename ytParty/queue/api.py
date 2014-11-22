from django.contrib.sessions import serializers
from django.http import HttpResponse
from django.http.response import Http404
from django.shortcuts import get_object_or_404
from django.core import serializers

import json

from models import Video, Party


def get_queue(request, party_token):
    print party_token
    party = Party.objects.get(token=party_token)
    all_videos = list(Video.objects.filter(party_id=party))
    return HttpResponse(serializers.serialize("json", all_videos), content_type="application/json")


def add_video(request, party_token, video_token, user_id):
    party = Party.objects.get(token=party_token)
    video = Video(party_id=party, token=video_token, user_id_id=user_id)
    video.save()
    return HttpResponse('SUCCESS')


def upvote_video(request, party_token, video_id):
    video = get_object_or_404(Video, pk=video_id)
    if video.status is not 'F':
        video.votes += 1
        video.save()
        return HttpResponse('SUCCESS')

    return HttpResponse('FAILURE')


def video_end(request, video_id):
    video = get_object_or_404(Video, pk=video_id)
    print video.status
    video.status = 'F'
    video.save()
    print video.status

    return HttpResponse('SUCCESS')


def get_next_video(request, party_token):
    party = Party.objects.get(token=party_token)
    videos = Video.objects.filter(party_id=party).exclude(status='F').order_by('-votes')

    try:
        video = videos.get(status='P')
        data = { 'token': video.token, 'id': video.id}
        return HttpResponse(json.dumps(data))
    except Video.DoesNotExist:
        pass

    if videos:
        video = videos[0]
        print video.status
        video.status = 'P'
        video.save()
        print video.status
        data = { 'token': video.token, 'id': video.id}
        return HttpResponse(json.dumps(data))
    else:
        raise Http404
