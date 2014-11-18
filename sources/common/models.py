__author__ = 'djud'

from django.db.models import signals
from django.contrib.auth import create_superuser, models as auth_models
from config.base import DEBUG


signals.post_syncdb.disconnect(
    create_superuser,
    sender=auth_models,
    dispatch_uid='django.contrib.auth.management.create_superuser')


def create_superuser(app, created_models, verbosity, **kwargs):
    if not DEBUG:
        return
    try:
        auth_models.User.objects.get(username='root')
    except auth_models.User.DoesNotExist:
        print('-' * 80)
        print('Creating root user -- login: root, password: root')
        print('-' * 80)
        auth_models.User.objects.create_superuser('root', 'djudman@ya.ru',
                                                  'root')
    else:
        print('User "root" already exists')


signals.post_syncdb.connect(create_superuser, sender=auth_models,
                            dispatch_uid='common.models.create_superuser')
