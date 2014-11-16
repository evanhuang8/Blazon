from django.conf.urls import patterns, include, url
from sponsorship.controllers import *

urlpatterns = patterns('',
  # Front end
  url(r'^$', index.index, name = 'index'),
  url(r'^login/$', index.login, name = 'login'),
  url(r'^register/$', index.register, name = 'register'),
  url(r'^email/$', index.view_email, name = 'view_email'),
  # Back end
  url(r'^user/create/$', user.create, name  = 'user.create'),
  url(r'^user/auth/$', user.auth, name = 'user.auth'),
  url(r'^user/logout/$', user.logout, name = 'user.logout'),
  url(r'^campaigns/$', campaign.CampaignList.as_view()),
  url(r'^campaigns/(?P<pk>[0-9]+)/$', campaign.CampaignDetails.as_view()),
  url(r'^campaigns/send_emails/$', campaign.send_emails, name = 'campaign.send_emails'),
  url(r'^tiers/$', tier.TierList.as_view()),
  url(r'^tiers/(?P<pk>[0-9]+)/$', tier.TierDetails.as_view()),
  url(r'^sponsorships/create/$', sponsorship.create, name = 'sponsorship.create'),
  url(r'^sponsorships/accept/$', sponsorship.accept, name = 'sponsorship.accept'),
  url(r'^sponsorships/reject/$', sponsorship.reject, name = 'sponsorship.reject'),
  url(r'^inkinds/$', inkind.InkindList.as_view()),
  url(r'^inkinds/(?P<pk>[0-9]+)/$', inkind.InkindDetails.as_view()),
  url(r'^donations/create/$', donation.create, name = 'donation.create'),
  url(r'^donations/accept/$', donation.accept, name = 'donation.accept'),
  url(r'^donations/reject/$', donation.reject, name = 'donation.reject'),
)