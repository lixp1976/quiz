from django.conf.urls import patterns, url

__author__ = 'djud'


urlpatterns = patterns('testing.views',
    url('^testing/start/(?P<qs_id>\d+)/$', 'start_testing', name='url_start_testing'),
    url('^testing/skip/$', 'skip_question', name='url_skip_question'),
    url('^testing/answer/$', 'answer', name='url_answer'),
    url('^testing/finish/$', 'finish', name='url_finish'),
    url('^question/$', 'show_question'),
    url('^question/(?P<question_id>\d+)/$', 'go_to_question',
        name='url_go_question'),
    url('^unanswered/$', 'show_unanswered_questions'),
)