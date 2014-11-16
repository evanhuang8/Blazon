from __future__ import absolute_import

import json
from django.http import HttpResponseForbidden
from rest_framework import mixins
from rest_framework import generics
from sponsorship.models import Campaign, Tier
from sponsorship.serializers import *

class TierList(mixins.ListModelMixin, 
               mixins.CreateModelMixin, 
               generics.GenericAPIView):

  serializer_class = TierSerializer

  def get_queryset(self):
    queryset = Tier.objects.filter(campaign__created_by = self.request.user.id)
    return queryset

  def get(self, request, *args, **kwargs):
    return self.list(request, *args, **kwargs)

  def post(self, request, *args, **kwargs):
    campaign = Campaign.objects.get(id = request.DATA['campaign'])
    if campaign.created_by.id != request.user.id:
      return HttpResponseForbidden()
    return self.create(request, *args, **kwargs)

class TierDetails(mixins.RetrieveModelMixin, 
                  mixins.UpdateModelMixin, 
                  mixins.DestroyModelMixin, 
                  generics.GenericAPIView):
  
  serializer_class = TierSerializer

  def get_queryset(self):
    queryset = Tier.objects.filter(campaign__created_by = self.request.user.id)
    return queryset

  def get(self, request, *args, **kwargs):
    return self.retrieve(request, *args, **kwargs)

  def post(self, request, *args, **kwargs):
    campaign = Campaign.objects.get(id = request.DATA['campaign'])
    if campaign.created_by.id != request.user.id:
      return HttpResponseForbidden()
    return self.update(request, *args, **kwargs)

  def delete(self, request, *args, **kwargs):
    return self.destroy(request, *args, **kwargs)