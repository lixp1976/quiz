# -*- coding:utf-8 -*-
import random
import string
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.contrib.auth.views import logout, login
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import redirect, render_to_response
from django.template import RequestContext
from accounts.forms import AccountForm
from settings import ADMINS

__author__ = 'djud'

import logging

logger = logging.getLogger('login')


def generate_password(max_length=8):
    new_password = ''
    symbols = list(string.printable[:63])
    for i in range(max_length):
        index = random.randint(0, 62)
        new_password += symbols[index]
    return new_password


def login_user(request):
    res = login(request, template_name='accounts/login.html')
    if request.user.is_authenticated():
        logger.info('[-> LOGIN] %s' % request.user.username)
    return res


def logout_user(request):
    logger.info('[<- LOGOUT] %s' % request.user.username)
    logout(request)
    return redirect("/")


@user_passes_test(lambda x: x.is_superuser)
def list_accounts(request):
    context = {
        'accounts': User.objects.all()
    }
    return render_to_response('accounts/list.html', context,
                              context_instance=RequestContext(request))


@user_passes_test(lambda x: x.is_superuser)
def delete_account(request, account_id):
    User.objects.get(id=account_id).delete()
    return redirect(list_accounts)

def delete_user(request, account_id):
    import os
    User.objects.get(id=account_id).delete()
    return redirect(list_accounts)

@user_passes_test(lambda x: x.is_superuser)
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


@user_passes_test(lambda x: x.is_superuser)
def edit_account(request, account_id):
    context = {
        'account': User.objects.get(id=account_id)
    }
    return render_to_response('accounts/edit.html', context,
                              context_instance=RequestContext(request))


@user_passes_test(lambda x: x.is_superuser)
def save_account(request, account_id):
    account = User.objects.get(id=account_id)
    form = AccountForm(request.POST, instance=account)
    if form.is_valid:
        form.save()
    return redirect(list_accounts)


@user_passes_test(lambda x: x.is_superuser)
def reset_password(request, account_id):
    user = User.objects.get(id=account_id)
    new_password = generate_password()
    user.set_password(new_password)
    user.save()
    logger.warn('Change password. User: %s, new password: %s' % (user.username, new_password))
    to_emails = [x[1] for x in ADMINS]
    #if int(request.GET.get('send_email', 0)) == 1:
    to_emails.append(user.email)
    text = u'''
Пользователь %(user)s сбросил ваш пароль.

http://%(host)s
Ваш логин: %(login)s
Ваш новый пароль: %(passwd)s

Мы сгенерировали для вас хороший пароль, однако, вы можете его поменять. Для этого нужно кликнуть по своему логину в правом верхнем углу и выбрать пункт 'Изменить пароль'.
Если вы меняете пароль, пожалуйста, ставьте более-менее надежный пароль, а не '123qwe'.
    ''' % {'user': request.user.username, 'login': user.username, 'passwd': new_password, 'host': request.META['HTTP_HOST']}
    send_mail(u'Сброс пароля', text, 'road404@ya.ru', to_emails, fail_silently=False)
    return HttpResponse('ok')
