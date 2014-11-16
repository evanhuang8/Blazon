from __future__ import absolute_import

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from sponsorship.models import *

def index(request):
  """
  Index page
  """
  if request.user.is_authenticated():
    return render(request, 'index/dashboard.html', locals())
  return render(request, 'index/landing.html', locals())

def login(request):
	return render(request, 'index/login.html', locals())

def campaign(request):
	return render(request, 'index/campaign.html', locals())

def register(request):
  return render(request, 'index/register.html', locals())

@login_required
def profile(request):
  return render(request, 'index/profile.html', locals())

@login_required
def create(request, id):
  campaign = get_object_or_404(Campaign, pk = id)
  tiers = Tier.objects.filter(campaign = campaign).order_by('-price')
  inkinds = Inkind.objects.filter(campaign = campaign).order_by('created_at')
  return render(request, 'index/create.html', locals())

def view_email(request):
	return render(request, 'email/request.html', locals())
