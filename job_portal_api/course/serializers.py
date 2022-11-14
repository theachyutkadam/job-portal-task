
from dataclasses import fields
from .models import Course
from rest_framework import serializers

class CourseSerializer(serializers.ModelSerializer):
  class Meta:
    model = Course
    fields = ('id', 'name', 'slug', 'description', 'technology_id', 'icon', 'image', 'meta_keywords', 'meta_description', 'is_active', 'banner')

  # # id =               serializers.IntegerField()
  # name =             serializers.CharField()
  # slug =             serializers.CharField()
  # description =      serializers.CharField()
  # technology_id =    serializers.IntegerField()
  # icon =             serializers.CharField()
  # image =            serializers.ImageField(required=False)
  # meta_keywords =    serializers.CharField()
  # meta_description = serializers.CharField()
  # is_active =        serializers.BooleanField()
  # banner =           serializers.BooleanField()

  def create(self, validated_data):
    return Course.objects.create(**validated_data)

  def update(self, instance, validated_data):
    instance.name = validated_data.get('name', instance.name),
    instance.slug = validated_data.get('slug', instance.slug),
    instance.description = validated_data.get('description', instance.description),
    instance.technology_id = validated_data.get('technology_id', instance.technology_id),
    instance.icon = validated_data.get('icon', instance.icon),
    instance.image = validated_data.get('image', instance.image),
    instance.meta_keywords = validated_data.get('meta_keywords', instance.meta_keywords),
    instance.meta_description = validated_data.get('meta_description', instance.meta_description),
    instance.is_active = validated_data.get('is_active', instance.is_active),
    instance.banner = validated_data.get('banner', instance.banner),
    instance.save()
    return instance
