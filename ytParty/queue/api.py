import json

from . import models
from django.http import HttpResponse


def get_queue(request, party_token):
    all_videos = list(models.Video.objects.filter(party_id=party_token))
    return HttpResponse(json.dumps(all_videos), content_type="application/json")

