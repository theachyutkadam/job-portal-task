from django.urls import path
from .views import CourseList, CourseDetail

urlpatterns = [
  path('course/', CourseList.as_view()),
  path('course/<int:pk>', CourseDetail.as_view())
]
