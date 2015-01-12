from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mango_testing.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'', include('frontpages.urls')),
    url(r'', include('accounts.urls')),
    url(r'', include('questions.urls')),
    url(r'', include('quiz.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
