from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

def index(request):
  """
  Index page
  """
  return render(request, 'index/landing.html', locals())

def view_email(request):
	return render(request, 'email/request.html', locals())