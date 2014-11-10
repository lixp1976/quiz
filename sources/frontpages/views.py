from django.shortcuts import render_to_response
from django.template import RequestContext

__author__ = 'djud'


def index(request):
    return render_to_response('frontpages/index.html', {},
                              context_instance=RequestContext(request))