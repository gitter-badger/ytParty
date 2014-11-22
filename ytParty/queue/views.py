from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render, redirect, render_to_response

import string
import random

from models import Party, User, Video

TOKEN_SIZE = 5
COOKIE_LIFETIME = 24 * 60 * 60


def _create_and_or_get_user(request):
    if 'user_id' in request.COOKIES:
        user_id = request.COOKIES['user_id']
        try:
            user = User.objects.get(pk=user_id)
            return (True, user)
        except ObjectDoesNotExist:
            pass

    user = User()
    user.name = "User %d" % User.objects.count()
    user.save()

    return (False, user)


def _create_party(user):
    party = Party()
    party.host_id = user
    party.status = 'P'
    party.token = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(TOKEN_SIZE))
    party.save()
    return party


def index_view(request):
    template = loader.get_template('queue/index.html')
    return HttpResponse(template.render(RequestContext(request)))


def create_party_view(request):
    context = RequestContext(request)

    user_existed, user = _create_and_or_get_user(request)
    party = _create_party(user)

    context_dict = {
        'party_token': party.token,
        'party_count': Party.objects.count(),
    }

    response = render_to_response('queue/host_view.html', context_dict, context)
    if not user_existed:
        response.set_cookie('user_id', user.id, COOKIE_LIFETIME)

    return response


def host_view(request, context, party):
    context_dict = {
        'party_token': party.token,
        'party_count': Party.objects.count()
    }
    response = render_to_response('queue/host_view.html', context_dict, context)
    return response


def party_view(request, party_token=None):
    try:
        party = Party.objects.get(token=party_token)
    except Party.DoesNotExist:
        party = None

    if party is None:
        return index_view(request)

    context = RequestContext(request)
    user_existed, user = _create_and_or_get_user(request)

    if user_existed and user == party.host_id:
        return host_view(request, context, party)

    context_dict = {
        'party_token': party.token,
    }

    response = render_to_response('queue/user_view.html', context_dict, context)
    if not user_existed:
        response.set_cookie('user_id', user.id, COOKIE_LIFETIME)

    return response


def player_view(request, party_token=None, video_token='M7lc1UVf-VE'):
    if party_token is None:
        raise Http404

    context = RequestContext(request)
    template = loader.get_template('queue/player.html')

    party = Party.objects.filter(token=party_token)
    videos = Video.objects.filter(party_id=party).order_by('-votes')
    try:
        video = videos.get(status='R')
    except Video.DoesNotExist:
        video = None

    if video is None and videos.count():
        video = videos[0]
        video.status = 'R'
        video.save()
        context_dict = {
            'video_token': video.token,
        }
    else:
        context_dict = {
            'video_token': video_token,
        }

    response = render_to_response('queue/player.html', context_dict, context)

    return response
