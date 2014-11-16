from __future__ import absolute_import

from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import render, redirect
from rest_framework import mixins
from rest_framework import generics
from sponsorship.models import User
from sponsorship.serializers import *

def create(request):
  email = request.POST.get('email', None)
  password = request.POST.get('password', None)
  firstName = request.POST.get('first_name', None)
  lastName = request.POST.get('last_name', None)
  user = None
  try:
    user = User.objects.create_user(email, firstName, lastName, password)
  except Exception as error:
    response = {
      'status': 'FAIL',
      'message': str(error)
    }
    return JsonResponse(response)
  user = authenticate(email = email, password = password)
  auth_login(request, user)
  response = {
    'status': 'OK'
  }
  return JsonResponse(response)

def auth(request):
  email = request.REQUEST.get('email', None)
  password = request.REQUEST.get('password', None)
  user = authenticate(email = email, password = password)
  if not user:
    response = {
      'status': 'FAIL',
      'message': 'Invalid email/password combo.'
    }
    return JsonResponse(response)
  auth_login(request, user)
  response = {
    'status': 'OK'
  }
  return JsonResponse(response)

def logout(request):
  auth_logout(request)
  return redirect('sponsorship:index')

class UserDetails(mixins.UpdateModelMixin, generics.GenericAPIView):
  
  serializer_class = UserSerializer

  def get_queryset(self):
    queryset = User.objects.filter(id = self.request.user.id)
    return queryset

  def post(self, request, *args, **kwargs):
    return self.update(request, *args, **kwargs)