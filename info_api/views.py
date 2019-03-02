from .models import Artiste, Solex, Notification, Description
from .serializers import ArtisteSerializer, SolexSerializer, NotificationSerializer, DescriptionSerializer
from rest_framework import generics

#GET uniquement
class ArtisteListCreate(generics.ListAPIView):
  queryset = Artiste.objects.all()
  serializer_class = ArtisteSerializer

#GET uniquement
class SolexListCreate(generics.ListAPIView):
  queryset = Solex.objects.all()
  serializer_class = SolexSerializer

#GET uniquement
class NotificationListCreate(generics.ListAPIView):
  queryset = Notification.objects.all()
  serializer_class = NotificationSerializer

#GET uniquement
class DescriptionListCreate(generics.ListAPIView):
  queryset = Description.objects.all()
  serializer_class = DescriptionSerializer

