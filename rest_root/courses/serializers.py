from rest_framework import serializers
from .models import Course


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    """
    THis class is used by the rest_framework package to convert a python object to json/xml and the other way around.
    the inner meta class tells the serializer what model it is serializing and which fields that should be included.
    """
    class Meta:
        model = Course
        fields = ["code", "name", "progression", "plan"]
