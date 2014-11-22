from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render, redirect

from models import Party


def _create_and_or_get_user():
    pass

def index_view(request):
    template = loader.get_template('queue/index.html')
    return HttpResponse(template.render(RequestContext(request)))

def player_view(request, party_token=None):
    try:
        party = Party.objects.get(token=party_token)
        context = RequestContext(request, {
            'party': party,
        })
        template = loader.get_template('queue/player.html')
        return HttpResponse(template.render(RequestContext(request)))

    except MultipleObjectsReturned:  # Would be really surprising
        return redirect('index')
    except ObjectDoesNotExist:
        return redirect('index')

