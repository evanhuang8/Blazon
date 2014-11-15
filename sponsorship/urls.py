from django.conf.urls import patterns, include, url
from sponsorship.controllers import *

urlpatterns = patterns('',
  url(r'^$', index.index, name = 'index'),
  url(r'^login/$', index.login, name = 'login'),
  url(r'^dashboard/$', index.dashboard, name = 'dashboard'),
  url(r'^email/$', index.view_email, name = 'view_email'),
)