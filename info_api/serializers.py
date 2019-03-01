from rest_framework.serializers import ModelSerializer
from .models import Artiste, Course, Notification, Description

class ArtisteSerializer(ModelSerializer):
  class Meta:
    model = Artiste
    fields = '__all__'

class CourseSerializer(ModelSerializer):
  class Meta:
    model = Course
    fields = '__all__'

class NotificationSerializer(ModelSerializer):
  class Meta:
    model = Notification
    fields = '__all__'

class DescriptionSerializer(ModelSerializer):
  class Meta:
    model = Description
    fields = '__all__'