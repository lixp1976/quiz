from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.utils import timezone
from frontpages.views import index
from testing.models import Testing
from testing.views import finish, show_question

__author__ = 'djud'


class CheckTimeMiddleware():

    def process_request(self, request):
        testing_id = request.session.get('testing_id')
        if not testing_id:
            return None
        testing = Testing.objects.get(id=testing_id)
        if timezone.now() >= testing.deadline:
            finish(request)
            return redirect(index)
        return None


class QuestionRedirectMiddleware():

    def process_request(self, request):
        if request.path in [reverse(show_question), reverse(finish)]:
            return None
        if request.session.get('testing_id'):
            return redirect(show_question)
        return None