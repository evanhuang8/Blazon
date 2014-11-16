from __future__ import absolute_import

import json
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, JsonResponse
from rest_framework import mixins
from rest_framework import generics
from sponsorship.models import User, Campaign, Prompt
from sponsorship.serializers import *

class CampaignList(mixins.ListModelMixin, 
                   mixins.CreateModelMixin, 
                   generics.GenericAPIView):

  serializer_class = CampaignSerializer

  def get_queryset(self):
    queryset = Campaign.objects.filter(created_by = self.request.user.id)
    return queryset

  def get(self, request, *args, **kwargs):
    return self.list(request, *args, **kwargs)

  def post(self, request, *args, **kwargs):
    request.DATA['created_by'] = request.user.id
    return self.create(request, *args, **kwargs)

class CampaignDetails(mixins.RetrieveModelMixin, 
                      mixins.UpdateModelMixin, 
                      mixins.DestroyModelMixin, 
                      generics.GenericAPIView):

  serializer_class = CampaignSerializer

  def get_queryset(self):
    queryset = Campaign.objects.filter(created_by = self.request.user.id)
    return queryset

  def get(self, request, *args, **kwargs):
    return self.retrieve(request, *args, **kwargs)

  def post(self, request, *args, **kwargs):
    request.DATA['created_by'] = request.user.id
    return self.update(request, *args, **kwargs)

  def delete(self, request, *args, **kwargs):
    return self.destroy(request, *args, **kwargs)

@login_required
def generate_pdf(request):
  pass

@login_required
def send_emails(request):
  params = json.loads(request.body)
  campaign = params['campaign']
  try:
    campaign = Campaign.objects.get(id = campaign)
  except ObjectDoesNotExist:
    raise Http404
  prompts = []
  for email in params['emails']:
    user, created = User.objects.get_or_create(email = email)
    prompt = Prompt(
      campaign = campaign,
      user = user
    )
    prompt.save()
    prompts.append(prompt)
  # Send emails
  response = [PromptSerializer(prompt).data for prompt in prompts]
  return JsonResponse(response, safe = False)