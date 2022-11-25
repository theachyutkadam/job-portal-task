"""job_portal_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework import routers
from django.conf.urls.static import static
from program import views as program_view
from technology import views as technology_view
# from authentication.views import login, logout_user

from django.contrib.auth.models import User
from authors.views import UserViewSet, AuthorViewSet, BookViewSet
# from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()
router.register(r'technology', technology_view.TechnologySerializer)
router.register(r'program', program_view.ProgramSerializer)

router.register(r'api/users', UserViewSet, basename='user')
router.register(r'api/authors', AuthorViewSet, basename='author')
router.register(r'api/books', BookViewSet, basename='book')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('authentication/login', login),
    # path('authentication/logout_user', logout_user),
    path('', include(router.urls)),
    path('', include('technology.urls')),
    path('', include('course.urls')),

    path(r'api/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
