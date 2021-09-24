from django.urls import path, re_path, include
from django.http import HttpResponseRedirect
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from . import views


router = routers.DefaultRouter()
router.register("courses", views.CourseViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("token/", obtain_auth_token),
    re_path("^auth/$", lambda request: HttpResponseRedirect("login/")),
    path("auth/", include("rest_framework.urls"))
]
