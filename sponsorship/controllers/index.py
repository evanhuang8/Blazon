from __future__ import absolute_import

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

def index(request):
  """
  Index page
  """
  if request.user.is_authenticated():
    return render(request, 'index/dashboard.html', locals())
  return render(request, 'index/landing.html', locals())

def login(request):
	return render(request, 'index/login.html', locals())

def register(request):
  return render(request, 'index/register.html', locals())

def view_email(request):
	return render(request, 'email/request.html', locals())
