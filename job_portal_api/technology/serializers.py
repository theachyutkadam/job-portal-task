from .models import Technology
from rest_framework import serializers

class TechnologySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Technology
        fields = ('url', 'name', 'description', 'is_active')
