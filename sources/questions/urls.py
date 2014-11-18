from django.conf.urls import patterns, url

__author__ = 'djud'


urlpatterns = patterns('questions.views',
    url('^question_set/new/$', 'new_question_set', name='url_new_qs'),
    url('^question_set/save/$', 'save_question_set', name='url_save_qs'),
    url('^question_set/(?P<pk>\d+)/edit/$', 'edit_question_set',
        name='url_edit_qs'),
    url('^question_set/(?P<pk>\d+)/remove/$', 'remove_question_set',
        name='url_remove_qs'),

    url('^question/list/(?P<qs_id>\d+)/$', 'list_questions',
        name='url_list_question'),


    url('^question/edit/(?P<qid>\d+)/$', 'edit_question',
        name='url_edit_question'),
    url('^question/new/(?P<qs_id>\d+)/$', 'new_question',
        name='url_new_question'),
    url('^question/save/(?P<qid>\d+)/$', 'save_question',
        name='url_save_question'),
    url('^question/remove/(?P<qid>\d+)/$', 'remove_question',
        name='url_remove_question'),


    url('^answer/add/(?P<qid>\d+)/$', 'add_answer', name='url_add_answer'),
    url('^answer/delete/(?P<id>\d+)/$', 'remove_answer',
        name='url_remove_answer'),
)