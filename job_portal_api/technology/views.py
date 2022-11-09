from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Technology
from .serializers import TechnologySerializer

class TechnologyView(APIView):
  def get(self, request):
    technologys = Technology.objects.all()
    serializer = TechnologySerializer(technologys, many=True)
    return Response({'technologys': serializer.data})

  def post(self, request):
    technology = request.data.get('technology')
    serializer = TechnologySerializer(data=technology)
    if serializer.is_valid(raise_exception=True):
      technology_saved = serializer.save()
    return Response({"success": "Technology '{}' created successfully". format(technology_saved.name)})

  def put(self, request, pk):
    saved_technology = get_object_or_404(Technology.objects.all(), pk=pk)
    data = request.data.get('technlology')
    serializer = TechnologySerializer(isinstance=saved_technology, data=data, partial=True)
    if serializer.is_valid(raise_exception=True):
      technology_saved = serializer.save()
    return Response({"success": "Technology '{}' updated successfully". format(technology_saved.name)})
