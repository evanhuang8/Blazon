from __future__ import absolute_import

import json
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, JsonResponse, HttpResponseForbidden
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from sponsorship.models import *
from sponsorship.serializers import *

@csrf_exempt
def create(request):
  inkind = request.POST.get('inkind', None)
  try:
    inkind = Inkind.objects.get(id = inkind)
  except ObjectDoesNotExist:
    raise Http404
  prompt = None
  accessToken = request.POST.get('access_token', None)
  try:
    prompt = Prompt.objects.get(campaign = inkind.campaign, access_token = accessToken)
  except ObjectDoesNotExist:
    return HttpResponseForbidden()
  attachment = None
  if request.FILES.has_key('attachment'):
    attachment = request.FILES['attachment']
  donation = Donation(
    prompt = prompt,
    inkind = inkind,
    description = request.POST.get('description', None),
    attachment = attachment
  )
  donation.save()
  return JsonResponse(DonationSerializer(donation).data)

@login_required
def accept(request):
  params = json.loads(request.body)
  donation = params['id']
  try:
    donation = Donation.objects.get(id = donation)
  except ObjectDoesNotExist:
    raise Http404
  if donation.prompt.campaign.created_by.id != request.user.id:
    return HttpResponseForbidden()
  if donation.is_accepted or donation.is_rejected:
    response = {
      'status': 'FAIL',
      'message': 'You cannot perform this operation.'
    }
    return JsonResponse(response)
  donation.is_accepted = True
  donation.accepted_at = timezone.now()
  donation.save()
  response = {
    'status': 'OK'
  }
  return JsonResponse(DonationSerializer(donation).data)

@login_required
def reject(request):
  params = json.loads(request.body)
  donation = params['id']
  try:
    donation = Donation.objects.get(id = donation)
  except ObjectDoesNotExist:
    raise Http404
  if donation.prompt.campaign.created_by.id != request.user.id:
    return HttpResponseForbidden()
  if donation.is_accepted or donation.is_rejected:
    response = {
      'status': 'FAIL',
      'message': 'You cannot perform this operation.'
    }
    return JsonResponse(response)
  donation.is_rejected = True
  donation.rejected_at = timezone.now()
  donation.save()
  response = {
    'status': 'OK'
  }
  return JsonResponse(DonationSerializer(donation).data)