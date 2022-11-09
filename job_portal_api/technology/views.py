from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_list_or_404, get_object_or_404
from faker import Faker

import time
import random

from .models import Technology
from .serializers import TechnologySerializer

class TechnologyView(APIView):
  def get(self, request):
    technologys = Technology.objects.all()
    serializer = TechnologySerializer(technologys, many=True)
    return Response({'technologys': serializer.data})

  def post(self, request):
    technology = request.data.get('technology')
    faker = Faker()
    for n in range(1, 50):
      technology['name'] = faker.name()
      technology['description'] = faker.text()
      technology['is_active'] = random.choice([True, False])

      print("+++++++++++++")
      print(technology)
      print("+++++++++++++")
      serializer = TechnologySerializer(data=technology)
      if serializer.is_valid(raise_exception=True):
        technology_saved = serializer.save()
      # time.sleep(1.5)

    return Response({"success": "Technology '{}' created successfully". format(technology_saved.name)})

  def put(self, request, pk):
    saved_technology = get_object_or_404(Technology.objects.all(), pk=pk)
    data = request.data.get('technlology')
    serializer = TechnologySerializer(isinstance=saved_technology, data=data, partial=True)
    if serializer.is_valid(raise_exception=True):
      technology_saved = serializer.save()
    return Response({"success": "Technology '{}' updated successfully". format(technology_saved.name)})


  def delete(self, request, pk):
    # Get object with this pk
    technology = get_object_or_404(Technology.objects.all(), pk=pk)
    technology.delete()
    return Response({"message": "Technology with id `{}` has been deleted.".format(pk)},status=204)
