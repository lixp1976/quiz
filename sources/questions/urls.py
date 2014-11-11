from django.conf.urls import patterns, url

__author__ = 'djud'


urlpatterns = patterns('questions.views',
    url('^question_set/new/$', 'new_question_set', name='url_new_qs'),
    url('^question_set/save/$', 'save_question_set', name='url_save_qs'),
    url('^question_set/(?P<pk>\d+)/edit/$', 'edit_question_set',
        name='url_edit_qs'),
    url('^question_set/(?P<pk>\d+)/remove/$', 'remove_question_set',
        name='url_remove_qs'),

    url('^question/new/$', 'new_question', name='url_new_question'),
)