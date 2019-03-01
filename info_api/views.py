from .models import Artiste, Course, Notification, Description
from .serializers import ArtisteSerializer, CourseSerializer, NotificationSerializer, DescriptionSerializer
from rest_framework import generics


class ArtisteListCreate(generics.ListAPIView):
  queryset = Artiste.objects.all()
  serializer_class = ArtisteSerializer

class CourseListCreate(generics.ListAPIView):
  queryset = Course.objects.all()
  serializer_class = CourseSerializer

class NotificationListCreate(generics.ListAPIView):
  queryset = Notification.objects.all()
  serializer_class = NotificationSerializer

class DescriptionListCreate(generics.ListAPIView):
  queryset = Description.objects.all()
  serializer_class = DescriptionSerializer

