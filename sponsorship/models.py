from django.conf import settings
from django.db import models

class Campaign(models.Model):

  name = models.CharField(max_length = 100)
  description = models.TextField()
  created_by = models.ForeignKey(settings.AUTH_USER_MODEL)
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)

class Tier(models.Model):

  campaign = models.ForeignKey('Campaign')
  name = models.CharField(max_length = 100)
  description = models.TextField()
  price = models.IntegerField()
  created_at = models.DateTimeField(auto_now_add = True)

class Inkind(models.Model):

  campaign = models.ForeignKey('Campaign')
  name = models.CharField(max_length = 100)
  description = models.TextField()
  created_at = models.DateTimeField(auto_now_add = True)