from django.urls import include, path
from .views import TechnologyView

app_name = "technology"

urlpatterns = [
  path('technology/', TechnologyView.as_view()),
  path('technology/<int:pk>', TechnologyView.as_view())
]
