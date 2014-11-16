from rest_framework import serializers
from sponsorship.models import *

class UserSerializer(serializers.ModelSerializer):

  email = serializers.CharField(source = 'email', read_only = True)

  class Meta:
    model = User
    fields = ('id', 'email', 'first_name', 'last_name', 'organization', 'title', 'address', 'tax_id', 'mission_statement', 'logo', 'signature')

class CampaignSerializer(serializers.ModelSerializer):

  created_at = serializers.DateTimeField(source = 'created_at', read_only = True)
  updated_at = serializers.DateTimeField(source = 'updated_at', read_only = True)

  class Meta:
    model = Campaign

class TierSerializer(serializers.ModelSerializer):

  created_at = serializers.DateTimeField(source = 'created_at', read_only = True)

  class Meta:
    model = Tier

class InkindSerializer(serializers.ModelSerializer):

  created_at = serializers.DateTimeField(source = 'created_at', read_only = True)

  class Meta:
    model = Inkind

class PromptSerializer(serializers.ModelSerializer):

  access_token = serializers.CharField(source = 'access_token', read_only = True)
  created_at = serializers.DateTimeField(source = 'created_at', read_only = True)

  class Meta:
    model = Prompt

class SponsorshipSerializer(serializers.ModelSerializer):

  class Meta:
    model = Sponsorship

class DonationSerializer(serializers.ModelSerializer):

  class Meta:
    model = Donation