from django.conf import settings
from django.contrib.auth.models import (
  BaseUserManager, AbstractBaseUser
)
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