from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TechnologySerializer
from .models import Technology

# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# # Create your views here.
# class TechnologyList(APIView):
#     """
#     List all technologies, or create a new Technology.
#     """
#     def get(self, request, format=None):
#       technologies = Technology.objects.all()
#       serializer = TechnologySerializer(technologies, many=True)
#       return Response(serializer.data)

#     def post(self, request, format=None):
#       technology = TechnologySerializer(data=request.data)
#       if technology.is_valid():
#         technology.save()
#         return Response(technology.data, status=status.HTTP_201_CREATED)
#       return Response(technology.errors, status=status.HTTP_400_BAD_REQUEST)

class TechnologyViewSet(viewsets.ModelViewSet):
  queryset = Technology.objects.all().order_by('name')
  serializer_class = TechnologySerializer
