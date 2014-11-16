from __future__ import absolute_import

import json
import simplify
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, JsonResponse, HttpResponseForbidden
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from sponsorship.models import *
from sponsorship.serializers import *

simplify.public_key = settings.MASTERCARD_PUBLIC
simplify.private_key = settings.MASTERCARD_PRIVATE

@csrf_exempt
def create(request):
  params = json.loads(request.body)
  tier = params['tier']
  try:
    tier = Tier.objects.get(id = tier)
  except ObjectDoesNotExist:
    raise Http404
  prompt = None
  accessToken = params['access_token']
  try:
    prompt = Prompt.objects.get(campaign = tier.campaign, access_token = accessToken)
  except ObjectDoesNotExist:
    return HttpResponseForbidden()
  token = params['token']
  payment = None
  try:
    payment = simplify.Payment.create({
      'amount': tier.price,
      'token': token,
      'description': 'Sponsorship',
      'currency': 'USD'
    })
  except Exception as error:
    response = {
      'status': 'FAIL',
      'message': str(error)
    }
    return JsonResponse(response)
  if not payment:
    response = {
      'status': 'FAIL',
      'message': 'Payment cannot be processed!'
    }
    return JsonResponse(response)
  if payment.paymentStatus != 'APPROVED':
    resposne = {
      'status': 'FAIL',
      'message': 'Payment is declined!'
    }
    return JsonResponse(response)
  checkout = Checkout(
    user = prompt.user,
    amount = tier.price,
    token = token,
    payment = payment.id
  )
  checkout.save()
  sponsorship = Sponsorship(
    prompt = prompt,
    tier = tier,
    checkout = checkout
  )
  sponsorship.save()
  return JsonResponse(SponsorshipSerializer(sponsorship).data)

@login_required
def accept(request):
  params = json.loads(request.body)
  sponsorship = params['id']
  try:
    sponsorship = Sponsorship.objects.get(id = sponsorship)
  except ObjectDoesNotExist:
    raise Http404
  if sponsorship.prompt.campaign.created_by.id != request.user.id:
    return HttpResponseForbidden()
  if sponsorship.is_accepted or sponsorship.is_rejected:
    response = {
      'status': 'FAIL',
      'message': 'You cannot perform this operation.'
    }
    return JsonResponse(response)
  sponsorship.is_accepted = True
  sponsorship.accepted_at = timezone.now()
  sponsorship.save()
  response = {
    'status': 'OK'
  }
  return JsonResponse(SponsorshipSerializer(sponsorship).data)

@login_required
def reject(request):
  params = json.loads(request.body)
  sponsorship = params['id']
  try:
    sponsorship = Sponsorship.objects.get(id = sponsorship)
  except ObjectDoesNotExist:
    raise Http404
  if sponsorship.prompt.campaign.created_by.id != request.user.id:
    return HttpResponseForbidden()
  if sponsorship.is_accepted or sponsorship.is_rejected:
    response = {
      'status': 'FAIL',
      'message': 'You cannot perform this operation.'
    }
    return JsonResponse(response)
  refund = simplify.Refund.create({
    'amount': sponsorship.checkout.amount,
    'payment': sponsorship.checkout.payment,
    'reason': 'Sponsorship declined'
  })
  sponsorship.checkout.refund = refund.id
  sponsorship.checkout.refund_at = timezone.now()
  sponsorship.checkout.save()
  sponsorship.is_rejected = True
  sponsorship.rejected_at = timezone.now()
  sponsorship.save()
  response = {
    'status': 'OK'
  }
  return JsonResponse(SponsorshipSerializer(sponsorship).data)