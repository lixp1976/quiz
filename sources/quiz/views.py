import datetime
import time
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from questions.models import QuestionSet, Answer
import random
from quiz.models import QuizQuestion, Quiz, QuizLog
from django.utils import timezone
from frontpages.views import index as index_view

__author__ = 'djud'


def start_testing(request, qs_id):
    if request.session.get('testing_id'):
        return redirect(show_question)
    question_set = QuestionSet.objects.get(id=qs_id)
    testing = Quiz.objects.create(
        user=request.user,
        question_set=question_set,
        deadline=timezone.now() +
                 datetime.timedelta(0, question_set.max_time),
        current_question=None,
    )

    questions = list(question_set.question_set.all())
    random.shuffle(questions)
    next = None
    prev = None
    for index, question in enumerate(questions):
        q = QuizQuestion.objects.create(
            index=index + 1,
            question=question,
            next=next,
            previous=prev,
            testing=testing,
        )
        if prev:
            p = QuizQuestion.objects.get(id=prev.id)
            p.next = q
            p.save()
        prev = q

    if QuizQuestion.objects.filter(testing=testing).count() == 0:
        return redirect(index_view)
    testing.current_question = QuizQuestion\
                                    .objects\
                                    .filter(testing=testing)\
                                    .order_by('index')[:1].get()
    testing.save()

    request.session['testing_id'] = testing.id
    request.session['total_questions'] = len(questions)
    return redirect(show_question)


def skip_question(request):
    testing_id = request.session['testing_id']
    testing = Quiz.objects.get(id=testing_id)
    if testing.current_question.is_last and testing.unanswered_questions:
        return redirect(show_unanswered_questions)

    testing.next_question()
    testing.save()
    if not testing.current_question:
        return redirect(finish)
    return redirect(show_question)


def answer(request):
    answer_id = request.REQUEST.get('answer_id')
    answer = Answer.objects.get(id=answer_id) if answer_id else None
    testing_id = request.session.get('testing_id')
    testing = Quiz.objects.get(id=testing_id)

    QuizLog.objects.create(
        testing=testing,
        question=testing.current_question.question,
        answer=answer,
    )

    is_last = testing.current_question.is_last
    testing.current_question.answered = True
    testing.current_question.save()

    if is_last and testing.unanswered_questions:
        return redirect(show_unanswered_questions)

    testing.next_question()
    testing.save()
    if not testing.current_question:
        return redirect(finish)
    return redirect(show_question)


def show_question(request):
    testing_id = request.session['testing_id']
    testing = Quiz.objects.get(id=testing_id)
    context = {
        'testing': testing,
        'question': testing.current_question.question,
        'variants': testing.current_question.question.answer_set.all(),
        'seconds_left': int(time.mktime(testing.deadline.timetuple())) -
                        int(time.mktime(timezone.now().timetuple()))
    }
    return render_to_response('quiz/question.html', context,
                              context_instance=RequestContext(request))


def show_unanswered_questions(request):
    testing_id = request.session['testing_id']
    testing = Quiz.objects.get(id=testing_id)
    context = {
        'questions': testing.unanswered_questions,
        'seconds_left': int(time.mktime(testing.deadline.timetuple())) -
                        int(time.mktime(timezone.now().timetuple()))
    }
    return render_to_response('quiz/unanswered.html', context,
                              context_instance=RequestContext(request))


def go_to_question(request, question_id):
    testing_id = request.session['testing_id']
    testing = Quiz.objects.get(id=testing_id)
    testing.current_question = QuizQuestion.objects.get(id=question_id)
    testing.save()
    return redirect(show_question)


def finish(request):
    testing_id = request.session['testing_id']
    del(request.session['testing_id'])
    del(request.session['total_questions'])
    testing = Quiz.objects.get(id=testing_id)
    testing.finished = timezone.now()
    return redirect(show_summary, testing_id)


def show_summary(request, testing_id):
    testing = Quiz.objects.get(id=testing_id)
    context = {
        'testing': testing
    }
    return render_to_response('quiz/summary.html', context,
                              context_instance=RequestContext(request))