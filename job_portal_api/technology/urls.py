from django.urls import include, path
from .views import TechnologyList, TechnologyDetail

app_name = "technology"

urlpatterns = [
  path('technology/', TechnologyList.as_view()),
  path('technology/<int:pk>', TechnologyDetail.as_view())
]
