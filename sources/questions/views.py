from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from questions.models import QuestionSet, QuestionType

__author__ = 'djud'


def list_question_set(request):
    context = {
        'list_question_set': QuestionSet.objects.all()
    }
    return render_to_response('questions/list_question_set.html', context,
                              context_instance=RequestContext(request))


def new_question_set(request):
    return render_to_response('questions/edit_qs.html', {},
                              context_instance=RequestContext(request))


def edit_question_set(request):
    qs = QuestionSet.objects.get(id=int(request.REQUEST['qs_id']))
    return render_to_response('questions/edit_qs.html', {'qs': qs},
                              context_instance=RequestContext(request))


def save_question_set(request):
    pk = request.REQUEST.get('pk')
    if not pk:
        qs = QuestionSet()
    else:
        qs = QuestionSet.objects.get(pk=int(pk))
    qs.title = request.REQUEST['title']
    qs.max_time = request.REQUEST['max_time']
    qs.save()
    return redirect(list_question_set)


def new_question(request):
    context = {
        'types': QuestionType.objects.all(),
    }
    return render_to_response('questions/new_question.html', {},
                              context_instance=RequestContext(request))