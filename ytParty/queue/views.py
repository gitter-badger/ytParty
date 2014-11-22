from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render, redirect

from models import Party


def index(request):
    template = loader.get_template('queue/index.html')
    return HttpResponse(template.render(RequestContext(request)))

def player(request, party_token=None):
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

