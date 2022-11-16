from dataclasses import fields
from rest_framework import serializers
from .models import Program
from course.serializers import CourseSerializer

class ProgramSerializer(serializers.HyperlinkedModelSerializer):
  course = CourseSerializer()  #User the CourseSerializer when you want show object of the course.
  class Meta:
    model = Program
    fields = ('name', 'url', 'description', 'course', 'detail_overview', 'cover_image', 'banner_image', 'is_active',
              'learning_mode', 'start_date', 'end_date', 'training_option', 'type', 'seats', 'feature', 'requirement',
              'eligitbility', 'tools_coverd', 'skill', 'is_free_course', 'meta_keywords', 'meta_description')
