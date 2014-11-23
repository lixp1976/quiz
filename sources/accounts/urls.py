from django.conf.urls import patterns, url

__author__ = 'djud'


urlpatterns = patterns('accounts.views',
    url('^login/$', 'login_user', name='url_login'),
    url('^logout/$', 'logout_user', name='url_logout'),

    url('^accounts/$', 'list_accounts', name='url_list_accounts'),
    url('^account/delete/(?P<account_id>\d+)/$', 'delete_account',
        name='url_delete_account'),
    url('^accounts/add/$', 'add_account', name='url_add_account'),
    url('^accounts/(?P<account_id>\d+)/$', 'edit_account',
        name='url_edit_account'),
    url('^accounts/save/(?P<account_id>\d+)/$', 'save_account',
        name='url_save_account'),
    url('^accounts/reset_password/(?P<account_id>\d+)/$', 'reset_password',
        name='url_reset_password'),
)