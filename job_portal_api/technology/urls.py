# from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import include, path
from rest_framework import routers
from . import views
# urlpatterns = [
#     path('technology/', views.TechnologyList.as_view()),
#     path('technology/<int:pk>/', views.TechnologyDetail.as_view()),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)
router = routers.DefaultRouter()
router.register(r'technology', views.TechnologyViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
