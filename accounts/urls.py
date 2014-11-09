from django.conf.urls import patterns, url

__author__ = 'djud'


urlpatterns = patterns('accounts.views',
    url('^login/$', 'login_user', name='url_login'),
    url('^logout/$', 'logout_user', name='url_logout'),
)