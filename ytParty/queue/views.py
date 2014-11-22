from django.http import HttpResponse
from django.template import RequestContext, loader


def index(request):
    template = loader.get_template('queue/index.html')
    return HttpResponse(template.render(RequestContext(request)))

def player(request):
    template = loader.get_template('queue/player.html')
    return HttpResponse(template.render(RequestContext(request)))
