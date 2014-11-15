from rest_framework import serializers
from sponsorship.models import *

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