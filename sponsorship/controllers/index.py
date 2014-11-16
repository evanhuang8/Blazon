from __future__ import absolute_import

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

def index(request):
  """
  Index page
  """
  return render(request, 'index/landing.html', locals())

def login(request):
	return render(request, 'index/login.html', locals())

def campaign(request):
	return render(request, 'index/campaign.html', locals())

def dashboard(request):
	return render(request, 'index/dashboard.html', locals())

def view_email(request):
	return render(request, 'email/request.html', locals())
