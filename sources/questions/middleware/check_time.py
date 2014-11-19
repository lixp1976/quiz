from django.shortcuts import redirect
from django.utils import timezone
from frontpages.views import index
from testing.models import Testing
from testing.views import finish

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