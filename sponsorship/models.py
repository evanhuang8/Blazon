from django.db import models

class Campaign(models.Model):

  name = models.CharField(max_length = 100)
  description = models.TextField()

class Tier(models.Model):

  name = models.CharField(max_length = 100)
  description = models.TextField()