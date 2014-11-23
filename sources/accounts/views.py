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


def add_account(request):
    username = request.POST['username']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    password = request.POST['password']
    is_superuser = int(request.POST.get('is_superuser', 0)) == 1
    is_active = int(request.POST.get('is_active', 0)) == 1
    if is_superuser:
        new_user = User.objects.create_superuser(username, email, password)
    else:
        new_user = User.objects.create_user(username, email, password)
    new_user.is_active = is_active
    new_user.first_name = first_name
    new_user.last_name = last_name
    new_user.save()
    return redirect(list_accounts)


def edit_account(request, account_id):
    context = {
        'account': User.objects.get(id=account_id)
    }
    return render_to_response('accounts/edit.html', context,
                              context_instance=RequestContext(request))


def save_account(request, account_id):
    return redirect(list_accounts)


def reset_password(request, account_id):
    # может делать только суперпользователь
    return 'ok'