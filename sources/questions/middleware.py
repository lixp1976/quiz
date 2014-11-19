from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.utils import timezone
from testing.models import Testing
from testing.views import finish, show_question, answer, skip_question, \
    show_unanswered_questions, go_to_question, show_summary

__author__ = 'djud'


class CheckTimeMiddleware():

    def process_request(self, request):
        testing_id = request.session.get('testing_id')
        if not testing_id:
            return None
        testing = Testing.objects.get(id=testing_id)
        if timezone.now() >= testing.deadline:
            finish(request)
            return redirect(show_summary, testing_id)
        return None


class QuestionRedirectMiddleware():

    def process_request(self, request):
        if request.path in [
            reverse(show_question),
            reverse(finish),
            reverse(answer),
            reverse(skip_question),
            reverse(show_unanswered_questions)
        ]:
            return None
        if request.session.get('testing_id'):
            testing = Testing.objects.get(id=request.session.get(
                'testing_id'))
            if request.path == reverse(go_to_question,
                                       testing.current_question.id):
                return None
            return redirect(show_question)
        return None