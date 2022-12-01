from rest_framework import viewsets
from .serializers import ExperianceSerializer
from .models import Experiance

class ExperianceSerializer(viewsets.ModelViewSet):
  queryset = Experiance.objects.all()
  serializer_class = ExperianceSerializer
