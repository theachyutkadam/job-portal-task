from .models import Technology
from rest_framework import serializers
from dataclasses import fields

class TechnologySerializer(serializers.ModelSerializer):
  # id = serializers.IntegerField()
  # name = serializers.CharField()
  # description = serializers.CharField()
  # is_active = serializers.BooleanField()
  class Meta:
    model = Technology
    fields = ('id','url', 'name', 'description', 'is_active')

  def create(self, validated_data):
    return Technology.objects.create(**validated_data)

  def update(self, instance, validated_data):
    instance.name = validated_data.get('name', instance.name)
    instance.description = validated_data.get('description', instance.description)
    instance.is_active = validated_data.get('is_active', instance.is_active)

    instance.save()
    return instance
