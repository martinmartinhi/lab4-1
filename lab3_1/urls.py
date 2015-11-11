from django.conf.urls import patterns, include, url
from lab3.views import *

from django.contrib import admin
admin.autodiscover()

from lab3_1 import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lab3_1.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',first),
    url(r'^delete/', delete),
    url(r'^update/', update),
    url(r'^search/', search),
    url(r'^sear/', sear),            
    url(r'^catlog/', catlog),
    url(r'^add/', add),
    url(r'^addbook/', addbook),                
    url(r'^authorad/', authorad),
    url(r'^showall/', showall),
    url(r'^showdata/', showdata),
    url(r'^images/', images),
    (r'^Media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATICFILES_DIRS,'show_indexes': True}),
)
