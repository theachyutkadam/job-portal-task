from dataclasses import fields
from .models import Experiance
from rest_framework import serializers

class ExperianceSerializer(serializers.ModelSerializer):
  class Meta:
    model = Experiance
    fields = ('role' ,'company_name' ,'start_date' ,'end_date' ,'resume_id' ,'description' ,'banner')
