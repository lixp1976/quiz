from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from frontpages.views import index
from questions.forms import QuestionSetForm, QuestionSetFormSet
from questions.models import QuestionSet, QuestionType

__author__ = 'djud'


def new_question_set(request):
    context = {
        'form': QuestionSetForm()
    }
    return render_to_response('questions/edit_qs.html',
                              context,
                              context_instance=RequestContext(request))


def save_question_set(request):
    pk = request.REQUEST.get('pk')
    obj = None
    if pk:
        obj = get_object_or_404(QuestionSet, pk=pk)
    form = QuestionSetForm(request.REQUEST, instance=obj)
    if form.is_valid():
        form.save()
    return redirect(index)


def remove_question_set(request, pk):
    QuestionSet.objects.get(pk=pk).delete()
    return redirect(index)


def edit_question_set(request, pk):
    qs = QuestionSet.objects.get(pk=pk)
    context = {
        'form': QuestionSetForm(instance=qs)
    }
    return render_to_response('questions/edit_qs.html', context,
                              context_instance=RequestContext(request))


def new_question(request):
    context = {
        'types': QuestionType.objects.all(),
    }
    return render_to_response('questions/new_question.html', {},
                              context_instance=RequestContext(request))