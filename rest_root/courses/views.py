from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from .models import Course
from .serializers import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """
    This view set controls what will be sent to the browser and what authentication is needed.
    This is called from ./urls.py
    """
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
