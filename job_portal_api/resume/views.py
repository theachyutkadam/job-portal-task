from rest_framework import viewsets
from .serializers import ResumeSerializer
from .models import Resume

class ResumeSerializer(viewsets.ModelViewSet):
  queryset = Resume.objects.all()
  serializer_class = ResumeSerializer
