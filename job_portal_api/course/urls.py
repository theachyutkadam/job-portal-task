from django.urls import path
from .views import CourseList, CourseDetail

app_name = "course"

urlpatterns = [
  path('course/', CourseList.as_view()),
  path('course/<int:pk>', CourseDetail.as_view())
]
