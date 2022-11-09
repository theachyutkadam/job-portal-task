from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Technology
from .serializers import TechnologySerializer

class TechnologyView(APIView):
    def get(self, request):
        technologys = Technology.objects.all()
        serializer = TechnologySerializer(technologys, many=True)
        return Response({'technologys': serializer.data})
