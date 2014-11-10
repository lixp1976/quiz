from django.conf.urls import patterns, url

__author__ = 'djud'


urlpatterns = patterns('questions.views',
    url('^question_sets/$', 'list_question_set', name='url_list_qs'),
    url('^question_set/new/$', 'new_question_set', name='url_new_qs'),
    #url('^question_set/add/$', 'add_question_set', name='url_add_qs'),
    url('^question_set/save/$', 'save_question_set', name='url_save_qs'),

    url('^question/new/$', 'new_question', name='url_new_question'),
)