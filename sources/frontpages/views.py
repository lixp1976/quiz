from django.shortcuts import render_to_response
from django.template import RequestContext
from questions.forms import QuestionSetFormSet
from questions.models import QuestionSet

__author__ = 'djud'


def index(request):
    context = {
        'formset': QuestionSetFormSet(queryset=QuestionSet.objects.all())
    }
    return render_to_response('frontpages/index.html', context,
                              context_instance=RequestContext(request))