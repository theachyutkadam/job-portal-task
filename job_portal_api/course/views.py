from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from .models import Course
from .serializers import CourseSerializer

class CourseList(APIView):
  def get(self, request, format=None):
    courses = Course.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)

  def post(self, request, format=None):
    serializer = CourseSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    permission_classes = [permissions.IsAuthenticated]

class CourseDetail(APIView):
  """
  Retrieve, update or delete a course instance.
  """
  def get_object(self, pk):
    try:
      return Course.objects.get(pk=pk)
    except Course.DoesNotExist:
      raise Http404

  def get(self, request, pk, format=None):
    course = self.get_object(pk)
    serializer = CourseSerializer(course)
    return Response(serializer.data)

  def put(self, request, pk, format=None):
    course = self.get_object(pk)
    serializer = CourseSerializer(course, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    course = self.get_object(pk)
    course.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
