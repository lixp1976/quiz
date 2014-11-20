__author__ = 'djud'

from config.base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '../db.sqlite3.live'),
    }
}

MEDIA_ROOT = PROJECT_DIR('../static/media/')
STATIC_ROOT = PROJECT_DIR('../static/')

STATICFILES_DIRS = (
    PROJECT_DIR('static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)