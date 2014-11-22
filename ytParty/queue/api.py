import json

from . import models
from django.http import HttpResponse
from django.shortcuts import get_object_or_404


def get_queue(request, party_token):
    all_videos = list(models.Video.objects.filter(party_id=party_token))
    return HttpResponse(json.dumps(all_videos), content_type="application/json")


def add_video(request, party_token, video_token, user_id):
    video = models.Video(party_id_id=party_token, token=video_token, user_id_id=user_id)
    video.save()
    return HttpResponse('Success. Video added.')


def upvote_video(request, party_token, video_id):
    video = get_object_or_404(models.Video, pk=video_id)
    print video.__repr__()
    video.votes += 1
    print video.votes
    video.save()
    return HttpResponse('Success. Video upvoated.')
