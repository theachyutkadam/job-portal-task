from rest_framework.views import APIView
from rest_framework import viewsets
from .serializers import TechnologySerializer
from .models import Technology
from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework import generics

from rest_framework import filters

class TechnologySerializer(viewsets.ModelViewSet):
  queryset = Technology.objects.all()
  serializer_class = TechnologySerializer
  filter_backends = [filters.SearchFilter]
  search_fields = ['name', 'description']
# class TechnologyList(APIView):
#   def get(self, request, format=None):
#     technologys = Technology.objects.all()
#     serializer = TechnologySerializer(technologys, many=True)
#     return Response(serializer.data)

#   def post(self, request, format=None):
#     serializer = TechnologySerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#       serializer.save()
#       return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TechnologyDetail(APIView):
  """
  Retrieve, update or delete a technology instance.
  """
  def get_object(self, pk):
    try:
      return Technology.objects.get(pk=pk)
    except Technology.DoesNotExist:
      raise Http404

  def get(self, request, pk, format=None):
    technology = self.get_object(pk)
    # serializer_context = {'request': request}
    serializer = TechnologySerializer(technology)
    return Response(serializer.data)

  def put(self, request, pk, format=None):
    technology = self.get_object(pk)
    serializer = TechnologySerializer(technology, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    technology = self.get_object(pk)
    technology.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
