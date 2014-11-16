import os
import hashlib
from django.conf import settings
from django.contrib.auth.models import (
  BaseUserManager, AbstractBaseUser
)
from django.core.exceptions import ObjectDoesNotExist
from django.db import models

class UserManager(BaseUserManager):

  def create_user(self, email, first_name, last_name, password = None):
    if not email:
      raise ValueError('Email is required!')
    if not first_name:
      raise Valuerror('First name is required!')
    if not last_name:
      raise ValueError('Last name is required!')
    user = self.model(
      email = self.normalize_email(email),
      first_name = first_name,
      last_name = last_name,
    )
    user.set_password(password)
    user.save(using = self._db)
    return user

  def create_superuser(self, email, first_name, last_name, password = None):
    user = self.create_user(email, first_name, last_name, password)
    user.is_admin = True
    user.save(using = self._db)
    return user

class User(AbstractBaseUser):

  email = models.EmailField(max_length = 255, unique = True)
  first_name = models.CharField(max_length = 100)
  last_name = models.CharField(max_length = 100)
  created_at = models.DateTimeField(auto_now_add = True)

  is_admin = models.BooleanField(default = False)

  objects = UserManager()

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['first_name', 'last_name']

  def get_full_name(self):
    return self.first_name + ' ' + self.last_name

  def get_short_name(self):
    return self.first_name

  @property
  def is_staff(self):
    return self.is_admin

class UserAuthBackend(object):

  def authenticate(self, email = None, password = None):
    user = None
    try:
      user = User.objects.get(email = email)
    except ObjectDoesNotExist:
      return None
    if not user.check_password(password):
      return None
    return user

  def get_user(self, pk):
    try:
      return User.objects.get(pk = pk)
    except ObjectDoesNotExist:
      pass
    return None

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
  price = models.IntegerField() # in cents
  created_at = models.DateTimeField(auto_now_add = True)

class Inkind(models.Model):

  campaign = models.ForeignKey('Campaign')
  name = models.CharField(max_length = 100)
  description = models.TextField()
  created_at = models.DateTimeField(auto_now_add = True)

class Prompt(models.Model):

  campaign = models.ForeignKey('campaign')
  user = models.ForeignKey('User')
  access_token = models.CharField(max_length = 128)
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)

  def save(self, *args, **kwargs):
    if self.access_token is None or len(self.access_token) == 0:
      self.access_token = hashlib.sha1(os.urandom(128)).hexdigest()
    super(Prompt, self).save(*args, **kwargs)
    return

class Sponsorship(models.Model):

  prompt = models.ForeignKey('Prompt')
  tier = models.ForeignKey('Tier')
  checkout = models.ForeignKey('Checkout')
  is_accepted = models.BooleanField(default = False)
  accepted_at = models.DateTimeField(null = True, default = None)
  is_rejected = models.BooleanField(default = False)
  rejected_at = models.DateTimeField(null = True, default = None)
  created_at = models.DateTimeField(auto_now_add = True)

class Checkout(models.Model):

  user = models.ForeignKey('User')
  amount = models.IntegerField() # in cents
  token = models.CharField(max_length = 255)
  payment = models.CharField(max_length = 255)
  refund = models.CharField(max_length = 255, null = True, default = None)
  refunded_at = models.DateTimeField(null = True, default = None)

class Donation(models.Model):

  prompt = models.ForeignKey('Prompt')
  inkind = models.ForeignKey('Inkind')
  description = models.TextField()
  attachment = models.FileField(upload_to = 'uploads/%Y-%m-%d/', null = True, default = None)
  is_accepted = models.BooleanField(default = False)
  accepted_at = models.DateTimeField(null = True, default = None)
  is_rejected = models.BooleanField(default = False)
  rejected_at = models.DateTimeField(null = True, default = None)
  created_at = models.DateTimeField(auto_now_add = True)