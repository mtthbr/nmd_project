from .models import Festivalier
from .serializers import FestivalierSerializer
from rest_framework import generics


class FestivalierListCreate(generics.ListCreateAPIView):
  queryset = Festivalier.objects.all()
  serializer_class = FestivalierSerializer

