# from .models import Technology
from rest_framework import serializers

class TechnologySerializer(serializers.Serializer):
  name = serializers.CharField()
  description = serializers.CharField()
  is_active = serializers.BooleanField()
