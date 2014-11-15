from django.conf.urls import patterns, include, url
from sponsorship.controllers import *

urlpatterns = patterns('',
  url(r'^$', index.index, name = 'index'),
  url(r'^user/create/$', user.create, name  = 'user.create'),
  url(r'^user/auth/$', user.auth, name = 'user.auth'),
  url(r'^campaigns/$', campaign.CampaignList.as_view()),
  url(r'^campaigns/(?P<pk>[0-9]+)/$', campaign.CampaignDetails.as_view()),
  url(r'^campaigns/send_emails/$', campaign.send_emails, name = 'campaign.send_emails'),
  url(r'^tiers/$', tier.TierList.as_view()),
  url(r'^tiers/(?P<pk>[0-9]+)/$', tier.TierDetails.as_view()),
  url(r'^inkinds/$', inkind.InkindList.as_view()),
  url(r'^inkinds/(?P<pk>[0-9]+)/$', inkind.InkindDetails.as_view()),
)