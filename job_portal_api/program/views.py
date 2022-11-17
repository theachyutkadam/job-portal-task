from rest_framework import viewsets
# from rest_framework import permissions
from .serializers import ProgramSerializer
from .models import Program

class ProgramSerializer(viewsets.ModelViewSet):
  queryset = Program.objects.all().order_by('id')
  serializer_class = ProgramSerializer
  # permission_classes = [permissions.IsAuthenticated]
