from django.contrib.sessions import serializers
from django.http import HttpResponse
from django.http.response import Http404
from django.shortcuts import get_object_or_404
from django.core import serializers

import json

from models import Video, Party, UserVote, User, UserParty


def get_queue(request, party_token, user_id):
    party = Party.objects.get(token=party_token)
    all_videos = Video.objects.filter(party_id=party, status='Q').order_by('-time_added').order_by('-votes')
    counter = 1
    videos = []
    for video in all_videos:
        vid = {
            "id": video.id,
            'votes': video.votes,
            'token': video.token,
            'user_id': video.user_id.id,
            'status': video.status,
            'rank': counter,
            "likes": len(UserVote.objects.filter(user_id=user_id, video_id=video.id)),
        }
        videos.append(vid)
        counter = counter + 1
    return HttpResponse(json.dumps(videos), content_type="application/json")


def add_video(request, party_token, video_token, user_id):
    party = Party.objects.get(token=party_token)
    video = Video(party_id=party, token=video_token, user_id_id=user_id, status='Q')
    video.save()
    return HttpResponse('SUCCESS')


def vote_video(request, video_id, delta, user_id):
    delta = int(delta)
    user_id = int(user_id)
    video_id = int(video_id)
    video = get_object_or_404(Video, pk=video_id)
    if video.status is 'F':
        return HttpResponse('FAILURE')
    if delta not in {1, -1}:
        return HttpResponse('FAILURE')
    old_vote = UserVote.objects.filter(user_id=user_id, video_id=video_id)
    if not old_vote:
        vote = UserVote(user=User.objects.get(pk=user_id), video=Video.objects.get(pk=video_id), delta=delta)
        vote.save()
        video.votes += delta
    elif old_vote.delta == 1:
        if delta == 1:
            return HttpResponse('FAILURE')
        else:
            old_vote.delete()
            video.votes -= 1
    else:
        if delta == -1:
            return HttpResponse('FAILURE')
        else:
            old_vote.delete()
            video.votes += 1
    video.save()
    return HttpResponse('SUCCESS')


def video_end(request, video_id):
    video = get_object_or_404(Video, pk=video_id)
    video.status = 'F'
    video.save()
    return HttpResponse('SUCCESS')


def get_next_video(request, party_token):
    party = Party.objects.get(token=party_token)
    videos = Video.objects.filter(party_id=party).exclude(status='F').order_by('-votes')
    try:
        video = videos.get(status='P')
        data = {'token': video.token, 'id': video.id}
        return HttpResponse(json.dumps(data))
    except Video.DoesNotExist:
        pass
    if videos:
        video = videos[0]
        video.status = 'P'
        video.save()
        data = {'token': video.token, 'id': video.id}
        return HttpResponse(json.dumps(data))
    else:
        raise Http404
