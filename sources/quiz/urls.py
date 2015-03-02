from django.conf.urls import patterns, url

__author__ = 'djud'


urlpatterns = patterns('quiz.views',
    url('^quiz/start/(?P<qs_id>\d+)/$', 'start_testing', name='url_start_testing'),
    url('^quiz/skip/$', 'skip_question', name='url_skip_question'),
    url('^quiz/answer/$', 'answer', name='url_answer'),
    url('^quiz/finish/$', 'finish', name='url_finish'),
    url('^question/$', 'show_question', name='url_show_question'),
    url('^question/(?P<question_id>\d+)/$', 'go_to_question',
        name='url_go_question'),
    url('^unanswered/$', 'show_unanswered_questions'),
    url('^summary/(?P<testing_id>\d+)/$', 'show_summary', name='url_summary'),
    url('^history/(?P<question_set_id>\d+)/$', 'get_quiz_history', name='url_history'),
    url('^quiz/(?P<quiz_id>\d+)/log/$', 'get_quiz_log', name='url_quiz_log'),
)