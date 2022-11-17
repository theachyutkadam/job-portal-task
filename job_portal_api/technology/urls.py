from django.urls import include, path
from .views import TechnologyDetail

urlpatterns = [
  # path('technology/', TechnologyList.as_view()),
  path('technology/<int:pk>', TechnologyDetail.as_view())
]
