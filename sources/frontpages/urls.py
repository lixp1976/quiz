from django.conf.urls import url, patterns

__author__ = 'djud'

urlpatterns = patterns('frontpages.views',
    url(r'^$', 'index'),
)