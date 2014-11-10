from django.contrib.auth.views import logout, login
from django.shortcuts import redirect

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