from django.conf.urls import patterns, include, url
from sponsorship.controllers import *

urlpatterns = patterns('',
  url(r'^$', index.index, name = 'index'),
  url(r'^email/$', index.view_email, name = 'view_email'),
)