from django.urls import path, re_path, include
from django.http import HttpResponseRedirect
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from . import views

# the api routes
router = routers.DefaultRouter()
router.register("courses", views.CourseViewSet)


urlpatterns = [
    path("", include(router.urls)),

    # requesting this properly will give an api key back.
    path("token/", obtain_auth_token),

    # redirects to auth/login/ if someone only enters auth/ in the URL
    re_path("^auth/$", lambda request: HttpResponseRedirect("login/")),
    path("auth/", include("rest_framework.urls"))
]
