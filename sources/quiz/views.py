import datetime
import time
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from questions.models import QuestionSet, Answer, Question
import random
from quiz.models import QuizQuestion, Quiz, QuizLog
from django.utils import timezone
from frontpages.views import index as index_view

__author__ = 'djud'


def start_testing(request, qs_id):
    if request.session.get('testing_id'):
        return redirect(show_question)
    question_set = QuestionSet.objects.get(id=qs_id)
    quiz = Quiz.objects.create(
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
            testing=quiz,
        )
        if prev:
            p = QuizQuestion.objects.get(id=prev.id)
            p.next = q
            p.save()
        prev = q

    if QuizQuestion.objects.filter(testing=quiz).count() == 0:
        return redirect(index_view)
    quiz.current_question = QuizQuestion\
                                    .objects\
                                    .filter(testing=quiz)\
                                    .order_by('index')[:1].get()
    quiz.save()

    request.session['testing_id'] = quiz.id
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
    ans = Answer.objects.get(id=answer_id) if answer_id else None
    quiz_id = request.session.get('testing_id')
    quiz = Quiz.objects.get(id=quiz_id)
    question = quiz.current_question.question

    log = QuizLog.objects.get(quiz_id=quiz_id, question_id=question.id)
    log.answer = ans
    log.answer_dt = timezone.now()
    log.save()

    is_last = quiz.current_question.is_last
    quiz.current_question.answered = True
    quiz.current_question.save()

    if is_last and quiz.unanswered_questions:
        return redirect(show_unanswered_questions)

    quiz.next_question()
    quiz.save()
    if not quiz.current_question:
        return redirect(finish)
    return redirect(show_question)


def show_question(request):
    quiz_id = request.session['testing_id']
    quiz = Quiz.objects.get(id=quiz_id)
    question = quiz.current_question.question
    if not QuizLog.objects.filter(quiz_id=quiz_id, question_id=question.id):
        QuizLog.objects.create(
            quiz=quiz,
            question=question,
            question_dt=timezone.now(),
            question_set=quiz.question_set,
        )
    context = {
        'testing': quiz,
        'question': question,
        'variants': quiz.current_question.question.answer_set.all(),
        'seconds_left': int(time.mktime(quiz.deadline.timetuple())) -
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
    quiz_id = request.session['testing_id']
    del(request.session['testing_id'])
    del(request.session['total_questions'])
    quiz = Quiz.objects.get(id=quiz_id)
    quiz.finished = timezone.now()
    quiz.save()
    return redirect(show_summary, quiz_id)


def show_summary(request, testing_id):
    testing = Quiz.objects.get(id=testing_id)
    context = {
        'quiz': testing
    }
    return render_to_response('quiz/summary.html', context,
                              context_instance=RequestContext(request))


def get_quiz_history(request, question_set_id):
    quiz_logs = QuizLog.objects.filter(question_set_id=question_set_id)
    quiz_set = Quiz.objects.filter(question_set_id=question_set_id).order_by('-started')
    context = {
        'question_set': QuestionSet.objects.get(id=question_set_id),
        'history': quiz_logs,
        'quiz_set': quiz_set
    }
    return render_to_response('quiz/history.html', context,
                              context_instance=RequestContext(request))


def get_quiz_log(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    quiz_logs = QuizLog.objects.filter(quiz_id=quiz_id)
    context = {
        'quiz_logs': quiz_logs,
        'quiz': quiz
    }
    return render_to_response('quiz/quiz_log.html', context,
                              context_instance=RequestContext(request))
