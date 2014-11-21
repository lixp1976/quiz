from django.conf.urls import patterns, url

__author__ = 'djud'


urlpatterns = patterns('accounts.views',
    url('^login/$', 'login_user', name='url_login'),
    url('^logout/$', 'logout_user', name='url_logout'),

    url('^accounts/$', 'list_accounts', name='url_list_accounts'),
    url('^account/delete/(?P<account_id>\d+)/$', 'delete_account',
        name='url_delete_account'),
    url('^accounts/add/$', 'add_account', name='url_add_account'),
)