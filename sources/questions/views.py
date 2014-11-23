from datetime import datetime
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from frontpages.views import index
from questions.forms import QuestionSetForm, QuestionSetFormSet, QuestionForm, \
    AnswerForm, QuestionFormSet, AnswerFormSet
from questions.models import QuestionSet, Question, Answer

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
        obj = get_object_or_404(QuestionSet, id=pk)
    form = QuestionSetForm(request.REQUEST, instance=obj)
    if form.is_valid():
        form.save()
    return redirect(index)


def remove_question_set(request, pk):
    QuestionSet.objects.get(id=pk).delete()
    return redirect(index)


def edit_question_set(request, pk):
    qs = QuestionSet.objects.get(id=pk)
    context = {
        'form': QuestionSetForm(instance=qs)
    }
    return render_to_response('questions/edit_qs.html', context,
                              context_instance=RequestContext(request))


def list_questions(request, qs_id):
    qs = QuestionSet.objects.get(id=qs_id)
    formset = QuestionFormSet(queryset=qs.question_set.all())
    context = {
        'qs': qs,
        'questions': qs.question_set.all()
    }
    return render_to_response('questions/list_questions.html', context,
                              context_instance=RequestContext(request))


def new_question(request, qs_id):
    qs = QuestionSet.objects.get(id=qs_id)
    question = Question.objects.create(question_set=qs)
    context = {
        'qs': qs,
        'form': QuestionForm(instance=question),
    }
    return render_to_response('questions/edit_question.html', context,
                              context_instance=RequestContext(request))


def edit_question(request, qid):
    question = Question.objects.get(id=qid)
    context = {
        'qs': question.question_set,
        'form': QuestionForm(instance=question),
        'answers': AnswerFormSet(queryset=question.answer_set.all())
    }
    return render_to_response('questions/edit_question.html', context,
                              context_instance=RequestContext(request))


def save_question(request, qid):
    question = Question.objects.get(id=qid)
    question.updated = datetime.now()
    question_form = QuestionForm(request.REQUEST, files=request.FILES,
        instance=question)
    if question_form.is_valid():
        question_form.save()

    answers = AnswerFormSet(data=request.REQUEST)
    for form in answers:
        if form.is_valid():
            form.save()

    return redirect(list_questions,
                    question_form.instance.question_set.id)


def remove_question(request, qid):
    question = Question.objects.get(id=qid)
    qs_id = question.question_set_id
    question.delete()
    return redirect(list_questions, qs_id)


def add_answer(request, qid):
    question = Question.objects.get(id=qid)
    answer = Answer.objects.create(question=question)
    return redirect(edit_question, qid)


def remove_answer(request, id):
    answer = Answer.objects.get(id=id)
    qid = answer.question_id
    answer.delete()
    return redirect(edit_question, qid)
