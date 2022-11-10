from .models import Technology
from rest_framework import serializers

class TechnologySerializer(serializers.Serializer):
  id = serializers.IntegerField()
  name = serializers.CharField()
  description = serializers.CharField()
  is_active = serializers.BooleanField()

  def create(self, validated_data):
    return Technology.objects.create(**validated_data)

  def update(self, instance, validated_data):
    instance.name = validated_data.get('name', instance.name)
    instance.description = validated_data.get('description', instance.description)
    instance.is_active = validated_data.get('is_active', instance.is_active)

    instance.save()
    return instance
