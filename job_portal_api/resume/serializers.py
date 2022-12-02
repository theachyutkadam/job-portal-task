from dataclasses import fields
from .models import Resume
from rest_framework import serializers

class ResumeSerializer(serializers.ModelSerializer):
  # experiances = ExperianceSerializer(many=True)
  class Meta:
    model = Resume
    fields = ('first_name', 'last_name', 'gender', 'contact', 'github_link', 'twitter_link', 'avatar')
