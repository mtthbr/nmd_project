from rest_framework.serializers import ModelSerializer
from .models import Festivalier

class FestivalierSerializer(ModelSerializer):
  class Meta:
    model = Festivalier
    fields = '__all__'
