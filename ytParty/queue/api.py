from django.http import HttpResponse
from django.shortcuts import get_object_or_404

import json

from models import Video


def get_queue(request, party_token):
    all_videos = list(Video.objects.filter(party_id=party_token))
    return HttpResponse(json.dumps(all_videos), content_type="application/json")


def add_video(request, party_token, video_token, user_id):
    video = Video(party_id_id=party_token, token=video_token, user_id_id=user_id)
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
    video.status = 'F'
    video.save()

    return HttpResponse('SUKCES')

def get_next_video(request, party_token):
    videos = Video.objects.filter(party_id=party_token).order_by('-votes')
    try:
        video = videos.get(status='R')
        return video
    except Video.DoesNotExist:
        pass

    if videos:
        video = videos[0]
        video.status = 'R'
        video.save
        return None  # TODO: Should return serialized video
    else:
        raise Http404
