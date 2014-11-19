from django.contrib.auth.models import User
from django.contrib.auth.views import logout, login
from django.shortcuts import redirect, render_to_response
from django.template import RequestContext

__author__ = 'djud'

import logging

logger = logging.getLogger('login')


def login_user(request):
    res = login(request, template_name='accounts/login.html')
    if request.user.is_authenticated():
        logger.info('[-> LOGIN] %s' % request.user.username)
    return res


def logout_user(request):
    logger.info('[<- LOGOUT] %s' % request.user.username)
    logout(request)
    return redirect("/")


def list_accounts(request):
    context = {
        'accounts': User.objects.all()
    }
    return render_to_response('accounts/list.html', context,
                              context_instance=RequestContext(request))


def delete_account(request, account_id):
    User.objects.get(id=account_id).delete()
    return redirect(list_accounts)